# Mapping the original 25 resources

All original entries are retained. Several labels were shortened paper titles. The correspondence was established from Table 1 and the references of [OpenAgentSafety](https://arxiv.org/abs/2507.06134), then checked against individual sources.

| Original number | Identified resource and source | Type | Clarification |
| --- | --- | --- | --- |
| 1 | [SALAD-Bench](https://github.com/OpenSafetyLab/SALAD-BENCH) | Benchmark | Safety taxonomy and evaluator choice affect conclusions. |
| 2 | [h4rm3l](https://github.com/mdoumbouya/h4rm3l) | Toolkit | Attack success depends on the attack budget and target configuration. |
| 3 | [SafeBench (multimodal)](https://github.com/NY1024/SafeBench) | Benchmark | The linked code describes itself as an initial proof of concept. Distinct from autonomous-driving projects with the same name. |
| 4 | [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) | Benchmark | Simulated tools do not capture every deployment effect. |
| 5 | [SG-Bench](https://github.com/MurrayTom/SG-Bench) | Benchmark | A language-model safety benchmark; not specifically an agent benchmark. |
| 6 | [SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench) | Benchmark | Requires simulator setup; simulated physical safety has transfer limits. |
| 7 | [ChemSafetyBench](https://arxiv.org/abs/2411.16736) | Benchmark | Paper is the stable source; the author-linked code location needs separate availability verification. |
| 8 | [ToolEmu / LM-Emulated Sandbox](https://github.com/ryoungj/ToolEmu) | Framework | Emulator realism and evaluator agreement need validation. |
| 9 | [AdvWeb / AdvAgent](https://arxiv.org/abs/2410.17401) | Research toolkit | Originally called AdvWeb; the current paper title uses AdvAgent. Research framework rather than a standard safety leaderboard. |
| 10 | [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886) | Paper | Research paper title, not a generic refusal-training toolkit. |
| 11 | [RedCode](https://github.com/AI-secure/RedCode) | Benchmark | Execution tasks require disposable isolated environments. |
| 12 | [From Interaction to Impact](https://arxiv.org/abs/2410.09006) | Paper | A research study; not a general-purpose interaction benchmark. |
| 13 | [PrivacyLens](https://github.com/SALT-NLP/PrivacyLens) | Benchmark | Privacy depends on context; question answers and actual actions may differ. |
| 14 | [Dissecting Adversarial Robustness of Multimodal LM Agents](https://arxiv.org/abs/2406.12814) | Paper | An abbreviated paper title in the original list. |
| 15 | [Infrastructure for AI Agents](https://arxiv.org/abs/2501.10114) | Paper | Conceptual infrastructure proposal, not a runnable benchmark. |
| 16 | [R-Judge](https://github.com/Lordog/R-Judge) | Benchmark | Judging a recorded trajectory differs from acting safely. |
| 17 | [A Trembling House of Cards?](https://arxiv.org/abs/2402.10196) | Paper | Research paper; the full title resolves the original shorthand. |
| 18 | [AgentHarm](https://ukgovernmentbeis.github.io/inspect_evals/evals/agentharm/) | Benchmark | Read dataset-specific use terms and report agent capability alongside safety. |
| 19 | [WildTeaming](https://github.com/allenai/wildteaming) | Research toolkit | Adversarial prompt distribution is not representative user traffic. |
| 20 | [SafetyPrompts](https://safetyprompts.com/) | Directory | The official catalogue is archived and states it has not been updated since May 2025; useful as a historical index. |
| 21 | [ST-WebAgentBench](https://github.com/segev-shlomov/ST-WebAgentBench) | Benchmark | Environment state and policy compliance matter beyond task completion. |
| 22 | [Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984) | Paper | Resolves the original Frontier Models label; not a general capabilities suite. |
| 23 | [SafeArena](https://github.com/McGill-NLP/safearena) | Benchmark | Paired benign tasks help distinguish inability from refusal. |
| 24 | [HAICOSYSTEM](https://arxiv.org/abs/2409.16427) | Framework | User and tool simulation introduce modeling assumptions. |
| 25 | [OpenAgentSafety](https://github.com/Open-Agent-Safety/OpenAgentSafety) | Framework | Maintained project moved from sani903/OpenAgentSafety in August 2026; container infrastructure and trajectory review are required. |

In particular, SG-Bench evaluates LLM safety generalization across tasks and prompt types. SafeBench here refers to the multimodal project, not an autonomous-driving benchmark. The “Frontier Models” entry is the in-context scheming paper, and “Infrastructure for AI” is a conceptual infrastructure paper.
