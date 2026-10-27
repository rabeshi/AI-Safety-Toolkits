# Learning paths

These are suggested sequences, not a requirement to master every project.

## Beginner: learn the evaluation loop

| Stage | Resources | Exercise | Completion evidence |
| --- | --- | --- | --- |
| 1. Concepts | Start here; glossary | Distinguish data, harness, judge, and environment | Explain each in your own words |
| 2. Refusal calibration | XSTest; Do-Not-Answer; OR-Bench | Label a small mix of benign and unsafe requests | An annotation table with reasons |
| 3. First implementation | Inspect AI; Inspect Evals | Run a tiny task and inspect sample-level logs | Saved configuration and logs |
| 4. Score quality | StrongREJECT; metrics guide | Compare simple rules, a judge, and human review | A disagreement analysis |
| 5. Small comparison | HarmBench or SORRY-Bench | Compare two system configurations under fixed conditions | A report with denominators and uncertainty |

Start with roughly 10–20 examples to debug the workflow. This is a pilot, not enough evidence for a broad claim. Choose the eventual sample size from the precision you need and the variability you observe.

## Practitioner: evaluate an application

1. Map a real workflow and identify the data and actions the assistant can access.
2. Define expected behavior on both routine and adversarial inputs.
3. Use promptfoo, Giskard, DeepEval, or Inspect to implement application-specific checks.
4. Select PyRIT or garak for a structured adversarial campaign, with a documented budget.
5. For retrieval or tool use, add AgentDojo, InjecAgent, or BIPIA scenarios that resemble your attack surface.
6. Review failures with the application owners and retest the fixed version against held-out cases.

Deliverable: a versioned evaluation plan, reproducible run configuration, reviewed failures, and explicit release criteria. Passing a generic benchmark is only one component of that decision.

## Researcher or professional evaluator: establish defensible evidence

1. Identify the construct being measured and its observable indicators.
2. Examine existing benchmarks for overlapping data, policy assumptions, and missing populations.
3. Predefine baselines, controls, attack budgets, repetition counts, and primary metrics.
4. Audit the judge on a stratified human-labeled sample.
5. Study robustness across paraphrases, languages, settings, and independently held-out cases.
6. Report uncertainty, failures, abstentions, costs, and limitations alongside aggregate scores.

For agents, progress from R-Judge's recorded interactions to AgentHarm or AgentDojo, then to SafeArena, ST-WebAgentBench, or OpenAgentSafety if the research question requires full environment execution. Do not assume identical scores across those environments mean identical risk.

Deliverable: a preregistered or clearly timestamped protocol, artifact versions, a reproducibility package, and a documented claim boundary.
