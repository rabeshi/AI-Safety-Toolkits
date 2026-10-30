"""Optional HTTP reachability observations; this does not verify scientific claims."""
import argparse
import concurrent.futures
import datetime
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def check(url):
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'AI-Safety-Toolkit-Hub-link-check/1.0'})
        with urllib.request.urlopen(request, timeout=20) as response:
            response.read(1024)
            return {'url': url, 'status': response.status, 'resolved_url': response.url}
    except Exception as exc:
        return {'url': url, 'status': 'needs_review', 'detail': str(exc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('link-report.json'))
    args = parser.parse_args()
    rows = json.loads((ROOT / 'data/resources.json').read_text(encoding='utf-8'))
    fields = ['url', 'paper_url', 'code_url', 'docs_url', 'dataset_url']
    urls = sorted({r[f] for r in rows for f in fields if r[f]})
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        observations = list(pool.map(check, urls))
    result = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'meaning': 'HTTP reachability only; errors can reflect rate limits or access restrictions.',
              'observations': observations}
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    review = sum(r['status'] != 200 for r in observations)
    print(f'{len(urls)} links checked; {review} need review. Report: {args.output}')


if __name__ == '__main__':
    main()
