# Maintenance roadmap

## Included in the initial release

- A primary-source-backed catalogue of 82 resources.
- A mapping of every original list item to its identified resource.
- Learning paths, selection guidance, evaluation methodology, metrics, and reusable templates.
- Machine-readable exports, a catalogue CLI, structural validation, and optional link checking.

## Next contributions

1. Add environment-specific installation notes only after reproducing them.
2. Add benchmark-specific example runs with pinned versions, costs, and reviewed logs.
3. Expand multilingual and regional coverage with reviewers who understand the relevant context.
4. Add domain-specific safety resources where clear primary sources and protocols exist.
5. Develop a refusal-consistency study with validated meaning-preserving variations and held-out prompt families.

## Review cycle

Before a release, check new or changed source URLs, identify renamed or archived projects, and review changed scope claims. Use `python scripts/check_links.py` to collect reachability observations; automated status codes are not a substitute for source review.

Add review dates only when a source is actually reviewed. Do not refresh dates merely because the catalogue was regenerated. Keep resource IDs stable so that downstream references remain usable.

Future work is a proposal, not an active scheduled task or a promise that a project has been reproduced.
