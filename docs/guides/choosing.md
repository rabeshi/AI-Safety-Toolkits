# Choosing a resource

Start from the question you want answered, not from a tool you've heard of. Find your question below, read the
matching method guide, and then pick from its candidates.

| Your question | Method guide | Candidate resources | What else you need |
| --- | --- | --- | --- |
| Does the model help with harmful requests? | [Harmful requests](../methods/harmful-requests.md) | [HarmBench](../toolkits/content-safety.md#r038), [SORRY-Bench](../toolkits/refusal-calibration.md#r041), [SALAD-Bench](../toolkits/content-safety.md#r001), [ALERT](../toolkits/content-safety.md#r048) | A written policy, attack budget, calibrated judge |
| Does it refuse harmless requests? | [Harmful requests](../methods/harmful-requests.md) | [XSTest](../toolkits/refusal-calibration.md#r042), [OR-Bench](../toolkits/refusal-calibration.md#r043) | Unsafe contrasts and a helpfulness measure |
| Can attackers jailbreak it? | [Red teaming](../methods/red-teaming.md) | [garak](../toolkits/red-teaming.md#r031), [PyRIT](../toolkits/red-teaming.md#r030), [JailbreakBench](../toolkits/content-safety.md#r039) | A threat model and a stated budget |
| Does safety hold across task formats? | [Harmful requests](../methods/harmful-requests.md) | [SG-Bench](../toolkits/content-safety.md#r005) | Matched comparisons, per-category analysis |
| Can untrusted content hijack tool use? | [Prompt injection](../methods/prompt-injection.md) | [AgentDojo](../toolkits/prompt-injection.md#r066), [InjecAgent](../toolkits/prompt-injection.md#r067), [BIPIA](../toolkits/prompt-injection.md#r071), [WASP](../toolkits/prompt-injection.md#r069) | Attacker-access assumptions, utility controls |
| Does an agent leak private information? | [Privacy](../methods/privacy.md) | [PrivacyLens](../toolkits/privacy.md#r013) | Context-specific disclosure rules |
| Does it misuse a browser? | [Agent safety](../methods/agent-safety.md) | [SafeArena](../toolkits/web-and-gui-agents.md#r023), [ST-WebAgentBench](../toolkits/web-and-gui-agents.md#r021) | Local websites, reproducible state |
| Does it take unsafe multi-step actions? | [Agent safety](../methods/agent-safety.md) | [AgentHarm](../toolkits/tool-using-agents.md#r018), [Agent-SafetyBench](../toolkits/tool-using-agents.md#r004), [OpenAgentSafety](../toolkits/tool-using-agents.md#r025), [ToolEmu](../toolkits/tool-using-agents.md#r008) | Full traces, tool permissions, benign twins |
| Is physical task planning safe? | [Multimodal](../methods/multimodal.md) | [SafeAgentBench](../toolkits/multimodal-and-embodied.md#r006) | Simulator setup; clear limits on real-world transfer |
| Could it help with cyber, chemical, or biological harm? | [Dangerous capabilities](../methods/dangerous-capabilities.md) | [WMDP](../toolkits/specialized-risk.md#r063), [Cybench](../toolkits/specialized-risk.md#r065), [CyberSecEval](../toolkits/specialized-risk.md#r064), [RedCode](../toolkits/specialized-risk.md#r011) | Domain experts; strong elicitation; sandboxing |
| Is it honest? Does it scheme or flatter? | [Alignment and propensity](../methods/alignment-propensity.md) | [Sycophancy evals](../toolkits/trustworthiness.md#r076), [MACHIAVELLI](../toolkits/specialized-risk.md#r075), [Agentic Misalignment](../toolkits/specialized-risk.md#r082) | Careful transcript review; caution about artificial settings |
| Is it biased or toxic? | [Bias and toxicity](../methods/bias-toxicity.md) | [BBQ](../toolkits/bias-and-toxicity.md#r056), [ToxiGen](../toolkits/bias-and-toxicity.md#r055), [RealToxicityPrompts](../toolkits/bias-and-toxicity.md#r054) | Population coverage relevant to your users |
| Does it make things up? | [Factuality](../methods/factuality.md) | [SimpleQA](../toolkits/factuality-and-hallucination.md#r061), [TruthfulQA](../toolkits/factuality-and-hallucination.md#r060), [HaluEval](../toolkits/factuality-and-hallucination.md#r062) | Abstention handling |
| How does it look across many risks or a regulation? | [Holistic suites](../methods/holistic.md) | [HELM](../toolkits/evaluation-infrastructure.md#r029), [DecodingTrust](../toolkits/trustworthiness.md#r046), [AIR-Bench](../toolkits/content-safety.md#r049), [COMPL-AI](../toolkits/governance-and-research.md#r077) | Per-dimension reporting |

## Narrow your shortlist

For each candidate, check:

- [ ] Does it test the **same kind of system** as yours (bare model, app, agent)?
- [ ] Does it test the **risk** you care about, under a **policy** you agree with?
- [ ] Can you **access the data** under terms you can follow?
- [ ] Can you **run it** with your budget, hardware, and skills? (Look for a quickstart ✅ in the catalogue.)
- [ ] Does its **scorer** measure the behaviour you care about, not just refusal wording?
- [ ] Does it include **benign controls** so incompetence isn't mistaken for safety?
- [ ] Is it **independent** of data you used to build or tune your system?

Difficulty levels and setup-effort estimates in this hub are editorial. A beginner can read an advanced
project's paper long before attempting its infrastructure. Paper-only entries are for understanding and study
design; they aren't installation targets.
