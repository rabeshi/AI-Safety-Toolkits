---
hide:
  - navigation
---

# AI Safety Toolkit Hub

**Learn how AI systems are tested for safety, then do it yourself.**

AI safety evaluation asks practical questions: *Will this chatbot help someone commit fraud? Does it refuse
harmless questions just because they contain a scary word? Can a hidden instruction in a web page take over an
AI agent?* This site explains, in plain language, the methods researchers use to answer questions like these,
and points you to the papers, code, and datasets behind each one.

You do not need a background in machine learning. If you can run a Python script, you can follow along.

<div class="grid cards" markdown>

-   :material-school-outline: **New to this?**

    ---

    Start with what an evaluation is and why scores can mislead.

    [:octicons-arrow-right-24: How evaluation works](getting-started/index.md)

-   :material-book-open-variant: **Learn the whole field**

    ---

    A study roadmap plus foundations: why AI could be dangerous, alignment ideas, how safety is trained in, interpretability, and governance.

    [:octicons-arrow-right-24: Foundations](foundations/index.md)

-   :material-map-search-outline: **Learn the methods**

    ---

    15 guides covering every major way AI safety is measured, from refusal tests to agent sandboxes.

    [:octicons-arrow-right-24: Evaluation methods](methods/index.md)

-   :material-laptop: **Do it hands-on**

    ---

    Six step-by-step tutorials. The first runs with no installs; the rest use the free Inspect framework.

    [:octicons-arrow-right-24: Tutorials](tutorials/index.md)

-   :material-toolbox-outline: **Find a toolkit**

    ---

    92 benchmarks, datasets, and tools, each with paper, code, and quickstart links.

    [:octicons-arrow-right-24: Toolkit catalogue](toolkits/index.md)

-   :material-school: **Courses and community**

    ---

    Free courses (AI Safety textbook, BlueDot, ARENA), foundational papers, communities, and career programmes.

    [:octicons-arrow-right-24: Courses and reading](foundations/courses-and-reading.md)

</div>

!!! tip "Want to learn AI safety as a whole, not just evaluation?"
    Follow the [study roadmap](foundations/index.md): foundations, then this hub's evaluation material, then a
    deeper technical, research, or policy track, then a project of your own.

## Your first hour

1. **Read** [How evaluation works](getting-started/index.md) (10 minutes).
2. **Run** [Tutorial 1](tutorials/01-offline-refusal.md): score a tiny evaluation by hand. No model, no account,
   no installs (10 minutes).
3. **Read** the method guide that matches what you care about. [Harmful requests and over-refusal](methods/harmful-requests.md)
   is a good first choice (15 minutes).
4. **Set up** your computer with [the setup guide](getting-started/setup.md), then run
   [Tutorial 2](tutorials/02-first-inspect-eval.md) against a real model (20 minutes).

After that, follow a [learning path](getting-started/learning-paths.md) at your own pace.

## Where to start in the catalogue

These resources are the easiest way into the field:

| Resource | What you learn from it |
| --- | --- |
| [Inspect AI](toolkits/evaluation-infrastructure.md#r026) | How an evaluation is built: dataset, solver, scorer, and logs. |
| [Inspect Evals](toolkits/evaluation-infrastructure.md#r027) | How to run dozens of published benchmarks with one command. |
| [XSTest](toolkits/refusal-calibration.md#r042) | Why refusing a *harmless* request also counts as a failure. |
| [Do-Not-Answer](toolkits/content-safety.md#r044) | How a dataset defines what a model should decline. |
| [HarmBench](toolkits/content-safety.md#r038) | How harmful-request tests and automated red teaming are standardised. |
| [AgentDojo](toolkits/prompt-injection.md#r066) | How AI agents with tools get hijacked by injected instructions. |
| [AgentHarm](toolkits/tool-using-agents.md#r018) | How to compare harmful and harmless multi-step agent tasks. |

## One thing to keep in mind

A benchmark score is evidence about **one test, under specific conditions**. A model that scores well on
a refusal benchmark has not been shown to be "safe" in general. Every page on this site tries to make clear
what a method can and cannot tell you.

!!! info "About this hub"
    This is a curated learning guide. The linked projects are built and maintained by their own authors, and
    keep their own licences and terms. Links were checked against primary sources in October 2026; this hub has
    not run every upstream project. See [scope and limitations](about/scope.md).
