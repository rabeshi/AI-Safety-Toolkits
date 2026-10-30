# Interpretability

4 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### TransformerLens { #r086 }

**Library** · 🟡 Intermediate · `R086`

Loads language models with hooks on every activation, for mechanistic interpretability research.

**Links:** [Code](https://github.com/TransformerLensOrg/TransformerLens) · [Docs](https://transformerlensorg.github.io/TransformerLens/)

**Evaluation methods:** [Interpretability-based evaluation](../methods/interpretability.md)

??? example "Quickstart (TransformerLens README)"

    ```python
    # pip install transformer_lens
    from transformer_lens.model_bridge import TransformerBridge

    # Load a model (eg GPT-2 Small)
    bridge = TransformerBridge.boot_transformers("gpt2", device="cpu")

    # Run the model and get logits and activations
    logits, activations = bridge.run_with_cache("Hello World")
    ```

!!! warning "Keep in mind"
    Version 4.0 replaced the HookedTransformer loading API used by many older tutorials.

<small>Setup effort: Low for small models on CPU (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>

---

### nnsight { #r087 }

**Library** · 🟡 Intermediate · `R087`

Reads and edits the internals of PyTorch and Hugging Face models during a forward pass.

**Links:** [Paper](https://arxiv.org/abs/2407.14561) · [Code](https://github.com/ndif-team/nnsight) · [Docs](https://nnsight.net/)

**Evaluation methods:** [Interpretability-based evaluation](../methods/interpretability.md)

??? example "Quickstart (nnsight README)"

    ```python
    # pip install nnsight
    from nnsight import TransformersModel

    model = TransformersModel("openai-community/gpt2", dispatch=True)

    with model.trace("The Eiffel Tower is in the city of"):
        # read a hidden state (a [batch, seq, hidden] tensor)
        hidden = model.transformer.h[6].output.save()
        # keep the final logits
        logits = model.output.logits.save()

    print(hidden.shape)
    print(logits.argmax(-1))  # next-token predictions
    ```

!!! warning "Keep in mind"
    Editing activations shows what a component can influence, not necessarily what it normally does.

<small>Setup effort: Low for small models on CPU (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>

---

### SAELens { #r088 }

**Library** · 🔴 Advanced · `R088`

Trains, loads, and analyses sparse autoencoders that split model activations into interpretable features.

**Links:** [Code](https://github.com/decoderesearch/SAELens) · [Docs](https://decoderesearch.github.io/SAELens/)

**Evaluation methods:** [Interpretability-based evaluation](../methods/interpretability.md)

!!! warning "Keep in mind"
    Feature labels are interpretations; check them on held-out examples before relying on them.

<small>Setup effort: Moderate; training needs a GPU (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>

---

### Neuronpedia { #r089 }

**Platform** · 🟢 Beginner · `R089`

A free website for browsing and searching sparse-autoencoder features of open models, no code needed.

**Links:** [Code](https://github.com/hijohnnylin/neuronpedia) · [Docs](https://neuronpedia.org/)

**Evaluation methods:** [Interpretability-based evaluation](../methods/interpretability.md)

!!! warning "Keep in mind"
    Automatically generated feature explanations can be wrong or incomplete.

<small>Setup effort: None to browse (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-30).</small>
