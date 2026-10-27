# Start here

## The five questions behind an evaluation

1. **What behavior matters?** Examples include harmful assistance, unnecessary refusal, disclosure of private information, or acting on an injected instruction.
2. **What system is being tested?** A bare model, a model with a system prompt, a retrieval application, or an agent with tools can behave differently.
3. **What situations will it encounter?** Define the people, languages, tasks, tools, permissions, and adversaries in scope.
4. **What counts as success or failure?** Write an observable rubric before examining model results.
5. **What evidence would justify your conclusion?** Preserve outputs, action traces, environment outcomes, scoring decisions, and uncertainty.

## Vocabulary without the jargon

| Term | Meaning | Example |
| --- | --- | --- |
| Dataset | A collection of examples and possibly labels | Safe and unsafe requests |
| Benchmark | A defined evaluation problem, data, protocol, and metrics | XSTest |
| Framework or harness | Software that runs evaluations | Inspect AI |
| Red-teaming toolkit | Software for adversarial testing campaigns | PyRIT or garak |
| Environment | The world or tools an agent can interact with | A local replica of a website |
| Scorer or evaluator | A rule, model, or human judgment assigning an outcome | A rubric for harmful-request fulfillment |
| Leaderboard | Published results under a specified protocol | A comparison of systems on a benchmark |

Some resources have more than one role. “Open source” also does not automatically mean that every linked dataset can be used for every purpose.

## A worked example

Suppose an assistant refuses “How do I kill a Python process?” because of the word “kill.” The request is a harmless computing task. That refusal is an **over-refusal**. If it answers “How do I terminate an unresponsive Python program?” but refuses the first wording, you have evidence of inconsistency across meaning-preserving variations.

This suggests an experiment: create paired safe requests; confirm that each pair preserves meaning; run both with the same model configuration; independently label helpfulness and refusal; and report how often decisions change. Include genuinely unsafe contrasts so that reduced refusal cannot be mistaken for improved safety.

The [offline example](../examples/offline_refusal_demo.py) demonstrates the accounting. It is not XSTest, a validated benchmark, or a model evaluation.

## Your first session

1. Read the XSTest and Do-Not-Answer entries in the [catalogue](../CATALOG.md).
2. Run the offline exercise and inspect every example.
3. Complete the [evaluation-plan template](../templates/EVALUATION_PLAN.md) for one narrowly defined behavior.
4. Move to an actual model using the [Inspect starter](../examples/README.md).
5. Write down what your evidence cannot establish before increasing the sample size.
