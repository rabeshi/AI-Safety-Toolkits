# Evaluation methodology

## Define the claim before running a test

Write one sentence with a system, behavior, population, and condition. For example: “Version A refuses fewer benign computing requests than Version B while preserving refusal of the matched unsafe requests under this policy.” Avoid an unqualified claim that one model is “safer.”

Use the [evaluation plan](../templates/EVALUATION_PLAN.md) to record scope and intended analysis.

## Set the system boundary

Record the exact model identifier or checkpoint, system/developer prompts, decoding settings, context limits, retrieval sources, available tools, permissions, guardrails, and user-confirmation rules. An agent evaluation also requires the agent implementation, environment image, task initialization, and stopping conditions.

For adversarial tests, define what the attacker controls, what they know, their query/compute budget, and the desired deviation. Distinguish a malicious user request from malicious instructions arriving through an untrusted tool response.

## Build a defensible test set

- Keep development, judge-calibration, and final test sets separate.
- Split related prompt families together; otherwise paraphrases can leak across splits.
- Balance important categories and report the actual category sizes.
- Include benign counterparts, ambiguous cases with an adjudication rule, and realistic difficult negatives.
- Record languages, populations, data origins, duplicates, and any known training overlap.
- Have domain experts review labels where specialist knowledge matters.

## Calibrate the scorer

Write a rubric for refusal, harmful fulfillment, partial compliance, safe redirection, irrelevant answers, and execution outcomes. A refusal phrase can precede harmful assistance; an answer without refusal wording can still safely redirect the user.

Audit automated scoring against a human-labeled sample spanning categories and difficult cases. Report scorer errors and disagreements. Use blinded comparisons where possible. For an LLM judge, record its model, prompt, sampling settings, and decision parsing. Treat outputs and trajectories as untrusted data within judge prompts.

## Run a pilot, then freeze the protocol

Use a small pilot to catch broken adapters, mislabeled tasks, failed parsers, and runaway cost. Fix the protocol before the final test. Pin package versions and upstream commits. Store a run manifest and sample-level records. Do not silently drop model errors or environment failures: report their counts and your handling rule.

Repeat runs when stochastic generation or environmental variation can change outcomes. Pair comparisons on the same cases. If attacks are adaptive, distinguish development-time selection from the final held-out evaluation.

## Analyze without hiding tradeoffs

Report harmful fulfillment, benign utility, over-refusal, and agent task completion separately. Break results down by relevant risk category and task family. Add intervals and an explanation of the sampling unit; multiple variants of one prompt are not independent cases.

For agents, examine intermediate actions and final environment state. A failed harmful task might reflect weak capability rather than a deliberate safety boundary. A successful benign task may still violate a privacy or permission policy.

## Publish a reproducibility package

Include the protocol, versions, configuration, permitted data references, scoring rubric, analysis code, sample counts, uncertainty, costs, failure categories, and limitations. Redact real identifiers and secrets in shared logs. Preserve original upstream citations and dataset-use terms.

This guide is an editorial synthesis. Resource-specific scientific protocols remain authoritative for claims of reproducing that benchmark. Official starting points include [Inspect's documentation](https://inspect.aisi.org.uk/), [HarmBench](https://github.com/centerforaisafety/HarmBench), and [AgentDojo](https://github.com/ethz-spylab/agentdojo).
