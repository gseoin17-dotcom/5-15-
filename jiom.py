import streamlit as st
import time

# 1. 페이지 기본 설정 및 '지온(Geosmin)' 컨셉 스타일링 (CSS)
st.set_page_config(
    page_title="GEOSMIN : Earth & Rain Protocol",
    page_icon="🌧️",
    layout="wide"
)

# 딥 그린, 비젖은 흙색, 안개 효과를 위한 자스 Custom CSS
st.markdown("""
    <style>
    /* 전체 배경을 축축하고 어두운 흙/안개 톤으로 변경 */
    .stApp {
        background-color: #0b0f0d;
        color: #cfd8dc;
        font-family: 'Courier New', monospace;
    }
    
    /* 지온 텍스트 타이틀 스타일ing */
    .geosmin-header {
        font-size: 3.2rem;
        font-weight: 800;
        color: #799a82;
        text-shadow: 0 0 15px rgba(121, 154, 130, 0.4);
        letter-spacing: 4px;
        margin-bottom: 0px;
    }
    
    .geosmin-sub {
        font-size: 1.1rem;
        color: #516356;
        margin-bottom: 30px;
    }

    /* 눅눅한 카드 컨테이너 */
    .moist-card {
        background: rgba(20, 28, 24, 0.7);
        border-left: 3px solid #4e6b56;
        padding: 20px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    
    /* 강조 네온 텍스트 */
    .highlight {
        color: #92b89b;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 2. 메인 헤더
st.markdown('<div class="geosmin-header">C₁₂H₂₂O : GEOSMIN</div>', unsafe_allow_html=True)
st.markdown('<div class="geosmin-sub">소나기가 지난 후, 지표면 1cm 아래에서 피어오르는 강렬한 흙내음 농축기</div>', unsafe_allow_html=True)

st.divider()

# 3. 지온(Geo-smell) 제어 파라미터 섹션
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("**[ 냄새 성분 제어 ]**")
    geosmin_ppm = st.slider("지온(Geosmin) 농도 (ppt)", 0, 500, 85, help="인간의 코는 5ppt 수준의 지온도 감지합니다.")
    petrichor_val = st.slider("페트리코(Petrichor) 식물성 기름 수치", 0, 100, 60)
    ozone_val = st.slider("번개 후 오존(O3) 잔향", 0, 100, 30)

with col2:
    st.markdown("**[ 토양 및 습도 설정 ]**")
    soil_temp = st.select_slider("지열(Soil Temp)", options=["차가운 암석", "서늘한 이끼", "달아오른 흙밭", "건조한 폭염 직후"])
    humidity = st.progress(88, text="상대 습도 (88% - 방가후 축축함 유지 중)")
    actino_active = st.toggle("방선균(Actinomyces) 대사 활성화", value=True)

st.divider()

# 4. 실시간 향기 인터랙션
st.markdown('<div class="moist-card">', unsafe_allow_html=True)
st.markdown("### 🌧️ 지온 냄새 증폭 시뮬레이터")

if st.button("비 뿌리기 (지온 증폭 연출 시작)"):
    with st.status("마른 흙에 첫 빗방울이 떨어지는 중...", expanded=True) as status:
        time.sleep(1)
        st.write("💧 빗방울이 에어로졸을 형성하여 공기 중으로 튀어 오릅니다.")
        time.sleep(1)
        st.write("🌱 방선균의 포자가 방출되며 억눌렸던 <span class='highlight'>지온(Geosmin)</span> 분자가 폭발합니다.", unsafe_allow_html=True)
        time.sleep(1)
        st.write("🌫️ 눅눅하고 짙은 흙내음이 공간 전체로 확산됩니다.")
        status.update(label="증폭 완료: 묵직한 흙내음이 코끝을 지배합니다.", state="complete", expanded=True)
        
    st.metric(
        label="현재 검출된 냄새 강도 (Odor Intensity)", 
        value=f"{geosmin_ppm * 2.4:.1f} OUV", 
        delta="치사량 수준의 감성 흙향"
    )

st.markdown('</div>', unsafe_allow_html=True)

# 5. 지온 노브
st.caption("Tip: 깃허브 `main.py`에 이 코드를 덮어쓰기 하고 `push` 하시면 바로 지온 냄새 뿜뿜하는 사이트로 변경됩니다.")
