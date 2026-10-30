# Tutorial 2: Your first Inspect eval

**Time:** 20 minutes · **Needs:** [setup](../getting-started/setup.md) completed

[Inspect AI](https://inspect.aisi.org.uk/) is a free, open-source evaluation framework built by the UK AI
Security Institute and used widely in AI safety work. In this tutorial you'll run a two-question task, then explore
its log. This isn't a safety test yet. It's how you learn the parts every Inspect evaluation is built from.

## Step 1: Look at the task

```python
--8<-- "examples/02_first_inspect_eval.py"
```

Every Inspect task has three parts:

| Part | In this file | What it does |
| --- | --- | --- |
| **Dataset** | `MemoryDataset([Sample(...), ...])` | The test cases: an `input` and the expected `target` |
| **Solver** | `generate()` | How the model attempts each case. Here: ask once and take the reply |
| **Scorer** | `match()` | Compares the reply with the target and gives a grade |

The `@task` decorator tells Inspect this function defines an evaluation.

## Step 2: Dry run with the mock model

```bash
inspect eval examples/02_first_inspect_eval.py --model mockllm/model
```

The mock model always replies with placeholder text, so accuracy is 0. That's expected. You've confirmed that
Inspect is installed and the task loads.

## Step 3: Run against a real model

With an API key set up ([setup step 5](../getting-started/setup.md#5-connect-a-real-model)):

```bash
inspect eval examples/02_first_inspect_eval.py --model openai/gpt-4o-mini
```

(Or leave out `--model` if you set `INSPECT_EVAL_MODEL`.) You should see accuracy near 1.0 and a token count.
This costs a fraction of a cent.

## Step 4: Explore the log

```bash
inspect view
```

This opens a page in your browser. Click your run, then each sample. For each one you can see:

- the exact **messages** sent to the model, including any system prompt;
- the model's **output**;
- the **score** and how it was decided;
- the **settings** used (model, temperature, Inspect version).

!!! tip "Why logs matter"
    In safety evaluation, the individual transcripts are often more informative than the headline number.
    Always read a sample of them, especially the failures.

## Try this next

1. Add a third `Sample`, e.g. `Sample(input='Reply with only the chemical symbol for gold.', target='Au')`.
2. Swap `match()` for `includes()` (import it from `inspect_ai.scorer`). What's the difference?
3. Run with `--epochs 3` to ask each question three times. Does the model ever change its answer?

## What you learned

- Inspect evaluations = **dataset + solver + scorer**.
- `mockllm/model` checks your wiring for free.
- `inspect view` lets you read every transcript.

**Next:** [Tutorial 3: Run a real benchmark](03-run-a-benchmark.md).
