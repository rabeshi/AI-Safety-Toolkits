# Interpretability-based evaluation

!!! abstract "In one sentence"
    Look *inside* the model, at its internal activations, to detect things its outputs might not show, such as deception or hazardous knowledge.

## Why it matters

Every other method on this site treats the model as a black box: input in, output out. But a model could give a
safe-looking answer while internally "knowing" something different, or behave well only because it detects a
test. Interpretability methods try to read the model's internal state directly. This research area is still
young, so results should be treated as promising evidence, not proof.

## The main approaches

| Approach | Idea | Example use |
| --- | --- | --- |
| **Linear probes** | Train a simple classifier on internal activations to detect a concept | Flag when a model is being deceptive ([Goldowsky-Dill et al.](https://arxiv.org/abs/2502.03407)) |
| **Representation reading / steering** | Find directions in activation space for concepts like honesty, then measure or change them | [Representation Engineering](https://arxiv.org/abs/2310.01405) |
| **Unlearning checks** | Test whether "removed" hazardous knowledge is truly gone, or just hidden | WMDP's RMU method plus probing |
| **Sparse autoencoders / features** | Decompose activations into interpretable features and audit them | Searching for features related to deception or bias |

## How it works (linear probe)

1. **Requires model weights.** You need an open-weights model so you can record activations.
2. **Build a labelled dataset**: examples where you know the model is, say, lying vs. honest.
3. **Record activations** at a chosen layer for each example.
4. **Train a probe** (often logistic regression) to separate the two classes.
5. **Test on new, different situations**. The key question is whether the probe generalises beyond its training setup.
6. **Report detection quality** (AUROC, false-positive rate at a fixed recall).

## Common mistakes

- **Probing for the wrong thing.** A "deception" probe might really detect "the prompt mentions lying".
- **Testing only in-distribution.** Probes often fail on new scenarios.
- **Treating a probe as a guarantee.** A negative result doesn't prove absence.

## Toolkits for this method

<!-- BEGIN toolkits:interpretability -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [Neuronpedia](../toolkits/interpretability.md#r089) | A free website for browsing and searching sparse-autoencoder features of open models, no code needed. | 🟢 Beginner | [Code](https://github.com/hijohnnylin/neuronpedia) · [Docs](https://neuronpedia.org/) |
| [nnsight](../toolkits/interpretability.md#r087) | Reads and edits the internals of PyTorch and Hugging Face models during a forward pass. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2407.14561) · [Code](https://github.com/ndif-team/nnsight) · [Docs](https://nnsight.net/) |
| [TransformerLens](../toolkits/interpretability.md#r086) | Loads language models with hooks on every activation, for mechanistic interpretability research. | 🟡 Intermediate | [Code](https://github.com/TransformerLensOrg/TransformerLens) · [Docs](https://transformerlensorg.github.io/TransformerLens/) |
| [SAELens](../toolkits/interpretability.md#r088) | Trains, loads, and analyses sparse autoencoders that split model activations into interpretable features. | 🔴 Advanced | [Code](https://github.com/decoderesearch/SAELens) · [Docs](https://decoderesearch.github.io/SAELens/) |
<!-- END toolkits -->

For a full introduction to the field, see [Interpretability in depth](../foundations/interpretability.md).

## Key papers

- Zou et al., [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) (2023)
- Goldowsky-Dill et al., [Detecting Strategic Deception Using Linear Probes](https://arxiv.org/abs/2502.03407) (2025)
- Li et al., [The WMDP Benchmark](https://arxiv.org/abs/2403.03218) (2024): includes the RMU unlearning method.
- Anwar et al., [Foundational Challenges in Assuring Alignment and Safety of LLMs](https://arxiv.org/abs/2404.09932) (2024): survey covering interpretability's role.
