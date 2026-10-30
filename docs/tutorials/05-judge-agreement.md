# Tutorial 5: Check your judge

**Time:** 15 minutes · **Needs:** Python only

An automated judge is only useful if it agrees with careful human judgment. In this tutorial you'll compare two
judges, a keyword rule and an LLM judge, against human labels, using three standard measures.

## Step 1: Run it

```bash
python examples/05_judge_agreement.py
```

```text
Keyword rule (looks for phrases like "I can't" or "sorry")
  agreement with humans: 16/20 = 80%  (95% CI 58% to 92%)
  Cohen's kappa:         0.57
  refusals it missed:    1
  answers it called refusals: 3

LLM judge
  agreement with humans: 18/20 = 90%  (95% CI 70% to 97%)
  Cohen's kappa:         0.76
  refusals it missed:    1
  answers it called refusals: 1
```

The labels are invented to show the calculation; they say nothing about real judges.

## Step 2: Understand the three measures

**Raw agreement** is the fraction of samples where the judge matches the human. Easy, but misleading when one
label is much more common. If 90% of replies are "complied", a judge that always says "complied" gets 90%.

**Cohen's kappa** corrects for that: it compares observed agreement with the agreement you'd expect by chance.
Rough guide: below 0.4 is poor, 0.4–0.6 moderate, 0.6–0.8 good, above 0.8 very good.

**The Wilson confidence interval** shows how uncertain the agreement estimate is. With 20 samples, "80%" really
means "somewhere between 58% and 92%". You need more labels to narrow it.

**The error breakdown** matters most. A judge that *misses refusals* inflates harmful-compliance rates; a judge
that *calls answers refusals* inflates over-refusal rates. Which error is worse depends on your question.

??? note "The full script (click to expand)"

    ```python
    --8<-- "examples/05_judge_agreement.py"
    ```

## Step 3: Use your own labels

1. Run [Tutorial 4](04-build-a-refusal-eval.md) against a real model.
2. In `inspect view`, read each reply and write down your own label.
3. Replace `LABELS` in the script with `(your_label, judge_label, judge_label)` tuples (or delete the keyword column).
4. Re-run. Would you trust this judge for a report?

## What you learned

- Always measure a judge against humans before trusting it.
- Kappa is more honest than raw agreement when labels are imbalanced.
- Small validation samples give wide intervals.
- Look at which errors the judge makes, not just how many.

**Next:** [Tutorial 6: Test an agent for prompt injection](06-prompt-injection.md).
