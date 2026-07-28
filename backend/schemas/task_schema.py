from datetime import date, datetime
from typing import Literal
from pydantic import BaseModel,Field

TaskStatus = Literal["TODO", "IN_PROGRESS","DONE"]
TaskPriority = Literal["LOW","MEDIUM","HIGH"]

class TaskCreate(BaseModel):
    title: str = Field(min_length=1,max_length=1000)
    description: str | None = Field(default=None,max_length=1000)
    assignee: str | None = Field(default=None, max_length=50)
    priority: TaskPriority = "MEDIUM"
    due_date: date | None = None

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    assignee: str | None = Field(default=None, max_length=50)
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    due_date: date | None = None

class TaskDetail(BaseModel):
    id: int
    project_id: int
    title: str
    description: str | None
    assignee: str | None
    status: TaskStatus
    priority: TaskPriority
    due_date: date | None
    created_at: datetime
    updated_at: datetime