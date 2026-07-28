from schemas.project_schema import ProjectCreate, ProjectGet, ProjectUpdate


# 1. 입력
def projects_create(projects: ProjectCreate) -> ProjectGet:
    """앙"""
    print("Database에 입력이 처리됩니다.")
    print(f"{projects.title} {projects.content}")

    return ProjectGet(
        id="",
        title=projects.title,
        content=projects.content,
        created_at="",
    )


# 2. 전체 조회
def projects_get_all() -> list[ProjectGet]:
    result = [
    {
        "id": "1",
        "title": "무선 블루투스 이어폰",
        "content": "노이즈 캔슬링과 최대 24시간 재생을 지원하는 무선 이어폰입니다.",
        "created_at": "2026-07-21 09:00:00"
    },
    {
        "id": "2",
        "title": "기계식 키보드",
        "content": "적축 스위치와 RGB 백라이트를 적용한 텐키리스 키보드입니다.",
        "created_at": "2026-07-22 10:30:00"
    },
    {
        "id": "3",
        "title": "27인치 QHD 모니터",
        "content": "QHD 해상도와 165Hz 주사율을 지원하는 게이밍 모니터입니다.",
        "created_at": "2026-07-23 14:20:00"
    },
    {
        "id": "4",
        "title": "USB-C 멀티 허브",
        "content": "HDMI, USB 3.0, SD 카드 및 PD 충전을 지원하는 멀티 허브입니다.",
        "created_at": "2026-07-24 11:10:00"
        },
        {
        "id": "5",
        "title": "휴대용 보조배터리",
        "content": "20,000mAh 용량과 25W 고속 충전을 지원하는 보조배터리입니다.",
        "created_at": "2026-07-25 16:40:00"
        }
]

    return result


# 3. 한 개 조회
def projects_get(projects_id: int) -> ProjectGet:
    print("한 개 조회 실행")

    return ProjectGet(
        id=str(projects_id),
        title="FastAPI",
        content="projects를 생성했습니다",
        created_at="2026-07-21 15:00:00",
    )


# 4. 수정
def projects_update(projects: ProjectUpdate) -> ProjectGet:
    print("Database에 수정이 처리됩니다.")
    print(f"{projects.title} {projects.content}")

    return ProjectGet(
        id=projects.id,
        title=projects.title,
        content=projects.content,
        created_at="",
    )


# 5. 삭제
def projects_delete(projects_id: int) -> dict:
    print(f"{projects_id}번 포로젝트가 삭제됩니다.")

    return {
        "message": f"{projects_id}번 프로젝트가 삭제되었습니다."
    }