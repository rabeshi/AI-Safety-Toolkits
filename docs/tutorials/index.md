# Tutorials

Six hands-on tutorials, from no installs to testing an AI agent. Each one builds on the previous, takes
15–30 minutes, and ends with "what you learned" and "try this next".

| # | Tutorial | You will learn | Needs |
| --- | --- | --- | --- |
| 1 | [Score an evaluation by hand](01-offline-refusal.md) | Test cases, labels, and metrics; over-refusal | Python only |
| 2 | [Your first Inspect eval](02-first-inspect-eval.md) | Datasets, solvers, scorers, and logs in a real framework | [Setup](../getting-started/setup.md) |
| 3 | [Run a real benchmark](03-run-a-benchmark.md) | Running published benchmarks (XSTest, TruthfulQA, AgentHarm) with one command | Setup + API key |
| 4 | [Build a refusal eval with a judge](04-build-a-refusal-eval.md) | Writing your own dataset and an LLM-as-judge scorer | Setup + API key |
| 5 | [Check your judge](05-judge-agreement.md) | Measuring judge reliability: agreement, kappa, confidence intervals | Python only |
| 6 | [Test an agent for prompt injection](06-prompt-injection.md) | Tools, agents, attacks hidden in data, security vs. utility | Setup + API key |

All the code is in the [`examples/`](https://github.com/rabeshi/AI-Safety-Toolkits/tree/main/examples) folder of
the repository.

!!! tip "No API key yet?"
    Every Inspect tutorial can be run with `--model mockllm/model`. The mock model gives fake answers for free,
    which is enough to check that everything is wired up correctly. The scores will be meaningless.

!!! warning "These are learning exercises"
    The tutorials use tiny, hand-written datasets. Their numbers are not evidence about any model. For real
    studies, use the published benchmarks in the [catalogue](../toolkits/index.md) and the
    [methodology guide](../guides/methodology.md).
