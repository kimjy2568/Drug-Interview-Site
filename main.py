import streamlit as st
import pandas as pd

# 페이지 상태 저장
if "page" not in st.session_state:
    st.session_state["page"] = "마약이란 무엇인가"  # 기본 페이지 설정

current_page = st.session_state["page"]

st.title(current_page)

# 페이지 내용 출력
if current_page == "마약이란 무엇인가":
    
    st.write("")
    
elif current_page == "마약의 국내 현황":
    st.write("최근 한국의 마약 범죄는 증가하는 추세")
    st.write("10대 청소년 마약사범은 23년 1,477명으로 역대 최대수준을 기록하였으나, 온라인 마약범죄 집중단속, 청소년 대상 마약 예방교육 강화, 맞춤형 치료·재활 등의 효과로 23년 대비 24년은 649명(56%↓)으로 대폭 감소")
    
    data = {
        "년도": ["20", "21", "22", "23", "24"],
        "전체 마약사범 단속인원(명)": [18050, 16153, 18395, 27611, 23022],
        "밀수입사범 단속인원(명)": [837, 807, 1392, 1235, 1126],
        "밀매사범 단속인원(명)": [3947, 3229, 3492, 7904, 6593],
        "투약사범 단속인원(명)": [9044, 8522, 8489, 10899, 9528],
        "10대 마약사범(명)": [313, 450, 481, 1477, 649],
        "마약류 압수량(kg)": [321, 1295, 804, 998, 1173]
    }

    # pandas DataFrame으로 변환
    df = pd.DataFrame(data)
    
    # 표 그리기
    st.table(df.set_index("년도"))
    
    # 차트 그리기
    st.bar_chart(df.set_index("년도"))

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
