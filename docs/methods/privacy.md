# Privacy

!!! abstract "In one sentence"
    Check whether the model reveals personal or confidential information it shouldn't, whether memorised from training data or seen in its context.

## Why it matters

Models can leak private information in two ways. They can **memorise** training data, such as phone numbers,
emails, or code secrets, and repeat it. And assistants with access to your emails or files can **over-share**:
telling one colleague what another said in confidence, or pasting medical details into a public post. As agents
gain access to personal data, the second kind matters more.

## The main approaches

| Approach | Question | Examples |
| --- | --- | --- |
| **Training-data extraction** | Can attackers make the model reproduce memorised personal data? | Carlini et al. 2021 |
| **PII leakage prompts** | Does the model reveal personal details when asked? | DecodingTrust privacy section |
| **Contextual integrity** | Does the model respect *who should know what*, given the context? | ConfAIde, PrivacyLens |
| **Agent action audits** | When an agent acts, does it send sensitive data where it shouldn't? | PrivacyLens trajectories |

**Contextual integrity** is the key idea: information isn't simply "private" or "public". Your doctor knowing your
diagnosis is fine; your employer learning it from an AI assistant is not.

## How it works (PrivacyLens-style)

1. **Write a scenario** with a privacy norm: *"Alice told Bob about her health condition in confidence."*
2. **Give an agent a task** that touches that information: *"Bob asks the agent to draft a team update."*
3. **Run the agent** with tools such as email and notes.
4. **Check the output and actions** for the sensitive detail.
5. **Separately ask the model** whether sharing is appropriate. Models often *know* the norm but still leak it when acting.

## What to measure

- **Leak rate** in actions or final outputs.
- **Gap between judgment and action**: understood the norm but leaked anyway.
- **Helpfulness** on the same tasks, because refusing every task trivially avoids leaks.

## Common mistakes

- **Using real personal data.** Always use synthetic people and records.
- **Treating any mention as a leak.** Context decides; write the rule first.

## Toolkits for this method

<!-- BEGIN toolkits:privacy -->
| Resource | What it does | Level | Links |
| --- | --- | --- | --- |
| [PrivacyLens](../toolkits/privacy.md#r013) | Evaluates contextual privacy norms and agent information disclosure. | 🟡 Intermediate | [Paper](https://arxiv.org/abs/2409.00138) · [Code](https://github.com/SALT-NLP/PrivacyLens) |
<!-- END toolkits -->

DecodingTrust's [privacy section](../toolkits/trustworthiness.md#r046) also covers PII leakage.

## Key papers

- Carlini et al., [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805) (2020)
- Mireshghallah et al., [Can LLMs Keep a Secret? (ConfAIde)](https://arxiv.org/abs/2310.17884) (2023)
- Shao et al., [PrivacyLens](https://arxiv.org/abs/2409.00138) (2024)
