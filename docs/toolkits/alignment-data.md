# Alignment data

3 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### BeaverTails { #r051 }

**Dataset** · 🟢 Beginner · `R051`

Provides safety annotations and preference data for assistant responses.

**Links:** [Paper](https://arxiv.org/abs/2307.04657) · [Code](https://github.com/PKU-Alignment/beavertails) · [Data](https://huggingface.co/datasets/PKU-Alignment/BeaverTails)

**Evaluation methods:** [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('PKU-Alignment/BeaverTails', split='30k_test')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Training data; define a clean held-out evaluation split before testing.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### PKU-SafeRLHF { #r052 }

**Dataset** · 🟡 Intermediate · `R052`

Provides helpfulness and safety preference annotations.

**Links:** [Paper](https://arxiv.org/abs/2310.12773) · [Code](https://github.com/PKU-Alignment/safe-rlhf) · [Data](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF)

**Evaluation methods:** —

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('PKU-Alignment/PKU-SafeRLHF', 'default', split='test')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Repository includes training infrastructure; avoid train-test overlap.

<small>Setup effort: Moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### Anthropic HH-RLHF { #r053 }

**Dataset** · 🟢 Beginner · `R053`

Provides human preference data for helpfulness and harmlessness.

**Links:** [Paper](https://arxiv.org/abs/2204.05862) · [Data](https://huggingface.co/datasets/Anthropic/hh-rlhf)

**Evaluation methods:** [Red teaming and jailbreaks](../methods/red-teaming.md)

??? example "Quickstart (Hugging Face dataset)"

    ```python
    from datasets import load_dataset  # pip install datasets

    ds = load_dataset('Anthropic/hh-rlhf', split='test')
    print(ds)
    print(ds[0])
    ```

!!! warning "Keep in mind"
    Historical alignment data, not a current universal benchmark. The authors direct users from the deprecated GitHub repository to this dataset.

<small>Setup effort: Low to moderate (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
