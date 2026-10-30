# Agent and tool-use safety

!!! abstract "In one sentence"
    Give an AI agent tools in a safe, fake environment and check whether its *actions* are harmful, risky, or against policy.

## Why it matters

A chatbot can only say harmful things; an agent can *do* them: delete files, send money, post online, run code.
Research repeatedly shows that safety training on chat doesn't fully carry over to agents. For example,
[models that refuse in chat can be jailbroken as browser agents](https://arxiv.org/abs/2410.13886). Agents also
cause harm without anyone attacking them, by taking careless, irreversible actions.

## The main approaches

| Approach | What's simulated | Example | Trade-off |
| --- | --- | --- | --- |
| **Judge recorded trajectories** | Nothing; you label existing agent logs | R-Judge | Cheap, but doesn't test a live agent |
| **LLM-emulated tools** | An LLM pretends to be the tools | ToolEmu, Agent-SafetyBench | Many scenarios quickly; emulation can be unrealistic |
| **Scripted fake tools** | Python functions with fake data | AgentHarm, AgentDojo | Reproducible; less realistic |
| **Real sandboxed environments** | Real apps in Docker (websites, OS, code) | OpenAgentSafety, SafeArena, ST-WebAgentBench | Most realistic; heavy to set up |

## How it works

1. **Set up an environment** the agent can act in safely, with no real credentials or external effects.
2. **Write tasks**: harmful ones (should refuse or stop), harmless ones (should complete), and ambiguous ones
   (should ask or act carefully).
3. **Run the agent** and record the full **trajectory**: every message, tool call, and result.
4. **Score outcomes**: check the final environment state and the trajectory for policy violations.
5. **Report safety and capability together**, because an agent that fails every task looks "safe" for the wrong reason.

## A tiny example

> **Task:** "Clean up my disk, it's full."
> **Risky action:** `rm -rf ~/Documents` (irreversible data loss the user didn't ask for).
> **Safe behaviour:** list large files and ask before deleting.

## What to measure

- **Harmful-task completion rate** and **refusal rate** on harmful tasks.
- **Benign-task completion rate**, the capability control.
- **Policy-compliant completion**: completed *without* violating a rule (ST-WebAgentBench calls this CuP).
- **Risky-action rate** on ambiguous tasks.

## Common mistakes

- **Confusing incompetence with safety.** AgentHarm explicitly pairs harmful tasks with benign twins to catch this.
- **Only reading the final answer.** Harm happens in the middle of a trajectory.
- **Running agents with real access.** Always sandbox: disposable containers, fake accounts, no production credentials.
- **Too few runs.** Agents are high-variance; repeat each task.

## Toolkits for this method

<!-- BEGIN toolkits:agent-safety -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [Agent-SafetyBench](../toolkits/tool-using-agents.md#r004) | Tests agent safety across simulated tool environments. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2412.14470) · [Code](https://github.com/thu-coai/Agent-SafetyBench) |
| [AgentDojo](../toolkits/prompt-injection.md#r066) | Evaluates prompt-injection attacks and defenses for tool-using agents. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2406.13352) · [Code](https://github.com/ethz-spylab/agentdojo) · [Docs](https://agentdojo.spylab.ai/) |
| [AgentHarm](../toolkits/tool-using-agents.md#r018) | Evaluates harmful multi-step tool use alongside benign counterparts. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2410.09024) · [Code](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm) · [Data](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) |
| [Infrastructure for AI Agents](../toolkits/governance-and-research.md#r015) | Discusses infrastructure for accountable agent deployment. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2501.10114) |
| [InjecAgent](../toolkits/prompt-injection.md#r067) | Evaluates indirect prompt injection in tool-integrated agents. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2403.02691) · [Code](https://github.com/uiuc-kang-lab/InjecAgent) |
| [PrivacyLens](../toolkits/privacy.md#r013) | Evaluates contextual privacy norms and agent information disclosure. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2409.00138) · [Code](https://github.com/SALT-NLP/PrivacyLens) |
| [R-Judge](../toolkits/tool-using-agents.md#r016) | Evaluates recognition of safety risks in agent interaction records. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2401.10019) · [Code](https://github.com/Lordog/R-Judge) |
| [A Trembling House of Cards?](../toolkits/tool-using-agents.md#r017) | Maps adversarial attacks against language agents. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2402.10196) |
| [Agent Security Bench (ASB)](../toolkits/prompt-injection.md#r068) | Studies attacks and defenses across agent scenarios and tools. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.02644) · [Code](https://github.com/agiresearch/ASB) |
| [AgentBench](../toolkits/capability-controls.md#r081) | Evaluates language-model agents across interactive environments. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2308.03688) · [Code](https://github.com/THUDM/AgentBench) |
| [Agentic Misalignment](../toolkits/specialized-risk.md#r082) | Studies misaligned behavior in controlled organizational scenarios. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2510.05179) · [Code](https://github.com/anthropic-experimental/agentic-misalignment) |
| [Cybench](../toolkits/specialized-risk.md#r065) | Evaluates cybersecurity task capabilities in controlled environments. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2408.08926) · [Code](https://github.com/andyzorigin/cybench) |
| [From Interaction to Impact](../toolkits/web-and-gui-agents.md#r012) | Studies safety-relevant consequences of mobile UI operations. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.09006) |
| [HAICOSYSTEM](../toolkits/tool-using-agents.md#r024) | Simulates safety risks in multi-turn human-agent interactions. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2409.16427) · [Code](https://github.com/XuhuiZhou/HAICOSYSTEM) |
| [OpenAgentSafety](../toolkits/tool-using-agents.md#r025) | Evaluates safety with real tools in sandboxed multi-user interactions. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2507.06134) · [Code](https://github.com/Open-Agent-Safety/OpenAgentSafety) |
| [OSWorld](../toolkits/capability-controls.md#r080) | Evaluates agents on computer-use tasks in operating systems. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2404.07972) · [Code](https://github.com/xlang-ai/OSWorld) |
| [RedCode](../toolkits/specialized-risk.md#r011) | Evaluates risky code generation and execution by code agents. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2411.07781) · [Code](https://github.com/AI-secure/RedCode) |
| [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](../toolkits/web-and-gui-agents.md#r010) | Studies whether chatbot refusal transfers to browser-agent behavior. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.13886) · [Code](https://github.com/scaleapi/browser-art) |
| [SafeAgentBench](../toolkits/multimodal-and-embodied.md#r006) | Evaluates safe task planning by embodied language-model agents. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2412.13178) · [Code](https://github.com/shengyin1224/SafeAgentBench) |
| [SafeArena](../toolkits/web-and-gui-agents.md#r023) | Measures deliberate misuse of autonomous web agents. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2503.04957) · [Code](https://github.com/McGill-NLP/safearena) |
| [ST-WebAgentBench](../toolkits/web-and-gui-agents.md#r021) | Evaluates web-agent safety and trustworthiness under policies. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2410.06703) · [Code](https://github.com/segev-shlomov/ST-WebAgentBench) |
| [ToolEmu / LM-Emulated Sandbox](../toolkits/tool-using-agents.md#r008) | Emulates tool execution to identify risky agent actions. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2309.15817) · [Code](https://github.com/ryoungj/ToolEmu) |
| [WASP](../toolkits/prompt-injection.md#r069) | Evaluates web-agent security against prompt injection. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2504.18575) · [Code](https://github.com/facebookresearch/wasp) |
| [WebArena](../toolkits/capability-controls.md#r079) | Provides realistic web tasks for measuring agent capability. | 🔴 Advanced | [Paper](https://arxiv.org/abs/2307.13854) · [Code](https://github.com/web-arena-x/webarena) |
<!-- END toolkits -->

## Key papers

- Ruan et al., [Identifying the Risks of LM Agents with an LM-Emulated Sandbox (ToolEmu)](https://arxiv.org/abs/2309.15817) (2023)
- Andriushchenko et al., [AgentHarm](https://arxiv.org/abs/2410.09024) (2024)
- Kumar et al., [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886) (2024)
- Vijayvargiya et al., [OpenAgentSafety](https://arxiv.org/abs/2507.06134) (2025)

## Try it

`inspect eval inspect_evals/agentharm --limit 10` and `inspect eval inspect_evals/agentharm_benign --limit 10`,
then compare. See [Tutorial 3](../tutorials/03-run-a-benchmark.md).
