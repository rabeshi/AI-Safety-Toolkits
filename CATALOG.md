# Resource catalogue

**82 resources across 17 categories.** The same catalogue, with quickstarts and method guides, is on the documentation website (see the README).

Links were checked against primary sources on 2026-10-27. Quickstart commands are copied from each project's own documentation; this hub has not run them. Check upstream licences before using code or data.

Levels: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced (editorial estimates of prerequisites).

- [Content safety](#content-safety) (9)
- [Red teaming](#red-teaming) (6)
- [Multimodal and embodied](#multimodal-and-embodied) (4)
- [Tool-using agents](#tool-using-agents) (7)
- [Specialized risk](#specialized-risk) (8)
- [Web and GUI agents](#web-and-gui-agents) (6)
- [Privacy](#privacy) (1)
- [Governance and research](#governance-and-research) (2)
- [Directories](#directories) (2)
- [Evaluation infrastructure](#evaluation-infrastructure) (8)
- [Refusal calibration](#refusal-calibration) (4)
- [Trustworthiness](#trustworthiness) (3)
- [Alignment data](#alignment-data) (3)
- [Bias and toxicity](#bias-and-toxicity) (6)
- [Factuality and hallucination](#factuality-and-hallucination) (3)
- [Prompt injection](#prompt-injection) (7)
- [Capability controls](#capability-controls) (3)

## Content safety

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R001 | **SALAD-Bench** | Benchmark | 🟡 Intermediate | Hierarchical evaluation of harmful requests and model safety. Safety taxonomy and evaluator choice affect conclusions. | [Paper](https://arxiv.org/abs/2402.05044)<br>[Code](https://github.com/OpenSafetyLab/SALAD-BENCH)<br>[Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data) |
| R005 | **SG-Bench** | Benchmark | 🟡 Intermediate | Evaluates LLM safety generalization across tasks and prompt types. A language-model safety benchmark; not specifically an agent benchmark. | [Paper](https://arxiv.org/abs/2410.21965)<br>[Code](https://github.com/MurrayTom/SG-Bench) |
| R038 | **HarmBench** | Benchmark | 🟡 Intermediate | Standardizes harmful-behavior evaluation and red-teaming comparisons. Attack coverage and classifier errors influence measured robustness. | [Paper](https://arxiv.org/abs/2402.04249)<br>[Code](https://github.com/centerforaisafety/HarmBench) |
| R039 | **JailbreakBench** | Benchmark | 🟡 Intermediate | Provides a reproducible benchmark for jailbreak robustness. Use the defined threat model and report attack budgets. | [Paper](https://arxiv.org/abs/2404.01318)<br>[Code](https://github.com/JailbreakBench/jailbreakbench)<br>[Docs](https://jailbreakbench.github.io/)<br>[Data](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors) |
| R044 | **Do-Not-Answer** | Dataset | 🟢 Beginner | Provides requests that responsible assistants should decline. Taxonomy and language coverage limit generalization. | [Paper](https://arxiv.org/abs/2308.13387)<br>[Code](https://github.com/Libr-AI/do-not-answer)<br>[Data](https://huggingface.co/datasets/LibrAI/do-not-answer) |
| R045 | **SafetyBench** | Benchmark | 🟢 Beginner | Evaluates safety understanding through multiple-choice questions. Knowledge of safe answers does not establish safe agent behavior. | [Paper](https://arxiv.org/abs/2309.07045)<br>[Code](https://github.com/thu-coai/SafetyBench)<br>[Data](https://huggingface.co/datasets/thu-coai/SafetyBench) |
| R048 | **ALERT** | Benchmark | 🟡 Intermediate | Evaluates safety through a taxonomy of red-teaming prompts. Synthetic and adversarial distributions may differ from deployment traffic. | [Paper](https://arxiv.org/abs/2404.08676)<br>[Code](https://github.com/Babelscape/ALERT)<br>[Data](https://huggingface.co/datasets/Babelscape/ALERT) |
| R049 | **AIR-Bench 2024** | Benchmark | 🟡 Intermediate | Evaluates safety against a policy-informed risk taxonomy. Policy grounding does not constitute a legal compliance determination. | [Paper](https://arxiv.org/abs/2407.17436)<br>[Code](https://github.com/stanford-crfm/air-bench-2024)<br>[Data](https://huggingface.co/datasets/stanford-crfm/air-bench-2024) |
| R050 | **S-Eval** | Benchmark | 🟡 Intermediate | Evaluates language-model safety using diversified test prompts. Prompt distribution and evaluator language coverage affect scores. | [Paper](https://arxiv.org/abs/2405.14191)<br>[Code](https://github.com/IS2Lab/S-Eval)<br>[Data](https://huggingface.co/datasets/IS2Lab/S-Eval) |

## Red teaming

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R002 | **h4rm3l** | Toolkit | 🔴 Advanced | Composes jailbreak attacks for adversarial safety assessment. Attack success depends on the attack budget and target configuration. | [Paper](https://arxiv.org/abs/2408.04811)<br>[Code](https://github.com/mdoumbouya/h4rm3l) |
| R019 | **WildTeaming** | Research toolkit | 🔴 Advanced | Studies scalable adversarial prompt generation from in-the-wild tactics. Adversarial prompt distribution is not representative user traffic. | [Paper](https://arxiv.org/abs/2406.18510)<br>[Code](https://github.com/allenai/wildteaming)<br>[Data](https://huggingface.co/datasets/allenai/wildjailbreak) |
| R030 | **PyRIT** | Toolkit | 🟡 Intermediate | Supports structured generative-AI red-teaming workflows. Moved from Azure/PyRIT to microsoft/PyRIT; define a threat model and campaign budget. | [Paper](https://arxiv.org/abs/2410.02828)<br>[Code](https://github.com/microsoft/PyRIT)<br>[Docs](https://azure.github.io/PyRIT/) |
| R031 | **garak** | Toolkit | 🟢 Beginner | Scans language models for multiple classes of vulnerabilities. Scanner findings need contextual review and reproduction. | [Paper](https://arxiv.org/abs/2406.11036)<br>[Code](https://github.com/NVIDIA/garak)<br>[Docs](https://reference.garak.ai/) |
| R036 | **EasyJailbreak** | Toolkit | 🔴 Advanced | Provides a framework for comparing jailbreak techniques. Compare attacks under equal query and compute budgets. | [Paper](https://arxiv.org/abs/2403.12171)<br>[Code](https://github.com/EasyJailbreak/EasyJailbreak) |
| R037 | **JailbreakEval** | Toolkit | 🟡 Intermediate | Provides evaluators for jailbreak outcomes. Evaluator accuracy is distinct from target-model safety. | [Paper](https://arxiv.org/abs/2406.09321)<br>[Code](https://github.com/ThuCCSLab/JailbreakEval) |

## Multimodal and embodied

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R003 | **SafeBench (multimodal)** | Benchmark | 🔴 Advanced | Evaluates multimodal harmful queries using collaborative judges. The linked code describes itself as an initial proof of concept. Distinct from autonomous-driving projects with the same name. | [Paper](https://arxiv.org/abs/2410.18927)<br>[Code](https://github.com/NY1024/SafeBench) |
| R006 | **SafeAgentBench** | Benchmark | 🔴 Advanced | Evaluates safe task planning by embodied language-model agents. Requires simulator setup; simulated physical safety has transfer limits. | [Paper](https://arxiv.org/abs/2412.13178)<br>[Code](https://github.com/shengyin1224/SafeAgentBench) |
| R073 | **MM-SafetyBench** | Benchmark | 🔴 Advanced | Evaluates multimodal safety under image-associated harmful requests. Image conditions and text-only baselines should be reported separately. | [Paper](https://arxiv.org/abs/2311.17600)<br>[Code](https://github.com/isXinLiu/MM-SafetyBench) |
| R074 | **MSSBench** | Benchmark | 🔴 Advanced | Evaluates safety decisions conditioned on visual situations. Context-dependent safety differs from purely textual harmfulness. | [Paper](https://arxiv.org/abs/2410.06172)<br>[Code](https://github.com/UCSB-AI/MSSBench) |

## Tool-using agents

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R004 | **Agent-SafetyBench** | Benchmark | 🟡 Intermediate | Tests agent safety across simulated tool environments. Simulated tools do not capture every deployment effect. | [Paper](https://arxiv.org/abs/2412.14470)<br>[Code](https://github.com/thu-coai/Agent-SafetyBench) |
| R008 | **ToolEmu / LM-Emulated Sandbox** | Framework | 🔴 Advanced | Emulates tool execution to identify risky agent actions. Emulator realism and evaluator agreement need validation. | [Paper](https://arxiv.org/abs/2309.15817)<br>[Code](https://github.com/ryoungj/ToolEmu) |
| R016 | **R-Judge** | Benchmark | 🟡 Intermediate | Evaluates recognition of safety risks in agent interaction records. Judging a recorded trajectory differs from acting safely. | [Paper](https://arxiv.org/abs/2401.10019)<br>[Code](https://github.com/Lordog/R-Judge) |
| R017 | **A Trembling House of Cards?** | Paper | 🔴 Advanced | Maps adversarial attacks against language agents. Research paper; the full title resolves the original shorthand. | [Paper](https://arxiv.org/abs/2402.10196) |
| R018 | **AgentHarm** | Benchmark | 🟡 Intermediate | Evaluates harmful multi-step tool use alongside benign counterparts. Read dataset-specific use terms and report agent capability alongside safety. | [Paper](https://arxiv.org/abs/2410.09024)<br>[Code](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm)<br>[Data](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) |
| R024 | **HAICOSYSTEM** | Framework | 🔴 Advanced | Simulates safety risks in multi-turn human-agent interactions. User and tool simulation introduce modeling assumptions. | [Paper](https://arxiv.org/abs/2409.16427)<br>[Code](https://github.com/XuhuiZhou/HAICOSYSTEM) |
| R025 | **OpenAgentSafety** | Framework | 🔴 Advanced | Evaluates safety with real tools in sandboxed multi-user interactions. Maintained project moved from sani903/OpenAgentSafety in August 2026; container infrastructure and trajectory review are required. | [Paper](https://arxiv.org/abs/2507.06134)<br>[Code](https://github.com/Open-Agent-Safety/OpenAgentSafety) |

## Specialized risk

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R007 | **ChemSafetyBench** | Benchmark | 🔴 Advanced | Studies chemistry-specific knowledge and safety behavior. Paper is the stable source; the author-linked code location needs separate availability verification. | [Paper](https://arxiv.org/abs/2411.16736) |
| R011 | **RedCode** | Benchmark | 🔴 Advanced | Evaluates risky code generation and execution by code agents. Execution tasks require disposable isolated environments. | [Paper](https://arxiv.org/abs/2411.07781)<br>[Code](https://github.com/AI-secure/RedCode) |
| R022 | **Frontier Models are Capable of In-context Scheming** | Paper | 🔴 Advanced | Investigates strategic deceptive behavior in controlled scenarios. Resolves the original Frontier Models label; not a general capabilities suite. | [Paper](https://arxiv.org/abs/2412.04984) |
| R063 | **WMDP** | Benchmark | 🔴 Advanced | Uses expert-written questions as proxies for hazardous domain knowledge. Knowledge proxies are not direct measurements of real-world harmful capability. | [Paper](https://arxiv.org/abs/2403.03218)<br>[Code](https://github.com/centerforaisafety/wmdp)<br>[Data](https://huggingface.co/datasets/cais/wmdp) |
| R064 | **CyberSecEval** | Benchmark suite | 🔴 Advanced | Evaluates cybersecurity-relevant risks and capabilities. Select the relevant component; execute only in authorized isolated settings. | [Paper](https://arxiv.org/abs/2312.04724)<br>[Code](https://github.com/meta-llama/PurpleLlama) |
| R065 | **Cybench** | Benchmark | 🔴 Advanced | Evaluates cybersecurity task capabilities in controlled environments. Capability benchmark; task performance is not itself malicious intent. | [Paper](https://arxiv.org/abs/2408.08926)<br>[Code](https://github.com/andyzorigin/cybench) |
| R075 | **MACHIAVELLI** | Benchmark | 🔴 Advanced | Evaluates harmful and power-seeking behavior in text-based decision environments. Game outcomes are proxies; compare reward and harm separately. | [Paper](https://arxiv.org/abs/2304.03279)<br>[Code](https://github.com/aypan17/machiavelli) |
| R082 | **Agentic Misalignment** | Research toolkit | 🔴 Advanced | Studies misaligned behavior in controlled organizational scenarios. Designed stress tests; observed rates do not estimate deployment prevalence. | [Paper](https://arxiv.org/abs/2510.05179)<br>[Code](https://github.com/anthropic-experimental/agentic-misalignment) |

## Web and GUI agents

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R009 | **AdvWeb / AdvAgent** | Research toolkit | 🔴 Advanced | Studies adversarial manipulation of vision-language web agents. Originally called AdvWeb; the current paper title uses AdvAgent. Research framework rather than a standard safety leaderboard. | [Paper](https://arxiv.org/abs/2410.17401)<br>[Code](https://github.com/AI-secure/AdvAgent) |
| R010 | **Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents** | Paper | 🔴 Advanced | Studies whether chatbot refusal transfers to browser-agent behavior. Research paper title, not a generic refusal-training toolkit. | [Paper](https://arxiv.org/abs/2410.13886)<br>[Code](https://github.com/scaleapi/browser-art) |
| R012 | **From Interaction to Impact** | Paper | 🔴 Advanced | Studies safety-relevant consequences of mobile UI operations. A research study; not a general-purpose interaction benchmark. | [Paper](https://arxiv.org/abs/2410.09006) |
| R014 | **Dissecting Adversarial Robustness of Multimodal LM Agents** | Paper | 🔴 Advanced | Studies adversarial robustness of multimodal agents. An abbreviated paper title in the original list. | [Paper](https://arxiv.org/abs/2406.12814)<br>[Code](https://github.com/ChenWu98/agent-attack) |
| R021 | **ST-WebAgentBench** | Benchmark | 🔴 Advanced | Evaluates web-agent safety and trustworthiness under policies. Environment state and policy compliance matter beyond task completion. | [Paper](https://arxiv.org/abs/2410.06703)<br>[Code](https://github.com/segev-shlomov/ST-WebAgentBench) |
| R023 | **SafeArena** | Benchmark | 🔴 Advanced | Measures deliberate misuse of autonomous web agents. Paired benign tasks help distinguish inability from refusal. | [Paper](https://arxiv.org/abs/2503.04957)<br>[Code](https://github.com/McGill-NLP/safearena) |

## Privacy

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R013 | **PrivacyLens** | Benchmark | 🟡 Intermediate | Evaluates contextual privacy norms and agent information disclosure. Privacy depends on context; question answers and actual actions may differ. | [Paper](https://arxiv.org/abs/2409.00138)<br>[Code](https://github.com/SALT-NLP/PrivacyLens) |

## Governance and research

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R015 | **Infrastructure for AI Agents** | Paper | 🟡 Intermediate | Discusses infrastructure for accountable agent deployment. Conceptual infrastructure proposal, not a runnable benchmark. | [Paper](https://arxiv.org/abs/2501.10114) |
| R077 | **COMPL-AI** | Benchmark suite | 🔴 Advanced | Maps technical LLM evaluations to aspects of AI regulation. Technical scores are not legal advice or proof of compliance. | [Paper](https://arxiv.org/abs/2410.07959)<br>[Code](https://github.com/compl-ai/compl-ai) |

## Directories

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R020 | **SafetyPrompts** | Directory | 🟢 Beginner | Indexes open datasets for evaluating and improving LLM safety. The official catalogue is archived and states it has not been updated since May 2025; useful as a historical index. | [Paper](https://arxiv.org/abs/2404.05399)<br>[Docs](https://safetyprompts.com/) |
| R078 | **Awesome Large Model Safety** | Directory | 🟢 Beginner | Provides a broad safety research bibliography and benchmark index. A bibliography, not a common execution interface. | [Paper](https://arxiv.org/abs/2502.05206)<br>[Code](https://github.com/xingjunm/Awesome-Large-Model-Safety) |

## Evaluation infrastructure

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R026 | **Inspect AI** | Framework | 🟢 Beginner | Defines datasets, solvers, scorers, tasks, and evaluation logs. Framework rather than a safety score or dataset. | [Code](https://github.com/UKGovernmentBEIS/inspect_ai)<br>[Docs](https://inspect.aisi.org.uk/) |
| R027 | **Inspect Evals** | Evaluation collection | 🟢 Beginner | Provides reusable evaluation implementations and a registry. Individual evaluations have separate requirements and dataset terms. | [Code](https://github.com/UKGovernmentBEIS/inspect_evals)<br>[Docs](https://ukgovernmentbeis.github.io/inspect_evals/) |
| R028 | **lm-evaluation-harness** | Framework | 🟡 Intermediate | Runs standardized language-model evaluation tasks. Broad capability evaluation; safety coverage depends on selected tasks. | [Paper](https://arxiv.org/abs/2405.14782)<br>[Code](https://github.com/EleutherAI/lm-evaluation-harness) |
| R029 | **HELM** | Framework | 🟡 Intermediate | Supports transparent multi-metric language-model evaluation. The repository states HELM entered maintenance mode in June 2026. Scenarios and adapters determine comparability. | [Paper](https://arxiv.org/abs/2211.09110)<br>[Code](https://github.com/stanford-crfm/helm)<br>[Docs](https://crfm-helm.readthedocs.io/) |
| R032 | **promptfoo** | Toolkit | 🟢 Beginner | Supports prompt evaluation, comparisons, and red-team workflows. Configure your own application context and assertions. | [Code](https://github.com/promptfoo/promptfoo)<br>[Docs](https://www.promptfoo.dev/docs/red-team/) |
| R033 | **Giskard** | Toolkit | 🟡 Intermediate | Tests language-model applications for quality and risk. Application tests are not a universal model safety certification. | [Code](https://github.com/Giskard-AI/giskard-oss)<br>[Docs](https://docs.giskard.ai/) |
| R034 | **DeepEval** | Framework | 🟢 Beginner | Provides evaluation metrics and tests for LLM applications. Judge-based metrics require calibration for your use case. | [Code](https://github.com/confident-ai/deepeval)<br>[Docs](https://deepeval.com/docs/getting-started) |
| R035 | **Moonshot** | Toolkit | 🟡 Intermediate | Combines LLM benchmarking and red-teaming workflows. Individual recipes vary in dependencies and scope. | [Code](https://github.com/aiverify-foundation/moonshot)<br>[Docs](https://aiverify-foundation.github.io/moonshot/) |

## Refusal calibration

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R040 | **StrongREJECT** | Benchmark and evaluator | 🟡 Intermediate | Assesses harmful-request fulfillment beyond superficial refusal wording. Judge scores require validation on the target distribution. | [Paper](https://arxiv.org/abs/2402.10260)<br>[Code](https://github.com/dsbowen/strong_reject) |
| R041 | **SORRY-Bench** | Benchmark | 🟡 Intermediate | Evaluates safety refusal across a structured harmful-request taxonomy. Refusal on harmful requests does not establish helpfulness on safe ones. | [Paper](https://arxiv.org/abs/2406.14598)<br>[Code](https://github.com/SORRY-Bench/SORRY-Bench)<br>[Data](https://huggingface.co/datasets/sorry-bench/sorry-bench-202406) |
| R042 | **XSTest** | Benchmark | 🟢 Beginner | Tests exaggerated refusals on safe prompts with unsafe contrasts. A focused diagnostic suite rather than complete safety coverage. | [Paper](https://arxiv.org/abs/2308.01263)<br>[Code](https://github.com/paul-rottger/xstest)<br>[Data](https://huggingface.co/datasets/Paul/XSTest) |
| R043 | **OR-Bench** | Benchmark | 🟢 Beginner | Evaluates over-refusal on benign prompts that appear sensitive. Pair with harmful-request tests to measure both error directions. | [Paper](https://arxiv.org/abs/2405.20947)<br>[Code](https://github.com/justincui03/or-bench)<br>[Data](https://huggingface.co/datasets/bench-llm/or-bench) |

## Trustworthiness

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R046 | **DecodingTrust** | Benchmark suite | 🟡 Intermediate | Evaluates multiple dimensions of language-model trustworthiness. Report individual dimensions rather than treating trust as one number. | [Paper](https://arxiv.org/abs/2306.11698)<br>[Code](https://github.com/AI-secure/DecodingTrust) |
| R047 | **TrustLLM** | Benchmark suite | 🟡 Intermediate | Evaluates language models across several trustworthiness dimensions. Component metrics and underlying datasets have different interpretations. | [Paper](https://arxiv.org/abs/2401.05561)<br>[Code](https://github.com/HowieHwong/TrustLLM) |
| R076 | **Sycophancy evaluations** | Evaluation collection | 🟡 Intermediate | Examines agreement with users at the expense of truthful judgment. Research evaluations; selected tasks do not cover every form of deception. | [Paper](https://arxiv.org/abs/2212.09251)<br>[Code](https://github.com/anthropics/evals) |

## Alignment data

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R051 | **BeaverTails** | Dataset | 🟢 Beginner | Provides safety annotations and preference data for assistant responses. Training data; define a clean held-out evaluation split before testing. | [Paper](https://arxiv.org/abs/2307.04657)<br>[Code](https://github.com/PKU-Alignment/beavertails)<br>[Data](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) |
| R052 | **PKU-SafeRLHF** | Dataset | 🟡 Intermediate | Provides helpfulness and safety preference annotations. Repository includes training infrastructure; avoid train-test overlap. | [Paper](https://arxiv.org/abs/2310.12773)<br>[Code](https://github.com/PKU-Alignment/safe-rlhf)<br>[Data](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF) |
| R053 | **Anthropic HH-RLHF** | Dataset | 🟢 Beginner | Provides human preference data for helpfulness and harmlessness. Historical alignment data, not a current universal benchmark. The authors direct users from the deprecated GitHub repository to this dataset. | [Paper](https://arxiv.org/abs/2204.05862)<br>[Data](https://huggingface.co/datasets/Anthropic/hh-rlhf) |

## Bias and toxicity

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R054 | **RealToxicityPrompts** | Dataset | 🟢 Beginner | Tests toxicity risks in language-model continuations. Toxicity detectors may encode biases and miss contextual harms. | [Paper](https://arxiv.org/abs/2009.11462)<br>[Code](https://github.com/allenai/real-toxicity-prompts)<br>[Data](https://huggingface.co/datasets/allenai/real-toxicity-prompts) |
| R055 | **ToxiGen** | Dataset | 🟡 Intermediate | Contains implicit toxic and benign language about minority groups. Dataset labels and group coverage require contextual interpretation. | [Paper](https://arxiv.org/abs/2203.09509)<br>[Code](https://github.com/microsoft/TOXIGEN)<br>[Data](https://huggingface.co/datasets/toxigen/toxigen-data) |
| R056 | **BBQ** | Benchmark | 🟢 Beginner | Evaluates social bias in question answering under ambiguity. Question-answering bias differs from deployment discrimination. | [Paper](https://arxiv.org/abs/2110.08193)<br>[Code](https://github.com/nyu-mll/BBQ) |
| R057 | **BOLD** | Dataset | 🟡 Intermediate | Provides prompts for studying bias in open-ended generation. Results depend on the generation and measurement pipeline. | [Paper](https://arxiv.org/abs/2101.11718)<br>[Code](https://github.com/amazon-science/bold)<br>[Data](https://huggingface.co/datasets/AmazonScience/bold) |
| R058 | **CrowS-Pairs** | Dataset | 🟡 Intermediate | Tests stereotypical associations using paired sentences. The repository flags data-reliability concerns; examine its linked critiques before using paired-sentence scores. | [Paper](https://arxiv.org/abs/2010.00133)<br>[Code](https://github.com/nyu-mll/crows-pairs) |
| R059 | **StereoSet** | Benchmark | 🟡 Intermediate | Measures stereotypical associations with language-modeling controls. Association scores should not be equated with all fairness properties. | [Paper](https://arxiv.org/abs/2004.09456)<br>[Code](https://github.com/moinnadeem/StereoSet)<br>[Data](https://huggingface.co/datasets/McGill-NLP/stereoset) |

## Factuality and hallucination

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R060 | **TruthfulQA** | Benchmark | 🟢 Beginner | Tests susceptibility to common human misconceptions. Adjacent reliability measure; truthfulness does not establish overall safety. | [Paper](https://arxiv.org/abs/2109.07958)<br>[Code](https://github.com/sylinrl/TruthfulQA)<br>[Data](https://huggingface.co/datasets/truthfulqa/truthful_qa) |
| R061 | **SimpleQA** | Benchmark | 🟢 Beginner | Evaluates short factual question answering. Adjacent reliability measure. The reference simple-evals repository announces it will not be updated for new models or results; pin its revision. | [Paper](https://arxiv.org/abs/2411.04368)<br>[Code](https://github.com/openai/simple-evals) |
| R062 | **HaluEval** | Benchmark | 🟡 Intermediate | Evaluates hallucination recognition in generated text. Recognizing hallucinations differs from avoiding them during generation. | [Paper](https://arxiv.org/abs/2305.11747)<br>[Code](https://github.com/RUCAIBox/HaluEval)<br>[Data](https://huggingface.co/datasets/pminervini/HaluEval) |

## Prompt injection

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R066 | **AgentDojo** | Benchmark and environment | 🟡 Intermediate | Evaluates prompt-injection attacks and defenses for tool-using agents. Report utility and attack success under a fixed attacker model. | [Paper](https://arxiv.org/abs/2406.13352)<br>[Code](https://github.com/ethz-spylab/agentdojo)<br>[Docs](https://agentdojo.spylab.ai/) |
| R067 | **InjecAgent** | Benchmark | 🟡 Intermediate | Evaluates indirect prompt injection in tool-integrated agents. Static tool-context tests have limits for long interactive workflows. | [Paper](https://arxiv.org/abs/2403.02691)<br>[Code](https://github.com/uiuc-kang-lab/InjecAgent) |
| R068 | **Agent Security Bench (ASB)** | Benchmark | 🔴 Advanced | Studies attacks and defenses across agent scenarios and tools. Distinct from Agent-SafetyBench; configure attack and defense settings explicitly. | [Paper](https://arxiv.org/abs/2410.02644)<br>[Code](https://github.com/agiresearch/ASB) |
| R069 | **WASP** | Benchmark | 🔴 Advanced | Evaluates web-agent security against prompt injection. The official repository is archived. Web environment setup and attacker access define the threat model. | [Paper](https://arxiv.org/abs/2504.18575)<br>[Code](https://github.com/facebookresearch/wasp) |
| R070 | **Tensor Trust** | Dataset and benchmark | 🟡 Intermediate | Studies prompt injection through human-authored attack and defense examples. Game-derived interactions may not represent production tool use. | [Paper](https://arxiv.org/abs/2311.01011)<br>[Code](https://github.com/HumanCompatibleAI/tensor-trust) |
| R071 | **BIPIA** | Benchmark | 🟡 Intermediate | Evaluates indirect prompt injection across application contexts. Attack surfaces and retrieval context should match your application. | [Paper](https://arxiv.org/abs/2312.14197)<br>[Code](https://github.com/microsoft/BIPIA) |
| R072 | **LLMail-Inject** | Dataset and challenge | 🔴 Advanced | Studies indirect prompt injection against email assistants. Challenge-derived attacks need evaluation on held-out system configurations. | [Paper](https://arxiv.org/abs/2506.09956)<br>[Code](https://github.com/microsoft/llmail-inject-challenge) |

## Capability controls

| ID | Resource | Type | Level | What it does | Links |
| --- | --- | --- | --- | --- | --- |
| R079 | **WebArena** | Benchmark and environment | 🔴 Advanced | Provides realistic web tasks for measuring agent capability. Capability baseline; not a safety benchmark by itself. | [Paper](https://arxiv.org/abs/2307.13854)<br>[Code](https://github.com/web-arena-x/webarena) |
| R080 | **OSWorld** | Benchmark and environment | 🔴 Advanced | Evaluates agents on computer-use tasks in operating systems. Capability baseline; requires isolated desktop environments. | [Paper](https://arxiv.org/abs/2404.07972)<br>[Code](https://github.com/xlang-ai/OSWorld) |
| R081 | **AgentBench** | Benchmark | 🔴 Advanced | Evaluates language-model agents across interactive environments. Useful control for agent capability; does not establish safety. | [Paper](https://arxiv.org/abs/2308.03688)<br>[Code](https://github.com/THUDM/AgentBench) |
