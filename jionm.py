import random
import sqlite3
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 0. SQLite DB 초기화 (랭킹용)
# -----------------------------------------------------------------------------
DB_NAME = "ranking.db"


def init_db():
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()
  c.execute("""
        CREATE TABLE IF NOT EXISTS rankings (
            username TEXT PRIMARY KEY,
            level INTEGER,
            money REAL
        )
    """)
  conn.commit()
  conn.close()


init_db()


def save_score_to_db(username, level, money):
  if not username:
    return
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()
  c.execute("SELECT level, money FROM rankings WHERE username = ?", (username,))
  row = c.fetchone()
  if row is None:
    c.execute(
        "INSERT INTO rankings (username, level, money) VALUES (?, ?, ?)",
        (username, level, money),
    )
  else:
    if level > row[0] or (level == row[0] and money > row[1]):
      c.execute(
          "UPDATE rankings SET level = ?, money = ? WHERE username = ?",
          (level, money, username),
      )
  conn.commit()
  conn.close()


def get_leaderboard():
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()
  c.execute(
      "SELECT username, level, money FROM rankings ORDER BY level DESC, money"
      " DESC LIMIT 10"
  )
  data = c.fetchall()
  conn.close()
  return data


# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 (와이드 모드)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - FANTASY CITY EDITION", page_icon="🏰", layout="wide"
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
if "username" not in st.session_state:
  st.session_state.username = "지온러"
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


def enhance():
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
    st.session_state.tears += 1
  elif r < destroy_limit:
    if st.session_state.shield > 0:
      st.session_state.shield -= 1
      st.session_state.status = "SHIELD_SAVED"
      st.session_state.tears += 1
    else:
      st.session_state.level = 0
      st.session_state.status = "DESTROYED"
      st.session_state.tears += 2
  else:
    st.session_state.status = "HOLD"
    st.session_state.tears += 1

  save_score_to_db(
      st.session_state.username, st.session_state.level, st.session_state.money
  )


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

  save_score_to_db(
      st.session_state.username, st.session_state.level, st.session_state.money
  )


# -----------------------------------------------------------------------------
# 6. 테마 CSS (대규모 UI 개편)
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at center, #090d16 0%, #020408 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 98% !important;
    }
    .game-panel {
        background: rgba(13, 20, 36, 0.75);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }
    .stat-card {
        background: rgba(18, 27, 48, 0.85);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(245, 158, 11, 0.3);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }
    .stat-title {
        font-size: 13px;
        font-weight: 600;
        color: #fde68a;
        margin-bottom: 2px;
    }
    .stat-value {
        font-size: 18px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 8px rgba(245, 158, 11, 0.4);
    }
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease !important;
        border: 1px solid rgba(217, 119, 6, 0.5) !important;
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.7), rgba(217, 119, 6, 0.7)) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(217, 119, 6, 0.8);
        border-color: rgba(255, 255, 255, 0.8) !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. 3단 레이아웃 구성 (좌측: 정보/랭킹, 중앙: 3D시각화 및 버튼, 우측: 상점 및 유틸)
# -----------------------------------------------------------------------------
col_left, col_center, col_right = st.columns([2.2, 5.6, 2.2], gap="medium")

with col_left:
  st.markdown('<div class="game-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='margin:0 0 10px 0; font-size: 16px; color:#fde68a;'>👤 유저"
      " 프로필</h3>",
      unsafe_allow_html=True,
  )
  user_input = st.text_input(
      "닉네임 설정", value=st.session_state.username, max_chars=10
  )
  if user_input != st.session_state.username:
    st.session_state.username = user_input
    save_score_to_db(
        st.session_state.username, st.session_state.level, st.session_state.money
    )
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown('<div class="game-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='margin:0 0 10px 0; font-size: 16px; color:#fde68a;'>🏆 명예의"
      " 전당 (Top 10)</h3>",
      unsafe_allow_html=True,
  )
  leaderboard_data = get_leaderboard()
  if leaderboard_data:
    rank_html = (
        "<table style='width:100%; font-size:12px; color:#f8fafc; border-collapse:"
        " collapse;'>"
        "<tr style='border-bottom: 1px solid rgba(255,255,255,0.2); "
        "color:#fde68a;'><th>순위</th><th>닉네임</th><th>단계</th></tr>"
    )
    for idx, (uname, lvl, mny) in enumerate(leaderboard_data, 1):
      crown = (
          "🥇" if idx == 1 else ("🥈" if idx == 2 else ("🥉" if idx == 3 else ""))
      )
      rank_html += f"<tr style='border-bottom: 1px solid rgba(255,255,255,0.05); text-align:center;'><td style='padding:5px;'>{crown} {idx}위</td><td style='padding:5px;'>{uname}</td><td style='padding:5px; font-weight:bold; color:#34d399;'>{lvl}단계</td></tr>"
    rank_html += "</table>"
    st.markdown(rank_html, unsafe_allow_html=True)
  else:
    st.caption("랭킹 데이터 없음")
  st.markdown("</div>", unsafe_allow_html=True)

with col_center:
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
            #holdFlashOverlay {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(56, 189, 248, 0.5);
                box-shadow: inset 0 0 100px rgba(14, 165, 233, 0.8);
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
                bottom: 15px; 
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                text-align: center;
                z-index: 100;
                pointer-events: none;
            }}

            .title-tier-1 {{ font-size: 32px; font-weight: 900; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
            .title-tier-2 {{ font-size: 36px; font-weight: 900; color: #f59e0b; text-shadow: 0 0 25px #f59e0b; }}
            .title-tier-3 {{ font-size: 40px; font-weight: 900; color: #ef4444; text-shadow: 0 0 30px #ef4444; }}
            .title-tier-4 {{ font-size: 44px; font-weight: 900; color: #c084fc; text-shadow: 0 0 35px #c084fc; }}
            .title-tier-5 {{ font-size: 48px; font-weight: 900; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .title-tier-6 {{ font-size: 52px; font-weight: 900; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

            .status-header {{ font-size: 18px; font-weight: 800; margin-bottom: 4px; letter-spacing: 2px; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }}
            .desc-text {{ font-size: 14px; color: #f3e8ff; margin-top: 4px; text-shadow: 0 2px 8px rgba(0,0,0,0.9); }}
            .price-text {{ font-size: 18px; font-weight: 800; color: #fbbf24; margin-top: 4px; text-shadow: 0 0 15px rgba(0,0,0,0.9); }}
            .cost-text {{ font-size: 14px; font-weight: 700; color: #f87171; margin-top: 2px; text-shadow: 0 0 12px rgba(0,0,0,0.9); }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="redFlashOverlay"></div>
        <div id="failFlashOverlay"></div>
        <div id="holdFlashOverlay"></div>
        <div id="shieldFlashOverlay"></div>
        <div id="critFlashOverlay"></div>
        <div id="successFlashOverlay"></div>
        <div id="container"></div>

        <div class="cinematic-ui">
            <div id="statusText" class="status-header">READY</div>
            <div class="title-tier-{tier}">{card_title}</div>
            <div class="desc-text">"{card_desc}"</div>
            <div class="price-text">예상 가치: {card_price}</div>
            <div class="cost-text">필요 강화 비용: {current_cost}</div>
        </div>

        <script>
            const status = "{status}";
            const statusText = document.getElementById('statusText');
            const flashOverlay = document.getElementById('redFlashOverlay');
            const failOverlay = document.getElementById('failFlashOverlay');
            const holdOverlay = document.getElementById('holdFlashOverlay');
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
            }} else if (status === "HOLD") {{
                statusText.innerText = "🔒 ENHANCE HOLD (단계 유지) 🔒";
                statusText.style.color = "#38bdf8";
            }}

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0.3, 9.0);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.getElementById('container').appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
            scene.add(ambientLight);

            const dirLight = new THREE.DirectionalLight(0xffffff, 1.8);
            dirLight.position.set(5, 8, 5);
            scene.add(dirLight);

            const cardPointLight = new THREE.PointLight("{card_color}", 8, 25);
            cardPointLight.position.set(0, 2, 4);
            scene.add(cardPointLight);

            const bgGroup = new THREE.Group();
            const ringGeo1 = new THREE.TorusGeometry(5.5, 0.04, 16, 100);
            const ringMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", emissive: "{card_color}", emissiveIntensity: 1.2, roughness: 0.1 }});
            const spaceRing1 = new THREE.Mesh(ringGeo1, ringMat);
            spaceRing1.rotation.x = Math.PI / 3;
            bgGroup.add(spaceRing1);
            scene.add(bgGroup);

            const cardGroup = new THREE.Group();
            const outerFrameGeo = new THREE.BoxGeometry(3.6, 5.2, 0.2);
            const outerFrameMat = new THREE.MeshStandardMaterial({{ color: 0xffd700, metalness: 1.0, roughness: 0.1, emissive: "{card_color}", emissiveIntensity: 0.4 }});
            const outerFrame = new THREE.Mesh(outerFrameGeo, outerFrameMat);
            cardGroup.add(outerFrame);

            const bodyGeo = new THREE.BoxGeometry(3.0, 3.0, 0.23);
            const bodyMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", metalness: 0.85, roughness: 0.15, emissive: "{card_color}", emissiveIntensity: 0.6 }});
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            body.position.y = 0.75;
            cardGroup.add(body);

            const coreGeo = new THREE.IcosahedronGeometry(0.8, 0);
            const coreMat = new THREE.MeshStandardMaterial({{ color: 0xffffff, emissive: "{card_color}", emissiveIntensity: 1.8, roughness: 0.0, metalness: 1.0 }});
            const core = new THREE.Mesh(coreGeo, coreMat);
            core.position.set(0, 0.75, 0.2);
            cardGroup.add(core);

            scene.add(cardGroup);

            if (status === "CRITICAL") {{
                gsap.fromTo(critOverlay, {{ opacity: 0.9 }}, {{ opacity: 0, duration: 1.0, ease: "power2.out" }});
            }} else if (status === "SUCCESS") {{
                gsap.fromTo(successOverlay, {{ opacity: 0.7 }}, {{ opacity: 0, duration: 0.8, ease: "power2.out" }});
            }} else if (status === "DESTROYED") {{
                gsap.fromTo(flashOverlay, {{ opacity: 0.85 }}, {{ opacity: 0, duration: 1.2, ease: "power2.out" }});
                cardGroup.visible = false;
            }}

            const clock = new THREE.Clock();
            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();
                spaceRing1.rotation.z = time * 0.2;
                if (cardGroup.visible) {{
                    cardGroup.rotation.y = Math.sin(time * 0.8) * 0.2;
                    cardGroup.position.y = Math.sin(time * 1.5) * 0.1 + 0.1;
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

  components.html(three_js_code, height=420, scrolling=False)

  # 중앙 하단 독립 강화/판매 버튼 구역 (여백 최소화 및 직관적 배치)
  btn_col1, btn_col2 = st.columns(2, gap="small")
  with btn_col1:
    if st.button(
        "🔥 강화 실행하기",
        use_container_width=True,
        disabled=(st.session_state.level >= 30),
    ):
      enhance()
      if st.session_state.status == "NOT_ENOUGH_MONEY":
        st.error("강화 비용 부족!")
      else:
        st.rerun()
  with btn_col2:
    if st.button(
        "💰 현재 냄새 판매",
        use_container_width=True,
        disabled=(st.session_state.level == 0),
    ):
      sell()
      st.rerun()

with col_right:
  st.markdown('<div class="game-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='margin:0 0 10px 0; font-size: 16px; color:#fde68a;'>🛒 상점 및"
      " 유틸</h3>",
      unsafe_allow_html=True,
  )

  tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])
  with tab_shop1:
    current_shield_cost = get_shield_cost(st.session_state.level)
    st.caption(
        f"파괴 방지권 (보유 2개 제한)\n(20단계 이상 구매 가능)\n가격:"
        f" {format_gold(current_shield_cost)}"
    )
    can_buy_shield = st.session_state.level >= 20 and st.session_state.shield < 2
    if st.button(
        "방지권 구입", use_container_width=True, disabled=not can_buy_shield
    ):
      if st.session_state.level < 20:
        st.warning("20단계 이상부터 구매 가능합니다.")
      elif st.session_state.shield >= 2:
        st.warning("최대 2개까지만 보유 가능합니다.")
      elif st.session_state.money >= current_shield_cost:
        st.session_state.money -= current_shield_cost
        st.session_state.shield += 1
        st.success("구매 완료!")
        save_score_to_db(
            st.session_state.username,
            st.session_state.level,
            st.session_state.money,
        )
        st.rerun()
      else:
        st.error("금액 부족")

  with tab_shop2:
    st.caption("눈물 20개로 1단계 확정 상승")
    if st.button("확정 상승 교환", use_container_width=True):
      if st.session_state.tears >= 20 and st.session_state.level < 30:
        st.session_state.tears -= 20
        st.session_state.level += 1
        st.session_state.status = "SUCCESS"
        st.success("강화 성공!")
        save_score_to_db(
            st.session_state.username,
            st.session_state.level,
            st.session_state.money,
        )
        st.rerun()
      else:
        st.error("조건 미달")
  st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 8. 하단 고정 대시보드 (컴팩트 스탯 바)
# -----------------------------------------------------------------------------
st.write("")
b_col1, b_col2, b_col3, b_col4 = st.columns(4, gap="small")

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
            <div class="stat-title">🛡️ 파괴 방지권</div>
            <div class="stat-value">{st.session_state.shield} / 2개</div>
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
  if st.session_state.level < 30:
    sp, down_p, dp, hold_p = PROB_TABLE[st.session_state.level]
    prob_str = f"성공:{sp}% | 하락:{down_p}%<br>파괴:{dp}% | 유지:{hold_p}%"
  else:
    prob_str = "최고 단계 도달 완료"

  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">📊 현재 단계 확률</div>
            <div class="stat-value" style="font-size: 11px; line-height: 1.2;">{prob_str}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
