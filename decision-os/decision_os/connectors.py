"""Layer 2 — Connective tissue (the agnostic, plug-and-play layer).

This is where "seamlessly plug into the existing stack" literally lives. Every
data source is reduced to one tiny contract: a connector that yields rows as
plain dictionaries. Adding a new integration (Salesforce, SAP, a data
warehouse, SharePoint...) means implementing a single ``fetch`` method and
registering it — nothing else in the platform changes. That is what keeps the
platform *agnostic*.

v1 ships two connectors that cover a huge amount of real-world ground:
  * ``csv``    - any exported file / spreadsheet dump.
  * ``sqlite`` - any query against an existing SQLite database.
"""
from __future__ import annotations

import abc
import csv
import io
import sqlite3
from typing import Any, Iterable


class Connector(abc.ABC):
    """The one interface every integration implements."""

    #: short, stable identifier used in the API and registry.
    name: str = ""

    @abc.abstractmethod
    def fetch(self, config: dict[str, Any]) -> Iterable[dict[str, Any]]:
        """Yield source rows as dictionaries. Keep it lazy where possible."""
        raise NotImplementedError

    def describe(self) -> dict[str, Any]:
        """Human-readable metadata for the UI."""
        return {"name": self.name, "doc": (self.__doc__ or "").strip()}


class CSVConnector(Connector):
    """Reads CSV. Pass either ``content`` (raw CSV text) or ``path`` (a file)."""

    name = "csv"

    def fetch(self, config: dict[str, Any]) -> Iterable[dict[str, Any]]:
        if "content" in config and config["content"] is not None:
            handle: Iterable[str] = io.StringIO(config["content"])
        elif "path" in config:
            handle = open(config["path"], newline="", encoding="utf-8")
        else:
            raise ValueError("csv connector needs 'content' or 'path'")
        reader = csv.DictReader(handle)
        for row in reader:
            # Strip None keys that DictReader can produce on ragged rows.
            yield {k: v for k, v in row.items() if k is not None}


class SQLiteConnector(Connector):
    """Runs a read-only query against an existing SQLite database file.

    config: {"path": "<db file>", "query": "SELECT ..."}
    """

    name = "sqlite"

    def fetch(self, config: dict[str, Any]) -> Iterable[dict[str, Any]]:
        path = config["path"]
        query = config["query"]
        src = sqlite3.connect(path)
        src.row_factory = sqlite3.Row
        try:
            for row in src.execute(query):
                yield dict(row)
        finally:
            src.close()


# --- Registry --------------------------------------------------------------
_REGISTRY: dict[str, Connector] = {
    CSVConnector.name: CSVConnector(),
    SQLiteConnector.name: SQLiteConnector(),
}


def get_connector(name: str) -> Connector:
    try:
        return _REGISTRY[name]
    except KeyError:
        raise ValueError(
            f"unknown connector {name!r}; available: {sorted(_REGISTRY)}"
        ) from None


def available_connectors() -> list[dict[str, Any]]:
    return [c.describe() for c in _REGISTRY.values()]


def register_connector(connector: Connector) -> None:
    """Extension point: third parties / your team add connectors here."""
    _REGISTRY[connector.name] = connector
