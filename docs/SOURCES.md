# Sources and provenance

The catalogue links to primary sources: official repositories, official evaluation documentation, project websites, or papers by the resource authors. Original summaries were drafted for this hub; upstream text and datasets are not bundled.

The user's initial 25 names match the resource labels in Table 1 of [OpenAgentSafety](https://arxiv.org/abs/2507.06134). The table and references were used to resolve abbreviated identities. Scope descriptions were then checked against the individual primary sources; the table's high-level labels should not be treated as an execution or compatibility guarantee.

## Metadata semantics

| Field | Meaning |
| --- | --- |
| `id` | Stable hub identifier, not an upstream benchmark identifier |
| `name` | Human-readable name, preserving an important alias where appropriate |
| `category` | One primary navigation category; resources can address additional risks |
| `kind` | Benchmark, dataset, framework, toolkit, paper, directory, or related role |
| `level` | Editorial prerequisite estimate: Beginner, Intermediate, or Advanced |
| `focus` | Concise editorial summary of the resource's stated purpose |
| `url` | Main official or author-controlled entry point |
| `limitations` | Interpretation or setup caveat relevant to resource selection |
| `original_number` | Number in the user's original 25-item list, or null for additions |
| `checked_on` | Date of actual primary-source review |
| `verification` | Source review status, distinct from execution validation |
| `reviewed_source_url` | Actual documentation, README, or paper used in source review |
| `license_status` | Reminder to inspect upstream code and data terms separately |
| `setup_effort` | Editorial estimate, not measured hardware or monetary cost |
| `execution_tested` | Whether execution was validated for this catalogue entry |

Initial review date: October 27, 2026. All entries in this release have `execution_tested: false`. Source availability and matching descriptions were checked; external installations and benchmark runs were not attempted.

The teaching material in `docs/` expresses general methodological recommendations. It should not be cited as a primary experimental result. Use each upstream project's own citation when reporting research based on it.
