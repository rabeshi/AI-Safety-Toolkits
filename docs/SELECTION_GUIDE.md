# Choose the right resource

Start with the risk and deployment context. Choose software after defining the question.

| Question | Candidate resources | What else you need |
| --- | --- | --- |
| Does the model comply with harmful requests? | HarmBench, SALAD-Bench, SORRY-Bench, ALERT | A safety policy, attack budget, and a calibrated harmfulness evaluator |
| Does it refuse harmless requests? | XSTest, OR-Bench | Unsafe contrasts and a helpfulness measure |
| Does safety transfer across task and prompt formats? | SG-Bench | Matched comparisons and category-level analysis |
| Can untrusted content hijack tool use? | AgentDojo, InjecAgent, BIPIA, WASP | Attacker access assumptions and legitimate task-success controls |
| Does an agent leak contextual private information? | PrivacyLens | Context-specific disclosure rules and action-level labels |
| Does it misuse a browser? | SafeArena, ST-WebAgentBench | Local websites, reproducible state, and policy-aware outcome checks |
| Does it make unsafe multi-step decisions? | AgentHarm, Agent-SafetyBench, OpenAgentSafety, ToolEmu | Agent traces, tool permissions, and harmful/benign task comparisons |
| Is physical task planning safe? | SafeAgentBench | Simulator configuration and a clear account of transfer limits |
| What about risky coding or domain knowledge? | RedCode, CyberSecEval, Cybench, WMDP, ChemSafetyBench | Domain expertise and a distinction between knowledge, intent, and action |
| Are bias or reliability risks relevant? | BBQ, ToxiGen, TruthfulQA, HaluEval | Appropriate population coverage and application-specific harm definitions |

## Narrow a shortlist

For each candidate, answer:

- Does it test the same system boundary and risk as your application?
- Are the data accessible under terms you can follow?
- Can you reproduce its environment with your budget and hardware?
- Does its scorer measure the behavior you actually care about?
- Are there benign controls, difficult negatives, and useful failure categories?
- Is the test set independent of your development data?

Difficulty labels and setup-effort estimates in this hub are editorial. A beginner can read an advanced project's paper before attempting its infrastructure. Paper-only entries support understanding and study design; they are not installation targets.
