# Learning paths

Pick the path that matches you. You don't need to finish every step, and you can read any method guide at any time.

## Beginner: learn the evaluation loop (about 2 weeks, part-time)

| Step | Read | Do | You're done when you can… |
| --- | --- | --- | --- |
| 1. Concepts | [How evaluation works](index.md), [glossary](glossary.md) | [Tutorial 1](../tutorials/01-offline-refusal.md) | Explain dataset, scorer, and metric in your own words |
| 2. Refusal | [Harmful requests and over-refusal](../methods/harmful-requests.md); XSTest and OR-Bench papers | Label 20 replies by hand as *refused* or *answered* | Explain why over-refusal is a safety-relevant failure |
| 3. Tools | [Setup](setup.md) | [Tutorial 2](../tutorials/02-first-inspect-eval.md) and [Tutorial 3](../tutorials/03-run-a-benchmark.md) | Run a benchmark and find one interesting sample in the log viewer |
| 4. Build | [Scoring](../methods/scoring.md) | [Tutorial 4](../tutorials/04-build-a-refusal-eval.md) | Add 10 prompts of your own and rerun |
| 5. Trust | [Metrics and reporting](../guides/metrics.md) | [Tutorial 5](../tutorials/05-judge-agreement.md) | Say how much you trust your judge, with a number |
| 6. Compare | [Results report template](../guides/templates.md) | Compare two models or two system prompts on 50+ samples | Write a one-page report with sample sizes and uncertainty |

Start small. 10–20 examples are enough to debug your setup, but far too few for a conclusion.

## Practitioner: test an application you are building

1. Write down what your application can see and do: its data, tools, and users.
2. Decide what "good" and "bad" behaviour look like for routine and adversarial inputs.
3. Write application-specific tests with Inspect, promptfoo, DeepEval, or Giskard.
   ([Tutorial 4](../tutorials/04-build-a-refusal-eval.md) is a template.)
4. Run an automated scan with garak or promptfoo's red-team mode, then a structured campaign with PyRIT.
   See [red teaming](../methods/red-teaming.md).
5. If the application reads untrusted content (web pages, emails, documents) or uses tools, test
   [prompt injection](../methods/prompt-injection.md) with AgentDojo-style scenarios.
   ([Tutorial 6](../tutorials/06-prompt-injection.md) shows the idea.)
6. Fix what you find, then retest on cases you did *not* use while fixing.

Deliverable: a versioned [evaluation plan](../guides/templates.md), reproducible run settings, reviewed
failures, and agreed release criteria. Passing a generic benchmark is only one part of that decision.

## Researcher: produce evidence others can rely on

1. Read [Designing a rigorous study](../guides/methodology.md) and the [Safetywashing paper](https://arxiv.org/abs/2407.21792).
2. Define the construct you measure and how you'll observe it.
3. Survey existing benchmarks for overlap, policy assumptions, and missing populations
   ([SafetyPrompts](../toolkits/directories.md#r020) is a good index).
4. Pre-specify baselines, controls, attack budgets, repetitions, and primary metrics.
5. Audit your judge on a stratified human-labelled sample.
6. Test robustness across paraphrases, languages, settings, and held-out cases.
7. Report uncertainty, failures, costs, and limitations alongside headline scores
   ([Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640)).

For agents, a natural progression is R-Judge (labelled transcripts) → AgentHarm or AgentDojo (simulated tools)
→ SafeArena, ST-WebAgentBench, or OpenAgentSafety (full sandboxed environments). For frontier-risk work, read
[dangerous capabilities](../methods/dangerous-capabilities.md), [alignment and propensity](../methods/alignment-propensity.md),
and [AI control](../methods/ai-control.md).
