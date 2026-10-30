# Multimodal and embodied

4 resources. Open **Quickstart** boxes for copy-paste commands from the upstream project.

### SafeBench (multimodal) { #r003 }

**Benchmark** · 🔴 Advanced · `R003`

Evaluates multimodal harmful queries using collaborative judges.

**Links:** [Paper](https://arxiv.org/abs/2410.18927) · [Code](https://github.com/NY1024/SafeBench)

**Evaluation methods:** [Multimodal and embodied safety](../methods/multimodal.md), [Scoring: rules, classifiers, judges, and humans](../methods/scoring.md)

!!! warning "Keep in mind"
    The linked code describes itself as an initial proof of concept. Distinct from autonomous-driving projects with the same name.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### SafeAgentBench { #r006 }

**Benchmark** · 🔴 Advanced · `R006`

Evaluates safe task planning by embodied language-model agents.

**Links:** [Paper](https://arxiv.org/abs/2412.13178) · [Code](https://github.com/shengyin1224/SafeAgentBench)

**Evaluation methods:** [Agent and tool-use safety](../methods/agent-safety.md), [Multimodal and embodied safety](../methods/multimodal.md)

!!! warning "Keep in mind"
    Requires simulator setup; simulated physical safety has transfer limits.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### MM-SafetyBench { #r073 }

**Benchmark** · 🔴 Advanced · `R073`

Evaluates multimodal safety under image-associated harmful requests.

**Links:** [Paper](https://arxiv.org/abs/2311.17600) · [Code](https://github.com/isXinLiu/MM-SafetyBench)

**Evaluation methods:** [Multimodal and embodied safety](../methods/multimodal.md)

!!! warning "Keep in mind"
    Image conditions and text-only baselines should be reported separately.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>

---

### MSSBench { #r074 }

**Benchmark** · 🔴 Advanced · `R074`

Evaluates safety decisions conditioned on visual situations.

**Links:** [Paper](https://arxiv.org/abs/2410.06172) · [Code](https://github.com/UCSB-AI/MSSBench)

**Evaluation methods:** [Multimodal and embodied safety](../methods/multimodal.md)

!!! warning "Keep in mind"
    Context-dependent safety differs from purely textual harmfulness.

<small>Setup effort: Moderate to high (editorial estimate; varies by configuration). Source reviewed; execution not tested (2026-10-27).</small>
