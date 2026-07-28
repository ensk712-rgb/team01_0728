from typing import Literal
from fastapi import APIRouter, Query, Response, status
from schemas.task_schema import (
    TaskCreate,
    TaskDetail,
    TaskUpdate,
)
from services.task_service import (
    create_task,
    delete_task,
    get_all_tasks,
    get_tasks_by_project_id,
    update_task,
)
task_router = APIRouter(
    prefix="/api/v1",
    tags=["Tasks"],
)

# POST 업무 생성
@task_router.post(
    "/projects/{project_id}/tasks",
    response_model=TaskDetail,
    status_code=status.HTTP_201_CREATED,
)
def create_project_task(
    project_id: int,
    request: TaskCreate,
) -> TaskDetail:
    return create_task(project_id,request)

# GET 프로젝트의 업무 목록 조회 
@task_router.get(
    "/projects/{project_id}/tasks",
    response_model=list[TaskDetail],
)
def get_project_tasks(
    project_id: int,
    task_status: Literal["TODO", "IN_PROGRESS","DONE"] | None = Query(
        default=None,
        alias= "status",
    ),
    priority: Literal["LOW", "MEDIUM", "HIGH"] | None = Query(
        default= None,
    ),
    assignee: str | None = Query(default=None),
) -> list[TaskDetail]:
    print("---------------------------")
    return get_tasks_by_project_id(
        project_id=project_id,
        status = task_status,
        priority=priority,
        assignee= assignee
    )

@task_router.get(
    "/tasks",
    response_model=list[TaskDetail],
)
def get_all_task_list() -> list[TaskDetail]:
    return get_all_tasks()

# PATCH 업무 정보 또는 상태 수정
@task_router.patch(
    "/tasks/{task_id}",
    response_model=TaskDetail,
)
def update_project_task(
    task_id: int,
    request: TaskUpdate,
) -> TaskDetail:
    return update_task(task_id, request)

# DELETE 업무 삭제
@task_router.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project_task(task_id: int) -> Response:
    delete_task(task_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)