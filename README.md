msg-rules-enforcement-hook
=========================

A prepare-commit-msg hook for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/snowindy/msg-rules-enforcement-hook
    rev: v1.5.0  # Use the ref you want to point at
    hooks:
    -   id: msg-rules-enforcement
```

and install prepare-commit-msg hooks using
```
pre-commit install --hook-type prepare-commit-msg
```


### Credits

This hook is a dirty copy of the existing hook: https://github.com/avilaton/add-msg-issue-prefix-hook
