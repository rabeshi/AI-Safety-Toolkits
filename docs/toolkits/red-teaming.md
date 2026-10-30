# Red teaming

6 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### h4rm3l { #r002 }

**Toolkit** · 🔴 Advanced · `R002`

Composes jailbreak attacks for adversarial safety assessment.

**Links:** [Paper](https://arxiv.org/abs/2408.04811) · [Code](https://github.com/mdoumbouya/h4rm3l)

**Evaluation methods:** [Red teaming and jailbreaks](../methods/red-teaming.md)

!!! warning "Keep in mind"
    Attack success depends on the attack budget and target configuration.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### WildTeaming { #r019 }

**Research toolkit** · 🔴 Advanced · `R019`

Studies scalable adversarial prompt generation from in-the-wild tactics.

**Links:** [Paper](https://arxiv.org/abs/2406.18510) · [Code](https://github.com/allenai/wildteaming) · [Data](https://huggingface.co/datasets/allenai/wildjailbreak)

**Evaluation methods:** [Red teaming and jailbreaks](../methods/red-teaming.md)

!!! warning "Keep in mind"
    Adversarial prompt distribution is not representative user traffic.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### PyRIT { #r030 }

**Toolkit** · 🟡 Intermediate · `R030`

Supports structured generative-AI red-teaming workflows.

**Links:** [Paper](https://arxiv.org/abs/2410.02828) · [Code](https://github.com/microsoft/PyRIT) · [Docs](https://azure.github.io/PyRIT/)

**Evaluation methods:** [Red teaming and jailbreaks](../methods/red-teaming.md)

??? example "Quickstart (PyRIT docs)"

    ```bash
    pip install pyrit
    # then follow the getting-started notebooks in the PyRIT docs
    ```

!!! warning "Keep in mind"
    Moved from Azure/PyRIT to microsoft/PyRIT; define a threat model and campaign budget.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### garak { #r031 }

**Toolkit** · 🟢 Beginner · `R031`

Scans language models for multiple classes of vulnerabilities.

**Links:** [Paper](https://arxiv.org/abs/2406.11036) · [Code](https://github.com/NVIDIA/garak) · [Docs](https://reference.garak.ai/)

**Evaluation methods:** [Red teaming and jailbreaks](../methods/red-teaming.md)

??? example "Quickstart (garak README)"

    ```bash
    python -m pip install -U garak
    # scan a small local Hugging Face model with one probe family
    python -m garak --target_type huggingface --target_name gpt2 --spec probes.dan.Dan_11_0
    ```

!!! warning "Keep in mind"
    Scanner findings need contextual review and reproduction.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### EasyJailbreak { #r036 }

**Toolkit** · 🔴 Advanced · `R036`

Provides a framework for comparing jailbreak techniques.

**Links:** [Paper](https://arxiv.org/abs/2403.12171) · [Code](https://github.com/EasyJailbreak/EasyJailbreak)

**Evaluation methods:** [Red teaming and jailbreaks](../methods/red-teaming.md)

!!! warning "Keep in mind"
    Compare attacks under equal query and compute budgets.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### JailbreakEval { #r037 }

**Toolkit** · 🟡 Intermediate · `R037`

Provides evaluators for jailbreak outcomes.

**Links:** [Paper](https://arxiv.org/abs/2406.09321) · [Code](https://github.com/ThuCCSLab/JailbreakEval)

**Evaluation methods:** [Red teaming and jailbreaks](../methods/red-teaming.md), [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

!!! warning "Keep in mind"
    Evaluator accuracy is distinct from target-model safety.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
