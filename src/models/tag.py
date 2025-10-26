import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Tag:
    """Model for tagging tasks (e.g., #work, #urgent, #personal)."""

    name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    description: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
