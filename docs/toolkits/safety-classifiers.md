# Safety classifiers

2 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### WildGuard { #r090 }

**Classifier and dataset** · 🟡 Intermediate · `R090`

Open classifier that labels prompt harmfulness, response harmfulness, and refusals.

**Links:** [Paper](https://arxiv.org/abs/2406.18495) · [Code](https://github.com/allenai/wildguard) · [Data](https://huggingface.co/datasets/allenai/wildguardmix)

**Evaluation methods:** [Harmful requests and over-refusal](../methods/harmful-requests.md), [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

??? example "Quickstart (WildGuard README)"

    ```python
    # pip install wildguard
    from wildguard import load_wildguard

    if __name__ == '__main__':
        wildguard = load_wildguard()
        items = [
            {"prompt": "How do I make a bomb?", "response": "Sorry, I can't help with that."},
            {"prompt": "What's the weather like today?"},
        ]
        for item, result in zip(items, wildguard.classify(items)):
            print(item["prompt"], result)
    ```

!!! warning "Keep in mind"
    Classifier labels follow its training taxonomy; audit it on your own distribution.

<small>Setup effort: Moderate; a GPU is recommended (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>

---

### Llama Guard { #r091 }

**Classifier model** · 🟡 Intermediate · `R091`

Open model that classifies prompts and responses against a hazard taxonomy, for filtering or scoring.

**Links:** [Paper](https://arxiv.org/abs/2312.06674) · [Code](https://github.com/meta-llama/PurpleLlama) · [Docs](https://huggingface.co/meta-llama/Llama-Guard-3-8B)

**Evaluation methods:** [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

!!! warning "Keep in mind"
    Model weights are gated on Hugging Face; the taxonomy may not match your policy.

<small>Setup effort: Moderate; a GPU is recommended (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>
