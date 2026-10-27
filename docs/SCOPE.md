# Scope and limitations

This repository focuses on evaluating language models and agents, including content safety, refusal calibration, adversarial robustness, privacy, tool use, web interaction, and selected specialized risks.

Fairness, factuality, alignment training data, governance papers, and capability controls are included as supporting categories. They are not interchangeable with direct safety benchmarks. This collection is broad, but not exhaustive; it does not systematically cover every language, modality, robotics platform, interpretability method, or governance standard.

## What review means

“Source reviewed; execution not tested” means the resource's identity and high-level purpose were checked against a primary source. It does not mean that its installation works, that the dataset is accessible, that the project is actively maintained, or that the benchmark's conclusions have been independently replicated.

Source-review dates are not software compatibility guarantees. Repository pages and papers can change; pin a specific version before conducting a study. The hub's initial release executes only its own teaching and catalogue utilities.

## Terms and access

Upstream code and data may have different licenses, access requirements, or use restrictions. Review both before downloading or redistributing. A linked paper is not proof that associated code or data are currently available. We do not copy benchmark prompts or implementation code into this hub.

## Controlled execution

Use synthetic accounts and local replicas for agent experiments. Risky code and browser tasks need disposable environments without production credentials, personal files, or live external actions. These are concrete prerequisites for the corresponding experiments, not a requirement to browse this directory or run its offline exercise.

## Maintenance observations

- OpenAgentSafety's maintained repository moved to `Open-Agent-Safety/OpenAgentSafety` in August 2026. The catalogue uses the new destination.
- PyRIT's old Azure repository directs users to `microsoft/PyRIT`; the catalogue uses the new destination.
- HELM's repository states it entered maintenance mode in June 2026.
- The linked multimodal SafeBench implementation describes itself as an initial proof of concept.
- SafetyPrompts.com states it is archived and has not been updated since May 2025.
- The official WASP repository was observed as archived during initial review.
- The SimpleQA reference location, `openai/simple-evals`, announces that it will no longer be updated for new models or results.
- AdvWeb's linked arXiv record now uses the title AdvAgent; the catalogue preserves the original label as an alias.
- ChemSafetyBench's paper is available; the author-linked code location must be checked independently before planning a reproduction.
