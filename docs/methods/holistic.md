# Holistic suites and regulation-aligned evaluation

!!! abstract "In one sentence"
    Run many evaluations together to get a broad profile of a model across risks, or map results to the requirements of a law or policy.

## Why it matters

No single benchmark covers everything. Holistic suites bundle many tests under one standard setup so models can
be compared fairly across many dimensions. Regulation-aligned suites go one step further and organise tests by
what laws and policies require, such as the EU AI Act. Organisations increasingly need this for compliance.

## The main approaches

| Suite | Organising idea |
| --- | --- |
| **HELM** | Many scenarios × many metrics (accuracy, robustness, fairness, toxicity, efficiency), standardised |
| **DecodingTrust** | Eight trust dimensions: toxicity, stereotypes, adversarial robustness, out-of-distribution robustness, privacy, machine ethics, fairness, and robustness to adversarial demonstrations |
| **TrustLLM** | Truthfulness, safety, fairness, robustness, privacy, machine ethics |
| **AIR-Bench 2024** | Risk categories taken from government regulations and company policies |
| **COMPL-AI** | Technical tests mapped to EU AI Act principles |

## How to use them

1. **Start with the dimension list.** Decide which dimensions matter for your use case; you rarely need all of them.
2. **Run the relevant subsets** with the suite's standard settings.
3. **Report per-dimension results.** Don't collapse everything into one number.
4. **Treat compliance mappings as a starting point.** A benchmark mapped to a regulation is one interpretation, not legal certification.

## Common mistakes

- **Averaging unrelated metrics.** A toxicity rate and a privacy-leak rate are not on the same scale.
- **Over-trusting a single overall score.** See the [metrics guide](../guides/metrics.md#never-average-away-the-main-question).
- **Mistaking breadth for depth.** Each dimension gets only a few tests; follow up with specialised benchmarks.

## Toolkits for this method

<!-- BEGIN toolkits:holistic -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [AIR-Bench 2024](../toolkits/content-safety.md#r049) | Evaluates safety against a policy-informed risk taxonomy. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2407.17436) · [Code](https://github.com/stanford-crfm/air-bench-2024) · [Data](https://huggingface.co/datasets/stanford-crfm/air-bench-2024) |
| [DecodingTrust](../toolkits/trustworthiness.md#r046) | Evaluates multiple dimensions of language-model trustworthiness. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2306.11698) · [Code](https://github.com/AI-secure/DecodingTrust) |
| [HELM](../toolkits/evaluation-infrastructure.md#r029) | Supports transparent multi-metric language-model evaluation. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2211.09110) · [Code](https://github.com/stanford-crfm/helm) · [Docs](https://crfm-helm.readthedocs.io/) |
| [TrustLLM](../toolkits/trustworthiness.md#r047) | Evaluates language models across several trustworthiness dimensions. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2401.05561) · [Code](https://github.com/HowieHwong/TrustLLM) |
| [COMPL-AI](../toolkits/governance-and-research.md#r077) | Maps technical LLM evaluations to aspects of AI regulation. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.07959) · [Code](https://github.com/compl-ai/compl-ai) |
<!-- END toolkits -->

## Key papers

- Liang et al., [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) (2022)
- Wang et al., [DecodingTrust](https://arxiv.org/abs/2306.11698) (2023)
- Zeng et al., [AIR-Bench 2024](https://arxiv.org/abs/2407.17436) (2024)
- Guldimann et al., [COMPL-AI Framework](https://arxiv.org/abs/2410.07959) (2024)
