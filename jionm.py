import streamlit as st
import random
import time

# -----------------------------------------------------------------------------
# 1. 페이지 설정 및 지독한 냄새 테마 / 애니메이션 CSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - 30단계 도전!",
    page_icon="🤢",
    layout="centered"
)

# 냄새나고 눅눅한 썩은 늪지대 스타일 커스텀 CSS
st.markdown("""
    <style>
    /* 배경: 썩은 독성 습지 및 냄새 안개 그라데이션 */
    .stApp {
        background: linear-gradient(135deg, #050e06 0%, #111e0e 50%, #0a1309 100%);
        color: #d2e8d4;
        font-family: 'Malgun Gothic', 'Dotum', sans-serif;
    }

    /* 화면 전체에 냄새/연기가 일렁이는 듯한 독성 애니메이션 */
    @keyframes stinkyFog {
        0% { box-shadow: inset 0 0 50px rgba(45, 90, 39, 0.3); }
        50% { box-shadow: inset 0 0 100px rgba(100, 160, 40, 0.5); }
        100% { box-shadow: inset 0 0 50px rgba(45, 90, 39, 0.3); }
    }
    
    .stApp > header { background-color: transparent !important; }

    /* 화면 흔들림 (파괴 시 적용) */
    @keyframes shake {
        0% { transform: translate(1px, 1px) rotate(0deg); }
        10% { transform: translate(-2px, -2px) rotate(-1deg); }
        20% { transform: translate(-3px, 0px) rotate(1deg); }
        30% { transform: translate(3px, 2px) rotate(0deg); }
        40% { transform: translate(1px, -1px) rotate(1deg); }
        50% { transform: translate(-1px, 2px) rotate(-1deg); }
        60% { transform: translate(-3px, 1px) rotate(0deg); }
        70% { transform: translate(3px, 1px) rotate(-1deg); }
        80% { transform: translate(-1px, -1px) rotate(1deg); }
        90% { transform: translate(1px, 2px) rotate(0deg); }
        100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    
    /* 냄새나는 게임 메인 박스 */
    .game-box {
        background: rgba(18, 31, 20, 0.85);
        border: 3px solid #5a8a4f;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 30px rgba(80, 200, 60, 0.25);
        margin-bottom: 20px;
        animation: stinkyFog 4s infinite ease-in-out;
        position: relative;
    }

    .destroyed-screen {
        animation: shake 0.5s !important;
        border: 4px solid #ff2222 !important;
        background: rgba(60, 10, 10, 0.9) !important;
        box-shadow: 0 0 40px rgba(255, 0, 0, 0.6) !important;
    }
    
    .smell-level {
        font-size: 1.3rem;
        color: #92d480;
        font-weight: bold;
    }
    
    .smell-title {
        font-size: 2.2rem;
        color: #55ff66;
        font-weight: 900;
        text-shadow: 0 0 15px rgba(85, 255, 102, 0.8);
        margin: 15px 0;
    }
    
    .smell-desc {
        font-size: 1.05rem;
        color: #c0ebbd;
        font-style: italic;
        background: rgba(5, 15, 7, 0.7);
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #3d6337;
    }
    
    .stat-badge {
        background: rgba(15, 30, 17, 0.9);
        border: 1px solid #52804b;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: bold;
        color: #e1f5e2;
        display: inline-block;
        margin: 5px;
    }
    
    .prob-info {
        font-size: 0.95rem;
        color: #e0e0e0;
        background: rgba(10, 20, 11, 0.9);
        padding: 12px;
        border-radius: 8px;
        border-left: 5px solid #d4ac0d;
    }
    
    /* 빡침 경고창 */
    .rage-box {
        background: #4a0000;
        color: #ffb3b3;
        border: 2px dashed #ff3333;
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
        font-size: 1.15rem;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(255,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. 30단계 데이터베이스 (20단계부터 자이온맘 집중 배치!)
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 무취의 공간", "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.", "price": 0},
    1: {"name": "1단계 : 스쳐가는 지온냄새", "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.", "price": 100},
    2: {"name": "2단계 : 은은한 자이온냄새", "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.", "price": 300},
    3: {"name": "3단계 : 습한 지온냄새", "desc": "비 온 뒤 짙은 상록수 숲속에서 감도는 냄새.", "price": 700},
    4: {"name": "4단계 : 진득한 자이온냄새", "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.", "price": 1500},
    5: {"name": "5단계 : 자극적인 지온냄새", "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.", "price": 3500},
    6: {"name": "6단계 : 풍부한 자이온냄새", "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.", "price": 8000},
    7: {"name": "7단계 : 압도적인 지온냄새", "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.", "price": 18000},
    8: {"name": "8단계 : 폭발하는 자이온냄새", "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.", "price": 40000},
    9: {"name": "9단계 : 시공을 뒤흔드는 지온냄새", "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.", "price": 90000},
    10: {"name": "10단계 : 치명적인 자이온냄새", "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.", "price": 200000},
    11: {"name": "11단계 : 환각을 부르는 지온냄새", "desc": "태초의 지구 흙밭을 거니는 환각을 본다.", "price": 450000},
    12: {"name": "12단계 : 공간지배 자이온냄새", "desc": "방 안의 모든 산소를 지온 분자로 채운다.", "price": 1000000},
    13: {"name": "13단계 : 전설의 지온냄새", "desc": "역사서에서 언급되던 전설 속의 지구 향기.", "price": 2200000},
    14: {"name": "14단계 : 신성한 자이온냄새", "desc": "마음이 경건해지며 흙과 하나가 되는 기분.", "price": 5000000},
    15: {"name": "15단계 : 신화급 지온냄새", "desc": "신들이 세계를 창조할 때 맡았다는 향.", "price": 12000000},
    16: {"name": "16단계 : 우주관통 자이온냄새", "desc": "성층권을 뚫고 우주선까지 퍼져나간다.", "price": 30000000},
    17: {"name": "17단계 : 차원균열 지온냄새", "desc": "평행세계의 흙냄새까지 끌어당긴다.", "price": 75000000},
    18: {"name": "18단계 : Absolute 자이온냄새", "desc": "만물의 요소를 지온 입자로 바꿔버린다.", "price": 180000000},
    19: {"name": "19단계 : 초월적 지온냄새", "desc": "인간의 감각으로는 수용 불가능한 향기.", "price": 450000000},
    
    # --- 20단계부터 세계관 최강자 '자이온맘' 강림 ---
    20: {"name": "20단계 : 자이온맘의 포근한 집밥 냄새", "desc": "지온 최고 존엄 자이온맘의 강림! 따스하고 거부할 수 없는 구수한 냄새.", "price": 1000000000},
    21: {"name": "21단계 : 자이온맘의 엄격한 등짝 스매싱 냄새", "desc": "매콤하면서도 사랑이 깃든 자이온맘 특유의 정신이 번쩍 드는 향.", "price": 2500000000},
    22: {"name": "22단계 : 자이온맘이 끓여준 전설의 흙된장국", "desc": "한 입 가득 퍼지는 극상의 흙내음과 자이온맘의 깊은 손맛.", "price": 6000000000},
    23: {"name": "23단계 : 자이온맘의 100년 숙성 지온 원액", "desc": "자이온맘이 장독대 깊은 곳에서 몰래 아껴둔 냄새의 결정체.", "price": 15000000000},
    24: {"name": "24단계 : 자이온맘의 잔소리가 담긴 지온스프레이", "desc": "청소할 때 자이온맘이 집안 가득 뿌리는 치명적인 청량함.", "price": 40000000000},
    25: {"name": "25단계 : 자이온맘의 무한한 지온 은혜", "desc": "온 은하수 아이들에게 평화와 흙향을 내리는 자이온맘의 자애로움.", "price": 100000000000},
    26: {"name": "26단계 : 자이온맘의 궁극의 지온 필살기", "desc": "자이온맘이 분노하면 우주 전체가 지온 향으로 뒤덮인다.", "price": 250000000000},
    27: {"name": "27단계 : 자이온맘의 창조와 구원의 지온향", "desc": "우주 빅뱅 당시 자이온맘이 손수 터뜨린 절대 구원의 향기.", "price": 600000000000},
    28: {"name": "28단계 : 자이온맘 권능의 신성 지온냄새", "desc": "창조주도 자이온맘 앞에서는 고개를 숙이고 냄새를 맡는다.", "price": 1500000000000},
    29: {"name": "29단계 : 만물의 어머니 ★자이온맘★의 숨결", "desc": "우주 만물이 자이온맘의 품으로 돌아가는 최종 직전의 오라.", "price": 4000000000000},
    30: {"name": "30단계 : ★태초의 자이온맘★ 절대신성 지온냄새", "desc": "강화의 정점! 우주를 지온의 온기와 냄새로 통일한 자이온맘의 완성.", "price": 10000000000000}
}

# -----------------------------------------------------------------------------
# 3. 강화 확률표
# -----------------------------------------------------------------------------
PROB_TABLE = {
    0: (100, 0, 0), 1: (95, 5, 0), 2: (90, 10, 0), 3: (85, 15, 0), 4: (80, 20, 0),
    5: (75, 25, 0), 6: (70, 28, 2), 7: (65, 30, 5), 8: (60, 32, 8), 9: (55, 35, 10),
    10: (50, 38, 12), 11: (45, 40, 15), 12: (40, 42, 18), 13: (35, 45, 20), 14: (30, 48, 22),
    15: (25, 50, 25), 16: (20, 53, 27), 17: (15, 55, 30), 18: (12, 53, 35), 19: (10, 50, 40),
    20: (8, 47, 45), 21: (6, 44, 50), 22: (5, 40, 55), 23: (4, 36, 60), 24: (3, 32, 65),
    25: (2, 28, 70), 26: (1.5, 23.5, 75), 27: (1.0, 19.0, 80), 28: (0.5, 14.5, 85), 29: (0.1, 9.9, 90)
}

# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
    st.session_state.level = 0
if "money" not in st.session_state:
    st.session_state.money = 1000
if "max_level" not in st.session_state:
    st.session_state.max_level = 0
if "is_destroyed" not in st.session_state:
    st.session_state.is_destroyed = False
if "rage_msg" not in st.session_state:
    st.session_state.rage_msg = ""

RAGE_QUOTES = [
    "🖐️ 자이온맘: '어딜 감히 손을 대! 마르지도 않은 냄새 억지로 피우다가 다 터졌잖아!'",
    "💥 팡-!! 냄새 분자가 수용량을 초과하여 증발했습니다. 0단계부터 다시 하세요 ㅋㅋㅋ",
    "👋 자이온맘의 등짝 스매싱이 불을 뿜었습니다! (지온 농도 0%로 초기화)",
    "🤣 방금 그 확률을 못 뚫고 터지셨나요? 능지 상승 추천드립니다!",
    "💸 강화 스노우볼 깔끔하게 폭파! 소중한 자이온냄새는 공기 중으로 사라졌습니다."
]

# -----------------------------------------------------------------------------
# 5. 강화 / 판매 로직
# -----------------------------------------------------------------------------
def enhance():
    st.session_state.is_destroyed = False
    st.session_state.rage_msg = ""
    curr_lvl = st.session_state.level
    
    if curr_lvl >= 30:
        return

    # 강화 시 냄새 응축 연출
    with st.spinner("🤢 눅눅한 지온 입자를 응축하는 중..."):
        time.sleep(0.8)

    succ_p, fail_p, dest_p = PROB_TABLE[curr_lvl]
    rand_val = random.uniform(0, 100)
    
    # 성공
    if rand_val < succ_p:
        st.session_state.level += 1
        new_lvl = st.session_state.level
        if new_lvl > st.session_state.max_level:
            st.session_state.max_level = new_lvl
        st.toast(f"✨ 성공! {new_lvl}단계 달성!", icon="🤢")
        if new_lvl >= 20:
            st.balloons()
            
    # 파괴
    elif rand_val < (succ_p + dest_p):
        st.session_state.level = 0
        st.session_state.is_destroyed = True
        st.session_state.rage_msg = random.choice(RAGE_QUOTES)
        st.toast("💥 펑!! 냄새가 터졌습니다!!", icon="💣")
        
    # 실패 (하락)
    else:
        if curr_lvl > 0:
            st.session_state.level -= 1
            st.toast("🔻 실패... 1단계 하락", icon="🌧️")

def sell():
    curr_lvl = st.session_state.level
    if curr_lvl == 0:
        return
        
    price = SMELL_DB[curr_lvl]['price']
    st.session_state.money += price
    st.session_state.level = 0
    st.session_state.is_destroyed = False
    st.toast(f"💰 {price:,} 골드 획득!", icon="💵")

# -----------------------------------------------------------------------------
# 6. 메인 UI
# -----------------------------------------------------------------------------
st.title("🤢 지온냄새 강화하기")
st.caption("독성 안개 연출 탑재 | 후반부 자이온맘 강림")

# 상단 상태바
c1, c2 = st.columns(2)
with c1:
    st.markdown(f'<div class="stat-badge">💰 보유 골드: {st.session_state.money:,} G</div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="stat-badge">🏆 최고 기록: {st.session_state.max_level} 단계</div>', unsafe_allow_html=True)

st.write("")

# 💥 파괴 시 출력되는 빡침 메시지 박스
if st.session_state.is_destroyed:
    st.markdown(f'<div class="rage-box">{st.session_state.rage_msg}</div>', unsafe_allow_html=True)

# 메인 강화 디스플레이
box_class = "game-box destroyed-screen" if st.session_state.is_destroyed else "game-box"
curr_data = SMELL_DB[st.session_state.level]

st.markdown(f"""
    <div class="{box_class}">
        <div class="smell-level">현재 지온 농도 [ {st.session_state.level} / 30 단계 ]</div>
        <div class="smell-title">{curr_data['name']}</div>
        <div class="smell-desc">"{curr_data['desc']}"</div>
        <br>
        <div style="font-size: 1.1rem; color: #75ff85; font-weight: bold;">
            현재 판매 가치: {curr_data['price']:,} G
        </div>
    </div>
""", unsafe_allow_html=True)

# 강화 확률 안내
if st.session_state.level < 30:
    sp, fp, dp = PROB_TABLE[st.session_state.level]
    st.markdown(f"""
        <div class="prob-info">
            <b>📊 강화 확률</b> — 
            성공: <span style="color:#2ecc71; font-weight:bold;">{sp}%</span> | 
            실패(하락): <span style="color:#e67e22; font-weight:bold;">{fp}%</span> | 
            <span style="color:#ff4d4d; font-weight:bold;">파괴: {dp}%</span>
        </div>
    """, unsafe_allow_html=True)
else:
    st.success("🎉 축하합니다! ★태초의 자이온맘★ 신의 지온냄새를 완성하셨습니다!")

st.write("")

# 조작 버튼
btn1, btn2 = st.columns(2)
with btn1:
    if st.button("🔥 냄새 강화하기", use_container_width=True, disabled=(st.session_state.level >= 30)):
        enhance()
        st.rerun()

with btn2:
    if st.button("💰 냄새 판매하기", use_container_width=True, disabled=(st.session_state.level == 0)):
        sell()
        st.rerun()
