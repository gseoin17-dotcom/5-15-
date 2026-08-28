import random
import math
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="메이플 자이온 스토리 - 3D 강화 & 모험",
    page_icon="🍁",
    layout="wide",
)

# -----------------------------------------------------------------------------
# 2. 유틸리티 함수 및 포맷 설정
# -----------------------------------------------------------------------------
def format_gold(amount):
    if amount == 0 or amount == float("inf"):
        return "0메소" if amount == 0 else "무한대(INF)"
    units = ["", "만", "억", "조", "경", "해"]
    result = []
    unit_idx = 0
    while amount > 0 and unit_idx < len(units):
        remainder = int(amount % 10000)
        if remainder > 0:
            result.insert(0, f"{remainder:,}{units[unit_idx]}")
        amount //= 10000
        unit_idx += 1
    return "".join(result) + "메소"

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
# 3. 게임 데이터베이스 (지온냄새 0~30단계)
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
    30: {"name": "30단계 : ★태초의 자이온맘★ 절대신성", "desc": "우주를 지온으로 통일한 자이온맘의 완성.", "price": float("inf"), "color": "#00ffff", "tier": 6},
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

# 메이플 필드 몬스터 데이터 (사냥터별)
MAPS = {
    "초보자의 수련장 (Lv.1)": {"mob": "주황버섯 닮은 무취슬라임", "hp": 100, "meso": 50, "req_lvl": 0},
    "자이온의 오솔길 (Lv.10)": {"mob": "표백된 스텀프", "hp": 3500, "meso": 1200, "req_lvl": 5},
    "자이온맘의 연구소 (Lv.20)": {"mob": "무취 클리너 로봇", "hp": 85000, "meso": 25000, "req_lvl": 15},
    "👑 [보스맵] 자이온왕의 궁전 (Lv.30)": {"mob": "최종보스 자이온왕", "hp": 9999999, "meso": 5000000, "req_lvl": 25},
}

# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state: st.session_state.level = 0
if "max_level" not in st.session_state: st.session_state.max_level = 0
if "money" not in st.session_state: st.session_state.money = 5000  # 초기 정착금 5000 메소
if "status" not in st.session_state: st.session_state.status = "READY"
if "shield" not in st.session_state: st.session_state.shield = 0
if "tears" not in st.session_state: st.session_state.tears = 0
if "pity_count" not in st.session_state: st.session_state.pity_count = 0

# 메이플 사냥 관련 상태
if "current_map" not in st.session_state: st.session_state.current_map = "초보자의 수련장 (Lv.1)"
current_mob_data = MAPS[st.session_state.current_map]
if "mob_hp" not in st.session_state: st.session_state.mob_hp = current_mob_data["hp"]
if "mob_max_hp" not in st.session_state: st.session_state.mob_max_hp = current_mob_data["hp"]
if "battle_logs" not in st.session_state: st.session_state.battle_logs = ["🍁 메이플 월드에 접속하셨습니다. 사냥을 통해 메소(골드)를 모으세요!"]
if "game_cleared" not in st.session_state: st.session_state.game_cleared = False

# -----------------------------------------------------------------------------
# 5. 게임 로직 (강화 및 사냥)
# -----------------------------------------------------------------------------
def log_msg(msg):
    st.session_state.battle_logs.insert(0, msg)
    if len(st.session_state.battle_logs) > 6:
        st.session_state.battle_logs.pop()

def get_player_dmg(level):
    if level == 0: return 20
    tier = SMELL_DB[level]["tier"]
    return int(25 * (1.4 ** level) * (tier ** 1.3))

def attack_mob(times=1):
    if st.session_state.game_cleared: return
    
    for _ in range(times):
        dmg = get_player_dmg(st.session_state.level)
        st.session_state.mob_hp -= dmg
        m_data = MAPS[st.session_state.current_map]
        
        if st.session_state.mob_hp <= 0:
            reward = m_data["meso"]
            st.session_state.money += reward
            log_msg(f"🎉 [{m_data['mob']}] 격파! 획득: {format_gold(reward)}")
            
            # 보스 클리어 체크
            if "자이온왕" in m_data["mob"]:
                st.session_state.game_cleared = True
                log_msg("👑 자이온왕을 토벌하고 메이플 월드에 평화가 찾아왔습니다!")
                break
                
            # 체력 리필 및 새 몬스터 소환
            st.session_state.mob_max_hp = m_data["hp"]
            st.session_state.mob_hp = m_data["hp"]
        else:
            log_msg(f"⚔️ 자이온의 [지온냄새] 공격! 데미지: {dmg:,} (적 HP 남음)")

def run_enhance():
    curr = st.session_state.level
    if curr >= 30: return
    cost = get_enhance_cost(curr)
    if st.session_state.money < cost:
        st.session_state.status = "NOT_ENOUGH_MONEY"
        return

    st.session_state.money -= cost

    if st.session_state.pity_count >= PITY_MAX - 1:
        st.session_state.level += 1
        st.session_state.status = "PITY_SUCCESS"
        st.session_state.pity_count = 0
        if st.session_state.level > st.session_state.max_level: st.session_state.max_level = st.session_state.level
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

    if st.session_state.level > st.session_state.max_level:
        st.session_state.max_level = st.session_state.level

# -----------------------------------------------------------------------------
# 6. 메이플풍 스타일 CSS UI
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
        font-family: 'MapleStory', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .maple-box {
        background: rgba(30, 41, 59, 0.85);
        border: 2px solid #475569;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        margin-bottom: 12px;
    }
    .maple-title {
        font-size: 18px; font-weight: 800; color: #fde68a; margin-bottom: 8px;
        text-shadow: 2px 2px 0px #000;
    }
    .hp-bg {
        width: 100%; height: 22px; background: #334155; border-radius: 11px; overflow: hidden; border: 1px solid #64748b;
    }
    .hp-fill {
        height: 100%; background: linear-gradient(90deg, #ef4444, #f87171); transition: width 0.2s;
    }
    .chat-box {
        background: #020617; border: 1px solid #334155; border-radius: 8px; padding: 10px;
        font-family: monospace; font-size: 13px; color: #cbd5e1; height: 130px; overflow-y: auto;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. 엔딩 처리
# -----------------------------------------------------------------------------
if st.session_state.game_cleared:
    st.balloons()
    st.markdown("""
        <div style='text-align:center; padding: 40px;'>
            <h1 style='color: #00ffff; font-size: 45px; text-shadow: 0 0 20px #00ffff;'>🍁 메이플 월드 구원 완료! 🍁</h1>
            <h3 style='color: #fde68a;'>자이온과 자이온맘의 향기가 자이온왕을 정화했습니다.</h3>
            <p style='color: #cbd5e1;'>모든 모험을 완수했습니다. 축하합니다!</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🔄 캐릭터 초기화 후 다시 모험하기", use_container_width=True):
        st.session_state.clear()
        st.rerun()
    st.stop()

# -----------------------------------------------------------------------------
# 8. 메인 UI 구성 (메이플 스타일 좌우 배치)
# -----------------------------------------------------------------------------
st.title("🍁 메이플 자이온 : 지온냄새 대모험")
st.markdown("사냥터에서 몬스터를 잡아 메소를 벌고, **자이온맘의 대장간**에서 지온냄새 무기를 강화하여 최강의 모험가가 되세요!")

col_left, col_right = st.columns([1.1, 1.2], gap="medium")

with col_left:
    st.markdown("<div class='maple-box'>", unsafe_allow_html=True)
    st.markdown("<div class='maple-title'>🗺️ 메이플 필드 & 사냥터</div>", unsafe_allow_html=True)
    
    # 맵 선택 드롭다운
    map_list = list(MAPS.keys())
    selected_map = st.selectbox("사냥터 이동", map_list, index=map_list.index(st.session_state.current_map))
    
    if selected_map != st.session_state.current_map:
        req = MAPS[selected_map]["req_lvl"]
        if st.session_state.level < req:
            st.warning(f"⚠️ 이 사냥터는 무기 강화 <b>{req}단계</b> 이상부터 입장 가능합니다!")
        else:
            st.session_state.current_map = selected_map
            m_dat = MAPS[selected_map]
            st.session_state.mob_max_hp = m_dat["hp"]
            st.session_state.mob_hp = m_dat["hp"]
            log_msg(f"🚀 [{selected_map}] (으)로 이동했습니다.")
            st.rerun()

    m_info = MAPS[st.session_state.current_map]
    st.markdown(f"**현재 몬스터:** `{m_info['mob']}` (처치 보상: {format_gold(m_info['meso'])})")
    
    # 몬스터 체력바
    hp_pct = max(0, min(100, (st.session_state.mob_hp / st.session_state.mob_max_hp) * 100))
    st.markdown(f"""
        <div class='hp-bg'>
            <div class='hp-fill' style='width: {hp_pct}%;'></div>
        </div>
        <div style='text-align:right; font-size:12px; color:#cbd5e1; margin-top:2px;'>
            HP: {st.session_state.mob_hp:,} / {st.session_state.mob_max_hp:,}
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("⚔️ 기본 공격 (1회)", use_container_width=True):
            attack_mob(1)
            st.rerun()
    with c_btn2:
        if st.button("⚡ 연속 사냥 (10회)", use_container_width=True, type="primary"):
            attack_mob(10)
            st.rerun()
            
    st.write("")
    st.markdown("**📜 전투 로그**")
    logs_html = "<div class='chat-box'>" + "<br>".join(st.session_state.battle_logs) + "</div>"
    st.markdown(logs_html, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("<div class='maple-box'>", unsafe_allow_html=True)
    st.markdown("<div class='maple-title'>🔨 자이온맘의 대장간 (강화 시스템)</div>", unsafe_allow_html=True)
    
    curr_lvl = st.session_state.level
    cur_data = SMELL_DB[curr_lvl]
    enhance_cost = get_enhance_cost(curr_lvl)
    
    st.markdown(f"💳 **보유 메소:** <span style='color:#fde68a; font-weight:bold;'>{format_gold(st.session_state.money)}</span>", unsafe_allow_html=True)
    st.markdown(f"🛡️ **장착 무기:** <span style='color:{cur_data['color']}; font-weight:bold;'>{cur_data['name']}</span>", unsafe_allow_html=True)
    st.caption(f"\"{cur_data['desc']}\" (내 공격력: {get_player_dmg(curr_lvl):,})")
    
    # 강화 버튼
    if st.button(f"🔥 지온냄새 강화하기 (비용: {format_gold(enhance_cost)})", use_container_width=True, disabled=(curr_lvl >= 30)):
        if st.session_state.money < enhance_cost:
            st.error("메소가 부족합니다! 필드에서 사냥을 더 하고 오세요.")
        else:
            run_enhance()
            st.rerun()
            
    # 강화 상태 피드백
    status = st.session_state.status
    if status == "SUCCESS": st.success("✨ 메이플 강화 성공! 지온냄새가 더욱 진해졌습니다!")
    elif status == "CRITICAL": st.success("⚡ 럭키 대성공!! 무려 2단계나 수직 상승했습니다!")
    elif status == "PITY_SUCCESS": st.info("✨ 자이온맘의 따스한 가호 발동! (100% 성공)")
    elif status == "FAILED": st.warning("🔻 강화 실패... 레벨이 1 떨어졌습니다.")
    elif status == "DESTROYED": st.error("💥 장비 파괴! 눈물 흘리며 0단계로 초기화되었습니다...")
    elif status == "SHIELD_SAVED": st.info("🛡️ 파괴 방지권이 발동하여 장비를 보호했습니다!")
    elif status == "HOLD": st.caption("🔒 에너지가 유지되어 변화가 없습니다.")

    st.markdown("<hr style='border-color:rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
    
    # 편의 기능 탭 (방지권 및 눈물)
    t_tab1, t_tab2 = st.tabs(["🛡️ 파괴 방지권 상점", "💧 자이온의 눈물"])
    with t_tab1:
        s_cost = get_shield_cost(curr_lvl)
        st.write(f"보유 방지권: **{st.session_state.shield} / 3개** (18단계 이상 구매 가능)")
        if st.button("방지권 구매", use_container_width=True):
            if curr_lvl < 18: st.warning("18단계부터 구매할 수 있습니다.")
            elif st.session_state.shield >= 3: st.warning("최대 3개까지만 소지 가능합니다.")
            elif st.session_state.money >= s_cost:
                st.session_state.money -= s_cost
                st.session_state.shield += 1
                st.success("파괴 방지권 획득!")
                st.rerun()
            else: st.error("메소가 부족합니다.")
            
    with t_tab2:
        st.write(f"누적 눈물: **{st.session_state.tears} / 120개** (실패 시 적립)")
        if st.button("눈물 40개로 기적 가동 (50% 확률로 1~3업)", use_container_width=True):
            if curr_lvl >= 28: st.warning("28단계 이상에서는 신성한 기운으로 사용할 수 없습니다.")
            elif st.session_state.tears >= 40:
                st.session_state.tears -= 40
                if random.random() < 0.5:
                    add_l = random.choice([1, 2, 3])
                    st.session_state.level = min(30, curr_lvl + add_l)
                    st.success(f"기적 대성공! {add_l}단계 상승!")
                else:
                    st.warning("눈물의 기적이 실패했습니다...")
                st.rerun()
            else: st.error("눈물 40개가 필요합니다.")

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 9. 3D 메이플 스타일 무기 뷰어 (Three.js)
# -----------------------------------------------------------------------------
st.write("")
st.markdown("<div class='maple-title'>🔮 메이플 장비 슬롯 : 지온냄새 3D 프로젝터</div>", unsafe_allow_html=True)

card_color = cur_data["color"]
three_js_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body style="margin:0; overflow:hidden; background: transparent;">
    <div id="container" style="width:100%; height:260px;"></div>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(40, window.innerWidth / 260, 0.1, 1000);
        camera.position.set(0, 0, 6.5);

        const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, 260);
        document.getElementById('container').appendChild(renderer.domElement);

        const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
        scene.add(ambientLight);
        
        const pointLight = new THREE.PointLight("{card_color}", 25, 30);
        pointLight.position.set(2, 3, 3);
        scene.add(pointLight);

        // 메이플 아이템 같은 느낌의 입체 도형
        const lvl = {curr_lvl};
        let geo;
        if (lvl <= 5) geo = new THREE.BoxGeometry(1.6, 1.6, 1.6);
        else if (lvl <= 10) geo = new THREE.CylinderGeometry(1.3, 1.3, 2.0, 6);
        else if (lvl <= 15) geo = new THREE.OctahedronGeometry(1.6);
        else if (lvl <= 20) geo = new THREE.IcosahedronGeometry(1.6);
        else if (lvl <= 25) geo = new THREE.TorusGeometry(1.3, 0.45, 16, 32);
        else geo = new THREE.TorusKnotGeometry(1.1, 0.35, 64, 16);

        const mat = new THREE.MeshPhysicalMaterial({{
            color: "{card_color}", metalness: 0.85, roughness: 0.15, 
            transparent: true, opacity: 0.92, emissive: "{card_color}", emissiveIntensity: 0.6
        }});
        
        const itemMesh = new THREE.Mesh(geo, mat);
        scene.add(itemMesh);

        function animate() {{
            requestAnimationFrame(animate);
            itemMesh.rotation.x += 0.012;
            itemMesh.rotation.y += 0.018;
            renderer.render(scene, camera);
        }}
        animate();
    </script>
</body>
</html>
"""
components.html(three_js_code, height=260)
