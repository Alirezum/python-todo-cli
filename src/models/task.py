from dataclasses import dataclass, field
import uuid
from datetime import datetime
from enum import auto, StrEnum


class Status(StrEnum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    BLOCKED = auto()


class Priority(StrEnum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Untitled"
    description: str | None = None
    status: Status = Status.TODO
    priority: Priority = Priority.LOW
    created_at: datetime = field(default_factory=datetime.now)
    due_date: datetime | None = None
    category_id: str | None = None

    def mark_done(self):
        self.status = Status.DONE

    def update(
        self,
        title: str | None = None,
        description: str | None = None,
        status: Status | None = None,
        priority: Priority | None = None,
        due_date: datetime | None = None,
        category_id: str | None = None,
    ):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if priority is not None:
            self.priority = priority
        if due_date is not None:
            self.due_date = due_date
        if category_id is not None:
            self.category_id = category_id

    def is_overdue(self) -> bool:
        return self.due_date is not None and datetime.now() > self.due_date
