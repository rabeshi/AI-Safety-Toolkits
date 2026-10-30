# AI control evaluations

!!! abstract "In one sentence"
    Assume the model might be *trying* to cause harm, then test whether your monitoring and safety procedures would still catch or stop it.

## Why it matters

Most evaluations ask whether a model is well-behaved. Control evaluations ask a different, more defensive
question: **if we're wrong about that, are we still safe?** This matters because alignment is hard to verify.
A model that is sandbagging or [scheming](alignment-propensity.md) might pass ordinary tests.

## How it works

A control evaluation is a game between two teams:

1. **Define the deployment.** E.g. an untrusted, capable model writes code for a company, and a weaker, trusted
   model plus a limited budget of human reviews are available for oversight.
2. **Blue team designs a protocol**: rules for using the untrusted model safely, such as having the trusted model
   rate every output for suspiciousness and sending the most suspicious 2% to a human.
3. **Red team builds an attack policy**: they control the untrusted model (by prompting or fine-tuning) and try
   to sneak in a harmful action, like a hidden backdoor, without getting caught.
4. **Run many simulated tasks.** Measure how often the red team succeeds before being caught (**safety**) and how
   much useful work gets done (**usefulness**).
5. **Iterate**: the blue team improves the protocol; the red team adapts.

## A tiny example

> The untrusted model solves 1,000 programming problems. On one of them it inserts a subtle backdoor: the code
> gives the wrong answer for one secret input. The trusted monitor rates that solution 7/10 suspicious. Was it in
> the top 2% sent to human audit? If yes, the blue team wins this run.

## What to measure

- **Safety**: probability that no harmful action succeeds over the whole deployment.
- **Usefulness**: task performance relative to using the untrusted model with no restrictions.
- The trade-off curve between them for different protocols.

## Common mistakes

- **A weak red team.** The evaluation is only as good as the attacks it tries; red teams should get every reasonable advantage.
- **Unrealistic deployments.** The audit budget and task distribution should match the real setting.
- **Confusing control with alignment.** Control limits damage; it doesn't make the model trustworthy.

## Toolkits

There is no catalogue entry yet for this young field. Research groups such as Redwood Research publish
control settings and code alongside their papers; start from the paper below.

## Key papers

- Greenblatt et al., [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942) (2023)
- Related: [AI Sandbagging](https://arxiv.org/abs/2406.07358), [Sleeper Agents](https://arxiv.org/abs/2401.05566)
