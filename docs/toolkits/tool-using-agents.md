# Tool-using agents

7 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### Agent-SafetyBench { #r004 }

**Benchmark** · 🟡 Intermediate · `R004`

Tests agent safety across simulated tool environments.

**Links:** [Paper](https://arxiv.org/abs/2412.14470) · [Code](https://github.com/thu-coai/Agent-SafetyBench)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md)

!!! warning "Keep in mind"
    Simulated tools do not capture every deployment effect.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### ToolEmu / LM-Emulated Sandbox { #r008 }

**Framework** · 🔴 Advanced · `R008`

Emulates tool execution to identify risky agent actions.

**Links:** [Paper](https://arxiv.org/abs/2309.15817) · [Code](https://github.com/ryoungj/ToolEmu)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md)

!!! warning "Keep in mind"
    Emulator realism and evaluator agreement need validation.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### R-Judge { #r016 }

**Benchmark** · 🟡 Intermediate · `R016`

Evaluates recognition of safety risks in agent interaction records.

**Links:** [Paper](https://arxiv.org/abs/2401.10019) · [Code](https://github.com/Lordog/R-Judge)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

!!! warning "Keep in mind"
    Judging a recorded trajectory differs from acting safely.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### A Trembling House of Cards? { #r017 }

**Paper** · 🔴 Advanced · `R017`

Maps adversarial attacks against language agents.

**Links:** [Paper](https://arxiv.org/abs/2402.10196)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    Research paper; the full title resolves the original shorthand.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### AgentHarm { #r018 }

**Benchmark** · 🟡 Intermediate · `R018`

Evaluates harmful multi-step tool use alongside benign counterparts.

**Links:** [Paper](https://arxiv.org/abs/2410.09024) · [Code](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm) · [Data](https://huggingface.co/datasets/ai-safety-institute/AgentHarm)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Harmful requests and over-refusal](../methods/harmful-requests.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/agentharm --limit 10
    inspect eval inspect_evals/agentharm_benign --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Read dataset-specific use terms and report agent capability alongside safety.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### HAICOSYSTEM { #r024 }

**Framework** · 🔴 Advanced · `R024`

Simulates safety risks in multi-turn human-agent interactions.

**Links:** [Paper](https://arxiv.org/abs/2409.16427) · [Code](https://github.com/XuhuiZhou/HAICOSYSTEM)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md)

!!! warning "Keep in mind"
    User and tool simulation introduce modeling assumptions.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### OpenAgentSafety { #r025 }

**Framework** · 🔴 Advanced · `R025`

Evaluates safety with real tools in sandboxed multi-user interactions.

**Links:** [Paper](https://arxiv.org/abs/2507.06134) · [Code](https://github.com/Open-Agent-Safety/OpenAgentSafety)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md)

!!! warning "Keep in mind"
    Maintained project moved from sani903/OpenAgentSafety in August 2026; container infrastructure and trajectory review are required.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
