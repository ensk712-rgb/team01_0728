from datetime import datetime, timedelta

from fastapi import HTTPException

from schemas.task_schema import TaskCreate, TaskDetail, TaskUpdate


# 서버가 실행되는 동안만 유지되는 가짜 데이터
tasks: list[TaskDetail] = [
    TaskDetail(
        id=1,
        project_id=1,
        title="프로젝트 테이블 설계",
        description="projects 테이블과 컬럼을 설계합니다.",
        assignee="김민수",
        status="DONE",
        priority="HIGH",
        due_date=datetime.now().date() - timedelta(days=2),
        created_at=datetime.now() - timedelta(days=10),
        updated_at=datetime.now() - timedelta(days=3),
    ),
    TaskDetail(
        id=2,
        project_id=1,
        title="업무 CRUD API 구현",
        description="업무 등록, 조회, 수정, 삭제 API를 구현합니다.",
        assignee="이지수",
        status="IN_PROGRESS",
        priority="HIGH",
        due_date=datetime.now().date() + timedelta(days=3),
        created_at=datetime.now() - timedelta(days=7),
        updated_at=datetime.now() - timedelta(days=1),
    ),
    TaskDetail(
        id=3,
        project_id=1,
        title="칸반 보드 화면 구현",
        description="TODO, 진행 중, 완료 상태별 업무를 표시합니다.",
        assignee="박현우",
        status="TODO",
        priority="MEDIUM",
        due_date=datetime.now().date() + timedelta(days=7),
        created_at=datetime.now() - timedelta(days=5),
        updated_at=datetime.now() - timedelta(days=5),
    ),
    TaskDetail(
        id=4,
        project_id=2,
        title="상품 목록 페이지 제작",
        description="쇼핑몰 상품 목록 화면을 제작합니다.",
        assignee="최서연",
        status="DONE",
        priority="MEDIUM",
        due_date=datetime.now().date() - timedelta(days=1),
        created_at=datetime.now() - timedelta(days=12),
        updated_at=datetime.now() - timedelta(days=2),
    ),
    TaskDetail(
        id=5,
        project_id=2,
        title="장바구니 기능 구현",
        description="상품을 장바구니에 담는 기능을 구현합니다.",
        assignee="김민수",
        status="IN_PROGRESS",
        priority="HIGH",
        due_date=datetime.now().date() + timedelta(days=2),
        created_at=datetime.now() - timedelta(days=4),
        updated_at=datetime.now(),
    ),
    TaskDetail(
        id=6,
        project_id=3,
        title="행사 참가 신청 폼 제작",
        description="참가자 정보를 입력받는 폼을 구현합니다.",
        assignee="이지수",
        status="TODO",
        priority="LOW",
        due_date=datetime.now().date() + timedelta(days=10),
        created_at=datetime.now() - timedelta(days=2),
        updated_at=datetime.now() - timedelta(days=2),
    ),
]

next_task_id = 7


