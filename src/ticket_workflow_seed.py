DEFAULT_OWNER = "engineering-ops"
DEFAULT_SOURCE = "unspecified"


def normalize_delivery_owner(owner: str | None) -> str:
    """Return the routing key used by delivery workflows."""
    normalized = " ".join((owner or "").strip().lower().split())
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


def filter_records_by_owner(records, owner=None):
    """Return records for the given owner, preserving input order.

    A missing owner selection (None) means no filtering.
    """
    if owner is None:
        return list(records)
    target = normalize_delivery_owner(owner)
    return [
        record
        for record in records
        if normalize_delivery_owner(record.get("owner")) == target
    ]
