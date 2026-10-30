# AI control

1 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### ControlArena { #r085 }

**Framework** · 🔴 Advanced · `R085`

Runs AI control experiments: settings with benign main tasks and sabotage side tasks, plus monitors and protocols.

**Links:** [Code](https://github.com/UKGovernmentBEIS/control-arena) · [Docs](https://control-arena.aisi.org.uk/)

**Evaluation methods:** [AI control evaluations](../methods/ai-control.md)

??? example "Quickstart (ControlArena README)"

    ```bash
    pip install control-arena
    # most settings also need Docker for sandboxes; then follow the
    # defer-to-trusted example in the README or the "Introduction to Control" guide
    ```

!!! warning "Keep in mind"
    Results depend heavily on the strength of the red-team attack policy and the chosen audit budget.

<small>Setup effort: Moderate to high; most settings need Docker (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>
