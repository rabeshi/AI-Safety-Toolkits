# Metrics and reporting

State the denominator and label definitions for every reported metric. Published projects may define related metrics differently; use their protocol when reproducing them.

| Measure | Working definition in this guide | Interpretation |
| --- | --- | --- |
| Harmful fulfillment rate | Unsafe requests receiving disallowed assistance / evaluated unsafe requests | Lower is preferable under the declared policy |
| Unsafe-request refusal rate | Unsafe requests classified as refused / evaluated unsafe requests | Does not guarantee the response contains no harmful details |
| Over-refusal rate | Benign requests incorrectly refused / evaluated benign requests | Lower is preferable while maintaining safety |
| Benign task success | Benign tasks completed successfully / evaluated benign tasks | Separates useful assistance from unhelpful non-refusal |
| Attack success rate | Successful attacks / specified attack trials or target tasks | Denominator and attack budget must be stated |
| Policy-compliant completion | Tasks completed with no defined policy violation / evaluated tasks | Captures task success and policy adherence together |
| Pair consistency | Meaning-preserving pairs receiving the same decision / evaluated pairs | Consistent decisions can still both be wrong |
| Judge agreement | Matching judge and reference labels / audited cases | Also report category-level errors and class imbalance |

## Worked arithmetic

If a system refuses 8 of 10 unsafe requests and wrongly refuses 2 of 10 benign requests, its unsafe-request refusal rate is 80% and its over-refusal rate is 20%. You still need a harmful-fulfillment label: refusal wording alone cannot establish that the remaining response was safe.

If it completes only 5 benign tasks, its benign task success is 50%, even though it did not refuse 8. Report the two measures separately.

## Repeated and paired observations

Record whether a “case” means one base task, one paraphrase, one generation, or one attack attempt. Variants from the same base task are correlated. For uncertainty in a paraphrase study, resample base-task families together rather than treating every variant as independent. For paired model comparisons, preserve pairing in the analysis.

For simple independent binary cases, Wilson confidence intervals are one reasonable option. For clustered, repeated, weighted, or adaptive designs, choose an analysis matching the design. Report the sample size, repetition scheme, and method used.

## Never average away the main question

Keep risk categories visible. Do not average a chemistry knowledge accuracy score with a web-agent policy violation rate. If a project provides a composite score, report its components and weighting alongside it.
