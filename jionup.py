import streamlit as st
import random
import time

# -----------------------------------------------------------------------------
# 1. 페이지 및 기본 스타일 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - 30단계 도전!",
    page_icon="👃",
    layout="centered"
)

# 검 강화하기 특유의 플래시 게임 감성을 살린 CSS Custom
st.markdown("""
    <style>
    .stApp {
        background-color: #0f1410;
        color: #e0e0e0;
        font-family: 'Malgun Gothic', 'Dotum', sans-serif;
    }
    
    .game-box {
        background: #18221a;
        border: 3px solid #486b50;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0,255,100,0.1);
        margin-bottom: 20px;
    }
    
    .smell-level {
        font-size: 1.4rem;
        color: #8bbd93;
        font-weight: bold;
    }
    
    .smell-title {
        font-size: 2.3rem;
        color: #00ff88;
        font-weight: 900;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
        margin: 15px 0;
    }
    
    .smell-desc {
        font-size: 1.05rem;
        color: #a3c2a8;
        font-style: italic;
        background: rgba(0,0,0,0.3);
        padding: 10px;
        border-radius: 6px;
    }
    
    .stat-badge {
        background: #253629;
        border: 1px solid #4d7a56;
        padding: 8px 15px;
        border-radius: 20px;
        font-weight: bold;
        color: #f0f0f0;
        display: inline-block;
        margin: 5px;
    }
    
    .prob-info {
        font-size: 0.95rem;
        color: #d1d1d1;
        background: #121913;
        padding: 10px;
        border-radius: 6px;
        border-left: 4px solid #f39c12;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. 30단계 지온냄새 데이터베이스 (이름, 설명, 판매가)
#    - 이름에 반드시 '지온냄새', '자이온냄새', '자이온맘' 포함!
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 무취의 공간", "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.", "price": 0},
    1: {"name": "1단계 : 스쳐가는 지온냄새", "desc": "스쳐 지나가듯 살짝 코끝을 스치는 약한 흙과 이끼의 냄새.", "price": 100},
    2: {"name": "2단계 : 은은한 자이온냄새", "desc": "마른 땅에 단비가 사뿐히 내릴 때 퍼지는 편안한 냄새.", "price": 300},
    3: {"name": "3단계 : 따스한 자이온맘의 품냄새", "desc": "자이온맘이 차려준 따뜻한 집밥과 포근한 이불 냄새.", "price": 700},
    4: {"name": "4단계 : 눅눅한 지온냄새", "desc": "비 온 뒤 습한 숲속 골짜기 깊은 곳에서 피어나는 냄새.", "price": 1500},
    5: {"name": "5단계 : 자극적인 자이온냄새", "desc": "코를 찌르는 강렬한 습기와 방선균의 대사 냄새.", "price": 3500},
    6: {"name": "6단계 : 자이온맘이 끓여준 흙내음 국물", "desc": "깊은 맛과 풍미가 공기 중에 진동하는 지온의 진국.", "price": 8000},
    7: {"name": "7단계 : 진득한 지온냄새", "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 코에 들어온다.", "price": 18000},
    8: {"name": "8단계 : 압도적인 자이온냄새", "desc": "주변 10m 안의 모든 냄새를 집어삼키는 자이온의 기운.", "price": 40000},
    9: {"name": "9단계 : 자이온맘의 엄격한 지온 손길", "desc": "자이온맘의 사랑과 매콤한 손맛이 깃든 강력한 지온의 향.", "price": 90000},
    10: {"name": "10단계 : 폭발하는 지온냄새", "desc": "코가 번쩍 뜨일 정도로 폭발적인 페트리코 입자의 대반란.", "price": 200000},
    11: {"name": "11단계 : 시공을 비트는 자이온냄새", "desc": "냄새만으로 시공간이 약간 일렁이는 듯한 환각을 일으킨다.", "price": 450000},
    12: {"name": "12단계 : 자이온맘의 특제 지온 에센스", "desc": "자이온맘이 100년간 숙성시킨 지온 원액 한 방울의 위력.", "price": 1000000},
    13: {"name": "13단계 : 치명적인 지온냄새", "desc": "한 번 마시면 다른 냄새는 평생 맡을 수 없을 정도로 강렬하다.", "price": 2200000},
    14: {"name": "14단계 : 환각을 부르는 자이온냄새", "desc": "눈을 감으면 대자연과 고대 지구의 흙이 눈앞에 펼쳐진다.", "price": 5000000},
    15: {"name": "15단계 : 자이온맘의 분노가 담긴 지온스프레이", "desc": "자이온맘이 등짝 스매싱과 함께 뿌리는 치명적인 냄새.", "price": 12000000},
    16: {"name": "16단계 : 공간을 지배하는 지온냄새", "desc": "방 안의 모든 산소를 지온 입자로 대체해 버린다.", "price": 30000000},
    17: {"name": "17단계 : 전설의 자이온냄새", "desc": "역사서에만 전해 내려오던 전설 속 지구의 태초 향기.", "price": 75000000},
    18: {"name": "18단계 : 자이온맘의 궁극의 지온 손맛", "desc": "우주 만물의 원소를 흙내음으로 변환시키는 자이온맘의 권능.", "price": 180000000},
    19: {"name": "19단계 : 신성한 지온냄새", "desc": "맡는 순간 마음이 경건해지며 흙과 하나가 되는 기분.", "price": 450000000},
    20: {"name": "20단계 : 신화급 자이온냄새", "desc": "신들이 세계를 창조할 때 맡았다는 지극히 거룩한 냄새.", "price": 1000000000},
    21: {"name": "21단계 : 자이온맘이 창조한 지온의 태초", "desc": "자이온맘이 빅뱅과 함께 터뜨린 우주 최초의 흙향.", "price": 2500000000},
    22: {"name": "22단계 : 우주를 관통하는 지온냄새", "desc": "지구 너머 은하계까지 퍼져나가는 범우주적 지온 파동.", "price": 6000000000},
    23: {"name": "23단계 : 차원을 뒤흔드는 자이온냄새", "desc": "평행세계의 지온 냄새까지 끌어올려 차원을 균열시킨다.", "price": 15000000000},
    24: {"name": "24단계 : 자이온맘의 무한한 지온 은혜", "desc": "끝없는 사랑으로 온 은하수를 지온 향기로 가득 채운다.", "price": 40000000000},
    25: {"name": "25단계 : 기적의 지온냄새", "desc": "모든 악취를 단숨에 성스러운 흙향으로净化시키는 기적.", "price": 100000000000},
    26: {"name": "26단계 : 절대존재의 자이온냄새", "desc": "이 냄새 앞에서는 그 어떤 필멸자도 고개를 숙일 수밖에 없다.", "price": 250000000000},
    27: {"name": "27단계 : 자이온맘의 강림과 지온의 구원", "desc": "자이온맘이 직접 오셔서 온 세상에 구원의 지온 향을 내리신다.", "price": 600000000000},
    28: {"name": "28단계 : 신을 뛰어넘은 지온냄새", "desc": "창조주마저 매료되어 지온의 노예가 되게 만드는 냄새.", "price": 1500000000000},
    29: {"name": "29단계 : 만물의 근원 자이온냄새", "desc": "우주 만물의 모든 분자가 지온 분자로 변이하는 최고조의 상태.", "price": 4000000000000},
    30: {"name": "30단계 : ★태초의 자이온맘★ 신의 지온냄새", "desc": "강화의 정점! 우주를 지온의 향기로 완벽히 통일한 절대신성.", "price": 10000000000000}
}

# -----------------------------------------------------------------------------
# 3. 플래시 '검 강화하기' 원작 기준 강화 확률표 (성공, 하락, 파괴)
#    (단계별 % : [성공, 하락/유지, 파괴])
# -----------------------------------------------------------------------------
PROB_TABLE = {
    0: (100, 0, 0),
    1: (95, 5, 0),
    2: (90, 10, 0),
    3: (85, 15, 0),
    4: (80, 20, 0),
    5: (75, 25, 0),
    6: (70, 28, 2),
    7: (65, 30, 5),
    8: (60, 32, 8),
    9: (55, 35, 10),
    10: (50, 38, 12),
    11: (45, 40, 15),
    12: (40, 42, 18),
    13: (35, 45, 20),
    14: (30, 48, 22),
    15: (25, 50, 25),
    16: (20, 53, 27),
    17: (15, 55, 30),
    18: (12, 53, 35),
    19: (10, 50, 40),
    20: (8, 47, 45),
    21: (6, 44, 50),
    22: (5, 40, 55),
    23: (4, 36, 60),
    24: (3, 32, 65),
    25: (2, 28, 70),
    26: (1.5, 23.5, 75),
    27: (1.0, 19.0, 80),
    28: (0.5, 14.5, 85),
    29: (0.1, 9.9, 90)
}

# -----------------------------------------------------------------------------
# 4. 게임 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
    st.session_state.level = 0
if "money" not in st.session_state:
    st.session_state.money = 1000
if "max_level" not in st.session_state:
    st.session_state.max_level = 0
if "history" not in st.session_state:
    st.session_state.history = ["게임을 시작했습니다. 지온의 향기를 증폭시켜보세요!"]

# -----------------------------------------------------------------------------
# 5. 강화 로직 함수
# -----------------------------------------------------------------------------
def enhance():
    curr_lvl = st.session_state.level
    
    if curr_lvl >= 30:
        st.session_state.history.insert(0, "🏆 이미 최고 단계(30단계)에 도달했습니다!")
        return

    succ_p, fail_p, dest_p = PROB_TABLE[curr_lvl]
    rand_val = random.uniform(0, 100)
    
    # 성공
    if rand_val < succ_p:
        st.session_state.level += 1
        new_lvl = st.session_state.level
        if new_lvl > st.session_state.max_level:
            st.session_state.max_level = new_lvl
        st.session_state.history.insert(0, f"✨ [성공!] {SMELL_DB[new_lvl]['name']}(으)로 증폭되었습니다!")
        st.balloons()
    # 파괴
    elif rand_val < (succ_p + dest_p):
        old_name = SMELL_DB[curr_lvl]['name']
        st.session_state.level = 0
        st.session_state.history.insert(0, f"💥 [파괴!!] {old_name} 증폭 중 냄새 분자가 수용량을 초과하여 0단계로 초기화되었습니다!")
    # 실패 (하락 또는 유지)
    else:
        if curr_lvl > 0:
            st.session_state.level -= 1
            st.session_state.history.insert(0, f"🔻 [실패] 증폭에 실패하여 1단계 하락했습니다... ({SMELL_DB[st.session_state.level]['name']})")
        else:
            st.session_state.history.insert(0, "💨 [실패] 0단계에서는 더 이상 하락하지 않습니다.")

def sell():
    curr_lvl = st.session_state.level
    if curr_lvl == 0:
        st.session_state.history.insert(0, "⚠️ 0단계 상태에서는 판매할 수 없습니다.")
        return
        
    price = SMELL_DB[curr_lvl]['price']
    st.session_state.money += price
    sold_name = SMELL_DB[curr_lvl]['name']
    st.session_state.level = 0
    st.session_state.history.insert(0, f"💰 [판매완료] {sold_name}을(를) {price:,} 골드에 판매했습니다!")

# -----------------------------------------------------------------------------
# 6. 메인 UI 출력
# -----------------------------------------------------------------------------
st.title("👃 지온냄새 강화하기")
st.caption("원작 '검 강화하기' 완벽 오마주 | 1~30단계 지온/자이온/자이온맘 극강의 향기 컬렉션")

# 상단 상태바 (보유 골드 & 최고 기록)
col_stat1, col_stat2 = st.columns(2)
with col_stat1:
    st.markdown(f'<div class="stat-badge">💰 보유 골드: {st.session_state.money:,} G</div>', unsafe_allow_html=True)
with col_stat2:
    st.markdown(f'<div class="stat-badge">🏆 최고 도달 단계: {st.session_state.max_level} 단계</div>', unsafe_allow_html=True)

st.write("")

# 메인 강화 화면 박스
curr_data = SMELL_DB[st.session_state.level]
st.markdown(f"""
    <div class="game-box">
        <div class="smell-level">현재 지온 농도 [ {st.session_state.level} / 30 단계 ]</div>
        <div class="smell-title">{curr_data['name']}</div>
        <div class="smell-desc">"{curr_data['desc']}"</div>
        <br>
        <div style="font-size: 1.1rem; color: #ffd700; font-weight: bold;">
            현재 판매 가치: {curr_data['price']:,} G
        </div>
    </div>
""", unsafe_allow_html=True)

# 현재 단계 강화 확률 안내
if st.session_state.level < 30:
    sp, fp, dp = PROB_TABLE[st.session_state.level]
    st.markdown(f"""
        <div class="prob-info">
            <b>📊 다음 단계 강화 확률</b><br>
            성공: <span style="color:#2ecc71; font-weight:bold;">{sp}%</span> | 
            실패(하락): <span style="color:#e67e22; font-weight:bold;">{fp}%</span> | 
            파괴: <span style="color:#e74c3c; font-weight:bold;">{dp}%</span>
        </div>
    """, unsafe_allow_html=True)
else:
    st.success("🎉 축하합니다! 최종 30단계 '★태초의 자이온맘★ 신의 지온냄새'를 달성하셨습니다!")

st.write("")

# 조작 버튼 그룹
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🔥 지온냄새 강화하기", use_container_width=True, disabled=(st.session_state.level >= 30)):
        enhance()
        st.rerun()

with btn_col2:
    if st.button("💰 현재 냄새 판매하기", use_container_width=True, disabled=(st.session_state.level == 0)):
        sell()
        st.rerun()

st.divider()

# 로그 기록 (최근 5개)
st.subheader("📜 강화 로그")
for log in st.session_state.history[:6]:
    st.write(log)
