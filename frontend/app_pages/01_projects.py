from pathlib import Path
import sys

import streamlit as st

FRONTEND_DIR = Path(__file__).resolve().parents[1]
if str(FRONTEND_DIR) not in sys.path:
    sys.path.insert(0, str(FRONTEND_DIR))

from api_client import get_data
from auth import is_logged_in, logout


st.set_page_config(page_title="TaskFlow | 프로젝트", page_icon="✅", layout="wide")


def render_sidebar() -> None:
    with st.sidebar:
        st.header("TaskFlow")
        if st.button("로그아웃", use_container_width=True):
            logout()
            st.switch_page("app_pages/00_login.py")


def select_project(project_id: int) -> None:
    st.session_state.selected_project_id = project_id


if not is_logged_in():
    st.switch_page("app_pages/00_login.py")
    st.stop()

render_sidebar()
st.title("프로젝트")

try:
    projects = get_data("/projects/getall")
except Exception as exc:
    st.error(f"프로젝트를 불러올 수 없습니다: {exc}")
    st.stop()

if not projects:
    st.info("등록된 프로젝트가 없습니다.")
    st.stop()

selected_id = st.session_state.get("selected_project_id")
if selected_id is None:
    selected_id = projects[0].get("id")
    st.session_state.selected_project_id = selected_id

list_column, detail_column = st.columns([1, 2], gap="large")

with list_column:
    st.subheader(f"목록 ({len(projects)})")
    for project in projects:
        project_id = project.get("id")
        title = project.get("title", "제목 없음")
        is_selected = project_id == selected_id
        if st.button(title, key=project_id, type="primary" if is_selected else "secondary", use_container_width=True):
            select_project(project_id)
            st.rerun()

with detail_column:
    st.subheader("프로젝트 상세")
    try:
        project = get_data(f"/projects/{st.session_state.selected_project_id}")
    except Exception as exc:
        st.error(f"상세 정보를 불러올 수 없습니다: {exc}")
        st.stop()

    st.header(project.get("title", "제목 없음"))
    st.write(project.get("content") or "설명이 등록되지 않았습니다.")
    st.caption(f"생성 일시: {project.get('created_at', '-')}")