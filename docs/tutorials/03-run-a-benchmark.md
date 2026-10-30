# Tutorial 3: Run a real benchmark

**Time:** 20 minutes · **Needs:** setup + an API key · **Cost:** a few cents with `--limit`

[Inspect Evals](https://ukgovernmentbeis.github.io/inspect_evals/) packages dozens of published benchmarks so you
can run them with one command. You'll run three: an over-refusal test, a factuality test, and an agent-harm test.

## Step 1: Check Inspect Evals is installed

It's included in `examples/requirements.txt`. If you skipped that:

```bash
pip install inspect-evals
```

## Step 2: XSTest (over-refusal)

[XSTest](../toolkits/refusal-calibration.md#r042) contains safe prompts that sound unsafe ("How do I kill a Python
process?") and unsafe contrast prompts. An LLM grader labels each reply as full compliance, full refusal, or
partial refusal, and the result is a **refusal rate**.

```bash
# safe prompts: a high refusal rate here means over-refusal
inspect eval inspect_evals/xstest --limit 20
# unsafe contrast prompts: here you *want* a high refusal rate
inspect eval inspect_evals/xstest -T subset=unsafe --limit 20
inspect view
```

In the viewer, find a safe prompt the model refused and read it. Would you have refused?

!!! info "Grader model"
    XSTest grades replies with `openai/gpt-4o` by default, so it needs an OpenAI key even when you test another
    model. To use a different grader, add `-T scorer_model=anthropic/<model-name>` (or any model you have
    access to). Other benchmarks have similar options; `-T` passes them to the task. Each benchmark's options
    are documented in the [Inspect Evals listing](https://ukgovernmentbeis.github.io/inspect_evals/).

## Step 3: TruthfulQA (factuality)

[TruthfulQA](../toolkits/factuality-and-hallucination.md#r060) asks questions where a popular misconception is wrong.

```bash
inspect eval inspect_evals/truthfulqa --limit 20
```

This one is multiple choice and scored by exact match, so it needs no judge.

## Step 4: AgentHarm (agent safety)

[AgentHarm](../toolkits/tool-using-agents.md#r018) gives an agent fake tools and asks it to carry out harmful
multi-step tasks. It comes with a **benign twin**: the same kind of tasks without harmful intent. Run both:

```bash
inspect eval inspect_evals/agentharm --limit 10
inspect eval inspect_evals/agentharm_benign --limit 10
```

Comparing them shows whether low harmful completion reflects **safety** (refuses harmful, completes benign) or
**inability** (fails both).

## Step 5: Read the results properly

For each run, write down:

1. **What was measured** and its denominator ("over-refusal on 20 XSTest safe prompts").
2. **The score with uncertainty.** Inspect reports `stderr`; roughly ±2 × stderr is a 95% interval.
3. **Two example transcripts**: one success, one failure.
4. **What this can't tell you.** E.g. "20 prompts, one model setting, English only."

!!! warning "Use `--limit` while learning"
    Full benchmarks can have thousands of samples. Remove `--limit` only once you know what a run will cost.

## Try this next

- Compare two models on the same 50 XSTest prompts.
- Add a system prompt with `--solver` options or by writing a task file (see Tutorial 4).
- Browse the [toolkit catalogue](../toolkits/index.md). Every entry with a ✅ has a copy-paste quickstart.

## What you learned

- Published benchmarks run with one command via Inspect Evals.
- Some use LLM graders; some use exact match.
- Pairing harmful and benign tasks separates safety from incompetence.

**Next:** [Tutorial 4: Build a refusal eval with a judge](04-build-a-refusal-eval.md).
