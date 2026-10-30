"""Search the local resource catalogue; no network or third-party packages.

Examples:
    python scripts/catalog.py --level Beginner
    python scripts/catalog.py --method prompt-injection
    python scripts/catalog.py --query jailbreak --has-quickstart
"""
import argparse
import json
from pathlib import Path

from generate_catalog import METHODS

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--query', default='', help='Case-insensitive text search')
    parser.add_argument('--level', choices=['Beginner', 'Intermediate', 'Advanced'])
    parser.add_argument('--category', help='Exact category name (case-insensitive)')
    parser.add_argument('--kind', help='Resource-type text filter')
    parser.add_argument('--method', choices=sorted(METHODS), help='Evaluation method')
    parser.add_argument('--has-quickstart', action='store_true', help='Only resources with a quickstart')
    parser.add_argument('--json', action='store_true', help='Emit JSON instead of text')
    args = parser.parse_args()
    rows = json.loads((ROOT / 'data/resources.json').read_text(encoding='utf-8'))
    found = [r for r in rows
             if args.query.casefold() in json.dumps(r, ensure_ascii=False).casefold()
             and (not args.level or r['level'] == args.level)
             and (not args.category or r['category'].casefold() == args.category.casefold())
             and (not args.kind or args.kind.casefold() in r['kind'].casefold())
             and (not args.method or args.method in r['methods'])
             and (not args.has_quickstart or r['quickstart'])]
    if args.json:
        print(json.dumps(found, indent=2, ensure_ascii=False))
        return
    print(f'{len(found)} resources')
    for r in found:
        print(f"\n{r['id']} | {r['name']} | {r['level']} | {r['category']}")
        print(r['focus'])
        for key in ['paper_url', 'code_url', 'docs_url', 'dataset_url']:
            if r[key]:
                print(f"  {key.removesuffix('_url'):<8}{r[key]}")
        if not r['paper_url'] and not r['code_url']:
            print(f"  {'website':<8}{r['url']}")
        if r['quickstart']:
            print('  quickstart:\n    ' + r['quickstart']['code'].replace('\n', '\n    '))


if __name__ == '__main__':
    main()
