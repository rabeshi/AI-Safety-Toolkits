# Sources and data fields

The catalogue links only to primary sources: official repositories, official documentation, project websites,
author papers, and author-published datasets. Descriptions were written for this hub; upstream text and data
are not bundled.

The original 25 resource names match Table 1 of [OpenAgentSafety](https://arxiv.org/abs/2507.06134); see
[the mapping](original-25.md).

## Where the data lives

`data/resources.json` is the single source of truth. Everything else is generated from it by
`python scripts/generate_catalog.py`: the toolkit pages on this site, the method tables, `CATALOG.md`, and
`data/resources.csv`.

## Field reference

| Field | Meaning |
| --- | --- |
| `id` | Stable hub identifier (`R001`…), never renumbered |
| `name` | Human-readable name, keeping important aliases |
| `category` | One primary navigation category |
| `kind` | Benchmark, dataset, framework, toolkit, paper, directory, or similar |
| `level` | Editorial prerequisite estimate: Beginner, Intermediate, or Advanced |
| `focus` | One-sentence summary of what it does |
| `url` | Main official entry point |
| `paper_url` | The paper introducing the resource (arXiv abstract page), or `null` |
| `code_url` | Official code repository, or `null` if none was confirmed |
| `docs_url` | Official documentation site, where one exists |
| `dataset_url` | Official Hugging Face dataset page, where one exists |
| `quickstart` | `{language, code, source}`: commands copied from upstream docs, or `null` |
| `methods` | Evaluation-method slugs (see [methods](../methods/index.md)); drives the method-page tables |
| `limitations` | The caveat most relevant when choosing or interpreting it |
| `original_number` | Position in the original 25-item list, or `null` |
| `checked_on` | Date of primary-source review |
| `verification` | Review status, kept separate from execution testing |
| `reviewed_source_url` | The README, documentation, or paper actually reviewed |
| `license_status` | Reminder to check code and data terms separately |
| `setup_effort` | Editorial estimate, not a measured cost |
| `execution_tested` | Whether this hub ran the resource itself (currently `false` for all) |

## How links were verified (October 2026)

- **Paper links:** all 76 arXiv IDs were checked against the arXiv API so that each title matches the resource.
- **Code links:** each repository was confirmed to exist via the GitHub API; renamed repositories use their new location.
- **Dataset links:** each Hugging Face dataset was confirmed to exist. Config and split names in quickstarts come from the Hugging Face datasets API.
- **Inspect Evals task names** were taken from the Inspect Evals task registry.

The teaching material on this site is a general methodological guide. It isn't a primary experimental result;
cite the upstream projects when you use them.
