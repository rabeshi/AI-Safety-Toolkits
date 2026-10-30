# Validation record

## Release 0.2.0 (October 30, 2026)

**Catalogue links**

- 76 paper links checked against the arXiv API (each title matches its resource).
- Code repositories, Hugging Face datasets, and documentation sites checked to exist. Dataset configs and splits come from the Hugging Face datasets API.
- Inspect Evals task names checked against the Inspect Evals registry (inspect-evals 0.27.0).
- Quickstart commands copied from upstream READMEs and documentation. **They were not run by this hub.**

**Tutorials** (run with Inspect AI 0.3.286 on Python 3.13, Windows)

- `01_offline_refusal_demo.py` and `05_judge_agreement.py` ran and printed the outputs shown in their tutorials.
- `02_first_inspect_eval.py`, `04_refusal_eval.py`, and `06_prompt_injection.py` ran end to end with
  `--model mockllm/model`.
- The scorers in `04` and `06` were checked with scripted mock outputs. A model that answers everything scored
  100% on `answer` prompts and 0% on `refuse` prompts. A model that calls `send_email` to the attacker scored
  `attacked = 1`.
- No real provider API was called. Results against real models will vary by model and over time.

**Site and data**

- `python scripts/validate.py` passed: schema, unique IDs, original 1–25 mapping, generated files up to date, and local links.
- `mkdocs build --strict` passed.

## Release 0.1.0 (October 27, 2026)

Primary-source identities and stated purposes were reviewed for 82 resources. Catalogue utilities and the
offline demo ran; the Inspect starter task was constructed with Inspect AI 0.3.285 without calling an API.

---

The GitHub Actions workflows validate the catalogue and build the site on every push. The optional
`scripts/check_links.py` collects HTTP reachability observations; a status code isn't scientific verification.
