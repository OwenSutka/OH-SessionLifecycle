"""MCP stdio entry point for session-lifecycle.

The scaffold exposes ``session_list`` only: it proves the handshake and the
launcher wiring. Records, artifact capture and the sync server arrive in Wave 3
and 4.
"""

from __future__ import annotations

from typing import Any

from mcp.server.mcpserver import MCPServer

server = MCPServer(
    "session-lifecycle",
    instructions=(
        "Durable session records. Use session_list to see past sessions and "
        "session_resume to get the pointer back into one."
    ),
)


@server.tool()
def session_list() -> dict[str, Any]:
    """List recorded sessions, most recent first."""
    return {"sessions": []}


def main() -> None:
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
