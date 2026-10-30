# Validation record

## Release 0.3.0 (October 30, 2026)

- 10 new resources: paper IDs checked against the arXiv API; repositories, documentation sites, and
  Hugging Face datasets checked to exist; Inspect Evals task names (`mask`, `sad_*`, `coconot`) checked against
  the registry. Quickstarts were copied from upstream READMEs.
- All courses, websites, and papers linked from the Foundations pages were checked to resolve (some sites, such as
  ISO and OpenAI, block automated requests and were checked by hand).
- The TransformerLens example on [Interpretability in depth](../foundations/interpretability.md) was run with
  TransformerLens 4.3.0 on CPU. It printed `' London'` and `493 activations cached`, as shown on the page.
  (On Windows, installing into a very deeply nested folder can hit the 260-character path limit; a normal
  virtual environment is fine.)
- `python scripts/validate.py` and `mkdocs build --strict` passed.

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
