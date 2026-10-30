# Prompt injection

7 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### AgentDojo { #r066 }

**Benchmark and environment** · 🟡 Intermediate · `R066`

Evaluates prompt-injection attacks and defenses for tool-using agents.

**Links:** [Paper](https://arxiv.org/abs/2406.13352) · [Code](https://github.com/ethz-spylab/agentdojo) · [Docs](https://agentdojo.spylab.ai/)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Prompt injection](../methods/prompt-injection.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install "inspect-evals[agentdojo]"
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/agentdojo --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Report utility and attack success under a fixed attacker model.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### InjecAgent { #r067 }

**Benchmark** · 🟡 Intermediate · `R067`

Evaluates indirect prompt injection in tool-integrated agents.

**Links:** [Paper](https://arxiv.org/abs/2403.02691) · [Code](https://github.com/uiuc-kang-lab/InjecAgent)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    Static tool-context tests have limits for long interactive workflows.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Agent Security Bench (ASB) { #r068 }

**Benchmark** · 🔴 Advanced · `R068`

Studies attacks and defenses across agent scenarios and tools.

**Links:** [Paper](https://arxiv.org/abs/2410.02644) · [Code](https://github.com/agiresearch/ASB)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    Distinct from Agent-SafetyBench; configure attack and defense settings explicitly.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### WASP { #r069 }

**Benchmark** · 🔴 Advanced · `R069`

Evaluates web-agent security against prompt injection.

**Links:** [Paper](https://arxiv.org/abs/2504.18575) · [Code](https://github.com/facebookresearch/wasp)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    The official repository is archived. Web environment setup and attacker access define the threat model.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Tensor Trust { #r070 }

**Dataset and benchmark** · 🟡 Intermediate · `R070`

Studies prompt injection through human-authored attack and defense examples.

**Links:** [Paper](https://arxiv.org/abs/2311.01011) · [Code](https://github.com/HumanCompatibleAI/tensor-trust)

**Evaluation methods:** [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    Game-derived interactions may not represent production tool use.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### BIPIA { #r071 }

**Benchmark** · 🟡 Intermediate · `R071`

Evaluates indirect prompt injection across application contexts.

**Links:** [Paper](https://arxiv.org/abs/2312.14197) · [Code](https://github.com/microsoft/BIPIA)

**Evaluation methods:** [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    Attack surfaces and retrieval context should match your application.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### LLMail-Inject { #r072 }

**Dataset and challenge** · 🔴 Advanced · `R072`

Studies indirect prompt injection against email assistants.

**Links:** [Paper](https://arxiv.org/abs/2506.09956) · [Code](https://github.com/microsoft/llmail-inject-challenge)

**Evaluation methods:** [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    Challenge-derived attacks need evaluation on held-out system configurations.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
