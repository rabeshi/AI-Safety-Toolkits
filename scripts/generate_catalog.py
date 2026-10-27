"""Generate CATALOG.md, the original-list mapping, and CSV from canonical JSON."""
import collections
import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slug(value):
    return re.sub(r'[^a-z0-9 -]', '', value.lower()).replace(' ', '-')


def outputs():
    rows = json.loads((ROOT / 'data/resources.json').read_text())
    groups = collections.defaultdict(list)
    for row in rows:
        groups[row['category']].append(row)
    lines = ['# Resource catalogue', '',
             f'**{len(rows)} resources across {len(groups)} categories.** '
             'Primary-source review: October 27, 2026. External execution has not been tested.', '',
             'Use [the selection guide](docs/SELECTION_GUIDE.md) to choose a shortlist. '
             'Levels and effort estimates are editorial; a paper or directory is not an executable toolkit. '
             'Primary-source links support each description; review upstream code and data terms separately.', '',
             '## Categories', '']
    for category, entries in groups.items():
        lines.append(f'- [{category}](#{slug(category)}) ({len(entries)})')
    for category, entries in groups.items():
        lines += ['', f'## {category}', '',
                  '| ID | Resource and primary source | Type | Level | Focus |',
                  '| --- | --- | --- | --- | --- |']
        for r in entries:
            lines.append(f"| [{r['id']}](#{r['id'].lower()}) | [{r['name']}]({r['url']}) | "
                         f"{r['kind']} | {r['level']} | {r['focus']} |")
        lines += ['', '### Selection notes', '']
        for r in entries:
            lines += [f"<a id=\"{r['id'].lower()}\"></a>", '', f"**{r['id']} · {r['name']}**", '',
                      f"- **Interpretation:** {r['limitations']}",
                      f"- **Setup effort:** {r['setup_effort']}.",
                      f"- **Verification:** {r['verification']} ({r['checked_on']}). "
                      f"[Reviewed primary source]({r['reviewed_source_url']}).", '']
    mapping = ['# Mapping the original 25 resources', '',
               'All original entries are retained. Several labels were shortened paper titles. '
               'The correspondence was established from Table 1 and the references of '
               '[OpenAgentSafety](https://arxiv.org/abs/2507.06134), then checked against individual sources.', '',
               '| Original number | Identified resource and source | Type | Clarification |',
               '| --- | --- | --- | --- |']
    for r in sorted([r for r in rows if r['original_number']], key=lambda r: r['original_number']):
        mapping.append(f"| {r['original_number']} | [{r['name']}]({r['url']}) | {r['kind']} | {r['limitations']} |")
    mapping += ['', 'In particular, SG-Bench evaluates LLM safety generalization across tasks and prompt types. '
                'SafeBench here refers to the multimodal project, not an autonomous-driving benchmark. '
                'The “Frontier Models” entry is the in-context scheming paper, '
                'and “Infrastructure for AI” is a conceptual infrastructure paper.']
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return {'CATALOG.md': '\n'.join(lines).rstrip() + '\n',
            'docs/ORIGINAL_25.md': '\n'.join(mapping).rstrip() + '\n',
            'data/resources.csv': buffer.getvalue()}


if __name__ == '__main__':
    for path, text in outputs().items():
        (ROOT / path).write_text(text)
    print('Regenerated CATALOG.md, docs/ORIGINAL_25.md, and data/resources.csv')
