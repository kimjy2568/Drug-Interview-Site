import streamlit as st
import pandas as pd

def get_theme_colors():
    if st.session_state.get("theme") == "dark":
        return "#f1f1f1", "#333333"  # 다크모드: 밝은 배경에 어두운 글자
    else:
        return "#333333", "#f1f1f1"  # 라이트모드: 어두운 배경에 밝은 글자
    
# 페이지 상태 저장
if "page" not in st.session_state:
    st.session_state["page"] = "마약이란 무엇인가"  # 기본 페이지 설정

current_page = st.session_state["page"]

st.title(current_page)

# 페이지 내용 출력
if current_page == "마약이란 무엇인가":
    st.subheader("그래서 마약이 뭐야?")
    st.write("#### 마취나 환각 등의 작용을 하는 약물.")
    st.write("##### 일부 마약으로 분류된 물질 중에서는 환자의 고통을 줄이는 등 의학적인 목적으로도 쓰이나 극도로 제한됨")
    st.image("image/drug_example.jpg", caption="마약하면 떠올리는 대표적인 이미지")
    st.subheader("마약의 부작용")
    st.markdown("""
    1. **심리적 의존**  
        마약 사용자는 시간이 지날수록 마약에 대한 심리적 의존이 생기게 됩니다. 이는 지속적인 사용을 초래하고 중독 상태에 빠질 위험을 높입니다.

    2. **신체적 부작용**  
        마약은 심장박동 수를 변화시키고, 신경계를 자극하여 여러 가지 신체적 증상을 유발할 수 있습니다. 지속적인 사용은 심각한 건강 문제를 일으킬 수 있습니다.

    3. **사회적 문제**  
        마약 중독은 개인의 삶에만 영향을 미치는 것이 아니라, 가족, 친구, 사회와의 관계를 단절시킬 수 있습니다. 이는 법적 문제와 사회적 불안을 초래할 수 있습니다.

    4. **치료의 어려움**  
        마약에 의존하게 되면 치료가 어려워질 수 있습니다. 중독 치료를 받지 않으면 정신적, 신체적 문제가 지속될 수 있습니다.
    """)
        
elif current_page == "마약의 국내 현황":
    st.write("### 최근 한국의 마약 범죄는 증가하는 추세")
    st.write("##### 10대 청소년 마약사범은 23년 1,477명으로 역대 최대수준을 기록하였으나, 온라인 마약범죄 집중단속, 청소년 대상 마약 예방교육 강화, 맞춤형 치료·재활 등의 효과로 23년 대비 24년은 649명(56%↓)으로 대폭 감소")
    
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
    st.markdown("""
    1. **마약 예방 및 경각심 높이기**  
        본인과 주변 사람들이 마약의 위험성을 정확히 알고 경각심을 가질 수 있도록 노력하기.  
    친구나 가족이 위험한 상황에 빠질 조짐이 보이면 적극적으로 상담하거나 도움 요청하기.

    2. **의심스러운 상황 신고하기**  
        마약 판매나 유통이 의심되는 상황을 목격하면 경찰(112)이나 관할 기관에 신고.  
        익명으로 신고할 수 있는 채널(예: 경찰청 사이버 범죄 신고) 활용.

    3. **건강한 사회문화 조성**  
        마약 대신 건강한 스트레스 해소법(운동, 취미 활동 등) 찾기.  
        청소년이나 주변인들이 유혹에 빠지지 않도록 긍정적인 환경 조성하기.

    4. **인터넷·SNS에서의 경각심 가지기**  
        SNS, 다크웹 등을 통한 마약 거래가 증가하는 만큼 의심스러운 광고나 연락 주의하기.  
        마약 관련 유혹이 있는 경우 단호하게 거절하고 관련 정보를 공유하지 않기.
    """)
    st.video("https://www.youtube.com/watch?v=lwlGZ2YdLi8")

elif current_page == "마약을 겪은 사람과의 인터뷰":
    interview = [
        ("Q. 마약을 어떻게 접하게 되었나요?", "A. 처음에는 친구들의 유혹으로 마약을 접하게 되었습니다. 당시에는 호기심과 스트레스 해소를 위해 시작했지만, 점점 더 빠져들게 되었습니다."),
        ("Q. 마약 중독의 과정은 어땠나요?", "A. 처음에는 즐거운 기분을 느꼈지만 점차 의존성이 커졌습니다. 점점 마약 없이 일상생활을 하기 어려워졌고, 결국 중독을 겪게 되었습니다."),
        ("Q. 중독 회복 과정은 어떻게 되었나요?", "A. 회복 과정은 매우 힘들었습니다. 나 자신을 되돌아보며 점차 나아가려는 노력이 필요했지만, 모임에서 받은 도움과 함께 조금씩 회복할 수 있었습니다. 주위의 지지와 나만의 변화가 중요한 역할을 했습니다."),
        ("Q. 마약 예방을 위해 사회에서 무엇을 해야 할까요?", "A. 사회는 마약 중독을 단순히 범죄로 보지 말고, 질병으로 인식해야 합니다. 마약 예방 교육과 지원 시스템이 중요하며, 청소년들에게는 건강한 대체 활동을 제공하는 것이 필요합니다."),
        ("Q. 앞으로 마약에 대한 인식을 어떻게 개선할 수 있을까요?", "A. 마약을 단순한 잘못된 선택이 아니라, 질병으로 인식하는 문화가 필요합니다. 또한 마약의 위험성을 알리고, 중독자들을 돕는 사회적 분위기와 지원 체계가 더욱 강화되어야 합니다.")
    ]

    question_color, answer_color = get_theme_colors()
    
    # 말풍선 스타일로 질문은 왼쪽, 답변은 그 아래에 배치
    for q, a in interview:
        st.markdown(f'''
        <div style="display: flex; justify-content: flex-start; margin-bottom: 20px;">
            <div style="background-color:{question_color}; color:{answer_color}; border-radius:15px; padding:10px; width:60%; font-size:16px; font-family:Arial, sans-serif; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);">
                <strong>{q}</strong>
            </div>
        </div>
        <div style="display: flex; justify-content: flex-end; margin-bottom: 20px;">
            <div style="background-color:{answer_color}; color:{question_color}; border-radius:15px; padding:10px; width:80%; font-size:16px; font-family:Arial, sans-serif; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); margin-top: 10px;">
                {a}
            </div>
        </div>
        ''', unsafe_allow_html=True)
    st.write("###### 출처: https://channelpnu.pusan.ac.kr/news/articleView.html?idxno=34682")

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
