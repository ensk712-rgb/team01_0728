from datetime import datetime

from fastapi import HTTPException

from schemas.task_schema import TaskCreate, TaskDetail, TaskUpdate


# 가짜 업무 데이터: 서버를 재시작하면 처음 상태로 돌아갑니다.
task_list: list[TaskDetail] = [
    TaskDetail(
        id=1,
        project_id=1,
        title="프로젝트 테이블 설계",
        description="프로젝트 CRUD를 위한 테이블과 컬럼을 설계합니다.",
        assignee="김민수",
        status="DONE",
        priority="HIGH",
        due_date="2026-07-21",
        created_at="2026-07-10T09:00:00",
        updated_at="2026-07-20T15:30:00",
    ),
    TaskDetail(
        id=2,
        project_id=1,
        title="업무 CRUD API 구현",
        description="업무 생성, 조회, 수정, 삭제 API를 구현합니다.",
        assignee="박현우",
        status="IN_PROGRESS",
        priority="HIGH",
        due_date="2026-08-02",
        created_at="2026-07-15T10:00:00",
        updated_at="2026-07-27T13:20:00",
    ),
    TaskDetail(
        id=3,
        project_id=1,
        title="칸반 보드 화면 구현",
        description="TODO, 진행 중, 완료 상태별 업무를 표시합니다.",
        assignee="이지수",
        status="IN_PROGRESS",
        priority="MEDIUM",
        due_date="2026-08-05",
        created_at="2026-07-17T11:30:00",
        updated_at="2026-07-28T09:10:00",
    ),
    TaskDetail(
        id=4,
        project_id=1,
        title="상태별 업무 차트 구현",
        description="업무 상태 비율을 도넛 차트로 표시합니다.",
        assignee="최서연",
        status="TODO",
        priority="MEDIUM",
        due_date="2026-08-08",
        created_at="2026-07-25T14:00:00",
        updated_at="2026-07-25T14:00:00",
    ),
    TaskDetail(
        id=5,
        project_id=2,
        title="상품 목록 API 구현",
        description="상품 목록과 카테고리 필터 API를 구현합니다.",
        assignee="김민수",
        status="DONE",
        priority="HIGH",
        due_date="2026-07-20",
        created_at="2026-07-08T09:30:00",
        updated_at="2026-07-19T16:00:00",
    ),
    TaskDetail(
        id=6,
        project_id=2,
        title="장바구니 기능 구현",
        description="상품 추가, 수량 변경, 삭제 기능을 구현합니다.",
        assignee="박현우",
        status="IN_PROGRESS",
        priority="HIGH",
        due_date="2026-08-01",
        created_at="2026-07-18T10:20:00",
        updated_at="2026-07-27T17:30:00",
    ),
    TaskDetail(
        id=7,
        project_id=2,
        title="상품 검색 화면 구현",
        description="상품 이름으로 검색하는 화면을 구현합니다.",
        assignee="이지수",
        status="TODO",
        priority="LOW",
        due_date="2026-08-10",
        created_at="2026-07-26T13:00:00",
        updated_at="2026-07-26T13:00:00",
    ),
    TaskDetail(
        id=8,
        project_id=3,
        title="행사 등록 API 구현",
        description="관리자가 행사를 등록하는 API를 구현합니다.",
        assignee="김민수",
        status="DONE",
        priority="HIGH",
        due_date="2026-07-22",
        created_at="2026-07-11T09:00:00",
        updated_at="2026-07-21T18:00:00",
    ),
    TaskDetail(
        id=9,
        project_id=3,
        title="참가 신청 폼 구현",
        description="사용자가 행사 참가를 신청하는 폼을 구현합니다.",
        assignee="이지수",
        status="IN_PROGRESS",
        priority="HIGH",
        due_date="2026-08-03",
        created_at="2026-07-20T11:10:00",
        updated_at="2026-07-28T10:00:00",
    ),
    TaskDetail(
        id=10,
        project_id=3,
        title="참가자 목록 조회 API",
        description="행사별 참가자 정보를 조회하는 API를 구현합니다.",
        assignee="박현우",
        status="TODO",
        priority="MEDIUM",
        due_date="2026-08-06",
        created_at="2026-07-24T14:30:00",
        updated_at="2026-07-24T14:30:00",
    ),
]

next_task_id = len(task_list) + 1


def create_task(project_id: int, request: TaskCreate) -> TaskDetail:
    global next_task_id

    task = TaskDetail(
        id=next_task_id,
        project_id=project_id,
        title=request.title,
        description=request.description,
        assignee=request.assignee,
        status="TODO",
        priority=request.priority,
        due_date=request.due_date,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    task_list.append(task)
    next_task_id += 1

    return task


def get_all_tasks() -> list[TaskDetail]:
    return task_list


def get_tasks_by_project_id(
    project_id: int,
    status: str | None = None,
    priority: str | None = None,
    assignee: str | None = None,
) -> list[TaskDetail]:
    result = [
        task
        for task in task_list
        if task.project_id == project_id
    ]

    if status:
        result = [
            task
            for task in result
            if task.status == status
        ]

    if priority:
        result = [
            task
            for task in result
            if task.priority == priority
        ]

    if assignee:
        result = [
            task
            for task in result
            if task.assignee == assignee
        ]

    return result


def get_task(task_id: int) -> TaskDetail:
    for task in task_list:
        if task.id == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="업무를 찾을 수 없습니다.",
    )


def update_task(task_id: int, request: TaskUpdate) -> TaskDetail:
    task = get_task(task_id)

    update_data = request.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=422,
            detail="수정할 데이터를 입력해주세요.",
        )

    updated_task = task.model_copy(
        update={
            **update_data,
            "updated_at": datetime.now(),
        }
    )

    task_index = task_list.index(task)
    task_list[task_index] = updated_task

    return updated_task


def delete_task(task_id: int) -> dict:
    task = get_task(task_id)
    task_list.remove(task)

    return {
        "message": f"{task_id}번 업무가 삭제되었습니다."
    }