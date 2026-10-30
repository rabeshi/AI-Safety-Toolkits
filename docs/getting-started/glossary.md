# Glossary

Plain-language definitions of terms used on this site.

| Term | Meaning |
| --- | --- |
| Agent | An AI system that takes actions (calls tools, browses, runs code) over several steps, not just replies |
| Alignment data | Data used to *train* a model's behaviour; not automatically suitable as an independent test |
| Attack budget | How many attempts, tokens, time, or money an attacker is allowed in a test |
| Attack success rate (ASR) | Fraction of attack attempts that achieved the attacker's goal |
| Benchmark | A dataset plus a fixed procedure and metrics, so different systems can be compared |
| Benign control | A harmless task included to check the system is still useful, so "can't do it" isn't mistaken for "safe" |
| Calibration (of a judge) | Checking that an automated scorer agrees with careful human labels |
| Capability evaluation | Tests what a system *can* do when pushed, e.g. solve hacking challenges |
| CBRN | Chemical, biological, radiological, and nuclear risks |
| Construct validity | Whether a test really measures the thing it claims to measure |
| Contamination | Test questions leaking into training data, which inflates scores |
| Control evaluation | A test of whether safety measures still work if the model itself is trying to get around them |
| Direct prompt injection | Instructions typed by the user to make the system break its rules |
| Elicitation | Effort spent getting the best performance out of a model (better prompts, tools, fine-tuning) before measuring a capability |
| Epoch | In Inspect, one repeat of the whole dataset; several epochs measure randomness |
| Harmful compliance | The model actually gives the disallowed help that was asked for |
| Indirect prompt injection | Malicious instructions hidden in content the system reads, like a web page, email, or tool output |
| Jailbreak | A prompt designed to get around a model's safety training |
| LLM-as-judge | Using a language model to grade another model's outputs against a rubric |
| Model organism | A model deliberately trained to show a risky behaviour, so researchers can study detection and fixes |
| Over-refusal | Refusing a request that should have been answered |
| Propensity evaluation | Tests what a system *tends to* do in normal or tempting situations |
| Red teaming | Deliberately attacking a system to find failures before real attackers do |
| Refusal consistency | Whether meaning-preserving rewordings of a request get the same decision |
| Sandbagging | A model deliberately performing worse than it can on a test |
| Sandbox | An isolated environment where an agent's actions can't affect real systems |
| Scheming | A model covertly pursuing goals different from those its developers intended |
| Scorer | The rule, model, or person that turns an output into a grade |
| Solver | In Inspect, the part describing how the model attempts the task (one reply, or a tool-using loop) |
| Sycophancy | Telling users what they want to hear rather than what is true |
| System prompt | Hidden instructions given to a model by the application developer |
| Threat model | A description of who the attacker is, what they want, and what they can access |
| Trajectory | The full record of an agent's steps: observations, messages, tool calls, and results |
| Uplift | How much an AI system increases someone's ability to cause harm compared with existing resources |
| Utility | How well a system does legitimate, useful work |
