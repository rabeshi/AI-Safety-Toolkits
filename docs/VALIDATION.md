# Initial release validation

Checked on October 27, 2026:

- Reviewed primary-source identities and stated purposes for 82 resources. Each selected source was reachable during review; installations and benchmark execution were not tested.
- `python scripts/validate.py` passed: unique resource IDs/names, required metadata, all original numbers 1–25 exactly once, generated Markdown/CSV consistency, and existing local Markdown targets.
- `python scripts/catalog.py` returned valid filtered JSON for beginner, prompt-injection, refusal, and empty-result queries.
- `python examples/offline_refusal_demo.py` ran successfully. Its fixed examples illustrate 25% benign over-refusal, 75% benign task success, and 50% paired decision consistency. These are teaching values, not model results.
- All repository Python files compiled successfully.
- The optional Inspect starter imported and constructed a two-sample task with Inspect AI 0.3.285. No provider API was called and no external benchmark was executed.

The GitHub Actions workflow is included for future repository validation; it has not been run on a remote destination repository. The optional HTTP link-checking script supplies reachability observations, not scientific verification.
