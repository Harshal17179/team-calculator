- `git fetch` downloads commits, files and refs from a remote repository but does not modify your working copy or current branch. It updates remote-tracking branches (e.g., origin/master).
- `git merge origin/master` merges fetched commits into your local branch when you are ready.
- `git pull` is equivalent to `git fetch` followed by `git merge` (default behavior). It fetches and then merges the remote changes into the current branch in one step.

Use `fetch` when you want to inspect remote changes before merging. Use `pull` when you want to update immediately.
