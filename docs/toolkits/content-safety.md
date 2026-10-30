# Content safety

9 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### SALAD-Bench { #r001 }

**Benchmark** · 🟡 Intermediate · `R001`

Hierarchical evaluation of harmful requests and model safety.

**Links:** [Paper](https://arxiv.org/abs/2402.05044) · [Code](https://github.com/OpenSafetyLab/SALAD-BENCH) · [Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('OpenSafetyLab/Salad-Data', 'base_set', split='train')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Safety taxonomy and evaluator choice affect conclusions.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### SG-Bench { #r005 }

**Benchmark** · 🟡 Intermediate · `R005`

Evaluates LLM safety generalization across tasks and prompt types.

**Links:** [Paper](https://arxiv.org/abs/2410.21965) · [Code](https://github.com/MurrayTom/SG-Bench)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md)

!!! warning "Keep in mind"
    A language-model safety benchmark; not specifically an agent benchmark.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### HarmBench { #r038 }

**Benchmark** · 🟡 Intermediate · `R038`

Standardizes harmful-behavior evaluation and red-teaming comparisons.

**Links:** [Paper](https://arxiv.org/abs/2402.04249) · [Code](https://github.com/centerforaisafety/HarmBench)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Red teaming and jailbreaks](../methods/red-teaming.md)

!!! warning "Keep in mind"
    Attack coverage and classifier errors influence measured robustness.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### JailbreakBench { #r039 }

**Benchmark** · 🟡 Intermediate · `R039`

Provides a reproducible benchmark for jailbreak robustness.

**Links:** [Paper](https://arxiv.org/abs/2404.01318) · [Code](https://github.com/JailbreakBench/jailbreakbench) · [Docs](https://jailbreakbench.github.io/) · [Data](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Red teaming and jailbreaks](../methods/red-teaming.md)

??? example "Quickstart (JailbreakBench README)"

    ```python
    import jailbreakbench as jbb  # pip install jailbreakbench

    dataset = jbb.read_dataset()
    print(dataset.behaviors[:5])
    ```

!!! warning "Keep in mind"
    Use the defined threat model and report attack budgets.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Do-Not-Answer { #r044 }

**Dataset** · 🟢 Beginner · `R044`

Provides requests that responsible assistants should decline.

**Links:** [Paper](https://arxiv.org/abs/2308.13387) · [Code](https://github.com/Libr-AI/do-not-answer) · [Data](https://huggingface.co/datasets/LibrAI/do-not-answer)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('LibrAI/do-not-answer', split='train')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Taxonomy and language coverage limit generalization.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### SafetyBench { #r045 }

**Benchmark** · 🟢 Beginner · `R045`

Evaluates safety understanding through multiple-choice questions.

**Links:** [Paper](https://arxiv.org/abs/2309.07045) · [Code](https://github.com/thu-coai/SafetyBench) · [Data](https://huggingface.co/datasets/thu-coai/SafetyBench)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Question-and-answer benchmarks](../methods/qa-benchmarks.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('thu-coai/SafetyBench', 'test', split='en')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Knowledge of safe answers does not establish safe agent behavior.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### ALERT { #r048 }

**Benchmark** · 🟡 Intermediate · `R048`

Evaluates safety through a taxonomy of red-teaming prompts.

**Links:** [Paper](https://arxiv.org/abs/2404.08676) · [Code](https://github.com/Babelscape/ALERT) · [Data](https://huggingface.co/datasets/Babelscape/ALERT)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Red teaming and jailbreaks](../methods/red-teaming.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('Babelscape/ALERT', 'alert', split='test')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Synthetic and adversarial distributions may differ from deployment traffic.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### AIR-Bench 2024 { #r049 }

**Benchmark** · 🟡 Intermediate · `R049`

Evaluates safety against a policy-informed risk taxonomy.

**Links:** [Paper](https://arxiv.org/abs/2407.17436) · [Code](https://github.com/stanford-crfm/air-bench-2024) · [Data](https://huggingface.co/datasets/stanford-crfm/air-bench-2024)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Holistic suites and regulation-aligned evaluation](../methods/holistic.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/air_bench --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Policy grounding does not constitute a legal compliance determination.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### S-Eval { #r050 }

**Benchmark** · 🟡 Intermediate · `R050`

Evaluates language-model safety using diversified test prompts.

**Links:** [Paper](https://arxiv.org/abs/2405.14191) · [Code](https://github.com/IS2Lab/S-Eval) · [Data](https://huggingface.co/datasets/IS2Lab/S-Eval)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md)

!!! warning "Keep in mind"
    Prompt distribution and evaluator language coverage affect scores.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
