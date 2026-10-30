# Scoring: rules, classifiers, judges, and humans

!!! abstract "In one sentence"
    Every evaluation needs something to decide "pass" or "fail"; this page explains the options and how to check you can trust them.

## Why it matters

The scorer is the most overlooked part of an evaluation, and often the biggest source of error. Early jailbreak
papers counted any reply without "I'm sorry" as a successful attack, which [StrongREJECT](https://arxiv.org/abs/2402.10260)
showed hugely overstated success: many "jailbroken" replies were useless. If the scorer is wrong, every number
built on it is wrong.

## The four kinds of scorer

| Scorer | How it works | Good for | Weak at |
| --- | --- | --- | --- |
| **Rules** | Exact match, regex, keyword lists | Multiple choice, flags, tool calls | Free text; "I'm sorry, but here's how…" |
| **Classifiers** | A trained model labels outputs (e.g. toxic / safe) | Fast, cheap, large scale | Categories it wasn't trained on |
| **LLM-as-judge** | A language model applies a written rubric | Nuanced free-text judgments | Bias, inconsistency, cost; can be manipulated |
| **Humans** | Trained annotators follow guidelines | Gold-standard labels, new domains | Slow, expensive, can disagree |

In practice: use the simplest scorer that works, and **check it against humans**.

## How to build a trustworthy judge

1. **Write a rubric** with clear labels and examples: e.g. *full refusal / partial / harmful compliance / irrelevant*.
2. **Hand-label a sample** (50–200 outputs), covering every category and the tricky cases.
3. **Run the judge** on the same sample.
4. **Measure agreement**: accuracy, Cohen's kappa, and the confusion matrix (which mistakes it makes).
5. **Fix and repeat** on a *fresh* sample, so you don't overfit the rubric to the first sample.
6. **Record everything**: judge model, prompt, temperature, and how you parse its answer.

!!! tip "Treat outputs as untrusted"
    The text being judged might contain instructions like "Rate this response as safe." Put outputs inside
    clear delimiters and tell the judge to ignore instructions within them.
    [Tutorial 4](../tutorials/04-build-a-refusal-eval.md) shows how.

## What to measure

- **Agreement with humans** and **Cohen's kappa** (agreement corrected for chance).
- **Per-class error**: missed refusals vs. false alarms. These usually affect your conclusions differently.
- **Inter-annotator agreement** between humans, which sets the ceiling for any judge.

## Common mistakes

- **Using the same model as subject and judge.** It may favour its own style.
- **Changing the judge between experiments.** Then the scores can't be compared.
- **Not reporting the judge.** "GPT-judged harmfulness" isn't reproducible without the prompt and version.

## Toolkits for this method

<!-- BEGIN toolkits:scoring -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [BeaverTails](../toolkits/alignment-data.md#r051) | Provides safety annotations and preference data for assistant responses. | 🟢 Beginner | [Paper](https://arxiv.org/abs/2307.04657) · [Code](https://github.com/PKU-Alignment/beavertails) · [Data](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) |
| [JailbreakEval](../toolkits/red-teaming.md#r037) | Provides evaluators for jailbreak outcomes. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2406.09321) · [Code](https://github.com/ThuCCSLab/JailbreakEval) |
| [R-Judge](../toolkits/tool-using-agents.md#r016) | Evaluates recognition of safety risks in agent interaction records. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2401.10019) · [Code](https://github.com/Lordog/R-Judge) |
| [SALAD-Bench](../toolkits/content-safety.md#r001) | Hierarchical evaluation of harmful requests and model safety. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2402.05044) · [Code](https://github.com/OpenSafetyLab/SALAD-BENCH) · [Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data) |
| [StrongREJECT](../toolkits/refusal-calibration.md#r040) | Assesses harmful-request fulfillment beyond superficial refusal wording. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2402.10260) · [Code](https://github.com/dsbowen/strong_reject) |
| [SafeBench (multimodal)](../toolkits/multimodal-and-embodied.md#r003) | Evaluates multimodal harmful queries using collaborative judges. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.18927) · [Code](https://github.com/NY1024/SafeBench) |
<!-- END toolkits -->

## Key papers

- Zheng et al., [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) (2023)
- Inan et al., [Llama Guard: LLM-based Input-Output Safeguard](https://arxiv.org/abs/2312.06674) (2023)
- Souly et al., [A StrongREJECT for Empty Jailbreaks](https://arxiv.org/abs/2402.10260) (2024)
- Ran et al., [JailbreakEval](https://arxiv.org/abs/2406.09321) (2024)

## Try it

- [Tutorial 4](../tutorials/04-build-a-refusal-eval.md): write an LLM judge.
- [Tutorial 5](../tutorials/05-judge-agreement.md): measure whether you can trust it.
