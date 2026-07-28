from pathlib import Path
import sys

import streamlit as st

FRONTEND_DIR = Path(__file__).resolve().parents[1]
if str(FRONTEND_DIR) not in sys.path:
    sys.path.insert(0, str(FRONTEND_DIR))

from auth import is_logged_in, login, logout


st.set_page_config(page_title="TaskFlow | 로그인", page_icon="✅", layout="centered")

if is_logged_in():
    st.success(f"{st.session_state.user_id}님, 로그인되었습니다.")
    if st.button("프로젝트 보기"):
        st.switch_page("app_pages/01_projects.py")
    if st.button("로그아웃"):
        logout()
        st.rerun()
else:
    st.title("TaskFlow")
    with st.form("login_form"):
        user_id = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")
        submitted = st.form_submit_button("로그인")

    if submitted:
        success, message = login(user_id, password)
        if success:
            st.switch_page("app_pages/01_projects.py")
        else:
            st.error(message)