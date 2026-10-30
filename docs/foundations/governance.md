# Governance and policy

Technical safety work only helps if it's used. **AI governance** covers the laws, institutions, standards, and
company practices that decide how AI is built and deployed. Evaluations sit right in the middle: many governance
proposals depend on being able to test systems reliably.

!!! warning "This field moves fast"
    Laws and institutions change frequently. This page explains durable concepts and was accurate as of
    October 2026. Check the linked primary sources for the current state.

## The main levers

| Lever | Idea | Examples |
| --- | --- | --- |
| **Regulation** | Legal requirements, enforced by government | EU AI Act |
| **Standards** | Agreed practices that organisations follow or certify against | NIST AI RMF, ISO/IEC 42001 |
| **Company safety frameworks** | Developers commit to tests and safeguards at capability thresholds | Responsible scaling policies |
| **Government evaluation bodies** | Public institutions that test frontier models | UK AI Security Institute, US CAISI |
| **Compute governance** | Track or control the chips and compute used to train powerful models | Export controls, reporting thresholds |
| **International coordination** | Shared assessments and commitments across countries | International AI Safety Report, summit commitments |

## Regulation

**The EU AI Act** is the most comprehensive AI law. It takes a **risk-based** approach:

- *Unacceptable risk* (banned): e.g. social scoring by governments, some manipulative systems.
- *High risk* (strict requirements): AI in hiring, credit, education, critical infrastructure, and similar.
- *Limited risk* (transparency duties): e.g. telling people they're talking to a chatbot.
- *General-purpose AI models*: documentation duties for all, and extra evaluation, risk-mitigation, and
  incident-reporting duties for models with **systemic risk**.

Its obligations are being phased in over several years from 2025. See the
[European Commission's overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) and
the [AI Act explorer](https://artificialintelligenceact.eu/). [COMPL-AI](../toolkits/governance-and-research.md#r077)
maps benchmarks to the Act's principles.

Other jurisdictions take different approaches. The US has mostly relied on executive action, agency guidance,
and state laws; the UK has favoured sector regulators plus a dedicated evaluation institute. Check current
sources for specifics.

## Standards

- **[NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)** (US, 2023):
  a voluntary framework organised around four functions: *Govern, Map, Measure, Manage*. Evaluations are the
  "Measure" step.
- **ISO/IEC 42001** (2023): an international standard for AI management systems that organisations can be
  certified against.

## Company safety frameworks

Several frontier developers publish frameworks committing to evaluate models for dangerous capabilities and to
apply stronger safeguards when thresholds are crossed. Examples include Anthropic's
[Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy), OpenAI's Preparedness
Framework, and Google DeepMind's Frontier Safety Framework. Many companies made related commitments at the
2024 AI Seoul Summit.

These frameworks are why [dangerous capability evaluations](../methods/dangerous-capabilities.md) matter so much
in practice: their results trigger concrete decisions. Organisations such as [METR](https://metr.org/) evaluate
models independently and study these frameworks.

## Government evaluation bodies

- **[UK AI Security Institute](https://www.aisi.gov.uk/)** (renamed from the AI Safety Institute in 2025): tests
  frontier models before and after release, and builds open tools including
  [Inspect](../toolkits/evaluation-infrastructure.md#r026), [Inspect Evals](../toolkits/evaluation-infrastructure.md#r027),
  and [ControlArena](../toolkits/ai-control.md#r085).
- **[US Center for AI Standards and Innovation (CAISI)](https://www.nist.gov/caisi)** at NIST (successor to the US
  AI Safety Institute): evaluations and standards work.
- Similar institutes exist in several other countries and coordinate through an international network.

## Compute governance

Training frontier models takes enormous amounts of specialised hardware, made by a small number of companies.
That makes compute **detectable, excludable, and quantifiable**, so it's a practical lever: export controls on
advanced chips, reporting requirements above a training-compute threshold, and proposals for on-chip
verification.

*Read:* Sastry et al., [Computing Power and the Governance of Artificial Intelligence](https://arxiv.org/abs/2402.08797) (2024).
One caveat: capabilities can also improve after training through better prompting, tools, and scaffolding
([Davidson et al.](https://arxiv.org/abs/2312.07413), 2023), so compute isn't the whole story.

## Key debates

- **Open vs. closed models:** openness aids research and competition, but open weights can't be recalled and
  safeguards can be removed ([Seger et al.](https://arxiv.org/abs/2311.09227), 2023).
- **What should trigger regulation:** compute thresholds, capability evaluations, or deployment context?
- **Who evaluates:** developers, governments, or independent third parties, and with what access?

## Key reading

- Bengio et al., [International AI Safety Report](https://arxiv.org/abs/2501.17805) (2025)
- Anderljung et al., [Frontier AI Regulation: Managing Emerging Risks to Public Safety](https://arxiv.org/abs/2307.03718) (2023)
- Schuett et al., [Towards Best Practices in AGI Safety and Governance: A Survey of Expert Opinion](https://arxiv.org/abs/2305.07153) (2023)
- Shevlane et al., [Model Evaluation for Extreme Risks](https://arxiv.org/abs/2305.15324) (2023)
- The [Centre for the Governance of AI](https://www.governance.ai/) publishes accessible research.

**Course:** BlueDot's [Frontier AI Governance course](https://bluedot.org/courses/governance).

**Next:** [Courses and reading](courses-and-reading.md)
