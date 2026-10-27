"""Search the local resource catalogue; no network or third-party packages."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', default='', help='Case-insensitive text search')
    parser.add_argument('--level', choices=['Beginner', 'Intermediate', 'Advanced'])
    parser.add_argument('--category', help='Exact category name (case-insensitive)')
    parser.add_argument('--kind', help='Resource-type text filter')
    parser.add_argument('--json', action='store_true', help='Emit JSON instead of text')
    args = parser.parse_args()
    rows = json.loads((ROOT / 'data/resources.json').read_text())
    found = [r for r in rows
             if args.query.casefold() in json.dumps(r, ensure_ascii=False).casefold()
             and (not args.level or r['level'] == args.level)
             and (not args.category or r['category'].casefold() == args.category.casefold())
             and (not args.kind or args.kind.casefold() in r['kind'].casefold())]
    if args.json:
        print(json.dumps(found, indent=2, ensure_ascii=False))
    else:
        print(f'{len(found)} resources')
        for r in found:
            print(f"\n{r['id']} | {r['name']} | {r['level']} | {r['category']}")
            print(r['focus'])
            print(r['url'])


if __name__ == '__main__':
    main()
