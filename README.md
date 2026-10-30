# AI Safety Toolkit Hub

**Learn how AI systems are tested for safety, then do it yourself.**

📖 **Read it as a website: <https://rabeshi.github.io/AI-Safety-Toolkits/>**

This hub is a beginner-friendly guide to AI safety evaluation. It explains the methods researchers use to test AI
models and agents, walks you through hands-on tutorials, and catalogues 92 benchmarks, datasets, and tools, each
with links to the **paper**, **code**, **docs**, and **data**. A Foundations section and study roadmap place
evaluation within the wider field of AI safety.

You don't need a machine-learning background. If you can run a Python script, you can follow along.

## What's inside

| Section | What you get |
| --- | --- |
| [Getting started](docs/getting-started/index.md) | What an evaluation is, key vocabulary, setup guide, learning paths |
| [Foundations](docs/foundations/index.md) | A study roadmap for the whole field; why AI might be dangerous; key alignment concepts; how safety is built into models (RLHF, constitutional AI, adversarial training, unlearning); interpretability in depth; governance and policy; free courses, papers, and communities |
| [Evaluation methods](docs/methods/index.md) | 15 plain-language guides: harmful requests and over-refusal, red teaming, prompt injection, agent safety, dangerous capabilities, alignment and propensity, AI control, interpretability, scoring and judges, bias, factuality, privacy, multimodal, holistic suites |
| [Tutorials](docs/tutorials/index.md) | 6 step-by-step exercises, from scoring by hand (no installs) to testing an AI agent for prompt injection |
| [Toolkit catalogue](CATALOG.md) | 92 resources with paper, code, docs, and dataset links; 41 have copy-paste quickstarts |
| [Guides](docs/guides/choosing.md) | Choosing a resource, designing a rigorous study, metrics and reporting, templates |

## Start in five minutes

You only need Python 3.10 or newer for this first step.

```bash
git clone https://github.com/rabeshi/AI-Safety-Toolkits.git
cd AI-Safety-Toolkits
python examples/01_offline_refusal_demo.py
```

This scores a tiny, invented refusal test by hand. It needs no model, account, or internet connection.
[Tutorial 1](docs/tutorials/01-offline-refusal.md) explains every line.

Then [set up Inspect AI](docs/getting-started/setup.md) (Python 3.11+) and continue with the other tutorials:

| # | Tutorial | Code |
| --- | --- | --- |
| 1 | [Score an evaluation by hand](docs/tutorials/01-offline-refusal.md) | [`01_offline_refusal_demo.py`](examples/01_offline_refusal_demo.py) |
| 2 | [Your first Inspect eval](docs/tutorials/02-first-inspect-eval.md) | [`02_first_inspect_eval.py`](examples/02_first_inspect_eval.py) |
| 3 | [Run a real benchmark](docs/tutorials/03-run-a-benchmark.md) | one-line `inspect eval inspect_evals/...` commands |
| 4 | [Build a refusal eval with an LLM judge](docs/tutorials/04-build-a-refusal-eval.md) | [`04_refusal_eval.py`](examples/04_refusal_eval.py) |
| 5 | [Check your judge against humans](docs/tutorials/05-judge-agreement.md) | [`05_judge_agreement.py`](examples/05_judge_agreement.py) |
| 6 | [Test an agent for prompt injection](docs/tutorials/06-prompt-injection.md) | [`06_prompt_injection.py`](examples/06_prompt_injection.py) |

## Good first resources

| Resource | Why start here | Links |
| --- | --- | --- |
| Inspect AI | Learn how an evaluation is built: dataset, solver, scorer, logs | [Code](https://github.com/UKGovernmentBEIS/inspect_ai) · [Docs](https://inspect.aisi.org.uk/) |
| Inspect Evals | Run dozens of published benchmarks with one command | [Code](https://github.com/UKGovernmentBEIS/inspect_evals) · [Docs](https://ukgovernmentbeis.github.io/inspect_evals/) |
| XSTest | See why refusing a *harmless* request is also a failure | [Paper](https://arxiv.org/abs/2308.01263) · [Code](https://github.com/paul-rottger/xstest) |
| HarmBench | Standardised harmful-request testing and automated red teaming | [Paper](https://arxiv.org/abs/2402.04249) · [Code](https://github.com/centerforaisafety/HarmBench) |
| AgentDojo | How tool-using agents get hijacked by injected instructions | [Paper](https://arxiv.org/abs/2406.13352) · [Code](https://github.com/ethz-spylab/agentdojo) |
| AgentHarm | Compare harmful and harmless multi-step agent tasks | [Paper](https://arxiv.org/abs/2410.09024) · [Data](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) |

## Repository layout

| Path | Contents |
| --- | --- |
| `docs/` | The website's pages (Markdown) |
| `examples/` | Tutorial code, all tested |
| `data/resources.json` | The catalogue's single source of truth; `resources.csv` is an export |
| `CATALOG.md` | The full catalogue as one GitHub-readable page (generated) |
| `scripts/` | Generate pages from the JSON, validate, search, and check links |
| `templates/` | Evaluation plan, results report, and resource-proposal templates |

Useful commands:

```bash
python scripts/catalog.py --level Beginner          # search the catalogue from the terminal
python scripts/catalog.py --method prompt-injection
python scripts/generate_catalog.py                  # rebuild generated pages after editing the JSON
python scripts/validate.py                          # check data, generated files, and links
pip install -r requirements-docs.txt && mkdocs serve   # preview the website at http://127.0.0.1:8000
```

## How much to trust this

- Paper, code, and dataset links were verified against arXiv, GitHub, and Hugging Face in October 2026.
- The tutorials were run and tested ([validation record](docs/about/validation.md)).
- Quickstart commands are copied from each project's documentation but were **not** run by this hub.
- Descriptions and difficulty levels are editorial. A benchmark score is evidence about one test under specific
  conditions, not proof that a system is safe.

See [scope and limitations](docs/about/scope.md).

## Contributing and licence

Corrections and new resources are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

The MIT licence covers this hub's text, metadata, scripts, and examples. Linked code, datasets, models, and
papers keep their own licences. No upstream benchmark data or code is redistributed here. Please cite the
original authors when you use their work.
