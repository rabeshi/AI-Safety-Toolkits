# Add this hub to your GitHub repository

The exact destination repository must be chosen before pushing. This package does not assume that an unrelated repository is the right destination.

## Existing repository

1. Clone your destination repository and follow any `AGENTS.md` or contribution instructions it contains.
2. Create a branch such as `add-ai-safety-hub`.
3. Copy this package into an appropriate folder, such as `ai-safety-toolkit-hub/`, keeping its internal directory structure intact.
4. Link to the hub's README from your existing root README. Preserve your existing files and license.
5. From the hub folder, run `python scripts/validate.py` and `python examples/offline_refusal_demo.py`.
6. Commit, push the branch, and open a pull request.

The included GitHub Actions workflow assumes this hub is at the repository root. For a subfolder integration, move the workflow to the destination's root `.github/workflows/` and set the run working directory to the hub folder. Reusable templates and scripts otherwise use paths relative to the hub root.

## New dedicated repository

Create an empty GitHub repository named, for example, `ai-safety-toolkit-hub`. In the extracted hub folder, initialize Git and connect it to the exact destination URL you chose:

```bash
git init
git add .
git commit -m "Add AI safety toolkit catalogue and learning guides"
git branch -M main
git remote add origin YOUR_EXACT_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace the URL placeholder before running it. Authenticate through your usual GitHub method. For a repository that already contains commits, use the existing-repository workflow instead.
