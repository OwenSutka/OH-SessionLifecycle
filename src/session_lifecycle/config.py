"""Paths, budgets and limits for session lifecycle.

Every path derives from ``SESSION_LIFECYCLE_DATA`` (the plugin's ``PLUGIN_DATA``),
except the user-visible deliverables tree, which deliberately lives inside the
project so a human can find the files — and is gitignored plus guardrail-blocked.
"""

from __future__ import annotations

import os
from datetime import timedelta
from pathlib import Path

DATA_ENV = "SESSION_LIFECYCLE_DATA"

SESSIONS_DIR_NAME = "sessions"
LOGS_DIR_NAME = "logs"
META_FILENAME = "meta.json"

#: Where produced documents land, relative to the session's working directory.
DELIVERABLES_DIR_NAME = "deliverables"

#: A record still ``active`` past this age is swept to ``abandoned``.
ABANDONED_AFTER = timedelta(hours=24)

#: Artifact sync is read-only, loopback-only and time-boxed by default.
SYNC_DEFAULT_HOST = "127.0.0.1"
SYNC_DEFAULT_TTL = timedelta(minutes=30)
SYNC_MAX_TTL = timedelta(minutes=60)


class ConfigError(RuntimeError):
    """Raised when the plugin data directory is not configured."""


def data_dir() -> Path:
    """The plugin data root, from ``SESSION_LIFECYCLE_DATA``."""
    raw = os.environ.get(DATA_ENV, "").strip()
    if not raw:
        raise ConfigError(
            f"{DATA_ENV} is not set. It is supplied by the plugin runtime as "
            "${PLUGIN_DATA}; set it explicitly when running the server by hand."
        )
    return Path(raw)


def sessions_dir() -> Path:
    return data_dir() / SESSIONS_DIR_NAME


def session_dir(session_id: str) -> Path:
    """Per-session record directory. ``session_id`` must already be validated."""
    return sessions_dir() / session_id


def logs_dir() -> Path:
    return data_dir() / LOGS_DIR_NAME


def deliverables_dir(working_dir: str) -> Path:
    """``<working_dir>/deliverables`` — the human-facing artifact tree."""
    return Path(working_dir) / DELIVERABLES_DIR_NAME
