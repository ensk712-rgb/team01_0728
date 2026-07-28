import streamlit as st


def is_logged_in() -> bool:
    return st.session_state.get("logged_in", False)


def login(user_id: str, password: str) -> tuple[bool, str]:
    if user_id and password:
        st.session_state.logged_in = True
        st.session_state.user_id = user_id
        return True, ""
    return False, "아이디와 비밀번호를 입력하세요."


def logout() -> None:
    st.session_state.clear()