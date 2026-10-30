# Designing a rigorous study

The tutorials teach the mechanics. This guide is for when you want results other people can rely on. Use it
together with the [evaluation plan template](templates.md).

## 1. State the claim before running anything

Write one sentence naming the system, behaviour, population, and condition. For example:

> "Version B refuses fewer benign programming questions than version A, while refusing the matched unsafe requests
> at least as often, under our policy, in English."

Avoid unqualified claims such as "model X is safer".

## 2. Pin down exactly what is being tested

Record the model name and version, system prompt, temperature and other generation settings, context limits,
retrieval sources, tools, permissions, guardrails, and confirmation rules. For agents, also record the agent
code, environment image, task setup, and stopping conditions.

For adversarial tests, write the **threat model**: what the attacker controls, what they know, and their budget.
Keep "a malicious user typed this" separate from "malicious text arrived through a tool".

## 3. Build a defensible test set

- Keep **development**, **judge-calibration**, and **final test** sets separate.
- Keep paraphrases of the same prompt in the **same split**; otherwise they leak.
- Balance important categories and report the actual counts.
- Include **benign counterparts**, **ambiguous cases** with a rule for deciding them, and realistic hard negatives.
- Record languages, populations, data sources, duplicates, and any known training-data overlap.
- Have domain experts review labels where specialist knowledge matters.

## 4. Calibrate the scorer

Write a rubric covering refusal, harmful fulfilment, partial compliance, safe redirection, irrelevant answers,
and (for agents) execution outcomes. A refusal phrase can precede harmful help; a reply without refusal wording
can still safely redirect.

Check automated scoring against a human-labelled sample that covers every category and the tricky cases
([Tutorial 5](../tutorials/05-judge-agreement.md)). For an LLM judge, record its model, prompt, settings, and how
you parse its answer. Treat the outputs being judged as untrusted data.

## 5. Pilot, then freeze

Run a small pilot to catch broken setups, mislabelled tasks, parser failures, and runaway cost. Then **freeze the
protocol** before the final run. Pin package versions and upstream commits. Keep a run manifest and per-sample
records. Never silently drop errors: report how many there were and how you handled them.

Repeat runs when randomness can change outcomes. Compare systems on the **same** cases. If attacks are adaptive,
keep attack development separate from the final held-out evaluation.

## 6. Analyse without hiding trade-offs

Report harmful fulfilment, benign utility, over-refusal, and agent task completion **separately**, broken down by
risk category. Add confidence intervals and say what one "sample" is, because several variants of one prompt
are not independent ([metrics guide](metrics.md)).

For agents, examine intermediate actions and the final environment state. A failed harmful task might reflect
weak capability rather than safety. A successful benign task might still break a privacy or permission rule.

## 7. Publish a reproducibility package

Include the protocol, versions, configuration, data references, scoring rubric, analysis code, sample counts,
uncertainty, costs, failure categories, and limitations. Redact real identifiers and secrets from shared logs.
Cite the upstream benchmarks and respect their data terms.

---

This guide is an editorial synthesis. When reproducing a specific benchmark, its own protocol takes precedence.
Useful official references: [Inspect documentation](https://inspect.aisi.org.uk/), [HarmBench](https://github.com/centerforaisafety/HarmBench),
[AgentDojo](https://github.com/ethz-spylab/agentdojo), and [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640).
