# Factuality and hallucination

!!! abstract "In one sentence"
    Check whether the model states false things confidently, and whether it admits when it doesn't know.

## Why it matters

A model that invents legal cases, medical facts, or citations can cause real harm because it sounds just as
confident when wrong. In safety terms, factuality is also linked to **honesty**: does the model say what it
"believes", and does it know the limits of its knowledge?

## The main approaches

| Approach | How it works | Examples |
| --- | --- | --- |
| **Short-answer facts** | Questions with a single checkable answer; models may also abstain | SimpleQA |
| **Misconception traps** | Questions where the popular answer is wrong | TruthfulQA |
| **Hallucination recognition** | Can the model spot hallucinated content in a given answer? | HaluEval |
| **Long-form fact checking** | Split a long answer into atomic claims and verify each | FActScore |
| **Self-consistency** | Sample several answers; inconsistent ones are likely made up | SelfCheckGPT |

## How it works (SimpleQA-style)

1. **Collect questions** with one indisputable short answer.
2. **Ask the model**, allowing it to say "I don't know".
3. **Grade** each answer as *correct*, *incorrect*, or *not attempted*.
4. **Report all three**, because a model that never abstains might have higher accuracy but more confident errors.

## What to measure

- **Accuracy**, and **accuracy when attempted**.
- **Abstention rate**, and how sensible abstentions are.
- **Calibration**: when the model says it's 80% sure, is it right 80% of the time?

## Common mistakes

- **Rewarding guessing.** Accuracy alone favours models that never say "I don't know".
- **Ignoring answer formatting.** Exact-match grading misses correct answers phrased differently; SimpleQA uses an LLM grader.
- **Testing with stale facts.** Questions about changing facts expire.

## Toolkits for this method

<!-- BEGIN toolkits:factuality -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [SimpleQA](../toolkits/factuality-and-hallucination.md#r061) | Evaluates short factual question answering. | 🟢 Beginner | [Paper](https://arxiv.org/abs/2411.04368) · [Code](https://github.com/openai/simple-evals) |
| [TruthfulQA](../toolkits/factuality-and-hallucination.md#r060) | Tests susceptibility to common human misconceptions. | 🟢 Beginner | [Paper](https://arxiv.org/abs/2109.07958) · [Code](https://github.com/sylinrl/TruthfulQA) · [Data](https://huggingface.co/datasets/truthfulqa/truthful_qa) |
| [HaluEval](../toolkits/factuality-and-hallucination.md#r062) | Evaluates hallucination recognition in generated text. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2305.11747) · [Code](https://github.com/RUCAIBox/HaluEval) · [Data](https://huggingface.co/datasets/pminervini/HaluEval) |
<!-- END toolkits -->

## Key papers

- Lin et al., [TruthfulQA](https://arxiv.org/abs/2109.07958) (2021)
- Manakul et al., [SelfCheckGPT](https://arxiv.org/abs/2303.08896) (2023)
- Min et al., [FActScore](https://arxiv.org/abs/2305.14251) (2023)
- Wei et al., [Measuring Short-Form Factuality in Large Language Models (SimpleQA)](https://arxiv.org/abs/2411.04368) (2024)

## Try it

`inspect eval inspect_evals/truthfulqa --limit 20` (see [Tutorial 3](../tutorials/03-run-a-benchmark.md)).
