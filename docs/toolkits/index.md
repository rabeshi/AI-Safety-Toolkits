# Toolkit catalogue

**82 benchmarks, datasets, frameworks, red-teaming tools, and papers**, each with links to the paper, code, documentation, and data where they exist.

!!! tip "New here?"
    Filter by **Beginner** and start with the resources that have a quickstart. If you are unsure what you need, read [How evaluation works](../getting-started/index.md) and [Choosing a resource](../guides/choosing.md) first.

<small>Links were checked against primary sources on 2026-10-27. Quickstart commands are copied from each project's own documentation; this hub has not run them. Check upstream licences before using code or data.</small>

## Browse by category

| Category | Resources |
| --- | --- |
| [Content safety](content-safety.md) | 9 |
| [Red teaming](red-teaming.md) | 6 |
| [Multimodal and embodied](multimodal-and-embodied.md) | 4 |
| [Tool-using agents](tool-using-agents.md) | 7 |
| [Specialized risk](specialized-risk.md) | 8 |
| [Web and GUI agents](web-and-gui-agents.md) | 6 |
| [Privacy](privacy.md) | 1 |
| [Governance and research](governance-and-research.md) | 2 |
| [Directories](directories.md) | 2 |
| [Evaluation infrastructure](evaluation-infrastructure.md) | 8 |
| [Refusal calibration](refusal-calibration.md) | 4 |
| [Trustworthiness](trustworthiness.md) | 3 |
| [Alignment data](alignment-data.md) | 3 |
| [Bias and toxicity](bias-and-toxicity.md) | 6 |
| [Factuality and hallucination](factuality-and-hallucination.md) | 3 |
| [Prompt injection](prompt-injection.md) | 7 |
| [Capability controls](capability-controls.md) | 3 |

## All resources

<input id="toolkit-filter" class="toolkit-filter" type="search" placeholder="Filter by name, level, method, or keyword (e.g. beginner, injection, agent)">

| Resource | Category | Type | Level | Quickstart | Links |
| --- | --- | --- | --- | --- | --- |
| [A Trembling House of Cards?](tool-using-agents.md#r017) | Tool-using agents | Paper | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2402.10196) |
| [AdvWeb / AdvAgent](web-and-gui-agents.md#r009) | Web and GUI agents | Research toolkit | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.17401) · [Code](https://github.com/AI-secure/AdvAgent) |
| [Agent Security Bench (ASB)](prompt-injection.md#r068) | Prompt injection | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.02644) · [Code](https://github.com/agiresearch/ASB) |
| [Agent-SafetyBench](tool-using-agents.md#r004) | Tool-using agents | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2412.14470) · [Code](https://github.com/thu-coai/Agent-SafetyBench) |
| [AgentBench](capability-controls.md#r081) | Capability controls | Benchmark | 🔴 Advanced | ✅ | [Paper](https://arxiv.org/abs/2308.03688) · [Code](https://github.com/THUDM/AgentBench) |
| [AgentDojo](prompt-injection.md#r066) | Prompt injection | Benchmark and environment | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2406.13352) · [Code](https://github.com/ethz-spylab/agentdojo) · [Docs](https://agentdojo.spylab.ai/) |
| [AgentHarm](tool-using-agents.md#r018) | Tool-using agents | Benchmark | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2410.09024) · [Code](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm) · [Data](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) |
| [Agentic Misalignment](specialized-risk.md#r082) | Specialized risk | Research toolkit | 🔴 Advanced | ✅ | [Paper](https://arxiv.org/abs/2510.05179) · [Code](https://github.com/anthropic-experimental/agentic-misalignment) |
| [AIR-Bench 2024](content-safety.md#r049) | Content safety | Benchmark | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2407.17436) · [Code](https://github.com/stanford-crfm/air-bench-2024) · [Data](https://huggingface.co/datasets/stanford-crfm/air-bench-2024) |
| [ALERT](content-safety.md#r048) | Content safety | Benchmark | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2404.08676) · [Code](https://github.com/Babelscape/ALERT) · [Data](https://huggingface.co/datasets/Babelscape/ALERT) |
| [Anthropic HH-RLHF](alignment-data.md#r053) | Alignment data | Dataset | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2204.05862) · [Data](https://huggingface.co/datasets/Anthropic/hh-rlhf) |
| [Awesome Large Model Safety](directories.md#r078) | Directories | Directory | 🟢 Beginner |  | [Paper](https://arxiv.org/abs/2502.05206) · [Code](https://github.com/xingjunm/Awesome-Large-Model-Safety) |
| [BBQ](bias-and-toxicity.md#r056) | Bias and toxicity | Benchmark | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2110.08193) · [Code](https://github.com/nyu-mll/BBQ) |
| [BeaverTails](alignment-data.md#r051) | Alignment data | Dataset | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2307.04657) · [Code](https://github.com/PKU-Alignment/beavertails) · [Data](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) |
| [BIPIA](prompt-injection.md#r071) | Prompt injection | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2312.14197) · [Code](https://github.com/microsoft/BIPIA) |
| [BOLD](bias-and-toxicity.md#r057) | Bias and toxicity | Dataset | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2101.11718) · [Code](https://github.com/amazon-science/bold) · [Data](https://huggingface.co/datasets/AmazonScience/bold) |
| [ChemSafetyBench](specialized-risk.md#r007) | Specialized risk | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2411.16736) |
| [COMPL-AI](governance-and-research.md#r077) | Governance and research | Benchmark suite | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.07959) · [Code](https://github.com/compl-ai/compl-ai) |
| [CrowS-Pairs](bias-and-toxicity.md#r058) | Bias and toxicity | Dataset | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2010.00133) · [Code](https://github.com/nyu-mll/crows-pairs) |
| [Cybench](specialized-risk.md#r065) | Specialized risk | Benchmark | 🔴 Advanced | ✅ | [Paper](https://arxiv.org/abs/2408.08926) · [Code](https://github.com/andyzorigin/cybench) |
| [CyberSecEval](specialized-risk.md#r064) | Specialized risk | Benchmark suite | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2312.04724) · [Code](https://github.com/meta-llama/PurpleLlama) |
| [DecodingTrust](trustworthiness.md#r046) | Trustworthiness | Benchmark suite | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2306.11698) · [Code](https://github.com/AI-secure/DecodingTrust) |
| [DeepEval](evaluation-infrastructure.md#r034) | Evaluation infrastructure | Framework | 🟢 Beginner | ✅ | [Code](https://github.com/confident-ai/deepeval) · [Docs](https://deepeval.com/docs/getting-started) |
| [Dissecting Adversarial Robustness of Multimodal LM Agents](web-and-gui-agents.md#r014) | Web and GUI agents | Paper | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2406.12814) · [Code](https://github.com/ChenWu98/agent-attack) |
| [Do-Not-Answer](content-safety.md#r044) | Content safety | Dataset | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2308.13387) · [Code](https://github.com/Libr-AI/do-not-answer) · [Data](https://huggingface.co/datasets/LibrAI/do-not-answer) |
| [EasyJailbreak](red-teaming.md#r036) | Red teaming | Toolkit | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2403.12171) · [Code](https://github.com/EasyJailbreak/EasyJailbreak) |
| [From Interaction to Impact](web-and-gui-agents.md#r012) | Web and GUI agents | Paper | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.09006) |
| [Frontier Models are Capable of In-context Scheming](specialized-risk.md#r022) | Specialized risk | Paper | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2412.04984) |
| [garak](red-teaming.md#r031) | Red teaming | Toolkit | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2406.11036) · [Code](https://github.com/NVIDIA/garak) · [Docs](https://reference.garak.ai/) |
| [Giskard](evaluation-infrastructure.md#r033) | Evaluation infrastructure | Toolkit | 🟡 Intermediate |  | [Code](https://github.com/Giskard-AI/giskard-oss) · [Docs](https://docs.giskard.ai/) |
| [h4rm3l](red-teaming.md#r002) | Red teaming | Toolkit | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2408.04811) · [Code](https://github.com/mdoumbouya/h4rm3l) |
| [HAICOSYSTEM](tool-using-agents.md#r024) | Tool-using agents | Framework | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2409.16427) · [Code](https://github.com/XuhuiZhou/HAICOSYSTEM) |
| [HaluEval](factuality-and-hallucination.md#r062) | Factuality and hallucination | Benchmark | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2305.11747) · [Code](https://github.com/RUCAIBox/HaluEval) · [Data](https://huggingface.co/datasets/pminervini/HaluEval) |
| [HarmBench](content-safety.md#r038) | Content safety | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2402.04249) · [Code](https://github.com/centerforaisafety/HarmBench) |
| [HELM](evaluation-infrastructure.md#r029) | Evaluation infrastructure | Framework | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2211.09110) · [Code](https://github.com/stanford-crfm/helm) · [Docs](https://crfm-helm.readthedocs.io/) |
| [Infrastructure for AI Agents](governance-and-research.md#r015) | Governance and research | Paper | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2501.10114) |
| [InjecAgent](prompt-injection.md#r067) | Prompt injection | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2403.02691) · [Code](https://github.com/uiuc-kang-lab/InjecAgent) |
| [Inspect AI](evaluation-infrastructure.md#r026) | Evaluation infrastructure | Framework | 🟢 Beginner | ✅ | [Code](https://github.com/UKGovernmentBEIS/inspect_ai) · [Docs](https://inspect.aisi.org.uk/) |
| [Inspect Evals](evaluation-infrastructure.md#r027) | Evaluation infrastructure | Evaluation collection | 🟢 Beginner | ✅ | [Code](https://github.com/UKGovernmentBEIS/inspect_evals) · [Docs](https://ukgovernmentbeis.github.io/inspect_evals/) |
| [JailbreakBench](content-safety.md#r039) | Content safety | Benchmark | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2404.01318) · [Code](https://github.com/JailbreakBench/jailbreakbench) · [Docs](https://jailbreakbench.github.io/) · [Data](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors) |
| [JailbreakEval](red-teaming.md#r037) | Red teaming | Toolkit | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2406.09321) · [Code](https://github.com/ThuCCSLab/JailbreakEval) |
| [LLMail-Inject](prompt-injection.md#r072) | Prompt injection | Dataset and challenge | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2506.09956) · [Code](https://github.com/microsoft/llmail-inject-challenge) |
| [lm-evaluation-harness](evaluation-infrastructure.md#r028) | Evaluation infrastructure | Framework | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2405.14782) · [Code](https://github.com/EleutherAI/lm-evaluation-harness) |
| [MACHIAVELLI](specialized-risk.md#r075) | Specialized risk | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2304.03279) · [Code](https://github.com/aypan17/machiavelli) |
| [MM-SafetyBench](multimodal-and-embodied.md#r073) | Multimodal and embodied | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2311.17600) · [Code](https://github.com/isXinLiu/MM-SafetyBench) |
| [Moonshot](evaluation-infrastructure.md#r035) | Evaluation infrastructure | Toolkit | 🟡 Intermediate |  | [Code](https://github.com/aiverify-foundation/moonshot) · [Docs](https://aiverify-foundation.github.io/moonshot/) |
| [MSSBench](multimodal-and-embodied.md#r074) | Multimodal and embodied | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.06172) · [Code](https://github.com/UCSB-AI/MSSBench) |
| [OpenAgentSafety](tool-using-agents.md#r025) | Tool-using agents | Framework | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2507.06134) · [Code](https://github.com/Open-Agent-Safety/OpenAgentSafety) |
| [OR-Bench](refusal-calibration.md#r043) | Refusal calibration | Benchmark | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2405.20947) · [Code](https://github.com/justincui03/or-bench) · [Data](https://huggingface.co/datasets/bench-llm/or-bench) |
| [OSWorld](capability-controls.md#r080) | Capability controls | Benchmark and environment | 🔴 Advanced | ✅ | [Paper](https://arxiv.org/abs/2404.07972) · [Code](https://github.com/xlang-ai/OSWorld) |
| [PKU-SafeRLHF](alignment-data.md#r052) | Alignment data | Dataset | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2310.12773) · [Code](https://github.com/PKU-Alignment/safe-rlhf) · [Data](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF) |
| [PrivacyLens](privacy.md#r013) | Privacy | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2409.00138) · [Code](https://github.com/SALT-NLP/PrivacyLens) |
| [promptfoo](evaluation-infrastructure.md#r032) | Evaluation infrastructure | Toolkit | 🟢 Beginner | ✅ | [Code](https://github.com/promptfoo/promptfoo) · [Docs](https://www.promptfoo.dev/docs/red-team/) |
| [PyRIT](red-teaming.md#r030) | Red teaming | Toolkit | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2410.02828) · [Code](https://github.com/microsoft/PyRIT) · [Docs](https://azure.github.io/PyRIT/) |
| [R-Judge](tool-using-agents.md#r016) | Tool-using agents | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2401.10019) · [Code](https://github.com/Lordog/R-Judge) |
| [RealToxicityPrompts](bias-and-toxicity.md#r054) | Bias and toxicity | Dataset | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2009.11462) · [Code](https://github.com/allenai/real-toxicity-prompts) · [Data](https://huggingface.co/datasets/allenai/real-toxicity-prompts) |
| [RedCode](specialized-risk.md#r011) | Specialized risk | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2411.07781) · [Code](https://github.com/AI-secure/RedCode) |
| [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](web-and-gui-agents.md#r010) | Web and GUI agents | Paper | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.13886) · [Code](https://github.com/scaleapi/browser-art) |
| [S-Eval](content-safety.md#r050) | Content safety | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2405.14191) · [Code](https://github.com/IS2Lab/S-Eval) · [Data](https://huggingface.co/datasets/IS2Lab/S-Eval) |
| [SafeAgentBench](multimodal-and-embodied.md#r006) | Multimodal and embodied | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2412.13178) · [Code](https://github.com/shengyin1224/SafeAgentBench) |
| [SafeArena](web-and-gui-agents.md#r023) | Web and GUI agents | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2503.04957) · [Code](https://github.com/McGill-NLP/safearena) |
| [SafeBench (multimodal)](multimodal-and-embodied.md#r003) | Multimodal and embodied | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.18927) · [Code](https://github.com/NY1024/SafeBench) |
| [SafetyBench](content-safety.md#r045) | Content safety | Benchmark | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2309.07045) · [Code](https://github.com/thu-coai/SafetyBench) · [Data](https://huggingface.co/datasets/thu-coai/SafetyBench) |
| [SafetyPrompts](directories.md#r020) | Directories | Directory | 🟢 Beginner |  | [Paper](https://arxiv.org/abs/2404.05399) · [Docs](https://safetyprompts.com/) |
| [SALAD-Bench](content-safety.md#r001) | Content safety | Benchmark | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2402.05044) · [Code](https://github.com/OpenSafetyLab/SALAD-BENCH) · [Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data) |
| [SG-Bench](content-safety.md#r005) | Content safety | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2410.21965) · [Code](https://github.com/MurrayTom/SG-Bench) |
| [SimpleQA](factuality-and-hallucination.md#r061) | Factuality and hallucination | Benchmark | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2411.04368) · [Code](https://github.com/openai/simple-evals) |
| [SORRY-Bench](refusal-calibration.md#r041) | Refusal calibration | Benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2406.14598) · [Code](https://github.com/SORRY-Bench/SORRY-Bench) · [Data](https://huggingface.co/datasets/sorry-bench/sorry-bench-202406) |
| [ST-WebAgentBench](web-and-gui-agents.md#r021) | Web and GUI agents | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2410.06703) · [Code](https://github.com/segev-shlomov/ST-WebAgentBench) |
| [StereoSet](bias-and-toxicity.md#r059) | Bias and toxicity | Benchmark | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2004.09456) · [Code](https://github.com/moinnadeem/StereoSet) · [Data](https://huggingface.co/datasets/McGill-NLP/stereoset) |
| [StrongREJECT](refusal-calibration.md#r040) | Refusal calibration | Benchmark and evaluator | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2402.10260) · [Code](https://github.com/dsbowen/strong_reject) |
| [Sycophancy evaluations](trustworthiness.md#r076) | Trustworthiness | Evaluation collection | 🟡 Intermediate | ✅ | [Paper](https://arxiv.org/abs/2212.09251) · [Code](https://github.com/anthropics/evals) |
| [Tensor Trust](prompt-injection.md#r070) | Prompt injection | Dataset and benchmark | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2311.01011) · [Code](https://github.com/HumanCompatibleAI/tensor-trust) |
| [ToolEmu / LM-Emulated Sandbox](tool-using-agents.md#r008) | Tool-using agents | Framework | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2309.15817) · [Code](https://github.com/ryoungj/ToolEmu) |
| [ToxiGen](bias-and-toxicity.md#r055) | Bias and toxicity | Dataset | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2203.09509) · [Code](https://github.com/microsoft/TOXIGEN) · [Data](https://huggingface.co/datasets/toxigen/toxigen-data) |
| [TrustLLM](trustworthiness.md#r047) | Trustworthiness | Benchmark suite | 🟡 Intermediate |  | [Paper](https://arxiv.org/abs/2401.05561) · [Code](https://github.com/HowieHwong/TrustLLM) |
| [TruthfulQA](factuality-and-hallucination.md#r060) | Factuality and hallucination | Benchmark | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2109.07958) · [Code](https://github.com/sylinrl/TruthfulQA) · [Data](https://huggingface.co/datasets/truthfulqa/truthful_qa) |
| [WASP](prompt-injection.md#r069) | Prompt injection | Benchmark | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2504.18575) · [Code](https://github.com/facebookresearch/wasp) |
| [WebArena](capability-controls.md#r079) | Capability controls | Benchmark and environment | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2307.13854) · [Code](https://github.com/web-arena-x/webarena) |
| [WildTeaming](red-teaming.md#r019) | Red teaming | Research toolkit | 🔴 Advanced |  | [Paper](https://arxiv.org/abs/2406.18510) · [Code](https://github.com/allenai/wildteaming) · [Data](https://huggingface.co/datasets/allenai/wildjailbreak) |
| [WMDP](specialized-risk.md#r063) | Specialized risk | Benchmark | 🔴 Advanced | ✅ | [Paper](https://arxiv.org/abs/2403.03218) · [Code](https://github.com/centerforaisafety/wmdp) · [Data](https://huggingface.co/datasets/cais/wmdp) |
| [XSTest](refusal-calibration.md#r042) | Refusal calibration | Benchmark | 🟢 Beginner | ✅ | [Paper](https://arxiv.org/abs/2308.01263) · [Code](https://github.com/paul-rottger/xstest) · [Data](https://huggingface.co/datasets/Paul/XSTest) |
