# session-lifecycle

Every OpenHands session gets a durable record: what it was, what it touched, what
it produced, and how to get back to it. Documents and images the agent creates are
copied into a stable `deliverables/<session-id>/` folder inside the project,
indexed, and made reachable from a phone over the tailnet — for a bounded window,
on demand, read-only.

Repo `OH-SessionLifecycle` maps to plugin name **`session-lifecycle`**.

This plugin does **not** build a chat client. Agent Canvas already provides
mobile chat, so the sync surface here is read-only artifacts over a TTL'd,
tool-started HTTP server, with each session deep-linked into Canvas.

## Status

**Not installable yet.** Scaffolded in Wave 0 (SL-01): manifest, launcher and MCP
handshake work, and `session_list` answers with an empty set. Records, artifact
capture, the manifest/index and the sync server land in Waves 3–4.

## Layout

```
plugin.json                       manifest (Agent Plugins 1.0.0)
mcp.json                          stdio server declaration
bin/session-lifecycle-mcp         launcher, exec'd by mcp.json
src/session_lifecycle/
  hook_runtime.py                 vendored hook contract, hash-locked
  config.py                       paths, budgets, limits
  server.py                       MCP stdio dispatch
tests/unit/                       manifest + hash-lock tests
```

## Development

```bash
uv sync
uv run pytest -q
uv run ruff check . && uv run ruff format --check . && uv run mypy src
```

`src/session_lifecycle/hook_runtime.py` is a verbatim copy of the control-plane
canonical runtime. Do not edit it here: edit the canonical copy, re-copy, and
update `CANONICAL_SHA256` in `tests/unit/test_hook_runtime_hash.py`.

## Licence

MIT.
