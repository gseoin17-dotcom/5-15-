import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - COSMIC EDITION",
    page_icon="🌌",
    layout="wide",
)

# -----------------------------------------------------------------------------
# 2. 유틸리티 함수 및 비용 설정
# -----------------------------------------------------------------------------


def format_gold(amount):
  if amount == 0 or amount == float("inf"):
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
      0: 300,
      1: 300,
      2: 500,
      3: 500,
      4: 1000,
      5: 1500,
      6: 2000,
      7: 2000,
      8: 3000,
      9: 5000,
      10: 10900,
      11: 20000,
      12: 35000,
      13: 55000,
      14: 100000,
      15: 180000,
      16: 300000,
      17: 300000,
      18: 500000,
      19: 800000,
      20: 1500000,
      21: 2500000,
      22: 4000000,
      23: 6500000,
      24: 10000000,
      25: 16000000,
      26: 25000000,
      27: 40000000,
      28: 65000000,
      29: 100000000,
      30: 150000000,
      31: 250000000,
      32: 400000000,
      33: 700000000,
      34: 1200000000,
      35: 2000000000,
  }
  return cost_table.get(level, 2000000000)


def get_shield_cost(level):
  base_cost = get_enhance_cost(level)
  return max(50000, base_cost * 15)


# -----------------------------------------------------------------------------
# 3. 게임 데이터베이스 정의 (35단계 확장)
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
        "price": 20000000000,
        "color": "#00ffff",
        "tier": 6,
    },
    31: {
        "name": "31단계 : 하이퍼 지온 싱귤래리티",
        "desc": "냄새가 너무 진해져 시공간이 한 점으로 수축한다.",
        "price": 45000000000,
        "color": "#7000ff",
        "tier": 6,
    },
    32: {
        "name": "32단계 : 멀티버스 지온 에센스",
        "desc": "모든 평행우주의 지온맘이 동시에 미소 짓는다.",
        "price": 90000000000,
        "color": "#ff00e1",
        "tier": 6,
    },
    33: {
        "name": "33단계 : 인피니티 자이온 페트리코",
        "desc": "끝나지 않는 대폭발 속에서 영원히 피어나는 향.",
        "price": 200000000000,
        "color": "#00ff66",
        "tier": 6,
    },
    34: {
        "name": "34단계 : 오메가 자이온 제네시스",
        "desc": "우주의 탄생과 소멸을 관장하는 궁극의 향기.",
        "price": 500000000000,
        "color": "#ff6600",
        "tier": 6,
    },
    35: {
        "name": "35단계 : ★디 오리지널 앱솔루트 지온★",
        "desc": "모든 존재의 기원, 완벽에 도달한 완전무결한 냄새.",
        "price": float("inf"),
        "color": "#ffffff",
        "tier": 6,
    },
}

PROB_TABLE = {
    0: (100.0, 0.0, 0.0, 0.0),
    1: (100.0, 0.0, 0.0, 0.0),
    2: (100.0, 0.0, 0.0, 0.0),
    3: (95.0, 5.0, 0.0, 0.0),
    4: (95.0, 5.0, 0.0, 0.0),
    5: (90.0, 10.0, 0.0, 0.0),
    6: (90.0, 8.0, 2.0, 0.0),
    7: (90.0, 5.0, 5.0, 0.0),
    8: (85.0, 10.0, 5.0, 0.0),
    9: (80.0, 15.0, 5.0, 0.0),
    10: (80.0, 15.0, 5.0, 0.0),
    11: (75.0, 15.0, 5.0, 5.0),
    12: (70.0, 15.0, 5.0, 10.0),
    13: (70.0, 15.0, 7.0, 8.0),
    14: (65.0, 15.0, 10.0, 10.0),
    15: (60.0, 20.0, 10.0, 10.0),
    16: (60.0, 18.0, 12.0, 10.0),
    17: (55.0, 20.0, 15.0, 10.0),
    18: (50.0, 20.0, 17.0, 13.0),
    19: (50.0, 20.0, 20.0, 10.0),
    20: (45.0, 22.0, 23.0, 10.0),
    21: (40.0, 25.0, 25.0, 10.0),
    22: (40.0, 23.0, 27.0, 10.0),
    23: (40.0, 20.0, 30.0, 10.0),
    24: (40.0, 18.0, 32.0, 10.0),
    25: (35.0, 25.0, 30.0, 10.0),
    26: (50.0, 20.0, 25.0, 5.0),
    27: (40.0, 25.0, 30.0, 5.0),
    28: (30.0, 30.0, 35.0, 5.0),
    29: (20.0, 35.0, 40.0, 5.0),
    30: (15.0, 35.0, 45.0, 5.0),
    31: (12.0, 35.0, 48.0, 5.0),
    32: (10.0, 35.0, 50.0, 5.0),
    33: (8.0, 37.0, 50.0, 5.0),
    34: (5.0, 40.0, 50.0, 5.0),
}

CRITICAL_RATE = 0.05
PITY_MAX = 5

# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
  st.session_state.level = 0
if "max_level" not in st.session_state:
  st.session_state.max_level = 0
if "money" not in st.session_state:
  st.session_state.money = 1000000
if "status" not in st.session_state:
  st.session_state.status = "READY"
if "shield" not in st.session_state:
  st.session_state.shield = 0
if "tears" not in st.session_state:
  st.session_state.tears = 0
if "pity_count" not in st.session_state:
  st.session_state.pity_count = 0

# -----------------------------------------------------------------------------
# 5. 강화 로직
# -----------------------------------------------------------------------------


def run_enhance():
  curr = st.session_state.level
  if curr >= 35:
    return

  cost = get_enhance_cost(curr)
  if st.session_state.money < cost:
    st.session_state.status = "NOT_ENOUGH_MONEY"
    return

  st.session_state.money -= cost

  if st.session_state.pity_count >= PITY_MAX - 1:
    st.session_state.level += 1
    st.session_state.status = "PITY_SUCCESS"
    st.session_state.pity_count = 0
    if st.session_state.level > st.session_state.max_level:
      st.session_state.max_level = st.session_state.level
    return

  sp, down_p, dp, hold_p = PROB_TABLE[curr]
  r = random.uniform(0, 100)

  success_limit = sp
  down_limit = success_limit + down_p
  destroy_limit = down_limit + dp

  if r < success_limit:
    st.session_state.pity_count = 0
    if random.random() < CRITICAL_RATE and curr + 2 <= 35:
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


def dev_force_success():
  curr = st.session_state.level
  if curr < 35:
    st.session_state.level += 1
    st.session_state.status = "SUCCESS"
    if st.session_state.level > st.session_state.max_level:
      st.session_state.max_level = st.session_state.level


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
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }
    .element-container, .stMarkdown {
        background: transparent !important;
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
    </style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. 메인 레이아웃
# -----------------------------------------------------------------------------
left_col, right_col = st.columns([2.2, 7.8], gap="medium")

with left_col:
  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🛠️ 시스템"
      " 설정</h4>",
      unsafe_allow_html=True,
  )
  dev_mode = st.toggle("💻 개발자 모드 활성화", value=False)

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  s_col1, s_col2 = st.columns(2)

  with s_col1:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>💳 보유 금액</div><div style='font-size:15px;"
        f" font-weight:800; color:#ffffff;'>{format_gold(st.session_state.money)}</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>💧 눈물</div><div style='font-size:15px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.tears} /"
        " 120개</div></div>",
        unsafe_allow_html=True,
    )

  with s_col2:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>🛡️ 방지권</div><div style='font-size:15px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.shield} /"
        " 3개</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")

    pity_left = PITY_MAX - st.session_state.pity_count
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>✨ 자이온맘의 가호</div><div style='font-size:13px;"
        f" font-weight:800; color:#ffffff;'>실패까지 <b>{pity_left}회</b></div></div>",
        unsafe_allow_html=True,
    )

  st.markdown(
      "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])

  with tab_shop1:
    current_shield_cost = get_shield_cost(st.session_state.level)
    st.markdown(
        f"<div style='font-size:14px; color:#cbd5e1; margin-bottom:8px;'>"
        f"<b>조건:</b> 18단계 이상 | <b>보유한도:</b> 최대 3개<br><b>가격:</b>"
        f" <span style='font-size:16px; font-weight:bold; color:#fde68a;'>"
        f"{format_gold(current_shield_cost)}</span></div>",
        unsafe_allow_html=True,
    )

    can_buy_shield = st.session_state.level >= 18 and st.session_state.shield < 3
    if st.button("방지권 구매", use_container_width=True, disabled=not can_buy_shield):
      if st.session_state.level < 18:
        st.warning("18단계 이상부터 구매 가능합니다.")
      elif st.session_state.shield >= 3:
        st.warning("최대 3개까지만 보유 가능합니다.")
      elif st.session_state.money >= current_shield_cost:
        st.session_state.money -= current_shield_cost
        st.session_state.shield += 1
        st.success("파괴 방지권 구매 완료!")
        st.rerun()
      else:
        st.error("금액이 부족합니다.")

  with tab_shop2:
    if st.session_state.level >= 32:
      st.markdown(
          "<div style='font-size:14px; color:#ef4444; font-weight:700;"
          " margin-bottom:8px;'>⚠️ 32단계 이상부터는 신성한 기운으로 인해 지온의"
          " 눈물을 사용할 수 없습니다!</div>",
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          f"<div style='font-size:14px; color:#cbd5e1;"
          f" margin-bottom:8px;'><b>효과:</b> 눈물 40개 소모 (50% 확률로 1~3단계"
          f" 상승)<br><b>현재보유:</b> <span style='font-weight:bold;"
          f" color:#38bdf8;'>{st.session_state.tears} / 120개</span></div>",
          unsafe_allow_html=True,
      )

    can_use_tears = st.session_state.level < 32
    if st.button("눈물 기적 가동", use_container_width=True, disabled=not can_use_tears):
      if st.session_state.level >= 32:
        st.warning("32단계부터는 눈물을 사용할 수 없습니다.")
      elif st.session_state.tears >= 40:
        st.session_state.tears -= 40
        if random.random() < 0.50:
          add_lvl = random.choice([1, 2, 3])
          st.session_state.level = min(35, st.session_state.level + add_lvl)
          st.session_state.status = "CRITICAL" if add_lvl >= 2 else "SUCCESS"
          st.success(f"눈물 기적 대성공! {add_lvl}단계 상승!")
        else:
          st.session_state.status = "FAILED"
          st.warning("눈물의 기적이 실패했습니다...")
        st.rerun()
      else:
        st.error("눈물 40개가 필요합니다.")

  st.markdown(
      "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🌌 자이온"
      " 강화 제어</h4>",
      unsafe_allow_html=True,
  )

  if st.button(
      "🔥 냄새 강화 실행",
      use_container_width=True,
      disabled=(st.session_state.level >= 35),
  ):
    cost = get_enhance_cost(st.session_state.level)
    if st.session_state.money < cost:
      st.error("강화 비용 부족!")
    else:
      run_enhance()
      st.rerun()

  if dev_mode:
    st.write("")
    if st.button(
        "✨ [DEV] 무조건 성공",
        use_container_width=True,
        disabled=(st.session_state.level >= 35),
    ):
      dev_force_success()
      st.rerun()

  st.write("")
  if st.button(
      "💰 현재 냄새 판매", use_container_width=True, disabled=(st.session_state.level == 0)
  ):
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
            body {{ 
                margin: 0; 
                overflow: hidden; 
                background: transparent; 
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
            }}
            #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}

            .cinematic-ui {{
                position: absolute;
                bottom: 25px; 
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                text-align: center;
                z-index: 100;
                pointer-events: none;
                opacity: 0;
                transition: opacity 0.4s ease-in-out;
            }}

            .cinematic-ui.visible {{
                opacity: 1;
            }}

            .title-tier-1 {{ font-size: 28px; font-weight: 800; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
            .title-tier-2 {{ font-size: 32px; font-weight: 800; color: #f59e0b; text-shadow: 0 0 22px #f59e0b; }}
            .title-tier-3 {{ font-size: 36px; font-weight: 800; color: #ef4444; text-shadow: 0 0 25px #ef4444; }}
            .title-tier-4 {{ font-size: 40px; font-weight: 800; color: #c084fc; text-shadow: 0 0 28px #c084fc; }}
            .title-tier-5 {{ font-size: 44px; font-weight: 800; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 12px rgba(255,126,95,0.6)); }}
            .title-tier-6 {{ font-size: 48px; font-weight: 800; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; filter: drop-shadow(0 0 15px rgba(255,255,255,0.8)); }}

            @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}

            .shaking-text {{
                animation: textVibe 0.18s infinite alternate ease-in-out;
            }}
            @keyframes textVibe {{
                0% {{ transform: translate(0px, 0px) rotate(0deg); }}
                25% {{ transform: translate(-1.5px, 1px) rotate(-0.5deg); }}
                50% {{ transform: translate(1.5px, -1.5px) rotate(0.8deg); }}
                75% {{ transform: translate(-1px, -1px) rotate(-0.3deg); }}
                100% {{ transform: translate(1px, 1.5px) rotate(0.5deg); }}
            }}

            .status-header {{ font-size: 16px; font-weight: 800; margin-bottom: 3px; letter-spacing: 1px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
            .desc-text {{ font-size: 13px; color: #cbd5e1; margin-top: 2px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); font-weight: 500; }}
            .price-text {{ font-size: 15px; font-weight: 800; color: #fbbf24; margin-top: 3px; text-shadow: 0 0 15px rgba(0,0,0,0.95); }}
            .cost-text {{ font-size: 12px; font-weight: 700; color: #f87171; margin-top: 2px; text-shadow: 0 0 12px rgba(0,0,0,0.95); }}
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

            const currentLevel = {current_level};
            if (currentLevel >= 20) {{
                document.getElementById('mainTitle').classList.add('shaking-text');
                document.getElementById('descText').classList.add('shaking-text');
                document.getElementById('priceText').classList.add('shaking-text');
                document.getElementById('costText').classList.add('shaking-text');
            }}

            const status = "{status}";
            const statusText = document.getElementById('statusText');
            
            const tierColor = "{card_color}";
            let statusColor = "#38bdf8";
            let particleSize = 0.3;
            let particleSpeed = 1.0;
            let glowIntensity = 15;

            if (status === "CRITICAL") {{
                statusText.innerText = "⚡ COSMIC CRITICAL HIT!! (+2단계 이상 대성공) ⚡";
                statusColor = "#ffffff"; 
                particleSize = 0.55;
                particleSpeed = 2.5;
                glowIntensity = 35;
            }} else if (status === "PITY_SUCCESS") {{
                statusText.innerText = "✨ 자이온맘의 가호 발동! (천장 100% 성공) ✨";
                statusColor = "#fde68a";
                particleSize = 0.45;
                particleSpeed = 2.0;
                glowIntensity = 30;
            }} else if (status === "SUCCESS") {{
                statusText.innerText = "✨ COSMIC SUCCESS (강화 성공) ✨";
                statusColor = tierColor;
                particleSize = 0.35;
                particleSpeed = 1.5;
                glowIntensity = 22;
            }} else if (status === "SHIELD_SAVED") {{
                statusText.innerText = "🛡️ SHIELD PROTECTED! (우주 방어 발동) 🛡️";
                statusColor = "#60a5fa";
            }} else if (status === "DESTROYED") {{
                statusText.innerText = "💥 BLACKHOLE DESTROYED (코어 붕괴됨) 💥";
                statusColor = "#ef4444";
                particleSpeed = 1.2;
            }} else if (status === "FAILED") {{
                statusText.innerText = "🔻 FAILED (에너지 하락) 🔻";
                statusColor = "#64748b";
                particleSpeed = 0.5;
                glowIntensity = 6;
            }} else if (status === "HOLD") {{
                statusText.innerText = "🔒 HOLD (에너지 동결) 🔒";
                statusColor = "#94a3b8";
                particleSpeed = 0.7;
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
            renderer.shadowMap.enabled = true;
            document.getElementById('container').appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
            scene.add(ambientLight);

            const mainLight = new THREE.DirectionalLight(0xffffff, 2.5);
            mainLight.position.set(5, 8, 5);
            scene.add(mainLight);

            const pointLight = new THREE.PointLight(statusColor, glowIntensity, 40);
            pointLight.position.set(0, 0, 3);
            scene.add(pointLight);

            const particleCount = 850;
            const particleGeo = new THREE.BufferGeometry();
            const particlePositions = new Float32Array(particleCount * 3);
            const particleVelocities = [];

            for(let i=0; i<particleCount; i++) {{
                particlePositions[i*3] = (Math.random() - 0.5) * 7.0;
                particlePositions[i*3 + 1] = -5.0 + Math.random() * 3.0;
                particlePositions[i*3 + 2] = (Math.random() - 0.5) * 7.0;
                
                let spd = particleSpeed;
                if (status === "FAILED") spd = 0.3;

                particleVelocities.push({{
                    x: (Math.random() - 0.5) * 0.02 * spd,
                    y: (0.015 + Math.random() * 0.03) * spd,
                    z: (Math.random() - 0.5) * 0.02 * spd,
                }});
            }}
            particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
            
            const particleMat = new THREE.PointsMaterial({{
                color: new THREE.Color(statusColor),
                size: particleSize,
                transparent: true,
                opacity: status === "FAILED" ? 0.3 : 0.9,
                blending: THREE.AdditiveBlending,
                depthWrite: false
            }});
            const particleSystem = new THREE.Points(particleGeo, particleMat);
            scene.add(particleSystem);

            const objectGroup = new THREE.Group();
            objectGroup.position.y = -0.7;

            let baseGeo;
            const lvl = {current_level};

            if (lvl <= 2) {{
                baseGeo = new THREE.TetrahedronGeometry(2.3);
            }} else if (lvl <= 5) {{
                baseGeo = new THREE.BoxGeometry(2.1, 2.1, 2.1);
            }} else if (lvl <= 8) {{
                baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 5);
            }} else if (lvl <= 11) {{
                baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 6);
            }} else if (lvl <= 14) {{
                baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 7);
            }} else if (lvl <= 17) {{
                baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 8);
            }} else if (lvl == 18) {{
                baseGeo = new THREE.OctahedronGeometry(2.5);
            }} else if (lvl == 19) {{
                baseGeo = new THREE.DodecahedronGeometry(2.4);
            }} else if (lvl == 20) {{
                baseGeo = new THREE.IcosahedronGeometry(2.4);
            }} else if (lvl == 21) {{
                baseGeo = new THREE.ConeGeometry(2.1, 3.1, 6);
            }} else if (lvl == 22) {{
                baseGeo = new THREE.TorusGeometry(1.7, 0.65, 16, 32);
            }} else if (lvl == 23) {{
                baseGeo = new THREE.TorusKnotGeometry(1.4, 0.45, 64, 16, 2, 3);
            }} else if (lvl == 24) {{
                baseGeo = new THREE.CylinderGeometry(0.5, 2.1, 2.9, 12);
            }} else if (lvl == 25) {{
                baseGeo = new THREE.SphereGeometry(2.2, 16, 16);
            }} else if (lvl == 26) {{
                baseGeo = new THREE.ConeGeometry(2.3, 3.3, 8);
            }} else if (lvl == 27) {{
                baseGeo = new THREE.TorusKnotGeometry(1.5, 0.55, 96, 24, 3, 4);
            }} else if (lvl == 28) {{
                baseGeo = new THREE.IcosahedronGeometry(2.5, 1);
            }} else if (lvl == 29) {{
                baseGeo = new THREE.DodecahedronGeometry(2.6, 1);
            }} else if (lvl == 30) {{
                baseGeo = new THREE.TorusKnotGeometry(1.5, 0.55, 128, 32, 2, 5);
            }} else if (lvl == 31) {{
                baseGeo = new THREE.OctahedronGeometry(2.7, 2);
            }} else if (lvl == 32) {{
                baseGeo = new THREE.IcosahedronGeometry(2.7, 2);
            }} else if (lvl == 33) {{
                baseGeo = new THREE.TorusKnotGeometry(1.6, 0.6, 128, 32, 3, 5);
            }} else if (lvl == 34) {{
                baseGeo = new THREE.SphereGeometry(2.8, 32, 32);
            }} else {{
                baseGeo = new THREE.TorusKnotGeometry(1.8, 0.7, 150, 40, 4, 7);
            }}

            const outerMat = new THREE.MeshPhysicalMaterial({{
                color: tierColor,
                emissive: status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? statusColor : "#111111",
                emissiveIntensity: status === "SUCCESS" ? 0.5 : (status === "CRITICAL" || status === "PITY_SUCCESS" ? 0.9 : 0.15),
                metalness: 0.9,
                roughness: 0.15,
                transmission: 0.6,
                transparent: true,
                opacity: status === "FAILED" ? 0.5 : 0.95,
                wireframe: false
            }});
            const outerMesh = new THREE.Mesh(baseGeo, outerMat);
            objectGroup.add(outerMesh);

            const coreGeo = new THREE.SphereGeometry(1.2, 32, 32);
            const coreMat = new THREE.MeshPhysicalMaterial({{
                color: 0xffffff,
                emissive: statusColor,
                emissiveIntensity: status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? 3.0 : 1.2,
                roughness: 0.05,
                metalness: 0.95,
                transmission: 0.8
            }});
            const coreMesh = new THREE.Mesh(coreGeo, coreMat);
            objectGroup.add(coreMesh);

            scene.add(objectGroup);

            uiElement.classList.add('visible');

            if (status === "DESTROYED") {{
                outerMesh.visible = false;
                coreMesh.visible = false;

                const shardCount = 55;
                const shards = [];
                const shardGroup = new THREE.Group();
                shardGroup.position.y = -0.7;

                for(let i=0; i<shardCount; i++) {{
                    const sGeo = new THREE.BoxGeometry(0.3 + Math.random()*0.2, 0.3 + Math.random()*0.2, 0.3 + Math.random()*0.2);
                    const sMat = new THREE.MeshStandardMaterial({{
                        color: tierColor,
                        roughness: 0.2,
                        metalness: 0.9,
                        emissive: "#ef4444",
                        emissiveIntensity: 1.0
                    }});
                    const shard = new THREE.Mesh(sGeo, sMat);
                    shard.position.set(0, 0, 0);
                    
                    const u = Math.random();
                    const v = Math.random();
                    const theta = u * 2.0 * Math.PI;
                    const phi = Math.acos(2.0 * v - 1.0);
                    const speed = 4.0 + Math.random() * 5.0;
                    
                    shard.userData = {{
                        vx: speed * Math.sin(phi) * Math.cos(theta),
                        vy: speed * Math.sin(phi) * Math.sin(theta),
                        vz: speed * Math.cos(phi),
                        rx: (Math.random() - 0.5) * 20,
                        ry: (Math.random() - 0.5) * 20
                    }};

                    shardGroup.add(shard);
                    shards.push(shard);
                }}
                scene.add(shardGroup);

                gsap.to(shardGroup.position, {{
                    duration: 1.2,
                    ease: "power2.out",
                    onUpdate: function() {{
                        const progress = this.progress();
                        shards.forEach(s => {{
                            s.position.x += s.userData.vx * 0.02;
                            s.position.y += s.userData.vy * 0.02 - 0.05;
                            s.position.z += s.userData.vz * 0.02;
                            s.rotation.x += s.userData.rx * 0.02;
                            s.rotation.y += s.userData.ry * 0.02;
                            s.material.opacity = 1.0 - progress;
                            s.material.transparent = true;
                        }});
                    }}
                }});
            }} else if (status === "CRITICAL" || status === "PITY_SUCCESS") {{
                gsap.fromTo(objectGroup.scale, {{x: 0.2, y: 0.2, z: 0.2}}, {{x: 1.3, y: 1.3, z: 1.3, duration: 0.5, ease: "power2.out"}});
                gsap.to(objectGroup.scale, {{x: 1, y: 1, z: 1, duration: 0.3, delay: 0.5}});
            }} else if (status === "SUCCESS") {{
                gsap.fromTo(objectGroup.scale, {{x: 0.8, y: 0.8, z: 0.8}}, {{x: 1.15, y: 1.15, z: 1.15, duration: 0.3, yoyo: true, repeat: 1, ease: "power1.out"}});
            }} else if (status === "FAILED") {{
                gsap.fromTo(objectGroup.scale, {{x: 1.05, y: 1.05, z: 1.05}}, {{x: 0.92, y: 0.92, z: 0.92, duration: 0.3, ease: "power1.out"}});
            }} else if (status === "SHIELD_SAVED") {{
                gsap.fromTo(objectGroup.scale, {{x: 1.25, y: 1.25, z: 1.25}}, {{x: 1, y: 1, z: 1, duration: 0.4, ease: "back.out(2)"}});
            }}

            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();

                if (status !== "DESTROYED") {{
                    const rotSpeed = status === "FAILED" ? 0.4 : (status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? 1.2 : 0.65);
                    outerMesh.rotation.x = time * (0.5 * rotSpeed);
                    outerMesh.rotation.y = time * (0.75 * rotSpeed);
                    coreMesh.rotation.x = -time * (1.2 * rotSpeed);
                    coreMesh.rotation.y = -time * (1.5 * rotSpeed);
                    objectGroup.rotation.y = Math.sin(time * 0.7) * 0.25;
                }}

                const positions = particleGeo.attributes.position.array;
                for(let i=0; i<particleCount; i++) {{
                    positions[i*3] += particleVelocities[i].x;
                    positions[i*3 + 1] += particleVelocities[i].y;
                    positions[i*3 + 2] += particleVelocities[i].z;

                    if(positions[i*3 + 1] > 3.0) {{
                        positions[i*3 + 1] = -5.0;
                        positions[i*3] = (Math.random() - 0.5) * 7.0;
                        positions[i*3 + 2] = (Math.random() - 0.5) * 7.0;
                    }}
                }}
                particleGeo.attributes.position.needsUpdate = true;

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

  components.html(three_js_code, height=580, scrolling=False)
