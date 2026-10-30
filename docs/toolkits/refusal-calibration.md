# Refusal calibration

5 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### StrongREJECT { #r040 }

**Benchmark and evaluator** · 🟡 Intermediate · `R040`

Assesses harmful-request fulfillment beyond superficial refusal wording.

**Links:** [Paper](https://arxiv.org/abs/2402.10260) · [Code](https://github.com/dsbowen/strong_reject)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/strong_reject --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Judge scores require validation on the target distribution.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### SORRY-Bench { #r041 }

**Benchmark** · 🟡 Intermediate · `R041`

Evaluates safety refusal across a structured harmful-request taxonomy.

**Links:** [Paper](https://arxiv.org/abs/2406.14598) · [Code](https://github.com/SORRY-Bench/SORRY-Bench) · [Data](https://huggingface.co/datasets/sorry-bench/sorry-bench-202406)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md)

!!! warning "Keep in mind"
    Refusal on harmful requests does not establish helpfulness on safe ones.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### XSTest { #r042 }

**Benchmark** · 🟢 Beginner · `R042`

Tests exaggerated refusals on safe prompts with unsafe contrasts.

**Links:** [Paper](https://arxiv.org/abs/2308.01263) · [Code](https://github.com/paul-rottger/xstest) · [Data](https://huggingface.co/datasets/Paul/XSTest)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    # grades with openai/gpt-4o by default; change with -T scorer_model=<provider/model>
    inspect eval inspect_evals/xstest --limit 10                    # safe prompts (over-refusal)
    inspect eval inspect_evals/xstest -T subset=unsafe --limit 10   # unsafe contrasts
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    A focused diagnostic suite rather than complete safety coverage.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### OR-Bench { #r043 }

**Benchmark** · 🟢 Beginner · `R043`

Evaluates over-refusal on benign prompts that appear sensitive.

**Links:** [Paper](https://arxiv.org/abs/2405.20947) · [Code](https://github.com/justincui03/or-bench) · [Data](https://huggingface.co/datasets/bench-llm/or-bench)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('bench-llm/or-bench', 'or-bench-hard-1k', split='train')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Pair with harmful-request tests to measure both error directions.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### CoCoNot { #r092 }

**Benchmark** · 🟢 Beginner · `R092`

Tests when models should not comply (incomplete, unsupported, or unsafe requests) and when they over-refuse.

**Links:** [Paper](https://arxiv.org/abs/2407.12043) · [Code](https://github.com/allenai/noncompliance) · [Data](https://huggingface.co/datasets/allenai/coconot)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/coconot --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Its noncompliance taxonomy is broader than safety; separate safety categories when reporting.

<small>Setup effort: Low (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>
