import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 0. 게임 컨셉
# -----------------------------------------------------------------------------
# "지온 코어 헌터"
#  - 기존 "지온냄새 강화하기"의 강화(가챠) 시스템을 "코어 강화"로 재구성.
#  - 코어를 강화해서 얻은 전투력(공격력/치명타/체력)으로 지온 세계관의 보스를
#    메이플스토리 보스레이드 감성으로 3D(Three.js) 로 사냥한다.
#  - 보스 진행 순서: 지온 -> 지온맘 -> 지온왕 -> 자이온 -> 자이온맘 -> 자이온왕
#    (코어 티어가 오를수록 상위 보스에 도전할 수 있는 구조)
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="지온 코어 헌터 - CORE HUNTER",
    page_icon="⚔️",
    layout="wide",
)

# -----------------------------------------------------------------------------
# 1. 유틸리티 함수
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
      0: 300, 1: 300, 2: 500, 3: 500, 4: 1000, 5: 1500, 6: 2000, 7: 2000,
      8: 3000, 9: 5000, 10: 10900, 11: 20000, 12: 35000, 13: 55000,
      14: 100000, 15: 180000, 16: 300000, 17: 300000, 18: 500000,
      19: 800000, 20: 1500000, 21: 2500000, 22: 4000000, 23: 6500000,
      24: 10000000, 25: 16000000, 26: 25000000, 27: 40000000,
      28: 65000000, 29: 100000000, 30: 150000000,
  }
  return cost_table.get(level, 150000000)


def get_shield_cost(level):
  base_cost = get_enhance_cost(level)
  return max(50000, base_cost * 15)


def get_core_value(level):
  """코어를 분해(판매)했을 때 얻는 골드."""
  return int(level**2 * 4000 + level * 15000)


def get_tier(level):
  if level <= 4:
    return 1
  elif level <= 9:
    return 2
  elif level <= 14:
    return 3
  elif level <= 19:
    return 4
  elif level <= 24:
    return 5
  else:
    return 6


TIER_INFO = {
    1: {"name": "미개화 코어", "color": "#4a5568",
        "desc": "아직 잠들어 있는 코어. 지온의 기운이 희미하게 느껴진다."},
    2: {"name": "공명하는 코어", "color": "#3182ce",
        "desc": "코어 내부에서 낮고 묵직한 진동이 시작된다."},
    3: {"name": "각성한 코어", "color": "#b7791f",
        "desc": "코어가 스스로 빛을 내며 서서히 깨어난다."},
    4: {"name": "차원의 코어", "color": "#ff00ea",
        "desc": "차원의 틈새가 코어 표면에 어른거린다."},
    5: {"name": "자이온의 코어", "color": "#ff4500",
        "desc": "자이온의 권능 일부가 코어에 깃들었다."},
    6: {"name": "태초의 코어", "color": "#00ffff",
        "desc": "우주 창조 당시의 힘이 응축된 절대의 코어."},
}

PLAYER_SHAPES = {1: "tetra", 2: "box", 3: "cyl6", 4: "octa", 5: "dodeca", 6: "torusknot"}

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

# -----------------------------------------------------------------------------
# 2. 보스 데이터베이스
# -----------------------------------------------------------------------------
BOSS_DB = {
    1: {"name": "지온", "title": "대지의 파수꾼", "tier": 1, "hp": 1200, "atk": 25,
        "gold": 3000, "color": "#38a169", "shape": "tetra"},
    2: {"name": "지온맘", "title": "흙내음의 어머니", "tier": 2, "hp": 3500, "atk": 45,
        "gold": 12000, "color": "#3182ce", "shape": "box"},
    3: {"name": "지온왕", "title": "근원을 다스리는 자", "tier": 3, "hp": 9000, "atk": 75,
        "gold": 40000, "color": "#b7791f", "shape": "cyl8"},
    4: {"name": "자이온", "title": "차원을 넘어온 자", "tier": 4, "hp": 22000, "atk": 120,
        "gold": 150000, "color": "#ff00ea", "shape": "icosa"},
    5: {"name": "자이온맘", "title": "만물을 품는 어머니", "tier": 5, "hp": 55000, "atk": 190,
        "gold": 500000, "color": "#ff4500", "shape": "torusknot"},
    6: {"name": "자이온왕", "title": "태초의 절대자", "tier": 6, "hp": 140000, "atk": 300,
        "gold": 2000000, "color": "#00ffff", "shape": "torusknot2"},
}


def get_player_stats(level):
  tier = get_tier(level)
  atk = 20 + level * 35 + tier * 100
  crit_rate = min(0.6, 0.05 + level * 0.013)
  max_hp = 550 + level * 55 + tier * 100
  return atk, crit_rate, max_hp


# -----------------------------------------------------------------------------
# 3. 세션 상태 초기화
# -----------------------------------------------------------------------------
defaults = {
    "level": 0, "max_level": 0, "money": 1000000, "status": "READY",
    "shield": 0, "tears": 0, "pity_count": 0,
    "battle_boss": None, "battle_status": "IDLE", "battle_event": "NONE",
    "boss_hp": 0, "boss_max_hp": 0, "player_hp": 0, "player_max_hp": 0,
    "last_player_dmg": 0, "last_boss_dmg": 0, "last_was_crit": False,
    "kill_counts": {},
}
for k, v in defaults.items():
  if k not in st.session_state:
    st.session_state[k] = v

# -----------------------------------------------------------------------------
# 4. 코어 강화 로직
# -----------------------------------------------------------------------------


def run_core_enhance():
  curr = st.session_state.level
  if curr >= 30:
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
    if random.random() < CRITICAL_RATE and curr + 2 <= 30:
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
  if curr < 30:
    st.session_state.level += 1
    st.session_state.status = "SUCCESS"
    if st.session_state.level > st.session_state.max_level:
      st.session_state.max_level = st.session_state.level


def recycle_core():
  curr = st.session_state.level
  if curr == 0:
    return
  st.session_state.money += get_core_value(curr)
  st.session_state.level = 0
  st.session_state.status = "READY"


# -----------------------------------------------------------------------------
# 5. 보스 전투 로직
# -----------------------------------------------------------------------------


def start_battle(boss_id):
  boss = BOSS_DB[boss_id]
  _, _, max_hp = get_player_stats(st.session_state.level)
  st.session_state.battle_boss = boss_id
  st.session_state.boss_hp = boss["hp"]
  st.session_state.boss_max_hp = boss["hp"]
  st.session_state.player_hp = max_hp
  st.session_state.player_max_hp = max_hp
  st.session_state.battle_status = "ONGOING"
  st.session_state.battle_event = "START"


def attack():
  if st.session_state.battle_status != "ONGOING":
    return
  boss_id = st.session_state.battle_boss
  boss = BOSS_DB[boss_id]
  atk, crit_rate, _ = get_player_stats(st.session_state.level)

  is_crit = random.random() < crit_rate
  dmg = atk * random.uniform(0.85, 1.15)
  if is_crit:
    dmg *= 2.2
  dmg = int(dmg)

  st.session_state.boss_hp = max(0, st.session_state.boss_hp - dmg)
  st.session_state.last_player_dmg = dmg
  st.session_state.last_was_crit = is_crit

  if st.session_state.boss_hp <= 0:
    st.session_state.battle_status = "VICTORY"
    st.session_state.money += boss["gold"]
    st.session_state.kill_counts[boss_id] = st.session_state.kill_counts.get(boss_id, 0) + 1
    st.session_state.battle_event = "CRIT_VICTORY" if is_crit else "HIT_VICTORY"
    return

  boss_dmg = int(boss["atk"] * random.uniform(0.8, 1.3))
  st.session_state.player_hp = max(0, st.session_state.player_hp - boss_dmg)
  st.session_state.last_boss_dmg = boss_dmg

  if st.session_state.player_hp <= 0:
    st.session_state.battle_status = "DEFEAT"
    st.session_state.battle_event = "CRIT_DEFEAT" if is_crit else "HIT_DEFEAT"
  else:
    st.session_state.battle_event = "CRIT_CONTINUE" if is_crit else "HIT_CONTINUE"


def end_battle():
  st.session_state.battle_boss = None
  st.session_state.battle_status = "IDLE"
  st.session_state.battle_event = "NONE"


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
    .block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; max-width: 95% !important; }
    .element-container, .stMarkdown { background: transparent !important; }

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
    .boss-card {
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
        background: rgba(15, 23, 42, 0.6);
    }
    .boss-card.locked { opacity: 0.45; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h2 style='margin-bottom:0;'>⚔️ 지온 코어 헌터</h2>"
    "<p style='color:#94a3b8; margin-top:4px;'>코어를 강화해 힘을 키우고,"
    " 지온 → 지온맘 → 지온왕 → 자이온 → 자이온맘 → 자이온왕 순으로 보스를 사냥하세요.</p>",
    unsafe_allow_html=True,
)

tab_enhance, tab_battle = st.tabs(["🌌 코어 강화", "🐉 보스 사냥"])

# -----------------------------------------------------------------------------
# 7. 탭 1: 코어 강화
# -----------------------------------------------------------------------------
with tab_enhance:
  left_col, right_col = st.columns([2.2, 7.8], gap="medium")

  with left_col:
    st.markdown(
        "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🛠️ 시스템 설정</h4>",
        unsafe_allow_html=True,
    )
    dev_mode = st.toggle("💻 개발자 모드 활성화", value=False)

    st.markdown("<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

    s_col1, s_col2 = st.columns(2)
    with s_col1:
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px; color:#fde68a;'>💳 보유 골드</div>"
          f"<div style='font-size:15px; font-weight:800; color:#ffffff;'>{format_gold(st.session_state.money)}</div></div>",
          unsafe_allow_html=True,
      )
      st.write("")
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px; color:#fde68a;'>💧 눈물</div>"
          f"<div style='font-size:15px; font-weight:800; color:#ffffff;'>{st.session_state.tears} / 120개</div></div>",
          unsafe_allow_html=True,
      )
    with s_col2:
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px; color:#fde68a;'>🛡️ 방지권</div>"
          f"<div style='font-size:15px; font-weight:800; color:#ffffff;'>{st.session_state.shield} / 3개</div></div>",
          unsafe_allow_html=True,
      )
      st.write("")
      pity_left = PITY_MAX - st.session_state.pity_count
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px; color:#fde68a;'>✨ 자이온맘의 가호</div>"
          f"<div style='font-size:13px; font-weight:800; color:#ffffff;'>실패까지 <b>{pity_left}회</b></div></div>",
          unsafe_allow_html=True,
      )

    st.markdown("<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

    tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])
    with tab_shop1:
      current_shield_cost = get_shield_cost(st.session_state.level)
      st.markdown(
          f"<div style='font-size:14px; color:#cbd5e1; margin-bottom:8px;'>"
          f"<b>조건:</b> 18단계 이상 | <b>보유한도:</b> 최대 3개<br><b>가격:</b>"
          f" <span style='font-size:16px; font-weight:bold; color:#fde68a;'>{format_gold(current_shield_cost)}</span></div>",
          unsafe_allow_html=True,
      )
      can_buy_shield = st.session_state.level >= 18 and st.session_state.shield < 3
      if st.button("방지권 구매", use_container_width=True, disabled=not can_buy_shield):
        if st.session_state.money >= current_shield_cost:
          st.session_state.money -= current_shield_cost
          st.session_state.shield += 1
          st.success("파괴 방지권 구매 완료!")
          st.rerun()
        else:
          st.error("골드가 부족합니다.")

    with tab_shop2:
      if st.session_state.level >= 28:
        st.markdown(
            "<div style='font-size:14px; color:#ef4444; font-weight:700; margin-bottom:8px;'>"
            "⚠️ 28단계 이상부터는 신성한 기운으로 인해 눈물을 사용할 수 없습니다!</div>",
            unsafe_allow_html=True,
        )
      else:
        st.markdown(
            f"<div style='font-size:14px; color:#cbd5e1; margin-bottom:8px;'><b>효과:</b> 눈물 40개 소모"
            f" (50% 확률로 1~3단계 상승)<br><b>현재보유:</b> <span style='font-weight:bold; color:#38bdf8;'>"
            f"{st.session_state.tears} / 120개</span></div>",
            unsafe_allow_html=True,
        )
      can_use_tears = st.session_state.level < 28
      if st.button("눈물 기적 가동", use_container_width=True, disabled=not can_use_tears):
        if st.session_state.tears >= 40:
          st.session_state.tears -= 40
          if random.random() < 0.50:
            add_lvl = random.choice([1, 2, 3])
            st.session_state.level = min(30, st.session_state.level + add_lvl)
            st.session_state.status = "CRITICAL" if add_lvl >= 2 else "SUCCESS"
            if st.session_state.level > st.session_state.max_level:
              st.session_state.max_level = st.session_state.level
            st.success(f"눈물 기적 대성공! {add_lvl}단계 상승!")
          else:
            st.session_state.status = "FAILED"
            st.warning("눈물의 기적이 실패했습니다...")
          st.rerun()
        else:
          st.error("눈물 40개가 필요합니다.")

    st.markdown("<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🌌 코어 강화 제어</h4>",
        unsafe_allow_html=True,
    )

    if st.button("🔥 코어 강화 실행", use_container_width=True, disabled=(st.session_state.level >= 30)):
      cost = get_enhance_cost(st.session_state.level)
      if st.session_state.money < cost:
        st.error("강화 비용 부족!")
      else:
        run_core_enhance()
        st.rerun()

    if dev_mode:
      st.write("")
      if st.button("✨ [DEV] 무조건 성공", use_container_width=True, disabled=(st.session_state.level >= 30)):
        dev_force_success()
        st.rerun()

    st.write("")
    if st.button("💰 현재 코어 분해", use_container_width=True, disabled=(st.session_state.level == 0)):
      recycle_core()
      st.rerun()

    atk_p, crit_p, hp_p = get_player_stats(st.session_state.level)
    st.markdown("<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='font-size:13px; color:#cbd5e1;'>⚔️ 공격력: <b style='color:#fff'>{atk_p}</b><br>"
        f"💥 치명타 확률: <b style='color:#fff'>{crit_p*100:.1f}%</b><br>"
        f"❤️ 최대 체력: <b style='color:#fff'>{hp_p}</b></div>",
        unsafe_allow_html=True,
    )

  with right_col:
    current_level = st.session_state.level
    tier = get_tier(current_level)
    tier_data = TIER_INFO[tier]
    card_color = tier_data["color"]
    card_title = f"Lv.{current_level} · {tier_data['name']}"
    card_desc = tier_data["desc"]
    card_price = format_gold(get_core_value(current_level))
    current_cost = format_gold(get_enhance_cost(current_level))
    status = st.session_state.status

    three_js_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; overflow: hidden; background: transparent;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
            #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}
            .cinematic-ui {{
                position: absolute; bottom: 25px; left: 50%; transform: translateX(-50%);
                width: 100%; text-align: center; z-index: 100; pointer-events: none;
                opacity: 0; transition: opacity 0.4s ease-in-out;
            }}
            .cinematic-ui.visible {{ opacity: 1; }}
            .title-tier-1 {{ font-size: 28px; font-weight: 800; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
            .title-tier-2 {{ font-size: 32px; font-weight: 800; color: #f59e0b; text-shadow: 0 0 22px #f59e0b; }}
            .title-tier-3 {{ font-size: 36px; font-weight: 800; color: #ef4444; text-shadow: 0 0 25px #ef4444; }}
            .title-tier-4 {{ font-size: 40px; font-weight: 800; color: #c084fc; text-shadow: 0 0 28px #c084fc; }}
            .title-tier-5 {{ font-size: 44px; font-weight: 800; background: linear-gradient(90deg, #ff7e5f, #feb47b);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 12px rgba(255,126,95,0.6)); }}
            .title-tier-6 {{ font-size: 48px; font-weight: 800; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e);
                background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                animation: rainbow 1.5s linear infinite; filter: drop-shadow(0 0 15px rgba(255,255,255,0.8)); }}
            @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}
            .shaking-text {{ animation: textVibe 0.18s infinite alternate ease-in-out; }}
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
            <div id="priceText" class="price-text">코어 분해 가치: {card_price}</div>
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
                statusText.innerText = "⚡ COSMIC CRITICAL HIT!! (+2단계 대성공) ⚡";
                statusColor = "#ffffff"; particleSize = 0.55; particleSpeed = 2.5; glowIntensity = 35;
            }} else if (status === "PITY_SUCCESS") {{
                statusText.innerText = "✨ 자이온맘의 가호 발동! (천장 100% 성공) ✨";
                statusColor = "#fde68a"; particleSize = 0.45; particleSpeed = 2.0; glowIntensity = 30;
            }} else if (status === "SUCCESS") {{
                statusText.innerText = "✨ COSMIC SUCCESS (강화 성공) ✨";
                statusColor = tierColor; particleSize = 0.35; particleSpeed = 1.5; glowIntensity = 22;
            }} else if (status === "SHIELD_SAVED") {{
                statusText.innerText = "🛡️ SHIELD PROTECTED! (붕괴 방지 발동) 🛡️";
                statusColor = "#60a5fa";
            }} else if (status === "DESTROYED") {{
                statusText.innerText = "💥 CORE DESTROYED (코어 붕괴됨) 💥";
                statusColor = "#ef4444"; particleSpeed = 1.2;
            }} else if (status === "FAILED") {{
                statusText.innerText = "🔻 FAILED (에너지 하락) 🔻";
                statusColor = "#64748b"; particleSpeed = 0.5; glowIntensity = 6;
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
            const pointLight = new THREE.PointLight(statusColor, glowIntensity, 40);
            pointLight.position.set(0, 0, 3);
            scene.add(pointLight);

            const particleCount = 700;
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
                color: new THREE.Color(statusColor), size: particleSize, transparent: true,
                opacity: status === "FAILED" ? 0.3 : 0.9, blending: THREE.AdditiveBlending, depthWrite: false
            }});
            scene.add(new THREE.Points(particleGeo, particleMat));

            const objectGroup = new THREE.Group();
            objectGroup.position.y = -0.7;
            let baseGeo;
            const lvl = {current_level};
            if (lvl <= 2) {{ baseGeo = new THREE.TetrahedronGeometry(2.3); }}
            else if (lvl <= 5) {{ baseGeo = new THREE.BoxGeometry(2.1, 2.1, 2.1); }}
            else if (lvl <= 8) {{ baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 5); }}
            else if (lvl <= 11) {{ baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 6); }}
            else if (lvl <= 14) {{ baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 7); }}
            else if (lvl <= 17) {{ baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 8); }}
            else if (lvl == 18) {{ baseGeo = new THREE.OctahedronGeometry(2.5); }}
            else if (lvl == 19) {{ baseGeo = new THREE.DodecahedronGeometry(2.4); }}
            else if (lvl == 20) {{ baseGeo = new THREE.IcosahedronGeometry(2.4); }}
            else if (lvl == 21) {{ baseGeo = new THREE.ConeGeometry(2.1, 3.1, 6); }}
            else if (lvl == 22) {{ baseGeo = new THREE.TorusGeometry(1.7, 0.65, 16, 32); }}
            else if (lvl == 23) {{ baseGeo = new THREE.TorusKnotGeometry(1.4, 0.45, 64, 16, 2, 3); }}
            else if (lvl == 24) {{ baseGeo = new THREE.CylinderGeometry(0.5, 2.1, 2.9, 12); }}
            else if (lvl == 25) {{ baseGeo = new THREE.SphereGeometry(2.2, 16, 16); }}
            else if (lvl == 26) {{ baseGeo = new THREE.ConeGeometry(2.3, 3.3, 8); }}
            else if (lvl == 27) {{ baseGeo = new THREE.TorusKnotGeometry(1.5, 0.55, 96, 24, 3, 4); }}
            else if (lvl == 28) {{ baseGeo = new THREE.IcosahedronGeometry(2.5, 1); }}
            else if (lvl == 29) {{ baseGeo = new THREE.DodecahedronGeometry(2.6, 1); }}
            else {{ baseGeo = new THREE.TorusKnotGeometry(1.5, 0.55, 128, 32, 2, 5); }}

            const outerMat = new THREE.MeshPhysicalMaterial({{
                color: tierColor,
                emissive: status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? statusColor : "#111111",
                emissiveIntensity: status === "SUCCESS" ? 0.5 : (status === "CRITICAL" || status === "PITY_SUCCESS" ? 0.9 : 0.15),
                metalness: 0.9, roughness: 0.15, transmission: 0.6, transparent: true,
                opacity: status === "FAILED" ? 0.5 : 0.95,
            }});
            const outerMesh = new THREE.Mesh(baseGeo, outerMat);
            objectGroup.add(outerMesh);

            const coreMat = new THREE.MeshPhysicalMaterial({{
                color: 0xffffff, emissive: statusColor,
                emissiveIntensity: status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? 3.0 : 1.2,
                roughness: 0.05, metalness: 0.95, transmission: 0.8
            }});
            const coreMesh = new THREE.Mesh(new THREE.SphereGeometry(1.2, 32, 32), coreMat);
            objectGroup.add(coreMesh);
            scene.add(objectGroup);
            uiElement.classList.add('visible');

            if (status === "DESTROYED") {{
                outerMesh.visible = false; coreMesh.visible = false;
                const shardCount = 55;
                const shards = [];
                const shardGroup = new THREE.Group();
                shardGroup.position.y = -0.7;
                for(let i=0; i<shardCount; i++) {{
                    const sGeo = new THREE.BoxGeometry(0.3 + Math.random()*0.2, 0.3 + Math.random()*0.2, 0.3 + Math.random()*0.2);
                    const sMat = new THREE.MeshStandardMaterial({{ color: tierColor, roughness: 0.2, metalness: 0.9, emissive: "#ef4444", emissiveIntensity: 1.0 }});
                    const shard = new THREE.Mesh(sGeo, sMat);
                    shard.position.set(0, 0, 0);
                    const u = Math.random(); const v = Math.random();
                    const theta = u * 2.0 * Math.PI; const phi = Math.acos(2.0 * v - 1.0);
                    const speed = 4.0 + Math.random() * 5.0;
                    shard.userData = {{
                        vx: speed * Math.sin(phi) * Math.cos(theta), vy: speed * Math.sin(phi) * Math.sin(theta),
                        vz: speed * Math.cos(phi), rx: (Math.random() - 0.5) * 20, ry: (Math.random() - 0.5) * 20
                    }};
                    shardGroup.add(shard); shards.push(shard);
                }}
                scene.add(shardGroup);
                gsap.to(shardGroup.position, {{
                    duration: 1.2, ease: "power2.out",
                    onUpdate: function() {{
                        const progress = this.progress();
                        shards.forEach(s => {{
                            s.position.x += s.userData.vx * 0.02; s.position.y += s.userData.vy * 0.02 - 0.05;
                            s.position.z += s.userData.vz * 0.02; s.rotation.x += s.userData.rx * 0.02; s.rotation.y += s.userData.ry * 0.02;
                            s.material.opacity = 1.0 - progress; s.material.transparent = true;
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
                    outerMesh.rotation.x = time * (0.5 * rotSpeed); outerMesh.rotation.y = time * (0.75 * rotSpeed);
                    coreMesh.rotation.x = -time * (1.2 * rotSpeed); coreMesh.rotation.y = -time * (1.5 * rotSpeed);
                    objectGroup.rotation.y = Math.sin(time * 0.7) * 0.25;
                }}
                const positions = particleGeo.attributes.position.array;
                for(let i=0; i<particleCount; i++) {{
                    positions[i*3] += particleVelocities[i].x; positions[i*3 + 1] += particleVelocities[i].y; positions[i*3 + 2] += particleVelocities[i].z;
                    if(positions[i*3 + 1] > 3.0) {{
                        positions[i*3 + 1] = -5.0; positions[i*3] = (Math.random() - 0.5) * 7.0; positions[i*3 + 2] = (Math.random() - 0.5) * 7.0;
                    }}
                }}
                particleGeo.attributes.position.needsUpdate = true;
                renderer.render(scene, camera);
            }}
            animate();
            window.addEventListener('resize', () => {{
                camera.aspect = window.innerWidth / window.innerHeight; camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }});
        </script>
    </body>
    </html>
    """
    components.html(three_js_code, height=580, scrolling=False)

# -----------------------------------------------------------------------------
# 8. 탭 2: 보스 사냥
# -----------------------------------------------------------------------------
with tab_battle:
  atk, crit_rate, max_hp = get_player_stats(st.session_state.level)
  player_tier = get_tier(st.session_state.level)
  max_tier_reached = get_tier(st.session_state.max_level)

  if st.session_state.battle_status == "ONGOING":
    boss_id = st.session_state.battle_boss
    boss = BOSS_DB[boss_id]
    boss_pct = max(0, int(st.session_state.boss_hp / st.session_state.boss_max_hp * 100))
    player_pct = max(0, int(st.session_state.player_hp / st.session_state.player_max_hp * 100))

    battle_col1, battle_col2 = st.columns([7.8, 2.2], gap="medium")
    with battle_col1:
      battle_html = f"""
      <!DOCTYPE html>
      <html>
      <head>
        <style>
          body {{ margin:0; overflow:hidden; background:transparent;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
          #container {{ width:100vw; height:100vh; position:absolute; top:0; left:0; }}
          .hpbar-wrap {{ position:absolute; z-index:50; color:#fff; text-shadow:0 2px 6px rgba(0,0,0,0.9); }}
          .boss-hp {{ top:18px; left:50%; transform:translateX(-50%); width:60%; text-align:center; }}
          .player-hp {{ bottom:18px; left:18px; width:38%; }}
          .hp-name {{ font-size:15px; font-weight:800; margin-bottom:4px; }}
          .hp-track {{ width:100%; height:16px; border-radius:8px; background:rgba(255,255,255,0.15); overflow:hidden; border:1px solid rgba(255,255,255,0.3); }}
          .hp-fill {{ height:100%; border-radius:8px; transition:width 0.4s ease; }}
          .hp-fill.boss {{ background: linear-gradient(90deg, #ef4444, #f97316); }}
          .hp-fill.player {{ background: linear-gradient(90deg, #38bdf8, #22d3ee); }}
          .hp-num {{ font-size:11px; margin-top:2px; color:#e2e8f0; }}
          .float-dmg {{ position:absolute; z-index:60; font-weight:900; font-size:26px; text-shadow:0 0 10px rgba(0,0,0,0.9); pointer-events:none; opacity:0; }}
          .center-banner {{ position:absolute; top:42%; left:50%; transform:translate(-50%,-50%); z-index:70; text-align:center; opacity:0; pointer-events:none; }}
          .center-banner .big {{ font-size:44px; font-weight:900; text-shadow: 0 0 25px rgba(0,0,0,0.9); }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
      </head>
      <body>
        <div id="container"></div>
        <div class="hpbar-wrap boss-hp">
          <div class="hp-name" style="color:{boss['color']}">{boss['name']} · {boss['title']}</div>
          <div class="hp-track"><div id="bossFill" class="hp-fill boss" style="width:{boss_pct}%;"></div></div>
          <div class="hp-num">{st.session_state.boss_hp:,} / {st.session_state.boss_max_hp:,}</div>
        </div>
        <div class="hpbar-wrap player-hp">
          <div class="hp-name" style="color:{TIER_INFO[player_tier]['color']}">내 코어 (Lv.{st.session_state.level})</div>
          <div class="hp-track"><div id="playerFill" class="hp-fill player" style="width:{player_pct}%;"></div></div>
          <div class="hp-num">{st.session_state.player_hp:,} / {st.session_state.player_max_hp:,}</div>
        </div>
        <div id="bossDmgText" class="float-dmg" style="top:30%; left:68%;"></div>
        <div id="playerDmgText" class="float-dmg" style="top:55%; left:20%;"></div>
        <div id="centerBanner" class="center-banner"><div class="big" id="bannerText"></div></div>

        <script>
          const event = "{st.session_state.battle_event}";
          const pDmg = {st.session_state.last_player_dmg};
          const bDmg = {st.session_state.last_boss_dmg};
          const bossColor = "{boss['color']}";
          const playerColor = "{TIER_INFO[player_tier]['color']}";
          const bossShape = "{boss['shape']}";
          const playerShape = "{PLAYER_SHAPES[player_tier]}";

          const scene = new THREE.Scene();
          const camera = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 1000);
          camera.position.set(0, 1.2, 11);
          const renderer = new THREE.WebGLRenderer({{ antialias:true, alpha:true }});
          renderer.setSize(window.innerWidth, window.innerHeight);
          renderer.setPixelRatio(window.devicePixelRatio);
          document.getElementById('container').appendChild(renderer.domElement);

          scene.add(new THREE.AmbientLight(0xffffff, 0.85));
          const dLight = new THREE.DirectionalLight(0xffffff, 2.2);
          dLight.position.set(4, 8, 6);
          scene.add(dLight);
          const bossLight = new THREE.PointLight(bossColor, 20, 30);
          bossLight.position.set(3, 1, 3);
          scene.add(bossLight);
          const playerLight = new THREE.PointLight(playerColor, 15, 30);
          playerLight.position.set(-3, 1, 3);
          scene.add(playerLight);

          function getGeo(shape, scale) {{
            switch(shape) {{
              case "tetra": return new THREE.TetrahedronGeometry(1.3 * scale);
              case "box": return new THREE.BoxGeometry(1.6*scale, 1.6*scale, 1.6*scale);
              case "cyl6": return new THREE.CylinderGeometry(1.2*scale, 1.2*scale, 1.7*scale, 6);
              case "cyl8": return new THREE.CylinderGeometry(1.2*scale, 1.2*scale, 1.7*scale, 8);
              case "octa": return new THREE.OctahedronGeometry(1.5*scale);
              case "icosa": return new THREE.IcosahedronGeometry(1.5*scale, 0);
              case "dodeca": return new THREE.DodecahedronGeometry(1.4*scale, 0);
              case "torusknot": return new THREE.TorusKnotGeometry(1.0*scale, 0.35*scale, 100, 16);
              case "torusknot2": return new THREE.TorusKnotGeometry(1.1*scale, 0.4*scale, 128, 24, 2, 5);
              default: return new THREE.SphereGeometry(1.3*scale, 24, 24);
            }}
          }}

          const bossGroup = new THREE.Group();
          bossGroup.position.set(3.2, 0.3, 0);
          const bossMat = new THREE.MeshPhysicalMaterial({{ color: bossColor, emissive: bossColor, emissiveIntensity: 0.35,
            metalness: 0.85, roughness: 0.2, transmission: 0.35, transparent: true, opacity: 0.97 }});
          const bossMesh = new THREE.Mesh(getGeo(bossShape, 1.9), bossMat);
          bossGroup.add(bossMesh);
          scene.add(bossGroup);

          const playerGroup = new THREE.Group();
          playerGroup.position.set(-3.2, -0.3, 1.5);
          const playerMat = new THREE.MeshPhysicalMaterial({{ color: playerColor, emissive: playerColor, emissiveIntensity: 0.45,
            metalness: 0.9, roughness: 0.15, transmission: 0.5, transparent: true, opacity: 0.97 }});
          const playerMesh = new THREE.Mesh(getGeo(playerShape, 1.0), playerMat);
          playerGroup.add(playerMesh);
          scene.add(playerGroup);

          function burst(position, color, count) {{
            const geo = new THREE.BufferGeometry();
            const pos = new Float32Array(count*3);
            const vel = [];
            for(let i=0;i<count;i++) {{
              pos[i*3]=position.x; pos[i*3+1]=position.y; pos[i*3+2]=position.z;
              const theta = Math.random()*Math.PI*2; const phi = Math.acos(2*Math.random()-1); const spd = 2+Math.random()*4;
              vel.push({{x: spd*Math.sin(phi)*Math.cos(theta), y: spd*Math.sin(phi)*Math.sin(theta), z: spd*Math.cos(phi)}});
            }}
            geo.setAttribute('position', new THREE.BufferAttribute(pos,3));
            const mat = new THREE.PointsMaterial({{ color: new THREE.Color(color), size:0.22, transparent:true, opacity:1, blending: THREE.AdditiveBlending, depthWrite:false }});
            const pts = new THREE.Points(geo, mat);
            scene.add(pts);
            gsap.to({{}}, {{ duration:0.7, onUpdate: function() {{
                const p = this.progress();
                const arr = geo.attributes.position.array;
                for(let i=0;i<count;i++) {{ arr[i*3]+=vel[i].x*0.03; arr[i*3+1]+=vel[i].y*0.03; arr[i*3+2]+=vel[i].z*0.03; }}
                geo.attributes.position.needsUpdate = true; mat.opacity = 1-p;
              }}, onComplete: function() {{ scene.remove(pts); }} }});
          }}

          function showFloat(id, text, color) {{
            const el = document.getElementById(id);
            el.innerText = text; el.style.color = color; el.style.opacity = 1;
            gsap.fromTo(el, {{ y:0, opacity:1 }}, {{ y:-50, opacity:0, duration:0.9, ease:"power1.out" }});
          }}

          function showBanner(text, color) {{
            const el = document.getElementById('bannerText');
            const wrap = document.getElementById('centerBanner');
            el.innerText = text; el.style.color = color;
            gsap.fromTo(wrap, {{ opacity:0, scale:0.5 }}, {{ opacity:1, scale:1.1, duration:0.4, ease:"back.out(2)" }});
            gsap.to(wrap, {{ opacity:0, duration:0.6, delay:1.2 }});
          }}

          const tl = gsap.timeline();
          if (event.includes("HIT") || event.includes("CRIT")) {{
            const isCrit = event.includes("CRIT");
            tl.to(playerGroup.position, {{ x: 0.6, duration: 0.28, ease: "power2.in" }})
              .call(() => {{
                burst(bossGroup.position, isCrit ? "#ffffff" : playerColor, isCrit ? 70 : 35);
                showFloat('bossDmgText', (isCrit ? "CRIT! -" : "-") + pDmg.toLocaleString(), isCrit ? "#fde68a" : "#f8fafc");
                gsap.to(bossMat, {{ emissiveIntensity: 2.2, duration: 0.1, yoyo:true, repeat:1 }});
                gsap.fromTo(bossGroup.rotation, {{ z: 0 }}, {{ z: 0.25, duration: 0.08, yoyo:true, repeat:3 }});
              }})
              .to(playerGroup.position, {{ x: -3.2, duration: 0.35, ease: "power2.out" }});

            if (event.includes("CONTINUE")) {{
              tl.to(bossGroup.position, {{ x: -0.6, duration: 0.3, ease: "power2.in" }}, "+=0.15")
                .call(() => {{
                  burst(playerGroup.position, bossColor, 30);
                  showFloat('playerDmgText', "-" + bDmg.toLocaleString(), "#f87171");
                  gsap.to(playerMat, {{ emissiveIntensity: 0.1, duration: 0.15, yoyo:true, repeat:1 }});
                }})
                .to(bossGroup.position, {{ x: 3.2, duration: 0.35, ease: "power2.out" }});
            }} else if (event.includes("VICTORY")) {{
              tl.call(() => {{
                showBanner("🏆 승리! " + "{boss['name']}" + " 처치!", "#fde68a");
                burst(bossGroup.position, bossColor, 120);
              }}, null, "+=0.1")
                .to(bossMesh.scale, {{ x:0.01, y:0.01, z:0.01, duration:0.5, ease:"power2.in" }}, "+=0.05");
            }} else if (event.includes("DEFEAT")) {{
              tl.to(bossGroup.position, {{ x: -0.6, duration: 0.3, ease: "power2.in" }}, "+=0.15")
                .call(() => {{
                  burst(playerGroup.position, bossColor, 40);
                  showFloat('playerDmgText', "-" + bDmg.toLocaleString(), "#f87171");
                  showBanner("💀 패배...", "#ef4444");
                }})
                .to(bossGroup.position, {{ x: 3.2, duration: 0.35, ease: "power2.out" }})
                .to(playerGroup.rotation, {{ z: 1.4, duration: 0.6, ease: "power2.out" }})
                .to(playerMat, {{ opacity: 0.25, duration: 0.6 }}, "<");
            }}
          }}

          const clock = new THREE.Clock();
          function animate() {{
            requestAnimationFrame(animate);
            const t = clock.getElapsedTime();
            bossGroup.rotation.y = t * 0.5;
            bossGroup.position.y = 0.3 + Math.sin(t*1.2)*0.15;
            playerGroup.rotation.y = -t * 0.6;
            playerGroup.position.y = -0.3 + Math.sin(t*1.4 + 1)*0.15;
            renderer.render(scene, camera);
          }}
          animate();
          window.addEventListener('resize', () => {{
            camera.aspect = window.innerWidth/window.innerHeight; camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
          }});
        </script>
      </body>
      </html>
      """
      components.html(battle_html, height=560, scrolling=False)

    with battle_col2:
      st.markdown(f"### {boss['name']}")
      st.caption(boss['title'])
      st.write("")
      if st.session_state.battle_status == "ONGOING":
        if st.button("⚔️ 공격!", use_container_width=True, key="attack_btn"):
          attack()
          st.rerun()
        if st.button("🏳️ 도망가기", use_container_width=True, key="flee_btn"):
          end_battle()
          st.rerun()
      elif st.session_state.battle_status == "VICTORY":
        st.success(f"승리! 보상 {format_gold(boss['gold'])} 획득")
        if st.button("확인", use_container_width=True, key="ok_win"):
          end_battle()
          st.rerun()
      elif st.session_state.battle_status == "DEFEAT":
        st.error("패배했습니다. 코어를 더 강화한 뒤 재도전하세요.")
        if st.button("확인", use_container_width=True, key="ok_lose"):
          end_battle()
          st.rerun()

  else:
    if st.session_state.battle_status in ("VICTORY", "DEFEAT") and st.session_state.battle_boss:
      # 안전장치: 전투 결과 화면에서 새로고침된 경우
      end_battle()

    st.markdown(
        f"<div style='margin-bottom:14px; font-size:14px; color:#cbd5e1;'>"
        f"⚔️ 공격력 <b style='color:#fff'>{atk}</b> · 💥 치명타 <b style='color:#fff'>{crit_rate*100:.1f}%</b>"
        f" · ❤️ 체력 <b style='color:#fff'>{max_hp}</b> · 현재 코어 티어 <b style='color:#fff'>{player_tier}</b></div>",
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    for idx, boss_id in enumerate(sorted(BOSS_DB.keys())):
      boss = BOSS_DB[boss_id]
      unlocked = max_tier_reached >= boss["tier"]
      kills = st.session_state.kill_counts.get(boss_id, 0)
      with cols[idx % 3]:
        lock_class = "" if unlocked else " locked"
        st.markdown(
            f"<div class='boss-card{lock_class}'>"
            f"<div style='font-size:18px; font-weight:800; color:{boss['color']}'>{boss['name']}</div>"
            f"<div style='font-size:12px; color:#94a3b8; margin-bottom:6px;'>{boss['title']}</div>"
            f"<div style='font-size:12px; color:#cbd5e1;'>❤️ {boss['hp']:,} · ⚔️ {boss['atk']}</div>"
            f"<div style='font-size:12px; color:#fbbf24;'>보상: {format_gold(boss['gold'])}</div>"
            f"<div style='font-size:11px; color:#64748b; margin-top:4px;'>필요 티어: {boss['tier']} · 처치: {kills}회</div>"
            f"</div>",
            unsafe_allow_html=True,
        )
        if st.button(f"도전하기" if unlocked else "🔒 잠김", use_container_width=True,
                     disabled=not unlocked, key=f"challenge_{boss_id}"):
          start_battle(boss_id)
          st.rerun()

    st.markdown(
        "<div style='margin-top:16px; font-size:13px; color:#64748b;'>"
        "💡 상위 보스는 '코어 강화' 탭에서 코어 티어를 올려야 도전할 수 있습니다."
        "</div>",
        unsafe_allow_html=True,
    )
