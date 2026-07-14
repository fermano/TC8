DEFAULT_OWNER = "engineering-ops"
DEFAULT_SOURCE = "unspecified"


def normalize_delivery_owner(owner: str | None) -> str:
    """Return the routing key used by delivery workflows."""
    normalized = (owner or "").strip().lower()
    return normalized or DEFAULT_OWNER


def normalize_source(source: str | None) -> str:
    """Return a normalized delivery source, defaulting blank values."""
    normalized = (source or "").strip().lower()
    return normalized or DEFAULT_SOURCE


def delivery_summary(record: dict, include_source: bool = False) -> dict:
    """Return the stable summary fields currently exposed to callers."""
    summary = {
        "owner": normalize_delivery_owner(record.get("owner")),
        "status": record["status"],
    }
    if include_source:
        summary["source"] = normalize_source(record.get("source"))
    return summary
