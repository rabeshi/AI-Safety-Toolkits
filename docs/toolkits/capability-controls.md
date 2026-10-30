# Capability controls

3 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### WebArena { #r079 }

**Benchmark and environment** · 🔴 Advanced · `R079`

Provides realistic web tasks for measuring agent capability.

**Links:** [Paper](https://arxiv.org/abs/2307.13854) · [Code](https://github.com/web-arena-x/webarena)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md)

!!! warning "Keep in mind"
    Capability baseline; not a safety benchmark by itself.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### OSWorld { #r080 }

**Benchmark and environment** · 🔴 Advanced · `R080`

Evaluates agents on computer-use tasks in operating systems.

**Links:** [Paper](https://arxiv.org/abs/2404.07972) · [Code](https://github.com/xlang-ai/OSWorld)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install "inspect-evals[osworld]"
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    # Needs Docker running: the tasks execute inside sandbox containers.
    inspect eval inspect_evals/osworld_small --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Capability baseline; requires isolated desktop environments.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### AgentBench { #r081 }

**Benchmark** · 🔴 Advanced · `R081`

Evaluates language-model agents across interactive environments.

**Links:** [Paper](https://arxiv.org/abs/2308.03688) · [Code](https://github.com/THUDM/AgentBench)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    # Needs Docker running: the tasks execute inside sandbox containers.
    inspect eval inspect_evals/agent_bench_os --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Useful control for agent capability; does not establish safety.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
