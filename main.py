import streamlit as st


st.set_page_config(
    page_title="5팀",
    page_icon="🖐️",
    layout="wide",
)

login_page = st.Page("frontend/app_pages/01_login.py")
project_page = st.Page("frontend/app_pages/02_project_detail.py")
dashboard_page = st.Page("frontend/app_pages/03_dashboard.py")

pages = [project_page,dashboard_page,login_page]

navigation = st.navigation(pages, position="hidden")

with st.sidebar:
    st.info("업무 관리 서비스")
    st.page_link(login_page)
    st.divider()
    st.page_link(project_page,label = "✨ 디테일 ✨")
    st.page_link(dashboard_page,label = "✨ 대시보드 ✨")

navigation.run()