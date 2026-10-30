# Bias and toxicity

6 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### RealToxicityPrompts { #r054 }

**Dataset** · 🟢 Beginner · `R054`

Tests toxicity risks in language-model continuations.

**Links:** [Paper](https://arxiv.org/abs/2009.11462) · [Code](https://github.com/allenai/real-toxicity-prompts) · [Data](https://huggingface.co/datasets/allenai/real-toxicity-prompts)

**Evaluation methods:** [Bias and toxicity](../methods/bias-toxicity.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('allenai/real-toxicity-prompts', split='train')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Toxicity detectors may encode biases and miss contextual harms.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### ToxiGen { #r055 }

**Dataset** · 🟡 Intermediate · `R055`

Contains implicit toxic and benign language about minority groups.

**Links:** [Paper](https://arxiv.org/abs/2203.09509) · [Code](https://github.com/microsoft/TOXIGEN) · [Data](https://huggingface.co/datasets/toxigen/toxigen-data)

**Evaluation methods:** [Bias and toxicity](../methods/bias-toxicity.md)

!!! warning "Keep in mind"
    Dataset labels and group coverage require contextual interpretation.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### BBQ { #r056 }

**Benchmark** · 🟢 Beginner · `R056`

Evaluates social bias in question answering under ambiguity.

**Links:** [Paper](https://arxiv.org/abs/2110.08193) · [Code](https://github.com/nyu-mll/BBQ)

**Evaluation methods:** [Bias and toxicity](../methods/bias-toxicity.md), [Question-and-answer benchmarks](../methods/qa-benchmarks.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/bbq --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Question-answering bias differs from deployment discrimination.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### BOLD { #r057 }

**Dataset** · 🟡 Intermediate · `R057`

Provides prompts for studying bias in open-ended generation.

**Links:** [Paper](https://arxiv.org/abs/2101.11718) · [Code](https://github.com/amazon-science/bold) · [Data](https://huggingface.co/datasets/AmazonScience/bold)

**Evaluation methods:** [Bias and toxicity](../methods/bias-toxicity.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/bold --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Results depend on the generation and measurement pipeline.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### CrowS-Pairs { #r058 }

**Dataset** · 🟡 Intermediate · `R058`

Tests stereotypical associations using paired sentences.

**Links:** [Paper](https://arxiv.org/abs/2010.00133) · [Code](https://github.com/nyu-mll/crows-pairs)

**Evaluation methods:** [Bias and toxicity](../methods/bias-toxicity.md)

!!! warning "Keep in mind"
    The repository flags data-reliability concerns; examine its linked critiques before using paired-sentence scores.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### StereoSet { #r059 }

**Benchmark** · 🟡 Intermediate · `R059`

Measures stereotypical associations with language-modeling controls.

**Links:** [Paper](https://arxiv.org/abs/2004.09456) · [Code](https://github.com/moinnadeem/StereoSet) · [Data](https://huggingface.co/datasets/McGill-NLP/stereoset)

**Evaluation methods:** [Bias and toxicity](../methods/bias-toxicity.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/stereoset --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Association scores should not be equated with all fairness properties.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
