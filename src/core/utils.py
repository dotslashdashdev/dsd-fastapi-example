from datetime import datetime, timezone


def utc_now():
    return datetime.utcnow().replace(tzinfo=timezone.utc)
