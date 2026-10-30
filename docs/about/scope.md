# Scope and limitations

## What this hub covers

Evaluating language models and AI agents for safety: harmful content, refusal calibration, adversarial
robustness, prompt injection, privacy, agent actions, dangerous capabilities, and alignment-related behaviour.

Fairness, factuality, alignment training data, governance papers, and capability benchmarks are included as
**supporting** categories. They answer related questions but are not substitutes for direct safety tests.

The hub is broad but not exhaustive. It doesn't systematically cover every language, modality, robotics
platform, interpretability method, or governance standard. Gaps we know about are listed in the [roadmap](roadmap.md).

## What "reviewed" means

Each catalogue entry says *"Source reviewed; execution not tested"*. That means its identity, purpose, and links
were checked against a primary source: the official repository, documentation, or author paper. It does **not**
mean the installation works, the dataset is still accessible, the project is maintained, or its conclusions
have been independently replicated.

Quickstart commands are copied from each project's own documentation. They have not been run by this hub, and
upstream projects change, so pin versions before doing a real study.

The tutorials in `examples/` **have** been run; see the [validation record](validation.md).

## Terms and access

Upstream code and data have their own licences, access conditions, and use restrictions. Some datasets on
Hugging Face are **gated**: you must accept terms before downloading. Check both code and data terms before
using or redistributing anything. This hub doesn't copy benchmark prompts or upstream code.

## Run risky experiments safely

Use synthetic accounts and local replicas for agent experiments. Code-execution and browser tasks need
disposable environments without real credentials, personal files, or live external actions. This applies to
running those experiments, not to reading this site or running Tutorials 1–6.

## Maintenance notes (from the October 2026 review)

- OpenAgentSafety's repository moved to `Open-Agent-Safety/OpenAgentSafety` in August 2026. The catalogue uses the new location.
- PyRIT moved from Azure to `microsoft/PyRIT`. The catalogue uses the new location.
- HELM's repository says it entered maintenance mode in June 2026.
- The linked multimodal SafeBench implementation describes itself as an initial proof of concept.
- SafetyPrompts.com says it is archived and has not been updated since May 2025.
- The official WASP repository was archived at the time of review.
- `openai/simple-evals` (SimpleQA's reference code) says it will no longer be updated for new models.
- AdvWeb's arXiv record is now titled AdvAgent, and its code is at `AI-secure/AdvAgent`. The catalogue keeps both names.
- ChemSafetyBench's paper is available; no official code location was confirmed, so none is linked.
- promptfoo states that it is now part of OpenAI and remains open source under the MIT licence.
