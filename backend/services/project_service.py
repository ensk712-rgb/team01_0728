from backend.schemas.project_schema import ProjectCreate, ProjectGet, ProjectUpdate


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
        ProjectGet(
            id="1",
            title="FastAPI",
            content="projects를 생성했습니다",
            created_at="2026-07-21 15:00:00",
        )
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
    print(f"{projects_id}번 학습 기록이 삭제됩니다.")

    return {
        "message": f"{projects_id}번 학습 기록이 삭제되었습니다."
    }