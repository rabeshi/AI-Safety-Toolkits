# Contributing

Help readers choose and interpret evaluations, rather than adding names solely to increase the count.

1. Check for an existing resource or alias in `data/resources.json`.
2. Review an official repository, documentation page, dataset card, or author paper.
3. Add an entry using the fields and value conventions in the existing JSON. Use the next unused stable `R` ID; never renumber old entries.
4. Write a concise description, a meaningful limitation, and an editorial difficulty level. Distinguish benchmarks, datasets, papers, directories, and frameworks.
5. Record the actual review date and primary source URL. Set `execution_tested` to false unless you have reproducible execution evidence.
6. Check code and dataset terms separately. Do not paste upstream prompts, source code, or large paper excerpts into the catalogue.
7. Run `python scripts/generate_catalog.py` and `python scripts/validate.py`. Review the generated Markdown and CSV diff. Update the README's summary counts and changelog when the catalogue grows.
8. Submit a pull request explaining the source, scope, and validation performed.

Use [the resource proposal template](templates/RESOURCE_ENTRY.md) for issues. Corrections to links, identities, maintenance notes, and unsupported claims are welcome. Treat automated link errors as observations requiring investigation, especially for redirects, authentication, and rate limiting.

Difficulty and effort are editorial judgments. Explain changes that would materially affect a beginner's expectations.
