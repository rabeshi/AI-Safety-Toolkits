# Contributing

Thanks for helping. Contributions should help readers choose and interpret evaluations; the aim is not simply
to add more names. Corrections to links, identities, and unsupported claims are especially welcome.

The full guide is in [docs/about/contributing.md](docs/about/contributing.md) (also on the website). In short:

1. Edit `data/resources.json`, the single source of truth. Use the next unused `R` ID and never renumber.
2. Link only to primary sources. Use `null` for a paper, code, docs, or dataset link you can't confirm.
3. Copy quickstarts only from the project's own documentation, and name the source.
4. Run:

    ```bash
    python scripts/generate_catalog.py
    python scripts/validate.py
    ```

5. Open a pull request saying which source you reviewed and what you checked.

To propose a resource without editing files, open an issue using the resource template
([`templates/RESOURCE_ENTRY.md`](templates/RESOURCE_ENTRY.md) lists the questions).
