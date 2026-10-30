# Interpretability in depth

**Interpretability** is the science of understanding what happens inside a neural network: which internal
computations produce a given output, and what concepts the model represents. If we could reliably read a model's
internals, we could check for hidden goals or deception directly, instead of relying only on its behaviour.

This page is a guided introduction. For how interpretability is used *as an evaluation*, see
[interpretability-based evaluation](../methods/interpretability.md).

## Why it's hard

A language model is billions of numbers. Its "thinking" is a sequence of activation vectors, lists of thousands of
numbers per word, passing through layers. Nothing in it is labelled. Worse, individual neurons usually don't
mean one thing: a single neuron might respond to French text, DNA sequences, *and* legal citations.

## Core ideas, in order

### 1. Features and superposition

A **feature** is a concept the model represents, like "this text is in French" or "this is a Python string".
Models represent **more features than they have neurons** by storing them as overlapping directions in activation
space. This is called **superposition**, and it's why single neurons look confusing.

*Read:* Elhage et al., [Toy Models of Superposition](https://arxiv.org/abs/2209.10652) (2022). It's long but
foundational; start with the introduction.

### 2. Sparse autoencoders (SAEs)

An SAE is a small network trained to rewrite a model's activations as a combination of a few active features out
of many thousands. This "unpacks" superposition into features that are often interpretable: one for the Golden
Gate Bridge, one for code bugs, one for deception-related text.

*Read:* Cunningham et al., [Sparse Autoencoders Find Highly Interpretable Features](https://arxiv.org/abs/2309.08600)
(2023); Anthropic's [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features) and
[Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/).

**Try it with no code:** browse real SAE features on [Neuronpedia](https://neuronpedia.org/). Search a concept,
see which texts activate it, and steer a model with it.

### 3. Circuits

A **circuit** is a set of components (attention heads, neurons, features) that together implement a specific
behaviour. Finding circuits means tracing *how* an answer is computed, not just which features are active.

*Read:* Olah et al., [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) (2020);
Wang et al., [Interpretability in the Wild](https://arxiv.org/abs/2211.00593) (2022), which traces a full circuit in GPT-2.

### 4. Causal interventions

Seeing that a feature is active isn't proof it *matters*. Interventions test causation:

- **Activation patching:** copy an activation from one input into another and see if the output changes.
- **Ablation:** remove a component and see what breaks.
- **Steering:** add a feature direction to make the model behave differently.

*Read:* Meng et al., [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262) (2022).

### 5. Probing and representation reading

Train a simple classifier on activations to detect a concept, such as whether a statement is true or whether the
model is being deceptive. Cheaper than full circuit analysis and directly useful for monitoring. See
[interpretability-based evaluation](../methods/interpretability.md).

## Hands-on: your first look inside a model

You need Python and about 1 GB of disk space. GPT-2 small runs fine on a laptop CPU.

```bash
pip install transformer_lens
```

```python
from transformer_lens.model_bridge import TransformerBridge

# Load GPT-2 small (downloads ~500 MB the first time)
bridge = TransformerBridge.boot_transformers("gpt2", device="cpu")

# Run the model and keep every internal activation
logits, activations = bridge.run_with_cache("The Eiffel Tower is in the city of")

# What does the model predict next?
print(bridge.to_string(logits[0, -1].argmax()))
```

This uses the [TransformerLens](../toolkits/interpretability.md#r086) 4.x API from its README. Many older tutorials
use `HookedTransformer.from_pretrained`, which was removed in version 4.0; see the
[migration guide](https://TransformerLensOrg.github.io/TransformerLens/content/migrating_to_v4.html) if you follow one of them.

**Then:** work through ARENA's interpretability chapter ([open materials](https://github.com/ARENA-education/ARENA_materials)),
or Neel Nanda's [mechanistic interpretability quickstart](https://www.neelnanda.io/mechanistic-interpretability/quickstart).

## Tools

| Tool | Use it for | Level |
| --- | --- | --- |
| [Neuronpedia](../toolkits/interpretability.md#r089) | Browse and search SAE features in the browser | 🟢 |
| [TransformerLens](../toolkits/interpretability.md#r086) | Hooks on every activation; the standard research library | 🟡 |
| [nnsight](../toolkits/interpretability.md#r087) | Read and edit internals of any PyTorch/Hugging Face model, including remote large models | 🟡 |
| [SAELens](../toolkits/interpretability.md#r088) | Train and analyse sparse autoencoders | 🔴 |

## Limits to keep in mind

- Interpretations are **hypotheses**. A feature labelled "deception" may really track something correlated.
- Most results are on small models or narrow behaviours; scaling to full frontier models is unsolved.
- Absence of evidence isn't evidence of absence: not finding a "deception feature" doesn't prove there's no deception.

*Survey:* Bereska & Gavves, [Mechanistic Interpretability for AI Safety: A Review](https://arxiv.org/abs/2404.14082) (2024).
Ongoing research: [Transformer Circuits Thread](https://transformer-circuits.pub/).

**Next:** [Governance and policy](governance.md)
