"""Validate catalogue structure, generated exports, and local Markdown targets."""
import datetime
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from generate_catalog import outputs

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    rows = json.loads((ROOT / 'data/resources.json').read_text())
    required = {'id', 'name', 'category', 'kind', 'level', 'focus', 'url', 'limitations',
                'original_number', 'checked_on', 'verification', 'reviewed_source_url',
                'license_status', 'setup_effort', 'execution_tested'}
    ids, names = set(), set()
    for r in rows:
        label = r.get('id', '<missing id>')
        if set(r) != required:
            errors.append(f'{label}: unexpected or missing fields')
        if label in ids or r['name'].casefold() in names:
            errors.append(f'{label}: duplicate ID or resource name')
        ids.add(label)
        names.add(r['name'].casefold())
        if not re.fullmatch(r'R\d{3}', label):
            errors.append(f'{label}: invalid resource ID')
        if r['level'] not in {'Beginner', 'Intermediate', 'Advanced'}:
            errors.append(f'{label}: invalid audience level')
        if not isinstance(r['execution_tested'], bool):
            errors.append(f'{label}: execution_tested must be boolean')
        for field in ['url', 'reviewed_source_url']:
            if urlsplit(r[field]).scheme != 'https' or not urlsplit(r[field]).netloc:
                errors.append(f'{label}: invalid HTTPS URL in {field}')
        try:
            datetime.date.fromisoformat(r['checked_on'])
        except ValueError:
            errors.append(f'{label}: invalid review date')
        if not all(r[k] for k in required - {'original_number', 'execution_tested'}):
            errors.append(f'{label}: empty required metadata')
    original = sorted(r['original_number'] for r in rows if r['original_number'] is not None)
    if original != list(range(1, 26)):
        errors.append('Original-list mapping must contain 1–25 exactly once')
    for path, expected in outputs().items():
        with (ROOT / path).open(newline='') as f:
            if f.read() != expected:
                errors.append(f'{path}: generated content differs; run scripts/generate_catalog.py')
    for path in ROOT.rglob('*.md'):
        text = path.read_text()
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            local = target.split('#', 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f'{path.relative_to(ROOT)}: missing link target {local}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(rows)} unique resources; all 25 originals; generated exports; local links')


if __name__ == '__main__':
    main()
