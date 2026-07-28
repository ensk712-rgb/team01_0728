# 03_dashboard.py

import streamlit as st
import pandas as pd
import httpx
from datetime import date

API_URL = "http://127.0.0.1:8000"
PROJECT_ID = 1

st.title("📊 업무 대시보드")
st.caption("프로젝트 업무 진행 현황을 확인하세요.")

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

if df.empty:
    st.info("등록된 업무가 없습니다.")
    st.stop()

# 상태별 업무 개수
total_count = len(df)
todo_count = len(df[df["status"] == "TODO"])
progress_count = len(df[df["status"] == "IN_PROGRESS"])
done_count = len(df[df["status"] == "DONE"])

# -------------------------
# 업무 현황 카드
# -------------------------
st.subheader("업무 현황")

col1, col2, col3, col4 = st.columns(4)

col1.metric("📋 전체 업무", total_count)
col2.metric("🔵 할 일", todo_count)
col3.metric("🟡 진행 중", progress_count)
col4.metric("🟢 완료", done_count)

# -------------------------
# 완료율
# -------------------------
st.subheader("프로젝트 완료율")

completion_rate = round(done_count / total_count * 100, 1)

st.progress(completion_rate / 100)
st.write(f"현재 프로젝트는 **{completion_rate}%** 완료되었습니다.")

# -------------------------
# 차트
# -------------------------
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("상태별 업무 수")

    status_count = df["status"].value_counts().reindex(
        ["TODO", "IN_PROGRESS", "DONE"],
        fill_value=0,
    )

    st.bar_chart(status_count)

with right_col:
    st.subheader("우선순위별 업무 수")

    priority_count = df["priority"].value_counts().reindex(
        ["LOW", "MEDIUM", "HIGH"],
        fill_value=0,
    )

    st.bar_chart(priority_count)

# -------------------------
# 마감일 지난 업무
# -------------------------
st.divider()
st.subheader("⚠️ 마감일 지난 업무")

df["due_date"] = pd.to_datetime(
    df["due_date"],
    errors="coerce",
)

overdue_df = df[
    (df["due_date"].dt.date < date.today())
    & (df["status"] != "DONE")
]

if overdue_df.empty:
    st.success("마감일이 지난 업무가 없습니다.")

else:
    st.dataframe(
        overdue_df[
            ["title", "assignee", "status", "priority", "due_date"]
        ].rename(
            columns={
                "title": "업무명",
                "assignee": "담당자",
                "status": "상태",
                "priority": "우선순위",
                "due_date": "마감일",
            }
        ),
        hide_index=True,
        use_container_width=True,
    )

# -------------------------
# 담당자별 업무 현황
# -------------------------
st.divider()
st.subheader("👥 담당자별 업무 수")

assignee_count = df["assignee"].fillna("미지정").value_counts()

st.bar_chart(assignee_count)