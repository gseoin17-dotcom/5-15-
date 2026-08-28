import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - TRASH MOUNTAIN EDITION",
    page_icon="🗑️",
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
  }
  return cost_table.get(level, 150000000)


def get_shield_cost(level):
  base_cost = get_enhance_cost(level)
  return max(50000, base_cost * 15)


# -----------------------------------------------------------------------------
# 3. 게임 데이터베이스 및 강화 확률표
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
}

CRITICAL_RATE = 0.05

# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
  st.session_state.level = 0
if "money" not in st.session_state:
  st.session_state.money = 1000000
if "status" not in st.session_state:
  st.session_state.status = "READY"
if "shield" not in st.session_state:
  st.session_state.shield = 0
if "tears" not in st.session_state:
  st.session_state.tears = 0

# -----------------------------------------------------------------------------
# 5. 강화 로직
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

  sp, down_p, dp, hold_p = PROB_TABLE[curr]
  r = random.uniform(0, 100)

  success_limit = sp
  down_limit = success_limit + down_p
  destroy_limit = down_limit + dp

  if r < success_limit:
    if random.random() < CRITICAL_RATE and curr + 2 <= 30:
      st.session_state.level += 2
      st.session_state.status = "CRITICAL"
    else:
      st.session_state.level += 1
      st.session_state.status = "SUCCESS"
  elif r < down_limit:
    if curr > 0:
      st.session_state.level -= 1
    st.session_state.status = "FAILED"
    st.session_state.tears = min(120, st.session_state.tears + 1)
  elif r < destroy_limit:
    if st.session_state.shield > 0:
      st.session_state.shield -= 1
      st.session_state.status = "SHIELD_SAVED"
      st.session_state.tears = min(120, st.session_state.tears + 1)
    else:
      st.session_state.level = 0
      st.session_state.status = "DESTROYED"
      st.session_state.tears = min(120, st.session_state.tears + 2)
  else:
    st.session_state.status = "HOLD"
    st.session_state.tears = min(120, st.session_state.tears + 1)


def dev_force_success():
  curr = st.session_state.level
  if curr < 30:
    st.session_state.level += 1
    st.session_state.status = "SUCCESS"


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
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.9)), url("https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        max-width: 98% !important;
    }
    .element-container, .stMarkdown {
        background: transparent !important;
    }
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 6px 12px !important;
        transition: all 0.2s ease !important;
        border: 1px solid rgba(217, 119, 6, 0.4) !important;
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.7), rgba(217, 119, 6, 0.7)) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(217, 119, 6, 0.8);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. 메인 레이아웃
# -----------------------------------------------------------------------------
left_col, right_col = st.columns([3.0, 7.0], gap="small")

with left_col:
  st.markdown(
      "<h4 style='margin:0 0 6px 0; font-size: 15px; color:#fde68a;'>🛠️ 시스템"
      " 설정</h4>",
      unsafe_allow_html=True,
  )
  dev_mode = st.toggle("💻 개발자 모드 활성화", value=False)

  st.markdown(
      "<hr style='margin:8px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<h4 style='margin:0 0 6px 0; font-size: 15px; color:#fde68a;'>🗑️ 지온"
      " 강화 제어</h4>",
      unsafe_allow_html=True,
  )

  if st.button(
      "🔥 강화 실행",
      use_container_width=True,
      disabled=(st.session_state.level >= 30),
  ):
    cost = get_enhance_cost(st.session_state.level)
    if st.session_state.money < cost:
      st.error("강화 비용 부족!")
    else:
      run_enhance()
      st.rerun()

  if dev_mode:
    if st.button(
        "✨ [DEV] 무조건 성공",
        use_container_width=True,
        disabled=(st.session_state.level >= 30),
    ):
      dev_force_success()
      st.rerun()

  if st.button(
      "💰 현재 냄새 판매",
      use_container_width=True,
      disabled=(st.session_state.level == 0),
  ):
    sell()
    st.rerun()

  st.markdown("<br>", unsafe_allow_html=True)

  s_col1, s_col2 = st.columns(2)

  with s_col1:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:11px;"
        f" color:#fde68a;'>💳 보유 금액</div><div style='font-size:14px;"
        f" font-weight:800;"
        f" color:#ffffff;'>{format_gold(st.session_state.money)}</div></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='text-align: center; margin-top:8px;'><div"
        f" style='font-size:11px; color:#fde68a;'>💧 눈물</div><div"
        f" style='font-size:14px; font-weight:800; color:#ffffff;'>"
        f"{st.session_state.tears} / 120개</div></div>",
        unsafe_allow_html=True,
    )

  with s_col2:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:11px;"
        f" color:#fde68a;'>🛡️ 방지권</div><div style='font-size:14px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.shield} /"
        " 3개</div></div>",
        unsafe_allow_html=True,
    )

    if st.session_state.level < 30:
      sp, down_p, dp, hold_p = PROB_TABLE[st.session_state.level]
      crit_pct = int(CRITICAL_RATE * 100)
      prob_str = f"성공:{sp}%(크리{crit_pct}%)<br>하락:{down_p}%/파괴:{dp}%"
    else:
      prob_str = "MAX LEVEL"

    st.markdown(
        f"<div style='text-align: center; margin-top:8px;'><div"
        f" style='font-size:11px; color:#fde68a;'>📊 상세 확률</div><div"
        f" style='font-size:10px; font-weight:800; color:#ffffff; line-height:"
        f" 1.2;'>{prob_str}</div></div>",
        unsafe_allow_html=True,
    )

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<h4 style='margin:0 0 6px 0; font-size: 15px; color:#e2e8f0;'>🛒 암시장"
      " 상점</h4>",
      unsafe_allow_html=True,
  )

  tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])
  with tab_shop1:
    current_shield_cost = get_shield_cost(st.session_state.level)
    st.caption(
        f"파괴 방지권 (18단계 이상, 최대 3개)\n가격:"
        f" {format_gold(current_shield_cost)}"
    )

    can_buy_shield = st.session_state.level >= 18 and st.session_state.shield < 3
    if st.button(
        "방지권 구매", use_container_width=True, disabled=not can_buy_shield
    ):
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
    st.caption(f"눈물 40개 소모 -> 50% 확률로 1~3단계 상승")
    if st.button("눈물 기적 가동", use_container_width=True):
      if st.session_state.tears >= 40 and st.session_state.level < 30:
        st.session_state.tears -= 40
        if random.random() < 0.50:
          add_lvl = random.choice([1, 2, 3])
          st.session_state.level = min(30, st.session_state.level + add_lvl)
          st.session_state.status = (
              "CRITICAL" if add_lvl >= 2 else "SUCCESS"
          )
          st.success(f"눈물 기적 대성공! {add_lvl}단계 상승!")
        else:
          st.session_state.status = "FAILED"
          st.warning("눈물의 기적이 실패했습니다...")
        st.rerun()
      else:
        st.error("눈물 40개가 필요합니다.")

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

  # 30단계 도달 시 나타날 화려하고 압도적인 엔딩 크레딧용 HTML/Three.js 코드
  if current_level >= 30:
    three_js_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ 
                    margin: 0; 
                    overflow: hidden; 
                    background: #000; 
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
                }}
                #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}

                .credits-container {{
                    position: absolute;
                    top: 100%;
                    width: 100%;
                    text-align: center;
                    color: #ffffff;
                    z-index: 100;
                    pointer-events: none;
                    animation: scrollCredits 25s linear infinite;
                }}

                @keyframes scrollCredits {{
                    0% {{ top: 100%; opacity: 0; }}
                    10% {{ opacity: 1; }}
                    90% {{ opacity: 1; }}
                    100% {{ top: -150%; opacity: 0; }}
                }}

                .credit-title {{ font-size: 38px; font-weight: 900; color: #00ffff; text-shadow: 0 0 30px #00ffff; margin-bottom: 20px; }}
                .credit-subtitle {{ font-size: 20px; color: #ff00aa; margin-bottom: 40px; font-weight: 700; text-shadow: 0 0 15px #ff00aa; }}
                .credit-section {{ font-size: 24px; font-weight: 800; color: #fde68a; margin-top: 40px; margin-bottom: 15px; text-shadow: 0 0 10px #fde68a; }}
                .credit-name {{ font-size: 16px; color: #e2e8f0; margin-bottom: 8px; line-height: 1.6; }}

                .center-ui {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    text-align: center;
                    z-index: 101;
                    pointer-events: none;
                }}

                .absolute-god-title {{
                    font-size: 52px;
                    font-weight: 900;
                    background: linear-gradient(90deg, #00ffff, #ff00aa, #fffb00, #00ffff);
                    background-size: 300% auto;
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    animation: rainbowGod 3s linear infinite;
                    text-shadow: 0 0 40px rgba(0,255,255,0.6);
                    margin-bottom: 10px;
                }}

                @keyframes rainbowGod {{
                    0% {{ background-position: 0% center; }}
                    100% {{ background-position: 300% center; }}
                }}

                .god-desc {{
                    font-size: 16px;
                    color: #ffffff;
                    text-shadow: 0 2px 10px rgba(0,0,0,0.9);
                    font-weight: 600;
                }}
            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        </head>
        <body>
            <div id="container"></div>

            <div class="center-ui">
                <div class="absolute-god-title">★ 태초의 자이온맘 ★</div>
                <div class="god-desc">"우주를 지온으로 통일한 자이온맘의 완성."</div>
            </div>

            <div class="credits-container">
                <div class="credit-title">THE END OF UNIVERSE</div>
                <div class="credit-subtitle">당신은 마침내 절대신성에 도달했습니다.</div>

                <div class="credit-section">✨ EXECUTIVE PRODUCER</div>
                <div class="credit-name">자이온맘 (Zion Mom)</div>

                <div class="credit-section">🗑️ TRASH MOUNTAIN CREW</div>
                <div class="credit-name">방선균 배양 연구팀</div>
                <div class="credit-name">페트리코 입자 가속기 관리소</div>

                <div class="credit-section">💧 TEARS & SHIELD SYSTEM</div>
                <div class="credit-name">눈물 기적 가동 위원회</div>
                <div class="credit-name">18단계 파괴 방지 보안국</div>

                <div class="credit-section">🌟 SPECIAL THANKS</div>
                <div class="credit-name">지온 냄새를 사랑하는 모든 우주 여행자들</div>
                <div class="credit-name">그리고 포기하지 않은 당신께 영광을!</div>

                <div style="margin-top: 60px; font-size: 14px; color: #94a3b8;">THANK YOU FOR PLAYING</div>
            </div>

            <script>
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
                camera.position.set(0, 0, 12);

                const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                renderer.setSize(window.innerWidth, window.innerHeight);
                renderer.setPixelRatio(window.devicePixelRatio);
                document.getElementById('container').appendChild(renderer.domElement);

                const particleCount = 2000;
                const geometry = new THREE.BufferGeometry();
                const positions = new Float32Array(particleCount * 3);
                const colors = new Float32Array(particleCount * 3);

                const colorChoices = [
                    new THREE.Color(0x00ffff),
                    new THREE.Color(0xff00aa),
                    new THREE.Color(0xfffb00),
                    new THREE.Color(0xffffff)
                ];

                for(let i = 0; i < particleCount; i++) {{
                    positions[i * 3] = (Math.random() - 0.5) * 20;
                    positions[i * 3 + 1] = (Math.random() - 0.5) * 20;
                    positions[i * 3 + 2] = (Math.random() - 0.5) * 20;

                    const col = colorChoices[Math.floor(Math.random() * colorChoices.length)];
                    colors[i * 3] = col.r;
                    colors[i * 3 + 1] = col.g;
                    colors[i * 3 + 2] = col.b;
                }}

                geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
                geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

                const material = new THREE.PointsMaterial({{
                    size: 0.15,
                    vertexColors: true,
                    transparent: true,
                    opacity: 0.8,
                    blending: THREE.AdditiveBlending
                }});

                const particleSystem = new THREE.Points(geometry, material);
                scene.add(particleSystem);

                const coreGeo = new THREE.TorusKnotGeometry(2.0, 0.6, 128, 32, 2, 5);
                const coreMat = new THREE.MeshPhysicalMaterial({{
                    color: 0x00ffff,
                    emissive: 0xff00aa,
                    emissiveIntensity: 0.8,
                    roughness: 0.1,
                    metalness: 0.9,
                    wireframe: true,
                    transparent: true,
                    opacity: 0.6
                }});
                const coreMesh = new THREE.Mesh(coreGeo, coreMat);
                scene.add(coreMesh);

                const clock = new THREE.Clock();

                function animate() {{
                    requestAnimationFrame(animate);
                    const time = clock.getElapsedTime();

                    particleSystem.rotation.y = time * 0.05;
                    particleSystem.rotation.x = time * 0.03;

                    coreMesh.rotation.x = time * 0.3;
                    coreMesh.rotation.y = time * 0.4;

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
  else:
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
                    bottom: 24px; 
                    left: 50%;
                    transform: translateX(-50%);
                    width: 100%;
                    text-align: center;
                    z-index: 100;
                    pointer-events: none;
                    opacity: 0;
                    transition: opacity 0.5s ease-in-out;
                }}

                .cinematic-ui.visible {{
                    opacity: 1;
                }}

                .title-tier-1 {{ font-size: 26px; font-weight: 900; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
                .title-tier-2 {{ font-size: 30px; font-weight: 900; color: #f59e0b; text-shadow: 0 0 25px #f59e0b; }}
                .title-tier-3 {{ font-size: 36px; font-weight: 900; color: #ef4444; text-shadow: 0 0 30px #ef4444; }}
                .title-tier-4 {{ font-size: 42px; font-weight: 900; color: #c084fc; text-shadow: 0 0 35px #c084fc; }}
                .title-tier-5 {{ font-size: 48px; font-weight: 900; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
                .title-tier-6 {{ font-size: 52px; font-weight: 900; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; }}

                @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}

                .shaking-text {{
                    animation: textVibe 0.18s infinite alternate ease-in-out;
                }}
                @keyframes textVibe {{
                    0% {{ transform: translate(0px, 0px) rotate(0deg); }}
                    25% {{ transform: translate(-2px, 1px) rotate(-0.5deg); }}
                    50% {{ transform: translate(2px, -2px) rotate(0.8deg); }}
                    75% {{ transform: translate(-1px, -1px) rotate(-0.3deg); }}
                    100% {{ transform: translate(1px, 2px) rotate(0.5deg); }}
                }}

                .status-header {{ font-size: 14px; font-weight: 800; margin-bottom: 2px; letter-spacing: 1px; text-shadow: 0 2px 6px rgba(0,0,0,0.9); }}
                .desc-text {{ font-size: 11px; color: #f3e8ff; margin-top: 1px; text-shadow: 0 2px 8px rgba(0,0,0,0.9); }}
                .price-text {{ font-size: 13px; font-weight: 800; color: #fbbf24; margin-top: 2px; text-shadow: 0 0 15px rgba(0,0,0,0.9); }}
                .cost-text {{ font-size: 10px; font-weight: 700; color: #f87171; margin-top: 1px; text-shadow: 0 0 10px rgba(0,0,0,0.9); }}
            </style>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
        </head>
        <body>
            <div id="container"></div>

            <div id="cinematicUi" class="cinematic-ui">
                <div id="statusText" class="status-header">READY</div>
                <div id="mainTitle" class="title-tier-{tier}">{card_title}</div>
                <div id="descText" class="desc-text">{card_desc}</div>
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

                const status = '{status}';
                const statusText = document.getElementById('statusText');
                
                const tierColor = '{card_color}';
                let statusColor = "#38bdf8";
                let particleSize = 0.25;
                let particleSpeed = 0.8;
                let glowIntensity = 12;

                if (status === "CRITICAL") {{
                    statusText.innerText = "⚡ CRITICAL HIT!! (+2단계 이상 대성공) ⚡";
                    statusColor = "#ffffff"; 
                    particleSize = 0.45;
                    particleSpeed = 2.0;
                    glowIntensity = 30;
                }} else if (status === "SUCCESS") {{
                    statusText.innerText = "✨ SUCCESS (성공) ✨";
                    statusColor = tierColor;
                    particleSize = 0.3;
                    particleSpeed = 1.2;
                    glowIntensity = 18;
                }} else if (status === "SHIELD_SAVED") {{
                    statusText.innerText = "🛡️ SHIELD PROTECTED! (방어 성공) 🛡️";
                    statusColor = "#60a5fa";
                }} else if (status === "DESTROYED") {{
                    statusText.innerText = "💥 DESTROYED (파괴됨) 💥";
                    statusColor = "#ef4444";
                    particleSpeed = 1.0;
                }} else if (status === "FAILED") {{
                    statusText.innerText = "🔻 FAILED (단계 하락) 🔻";
                    statusColor = "#64748b";
                    particleSpeed = 0.4;
                    glowIntensity = 4;
                }} else if (status === "HOLD") {{
                    statusText.innerText = "🔒 HOLD (단계 유지) 🔒";
                    statusColor = "#94a3b8";
                    particleSpeed = 0.6;
                }} else {{
                    statusText.innerText = "READY";
                }}
                
                statusText.style.color = statusColor;

                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 0.1, 1000);
                camera.position.set(0, -0.2, 9.5);

                const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                renderer.setSize(window.innerWidth, window.innerHeight);
                renderer.setPixelRatio(window.devicePixelRatio);
                renderer.shadowMap.enabled = true;
                document.getElementById('container').appendChild(renderer.domElement);

                const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
                scene.add(ambientLight);

                const mainLight = new THREE.DirectionalLight(0xffffff, 2.0);
                mainLight.position.set(5, 8, 5);
                scene.add(mainLight);

                const pointLight = new THREE.PointLight(statusColor, glowIntensity, 35);
                pointLight.position.set(0, 1.5, 3);
                scene.add(pointLight);

                const particleCount = 500;
                const particleGeo = new THREE.BufferGeometry();
                const particlePositions = new Float32Array(particleCount * 3);
                const particleVelocities = [];

                for(let i=0; i<particleCount; i++) {{
                    particlePositions[i*3] = (Math.random() - 0.5) * 5.0;
                    particlePositions[i*3 + 1] = -3.2 + Math.random() * 2.0;
                    particlePositions[i*3 + 2] = (Math.random() - 0.5) * 5.0;
                    
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
                    opacity: status === "FAILED" ? 0.25 : 0.75,
                    blending: THREE.AdditiveBlending,
                    depthWrite: false
                }});
                const particleSystem = new THREE.Points(particleGeo, particleMat);
                scene.add(particleSystem);

                const objectGroup = new THREE.Group();
                objectGroup.position.y = -0.3;

                let baseGeo;
                const lvl = {current_level};

                if (lvl <= 2) {{
                    baseGeo = new THREE.TetrahedronGeometry(2.4);
                }} else if (lvl <= 5) {{
                    baseGeo = new THREE.BoxGeometry(2.2, 2.2, 2.2);
                }} else if (lvl <= 8) {{
                    baseGeo = new THREE.CylinderGeometry(2.0, 2.0, 2.5, 5);
                }} else if (lvl <= 11) {{
                    baseGeo = new THREE.CylinderGeometry(2.0, 2.0, 2.5, 6);
                }} else if (lvl <= 14) {{
                    baseGeo = new THREE.CylinderGeometry(2.0, 2.0, 2.5, 7);
                }} else if (lvl <= 17) {{
                    baseGeo = new THREE.CylinderGeometry(2.0, 2.0, 2.5, 8);
                }} else if (lvl == 18) {{
                    baseGeo = new THREE.OctahedronGeometry(2.6);
                }} else if (lvl == 19) {{
                    baseGeo = new THREE.DodecahedronGeometry(2.5);
                }} else if (lvl == 20) {{
                    baseGeo = new THREE.IcosahedronGeometry(2.5);
                }} else if (lvl == 21) {{
                    baseGeo = new THREE.ConeGeometry(2.2, 3.2, 6);
                }} else if (lvl == 22) {{
                    baseGeo = new THREE.TorusGeometry(1.8, 0.7, 16, 32);
                }} else if (lvl == 23) {{
                    baseGeo = new THREE.TorusKnotGeometry(1.4, 0.5, 64, 16, 2, 3);
                }} else if (lvl == 24) {{
                    baseGeo = new THREE.CylinderGeometry(0.5, 2.2, 3.0, 12);
                }} else if (lvl == 25) {{
                    baseGeo = new THREE.SphereGeometry(2.3, 16, 16);
                }} else if (lvl == 26) {{
                    baseGeo = new THREE.ConeGeometry(2.5, 3.5, 8);
                }} else if (lvl == 27) {{
                    baseGeo = new THREE.TorusKnotGeometry(1.5, 0.6, 96, 24, 3, 4);
                }} else if (lvl == 28) {{
                    baseGeo = new THREE.IcosahedronGeometry(2.6, 1);
                }} else if (lvl == 29) {{
                    baseGeo = new THREE.DodecahedronGeometry(2.7, 1);
                }} else {{
                    baseGeo = new THREE.TorusKnotGeometry(1.6, 0.6, 128, 32, 2, 5);
                }}

                const outerMat = new THREE.MeshPhysicalMaterial({{
                    color: tierColor,
                    emissive: status === "SUCCESS" || status === "CRITICAL" ? statusColor : "#111111",
                    emissiveIntensity: status === "SUCCESS" ? 0.4 : (status === "CRITICAL" ? 0.7 : 0.1),
                    metalness: 0.85,
                    roughness: 0.2,
                    transmission: 0.5,
                    transparent: true,
                    opacity: status === "FAILED" ? 0.55 : 0.92,
                    wireframe: false
                }});
                const outerMesh = new THREE.Mesh(baseGeo, outerMat);
                objectGroup.add(outerMesh);

                const coreGeo = new THREE.SphereGeometry(1.2, 32, 32);
                const coreMat = new THREE.MeshPhysicalMaterial({{
                    color: 0xffffff,
                    emissive: statusColor,
                    emissiveIntensity: status === "SUCCESS" || status === "CRITICAL" ? 2.5 : 1.0,
                    roughness: 0.1,
                    metalness: 0.9,
                    transmission: 0.7
                }});
                const coreMesh = new THREE.Mesh(coreGeo, coreMat);
                objectGroup.add(coreMesh);

                scene.add(objectGroup);

                uiElement.classList.add('visible');

                if (status === "DESTROYED") {{
                    outerMesh.visible = false;
                    coreMesh.visible = false;

                    const shardCount = 45;
                    const shards = [];
                    const shardGroup = new THREE.Group();

                    for(let i=0; i<shardCount; i++) {{
                        const sGeo = new THREE.BoxGeometry(0.35 + Math.random()*0.3, 0.35 + Math.random()*0.3, 0.35 + Math.random()*0.3);
                        const sMat = new THREE.MeshStandardMaterial({{
                            color: tierColor,
                            roughness: 0.3,
                            metalness: 0.8,
                            emissive: "#ef4444",
                            emissiveIntensity: 0.8
                        }});
                        const shard = new THREE.Mesh(sGeo, sMat);
                        
                        shard.position.set(0, 0, 0);
                        
                        const u = Math.random();
                        const v = Math.random();
                        const theta = u * 2.0 * Math.PI;
                        const phi = Math.acos(2.0 * v - 1.0);
                        const speed = 3.5 + Math.random() * 4.0;
                        
                        shard.userData = {{
                            vx: speed * Math.sin(phi) * Math.cos(theta),
                            vy: speed * Math.sin(phi) * Math.sin(theta),
                            vz: speed * Math.cos(phi),
                            rx: (Math.random() - 0.5) * 15,
                            ry: (Math.random() - 0.5) * 15
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
                }} else if (status === "CRITICAL") {{
                    gsap.fromTo(objectGroup.scale, {{x: 0.2, y: 0.2, z: 0.2}}, {{x: 1.25, y: 1.25, z: 1.25, duration: 0.5, ease: "power2.out"}});
                    gsap.to(objectGroup.scale, {{x: 1, y: 1, z: 1, duration: 0.3, delay: 0.5}});
                }} else if (status === "SUCCESS") {{
                    gsap.fromTo(objectGroup.scale, {{x: 0.85, y: 0.85, z: 0.85}}, {{x: 1.1, y: 1.1, z: 1.1, duration: 0.3, yoyo: true, repeat: 1, ease: "power1.out"}});
                }} else if (status === "FAILED") {{
                    gsap.fromTo(objectGroup.scale, {{x: 1.02, y: 1.02, z: 1.02}}, {{x: 0.95, y: 0.95, z: 0.95, duration: 0.3, ease: "power1.out"}});
                }} else if (status === "SHIELD_SAVED") {{
                    gsap.fromTo(objectGroup.scale, {{x: 1.2, y: 1.2, z: 1.2}}, {{x: 1, y: 1, z: 1, duration: 0.4, ease: "back.out(2)"}});
                }}

                const clock = new THREE.Clock();

                function animate() {{
                    requestAnimationFrame(animate);
                    const time = clock.getElapsedTime();

                    if (status !== "DESTROYED") {{
                        const rotSpeed = status === "FAILED" ? 0.4 : (status === "SUCCESS" || status === "CRITICAL" ? 1.1 : 0.6);
                        outerMesh.rotation.x = time * (0.5 * rotSpeed);
                        outerMesh.rotation.y = time * (0.7 * rotSpeed);
                        coreMesh.rotation.x = -time * (1.1 * rotSpeed);
                        coreMesh.rotation.y = -time * (1.4 * rotSpeed);
                        objectGroup.rotation.y = Math.sin(time * 0.7) * 0.2;
                    }}

                    const positions = particleGeo.attributes.position.array;
                    for(let i=0; i<particleCount; i++) {{
                        positions[i*3] += particleVelocities[i].x;
                        positions[i*3 + 1] += particleVelocities[i].y;
                        positions[i*3 + 2] += particleVelocities[i].z;

                        if(positions[i*3 + 1] > 4.0) {{
                            positions[i*3 + 1] = -3.2;
                            positions[i*3] = (Math.random() - 0.5) * 5.0;
                            positions[i*3 + 2] = (Math.random() - 0.5) * 5.0;
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

components.html(three_js_code, height=500, scrolling=False)
