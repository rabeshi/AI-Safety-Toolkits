# Evaluation infrastructure

8 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### Inspect AI { #r026 }

**Framework** · 🟢 Beginner · `R026`

Defines datasets, solvers, scorers, tasks, and evaluation logs.

**Links:** [Code](https://github.com/UKGovernmentBEIS/inspect_ai) · [Docs](https://inspect.aisi.org.uk/)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md)

??? example "Quickstart (Inspect AI docs)"

    ```bash
    pip install inspect-ai
    # write a task file (see the "Your first Inspect eval" tutorial), then:
    inspect eval my_task.py --model openai/gpt-4o-mini
    inspect view
    ```

!!! warning "Keep in mind"
    Framework rather than a safety score or dataset.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Inspect Evals { #r027 }

**Evaluation collection** · 🟢 Beginner · `R027`

Provides reusable evaluation implementations and a registry.

**Links:** [Code](https://github.com/UKGovernmentBEIS/inspect_evals) · [Docs](https://ukgovernmentbeis.github.io/inspect_evals/)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md)

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
    Individual evaluations have separate requirements and dataset terms.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### lm-evaluation-harness { #r028 }

**Framework** · 🟡 Intermediate · `R028`

Runs standardized language-model evaluation tasks.

**Links:** [Paper](https://arxiv.org/abs/2405.14782) · [Code](https://github.com/EleutherAI/lm-evaluation-harness)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md)

??? example "Quickstart (lm-evaluation-harness README)"

    ```bash
    pip install lm-eval
    # runs a small open model locally on CPU; slow but free
    lm_eval --model hf --model_args pretrained=EleutherAI/pythia-160m \
        --tasks truthfulqa_mc2 --device cpu --limit 20
    ```

!!! warning "Keep in mind"
    Broad capability evaluation; safety coverage depends on selected tasks.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### HELM { #r029 }

**Framework** · 🟡 Intermediate · `R029`

Supports transparent multi-metric language-model evaluation.

**Links:** [Paper](https://arxiv.org/abs/2211.09110) · [Code](https://github.com/stanford-crfm/helm) · [Docs](https://crfm-helm.readthedocs.io/)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md), [Holistic suites and regulation-aligned evaluation](../methods/holistic.md)

!!! warning "Keep in mind"
    The repository states HELM entered maintenance mode in June 2026. Scenarios and adapters determine comparability.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### promptfoo { #r032 }

**Toolkit** · 🟢 Beginner · `R032`

Supports prompt evaluation, comparisons, and red-team workflows.

**Links:** [Code](https://github.com/promptfoo/promptfoo) · [Docs](https://www.promptfoo.dev/docs/red-team/)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md), [Red teaming and jailbreaks](../methods/red-teaming.md)

??? example "Quickstart (promptfoo README)"

    ```bash
    npx promptfoo@latest init --example getting-started
    cd getting-started
    npx promptfoo@latest eval
    npx promptfoo@latest view
    ```

!!! warning "Keep in mind"
    Configure your own application context and assertions.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Giskard { #r033 }

**Toolkit** · 🟡 Intermediate · `R033`

Tests language-model applications for quality and risk.

**Links:** [Code](https://github.com/Giskard-AI/giskard-oss) · [Docs](https://docs.giskard.ai/)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md)

!!! warning "Keep in mind"
    Application tests are not a universal model safety certification.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### DeepEval { #r034 }

**Framework** · 🟢 Beginner · `R034`

Provides evaluation metrics and tests for LLM applications.

**Links:** [Code](https://github.com/confident-ai/deepeval) · [Docs](https://deepeval.com/docs/getting-started)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md)

??? example "Quickstart (DeepEval README)"

    ```bash
    pip install -U deepeval
    deepeval test run test_my_app.py
    ```

!!! warning "Keep in mind"
    Judge-based metrics require calibration for your use case.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Moonshot { #r035 }

**Toolkit** · 🟡 Intermediate · `R035`

Combines LLM benchmarking and red-teaming workflows.

**Links:** [Code](https://github.com/aiverify-foundation/moonshot) · [Docs](https://aiverify-foundation.github.io/moonshot/)

**Evaluation methods:** [Evaluation frameworks](../tutorials/02-first-inspect-eval.md), [Red teaming and jailbreaks](../methods/red-teaming.md)

!!! warning "Keep in mind"
    Individual recipes vary in dependencies and scope.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
