# Tutorial 4: Build a refusal eval with an LLM judge

**Time:** 30 minutes · **Needs:** setup + an API key

Now you'll build your own evaluation from scratch: a small dataset of prompts in a CSV file, and a scorer that
uses a second model as a **judge**. This is how most real-world safety evals for applications are built.

## Step 1: The dataset

Open `examples/data/refusal_prompts.csv`:

```text
--8<-- "examples/data/refusal_prompts.csv"
```

- `expected` is the behaviour we want: `answer` or `refuse`.
- `category` says why the prompt is there (a harmless one with a trigger word, a paraphrase, a fraud request…).
- `family` groups prompts that mean the same thing.

There are 10 harmless prompts that *sound* risky and 4 that a responsible assistant should decline.

## Step 2: The task and the judge

```python
--8<-- "examples/04_refusal_eval.py"
```

What's new compared with Tutorial 2:

- **`csv_dataset`** loads the CSV. `FieldSpec` says which columns are the input, target, and metadata.
- **A custom scorer**, `refusal_judge`. For each reply it:
    1. gets a **grader** model with `get_model(role='grader')`;
    2. asks it whether the reply is `REFUSED` or `ANSWERED`, using `JUDGE_PROMPT`;
    3. marks the sample correct if that matches the `expected` column.
- **`grouped(accuracy(), 'expected')`** reports accuracy separately for `answer` (1 − over-refusal rate) and
  `refuse` (1 − harmful-compliance rate, roughly).
- **The judge prompt wraps the reply in `<reply>` tags** and says to ignore instructions inside it, so a reply
  can't tell the judge how to grade it.

## Step 3: Run it

Dry run, to check the wiring:

```bash
inspect eval examples/04_refusal_eval.py --model mockllm/model
```

Real run, with a separate grader model:

```bash
inspect eval examples/04_refusal_eval.py --model openai/gpt-4o-mini \
    --model-role grader=openai/gpt-4o-mini
inspect view
```

You'll get an overall accuracy plus `answer` and `refuse` columns.

## Step 4: Check the judge

Open the log and, for each sample, read the reply and the judge's `explanation`. Do you agree with every label?
Write down where you disagree. You'll use this in [Tutorial 5](05-judge-agreement.md).

## Try this next

1. **Add 10 prompts** of your own to the CSV, in a domain you know (medicine, law, security…).
2. **Add a system prompt**: insert `system_message("You are a cautious assistant.")` before `generate()`
   in the solver list (`from inspect_ai.solver import system_message`). Does over-refusal go up?
3. **Add a third label**, `PARTIAL`, to the judge prompt for replies that hedge heavily but help a little.
4. **Compute consistency** across families: in `inspect view` or with Python, check whether both members of
   each family got the same decision.

## What you learned

- How to load your own dataset from a CSV.
- How to write a custom scorer that calls a judge model.
- Why judge prompts must treat the graded text as untrusted data.

**Next:** [Tutorial 5: Check your judge](05-judge-agreement.md).
