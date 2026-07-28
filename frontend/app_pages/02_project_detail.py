# 02_project_detail.py

import streamlit as st
import pandas as pd
import httpx
from datetime import date

API_URL = "http://127.0.0.1:8000"
PROJECT_ID = 1

st.title("📋 프로젝트 업무")

# 백엔드에서 업무 목록 가져오기
response = httpx.get(
    f"{API_URL}/api/v1/projects/{PROJECT_ID}/tasks"
)

if response.status_code == 200:
    tasks = response.json()
    df = pd.DataFrame(tasks)

else:
    st.error("백엔드에서 업무 목록을 가져오지 못했습니다.")
    st.stop()

# 상태 필터
status = st.selectbox(
    "상태 필터",
    ["전체", "TODO", "IN_PROGRESS", "DONE"]
)

if status != "전체":
    df = df[df["status"] == status]

# -------------------------
# 업무 보드
# -------------------------
st.subheader("🗂️ 업무 보드")

# 업무 상태별 개수
col1, col2, col3 = st.columns(3)

col1.metric("할 일", len(df[df["status"] == "TODO"]))
col2.metric("진행 중", len(df[df["status"] == "IN_PROGRESS"]))
col3.metric("완료", len(df[df["status"] == "DONE"]))

st.divider()

todo_col, progress_col, done_col = st.columns(3)

# 할 일 카드
with todo_col:
    st.markdown("### 🔵 할 일")

    todo_tasks = df[df["status"] == "TODO"]

    if todo_tasks.empty:
        st.caption("업무가 없습니다.")

    for _, task in todo_tasks.iterrows():
        with st.container(border=True):
            st.write(f"**{task['title']}**")
            st.caption(f"👤 담당자: {task['assignee']}")
            st.caption(f"⚡ 우선순위: {task['priority']}")
            st.caption(f"📅 마감일: {task['due_date']}")

# 진행 중 카드
with progress_col:
    st.markdown("### 🟡 진행 중")

    progress_tasks = df[df["status"] == "IN_PROGRESS"]

    if progress_tasks.empty:
        st.caption("업무가 없습니다.")

    for _, task in progress_tasks.iterrows():
        with st.container(border=True):
            st.write(f"**{task['title']}**")
            st.caption(f"👤 담당자: {task['assignee']}")
            st.caption(f"⚡ 우선순위: {task['priority']}")
            st.caption(f"📅 마감일: {task['due_date']}")

# 완료 카드
with done_col:
    st.markdown("### 🟢 완료")

    done_tasks = df[df["status"] == "DONE"]

    if done_tasks.empty:
        st.caption("업무가 없습니다.")

    for _, task in done_tasks.iterrows():
        with st.container(border=True):
            st.write(f"**{task['title']}**")
            st.caption(f"👤 담당자: {task['assignee']}")
            st.caption(f"⚡ 우선순위: {task['priority']}")
            st.caption(f"📅 마감일: {task['due_date']}")

# -------------------------
# 업무 목록
# -------------------------
st.divider()
st.subheader("📝 업무 목록")

st.dataframe(
    df[
        ["id", "title", "assignee", "status", "priority", "due_date"]
    ],
    hide_index=True,
    use_container_width=True,
)

# -------------------------
# 업무 등록
# -------------------------
st.divider()
st.subheader("➕ 업무 등록")

with st.form("task_form", clear_on_submit=True):
    title = st.text_input("업무명")
    assignee = st.text_input("담당자")

    priority = st.selectbox(
        "우선순위",
        ["LOW", "MEDIUM", "HIGH"]
    )

    due_date = st.date_input(
        "마감일",
        value=date.today()
    )

    submit = st.form_submit_button("등록")

    if submit:
        if title == "":
            st.warning("업무명을 입력해 주세요.")

        else:
            data = {
                "title": title,
                "assignee": assignee,
                "priority": priority,
                "due_date": str(due_date),
            }

            create_response = httpx.post(
                f"{API_URL}/api/v1/projects/{PROJECT_ID}/tasks",
                json=data,
            )

            if create_response.status_code == 201:
                st.success("업무가 등록되었습니다.")
                st.rerun()

            else:
                st.error("업무 등록에 실패했습니다.")