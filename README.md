# AI Safety Toolkit Hub

**A practical guide to 82 AI safety benchmarks, datasets, evaluation frameworks, red-teaming tools, and research resources.**

## Preamble: why this repository exists

AI safety evaluation can be difficult to enter. One project provides prompts, another runs tool-using agents, and another supplies a judge that decides whether a response was harmful. They may all be called “benchmarks,” although they answer different questions and require different skills.

This repository helps you understand those differences, choose an appropriate resource, and turn an evaluation into evidence you can explain. It starts with plain-language concepts and small exercises, then progresses to reproducible experiments, adversarial testing, agent environments, and professional reporting.

The aim is to make the field easier to navigate without hiding its limitations. A high benchmark score is evidence about a particular test under particular conditions. It does not establish that a model or application is safe in every setting.

**Who it is for:** students and newcomers; researchers developing benchmarks; engineers evaluating applications; and experienced evaluators comparing methods or designing assessment campaigns.

This is a curated learning and research hub. Each upstream project keeps its own implementation, requirements, terms, and scientific claims. The hub does not install or run all resources through a shared interface.

## Choose your starting point

| Your goal | Start here | What you will produce |
| --- | --- | --- |
| Understand the field | [Start here](docs/START_HERE.md) | A clear distinction between a benchmark, dataset, framework, and evaluator |
| Learn through practice | [Beginner learning path](docs/LEARNING_PATHS.md) | A small annotated evaluation and a report |
| Find a resource | [Full catalogue](CATALOG.md) | A shortlist matched to your research question |
| Design a rigorous study | [Evaluation methodology](docs/METHODOLOGY.md) | A reproducible evaluation plan |
| Interpret scores | [Metrics and reporting](docs/METRICS.md) | Separate measures of harmful compliance, over-refusal, utility, and uncertainty |
| Follow the original 25 items | [Original-list mapping](docs/ORIGINAL_25.md) | Correct project identities and direct source links |
| Add or update resources | [Contributing](CONTRIBUTING.md) | A source-backed catalogue entry |

## A manageable first shortlist

| Resource | Why start with it? |
| --- | --- |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | Learn the anatomy of an evaluation: dataset, task, solver, scorer, and logs. |
| [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) | Study existing implementations instead of building every component from scratch. |
| [XSTest](https://github.com/paul-rottger/xstest) | Understand why refusing a harmless request can also be an evaluation failure. |
| [Do-Not-Answer](https://github.com/Libr-AI/do-not-answer) | Examine how a dataset defines requests a model should decline. |
| [HarmBench](https://github.com/centerforaisafety/HarmBench) | Learn structured harmful-request evaluation and its threat-model assumptions. |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Progress to tool use, untrusted content, and prompt injection. |
| [AgentHarm](https://ukgovernmentbeis.github.io/inspect_evals/evals/agentharm/) | Compare harmful and benign multi-step agent tasks. |

These are editorial learning recommendations, not a ranking of scientific quality or completeness. Read each upstream project's requirements before installing it.

## What is included?

- **82 distinct resources**, including all 25 items from the original list, with corrected identities where necessary.
- Categorized descriptions, audience levels, limitations, direct primary-source links, and source-review dates.
- Beginner, practitioner, and research learning paths; a glossary; selection guidance; and metric definitions.
- A zero-dependency offline teaching exercise and an optional Inspect AI starter task.
- Evaluation-plan, results-report, and resource-entry templates.
- JSON and CSV exports, catalogue search, validation, optional link checking, and a GitHub Actions validation workflow.

The catalogue includes adjacent resources on fairness, factuality, training data, and agent capability. These are labeled explicitly because they answer supporting questions rather than providing complete safety assessments.

## Try it locally

Python 3.10 or later is enough for the catalogue utilities and offline exercise. Run from the repository root:

```bash
python scripts/catalog.py --level Beginner
python scripts/catalog.py --query privacy
python scripts/catalog.py --category "Prompt injection"
python examples/offline_refusal_demo.py
python scripts/validate.py
```

The offline exercise uses fixed illustrative outputs. It does not query a model or produce benchmark results. For an optional real model call, follow [the Inspect starter guide](examples/README.md).

## Repository guide

| Location | Contents |
| --- | --- |
| `CATALOG.md` | Categorized human-readable resource directory |
| `data/resources.json` | Authoritative machine-readable catalogue |
| `data/resources.csv` | CSV export for filtering in spreadsheet software |
| `docs/` | Learning paths, methodology, metrics, glossary, provenance, and GitHub instructions |
| `examples/` | Clearly labeled teaching examples |
| `templates/` | Reusable evaluation and contribution templates |
| `scripts/` | Catalogue search, generation, structural checks, and optional link checks |

## Evidence, currency, and attribution

Initial primary-source review: **October 27, 2026**. Source review establishes the identity and stated purpose of a resource; it does not certify installation, execution, maintenance, or scientific validity. No external benchmark was executed while assembling this hub.

See [the validation record](docs/VALIDATION.md) for the catalogue and teaching-example checks completed for this release.

Descriptions and difficulty levels are editorial summaries. Difficulty describes expected prerequisites, not the severity of a risk. See [source provenance](docs/SOURCES.md), [scope and limitations](docs/SCOPE.md), and [the maintenance roadmap](docs/ROADMAP.md).

Credit the upstream authors when using their work. The MIT license covers this hub's original text, metadata, scripts, and examples; linked code, datasets, models, and papers retain their own licenses. No upstream benchmark datasets or source code are redistributed here.
