# Roadmap

## Done

- 82 primary-source-reviewed resources, with separate paper, code, docs, and dataset links.
- 15 evaluation-method guides and 6 hands-on tutorials.
- A documentation website with a filterable catalogue and copy-paste quickstarts.
- Generated exports, validation, and CI for both the catalogue and the site.

## Next

1. **Run the quickstarts.** Execute each quickstart with pinned versions and mark `execution_tested` only with evidence.
2. **Fill method gaps in the catalogue:** AI control settings, interpretability tooling, honesty (MASK),
   situational awareness (SAD), and newer cyber benchmarks already in Inspect Evals.
3. **Notebook versions** of the tutorials for people who prefer Jupyter or Google Colab.
4. **Multilingual and regional coverage**, with reviewers who understand the relevant context.
5. **Example reports** showing a complete small study, from plan to write-up.

## Review cycle

Before each release, recheck changed or new links, look for renamed or archived projects, and review changed
scope claims. `python scripts/check_links.py` helps, but status codes aren't a substitute for reading the source.

Only update review dates when a source is actually reviewed. Keep resource IDs stable.
