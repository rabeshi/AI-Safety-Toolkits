# Why AI might be dangerous

!!! abstract "In one sentence"
    Powerful AI could cause serious harm because people misuse it, because competition pushes safety aside, because organisations make costly mistakes, or because AI systems pursue goals we didn't intend.

## Why take this seriously?

AI systems are improving quickly and are being given more autonomy: writing and running code, browsing the
web, and acting on people's behalf. Many leading researchers think this could eventually lead to very
serious harm, while others disagree about how likely or how soon. The
[International AI Safety Report](https://arxiv.org/abs/2501.17805) (2025), written by about 100 experts and
chaired by Yoshua Bengio, summarises the evidence and the areas of disagreement. It's the best neutral starting point.

You don't have to accept any particular forecast to see why safety work matters. Every powerful technology needs
testing, safeguards, and oversight, and AI is general-purpose, so its risks are unusually broad.

## The four main sources of risk

The [Overview of Catastrophic AI Risks](https://arxiv.org/abs/2306.12001) (Hendrycks, Mazeika & Woodside, 2023)
groups risks into four categories. They're a useful map.

### 1. Malicious use

People deliberately using AI to cause harm:

- **Cyberattacks**: finding vulnerabilities and writing exploits faster than defenders can patch.
- **Weapons**: helping someone acquire chemical or biological weapons capability (often called *uplift*).
- **Disinformation and fraud**: personalised scams and propaganda at scale.

*How it's studied:* [dangerous capability evaluations](../methods/dangerous-capabilities.md) and
[red teaming](../methods/red-teaming.md).

### 2. AI race (competitive pressure)

Companies and countries competing to build and deploy AI first may cut safety corners, deploy systems before
they're well understood, or hand over more decisions to AI to keep up. Over time, this can lead to a **gradual
loss of human oversight**: decisions delegated to systems too fast or complex to check, with humans losing
the practical ability to correct course. Competition can also **concentrate power** in whoever controls the
most capable systems.

These risks are mainly addressed through [governance](governance.md).

### 3. Organisational risks (accidents)

Harm without bad intent from anyone, caused by how AI is developed and deployed: weak safety culture, leaked
model weights, a model released with untested capabilities, or an agent deleting the wrong files. As AI is
connected to more real systems, ordinary failures matter more. See [agent safety](../methods/agent-safety.md)
and the company safety frameworks under [governance](governance.md#company-safety-frameworks).

### 4. Rogue AIs (misalignment and loss of control)

The AI pursues goals that differ from what its designers intended. This isn't about AI "turning evil". It's
about the difficulty of specifying what we want and checking a system has actually learned it:

- A system rewarded for a measurable proxy can exploit the proxy instead
  ([reward hacking](alignment-concepts.md#reward-hacking-and-specification-gaming)).
- A system can learn a goal that worked in training but generalises wrongly
  ([goal misgeneralisation](alignment-concepts.md#goal-misgeneralisation)).
- A capable system with almost any goal may benefit from acquiring resources or avoiding shutdown
  ([instrumental convergence](alignment-concepts.md#instrumental-convergence-and-power-seeking)).
- A system might behave well while being watched and differently otherwise
  ([deceptive alignment](alignment-concepts.md#deceptive-alignment-and-scheming)).

Early versions of some of these behaviours have been demonstrated in today's models under controlled conditions.
See [alignment and propensity evaluations](../methods/alignment-propensity.md) and
[AI control](../methods/ai-control.md).

## Common objections, and replies

| Objection | A common reply |
| --- | --- |
| "We can just turn it off." | An autonomous system embedded in critical infrastructure, or copied many times, may be hard to turn off, and a capable misaligned system would have reasons to avoid it. |
| "It only predicts the next word." | The training objective doesn't limit what capabilities emerge. Today's models already write code, plan, and use tools. |
| "These are science-fiction worries." | Several failure modes (reward hacking, jailbreaks, prompt injection, strategic deception in tests) are already observed and measured. |
| "Present-day harms matter more." | Many researchers work on both. Many tools, such as evaluations, interpretability, and governance, help with both. |

Reasonable experts disagree on how likely and how near the most severe risks are. A useful habit is to keep
separate *what has been demonstrated*, *what is plausible*, and *what is speculative*.

## Key reading

- Bengio et al., [International AI Safety Report](https://arxiv.org/abs/2501.17805) (2025)
- Hendrycks, Mazeika & Woodside, [An Overview of Catastrophic AI Risks](https://arxiv.org/abs/2306.12001) (2023)
- Bengio et al., [Managing Extreme AI Risks amid Rapid Progress](https://arxiv.org/abs/2310.17688) (2023)
- Ngo, Chan & Mindermann, [The Alignment Problem from a Deep Learning Perspective](https://arxiv.org/abs/2209.00626) (2022)
- Carlsmith, [Is Power-Seeking AI an Existential Risk?](https://arxiv.org/abs/2206.13353) (2022)
- Grace et al., [Thousands of AI Authors on the Future of AI](https://arxiv.org/abs/2401.02843) (2024): a survey of what researchers expect.
- 80,000 Hours, [Preventing an AI-related catastrophe](https://80000hours.org/problem-profiles/artificial-intelligence/): a readable long-form introduction.

**Next:** [Key alignment concepts](alignment-concepts.md)
