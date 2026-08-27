import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - FANTASY CITY EDITION", page_icon="🏰", layout="wide"
)

# -----------------------------------------------------------------------------
# 2. 초반부는 싸고, 15단계 이후부터 가파르게 상승하는 강화 비용 함수
# -----------------------------------------------------------------------------


def format_gold(amount):
  if amount == 0:
    return "0원"

  # 30단계 '무한' 처리용 예외 핸들링
  if amount == float("inf"):
    return "무한"

  units = ["", "만", "억", "조", "경", "해"]
  result = []

  unit_idx = 0
  while amount > 0 and unit_idx < len(units):
    remainder = amount % 10000
    if remainder > 0:
      result.insert(0, f"{remainder:,}{units[unit_idx]}")
    amount //= 10000
    unit_idx += 1

  return "".join(result) + "원"


def get_enhance_cost(level):
  if level == 0:
    return 100
  if level < 5:
    return int(100 * (1.5**level))
  elif level < 15:
    base_mid = 100 * (1.5**4)
    return int(base_mid * (1.18 ** (level - 4)))
  else:
    base_high = (100 * (1.5**4)) * (1.18**11)
    return int(base_high * (1.50 ** (level - 15)))


# -----------------------------------------------------------------------------
# 3. 게임 데이터베이스 및 강화 확률표 (성공, 실패, 파괴)[cite: 1]
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {
        "name": "0단계 : 무취의 공간",
        "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.",
        "price": 0,
        "color": "#4a5568",
        "tier": 1,
    },
    1: {
        "name": "1단계 : 스쳐가는 지온냄새",
        "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.",
        "price": 150,
        "color": "#718096",
        "tier": 1,
    },
    2: {
        "name": "2단계 : 은은한 자이온냄새",
        "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.",
        "price": 400,
        "color": "#38a169",
        "tier": 1,
    },
    3: {
        "name": "3단계 : 습한 지온냄새",
        "desc": "비 온 뒤 짙은 상록수 숲속에서 감오는 냄새.",
        "price": 600,
        "color": "#276749",
        "tier": 1,
    },
    4: {
        "name": "4단계 : 진득한 자이온냄새",
        "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.",
        "price": 800,
        "color": "#319795",
        "tier": 1,
    },
    5: {
        "name": "5단계 : 자극적인 지온냄새",
        "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.",
        "price": 3000,
        "color": "#2c7a7b",
        "tier": 1,
    },
    6: {
        "name": "6단계 : 풍부한 자이온냄새",
        "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.",
        "price": 3500,
        "color": "#3182ce",
        "tier": 2,
    },
    7: {
        "name": "7단계 : 압도적인 지온냄새",
        "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.",
        "price": 6100,
        "color": "#2b6cb0",
        "tier": 2,
    },
    8: {
        "name": "8단계 : 폭발하는 지온냄새",
        "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.",
        "price": 10000,
        "color": "#805ad5",
        "tier": 2,
    },
    9: {
        "name": "9단계 : 시공을 뒤흔드는 지온냄새",
        "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.",
        "price": 20000,
        "color": "#6b46c1",
        "tier": 2,
    },
    10: {
        "name": "10단계 : 치명적인 자이온냄새",
        "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.",
        "price": 35100,
        "color": "#d69e2e",
        "tier": 2,
    },
    11: {
        "name": "11단계 : 환각을 부르는 지온냄새",
        "desc": "태초의 지구 흙밭을 거니는 환각을 본다.",
        "price": 160000,
        "color": "#b7791f",
        "tier": 3,
    },
    12: {
        "name": "12단계 : 공간지배 자이온냄새",
        "desc": "방 안의 모든 산소를 지온 분자로 채운다.",
        "price": 350000,
        "color": "#dd6b20",
        "tier": 3,
    },
    13: {
        "name": "13단계 : 전설의 지온냄새",
        "desc": "역사서에서 언급되던 전설 속의 지구 향기.",
        "price": 1000000,
        "color": "#c05621",
        "tier": 3,
    },
    14: {
        "name": "14단계 : 신성한 자이온냄새",
        "desc": "마음이 경건해지며 흙과 하나가 되는 기분.",
        "price": 3000000,
        "color": "#e53e3e",
        "tier": 3,
    },
    15: {
        "name": "15단계 : 신화급 지온냄새",
        "desc": "신들이 세계를 창조할 때 맡았다는 향.",
        "price": 7500000,
        "color": "#9b2c2c",
        "tier": 3,
    },
    16: {
        "name": "16단계 : 우주관통 자이온냄새",
        "desc": "성층권을 뚫고 우주선까지 퍼져나간다.",
        "price": 14200000,
        "color": "#00f0ff",
        "tier": 4,
    },
    17: {
        "name": "17단계 : 차원균열 자이온냄새",
        "desc": "평행세계의 흙냄새까지 끌어당긴다.",
        "price": 20000000,
        "color": "#ff00ea",
        "tier": 4,
    },
    18: {
        "name": "18단계 : Absolute 자이온냄새",
        "desc": "만물의 요소를 지온 입자로 바꿔버린다.",
        "price": 30000000,
        "color": "#ffe600",
        "tier": 4,
    },
    19: {
        "name": "19단계 : 초월적 지온냄새",
        "desc": "인간의 감각으로는 수용 불가능한 향기.",
        "price": 47500000,
        "color": "#ff0055",
        "tier": 4,
    },
    20: {
        "name": "20단계 : 자이온맘의 포근한 집밥 냄새",
        "desc": "자이온맘의 강림! 따스하고 구수한 냄새.",
        "price": 68300000,
        "color": "#ffaa00",
        "tier": 4,
    },
    21: {
        "name": "21단계 : 자이온맘의 엄격한 등짝 스매싱",
        "desc": "매콤하면서 사랑이 깃든 자이온맘의 향.",
        "price": 101000000,
        "color": "#ff4500",
        "tier": 5,
    },
    22: {
        "name": "22단계 : 자이온맘의 전설의 흙된장국",
        "desc": "극상의 흙내음과 깊은 손맛.",
        "price": 160000000,
        "color": "#ff007f",
        "tier": 5,
    },
    23: {
        "name": "23단계 : 자이온맘의 100년 숙성 원액",
        "desc": "몰래 아껴둔 냄새의 결정체.",
        "price": 230000000,
        "color": "#7b00ff",
        "tier": 5,
    },
    24: {
        "name": "24단계 : 자이온맘의 지온스프레이",
        "desc": "집안 가득 뿌리는 치명적인 청량함.",
        "price": 300000000,
        "color": "#0088ff",
        "tier": 5,
    },
    25: {
        "name": "25단계 : 자이온맘의 무한한 은혜",
        "desc": "은하수 아이들에게 평화를 내리는 자애로움.",
        "price": 400000000,
        "color": "#00ffaa",
        "tier": 5,
    },
    26: {
        "name": "26단계 : 자이온맘의 궁극 필살기",
        "desc": "우주 전체가 지온 향으로 뒤덮인다.",
        "price": 1800000000,
        "color": "#ccff00",
        "tier": 6,
    },
    27: {
        "name": "27단계 : 자이온맘의 창조와 구원",
        "desc": "빅뱅 당시 터뜨린 절대 구원의 향기.",
        "price": 2500000000,
        "color": "#fffb00",
        "tier": 6,
    },
    28: {
        "name": "28단계 : 자이온맘의 권능 지온냄새",
        "desc": "창조주도 고개를 숙이고 냄새를 맡는다.",
        "price": 5500000000,
        "color": "#ffffff",
        "tier": 6,
    },
    29: {
        "name": "29단계 : 만물의 어머니 ★자이온맘★",
        "desc": "우주 만물이 품으로 돌아가는 최종 오라.",
        "price": 10500000000,
        "color": "#ff00aa",
        "tier": 6,
    },
    30: {
        "name": "30단계 : ★태초의 자이온맘★ 절대신성",
        "desc": "우주를 지온으로 통일한 자이온맘의 완성.",
        "price": float("inf"),
        "color": "#00ffff",
        "tier": 6,
    },
}

PROB_TABLE = {
    0: (100.0, 0.0, 0.0),
    1: (100.0, 0.0, 0.0),
    2: (100.0, 0.0, 0.0),
    3: (95.0, 5.0, 0.0),
    4: (95.0, 5.0, 0.0),
    5: (90.0, 10.0, 0.0),
    6: (90.0, 8.0, 2.0),
    7: (90.0, 5.0, 5.0),
    8: (85.0, 10.0, 5.0),
    9: (80.0, 15.0, 5.0),
    10: (80.0, 15.0, 5.0),
    11: (75.0, 20.0, 5.0),
    12: (70.0, 25.0, 5.0),
    13: (70.0, 23.0, 7.0),
    14: (65.0, 25.0, 10.0),
    15: (60.0, 30.0, 10.0),
    16: (60.0, 28.0, 12.0),
    17: (55.0, 30.0, 15.0),
    18: (50.0, 33.0, 17.0),
    19: (50.0, 30.0, 20.0),
    20: (45.0, 32.0, 23.0),
    21: (40.0, 35.0, 25.0),
    22: (40.0, 33.0, 27.0),
    23: (40.0, 30.0, 30.0),
    24: (40.0, 28.0, 32.0),
    25: (35.0, 30.0, 35.0),
    26: (50.0, 25.0, 25.0),
    27: (40.0, 30.0, 30.0),
    28: (30.0, 35.0, 35.0),
    29: (20.0, 40.0, 40.0),
}

CRITICAL_RATE = 0.05

# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
  st.session_state.level = 0
if "money" not in st.session_state:
  st.session_state.money = 5000
if "status" not in st.session_state:
  st.session_state.status = "READY"
if "shield" not in st.session_state:
  st.session_state.shield = 0
if "tears" not in st.session_state:
  st.session_state.tears = 0
if "dev_mode" not in st.session_state:
  st.session_state.dev_mode = False

# -----------------------------------------------------------------------------
# 5. 강화 로직
# -----------------------------------------------------------------------------


def enhance():
  curr = st.session_state.level
  if curr >= 30:
    return

  cost = get_enhance_cost(curr)
  if st.session_state.money < cost:
    st.session_state.status = "NOT_ENOUGH_MONEY"
    return

  st.session_state.money -= cost

  if st.session_state.dev_mode:
    st.session_state.level += 1
    st.session_state.status = "SUCCESS"
    return

  sp, fp, dp = PROB_TABLE[curr]
  r = random.uniform(0, 100)

  if r < sp:
    if random.random() < CRITICAL_RATE and curr + 2 <= 30:
      st.session_state.level += 2
      st.session_state.status = "CRITICAL"
    else:
      st.session_state.level += 1
      st.session_state.status = "SUCCESS"
  elif r < (sp + dp):
    if st.session_state.shield > 0:
      st.session_state.shield -= 1
      st.session_state.status = "SHIELD_SAVED"
      st.session_state.tears += 1
    else:
      st.session_state.level = 0
      st.session_state.status = "DESTROYED"
      st.session_state.tears += 2
  else:
    if curr > 0:
      st.session_state.level -= 1
    st.session_state.status = "FAILED"
    st.session_state.tears += 1


def sell():
  curr = st.session_state.level
  if curr == 0:
    return
  price_val = SMELL_DB[curr]["price"]
  if price_val == float("inf"):
    st.session_state.money = float("inf")
  else:
    st.session_state.money += price_val
  st.session_state.level = 0
  st.session_state.status = "READY"


# -----------------------------------------------------------------------------
# 6. 테마 CSS
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }
    .glass-panel {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
    }
    .stat-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(245, 158, 11, 0.4);
        padding: 12px 10px;
        border-radius: 10px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .stat-card:hover {
        border-color: rgba(245, 158, 11, 0.9);
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.5);
    }
    .stat-title {
        font-size: 14px;
        font-weight: 600;
        color: #fde68a;
        margin-bottom: 4px;
        letter-spacing: 0.5px;
    }
    .stat-value {
        font-size: 20px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
    }
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 10px 18px !important;
        transition: all 0.2s ease !important;
        border: 1px solid rgba(217, 119, 6, 0.4) !important;
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.6), rgba(217, 119, 6, 0.6)) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(217, 119, 6, 0.6);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. 메인 레이아웃
# -----------------------------------------------------------------------------
left_col, right_col = st.columns([2.2, 7.8], gap="medium")

with left_col:
  st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='margin:0 0 12px 0; font-size: 20px; color:#fde68a;'>🏰 왕도"
      " 판타지 지온 강화</h3>",
      unsafe_allow_html=True,
  )

  if st.button(
      "🔥 GOD MODE 강화 실행",
      use_container_width=True,
      disabled=(st.session_state.level >= 30),
  ):
    enhance()
    if st.session_state.status == "NOT_ENOUGH_MONEY":
      st.error("강화 비용이 부족합니다!")
    else:
      st.rerun()

  st.write("")
  if st.button(
      "💰 현재 냄새 판매",
      use_container_width=True,
      disabled=(st.session_state.level == 0),
  ):
    sell()
    st.rerun()
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#e2e8f0;'>⚙️ 모드"
      " 설정</h4>",
      unsafe_allow_html=True,
  )
  st.session_state.dev_mode = st.toggle(
      "🛠️ 개발자 테스트 모드 (100% 성공)", value=st.session_state.dev_mode
  )
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#e2e8f0;'>🛒 상점</h4>",
      unsafe_allow_html=True,
  )

  tab_shop1, tab_shop2 = st.tabs(["🛡️ 상점", "💧 눈물"])
  with tab_shop1:
    st.caption("파괴 방지권 (보유 시 자동 발동)")
    if st.button("구매 (25만 원)", use_container_width=True):
      if st.session_state.money >= 250000:
        st.session_state.money -= 250000
        st.session_state.shield += 1
        st.success("보호권 보유 중!")
        st.rerun()
      else:
        st.error("금액이 부족합니다.")

  with tab_shop2:
    st.caption("눈물 15개로 1단계 확정 상승")
    if st.button("1단계 확정 상승 (15개)", use_container_width=True):
      if st.session_state.tears >= 15 and st.session_state.level < 30:
        st.session_state.tears -= 15
        st.session_state.level += 1
        st.session_state.status = "SUCCESS"
        st.success("확정 강화 성공!")
        st.rerun()
      else:
        st.error("조건이 부족합니다.")

  st.markdown("</div>", unsafe_allow_html=True)

with right_col:
  curr_data = SMELL_DB[st.session_state.level]
  card_color = curr_data["color"]
  card_title = curr_data["name"]
  card_desc = curr_data["desc"]
  card_price = format_gold(curr_data["price"])
  current_cost = format_gold(get_enhance_cost(st.session_state.level))
  tier = curr_data["tier"]
  status = st.session_state.status

  three_js_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ 
                margin: 0; 
                overflow: hidden; 
                background: transparent; 
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
            }}
            #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}

            #redFlashOverlay {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(239, 68, 68, 0.85);
                box-shadow: inset 0 0 120px rgba(185, 28, 28, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            #failFlashOverlay {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(245, 158, 11, 0.4);
                box-shadow: inset 0 0 100px rgba(217, 119, 6, 0.7);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            #shieldFlashOverlay {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(59, 130, 246, 0.7);
                box-shadow: inset 0 0 100px rgba(37, 99, 235, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            #critFlashOverlay {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(245, 158, 11, 0.85);
                box-shadow: inset 0 0 120px rgba(217, 119, 6, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            #successFlashOverlay {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(16, 185, 129, 0.5);
                box-shadow: inset 0 0 100px rgba(5, 150, 105, 0.8);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            .cinematic-ui {{
                position: absolute;
                bottom: 25px; 
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                text-align: center;
                z-index: 100;
                pointer-events: none;
            }}

            .title-tier-1 {{ font-size: 42px; font-weight: 900; color: #fde68a; text-shadow: 0 0 25px #fde68a; }}
            .title-tier-2 {{ font-size: 48px; font-weight: 900; color: #f59e0b; text-shadow: 0 0 30px #f59e0b; letter-spacing: 1px; }}
            .title-tier-3 {{ font-size: 54px; font-weight: 900; color: #ef4444; text-shadow: 0 0 35px #ef4444; animation: pulse 1s infinite alternate; }}
            .title-tier-4 {{ font-size: 60px; font-weight: 900; color: #c084fc; text-shadow: 0 0 40px #c084fc; letter-spacing: 2px; }}
            .title-tier-5 {{ font-size: 66px; font-weight: 900; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 40px #ff7e5f); animation: shake 0.5s infinite alternate; }}
            .title-tier-6 {{ font-size: 72px; font-weight: 900; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; filter: drop-shadow(0 0 50px #ffffff); }}

            @keyframes pulse {{ 0% {{ transform: scale(1); }} 100% {{ transform: scale(1.04); }} }}
            @keyframes shake {{ 0% {{ transform: translate(2px, 2px); }} 100% {{ transform: translate(-2px, -2px); }} }}
            @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}

            .status-header {{ font-size: 22px; font-weight: 800; margin-bottom: 6px; letter-spacing: 4px; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }}
            .desc-text {{ font-size: 16px; color: #f3e8ff; margin-top: 6px; text-shadow: 0 2px 10px rgba(0,0,0,0.9); }}
            .price-text {{ font-size: 22px; font-weight: 800; color: #fbbf24; margin-top: 6px; text-shadow: 0 0 20px rgba(0,0,0,0.9); }}
            .cost-text {{ font-size: 16px; font-weight: 700; color: #f87171; margin-top: 4px; text-shadow: 0 0 15px rgba(0,0,0,0.9); }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="redFlashOverlay"></div>
        <div id="failFlashOverlay"></div>
        <div id="shieldFlashOverlay"></div>
        <div id="critFlashOverlay"></div>
        <div id="successFlashOverlay"></div>
        <div id="container"></div>

        <div class="cinematic-ui">
            <div id="statusText" class="status-header">READY</div>
            <div class="title-tier-{tier}">
                {card_title}
            </div>
            <div class="desc-text">"{card_desc}"</div>
            <div class="price-text">예상 가치: {card_price}</div>
            <div class="cost-text">필요 강화 비용: {current_cost}</div>
        </div>

        <script>
            const status = "{status}";
            const statusText = document.getElementById('statusText');
            const flashOverlay = document.getElementById('redFlashOverlay');
            const failOverlay = document.getElementById('failFlashOverlay');
            const shieldOverlay = document.getElementById('shieldFlashOverlay');
            const critOverlay = document.getElementById('critFlashOverlay');
            const successOverlay = document.getElementById('successFlashOverlay');
            
            if (status === "CRITICAL") {{
                statusText.innerText = "⚡ CRITICAL HIT!! (+2단계 대성공) ⚡";
                statusText.style.color = "#ffe600";
            }} else if (status === "SUCCESS") {{
                statusText.innerText = "✨ ENHANCE SUCCESS ✨";
                statusText.style.color = "#34d399";
            }} else if (status === "SHIELD_SAVED") {{
                statusText.innerText = "🛡️ SHIELD PROTECTED! (파괴 방지 발동) 🛡️";
                statusText.style.color = "#60a5fa";
            }} else if (status === "DESTROYED") {{
                statusText.innerText = "💥 DESTROYED 💥";
                statusText.style.color = "#ef4444";
            }} else if (status === "FAILED") {{
                statusText.innerText = "🔻 ENHANCE FAILED (단계 하락) 🔻";
                statusText.style.color = "#f59e0b";
            }}

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0.4, 9.5);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.getElementById('container').appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
            scene.add(ambientLight);

            const dirLight = new THREE.DirectionalLight(0xffffff, 1.5);
            dirLight.position.set(5, 8, 5);
            scene.add(dirLight);

            const cardPointLight = new THREE.PointLight("{card_color}", 7, 25);
            cardPointLight.position.set(0, 2, 4);
            scene.add(cardPointLight);

            const bgGroup = new THREE.Group();
            
            const ringGeo1 = new THREE.TorusGeometry(6.0, 0.04, 16, 100);
            const ringMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", emissive: "{card_color}", emissiveIntensity: 1.0, roughness: 0.1 }});
            const spaceRing1 = new THREE.Mesh(ringGeo1, ringMat);
            spaceRing1.rotation.x = Math.PI / 3;
            bgGroup.add(spaceRing1);

            const ringGeo2 = new THREE.TorusGeometry(7.5, 0.03, 16, 100);
            const spaceRing2 = new THREE.Mesh(ringGeo2, ringMat);
            spaceRing2.rotation.y = Math.PI / 4;
            bgGroup.add(spaceRing2);

            const ringGeo3 = new THREE.TorusGeometry(9.0, 0.02, 16, 100);
            const spaceRing3 = new THREE.Mesh(ringGeo3, ringMat);
            spaceRing3.rotation.z = Math.PI / 6;
            bgGroup.add(spaceRing3);

            scene.add(bgGroup);

            const particleGroup = new THREE.Group();
            const pCount = 2000;
            const pGeo = new THREE.BufferGeometry();
            const pPos = new Float32Array(pCount * 3);

            for(let i=0; i<pCount; i++) {{
                pPos[i*3] = (Math.random() - 0.5) * 40;
                pPos[i*3 + 1] = (Math.random() - 0.5) * 40;
                pPos[i*3 + 2] = (Math.random() - 0.5) * 40;
            }}

            pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
            const pMat = new THREE.PointsMaterial({{
                color: "{card_color}", size: 0.15, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending
            }});
            const particles = new THREE.Points(pGeo, pMat);
            particleGroup.add(particles);
            scene.add(particleGroup);

            const cardGroup = new THREE.Group();

            const frameGeo = new THREE.BoxGeometry(4.0, 5.9, 0.22);
            const frameMat = new THREE.MeshStandardMaterial({{ 
                color: 0xfbbf24, 
                metalness: 0.95, 
                roughness: 0.15,
                emissive: 0xd97706,
                emissiveIntensity: 0.2
            }});
            const frame = new THREE.Mesh(frameGeo, frameMat);
            cardGroup.add(frame);

            const inlayGeo = new THREE.BoxGeometry(3.7, 5.6, 0.24);
            const inlayMat = new THREE.MeshStandardMaterial({{ color: 0x111111, metalness: 0.5, roughness: 0.5 }});
            const inlay = new THREE.Mesh(inlayGeo, inlayMat);
            cardGroup.add(inlay);

            const bodyGeo = new THREE.BoxGeometry(3.3, 3.3, 0.26);
            const bodyMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", metalness: 0.75, roughness: 0.25, emissive: "{card_color}", emissiveIntensity: 0.3 }});
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            body.position.y = 0.85;
            cardGroup.add(body);

            const coreGeo = new THREE.OctahedronGeometry(0.85, 0);
            const coreMat = new THREE.MeshStandardMaterial({{
                color: 0xffffff, emissive: "{card_color}", emissiveIntensity: 1.5, roughness: 0.05, metalness: 0.9
            }});
            const core = new THREE.Mesh(coreGeo, coreMat);
            core.position.set(0, 0.85, 0.18);
            cardGroup.add(core);

            const nameplateGeo = new THREE.BoxGeometry(3.3, 1.4, 0.26);
            const nameplateMat = new THREE.MeshStandardMaterial({{ color: 0x222222, metalness: 0.8, roughness: 0.3 }});
            const nameplate = new THREE.Mesh(nameplateGeo, nameplateMat);
            nameplate.position.y = -1.55;
            cardGroup.add(nameplate);

            scene.add(cardGroup);

            const shieldGeo = new THREE.SphereGeometry(3.8, 32, 32);
            const shieldMat = new THREE.MeshStandardMaterial({{
                color: 0x60a5fa, emissive: 0x2563eb, emissiveIntensity: 0.8, transparent: true, opacity: 0.0, wireframe: true
            }});
            const shieldDome = new THREE.Mesh(shieldGeo, shieldMat);
            shieldDome.position.y = 0.2;
            scene.add(shieldDome);

            let shardsGroup = new THREE.Group();
            scene.add(shardsGroup);

            if (status === "SHIELD_SAVED") {{
                gsap.fromTo(shieldOverlay, {{ opacity: 0.8 }}, {{ opacity: 0, duration: 1.0, ease: "power2.out" }});
                gsap.fromTo(shieldMat, {{ opacity: 0.9, wireframe: true }}, {{ opacity: 0, duration: 1.5, ease: "power2.inOut" }});
                gsap.fromTo(shieldDome.scale, {{ x: 0.2, y: 0.2, z: 0.2 }}, {{ x: 1.2, y: 1.2, z: 1.2, duration: 0.8, ease: "back.out(1.7)" }});
                gsap.to(cardGroup.position, {{ z: -2, duration: 0.15, yoyo: true, repeat: 5 }});
            }} else if (status === "CRITICAL") {{
                gsap.fromTo(critOverlay, {{ opacity: 0.9 }}, {{ opacity: 0, duration: 1.0, ease: "power2.out" }});
                gsap.fromTo(camera.position, {{ z: 4 }}, {{ z: 9.5, duration: 1.5, ease: "bounce.out" }});
                gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 6, z: Math.PI * 2 }}, {{ y: 0, z: 0, duration: 1.5, ease: "power3.out" }});
            }} else if (status === "FAILED") {{
                gsap.fromTo(failOverlay, {{ opacity: 0.8 }}, {{ opacity: 0, duration: 0.8, ease: "power2.out" }});
                gsap.to(cardGroup.position, {{ x: 0.25, duration: 0.05, repeat: 5, yoyo: true, onComplete: () => {{ cardGroup.position.x = 0; }} }});
                gsap.fromTo(cardGroup.rotation, {{ z: -0.15 }}, {{ z: 0.15, duration: 0.08, repeat: 3, yoyo: true, onComplete: () => {{ cardGroup.rotation.z = 0; }} }});
            }} else if (status === "DESTROYED") {{
                gsap.fromTo(flashOverlay, {{ opacity: 0.85 }}, {{ opacity: 0, duration: 1.2, ease: "power2.out" }});
                gsap.to(camera.position, {{ x: 0.4, y: 0.8, duration: 0.04, repeat: 10, yoyo: true, onComplete: () => {{ camera.position.set(0, 0.4, 9.5); }} }});
                cardGroup.visible = false;

                const shardCount = 20;
                for(let i = 0; i < shardCount; i++) {{
                    const sGeo = new THREE.TetrahedronGeometry(Math.random() * 0.5 + 0.25);
                    const sMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", roughness: 0.2 }});
                    const shard = new THREE.Mesh(sGeo, sMat);
                    shard.position.set(0, 0.2, 0);
                    shardsGroup.add(shard);

                    gsap.to(shard.position, {{
                        x: (Math.random() - 0.5) * 7,
                        y: (Math.random() - 0.5) * 7,
                        z: (Math.random() - 0.5) * 7,
                        duration: 1.2,
                        ease: "power3.out"
                    }});
                    gsap.to(shard.rotation, {{
                        x: Math.random() * Math.PI * 4,
                        y: Math.random() * Math.PI * 4,
                        duration: 1.2
                    }});
                    gsap.to(shard.scale, {{ x: 0, y: 0, z: 0, duration: 1.2, ease: "power2.in" }});
                }}
            }} else if (status === "SUCCESS") {{
                gsap.fromTo(successOverlay, {{ opacity: 0.7 }}, {{ opacity: 0, duration: 0.8, ease: "power2.out" }});
                gsap.fromTo(camera.position, {{ z: 5 }}, {{ z: 9.5, duration: 1.2, ease: "power2.out" }});
                gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 2 }}, {{ y: 0, duration: 1.2, ease: "power2.out" }});
            }}

            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();

                spaceRing1.rotation.z = time * 0.2;
                spaceRing2.rotation.z = -time * 0.25;
                spaceRing3.rotation.x = time * 0.15;

                const pos = pGeo.attributes.position.array;
                for(let i=1; i<pCount*3; i+=3) {{
                    pos[i] += Math.sin(time + pos[i-1]) * 0.005 + 0.01;
                    if(pos[i] > 20) pos[i] = -20;
                }}
                pGeo.attributes.position.needsUpdate = true;

                if (cardGroup.visible) {{
                    cardGroup.rotation.y = Math.sin(time * 0.8) * 0.2;
                    cardGroup.position.y = Math.sin(time * 1.5) * 0.12 + 0.2;
                }}
                
                core.rotation.x = time * 2;
                core.rotation.y = time * 2;

                renderer.render(scene, camera);
            }}

            animate();

            window.addEventListener('resize', () => {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }});
        </script>
    </body>
    </html>
    """

  components.html(three_js_code, height=650, scrolling=False)

# -----------------------------------------------------------------------------
# 9. 하단 스탯 대시보드
# -----------------------------------------------------------------------------
st.write("")
b_col1, b_col2, b_col3, b_col4 = st.columns([1, 1, 1, 1], gap="small")

with b_col1:
  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">💳 보유 금액</div>
            <div class="stat-value">{format_gold(st.session_state.money)}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with b_col2:
  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">🛡️ 보유권 개수</div>
            <div class="stat-value">{st.session_state.shield}개</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with b_col3:
  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">💧 지온의 눈물</div>
            <div class="stat-value">{st.session_state.tears}개</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with b_col4:
  sp, fp, dp = (
      PROB_TABLE[st.session_state.level]
      if st.session_state.level < 30
      else (0, 0, 0)
  )
  crit_pct = int(CRITICAL_RATE * 100)
  prob_str = (
      "100% (DEV)"
      if st.session_state.dev_mode
      else f"{sp}% / {crit_pct}% / {dp}%"
  )
  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">📊 성공 / 크리 / 파괴</div>
            <div class="stat-value" style="font-size: 14px;">{prob_str}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
