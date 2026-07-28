from fastapi import APIRouter

from backend.schemas.project_schema import *
from backend.services.project_service import *

router = APIRouter()

#  1. create
@router.post("/projects")
def study_create(projects: ProjectCreate) ->ProjectGet:
    return study_create(projects)

#  2. 한개 조회
@router.get("/projects/{projects_id}")
def get(projects_id: int) -> ProjectGet:
    return projects_get(projects_id)

#  3. 전체 조회
@router.get("/projects/getall")
def get_all() -> list[ProjectGet]:
    return projects_get_all()

#  4. 한개 삭제
@router.delete("/projects/delete/{projects_id}")
def delete(projects_id: int) -> dict:
    return projects_delete(projects_id)

#  5. 수정
@router.put("/projects/update")
def put(projects: ProjectUpdate) -> ProjectGet:
    return projects_update(projects)
