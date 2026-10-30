"""Validate catalogue structure, generated files, and local Markdown links."""
import datetime
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from generate_catalog import METHODS, outputs

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {'id', 'name', 'category', 'kind', 'level', 'focus', 'url', 'limitations',
            'original_number', 'checked_on', 'verification', 'reviewed_source_url',
            'license_status', 'setup_effort', 'execution_tested',
            'paper_url', 'code_url', 'docs_url', 'dataset_url', 'quickstart', 'methods'}
OPTIONAL_URLS = ['paper_url', 'code_url', 'docs_url', 'dataset_url']
SKIP_DIRS = {'.git', '.venv', 'site', 'node_modules'}


def is_https(url):
    parts = urlsplit(url)
    return parts.scheme == 'https' and bool(parts.netloc)


def check_resource(r, errors):
    label = r.get('id', '<missing id>')
    if set(r) != REQUIRED:
        errors.append(f'{label}: unexpected or missing fields {sorted(set(r) ^ REQUIRED)}')
        return
    if not re.fullmatch(r'R\d{3}', label):
        errors.append(f'{label}: invalid resource ID')
    if r['level'] not in {'Beginner', 'Intermediate', 'Advanced'}:
        errors.append(f'{label}: invalid audience level')
    if not isinstance(r['execution_tested'], bool):
        errors.append(f'{label}: execution_tested must be boolean')
    for field in ['url', 'reviewed_source_url']:
        if not is_https(r[field]):
            errors.append(f'{label}: invalid HTTPS URL in {field}')
    for field in OPTIONAL_URLS:
        if r[field] is not None and not is_https(r[field]):
            errors.append(f'{label}: {field} must be an HTTPS URL or null')
    if r['paper_url'] and not re.fullmatch(r'https://arxiv\.org/abs/\d{4}\.\d{4,5}', r['paper_url']):
        errors.append(f'{label}: paper_url should be an arXiv abstract URL')
    q = r['quickstart']
    if q is not None and (set(q) != {'language', 'code', 'source'} or not all(q.values())):
        errors.append(f'{label}: quickstart needs non-empty language, code, and source')
    if not isinstance(r['methods'], list) or set(r['methods']) - set(METHODS):
        errors.append(f'{label}: unknown method in {r["methods"]}')
    try:
        datetime.date.fromisoformat(r['checked_on'])
    except ValueError:
        errors.append(f'{label}: invalid review date')
    always_filled = REQUIRED - {'original_number', 'execution_tested', 'quickstart', 'methods', *OPTIONAL_URLS}
    if not all(r[k] for k in always_filled):
        errors.append(f'{label}: empty required metadata')


def markdown_files():
    for path in ROOT.rglob('*.md'):
        if not SKIP_DIRS & set(path.relative_to(ROOT).parts):
            yield path


def main():
    errors = []
    rows = json.loads((ROOT / 'data/resources.json').read_text(encoding='utf-8'))
    ids, names = set(), set()
    for r in rows:
        check_resource(r, errors)
        if r.get('id') in ids or r.get('name', '').casefold() in names:
            errors.append(f"{r.get('id')}: duplicate ID or resource name")
        ids.add(r.get('id'))
        names.add(r.get('name', '').casefold())
    original = sorted(r['original_number'] for r in rows if r.get('original_number') is not None)
    if original != list(range(1, 26)):
        errors.append('Original-list mapping must contain 1–25 exactly once')
    for slug in METHODS:
        if slug != 'frameworks' and not (ROOT / f'docs/methods/{slug}.md').exists():
            errors.append(f'docs/methods/{slug}.md is missing')
    if not errors:
        for path, expected in outputs().items():
            target = ROOT / path
            if not target.exists() or target.read_bytes().decode('utf-8') != expected:
                errors.append(f'{path}: generated content is out of date; run scripts/generate_catalog.py')
    for path in markdown_files():
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)\s]+)\)', text):
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            local = target.split('#', 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f'{path.relative_to(ROOT).as_posix()}: missing link target {local}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(rows)} unique resources; all 25 originals; generated files; local links')


if __name__ == '__main__':
    main()
