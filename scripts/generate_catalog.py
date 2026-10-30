"""Generate the catalogue pages, method tables, and CSV export from data/resources.json.

Run after editing the JSON:  python scripts/generate_catalog.py
"""
import collections
import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW_NOTE = ('Links were checked against primary sources on {date}. '
               'Quickstart commands are copied from each project\'s own documentation; '
               'this hub has not run them. Check upstream licences before using code or data.')

# Method slugs used in data/resources.json -> page title in docs/methods/.
METHODS = {
    'qa-benchmarks': 'Question-and-answer benchmarks',
    'harmful-requests': 'Harmful requests and over-refusal',
    'red-teaming': 'Red teaming and jailbreaks',
    'prompt-injection': 'Prompt injection',
    'agent-safety': 'Agent and tool-use safety',
    'dangerous-capabilities': 'Dangerous capability evaluations',
    'alignment-propensity': 'Alignment and propensity evaluations',
    'ai-control': 'AI control evaluations',
    'interpretability': 'Interpretability-based evaluation',
    'scoring': 'Scoring: rules, classifiers, judges, and humans',
    'bias-toxicity': 'Bias and toxicity',
    'factuality': 'Factuality and hallucination',
    'privacy': 'Privacy',
    'multimodal': 'Multimodal and embodied safety',
    'holistic': 'Holistic suites and regulation-aligned evaluation',
    'frameworks': 'Evaluation frameworks',
}
METHOD_PAGE = {slug: f'../methods/{slug}.md' for slug in METHODS}
METHOD_PAGE['frameworks'] = '../tutorials/02-first-inspect-eval.md'
LEVEL_ICON = {'Beginner': '🟢', 'Intermediate': '🟡', 'Advanced': '🔴'}
BEGIN = re.compile(r'(<!-- BEGIN toolkits:([a-z-]+) -->\n)(.*?)(<!-- END toolkits -->)', re.S)


def slug(value):
    return re.sub(r'[^a-z0-9 -]', '', value.lower()).replace(' ', '-')


def load():
    return json.loads((ROOT / 'data/resources.json').read_text(encoding='utf-8'))


def links(r, sep=' · '):
    parts = [f'[{label}]({r[key]})' for key, label in
             [('paper_url', 'Paper'), ('code_url', 'Code'), ('docs_url', 'Docs'), ('dataset_url', 'Data')] if r[key]]
    if not r['paper_url'] and not r['code_url'] and not r['docs_url']:
        parts.insert(0, f"[Website]({r['url']})")
    return sep.join(parts)


def card_anchor(r):
    return f"{slug(r['category'])}.md#{r['id'].lower()}"


def card(r):
    level = f"{LEVEL_ICON[r['level']]} {r['level']}"
    methods = ', '.join(f"[{METHODS[m]}]({METHOD_PAGE[m]})" for m in r['methods']) or '—'
    lines = [f"### {r['name']} {{ #{r['id'].lower()} }}", '',
             f"**{r['kind']}** · {level} · `{r['id']}`", '',
             r['focus'], '',
             f"**Links:** {links(r)}", '',
             f"**Evaluation methods:** {methods}", '']
    if r['quickstart']:
        q = r['quickstart']
        lines += [f'??? example "Quickstart ({q["source"]})"', '',
                  f"    ```{q['language']}"]
        lines += [f'    {line}' if line else '' for line in q['code'].splitlines()]
        lines += ['    ```', '']
    lines += ['!!! warning "Keep in mind"', f"    {r['limitations']}", '',
              f"<small>Setup effort: {r['setup_effort']}. {r['verification']} ({r['checked_on']}).</small>", '', '---', '']
    return lines


def method_table(rows, method):
    picked = sorted((r for r in rows if method in r['methods']),
                    key=lambda r: (['Beginner', 'Intermediate', 'Advanced'].index(r['level']), r['name'].casefold()))
    lines = ['| Resource | What it does | Level | Links |', '| --- | --- | --- | --- |']
    for r in picked:
        lines.append(f"| [{r['name']}](../toolkits/{card_anchor(r)}) | {r['focus']} | "
                     f"{LEVEL_ICON[r['level']]} {r['level']} | {links(r)} |")
    return '\n'.join(lines) + '\n'


def outputs():
    rows = load()
    date = max(r['checked_on'] for r in rows)
    groups = collections.defaultdict(list)
    for row in rows:
        groups[row['category']].append(row)
    files = {}

    # Root CATALOG.md: a single page that reads well on GitHub.
    lines = ['# Resource catalogue', '',
             f'**{len(rows)} resources across {len(groups)} categories.** '
             'The same catalogue, with quickstarts and method guides, is on the documentation website '
             '(see the README).', '', REVIEW_NOTE.format(date=date), '',
             'Levels: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced (editorial estimates of prerequisites).', '']
    for category, entries in groups.items():
        lines.append(f'- [{category}](#{slug(category)}) ({len(entries)})')
    for category, entries in groups.items():
        lines += ['', f'## {category}', '',
                  '| ID | Resource | Type | Level | What it does | Links |',
                  '| --- | --- | --- | --- | --- | --- |']
        for r in entries:
            lines.append(f"| {r['id']} | **{r['name']}** | {r['kind']} | {LEVEL_ICON[r['level']]} {r['level']} | "
                         f"{r['focus']} {r['limitations']} | {links(r, '<br>')} |")
    files['CATALOG.md'] = '\n'.join(lines).rstrip() + '\n'

    # Website: one page per category plus a filterable index.
    index = ['# Toolkit catalogue', '',
             f'**{len(rows)} benchmarks, datasets, frameworks, red-teaming tools, and papers**, '
             'each with links to the paper, code, documentation, and data where they exist.', '',
             '!!! tip "New here?"',
             '    Filter by **Beginner** and start with the resources that have a quickstart. '
             'If you are unsure what you need, read [How evaluation works](../getting-started/index.md) '
             'and [Choosing a resource](../guides/choosing.md) first.', '',
             f'<small>{REVIEW_NOTE.format(date=date)}</small>', '',
             '## Browse by category', '',
             '| Category | Resources |', '| --- | --- |']
    for category, entries in groups.items():
        index.append(f'| [{category}]({slug(category)}.md) | {len(entries)} |')
    index += ['', '## All resources', '',
              '<input id="toolkit-filter" class="toolkit-filter" type="search" '
              'placeholder="Filter by name, level, method, or keyword (e.g. beginner, injection, agent)">', '',
              '| Resource | Category | Type | Level | Quickstart | Links |',
              '| --- | --- | --- | --- | --- | --- |']
    for r in sorted(rows, key=lambda r: r['name'].casefold()):
        index.append(f"| [{r['name']}]({card_anchor(r)}) | {r['category']} | {r['kind']} | "
                     f"{LEVEL_ICON[r['level']]} {r['level']} | {'✅' if r['quickstart'] else ''} | {links(r)} |")
    files['docs/toolkits/index.md'] = '\n'.join(index) + '\n'
    for category, entries in groups.items():
        page = [f'# {category}', '', f'{len(entries)} resources. '
                'Open **Quickstart** boxes for copy-paste commands from the upstream project.', '']
        for r in entries:
            page += card(r)
        files[f'docs/toolkits/{slug(category)}.md'] = '\n'.join(page).rstrip('-\n') + '\n'

    mapping = ['# Mapping the original 25 resources', '',
               'This hub began as a list of 25 resource names. Several were shortened paper titles. '
               'They were resolved using Table 1 and the references of '
               '[OpenAgentSafety](https://arxiv.org/abs/2507.06134), then checked against each primary source.', '',
               '| # | Identified resource | Type | Links | Clarification |',
               '| --- | --- | --- | --- | --- |']
    for r in sorted([r for r in rows if r['original_number']], key=lambda r: r['original_number']):
        mapping.append(f"| {r['original_number']} | [{r['name']}](../toolkits/{card_anchor(r)}) | {r['kind']} | "
                       f"{links(r)} | {r['limitations']} |")
    mapping += ['', 'SG-Bench evaluates LLM safety generalization across tasks and prompt types. '
                'SafeBench here is the multimodal project, not an autonomous-driving benchmark. '
                'The “Frontier Models” entry is the in-context scheming paper, '
                'and “Infrastructure for AI” is a conceptual infrastructure paper.']
    files['docs/about/original-25.md'] = '\n'.join(mapping).rstrip() + '\n'

    # Fill the generated toolkit tables inside hand-written method pages.
    for page in sorted((ROOT / 'docs/methods').glob('*.md')):
        text = page.read_text(encoding='utf-8')
        new = BEGIN.sub(lambda m: m.group(1) + method_table(rows, m.group(2)) + m.group(4), text)
        files[page.relative_to(ROOT).as_posix()] = new

    flat = []
    for r in rows:
        r = dict(r, methods=';'.join(r['methods']),
                 quickstart=r['quickstart']['code'] if r['quickstart'] else '')
        flat.append(r)
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=list(flat[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(flat)
    files['data/resources.csv'] = buffer.getvalue()
    return files


if __name__ == '__main__':
    for path, text in outputs().items():
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8', newline='')
    print('Regenerated CATALOG.md, docs/toolkits/, docs/about/original-25.md, method tables, and data/resources.csv')
