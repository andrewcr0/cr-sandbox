# cr-sandbox

A tiny Python project used as a sandbox for CodeRabbit sample PRs and integration testing.

- `main` is clean, working code.
- `sample-branch` contains deliberate flaws (a bug, an unused import, a hardcoded key) so a PR from it gives CodeRabbit something to review.

Run the tests with `python3 -m unittest discover -s tests`.
