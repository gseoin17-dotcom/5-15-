import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정 및 메타데이터
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="갤럭시 오브 지온 - 코스믹 유니버스 에디션",
    page_icon="🌌",
    layout="wide",
)

# -----------------------------------------------------------------------------
# 2. 대규모 상수 및 데이터베이스 정의 (확장형 스코프)
# -----------------------------------------------------------------------------
ACHIEVEMENTS_DB = {
    "first_step": {"name": "태초의 첫걸음", "desc": "1단계 강화에 최초로 도달하세요.", "reward": 50000},
    "tier_2": {"name": "대기권을 뚫고", "desc": "6단계(티어 2)에 도달하세요.", "reward": 300000},
    "tier_3": {"name": "행성 궤도 진입", "desc": "11단계(티어 3)에 도달하세요.", "reward": 2000000},
    "tier_4": {"name": "성간 항해자", "desc": "16단계(티어 4)에 도달하세요.", "reward": 15000000},
    "tier_5": {"name": "자이온맘의 친자인증", "desc": "21단계(티어 5)에 도달하세요.", "reward": 100000000},
    "tier_6": {"name": "우주의 지배자", "desc": "26단계(티어 6)에 도달하세요.", "reward": 1000000000},
    "max_god": {"name": "태초의 절대신", "desc": "최종 30단계 만렙을 달성하세요.", "reward": 50000000000},
    "bankrupt": {"name": "우주적 빈곤", "desc": "소지금이 정확히 0원이 되어보세요.", "reward": 100000},
}

QUESTS_DB = [
    {"id": 1, "title": "초보 에테르 수집", "target_level": 5, "reward": 10000, "desc": "지온 냄새를 5단계까지 강화하세요."},
    {"id": 2, "title": "중력장 돌파", "target_level": 10, "reward": 80000, "desc": "지온 냄새를 10단계까지 강화하세요."},
    {"id": 3, "title": "차원 왜곡 현상", "target_level": 15, "reward": 500000, "desc": "지온 냄새를 15단계까지 강화하세요."},
    {"id": 4, "title": "성단 지배", "target_level": 20, "reward": 3000000, "desc": "지온 냄새를 20단계까지 강화하세요."},
    {"id": 5, "title": "자이온맘과의 조우", "target_level": 25, "reward": 25000000, "desc": "지온 냄새를 25단계까지 강화하세요."},
    {"id": 6, "title": "우주 통일", "target_level": 30, "reward": 500000000, "desc": "지온 냄새를 30단계 만렙으로 만드세요."},
]

TITLE_DB = {
    0: "무소유의 방랑자",
    5: "코끝의 연금술사",
    10: "시공간의 방해꾼",
    15: "은하계의 후각 패권자",
    20: "자이온맘의 수양아들",
    25: "차원을 넘나드는 향기 마스터",
    30: "우주 만물의 근원 ★태초의 신★"
}

# -----------------------------------------------------------------------------
# 3. 유틸리티 및 경제 포맷터 함수
# -----------------------------------------------------------------------------
def format_gold(amount):
    if amount == 0 or amount == float('inf'):
        return "0원" if amount == 0 else "무한대(INF)"
    
    units = ["", "만", "억", "조", "경", "해"]
    result = []
    unit_idx = 0
    while amount > 0 and unit_idx < len(units):
        remainder = int(amount % 10000)
        if remainder > 0:
            result.insert(0, f"{remainder:,}{units[unit_idx]}")
        amount //= 10000
        unit_idx += 1
    return "".join(result) + "원"

def get_enhance_cost(level):
    cost_table = {
        0: 300, 1: 300, 2: 500, 3: 500, 4: 1000, 5: 1500, 6: 2000, 7: 2000, 8: 3000, 9: 5000,
        10: 10900, 11: 20000, 12: 35000, 13: 55000, 14: 100000, 15: 180000, 16: 300000, 17: 300000,
        18: 500000, 19: 800000, 20: 1500000, 21: 2500000, 22: 4000000, 23: 6500000, 24: 10000000,
        25: 16000000, 26: 25000000, 27: 40000000, 28: 65000000, 29: 100000000, 30: 150000000
    }
    return cost_table.get(level, 150000000)

def get_shield_cost(level):
    base_cost = get_enhance_cost(level)
    return max(50000, base_cost * 15)

# -----------------------------------------------------------------------------
# 4. 게임 데이터베이스 확장 정의 (아이템, 펫, 스킬 등)
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 무취의 공간", "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.", "price": 0, "color": "#4a5568", "tier": 1},
    1: {"name": "1단계 : 스쳐가는 지온냄새", "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.", "price": 150, "color": "#718096", "tier": 1},
    2: {"name": "2단계 : 은은한 자이온냄새", "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.", "price": 400, "color": "#38a169", "tier": 1},
    3: {"name": "3단계 : 습한 지온냄새", "desc": "비 온 뒤 짙은 상록수 숲속에서 감오는 냄새.", "price": 600, "color": "#276749", "tier": 1},
    4: {"name": "4단계 : 진득한 자이온냄새", "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.", "price": 800, "color": "#319795", "tier": 1},
    5: {"name": "5단계 : 자극적인 지온냄새", "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.", "price": 3000, "color": "#2c7a7b", "tier": 1},
    6: {"name": "6단계 : 풍부한 자이온냄새", "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.", "price": 3500, "color": "#3182ce", "tier": 2},
    7: {"name": "7단계 : 압도적인 지온냄새", "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.", "price": 6100, "color": "#2b6cb0", "tier": 2},
    8: {"name": "8단계 : 폭발하는 지온냄새", "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.", "price": 10000, "color": "#805ad5", "tier": 2},
    9: {"name": "9단계 : 시공을 뒤흔드는 지온냄새", "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.", "price": 20000, "color": "#6b46c1", "tier": 2},
    10: {"name": "10단계 : 치명적인 자이온냄새", "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.", "price": 35100, "color": "#d69e2e", "tier": 2},
    11: {"name": "11단계 : 환각을 부르는 지온냄새", "desc": "태초의 지구 흙밭을 거니는 환각을 본다.", "price": 160000, "color": "#b7791f", "tier": 3},
    12: {"name": "12단계 : 공간지배 자이온냄새", "desc": "방 안의 모든 산소를 지온 분자로 채운다.", "price": 350000, "color": "#dd6b20", "tier": 3},
    13: {"name": "13단계 : 전설의 지온냄새", "desc": "역사서에서 언급되던 전설 속의 지구 향기.", "price": 1000000, "color": "#c05621", "tier": 3},
    14: {"name": "14단계 : 신성한 자이온냄새", "desc": "마음이 경건해지며 흙과 하나가 되는 기분.", "price": 3000000, "color": "#e53e3e", "tier": 3},
    15: {"name": "15단계 : 신화급 지온냄새", "desc": "신들이 세계를 창조할 때 맡았다는 향.", "price": 7500000, "color": "#9b2c2c", "tier": 3},
    16: {"name": "16단계 : 우주관통 자이온냄새", "desc": "성층권을 뚫고 우주선까지 퍼져나간다.", "price": 14200000, "color": "#00f0ff", "tier": 4},
    17: {"name": "17단계 : 차원균열 자이온냄새", "desc": "평행세계의 흙냄새까지 끌어당긴다.", "price": 20000000, "color": "#ff00ea", "tier": 4},
    18: {"name": "18단계 : Absolute 자이온냄새", "desc": "만물의 요소를 지온 입자로 바꿔버린다.", "price": 30000000, "color": "#ffe600", "tier": 4},
    19: {"name": "19단계 : 초월적 지온냄새", "desc": "인간의 감각으로는 수용 불가능한 향기.", "price": 47500000, "color": "#ff0055", "tier": 4},
    20: {"name": "20단계 : 자이온맘의 포근한 집밥 냄새", "desc": "자이온맘의 강림! 따스하고 구수한 냄새.", "price": 68300000, "color": "#ffaa00", "tier": 4},
    21: {"name": "21단계 : 자이온맘의 엄격한 등짝 스매싱", "desc": "매콤하면서 사랑이 깃든 자이온맘의 향.", "price": 101000000, "color": "#ff4500", "tier": 5},
    22: {"name": "22단계 : 자이온맘의 전설의 흙된장국", "desc": "극상의 흙내음과 깊은 손맛.", "price": 160000000, "color": "#ff007f", "tier": 5},
    23: {"name": "23단계 : 자이온맘의 100년 숙성 원액", "desc": "몰래 아껴둔 냄새의 결정체.", "price": 230000000, "color": "#7b00ff", "tier": 5},
    24: {"name": "24단계 : 자이온맘의 지온스프레이", "desc": "집안 가득 뿌리는 치명적인 청량함.", "price": 300000000, "color": "#0088ff", "tier": 5},
    25: {"name": "25단계 : 자이온맘의 무한한 은혜", "desc": "은하수 아이들에게 평화를 내리는 자애로움.", "price": 400000000, "color": "#00ffaa", "tier": 5},
    26: {"name": "26단계 : 자이온맘의 궁극 필살기", "desc": "우주 전체가 지온 향으로 뒤덮인다.", "price": 1800000000, "color": "#ccff00", "tier": 6},
    27: {"name": "27단계 : 자이온맘의 창조와 구원", "desc": "빅뱅 당시 터뜨린 절대 구원의 향기.", "price": 2500000000, "color": "#fffb00", "tier": 6},
    28: {"name": "28단계 : 자이온맘의 권능 지온냄새", "desc": "창조주도 고개를 숙이고 냄새를 맡는다.", "price": 5500000000, "color": "#ffffff", "tier": 6},
    29: {"name": "29단계 : 만물의 어머니 ★자이온맘★", "desc": "우주 만물이 품으로 돌아가는 최종 오라.", "price": 10500000000, "color": "#ff00aa", "tier": 6},
    30: {"name": "30단계 : ★태초의 자이온맘★ 절대신성", "desc": "우주를 지온으로 통일한 자이온맘의 완성.", "price": float('inf'), "color": "#00ffff", "tier": 6},
}

PROB_TABLE = {
    0: (100.0, 0.0, 0.0, 0.0), 1: (100.0, 0.0, 0.0, 0.0), 2: (100.0, 0.0, 0.0, 0.0),
    3: (95.0, 5.0, 0.0, 0.0), 4: (95.0, 5.0, 0.0, 0.0), 5: (90.0, 10.0, 0.0, 0.0),
    6: (90.0, 8.0, 2.0, 0.0), 7: (90.0, 5.0, 5.0, 0.0), 8: (85.0, 10.0, 5.0, 0.0),
    9: (80.0, 15.0, 5.0, 0.0), 10: (80.0, 15.0, 5.0, 0.0), 11: (75.0, 15.0, 5.0, 5.0),
    12: (70.0, 15.0, 5.0, 10.0), 13: (70.0, 15.0, 7.0, 8.0), 14: (65.0, 15.0, 10.0, 10.0),
    15: (60.0, 20.0, 10.0, 10.0), 16: (60.0, 18.0, 12.0, 10.0), 17: (55.0, 20.0, 15.0, 10.0),
    18: (50.0, 20.0, 17.0, 13.0), 19: (50.0, 20.0, 20.0, 10.0), 20: (45.0, 22.0, 23.0, 10.0),
    21: (40.0, 25.0, 25.0, 10.0), 22: (40.0, 23.0, 27.0, 10.0), 23: (40.0, 20.0, 30.0, 10.0),
    24: (40.0, 18.0, 32.0, 10.0), 25: (35.0, 25.0, 30.0, 10.0), 26: (50.0, 20.0, 25.0, 5.0),
    27: (40.0, 25.0, 30.0, 5.0), 28: (30.0, 30.0, 35.0, 5.0), 29: (20.0, 35.0, 40.0, 5.0),
}

CRITICAL_RATE = 0.05
PITY_MAX = 5

PETS_DB = {
    "cosmic_cat": {"name": "코스믹 고양이", "cps": 100, "cost": 50000, "desc": "초당 100원의 우주 에테르를 정제합니다."},
    "zion_dog": {"name": "지온 수호견", "cps": 850, "cost": 450000, "desc": "초당 850원의 에테르를 뿜어냅니다."},
    "mother_drone": {"name": "자이온맘 드론", "cps": 5000, "cost": 3000000, "desc": "초당 5,000원의 고순도 냄새를 채굴합니다."},
    "singularity_core": {"name": "특이점 코어", "cps": 35000, "cost": 25000000, "desc": "초당 35,000원의 강력한 에너지를 생산합니다."}
}

# -----------------------------------------------------------------------------
# 5. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state: st.session_state.level = 0
if "max_level" not in st.session_state: st.session_state.max_level = 0
if "money" not in st.session_state: st.session_state.money = 1000000
if "status" not in st.session_state: st.session_state.status = "READY"
if "shield" not in st.session_state: st.session_state.shield = 0
if "tears" not in st.session_state: st.session_state.tears = 0
if "pity_count" not in st.session_state: st.session_state.pity_count = 0
if "total_enhanced" not in st.session_state: st.session_state.total_enhanced = 0
if "total_sold" not in st.session_state: st.session_state.total_sold = 0
if "auto_clicker_unlocked" not in st.session_state: st.session_state.auto_clicker_unlocked = False
if "pets" not in st.session_state: st.session_state.pets = {k: 0 for k in PETS_DB}
if "achievements" not in st.session_state: st.session_state.achievements = {k: False for k in ACHIEVEMENTS_DB}
if "quests_claimed" not in st.session_state: st.session_state.quests_claimed = []
if "buff_active" not in st.session_state: st.session_state.buff_active = False

# -----------------------------------------------------------------------------
# 6. 업적 및 보상 체크 함수
# -----------------------------------------------------------------------------
def check_achievements_and_quests():
    lvl = st.session_state.level
    max_lvl = st.session_state.max_level
    money = st.session_state.money
    
    # 업적 체크
    achs = st.session_state.achievements
    if not achs["first_step"] and max_lvl >= 1:
        achs["first_step"] = True
        st.session_state.money += ACHIEVEMENTS_DB["first_step"]["reward"]
        st.toast("🏆 업적 달성: 태초의 첫걸음!", icon="🎉")
    if not achs["tier_2"] and max_lvl >= 6:
        achs["tier_2"] = True
        st.session_state.money += ACHIEVEMENTS_DB["tier_2"]["reward"]
        st.toast("🏆 업적 달성: 대기권을 뚫고!", icon="🎉")
    if not achs["tier_3"] and max_lvl >= 11:
        achs["tier_3"] = True
        st.session_state.money += ACHIEVEMENTS_DB["tier_3"]["reward"]
        st.toast("🏆 업적 달성: 행성 궤도 진입!", icon="🎉")
    if not achs["tier_4"] and max_lvl >= 16:
        achs["tier_4"] = True
        st.session_state.money += ACHIEVEMENTS_DB["tier_4"]["reward"]
        st.toast("🏆 업적 달성: 성간 항해자!", icon="🎉")
    if not achs["tier_5"] and max_lvl >= 21:
        achs["tier_5"] = True
        st.session_state.money += ACHIEVEMENTS_DB["tier_5"]["reward"]
        st.toast("🏆 업적 달성: 자이온맘의 친자인증!", icon="🎉")
    if not achs["tier_6"] and max_lvl >= 26:
        achs["tier_6"] = True
        st.session_state.money += ACHIEVEMENTS_DB["tier_6"]["reward"]
        st.toast("🏆 업적 달성: 우주의 지배자!", icon="🎉")
    if not achs["max_god"] and max_lvl >= 30:
        achs["max_god"] = True
        st.session_state.money += ACHIEVEMENTS_DB["max_god"]["reward"]
        st.toast("🏆 업적 달성: 태초의 절대신!", icon="🎉")
    if not achs["bankrupt"] and money == 0 and st.session_state.total_enhanced > 0:
        achs["bankrupt"] = True
        st.session_state.money += ACHIEVEMENTS_DB["bankrupt"]["reward"]
        st.toast("🏆 업적 달성: 우적적 빈곤!", icon="💸")

# -----------------------------------------------------------------------------
# 7. 핵심 게임플레이 함수 (강화, 판매, 펫 구매 등)
# -----------------------------------------------------------------------------
def run_enhance():
    curr = st.session_state.level
    if curr >= 30:
        return

    cost = get_enhance_cost(curr)
    if st.session_state.money < cost:
        st.session_state.status = "NOT_ENOUGH_MONEY"
        return

    st.session_state.money -= cost
    st.session_state.total_enhanced += 1

    if st.session_state.pity_count >= PITY_MAX - 1:
        st.session_state.level += 1
        st.session_state.status = "PITY_SUCCESS"
        st.session_state.pity_count = 0
        if st.session_state.level > st.session_state.max_level:
            st.session_state.max_level = st.session_state.level
        check_achievements_and_quests()
        return

    sp, down_p, dp, hold_p = PROB_TABLE[curr]
    
    # 버프 적용 시 성공 확률 보정
    if st.session_state.buff_active:
        sp += 10.0
        
    r = random.uniform(0, 100)

    success_limit = sp
    down_limit = success_limit + down_p
    destroy_limit = down_limit + dp

    if r < success_limit:
        st.session_state.pity_count = 0
        crit_chance = CRITICAL_RATE + (0.05 if st.session_state.buff_active else 0.0)
        if random.random() < crit_chance and curr + 2 <= 30:
            st.session_state.level += 2
            st.session_state.status = "CRITICAL"
        else:
            st.session_state.level += 1
            st.session_state.status = "SUCCESS"
    elif r < down_limit:
        st.session_state.pity_count += 1
        if curr > 0:
            st.session_state.level -= 1
        st.session_state.status = "FAILED"
        st.session_state.tears = min(120, st.session_state.tears + 1)
    elif r < destroy_limit:
        if st.session_state.shield > 0:
            st.session_state.shield -= 1
            st.session_state.pity_count += 1
            st.session_state.status = "SHIELD_SAVED"
            st.session_state.tears = min(120, st.session_state.tears + 1)
        else:
            st.session_state.pity_count += 1
            st.session_state.level = 0
            st.session_state.status = "DESTROYED"
            st.session_state.tears = min(120, st.session_state.tears + 2)
    else:
        st.session_state.pity_count += 1
        st.session_state.status = "HOLD"
        st.session_state.tears = min(120, st.session_state.tears + 1)

    if st.session_state.level > st.session_state.max_level:
        st.session_state.max_level = st.session_state.level
    
    check_achievements_and_quests()

def dev_force_success():
    curr = st.session_state.level
    if curr < 30:
        st.session_state.level += 1
        st.session_state.status = "SUCCESS"
        if st.session_state.level > st.session_state.max_level:
            st.session_state.max_level = st.session_state.level
        check_achievements_and_quests()

def sell():
    curr = st.session_state.level
    if curr == 0:
        return
    price_val = SMELL_DB[curr]["price"]
    if price_val == float('inf'):
        st.session_state.money = float('inf')
    else:
        st.session_state.money += price_val
    st.session_state.total_sold += 1
    st.session_state.level = 0
    st.session_state.status = "READY"
    check_achievements_and_quests()

# -----------------------------------------------------------------------------
# 8. 테마 및 CSS 커스텀 스타일 정의
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background: 
            radial-gradient(circle at 20% 30%, rgba(76, 29, 149, 0.4) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(30, 58, 138, 0.5) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(15, 23, 42, 1) 0%, #020617 100%);
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 96% !important;
    }
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 9px 16px !important;
        transition: all 0.2s ease !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        background: rgba(15, 23, 42, 0.85) !important;
        color: #f8fafc !important;
        box-shadow: 0 4px 15px rgba(2, 6, 23, 0.6);
    }
    div.stButton > button:hover {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #0f172a !important;
        border: 1px solid #ffffff !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 255, 255, 0.25);
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        backdrop-filter: blur(5px);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 9. 메인 레이아웃 구성 (탭 시스템 및 확장 패널)
# -----------------------------------------------------------------------------
main_tab1, main_tab2, main_tab3, main_tab4 = st.tabs(["🌌 코스믹 강화소", "🐾 우주 펫 연구소", "📜 퀘스트 & 업적", "⚙️ 시스템 설정"])

with main_tab1:
    left_col, right_col = st.columns([2.4, 7.6], gap="medium")

    with left_col:
        st.markdown("<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>💳 자원 및 재화 현황</h4>", unsafe_allow_html=True)
        
        # 유저 칭호 표시
        current_title = "무소유의 방랑자"
        for lvl_req, t_name in sorted(TITLE_DB.items()):
            if st.session_state.max_level >= lvl_req:
                current_title = t_name
        st.markdown(f"<div style='background:rgba(15,23,42,0.9); border:1px solid #fde68a; padding:8px; border-radius:6px; text-align:center; margin-bottom:10px;'><span style='font-size:11px; color:#94a3b8;'>현재 칭호</span><br><b style='color:#fde68a; font-size:14px;'>{current_title}</b></div>", unsafe_allow_html=True)

        s_col1, s_col2 = st.columns(2)
        with s_col1:
            st.markdown(f"<div class='metric-card'><div style='font-size:11px; color:#fde68a;'>보유 금액</div><div style='font-size:13px; font-weight:800; color:#ffffff;'>{format_gold(st.session_state.money)}</div></div>", unsafe_allow_html=True)
            st.write("")
            st.markdown(f"<div class='metric-card'><div style='font-size:11px; color:#fde68a;'>눈물</div><div style='font-size:13px; font-weight:800; color:#ffffff;'>{st.session_state.tears}/120</div></div>", unsafe_allow_html=True)
        with s_col2:
            st.markdown(f"<div class='metric-card'><div style='font-size:11px; color:#fde68a;'>방지권</div><div style='font-size:13px; font-weight:800; color:#ffffff;'>{st.session_state.shield}/3</div></div>", unsafe_allow_html=True)
            st.write("")
            pity_left = PITY_MAX - st.session_state.pity_count
            st.markdown(f"<div class='metric-card'><div style='font-size:11px; color:#fde68a;'>가호 천장</div><div style='font-size:13px; font-weight:800; color:#ffffff;'>{pity_left}회 남음</div></div>", unsafe_allow_html=True)

        st.markdown("<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

        # 상점 탭 (방지권 및 눈물)
        tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권 상점", "💧 눈물 정제소"])
        with tab_shop1:
            current_shield_cost = get_shield_cost(st.session_state.level)
            st.markdown(f"<div style='font-size:12px; color:#cbd5e1; margin-bottom:6px;'>18단계 이상 구매 가능 (최대 3개)<br>가격: <b style='color:#fde68a;'>{format_gold(current_shield_cost)}</b></div>", unsafe_allow_html=True)
            if st.button("방지권 즉시 구매", use_container_width=True, disabled=(st.session_state.level < 18 or st.session_state.shield >= 3)):
                if st.session_state.money >= current_shield_cost:
                    st.session_state.money -= current_shield_cost
                    st.session_state.shield += 1
                    st.success("방지권 구매 완료!")
                    st.rerun()
                else:
                    st.error("잔액이 부족합니다.")

        with tab_shop2:
            st.markdown(f"<div style='font-size:12px; color:#cbd5e1; margin-bottom:6px;'>눈물 40개 소모 (50% 확률 1~3단계 상승)</div>", unsafe_allow_html=True)
            if st.button("눈물의 기적 가동", use_container_width=True, disabled=(st.session_state.level >= 28 or st.session_state.tears < 40)):
                st.session_state.tears -= 40
                if random.random() < 0.5:
                    add_lvl = random.choice([1, 2, 3])
                    st.session_state.level = min(30, st.session_state.level + add_lvl)
                    st.session_state.status = "SUCCESS"
                    st.success(f"눈물의 기적 성공! +{add_lvl}단계!")
                else:
                    st.session_state.status = "FAILED"
                    st.warning("기적이 실패했습니다...")
                st.rerun()

        st.markdown("<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

        st.markdown("<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🌌 자이온 강화 제어</h4>", unsafe_allow_html=True)
        if st.button("🔥 냄새 강화 실행", use_container_width=True, disabled=(st.session_state.level >= 30)):
            run_enhance()
            st.rerun()

        st.write("")
        if st.button("💰 현재 냄새 판매", use_container_width=True, disabled=(st.session_state.level == 0)):
            sell()
            st.rerun()

    with right_col:
        current_level = st.session_state.level
        curr_data = SMELL_DB[current_level]
        card_color = curr_data["color"]
        card_title = curr_data["name"]
        card_desc = curr_data["desc"]
        card_price = format_gold(curr_data["price"])
        current_cost = format_gold(get_enhance_cost(current_level))
        tier = curr_data["tier"]
        status = st.session_state.status

        three_js_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ margin: 0; overflow: hidden; background: transparent; font-family: -apple-system, sans-serif; }}
                #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}
                .cinematic-ui {{
                    position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%);
                    width: 100%; text-align: center; z-index: 100; pointer-events: none; opacity: 0; transition: opacity 0.4s ease-in-out;
                }}
                .cinematic-ui.visible {{ opacity: 1; }}
                .title-tier-1 {{ font-size: 26px; font-weight: 800; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
                .title-tier-2 {{ font-size: 30px; font-weight: 800; color: #f59e0b; text-shadow: 0 0 22px #f59e0b; }}
                .title-tier-3 {{ font-size: 34px; font-weight: 800; color: #ef4444; text-shadow: 0 0 25px #ef4444; }}
                .title-tier-4 {{ font-size: 38px; font-weight: 800; color: #c084fc; text-shadow: 0 0 28px #c084fc; }}
                .title-tier-5 {{ font-size: 42px; font-weight: 800; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
                .title-tier-6 {{ font-size: 46px; font-weight: 800; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; }}
                @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}
                .status-header {{ font-size: 15px; font-weight: 800; margin-bottom: 2px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
                .desc-text {{ font-size: 12px; color: #cbd5e1; margin-top: 2px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
                .price-text {{ font-size: 14px; font-weight: 800; color: #fbbf24; margin-top: 2px; text-shadow: 0 0 15px rgba(0,0,0,0.95); }}
                .cost-text {{ font-size: 11px; font-weight: 700; color: #f87171; margin-top: 2px; text-shadow: 0 0 12px rgba(0,0,0,0.95); }}
            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
        </head>
        <body>
            <div id="container"></div>
            <div id="cinematicUi" class="cinematic-ui">
                <div id="statusText" class="status-header">READY</div>
                <div id="mainTitle" class="title-tier-{tier}">{card_title}</div>
                <div id="descText" class="desc-text">"{card_desc}"</div>
                <div id="priceText" class="price-text">예상 가치: {card_price}</div>
                <div id="costText" class="cost-text">필요 강화 비용: {current_cost}</div>
            </div>
            <script>
                const uiElement = document.getElementById('cinematicUi');
                const status = "{status}";
                const statusText = document.getElementById('statusText');
                const tierColor = "{card_color}";
                let statusColor = "#38bdf8";
                let particleSize = 0.3;
                let particleSpeed = 1.0;

                if (status === "CRITICAL") {{
                    statusText.innerText = "⚡ COSMIC CRITICAL HIT!! (+2단계 이상 대성공) ⚡";
                    statusColor = "#ffffff"; particleSize = 0.55; particleSpeed = 2.5;
                }} else if (status === "PITY_SUCCESS") {{
                    statusText.innerText = "✨ 자이온맘의 가호 발동! (천장 100% 성공) ✨";
                    statusColor = "#fde68a"; particleSize = 0.45; particleSpeed = 2.0;
                }} else if (status === "SUCCESS") {{
                    statusText.innerText = "✨ COSMIC SUCCESS (강화 성공) ✨";
                    statusColor = tierColor; particleSize = 0.35; particleSpeed = 1.5;
                }} else if (status === "SHIELD_SAVED") {{
                    statusText.innerText = "🛡️ SHIELD PROTECTED! (우주 방어 발동) 🛡️";
                    statusColor = "#60a5fa";
                }} else if (status === "DESTROYED") {{
                    statusText.innerText = "💥 BLACKHOLE DESTROYED (코어 붕괴됨) 💥";
                    statusColor = "#ef4444";
                }} else if (status === "FAILED") {{
                    statusText.innerText = "🔻 FAILED (에너지 하락) 🔻";
                    statusColor = "#64748b"; particleSpeed = 0.5;
                }} else if (status === "HOLD") {{
                    statusText.innerText = "🔒 HOLD (에너지 동결) 🔒";
                    statusColor = "#94a3b8"; particleSpeed = 0.7;
                }} else {{
                    statusText.innerText = "READY - 우주 에너지가 집중됩니다";
                }}
                statusText.style.color = statusColor;

                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 0.1, 1000);
                camera.position.set(0, 0.6, 10.0);

                const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                renderer.setSize(window.innerWidth, window.innerHeight);
                renderer.setPixelRatio(window.devicePixelRatio);
                document.getElementById('container').appendChild(renderer.domElement);

                scene.add(new THREE.AmbientLight(0xffffff, 0.8));
                const mainLight = new THREE.DirectionalLight(0xffffff, 2.5);
                mainLight.position.set(5, 8, 5);
                scene.add(mainLight);

                const particleCount = 600;
                const particleGeo = new THREE.BufferGeometry();
                const particlePositions = new Float32Array(particleCount * 3);
                const particleVelocities = [];

                for(let i=0; i<particleCount; i++) {{
                    particlePositions[i*3] = (Math.random() - 0.5) * 7.0;
                    particlePositions[i*3 + 1] = -5.0 + Math.random() * 3.0;
                    particlePositions[i*3 + 2] = (Math.random() - 0.5) * 7.0;
                    particleVelocities.push({{
                        x: (Math.random() - 0.5) * 0.02 * particleSpeed,
                        y: (0.015 + Math.random() * 0.03) * particleSpeed,
                        z: (Math.random() - 0.5) * 0.02 * particleSpeed,
                    }});
                }}
                particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
                const particleMat = new THREE.PointsMaterial({{
                    color: new THREE.Color(statusColor), size: particleSize, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending
                }});
                scene.add(new THREE.Points(particleGeo, particleMat));

                const objectGroup = new THREE.Group();
                objectGroup.position.y = -0.7;
                const baseGeo = new THREE.IcosahedronGeometry(2.3, 0);
                const outerMat = new THREE.MeshPhysicalMaterial({{
                    color: tierColor, emissive: tierColor, emissiveIntensity: 0.4, metalness: 0.9, roughness: 0.2, transmission: 0.5, transparent: true, opacity: 0.9
                }});
                objectGroup.add(new THREE.Mesh(baseGeo, outerMat));
                scene.add(objectGroup);

                uiElement.classList.add('visible');
                const clock = new THREE.Clock();

                function animate() {{
                    requestAnimationFrame(animate);
                    const time = clock.getElapsedTime();
                    objectGroup.rotation.x = time * 0.5;
                    objectGroup.rotation.y = time * 0.7;

                    const positions = particleGeo.attributes.position.array;
                    for(let i=0; i<particleCount; i++) {{
                        positions[i*3 + 1] += particleVelocities[i].y;
                        if(positions[i*3 + 1] > 3.0) {{
                            positions[i*3 + 1] = -5.0;
                        }}
                    }}
                    particleGeo.attributes.position.needsUpdate = true;
                    renderer.render(scene, camera);
                }}
                animate();
            </script>
        </body>
        </html>
        """
        components.html(three_js_code, height=540, scrolling=False)

with main_tab2:
    st.markdown("### 🐾 우주 펫 연구소 (Idle 자동 에테르 채굴)")
    st.markdown("우주 펫을 고용하여 초당 자동으로 일정량의 금액(에테르)을 수급하세요.")
    
    pet_cols = st.columns(len(PETS_DB))
    for idx, (pet_id, pet_info) in enumerate(PETS_DB.items()):
        with pet_cols[idx]:
            st.markdown(f"""
                <div style='background:rgba(30,41,59,0.8); border:1px solid rgba(255,255,255,0.15); padding:15px; border-radius:10px; text-align:center;'>
                    <h4 style='margin:0; color:#fde68a;'>{pet_info['name']}</h4>
                    <p style='font-size:12px; color:#cbd5e1; margin:8px 0;'>{pet_info['desc']}</p>
                    <p style='font-size:12px; color:#38bdf8; margin:0;'>초당 생산: +{pet_info['cps']:,}원</p>
                    <p style='font-size:13px; font-weight:bold; color:#fbbf24; margin:5px 0;'>보유 수: {st.session_state.pets[pet_id]}마리</p>
                </div>
            """, unsafe_allow_html=True)
            
            buy_cost = int(pet_info['cost'] * (1.15 ** st.session_state.pets[pet_id]))
            if st.button(f"구매 ({format_gold(buy_cost)})", key=f"buy_pet_{pet_id}", use_container_width=True):
                if st.session_state.money >= buy_cost:
                    st.session_state.money -= buy_cost
                    st.session_state.pets[pet_id] += 1
                    st.success(f"{pet_info['name']} 고용 성공!")
                    st.rerun()
                else:
                    st.error("보유 금액이 부족합니다.")

with main_tab3:
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        st.markdown("### 📜 우주 퀘스트")
        for q in QUESTS_DB:
            is_completed = st.session_state.max_level >= q["target_level"]
            is_claimed = q["id"] in st.session_state.quests_claimed
            
            status_str = "✅ 완료 가능" if (is_completed and not is_claimed) else ("🎁 수령 완료" if is_claimed else "진행 중...")
            st.markdown(f"""
                <div style='background:rgba(30,41,59,0.6); border:1px solid rgba(255,255,255,0.1); padding:10px; border-radius:8px; margin-bottom:8px;'>
                    <b>{q['title']}</b> (목표: {q['target_level']}단계)<br>
                    <span style='font-size:12px; color:#cbd5e1;'>{q['desc']} | 보상: {format_gold(q['reward'])}</span><br>
                    <span style='font-size:12px; color:#fde68a;'>상태: {status_str}</span>
                </div>
            """, unsafe_allow_html=True)
            
            if is_completed and not is_claimed:
                if st.button(f"보상 수령 ({q['title']})", key=f"claim_q_{q['id']}"):
                    st.session_state.money += q["reward"]
                    st.session_state.quests_claimed.append(q["id"])
                    st.success("보상이 지급되었습니다!")
                    st.rerun()

    with col_q2:
        st.markdown("### 🏆 업적 시스템")
        for ach_id, ach_info in ACHIEVEMENTS_DB.items():
            achieved = st.session_state.achievements[ach_id]
            color_style = "#38bdf8" if achieved else "#64748b"
            st.markdown(f"""
                <div style='background:rgba(30,41,59,0.6); border:1px solid {color_style}; padding:10px; border-radius:8px; margin-bottom:8px;'>
                    <b style='color:{color_style};'>{ach_info['name']}</b> { "✅" if achieved else "🔒" }<br>
                    <span style='font-size:12px; color:#cbd5e1;'>{ach_info['desc']}</span><br>
                    <span style='font-size:11px; color:#fde68a;'>보상: {format_gold(ach_info['reward'])}</span>
                </div>
            """, unsafe_allow_html=True)

with main_tab4:
    st.markdown("### ⚙️ 시스템 설정 및 관리자 패널")
    dev_mode = st.toggle("💻 디버그 개발자 모드 활성화", value=False)
    
    if dev_mode:
        st.warning("개발자 모드가 활성화되었습니다. 강제 성공 및 자원 조작이 가능합니다.")
        col_d1, col_d2, col_d3 = st.columns(3)
        with col_d1:
            if st.button("✨ 무조건 성공 (DEV)", use_container_width=True):
                dev_force_success()
                st.rerun()
        with col_d2:
            if st.button("💰 1,000만 원 충전", use_container_width=True):
                st.session_state.money += 10000000
                st.rerun()
        with col_d3:
            if st.button("🔄 게임 데이터 초기화", use_container_width=True):
                st.session_state.clear()
                st.rerun()
    
    st.markdown("---")
    st.markdown("#### 🌟 게임 가이드")
    st.markdown("""
    * **강화 시스템**: 일정 확률에 따라 성공, 하락, 파괴, 동결이 결정됩니다.
    * **천장 시스템**: 실패가 누적되면(5회째) 자이온맘의 가호가 발동하여 100% 성공합니다.
    * **우주 펫**: 펫을 고용하면 게임을 켜놓는 동안 자동으로 자원이 채굴됩니다.
    """)
