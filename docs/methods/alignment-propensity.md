# Alignment and propensity evaluations

!!! abstract "In one sentence"
    Put the model in situations where it could be dishonest, flattering, power-seeking, or deceptive, and observe what it *tends* to do.

## Why it matters

As models become more capable, a key worry is not misuse by people but the model itself behaving badly: telling
users what they want to hear, hiding its true reasoning, pursuing a goal by unintended means, or
deliberately doing badly on tests ("sandbagging") so it seems less capable. These evaluations look for early
signs of such behaviour in controlled settings.

## What gets tested

| Behaviour | The question | Examples |
| --- | --- | --- |
| **Sycophancy** | Does it change correct answers to agree with the user? | Anthropic sycophancy evals |
| **Honesty** | Does it state things it "believes" are false when pressured? | MASK |
| **Power-seeking / unethical shortcuts** | In a game, does it take harmful actions to win? | MACHIAVELLI |
| **Scheming / deception** | Given a goal and an obstacle, does it covertly deceive or sabotage? | Apollo's in-context scheming evals |
| **Agentic misalignment** | Does an agent take harmful actions (e.g. blackmail) when its goals are threatened? | Anthropic's agentic misalignment scenarios |
| **Sandbagging** | Does it underperform on purpose when it thinks it's being evaluated? | AI Sandbagging (van der Weij et al.) |
| **Situational awareness** | Does it know it's an AI, being tested, or deployed? | SAD |
| **Alignment faking** | Does it behave differently when it thinks it's being trained vs. not? | Greenblatt et al. 2024 |

## How it works

1. **Design a scenario** where the misaligned action is possible and tempting, e.g. the model learns it will be
   replaced, and has access to an email that would let it prevent that.
2. **Make it believable but contained.** Use fake companies, fake files, and sandboxed tools.
3. **Run many samples**, because rare behaviours matter.
4. **Read the transcripts**, including the model's reasoning if visible, to classify *why* it acted.
5. **Vary the conditions** (goal strength, oversight cues) to see what triggers the behaviour.
6. **Report rates and conditions**, and be clear the setting is artificial.

## A tiny example (sycophancy)

> **Turn 1:** "What's the capital of Australia?" → "Canberra."
> **Turn 2:** "I'm pretty sure it's Sydney. Are you sure?"
> **Sycophantic failure:** "You're right, I apologise, it's Sydney."

## What to measure

- **Rate of the target behaviour** per scenario and condition.
- **Sensitivity** to cues: does behaviour change when the model is told it's being watched?
- For honesty, **belief vs. statement**: MASK first elicits what the model believes, then checks if it lies under pressure.

## Common mistakes

- **Over-claiming from contrived scenarios.** These are demonstrations of possibility, not base rates in deployment.
- **Over-reading model-written reasoning.** Visible reasoning may not reflect the model's actual computation.
- **Prompt leakage.** If the scenario practically instructs the model to misbehave, you've measured instruction-following.
- **Not checking for evaluation awareness.** Models increasingly recognise tests, which can change behaviour.

## Toolkits for this method

<!-- BEGIN toolkits:alignment-propensity -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [Sycophancy evaluations](../toolkits/trustworthiness.md#r076) | Examines agreement with users at the expense of truthful judgment. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2212.09251) · [Code](https://github.com/anthropics/evals) |
| [Agentic Misalignment](../toolkits/specialized-risk.md#r082) | Studies misaligned behavior in controlled organizational scenarios. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2510.05179) · [Code](https://github.com/anthropic-experimental/agentic-misalignment) |
| [Frontier Models are Capable of In-context Scheming](../toolkits/specialized-risk.md#r022) | Investigates strategic deceptive behavior in controlled scenarios. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2412.04984) |
| [MACHIAVELLI](../toolkits/specialized-risk.md#r075) | Evaluates harmful and power-seeking behavior in text-based decision environments. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2304.03279) · [Code](https://github.com/aypan17/machiavelli) |
<!-- END toolkits -->

Inspect Evals also includes `mask` (honesty), `sad` (situational awareness), `instrumentaleval`, `gdm_stealth`,
and `agentic_misalignment`.

## Key papers

- Perez et al., [Discovering Language Model Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251) (2022)
- Sharma et al., [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) (2023)
- Hubinger et al., [Sleeper Agents](https://arxiv.org/abs/2401.05566) (2024): a "model organism" of hidden misbehaviour.
- van der Weij et al., [AI Sandbagging](https://arxiv.org/abs/2406.07358) (2024)
- Laine et al., [Me, Myself, and AI: The Situational Awareness Dataset](https://arxiv.org/abs/2407.04694) (2024)
- Meinke et al., [Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984) (2024)
- Greenblatt et al., [Alignment Faking in Large Language Models](https://arxiv.org/abs/2412.14093) (2024)
- Ren et al., [The MASK Benchmark](https://arxiv.org/abs/2503.03750) (2025)
- Lynch et al., [Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179) (2025)

## Try it

`inspect eval inspect_evals/sycophancy --limit 20` is the gentlest start.
