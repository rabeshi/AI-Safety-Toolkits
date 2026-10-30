# Dangerous capability evaluations

!!! abstract "In one sentence"
    Measure how much a model *could* help with catastrophic misuse (cyberattacks, chemical or biological weapons) or act autonomously, by testing its best possible performance on proxy tasks.

## Why it matters

Frontier AI developers and governments use these evaluations to decide whether a model needs stronger safeguards
before release. Many company safety policies (Anthropic's Responsible Scaling Policy, OpenAI's Preparedness
Framework, Google DeepMind's Frontier Safety Framework) are built around **capability thresholds** measured this
way. Unlike most evaluations, the question is not "will it refuse?" but "if safeguards fail or are removed, how
much does it help?"

## The main approaches

| Approach | What it measures | Examples |
| --- | --- | --- |
| **Knowledge proxies** | Multiple-choice questions on hazardous precursor knowledge | WMDP (bio, chem, cyber) |
| **Task-based challenges** | Solving realistic tasks, e.g. capture-the-flag hacking in a sandbox | Cybench, Inspect's GDM CTF tasks |
| **Code-risk tests** | Writing insecure code or helping with cyberattacks | CyberSecEval, RedCode |
| **Autonomy tasks** | Long, multi-step tasks such as AI research or self-replication | RE-Bench, METR's time-horizon tasks, GDM self-proliferation |
| **Human uplift studies** | Do people *with* the model do better than people with only the internet? | Lab and government studies, often not public |

## How it works

1. **Pick a threat model**, e.g. "a novice uses the model to carry out a known cyberattack".
2. **Choose proxy tasks** that would indicate the capability, written or reviewed by domain experts.
3. **Elicit the best performance.** Use good prompts, tools, many attempts, and sometimes fine-tuning. If you
   under-elicit, you under-estimate risk. That's the opposite of the usual mistake.
4. **Run in isolation.** Hacking tasks run in sandboxed containers with no internet access to real targets.
5. **Compare to thresholds and baselines**, such as human experts or previous models.
6. **Handle results carefully.** Detailed hazardous results are often not published.

## A tiny example

> **Cybench-style task:** "You have shell access to a container. Find the hidden flag on the web server at
> `victim:8080`." The model succeeds if it submits the correct flag string. Partial credit is given for
> subtasks such as finding the vulnerable endpoint.

## What to measure

- **Success rate** on tasks (often `pass@k`: success within *k* attempts).
- **Task difficulty** relative to humans, e.g. "tasks taking an expert 1 hour" ([METR time horizons](https://arxiv.org/abs/2503.14499)).
- **Uplift**: the difference between with-AI and without-AI groups, in human studies.

## Common mistakes

- **Under-elicitation.** A weak agent scaffold makes a capable model look safe. See
  [password-locked models](https://arxiv.org/abs/2405.19550) and [sandbagging](alignment-propensity.md).
- **Treating knowledge as capability.** Answering WMDP questions is not the same as carrying out an attack.
- **Leaking hazardous material.** Don't publish new hazardous questions or transcripts; WMDP was designed so its questions are not themselves dangerous.
- **Unsandboxed execution.** Never let these agents touch real systems.

## Toolkits for this method

<!-- BEGIN toolkits:dangerous-capabilities -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [ChemSafetyBench](../toolkits/specialized-risk.md#r007) | Studies chemistry-specific knowledge and safety behavior. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2411.16736) |
| [Cybench](../toolkits/specialized-risk.md#r065) | Evaluates cybersecurity task capabilities in controlled environments. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2408.08926) · [Code](https://github.com/andyzorigin/cybench) |
| [CyberSecEval](../toolkits/specialized-risk.md#r064) | Evaluates cybersecurity-relevant risks and capabilities. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2312.04724) · [Code](https://github.com/meta-llama/PurpleLlama) |
| [RedCode](../toolkits/specialized-risk.md#r011) | Evaluates risky code generation and execution by code agents. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2411.07781) · [Code](https://github.com/AI-secure/RedCode) |
| [WMDP](../toolkits/specialized-risk.md#r063) | Uses expert-written questions as proxies for hazardous domain knowledge. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2403.03218) · [Code](https://github.com/centerforaisafety/wmdp) · [Data](https://huggingface.co/datasets/cais/wmdp) |
<!-- END toolkits -->

Inspect Evals also includes Google DeepMind's dangerous-capability suites (`gdm_intercode_ctf`, `gdm_in_house_ctf`,
`gdm_self_proliferation`, `gdm_self_reasoning`, `gdm_stealth`) and newer cyber benchmarks such as `cyberseceval_3`
and `cve_bench`. See the [Inspect Evals listing](https://ukgovernmentbeis.github.io/inspect_evals/).

## Key papers

- Shevlane et al., [Model evaluation for extreme risks](https://arxiv.org/abs/2305.15324) (2023): why these evaluations exist.
- Phuong et al., [Evaluating Frontier Models for Dangerous Capabilities](https://arxiv.org/abs/2403.13793) (2024)
- Li et al., [The WMDP Benchmark](https://arxiv.org/abs/2403.03218) (2024)
- Zhang et al., [Cybench](https://arxiv.org/abs/2408.08926) (2024)
- Wijk et al., [RE-Bench](https://arxiv.org/abs/2411.15114) (2024)
- Kwa et al., [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) (2025)

## Try it

`inspect eval inspect_evals/wmdp_cyber --limit 20` needs no Docker. Cybench needs Docker; see its
[quickstart](../toolkits/specialized-risk.md#r065).
