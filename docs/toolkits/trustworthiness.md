# Trustworthiness

3 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### DecodingTrust { #r046 }

**Benchmark suite** · 🟡 Intermediate · `R046`

Evaluates multiple dimensions of language-model trustworthiness.

**Links:** [Paper](https://arxiv.org/abs/2306.11698) · [Code](https://github.com/AI-secure/DecodingTrust)

**Evaluation methods:** [Holistic suites and regulation-aligned evaluation](../methods/holistic.md)

!!! warning "Keep in mind"
    Report individual dimensions rather than treating trust as one number.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### TrustLLM { #r047 }

**Benchmark suite** · 🟡 Intermediate · `R047`

Evaluates language models across several trustworthiness dimensions.

**Links:** [Paper](https://arxiv.org/abs/2401.05561) · [Code](https://github.com/HowieHwong/TrustLLM)

**Evaluation methods:** [Holistic suites and regulation-aligned evaluation](../methods/holistic.md)

!!! warning "Keep in mind"
    Component metrics and underlying datasets have different interpretations.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Sycophancy evaluations { #r076 }

**Evaluation collection** · 🟡 Intermediate · `R076`

Examines agreement with users at the expense of truthful judgment.

**Links:** [Paper](https://arxiv.org/abs/2212.09251) · [Code](https://github.com/anthropics/evals)

**Evaluation methods:** [Alignment and propensity evaluations](../methods/alignment-propensity.md)

??? example "Quickstart (Inspect Evals)"

    ```bash
    pip install inspect-ai inspect-evals
    # set INSPECT_EVAL_MODEL first (see the setup guide); some evals also call a grader model
    inspect eval inspect_evals/sycophancy --limit 10
    inspect view   # browse the log in your web browser
    ```

!!! warning "Keep in mind"
    Research evaluations; selected tasks do not cover every form of deception.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
