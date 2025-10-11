import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List

from task import Task


@dataclass
class Category:
    """Model for Category store task list """
    name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    description: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    tasks: list[Task] = field(default_factory=list)

    def rename(self, new_name: str):
        """
        Rename the category.

        Args:
            new_name (str): The new name for the category.
        """
        self.name = new_name
        self.updated_at = datetime.now(timezone.utc)

    def update_description(self, new_description: str):
        """
        Update the category's description.

        Args:
            new_description (str): The new description text.
        """
        self.description = new_description
        self.updated_at = datetime.now(timezone.utc)

    # Task Management
    def add_task_to_category(self, task: Task):
        """
        Add a task to the category.

        Args:
            task (Task): The task to add.
        """
        task.category_id = self.id  # Ensure the task knows its category
        self.tasks.append(task)
        self.updated_at = datetime.now(timezone.utc)

    def remove_task_from_category(self, task_id: str) -> bool:
        """
        Remove a task from the category by its ID.

        Args:
            task_id (str): The ID of the task to remove.

        Returns:
            bool: True if a task was removed, False if no task with the ID was found.
        """
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        removed = len(self.tasks) < initial_count
        if removed:
            self.updated_at = datetime.now(timezone.utc)
        return removed

    def list_tasks(self) -> List[Task]:
        """
        Get a copy of all tasks in the category.

        Returns:
            List[Task]: List of tasks.
        """
        return self.tasks.copy()

    def __repr__(self):
        return (
            f"Category(id={self.id}, name={self.name}, "
            f"tasks={len(self.tasks)}, created_at={self.created_at.isoformat()})"
        )
