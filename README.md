# TaskFlow - 팀 업무 관리 서비스

TaskFlow는 프로젝트와 업무를 체계적으로 관리하는 팀 협업 서비스입니다.
FastAPI 백엔드, Streamlit 프론트엔드, Supabase 데이터베이스를 사용하여
프로젝트와 업무의 전체 CRUD 흐름을 구현하는 것을 목표로 합니다.

## 프로젝트 목표

- 프로젝트와 업무의 생성, 조회, 수정, 삭제 기능을 구현합니다.
- 업무 상태를 `TODO`, `IN_PROGRESS`, `DONE`으로 관리합니다.
- 업무별 담당자, 마감일, 우선순위를 설정합니다.
- 프론트엔드와 백엔드 API 연동, 관계형 데이터베이스 설계를 연습합니다.

## 핵심 기능

| 구분 | CRUD 기능 |
| --- | --- |
| 프로젝트 | 프로젝트 생성, 목록/상세 조회, 이름 및 설명 수정, 삭제 |
| 업무 | 프로젝트별 업무 등록, 목록/필터 조회, 업무 정보 및 상태 수정, 삭제 |
| 대시보드 | 상태별 업무 수와 마감일이 지난 업무를 조회 |

### 업무(Task) 데이터

| 필드 | 설명 |
| --- | --- |
| `id` | 업무 고유 ID |
| `project_id` | 소속 프로젝트 ID |
| `title` | 업무 제목 |
| `description` | 업무 상세 설명(선택) |
| `status` | `TODO`, `IN_PROGRESS`, `DONE` |
| `priority` | `LOW`, `MEDIUM`, `HIGH` |
| `assignee` | 담당자 |
| `due_date` | 마감일 |
| `created_at` | 생성 일시 |

## 사용자 흐름

```text
프로젝트 목록 -> 프로젝트 생성 또는 선택 -> 업무 목록 조회
                                            -> 업무 등록
                                            -> 업무 수정 또는 상태 변경
                                            -> 업무 삭제
```

## API 초안

| Method | Endpoint | 설명 |
| --- | --- | --- |
| `GET` | `/projects` | 프로젝트 목록 조회 |
| `POST` | `/projects` | 프로젝트 생성 |
| `GET` | `/projects/{project_id}` | 프로젝트 상세 조회 |
| `PATCH` | `/projects/{project_id}` | 프로젝트 수정 |
| `DELETE` | `/projects/{project_id}` | 프로젝트 삭제 |
| `GET` | `/projects/{project_id}/tasks` | 프로젝트의 업무 목록 조회 |
| `POST` | `/projects/{project_id}/tasks` | 업무 생성 |
| `PATCH` | `/tasks/{task_id}` | 업무 정보 또는 상태 수정 |
| `DELETE` | `/tasks/{task_id}` | 업무 삭제 |

## 역할 분담 (4명)

| 담당 | 주요 업무 |
| --- | --- |
| 백엔드 1 | 프로젝트 API, Supabase 프로젝트 테이블, 요청/응답 스키마 |
| 백엔드 2 | 업무 API, 상태 변경 및 필터, 업무 테이블, API 테스트 |
| 프론트엔드 1 | 로그인/내비게이션, 프로젝트 목록 및 상세 페이지 |
| 프론트엔드 2 | 업무 보드/목록, 등록/수정 폼, 필터 및 대시보드 |

### 협업 규칙

- 프론트엔드 구현 전에 API 요청과 응답 형식을 먼저 합의합니다.
- API 경로와 공통 데이터 형식이 바뀌면 이 README도 함께 갱신합니다.
- 기능 단위로 브랜치를 만들고 Pull Request로 병합합니다.
- 프론트엔드는 Supabase에 직접 접근하지 않고 백엔드 API만 호출합니다.

## 권장 폴더 구조

```text
backend/
  main.py
  routers/
    project_router.py
    task_router.py
  services/
    project_service.py
    task_service.py
  schemas/
    project_schema.py
    task_schema.py
  core/
    supabase_client.py
frontend/
  app_pages/
    00_login.py
    01_projects.py
    02_project_detail.py
    03_dashboard.py
```

## 로컬 실행 방법

1. 가상환경을 만들고 의존성을 설치합니다.

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. 백엔드 폴더에 `.env` 파일을 생성합니다. 이 파일은 Git에 올리지 않습니다.

   ```env
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```

3. 서로 다른 터미널에서 백엔드와 프론트엔드를 실행합니다.

   ```powershell
   cd backend
   uvicorn ./backend/main:app --reload
   ```

   ```powershell
   streamlit run frontend/app_pages/00_login.py
   ```

## 완료 기준

- 프로젝트와 업무에 대한 CRUD 기능이 모두 동작합니다.
- 업무 상태를 세 단계 사이에서 변경할 수 있습니다.
- 프론트엔드는 API 호출의 로딩, 빈 목록, 오류 상태를 표시합니다.
- 제목 누락 및 잘못된 상태/우선순위 값은 API에서 검증합니다.
- 각 백엔드 엔드포인트에 성공 사례 테스트가 최소 1개 있습니다.
