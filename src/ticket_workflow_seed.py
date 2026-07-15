DEFAULT_OWNER = "engineering-ops"


def normalize_delivery_owner(owner: str | None) -> str:
    """Return the routing key used by delivery workflows."""
    normalized = " ".join((owner or "").strip().lower().split())
    return normalized or DEFAULT_OWNER


def delivery_summary(record: dict) -> dict:
    """Return the stable summary fields currently exposed to callers."""
    return {
        "owner": normalize_delivery_owner(record.get("owner")),
        "status": record["status"],
    }


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
