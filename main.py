import streamlit as st

# 페이지 상태 저장
if "page" not in st.session_state:
    st.session_state["page"] = "마약이란 무엇인가"  # 기본 페이지 설정

current_page = st.session_state["page"]

st.title(current_page)

# 페이지 내용 출력
if current_page == "마약이란 무엇인가":
    st.write("마약이란, 중독성과 의존성이 강한 화학 물질로...")
    
elif current_page == "마약의 국내 현황":
    st.write("최근 한국의 마약 범죄는 증가하는 추세이며...")
    st.bar_chart({"2020": 500, "2021": 700, "2022": 1200})  # 예제 데이터

elif current_page == "마약 예방 방법":
    st.write("마약을 예방하기 위해서는 교육과 법적 규제가 필요하며...")
    st.video("https://www.youtube.com/watch?v=예제URL")  # 유튜브 영상 추가 가능

elif current_page == "마약을 겪은 사람과의 인터뷰":
    st.write("이전에 마약을 경험했던 사람의 이야기를 들어보겠습니다...")

# 페이지 버튼 UI 생성
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("마약이란 무엇인가"):
        st.session_state["page"] = "마약이란 무엇인가"
        st.rerun()

with col2:
    if st.button("마약의 국내 현황"):
        st.session_state["page"] = "마약의 국내 현황"
        st.rerun()

with col3:
    if st.button("마약 예방 방법"):
        st.session_state["page"] = "마약 예방 방법"
        st.rerun()

with col4:
    if st.button("마약을 겪은 사람과의 인터뷰"):
        st.session_state["page"] = "마약을 겪은 사람과의 인터뷰"
        st.rerun()
