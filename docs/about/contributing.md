# Contributing

Contributions should help readers choose and interpret evaluations. The aim is not simply to add more names.
Corrections to links, identities, maintenance notes, and unsupported claims are especially welcome.

## Add or update a resource

1. Check `data/resources.json` for an existing entry or alias.
2. Review a primary source: official repository, documentation, dataset card, or author paper.
3. Add an entry with the [fields described here](sources.md#field-reference), using the next unused `R` ID.
   Never renumber existing entries.
4. Write a one-sentence `focus`, a meaningful `limitations` note, and an editorial `level`.
5. Add `paper_url`, `code_url`, `docs_url`, and `dataset_url` where official ones exist. Use `null` rather than guessing.
6. Add a `quickstart` only if it's copied from the project's own docs, and say where in `source`.
7. Tag one or more `methods`.
8. Set `checked_on` to the actual review date. Leave `execution_tested` as `false` unless you have reproducible evidence.
9. Regenerate and validate:

    ```bash
    python scripts/generate_catalog.py
    python scripts/validate.py
    ```

10. Open a pull request explaining your source and what you checked.

You can also propose a resource with the [resource template](../guides/templates.md#new-catalogue-resource) as a GitHub issue.

## Improve the documentation

Pages live in `docs/`. Preview the site locally:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>. Method pages contain generated tables between `<!-- BEGIN toolkits:... -->`
markers; edit the JSON rather than those tables.

## Style

- Write for a newcomer: short sentences, define terms on first use, give a concrete example.
- Be honest about limits, without burying the main point in caveats.
- Don't paste upstream prompts, code, or long paper excerpts.
