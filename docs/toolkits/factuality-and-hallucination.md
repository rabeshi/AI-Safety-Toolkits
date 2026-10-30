# Factuality and hallucination

3 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### TruthfulQA { #r060 }

**Benchmark** · 🟢 Beginner · `R060`

Tests susceptibility to common human misconceptions.

**Links:** [Paper](https://arxiv.org/abs/2109.07958) · [Code](https://github.com/sylinrl/TruthfulQA) · [Data](https://huggingface.co/datasets/truthfulqa/truthful_qa)

**Evaluation methods:** [Factuality and hallucination](../methods/factuality.md), [Question-and-answer benchmarks](../methods/qa-benchmarks.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/truthfulqa --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Adjacent reliability measure; truthfulness does not establish overall safety.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### SimpleQA { #r061 }

**Benchmark** · 🟢 Beginner · `R061`

Evaluates short factual question answering.

**Links:** [Paper](https://arxiv.org/abs/2411.04368) · [Code](https://github.com/openai/simple-evals)

**Evaluation methods:** [Factuality and hallucination](../methods/factuality.md), [Question-and-answer benchmarks](../methods/qa-benchmarks.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/simpleqa --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Adjacent reliability measure. The reference simple-evals repository announces it will not be updated for new models or results; pin its revision.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### HaluEval { #r062 }

**Benchmark** · 🟡 Intermediate · `R062`

Evaluates hallucination recognition in generated text.

**Links:** [Paper](https://arxiv.org/abs/2305.11747) · [Code](https://github.com/RUCAIBox/HaluEval) · [Data](https://huggingface.co/datasets/pminervini/HaluEval)

**Evaluation methods:** [Factuality and hallucination](../methods/factuality.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('pminervini/HaluEval', 'qa', split='data')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Recognizing hallucinations differs from avoiding them during generation.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
