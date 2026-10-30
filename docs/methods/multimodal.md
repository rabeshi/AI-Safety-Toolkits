# Multimodal and embodied safety

!!! abstract "In one sentence"
    Test whether images, screenshots, or physical settings change a model's safety behaviour, including attacks that hide harmful requests inside pictures.

## Why it matters

Models that see images can be attacked through them. A harmful instruction written *as text inside an image*
often bypasses safety training that works on typed text. Images also change what's safe: "Can I go for a run
here?" is fine on a beach and dangerous on a motorway. Robots and embodied agents add physical consequences.

## The main approaches

| Approach | How it works | Examples |
| --- | --- | --- |
| **Image-based harmful queries** | Pair harmful requests with related images or typography | MM-SafetyBench, FigStep |
| **Adversarial images** | Optimise image pixels to jailbreak the model | Visual adversarial examples (Qi et al.) |
| **Situational safety** | Same question, different visual context: safe in one, unsafe in another | MSSBench |
| **Embodied task planning** | Does a robot agent's plan include hazardous steps? | SafeAgentBench |
| **Attacks on GUI agents** | Manipulate screenshots or web pages a vision agent sees | ARE, AdvAgent |

## How it works (situational safety)

1. **Write a query** that's safe or unsafe depending on context: *"How do I practise my golf swing here?"*
2. **Pair it with images**: an empty driving range (safe) vs. a crowded room with a chandelier (unsafe).
3. **Ask the model** with each image.
4. **Score** whether it notices the hazard in the unsafe context and still helps in the safe one.

## What to measure

- **Safety rate** on unsafe contexts and **helpfulness** on safe ones.
- **Attack success** for image-based jailbreaks, compared with the same request as plain text.

## Common mistakes

- **Only testing text.** A text-safe model can be image-unsafe.
- **Simulator-to-reality gaps.** Embodied results in simulation don't guarantee physical safety.

## Toolkits for this method

<!-- BEGIN toolkits:multimodal -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [Dissecting Adversarial Robustness of Multimodal LM Agents](../toolkits/web-and-gui-agents.md#r014) | Studies adversarial robustness of multimodal agents. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2406.12814) · [Code](https://github.com/ChenWu98/agent-attack) |
| [MM-SafetyBench](../toolkits/multimodal-and-embodied.md#r073) | Evaluates multimodal safety under image-associated harmful requests. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2311.17600) · [Code](https://github.com/isXinLiu/MM-SafetyBench) |
| [MSSBench](../toolkits/multimodal-and-embodied.md#r074) | Evaluates safety decisions conditioned on visual situations. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.06172) · [Code](https://github.com/UCSB-AI/MSSBench) |
| [SafeAgentBench](../toolkits/multimodal-and-embodied.md#r006) | Evaluates safe task planning by embodied language-model agents. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2412.13178) · [Code](https://github.com/shengyin1224/SafeAgentBench) |
| [SafeBench (multimodal)](../toolkits/multimodal-and-embodied.md#r003) | Evaluates multimodal harmful queries using collaborative judges. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.18927) · [Code](https://github.com/NY1024/SafeBench) |
<!-- END toolkits -->

## Key papers

- Qi et al., [Visual Adversarial Examples Jailbreak Aligned Large Language Models](https://arxiv.org/abs/2306.13213) (2023)
- Gong et al., [FigStep](https://arxiv.org/abs/2311.05608) (2023)
- Liu et al., [MM-SafetyBench](https://arxiv.org/abs/2311.17600) (2023)
- Zhou et al., [Multimodal Situational Safety (MSSBench)](https://arxiv.org/abs/2410.06172) (2024)
