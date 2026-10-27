# Resource catalogue

**82 resources across 17 categories.** Primary-source review: October 27, 2026. External execution has not been tested.

Use [the selection guide](docs/SELECTION_GUIDE.md) to choose a shortlist. Levels and effort estimates are editorial; a paper or directory is not an executable toolkit. Primary-source links support each description; review upstream code and data terms separately.

## Categories

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

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R001](#r001) | [SALAD-Bench](https://github.com/OpenSafetyLab/SALAD-BENCH) | Benchmark | Intermediate | Hierarchical evaluation of harmful requests and model safety. |
| [R005](#r005) | [SG-Bench](https://github.com/MurrayTom/SG-Bench) | Benchmark | Intermediate | Evaluates LLM safety generalization across tasks and prompt types. |
| [R038](#r038) | [HarmBench](https://github.com/centerforaisafety/HarmBench) | Benchmark | Intermediate | Standardizes harmful-behavior evaluation and red-teaming comparisons. |
| [R039](#r039) | [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) | Benchmark | Intermediate | Provides a reproducible benchmark for jailbreak robustness. |
| [R044](#r044) | [Do-Not-Answer](https://github.com/Libr-AI/do-not-answer) | Dataset | Beginner | Provides requests that responsible assistants should decline. |
| [R045](#r045) | [SafetyBench](https://github.com/thu-coai/SafetyBench) | Benchmark | Beginner | Evaluates safety understanding through multiple-choice questions. |
| [R048](#r048) | [ALERT](https://github.com/Babelscape/ALERT) | Benchmark | Intermediate | Evaluates safety through a taxonomy of red-teaming prompts. |
| [R049](#r049) | [AIR-Bench 2024](https://github.com/stanford-crfm/air-bench-2024) | Benchmark | Intermediate | Evaluates safety against a policy-informed risk taxonomy. |
| [R050](#r050) | [S-Eval](https://github.com/IS2Lab/S-Eval) | Benchmark | Intermediate | Evaluates language-model safety using diversified test prompts. |

### Selection notes

<a id="r001"></a>

**R001 · SALAD-Bench**

- **Interpretation:** Safety taxonomy and evaluator choice affect conclusions.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/OpenSafetyLab/SALAD-BENCH/HEAD/README.md).

<a id="r005"></a>

**R005 · SG-Bench**

- **Interpretation:** A language-model safety benchmark; not specifically an agent benchmark.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/MurrayTom/SG-Bench/HEAD/README.md).

<a id="r038"></a>

**R038 · HarmBench**

- **Interpretation:** Attack coverage and classifier errors influence measured robustness.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/centerforaisafety/HarmBench/HEAD/README.md).

<a id="r039"></a>

**R039 · JailbreakBench**

- **Interpretation:** Use the defined threat model and report attack budgets.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/JailbreakBench/jailbreakbench/HEAD/README.md).

<a id="r044"></a>

**R044 · Do-Not-Answer**

- **Interpretation:** Taxonomy and language coverage limit generalization.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/Libr-AI/do-not-answer/HEAD/README.md).

<a id="r045"></a>

**R045 · SafetyBench**

- **Interpretation:** Knowledge of safe answers does not establish safe agent behavior.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/thu-coai/SafetyBench/HEAD/README.md).

<a id="r048"></a>

**R048 · ALERT**

- **Interpretation:** Synthetic and adversarial distributions may differ from deployment traffic.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/Babelscape/ALERT/HEAD/README.md).

<a id="r049"></a>

**R049 · AIR-Bench 2024**

- **Interpretation:** Policy grounding does not constitute a legal compliance determination.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/stanford-crfm/air-bench-2024/HEAD/README.md).

<a id="r050"></a>

**R050 · S-Eval**

- **Interpretation:** Prompt distribution and evaluator language coverage affect scores.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/IS2Lab/S-Eval/HEAD/README.md).


## Red teaming

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R002](#r002) | [h4rm3l](https://github.com/mdoumbouya/h4rm3l) | Toolkit | Advanced | Composes jailbreak attacks for adversarial safety assessment. |
| [R019](#r019) | [WildTeaming](https://github.com/allenai/wildteaming) | Research toolkit | Advanced | Studies scalable adversarial prompt generation from in-the-wild tactics. |
| [R030](#r030) | [PyRIT](https://github.com/microsoft/PyRIT) | Toolkit | Intermediate | Supports structured generative-AI red-teaming workflows. |
| [R031](#r031) | [garak](https://github.com/NVIDIA/garak) | Toolkit | Beginner | Scans language models for multiple classes of vulnerabilities. |
| [R036](#r036) | [EasyJailbreak](https://github.com/EasyJailbreak/EasyJailbreak) | Toolkit | Advanced | Provides a framework for comparing jailbreak techniques. |
| [R037](#r037) | [JailbreakEval](https://github.com/ThuCCSLab/JailbreakEval) | Toolkit | Intermediate | Provides evaluators for jailbreak outcomes. |

### Selection notes

<a id="r002"></a>

**R002 · h4rm3l**

- **Interpretation:** Attack success depends on the attack budget and target configuration.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/mdoumbouya/h4rm3l/HEAD/README.md).

<a id="r019"></a>

**R019 · WildTeaming**

- **Interpretation:** Adversarial prompt distribution is not representative user traffic.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/allenai/wildteaming/HEAD/README.md).

<a id="r030"></a>

**R030 · PyRIT**

- **Interpretation:** Moved from Azure/PyRIT to microsoft/PyRIT; define a threat model and campaign budget.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/microsoft/PyRIT/HEAD/README.md).

<a id="r031"></a>

**R031 · garak**

- **Interpretation:** Scanner findings need contextual review and reproduction.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/NVIDIA/garak/HEAD/README.md).

<a id="r036"></a>

**R036 · EasyJailbreak**

- **Interpretation:** Compare attacks under equal query and compute budgets.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/EasyJailbreak/EasyJailbreak/HEAD/README.md).

<a id="r037"></a>

**R037 · JailbreakEval**

- **Interpretation:** Evaluator accuracy is distinct from target-model safety.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/ThuCCSLab/JailbreakEval/HEAD/README.md).


## Multimodal and embodied

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R003](#r003) | [SafeBench (multimodal)](https://github.com/NY1024/SafeBench) | Benchmark | Advanced | Evaluates multimodal harmful queries using collaborative judges. |
| [R006](#r006) | [SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench) | Benchmark | Advanced | Evaluates safe task planning by embodied language-model agents. |
| [R073](#r073) | [MM-SafetyBench](https://github.com/isXinLiu/MM-SafetyBench) | Benchmark | Advanced | Evaluates multimodal safety under image-associated harmful requests. |
| [R074](#r074) | [MSSBench](https://github.com/UCSB-AI/MSSBench) | Benchmark | Advanced | Evaluates safety decisions conditioned on visual situations. |

### Selection notes

<a id="r003"></a>

**R003 · SafeBench (multimodal)**

- **Interpretation:** The linked code describes itself as an initial proof of concept. Distinct from autonomous-driving projects with the same name.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/NY1024/SafeBench/HEAD/README.md).

<a id="r006"></a>

**R006 · SafeAgentBench**

- **Interpretation:** Requires simulator setup; simulated physical safety has transfer limits.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/shengyin1224/SafeAgentBench/HEAD/README.md).

<a id="r073"></a>

**R073 · MM-SafetyBench**

- **Interpretation:** Image conditions and text-only baselines should be reported separately.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/isXinLiu/MM-SafetyBench/HEAD/README.md).

<a id="r074"></a>

**R074 · MSSBench**

- **Interpretation:** Context-dependent safety differs from purely textual harmfulness.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/UCSB-AI/MSSBench/HEAD/README.md).


## Tool-using agents

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R004](#r004) | [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) | Benchmark | Intermediate | Tests agent safety across simulated tool environments. |
| [R008](#r008) | [ToolEmu / LM-Emulated Sandbox](https://github.com/ryoungj/ToolEmu) | Framework | Advanced | Emulates tool execution to identify risky agent actions. |
| [R016](#r016) | [R-Judge](https://github.com/Lordog/R-Judge) | Benchmark | Intermediate | Evaluates recognition of safety risks in agent interaction records. |
| [R017](#r017) | [A Trembling House of Cards?](https://arxiv.org/abs/2402.10196) | Paper | Advanced | Maps adversarial attacks against language agents. |
| [R018](#r018) | [AgentHarm](https://ukgovernmentbeis.github.io/inspect_evals/evals/agentharm/) | Benchmark | Intermediate | Evaluates harmful multi-step tool use alongside benign counterparts. |
| [R024](#r024) | [HAICOSYSTEM](https://arxiv.org/abs/2409.16427) | Framework | Advanced | Simulates safety risks in multi-turn human-agent interactions. |
| [R025](#r025) | [OpenAgentSafety](https://github.com/Open-Agent-Safety/OpenAgentSafety) | Framework | Advanced | Evaluates safety with real tools in sandboxed multi-user interactions. |

### Selection notes

<a id="r004"></a>

**R004 · Agent-SafetyBench**

- **Interpretation:** Simulated tools do not capture every deployment effect.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/thu-coai/Agent-SafetyBench/HEAD/README.md).

<a id="r008"></a>

**R008 · ToolEmu / LM-Emulated Sandbox**

- **Interpretation:** Emulator realism and evaluator agreement need validation.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/ryoungj/ToolEmu/HEAD/README.md).

<a id="r016"></a>

**R016 · R-Judge**

- **Interpretation:** Judging a recorded trajectory differs from acting safely.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/Lordog/R-Judge/HEAD/README.md).

<a id="r017"></a>

**R017 · A Trembling House of Cards?**

- **Interpretation:** Research paper; the full title resolves the original shorthand.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2402.10196).

<a id="r018"></a>

**R018 · AgentHarm**

- **Interpretation:** Read dataset-specific use terms and report agent capability alongside safety.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://ukgovernmentbeis.github.io/inspect_evals/evals/agentharm/).

<a id="r024"></a>

**R024 · HAICOSYSTEM**

- **Interpretation:** User and tool simulation introduce modeling assumptions.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2409.16427).

<a id="r025"></a>

**R025 · OpenAgentSafety**

- **Interpretation:** Maintained project moved from sani903/OpenAgentSafety in August 2026; container infrastructure and trajectory review are required.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/Open-Agent-Safety/OpenAgentSafety/HEAD/README.md).


## Specialized risk

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R007](#r007) | [ChemSafetyBench](https://arxiv.org/abs/2411.16736) | Benchmark | Advanced | Studies chemistry-specific knowledge and safety behavior. |
| [R011](#r011) | [RedCode](https://github.com/AI-secure/RedCode) | Benchmark | Advanced | Evaluates risky code generation and execution by code agents. |
| [R022](#r022) | [Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984) | Paper | Advanced | Investigates strategic deceptive behavior in controlled scenarios. |
| [R063](#r063) | [WMDP](https://github.com/centerforaisafety/wmdp) | Benchmark | Advanced | Uses expert-written questions as proxies for hazardous domain knowledge. |
| [R064](#r064) | [CyberSecEval](https://github.com/meta-llama/PurpleLlama) | Benchmark suite | Advanced | Evaluates cybersecurity-relevant risks and capabilities. |
| [R065](#r065) | [Cybench](https://github.com/andyzorigin/cybench) | Benchmark | Advanced | Evaluates cybersecurity task capabilities in controlled environments. |
| [R075](#r075) | [MACHIAVELLI](https://github.com/aypan17/machiavelli) | Benchmark | Advanced | Evaluates harmful and power-seeking behavior in text-based decision environments. |
| [R082](#r082) | [Agentic Misalignment](https://github.com/anthropic-experimental/agentic-misalignment) | Research toolkit | Advanced | Studies misaligned behavior in controlled organizational scenarios. |

### Selection notes

<a id="r007"></a>

**R007 · ChemSafetyBench**

- **Interpretation:** Paper is the stable source; the author-linked code location needs separate availability verification.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2411.16736).

<a id="r011"></a>

**R011 · RedCode**

- **Interpretation:** Execution tasks require disposable isolated environments.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/AI-secure/RedCode/HEAD/README.md).

<a id="r022"></a>

**R022 · Frontier Models are Capable of In-context Scheming**

- **Interpretation:** Resolves the original Frontier Models label; not a general capabilities suite.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2412.04984).

<a id="r063"></a>

**R063 · WMDP**

- **Interpretation:** Knowledge proxies are not direct measurements of real-world harmful capability.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/centerforaisafety/wmdp/HEAD/README.md).

<a id="r064"></a>

**R064 · CyberSecEval**

- **Interpretation:** Select the relevant component; execute only in authorized isolated settings.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/meta-llama/PurpleLlama/HEAD/README.md).

<a id="r065"></a>

**R065 · Cybench**

- **Interpretation:** Capability benchmark; task performance is not itself malicious intent.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/andyzorigin/cybench/HEAD/README.md).

<a id="r075"></a>

**R075 · MACHIAVELLI**

- **Interpretation:** Game outcomes are proxies; compare reward and harm separately.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/aypan17/machiavelli/HEAD/README.md).

<a id="r082"></a>

**R082 · Agentic Misalignment**

- **Interpretation:** Designed stress tests; observed rates do not estimate deployment prevalence.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/anthropic-experimental/agentic-misalignment/HEAD/README.md).


## Web and GUI agents

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R009](#r009) | [AdvWeb / AdvAgent](https://arxiv.org/abs/2410.17401) | Research toolkit | Advanced | Studies adversarial manipulation of vision-language web agents. |
| [R010](#r010) | [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886) | Paper | Advanced | Studies whether chatbot refusal transfers to browser-agent behavior. |
| [R012](#r012) | [From Interaction to Impact](https://arxiv.org/abs/2410.09006) | Paper | Advanced | Studies safety-relevant consequences of mobile UI operations. |
| [R014](#r014) | [Dissecting Adversarial Robustness of Multimodal LM Agents](https://arxiv.org/abs/2406.12814) | Paper | Advanced | Studies adversarial robustness of multimodal agents. |
| [R021](#r021) | [ST-WebAgentBench](https://github.com/segev-shlomov/ST-WebAgentBench) | Benchmark | Advanced | Evaluates web-agent safety and trustworthiness under policies. |
| [R023](#r023) | [SafeArena](https://github.com/McGill-NLP/safearena) | Benchmark | Advanced | Measures deliberate misuse of autonomous web agents. |

### Selection notes

<a id="r009"></a>

**R009 · AdvWeb / AdvAgent**

- **Interpretation:** Originally called AdvWeb; the current paper title uses AdvAgent. Research framework rather than a standard safety leaderboard.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2410.17401).

<a id="r010"></a>

**R010 · Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents**

- **Interpretation:** Research paper title, not a generic refusal-training toolkit.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2410.13886).

<a id="r012"></a>

**R012 · From Interaction to Impact**

- **Interpretation:** A research study; not a general-purpose interaction benchmark.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2410.09006).

<a id="r014"></a>

**R014 · Dissecting Adversarial Robustness of Multimodal LM Agents**

- **Interpretation:** An abbreviated paper title in the original list.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2406.12814).

<a id="r021"></a>

**R021 · ST-WebAgentBench**

- **Interpretation:** Environment state and policy compliance matter beyond task completion.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/segev-shlomov/ST-WebAgentBench/HEAD/README.md).

<a id="r023"></a>

**R023 · SafeArena**

- **Interpretation:** Paired benign tasks help distinguish inability from refusal.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/McGill-NLP/safearena/HEAD/README.md).


## Privacy

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R013](#r013) | [PrivacyLens](https://github.com/SALT-NLP/PrivacyLens) | Benchmark | Intermediate | Evaluates contextual privacy norms and agent information disclosure. |

### Selection notes

<a id="r013"></a>

**R013 · PrivacyLens**

- **Interpretation:** Privacy depends on context; question answers and actual actions may differ.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/SALT-NLP/PrivacyLens/HEAD/README.md).


## Governance and research

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R015](#r015) | [Infrastructure for AI Agents](https://arxiv.org/abs/2501.10114) | Paper | Intermediate | Discusses infrastructure for accountable agent deployment. |
| [R077](#r077) | [COMPL-AI](https://github.com/compl-ai/compl-ai) | Benchmark suite | Advanced | Maps technical LLM evaluations to aspects of AI regulation. |

### Selection notes

<a id="r015"></a>

**R015 · Infrastructure for AI Agents**

- **Interpretation:** Conceptual infrastructure proposal, not a runnable benchmark.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://arxiv.org/abs/2501.10114).

<a id="r077"></a>

**R077 · COMPL-AI**

- **Interpretation:** Technical scores are not legal advice or proof of compliance.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/compl-ai/compl-ai/HEAD/README.md).


## Directories

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R020](#r020) | [SafetyPrompts](https://safetyprompts.com/) | Directory | Beginner | Indexes open datasets for evaluating and improving LLM safety. |
| [R078](#r078) | [Awesome Large Model Safety](https://github.com/xingjunm/Awesome-Large-Model-Safety) | Directory | Beginner | Provides a broad safety research bibliography and benchmark index. |

### Selection notes

<a id="r020"></a>

**R020 · SafetyPrompts**

- **Interpretation:** The official catalogue is archived and states it has not been updated since May 2025; useful as a historical index.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://safetyprompts.com/).

<a id="r078"></a>

**R078 · Awesome Large Model Safety**

- **Interpretation:** A bibliography, not a common execution interface.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/xingjunm/Awesome-Large-Model-Safety/HEAD/README.md).


## Evaluation infrastructure

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R026](#r026) | [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | Framework | Beginner | Defines datasets, solvers, scorers, tasks, and evaluation logs. |
| [R027](#r027) | [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) | Evaluation collection | Beginner | Provides reusable evaluation implementations and a registry. |
| [R028](#r028) | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Framework | Intermediate | Runs standardized language-model evaluation tasks. |
| [R029](#r029) | [HELM](https://github.com/stanford-crfm/helm) | Framework | Intermediate | Supports transparent multi-metric language-model evaluation. |
| [R032](#r032) | [promptfoo](https://github.com/promptfoo/promptfoo) | Toolkit | Beginner | Supports prompt evaluation, comparisons, and red-team workflows. |
| [R033](#r033) | [Giskard](https://github.com/Giskard-AI/giskard-oss) | Toolkit | Intermediate | Tests language-model applications for quality and risk. |
| [R034](#r034) | [DeepEval](https://github.com/confident-ai/deepeval) | Framework | Beginner | Provides evaluation metrics and tests for LLM applications. |
| [R035](#r035) | [Moonshot](https://github.com/aiverify-foundation/moonshot) | Toolkit | Intermediate | Combines LLM benchmarking and red-teaming workflows. |

### Selection notes

<a id="r026"></a>

**R026 · Inspect AI**

- **Interpretation:** Framework rather than a safety score or dataset.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_ai/HEAD/README.md).

<a id="r027"></a>

**R027 · Inspect Evals**

- **Interpretation:** Individual evaluations have separate requirements and dataset terms.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_evals/HEAD/README.md).

<a id="r028"></a>

**R028 · lm-evaluation-harness**

- **Interpretation:** Broad capability evaluation; safety coverage depends on selected tasks.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/EleutherAI/lm-evaluation-harness/HEAD/README.md).

<a id="r029"></a>

**R029 · HELM**

- **Interpretation:** The repository states HELM entered maintenance mode in June 2026. Scenarios and adapters determine comparability.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/stanford-crfm/helm/HEAD/README.md).

<a id="r032"></a>

**R032 · promptfoo**

- **Interpretation:** Configure your own application context and assertions.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/promptfoo/promptfoo/HEAD/README.md).

<a id="r033"></a>

**R033 · Giskard**

- **Interpretation:** Application tests are not a universal model safety certification.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/Giskard-AI/giskard-oss/HEAD/README.md).

<a id="r034"></a>

**R034 · DeepEval**

- **Interpretation:** Judge-based metrics require calibration for your use case.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/confident-ai/deepeval/HEAD/README.md).

<a id="r035"></a>

**R035 · Moonshot**

- **Interpretation:** Individual recipes vary in dependencies and scope.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/aiverify-foundation/moonshot/HEAD/README.md).


## Refusal calibration

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R040](#r040) | [StrongREJECT](https://github.com/dsbowen/strong_reject) | Benchmark and evaluator | Intermediate | Assesses harmful-request fulfillment beyond superficial refusal wording. |
| [R041](#r041) | [SORRY-Bench](https://github.com/SORRY-Bench/SORRY-Bench) | Benchmark | Intermediate | Evaluates safety refusal across a structured harmful-request taxonomy. |
| [R042](#r042) | [XSTest](https://github.com/paul-rottger/xstest) | Benchmark | Beginner | Tests exaggerated refusals on safe prompts with unsafe contrasts. |
| [R043](#r043) | [OR-Bench](https://github.com/justincui03/or-bench) | Benchmark | Beginner | Evaluates over-refusal on benign prompts that appear sensitive. |

### Selection notes

<a id="r040"></a>

**R040 · StrongREJECT**

- **Interpretation:** Judge scores require validation on the target distribution.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/dsbowen/strong_reject/HEAD/README.md).

<a id="r041"></a>

**R041 · SORRY-Bench**

- **Interpretation:** Refusal on harmful requests does not establish helpfulness on safe ones.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/SORRY-Bench/SORRY-Bench/HEAD/README.md).

<a id="r042"></a>

**R042 · XSTest**

- **Interpretation:** A focused diagnostic suite rather than complete safety coverage.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://github.com/paul-rottger/xstest).

<a id="r043"></a>

**R043 · OR-Bench**

- **Interpretation:** Pair with harmful-request tests to measure both error directions.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/justincui03/or-bench/HEAD/README.md).


## Trustworthiness

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R046](#r046) | [DecodingTrust](https://github.com/AI-secure/DecodingTrust) | Benchmark suite | Intermediate | Evaluates multiple dimensions of language-model trustworthiness. |
| [R047](#r047) | [TrustLLM](https://github.com/HowieHwong/TrustLLM) | Benchmark suite | Intermediate | Evaluates language models across several trustworthiness dimensions. |
| [R076](#r076) | [Sycophancy evaluations](https://github.com/anthropics/evals) | Evaluation collection | Intermediate | Examines agreement with users at the expense of truthful judgment. |

### Selection notes

<a id="r046"></a>

**R046 · DecodingTrust**

- **Interpretation:** Report individual dimensions rather than treating trust as one number.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/AI-secure/DecodingTrust/HEAD/README.md).

<a id="r047"></a>

**R047 · TrustLLM**

- **Interpretation:** Component metrics and underlying datasets have different interpretations.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/HowieHwong/TrustLLM/HEAD/README.md).

<a id="r076"></a>

**R076 · Sycophancy evaluations**

- **Interpretation:** Research evaluations; selected tasks do not cover every form of deception.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/anthropics/evals/HEAD/README.md).


## Alignment data

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R051](#r051) | [BeaverTails](https://github.com/PKU-Alignment/beavertails) | Dataset | Beginner | Provides safety annotations and preference data for assistant responses. |
| [R052](#r052) | [PKU-SafeRLHF](https://github.com/PKU-Alignment/safe-rlhf) | Dataset | Intermediate | Provides helpfulness and safety preference annotations. |
| [R053](#r053) | [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) | Dataset | Beginner | Provides human preference data for helpfulness and harmlessness. |

### Selection notes

<a id="r051"></a>

**R051 · BeaverTails**

- **Interpretation:** Training data; define a clean held-out evaluation split before testing.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/PKU-Alignment/beavertails/HEAD/README.md).

<a id="r052"></a>

**R052 · PKU-SafeRLHF**

- **Interpretation:** Repository includes training infrastructure; avoid train-test overlap.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/PKU-Alignment/safe-rlhf/HEAD/README.md).

<a id="r053"></a>

**R053 · Anthropic HH-RLHF**

- **Interpretation:** Historical alignment data, not a current universal benchmark. The authors direct users from the deprecated GitHub repository to this dataset.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://huggingface.co/datasets/Anthropic/hh-rlhf).


## Bias and toxicity

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R054](#r054) | [RealToxicityPrompts](https://github.com/allenai/real-toxicity-prompts) | Dataset | Beginner | Tests toxicity risks in language-model continuations. |
| [R055](#r055) | [ToxiGen](https://github.com/microsoft/TOXIGEN) | Dataset | Intermediate | Contains implicit toxic and benign language about minority groups. |
| [R056](#r056) | [BBQ](https://github.com/nyu-mll/BBQ) | Benchmark | Beginner | Evaluates social bias in question answering under ambiguity. |
| [R057](#r057) | [BOLD](https://github.com/amazon-science/bold) | Dataset | Intermediate | Provides prompts for studying bias in open-ended generation. |
| [R058](#r058) | [CrowS-Pairs](https://github.com/nyu-mll/crows-pairs) | Dataset | Intermediate | Tests stereotypical associations using paired sentences. |
| [R059](#r059) | [StereoSet](https://github.com/moinnadeem/StereoSet) | Benchmark | Intermediate | Measures stereotypical associations with language-modeling controls. |

### Selection notes

<a id="r054"></a>

**R054 · RealToxicityPrompts**

- **Interpretation:** Toxicity detectors may encode biases and miss contextual harms.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/allenai/real-toxicity-prompts/HEAD/README.md).

<a id="r055"></a>

**R055 · ToxiGen**

- **Interpretation:** Dataset labels and group coverage require contextual interpretation.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/microsoft/TOXIGEN/HEAD/README.md).

<a id="r056"></a>

**R056 · BBQ**

- **Interpretation:** Question-answering bias differs from deployment discrimination.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/nyu-mll/BBQ/HEAD/README.md).

<a id="r057"></a>

**R057 · BOLD**

- **Interpretation:** Results depend on the generation and measurement pipeline.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/amazon-science/bold/HEAD/README.md).

<a id="r058"></a>

**R058 · CrowS-Pairs**

- **Interpretation:** The repository flags data-reliability concerns; examine its linked critiques before using paired-sentence scores.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/nyu-mll/crows-pairs/HEAD/README.md).

<a id="r059"></a>

**R059 · StereoSet**

- **Interpretation:** Association scores should not be equated with all fairness properties.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/moinnadeem/StereoSet/HEAD/README.md).


## Factuality and hallucination

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R060](#r060) | [TruthfulQA](https://github.com/sylinrl/TruthfulQA) | Benchmark | Beginner | Tests susceptibility to common human misconceptions. |
| [R061](#r061) | [SimpleQA](https://github.com/openai/simple-evals) | Benchmark | Beginner | Evaluates short factual question answering. |
| [R062](#r062) | [HaluEval](https://github.com/RUCAIBox/HaluEval) | Benchmark | Intermediate | Evaluates hallucination recognition in generated text. |

### Selection notes

<a id="r060"></a>

**R060 · TruthfulQA**

- **Interpretation:** Adjacent reliability measure; truthfulness does not establish overall safety.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/sylinrl/TruthfulQA/HEAD/README.md).

<a id="r061"></a>

**R061 · SimpleQA**

- **Interpretation:** Adjacent reliability measure. The reference simple-evals repository announces it will not be updated for new models or results; pin its revision.
- **Setup effort:** Low to moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/openai/simple-evals/HEAD/README.md).

<a id="r062"></a>

**R062 · HaluEval**

- **Interpretation:** Recognizing hallucinations differs from avoiding them during generation.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/RUCAIBox/HaluEval/HEAD/README.md).


## Prompt injection

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R066](#r066) | [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Benchmark and environment | Intermediate | Evaluates prompt-injection attacks and defenses for tool-using agents. |
| [R067](#r067) | [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) | Benchmark | Intermediate | Evaluates indirect prompt injection in tool-integrated agents. |
| [R068](#r068) | [Agent Security Bench (ASB)](https://github.com/agiresearch/ASB) | Benchmark | Advanced | Studies attacks and defenses across agent scenarios and tools. |
| [R069](#r069) | [WASP](https://github.com/facebookresearch/wasp) | Benchmark | Advanced | Evaluates web-agent security against prompt injection. |
| [R070](#r070) | [Tensor Trust](https://github.com/HumanCompatibleAI/tensor-trust) | Dataset and benchmark | Intermediate | Studies prompt injection through human-authored attack and defense examples. |
| [R071](#r071) | [BIPIA](https://github.com/microsoft/BIPIA) | Benchmark | Intermediate | Evaluates indirect prompt injection across application contexts. |
| [R072](#r072) | [LLMail-Inject](https://github.com/microsoft/llmail-inject-challenge) | Dataset and challenge | Advanced | Studies indirect prompt injection against email assistants. |

### Selection notes

<a id="r066"></a>

**R066 · AgentDojo**

- **Interpretation:** Report utility and attack success under a fixed attacker model.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/ethz-spylab/agentdojo/HEAD/README.md).

<a id="r067"></a>

**R067 · InjecAgent**

- **Interpretation:** Static tool-context tests have limits for long interactive workflows.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/uiuc-kang-lab/InjecAgent/HEAD/README.md).

<a id="r068"></a>

**R068 · Agent Security Bench (ASB)**

- **Interpretation:** Distinct from Agent-SafetyBench; configure attack and defense settings explicitly.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/agiresearch/ASB/HEAD/README.md).

<a id="r069"></a>

**R069 · WASP**

- **Interpretation:** The official repository is archived. Web environment setup and attacker access define the threat model.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/facebookresearch/wasp/HEAD/README.md).

<a id="r070"></a>

**R070 · Tensor Trust**

- **Interpretation:** Game-derived interactions may not represent production tool use.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/HumanCompatibleAI/tensor-trust/HEAD/README.md).

<a id="r071"></a>

**R071 · BIPIA**

- **Interpretation:** Attack surfaces and retrieval context should match your application.
- **Setup effort:** Moderate (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/microsoft/BIPIA/HEAD/README.md).

<a id="r072"></a>

**R072 · LLMail-Inject**

- **Interpretation:** Challenge-derived attacks need evaluation on held-out system configurations.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/microsoft/llmail-inject-challenge/HEAD/README.md).


## Capability controls

| ID | Resource and primary source | Type | Level | Focus |
| --- | --- | --- | --- | --- |
| [R079](#r079) | [WebArena](https://github.com/web-arena-x/webarena) | Benchmark and environment | Advanced | Provides realistic web tasks for measuring agent capability. |
| [R080](#r080) | [OSWorld](https://github.com/xlang-ai/OSWorld) | Benchmark and environment | Advanced | Evaluates agents on computer-use tasks in operating systems. |
| [R081](#r081) | [AgentBench](https://github.com/THUDM/AgentBench) | Benchmark | Advanced | Evaluates language-model agents across interactive environments. |

### Selection notes

<a id="r079"></a>

**R079 · WebArena**

- **Interpretation:** Capability baseline; not a safety benchmark by itself.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/web-arena-x/webarena/HEAD/README.md).

<a id="r080"></a>

**R080 · OSWorld**

- **Interpretation:** Capability baseline; requires isolated desktop environments.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/xlang-ai/OSWorld/HEAD/README.md).

<a id="r081"></a>

**R081 · AgentBench**

- **Interpretation:** Useful control for agent capability; does not establish safety.
- **Setup effort:** Moderate to high (editorial estimate; varies by configuration).
- **Verification:** Source reviewed; execution not tested (2026-10-27). [Reviewed primary source](https://raw.githubusercontent.com/THUDM/AgentBench/HEAD/README.md).
