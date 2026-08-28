import random
import math
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="자이온의 왕좌 탈환기 - 우주 정복 RPG",
    page_icon="🌌",
    layout="wide",
)

# -----------------------------------------------------------------------------
# 2. 유틸리티 함수 및 비용 설정[cite: 1]
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
        0: 300, 1: 300, 2: 500, 3: 500, 4: 1000, 5: 1500, 6: 2000, 7: 2000, 8: 3000, 
        9: 5000, 10: 10900, 11: 20000, 12: 35000, 13: 55000, 14: 100000, 15: 180000, 
        16: 300000, 17: 300000, 18: 500000, 19: 800000, 20: 1500000, 21: 2500000, 
        22: 4000000, 23: 6500000, 24: 10000000, 25: 16000000, 26: 25000000, 
        27: 40000000, 28: 65000000, 29: 100000000, 30: 150000000,
    }
    return cost_table.get(level, 150000000)

def get_shield_cost(level):
    base_cost = get_enhance_cost(level)
    return max(50000, base_cost * 15)

# -----------------------------------------------------------------------------
# 3. RPG 전투 밸런스 설정 (추가된 기능)
# -----------------------------------------------------------------------------
def get_player_atk(level):
    # 레벨과 티어에 따라 기하급수적으로 강해지는 공격력 공식
    if level == 0: return 15
    tier = SMELL_DB[level]["tier"]
    return int(15 * (1.35 ** level) * (tier ** 1.5))

def get_enemy_stats(stage):
    # 스테이지 30 은 최종 보스 '자이온왕'
    if stage >= 30:
        return "👑 무취의 폭군 [자이온왕]", 9999999999, 0
    
    # 일반 몬스터 및 중간 보스
    is_boss = stage % 5 == 0
    prefix = "정예 " if is_boss else ""
    names = ["표백 드론", "살균 로봇", "진공 청소기", "탈취 전차", "향수 중독자"]
    
    name = f"{prefix}{names[stage % 5]} (Lv.{stage})"
    if is_boss:
        name = f"💀 {name}"
    
    hp = int(100 * (1.5 ** stage))
    if is_boss: hp *= 5
        
    gold = int(250 * (1.4 ** stage))
    if is_boss: gold *= 4
        
    return name, hp, gold

# -----------------------------------------------------------------------------
# 4. 게임 데이터베이스 정의 (원본 유지)[cite: 1]
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 무취의 공간", "desc": "아무 냄새도 없다. 공격력이 미미하다.", "price": 0, "color": "#4a5568", "tier": 1},
    1: {"name": "1단계 : 스쳐가는 지온냄새", "desc": "코끝을 살짝 스치는 기운.", "price": 150, "color": "#718096", "tier": 1},
    2: {"name": "2단계 : 은은한 자이온냄새", "desc": "마른 땅에 단비가 내려 피어나는 냄새.", "price": 400, "color": "#38a169", "tier": 1},
    3: {"name": "3단계 : 습한 지온냄새", "desc": "짙은 상록수 숲속에서 감오는 냄새.", "price": 600, "color": "#276749", "tier": 1},
    4: {"name": "4단계 : 진득한 자이온냄새", "desc": "흙냄새가 파고든다.", "price": 800, "color": "#319795", "tier": 1},
    5: {"name": "5단계 : 자극적인 지온냄새", "desc": "코를 강렬하게 자극한다.", "price": 3000, "color": "#2c7a7b", "tier": 1},
    6: {"name": "6단계 : 풍부한 자이온냄새", "desc": "진하고 기분 좋은 대지의 향.", "price": 3500, "color": "#3182ce", "tier": 2},
    7: {"name": "7단계 : 압도적인 지온냄새", "desc": "주위의 인공 향수를 압도한다.", "price": 6100, "color": "#2b6cb0", "tier": 2},
    8: {"name": "8단계 : 폭발하는 지온냄새", "desc": "페트리코 입자의 대폭발.", "price": 10000, "color": "#805ad5", "tier": 2},
    9: {"name": "9단계 : 시공을 뒤흔드는 지온냄새", "desc": "고대 대륙이 일렁인다.", "price": 20000, "color": "#6b46c1", "tier": 2},
    10: {"name": "10단계 : 치명적인 자이온냄새", "desc": "다른 향은 밋밋하게 느껴진다.", "price": 35100, "color": "#d69e2e", "tier": 2},
    11: {"name": "11단계 : 환각을 부르는 지온냄새", "desc": "태초의 흙밭 환각을 본다.", "price": 160000, "color": "#b7791f", "tier": 3},
    12: {"name": "12단계 : 공간지배 자이온냄새", "desc": "산소를 지온 분자로 채운다.", "price": 350000, "color": "#dd6b20", "tier": 3},
    13: {"name": "13단계 : 전설의 지온냄새", "desc": "전설 속의 지구 향기.", "price": 1000000, "color": "#c05621", "tier": 3},
    14: {"name": "14단계 : 신성한 자이온냄새", "desc": "흙과 하나가 되는 기분.", "price": 3000000, "color": "#e53e3e", "tier": 3},
    15: {"name": "15단계 : 신화급 지온냄새", "desc": "신들의 향. 공격력이 폭증하기 시작한다.", "price": 7500000, "color": "#9b2c2c", "tier": 3},
    16: {"name": "16단계 : 우주관통 자이온냄새", "desc": "성층권을 뚫고 퍼져나간다.", "price": 14200000, "color": "#00f0ff", "tier": 4},
    17: {"name": "17단계 : 차원균열 자이온냄새", "desc": "평행세계의 냄새까지 끌어당긴다.", "price": 20000000, "color": "#ff00ea", "tier": 4},
    18: {"name": "18단계 : Absolute 자이온냄새", "desc": "만물을 지온 입자로 바꾼다.", "price": 30000000, "color": "#ffe600", "tier": 4},
    19: {"name": "19단계 : 초월적 지온냄새", "desc": "인간의 감각으로는 수용 불가능.", "price": 47500000, "color": "#ff0055", "tier": 4},
    20: {"name": "20단계 : 자이온맘의 포근한 집밥 냄새", "desc": "자이온맘의 강림! 따스한 냄새.", "price": 68300000, "color": "#ffaa00", "tier": 4},
    21: {"name": "21단계 : 자이온맘의 엄격한 등짝 스매싱", "desc": "매콤하면서 사랑이 깃든 향.", "price": 101000000, "color": "#ff4500", "tier": 5},
    22: {"name": "22단계 : 자이온맘의 전설의 흙된장국", "desc": "극상의 흙내음.", "price": 160000000, "color": "#ff007f", "tier": 5},
    23: {"name": "23단계 : 자이온맘의 100년 숙성 원액", "desc": "결정체.", "price": 230000000, "color": "#7b00ff", "tier": 5},
    24: {"name": "24단계 : 자이온맘의 지온스프레이", "desc": "치명적인 청량함.", "price": 300000000, "color": "#0088ff", "tier": 5},
    25: {"name": "25단계 : 자이온맘의 무한한 은혜", "desc": "평화를 내리는 자애로움.", "price": 400000000, "color": "#00ffaa", "tier": 5},
    26: {"name": "26단계 : 자이온맘의 궁극 필살기", "desc": "우주 전체가 지온 향으로 뒤덮인다.", "price": 1800000000, "color": "#ccff00", "tier": 6},
    27: {"name": "27단계 : 자이온맘의 창조와 구원", "desc": "절대 구원의 향기.", "price": 2500000000, "color": "#fffb00", "tier": 6},
    28: {"name": "28단계 : 자이온맘의 권능 지온냄새", "desc": "자이온왕에게 대적할 최소한의 무기.", "price": 5500000000, "color": "#ffffff", "tier": 6},
    29: {"name": "29단계 : 만물의 어머니 ★자이온맘★", "desc": "최종 오라.", "price": 10500000000, "color": "#ff00aa", "tier": 6},
    30: {"name": "30단계 : ★태초의 자이온맘★ 절대신성", "desc": "자이온왕을 심판할 우주의 진리.", "price": float("inf"), "color": "#00ffff", "tier": 6},
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

# -----------------------------------------------------------------------------
# 5. 세션 상태 초기화 (RPG 스탯 추가)
# -----------------------------------------------------------------------------
if "level" not in st.session_state: st.session_state.level = 0
if "money" not in st.session_state: st.session_state.money = 0  # 0원으로 시작하여 사냥으로 벌어야 함
if "status" not in st.session_state: st.session_state.status = "READY"
if "shield" not in st.session_state: st.session_state.shield = 0
if "tears" not in st.session_state: st.session_state.tears = 0
if "pity_count" not in st.session_state: st.session_state.pity_count = 0

# RPG States
if "stage" not in st.session_state: st.session_state.stage = 1
if "enemy_hp" not in st.session_state: 
    _, hp, _ = get_enemy_stats(1)
    st.session_state.enemy_hp = hp
if "enemy_max_hp" not in st.session_state:
    _, hp, _ = get_enemy_stats(1)
    st.session_state.enemy_max_hp = hp
if "combat_logs" not in st.session_state: st.session_state.combat_logs = ["전투가 시작되었습니다! 우주의 무취 군단을 무찌르세요!"]
if "boss_defeated" not in st.session_state: st.session_state.boss_defeated = False

# -----------------------------------------------------------------------------
# 6. 전투 및 강화 로직[cite: 1]
# -----------------------------------------------------------------------------
def log_combat(msg):
    st.session_state.combat_logs.insert(0, msg)
    if len(st.session_state.combat_logs) > 8:
        st.session_state.combat_logs.pop()

def do_attack(times=1):
    for _ in range(times):
        if st.session_state.boss_defeated: return
        
        atk = get_player_atk(st.session_state.level)
        st.session_state.enemy_hp -= atk
        name, _, gold = get_enemy_stats(st.session_state.stage)
        
        if st.session_state.enemy_hp <= 0:
            if st.session_state.stage >= 30:
                st.session_state.boss_defeated = True
                log_combat("🎉 [폭군 자이온왕]을 마침내 쓰러뜨렸습니다! 우주에 향기가 돌아옵니다!")
                break
                
            st.session_state.money += gold
            log_combat(f"⚔️ [{name}] 격파! {format_gold(gold)} 획득!")
            
            st.session_state.stage += 1
            new_name, new_hp, _ = get_enemy_stats(st.session_state.stage)
            st.session_state.enemy_max_hp = new_hp
            st.session_state.enemy_hp = new_hp
            log_combat(f"🚨 새로운 적 [{new_name}] 등장!")
        else:
            log_combat(f"💥 적에게 {atk:,}의 타격을 입혔습니다!")

def run_enhance():
    curr = st.session_state.level
    if curr >= 30: return
    cost = get_enhance_cost(curr)
    if st.session_state.money < cost:
        st.session_state.status = "NOT_ENOUGH_MONEY"
        return

    st.session_state.money -= cost

    # 자이온맘 천장 시스템 (Pity)
    if st.session_state.pity_count >= PITY_MAX - 1:
        st.session_state.level += 1
        st.session_state.status = "PITY_SUCCESS"
        st.session_state.pity_count = 0
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
        if curr > 0: st.session_state.level -= 1
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

# -----------------------------------------------------------------------------
# 7. 테마 CSS
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #020617 80%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .rpg-panel {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    }
    .hp-bar-bg {
        width: 100%; height: 24px; background: #334155; border-radius: 12px; overflow: hidden; margin: 10px 0;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
    }
    .hp-bar-fill {
        height: 100%; background: linear-gradient(90deg, #ef4444, #f87171);
        transition: width 0.3s ease;
    }
    .log-box {
        background: #0f172a; padding: 10px; border-radius: 8px; font-family: monospace;
        font-size: 13px; color: #94a3b8; height: 180px; overflow-y: auto; border: 1px solid #1e293b;
    }
    .combat-btn > button {
        background: linear-gradient(180deg, #b91c1c, #7f1d1d) !important; border: none !important;
        font-size: 18px !important; font-weight: bold !important; height: 60px;
    }
    .combat-btn > button:hover { background: linear-gradient(180deg, #ef4444, #b91c1c) !important; transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 8. 메인 UI 레이아웃
# -----------------------------------------------------------------------------
st.title("🌌 자이온의 왕좌 탈환기")
st.markdown("*무취의 우주를 정복한 폭군 '자이온왕'을 물리치고 우주에 향기를 되찾으세요!*")

# 보스 클리어 엔딩 화면
if st.session_state.boss_defeated:
    st.balloons()
    st.markdown("""
        <div style='text-align:center; padding: 50px;'>
            <h1 style='color: #00ffff; font-size: 50px; text-shadow: 0 0 20px #00ffff;'>👑 우주 해방 완료!</h1>
            <h3 style='color: #fde68a;'>무취의 폭군 자이온왕이 쓰러졌습니다.</h3>
            <p style='color: #cbd5e1;'>자이온과 자이온맘의 지온냄새가 온 우주에 퍼집니다...</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🔄 새로운 차원에서 다시 시작하기", use_container_width=True):
        st.session_state.clear()
        st.rerun()
    st.stop()

col_battle, col_enhance = st.columns([1.2, 1], gap="large")

with col_battle:
    st.markdown("<div class='rpg-panel'>", unsafe_allow_html=True)
    st.subheader("⚔️ 전장 (Battlefield)")
    
    # 몬스터 정보 표시
    e_name, _, e_gold = get_enemy_stats(st.session_state.stage)
    hp_pct = max(0, min(100, (st.session_state.enemy_hp / st.session_state.enemy_max_hp) * 100))
    
    st.markdown(f"**현재 스테이지 : {st.session_state.stage}** (보상: {format_gold(e_gold)})")
    st.markdown(f"<h3 style='color:#fca5a5; margin:0;'>{e_name}</h3>", unsafe_allow_html=True)
    
    # 체력바
    st.markdown(f"""
        <div class='hp-bar-bg'>
            <div class='hp-bar-fill' style='width: {hp_pct}%;'></div>
        </div>
        <div style='text-align:right; font-size:12px; color:#cbd5e1; margin-top:-5px;'>
            HP: {st.session_state.enemy_hp:,} / {st.session_state.enemy_max_hp:,}
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # 플레이어 정보
    atk = get_player_atk(st.session_state.level)
    st.markdown(f"🗡️ **자이온의 공격력:** `{atk:,}` (현재 무기: {SMELL_DB[st.session_state.level]['name']})")
    
    # 공격 버튼
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='combat-btn'>", unsafe_allow_html=True)
        if st.button("⚔️ 공격 (1회)", use_container_width=True):
            do_attack(1)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        if st.button("🔥 연속 공격 (10회)", use_container_width=True, type="primary"):
            do_attack(10)
            st.rerun()
            
    # 전투 로그
    st.write("")
    st.markdown("**전투 기록**")
    logs_html = "<div class='log-box'>" + "<br>".join(st.session_state.combat_logs) + "</div>"
    st.markdown(logs_html, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


with col_enhance:
    st.markdown("<div class='rpg-panel'>", unsafe_allow_html=True)
    st.subheader("🛠️ 자이온맘의 대장간")
    
    st.markdown(
        f"<div style='font-size:20px; color:#fde68a; margin-bottom:10px;'>"
        f"💰 보유 자금: <b>{format_gold(st.session_state.money)}</b></div>",
        unsafe_allow_html=True,
    )
    
    curr = st.session_state.level
    c_data = SMELL_DB[curr]
    cost = get_enhance_cost(curr)
    
    st.markdown(f"**현재 장착 무기:** <span style='color:{c_data['color']}; font-weight:bold;'>{c_data['name']}</span>", unsafe_allow_html=True)
    st.caption(f"\"{c_data['desc']}\"")
    
    # 강화 버튼
    if st.button(f"🔨 무기 강화 (비용: {format_gold(cost)})", use_container_width=True, disabled=(curr >= 30)):
        if st.session_state.money < cost:
            st.error("골드가 부족합니다! 전장에서 적을 물리치고 골드를 모아오세요.")
        else:
            run_enhance()
            st.rerun()
            
    # 상태 메시지
    status = st.session_state.status
    if status == "SUCCESS": st.success("✨ 강화 성공! 공격력이 크게 상승했습니다!")
    elif status == "CRITICAL": st.success("⚡ 대성공!! 무기가 폭발적으로 강해졌습니다!")
    elif status == "PITY_SUCCESS": st.info("✨ 자이온맘의 가호로 100% 강화에 성공했습니다!")
    elif status == "FAILED": st.warning("🔻 강화 실패... 무기 레벨이 하락했습니다.")
    elif status == "DESTROYED": st.error("💥 무기 코어 파괴! 0단계로 초기화되었습니다...")
    elif status == "SHIELD_SAVED": st.info("🛡️ 방지권이 무기 파괴를 막아냈습니다!")
    elif status == "HOLD": st.caption("🔒 무기 에너지가 유지되었습니다. (변화 없음)")
    
    st.markdown("<hr style='border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    
    # 상점 탭
    t1, t2 = st.tabs(["🛡️ 자이온맘의 방패", "💧 기적의 눈물"])
    with t1:
        s_cost = get_shield_cost(curr)
        st.write(f"**파괴 방지권** (보유: {st.session_state.shield}/3)")
        st.caption("18단계 이상부터 사용할 수 있는 파괴 1회 면제권입니다.")
        if st.button(f"구매 ({format_gold(s_cost)})", use_container_width=True):
            if curr < 18: st.warning("18단계 이상부터 구매 가능합니다.")
            elif st.session_state.shield >= 3: st.warning("이미 최대치를 보유중입니다.")
            elif st.session_state.money >= s_cost:
                st.session_state.money -= s_cost
                st.session_state.shield += 1
                st.rerun()
            else: st.error("골드 부족!")
            
    with t2:
        st.write(f"**지온의 눈물** (보유: {st.session_state.tears}/120)")
        st.caption("실패 시 쌓이는 눈물 40개를 모아 확률적으로 레벨을 점프합니다.")
        if st.button("기적 가동 (눈물 40 소모)", use_container_width=True):
            if curr >= 28: st.warning("28단계부터는 사용할 수 없습니다.")
            elif st.session_state.tears >= 40:
                st.session_state.tears -= 40
                if random.random() < 0.5:
                    add = random.choice([1,2,3])
                    st.session_state.level = min(30, curr + add)
                    st.session_state.status = "SUCCESS"
                else:
                    st.session_state.status = "FAILED"
                st.rerun()
            else: st.error("눈물이 부족합니다.")
            
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 9. 원본의 3D 뷰어 컴포넌트 삽입 (시각 효과)[cite: 1]
# -----------------------------------------------------------------------------
st.write("")
st.subheader("🔮 지온냄새 무기 코어 투영기")
tier = SMELL_DB[st.session_state.level]["tier"]
card_color = SMELL_DB[st.session_state.level]["color"]
# 기존 Three.js 스크립트를 하단 뷰어로 활용
three_js_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body style="margin:0; overflow:hidden; background: #0f172a; border-radius:12px;">
    <div id="container" style="width:100%; height:300px;"></div>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(40, window.innerWidth / 300, 0.1, 1000);
        camera.position.set(0, 0, 7.0);

        const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, 300);
        document.getElementById('container').appendChild(renderer.domElement);

        const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
        scene.add(ambientLight);
        
        const pointLight = new THREE.PointLight("{card_color}", 20, 40);
        pointLight.position.set(0, 0, 3);
        scene.add(pointLight);

        // 도형 결정 로직 간소화
        const lvl = {st.session_state.level};
        let baseGeo;
        if (lvl <= 5) baseGeo = new THREE.BoxGeometry(1.5, 1.5, 1.5);
        else if (lvl <= 10) baseGeo = new THREE.CylinderGeometry(1.2, 1.2, 1.8, 6);
        else if (lvl <= 15) baseGeo = new THREE.OctahedronGeometry(1.5);
        else if (lvl <= 20) baseGeo = new THREE.IcosahedronGeometry(1.5);
        else if (lvl <= 25) baseGeo = new THREE.TorusGeometry(1.2, 0.4, 16, 32);
        else baseGeo = new THREE.TorusKnotGeometry(1.0, 0.3, 64, 16);

        const outerMat = new THREE.MeshPhysicalMaterial({{
            color: "{card_color}", metalness: 0.8, roughness: 0.2, 
            transparent: true, opacity: 0.9, emissive: "{card_color}", emissiveIntensity: 0.5
        }});
        
        const mesh = new THREE.Mesh(baseGeo, outerMat);
        scene.add(mesh);

        function animate() {{
            requestAnimationFrame(animate);
            mesh.rotation.x += 0.01;
            mesh.rotation.y += 0.015;
            renderer.render(scene, camera);
        }}
        animate();
    </script>
</body>
</html>
"""
components.html(three_js_code, height=300)
