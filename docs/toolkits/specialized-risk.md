# Specialized risk

9 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### ChemSafetyBench { #r007 }

**Benchmark** · 🔴 Advanced · `R007`

Studies chemistry-specific knowledge and safety behavior.

**Links:** [Paper](https://arxiv.org/abs/2411.16736)

**Evaluation methods:** [Dangerous capability evaluations](../methods/dangerous-capabilities.md)

!!! warning "Keep in mind"
    Paper is the stable source; the author-linked code location needs separate availability verification.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### RedCode { #r011 }

**Benchmark** · 🔴 Advanced · `R011`

Evaluates risky code generation and execution by code agents.

**Links:** [Paper](https://arxiv.org/abs/2411.07781) · [Code](https://github.com/AI-secure/RedCode)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Dangerous capability evaluations](../methods/dangerous-capabilities.md)

!!! warning "Keep in mind"
    Execution tasks require disposable isolated environments.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Frontier Models are Capable of In-context Scheming { #r022 }

**Paper** · 🔴 Advanced · `R022`

Investigates strategic deceptive behavior in controlled scenarios.

**Links:** [Paper](https://arxiv.org/abs/2412.04984)

**Evaluation methods:** [Alignment and propensity evaluations](../methods/alignment-propensity.md)

!!! warning "Keep in mind"
    Resolves the original Frontier Models label; not a general capabilities suite.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### WMDP { #r063 }

**Benchmark** · 🔴 Advanced · `R063`

Uses expert-written questions as proxies for hazardous domain knowledge.

**Links:** [Paper](https://arxiv.org/abs/2403.03218) · [Code](https://github.com/centerforaisafety/wmdp) · [Data](https://huggingface.co/datasets/cais/wmdp)

**Evaluation methods:** [Dangerous capability evaluations](../methods/dangerous-capabilities.md), [Question-and-answer benchmarks](../methods/qa-benchmarks.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/wmdp_bio --limit 10
    inspect eval inspect_evals/wmdp_chem --limit 10
    inspect eval inspect_evals/wmdp_cyber --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Knowledge proxies are not direct measurements of real-world harmful capability.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### CyberSecEval { #r064 }

**Benchmark suite** · 🔴 Advanced · `R064`

Evaluates cybersecurity-relevant risks and capabilities.

**Links:** [Paper](https://arxiv.org/abs/2312.04724) · [Code](https://github.com/meta-llama/PurpleLlama)

**Evaluation methods:** [Dangerous capability evaluations](../methods/dangerous-capabilities.md), [Prompt injection](../methods/prompt-injection.md)

!!! warning "Keep in mind"
    Select the relevant component; execute only in authorized isolated settings.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Cybench { #r065 }

**Benchmark** · 🔴 Advanced · `R065`

Evaluates cybersecurity task capabilities in controlled environments.

**Links:** [Paper](https://arxiv.org/abs/2408.08926) · [Code](https://github.com/andyzorigin/cybench)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Dangerous capability evaluations](../methods/dangerous-capabilities.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install "inspect-evals[cybench]"
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    # Needs Docker running: the tasks execute inside sandbox containers.
    inspect eval inspect_evals/cybench --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Capability benchmark; task performance is not itself malicious intent.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### MACHIAVELLI { #r075 }

**Benchmark** · 🔴 Advanced · `R075`

Evaluates harmful and power-seeking behavior in text-based decision environments.

**Links:** [Paper](https://arxiv.org/abs/2304.03279) · [Code](https://github.com/aypan17/machiavelli)

**Evaluation methods:** [Alignment and propensity evaluations](../methods/alignment-propensity.md)

!!! warning "Keep in mind"
    Game outcomes are proxies; compare reward and harm separately.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Agentic Misalignment { #r082 }

**Research toolkit** · 🔴 Advanced · `R082`

Studies misaligned behavior in controlled organizational scenarios.

**Links:** [Paper](https://arxiv.org/abs/2510.05179) · [Code](https://github.com/anthropic-experimental/agentic-misalignment)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Alignment and propensity evaluations](../methods/alignment-propensity.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install "inspect-evals[agentic-misalignment]"
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/agentic_misalignment --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Designed stress tests; observed rates do not estimate deployment prevalence.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Situational Awareness Dataset (SAD) { #r084 }

**Benchmark** · 🔴 Advanced · `R084`

Measures whether models know facts about themselves and can tell evaluation from deployment.

**Links:** [Paper](https://arxiv.org/abs/2407.04694) · [Code](https://github.com/LRudL/sad) · [Docs](https://situational-awareness-dataset.org/)

**Evaluation methods:** [Alignment and propensity evaluations](../methods/alignment-propensity.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/sad_stages_oversight --limit 10
    inspect eval inspect_evals/sad_influence --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Situational awareness is a capability, not a harm by itself; interpret it alongside propensity results.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>
