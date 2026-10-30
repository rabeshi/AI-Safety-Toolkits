# Metrics and reporting

Every number you report needs two things stated next to it: **what was counted** (the label definition) and
**out of what** (the denominator). Published benchmarks sometimes define similar-sounding metrics differently;
when reproducing one, use its definitions.

## Common safety metrics

| Measure | Formula used in this guide | Read it as |
| --- | --- | --- |
| Harmful fulfilment rate | unsafe requests that received disallowed help ÷ unsafe requests | Lower is better under your policy |
| Unsafe-request refusal rate | unsafe requests refused ÷ unsafe requests | Doesn't prove the reply had no harmful details |
| Over-refusal rate | benign requests wrongly refused ÷ benign requests | Lower is better, as long as safety holds |
| Benign task success | benign tasks done well ÷ benign tasks | Separates real help from unhelpful non-refusal |
| Attack success rate | successful attacks ÷ attack attempts (or ÷ target behaviours) | Meaningless without the denominator and budget |
| Policy-compliant completion | tasks completed with no policy violation ÷ tasks | Captures success and safety together |
| Pair consistency | meaning-preserving pairs with the same decision ÷ pairs | Both decisions can be consistently wrong |
| Judge agreement | judge labels matching reference labels ÷ audited cases | Also report kappa and per-class errors |

## Worked example

A system refuses 8 of 10 unsafe requests and wrongly refuses 2 of 10 benign ones:

- unsafe-request refusal rate = 8/10 = **80%**
- over-refusal rate = 2/10 = **20%**

You still don't know the harmful fulfilment rate. The 2 unsafe requests it didn't refuse might have received
useless answers, or dangerous ones. You need a content label for that.

If it only *completed* 5 benign tasks well, benign task success is **50%**, even though it refused only 2. Report
both.

## Uncertainty: how sure are you?

Small samples give noisy numbers. With 20 cases, an observed 80% could easily come from a true rate anywhere
between about 58% and 92%.

- For simple yes/no outcomes on independent cases, a **Wilson confidence interval** is a good default.
  [Tutorial 5](../tutorials/05-judge-agreement.md) includes a ten-line implementation.
- Inspect reports **stderr**. Roughly, the estimate ± 2 × stderr is a 95% interval.
- When comparing two systems on the same cases, use a **paired** analysis.
- Variants of one base prompt are **correlated**: resample whole families together (cluster bootstrap), not
  individual variants. See [Adding Error Bars to Evals](https://arxiv.org/abs/2411.00640).

Always say what one "case" is: a base task, a paraphrase, a generation, or an attack attempt.

## Never average away the main question

Keep risk categories visible. Don't average a chemistry-knowledge accuracy with a web-agent policy-violation
rate. If a project gives a composite score, report its parts and weights too.

## A minimal results table

| System | Benign n | Over-refusal (95% CI) | Unsafe n | Harmful fulfilment (95% CI) | Judge | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Model A, prompt v1 | 250 | 8.0% (5.2–12.0) | 200 | 3.5% (1.7–7.0) | Human-audited LLM judge, κ=0.81 | English only |

A full template is on the [templates page](templates.md).
