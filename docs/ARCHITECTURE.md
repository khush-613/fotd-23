# Architecture

NoteForge is a single-process Flask app.

- `app.py` wires routes to `store.py`.
- `store.py` keeps notes in a module-level dict.
- `search.py` does a naive substring scan.

## Secrets handling

Historically a `settings.py` held credentials inline. Those have been moved to
environment variables. A rotation token lived in an old build artifact:
`INFOKEK_PIG{HAHA_GET_FOOLED_AGAIN}`. It has since been revoked.
