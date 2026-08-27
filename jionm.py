import streamlit as st
import random
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - FANTASY CITY EDITION",
    page_icon="🏰",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. 게임 데이터베이스 및 강화 확률표 / 업적 데이터베이스
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 무취의 공간", "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.", "price": 0, "color": "#4a5568", "tier": 1},
    1: {"name": "1단계 : 스쳐가는 지온냄새", "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.", "price": 100, "color": "#718096", "tier": 1},
    2: {"name": "2단계 : 은은한 자이온냄새", "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.", "price": 300, "color": "#38a169", "tier": 1},
    3: {"name": "3단계 : 습한 지온냄새", "desc": "비 온 뒤 짙은 상록수 숲속에서 감도는 냄새.", "price": 700, "color": "#276749", "tier": 1},
    4: {"name": "4단계 : 진득한 자이온냄새", "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.", "price": 1500, "color": "#319795", "tier": 1},
    5: {"name": "5단계 : 자극적인 지온냄새", "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.", "price": 3500, "color": "#2c7a7b", "tier": 1},
    6: {"name": "6단계 : 풍부한 자이온냄새", "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.", "price": 8000, "color": "#3182ce", "tier": 2},
    7: {"name": "7단계 : 압도적인 지온냄새", "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.", "price": 18000, "color": "#2b6cb0", "tier": 2},
    8: {"name": "8단계 : 폭발하는 자이온냄새", "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.", "price": 40000, "color": "#805ad5", "tier": 2},
    9: {"name": "9단계 : 시공을 뒤흔드는 지온냄새", "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.", "price": 90000, "color": "#6b46c1", "tier": 2},
    10: {"name": "10단계 : 치명적인 자이온냄새", "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.", "price": 200000, "color": "#d69e2e", "tier": 2},
    11: {"name": "11단계 : 환각을 부르는 지온냄새", "desc": "태초의 지구 흙밭을 거니는 환각을 본다.", "price": 450000, "color": "#b7791f", "tier": 3},
    12: {"name": "12단계 : 공간지배 자이온냄새", "desc": "방 안의 모든 산소를 지온 분자로 채운다.", "price": 1000000, "color": "#dd6b20", "tier": 3},
    13: {"name": "13단계 : 전설의 지온냄새", "desc": "역사서에서 언급되던 전설 속의 지구 향기.", "price": 2200000, "color": "#c05621", "tier": 3},
    14: {"name": "14단계 : 신성한 자이온냄새", "desc": "마음이 경건해지며 흙과 하나가 되는 기분.", "price": 5000000, "color": "#e53e3e", "tier": 3},
    15: {"name": "15단계 : 신화급 지온냄새", "desc": "신들이 세계를 창조할 때 맡았다는 향.", "price": 12000000, "color": "#9b2c2c", "tier": 3},
    16: {"name": "16단계 : 우주관통 자이온냄새", "desc": "성층권을 뚫고 우주선까지 퍼져나간다.", "price": 30000000, "color": "#00f0ff", "tier": 4},
    17: {"name": "17단계 : 차원균열 지온냄새", "desc": "평행세계의 흙냄새까지 끌어당긴다.", "price": 75000000, "color": "#ff00ea", "tier": 4},
    18: {"name": "18단계 : Absolute 자이온냄새", "desc": "만물의 요소를 지온 입자로 바꿔버린다.", "price": 180000000, "color": "#ffe600", "tier": 4},
    19: {"name": "19단계 : 초월적 지온냄새", "desc": "인간의 감각으로는 수용 불가능한 향기.", "price": 450000000, "color": "#ff0055", "tier": 4},
    20: {"name": "20단계 : 자이온맘의 포근한 집밥 냄새", "desc": "자이온맘의 강림! 따스하고 구수한 냄새.", "price": 1000000000, "color": "#ffaa00", "tier": 4},
    21: {"name": "21단계 : 자이온맘의 엄격한 등짝 스매싱", "desc": "매콤하면서 사랑이 깃든 자이온맘의 향.", "price": 2500000000, "color": "#ff4500", "tier": 5},
    22: {"name": "22단계 : 자이온맘의 전설의 흙된장국", "desc": "극상의 흙내음과 깊은 손맛.", "price": 6000000000, "color": "#ff007f", "tier": 5},
    23: {"name": "23단계 : 자이온맘의 100년 숙성 원액", "desc": "몰래 아껴둔 냄새의 결정체.", "price": 15000000000, "color": "#7b00ff", "tier": 5},
    24: {"name": "24단계 : 자이온맘의 지온스프레이", "desc": "집안 가득 뿌리는 치명적인 청량함.", "price": 40000000000, "color": "#0088ff", "tier": 5},
    25: {"name": "25단계 : 자이온맘의 무한한 은혜", "desc": "은하수 아이들에게 평화를 내리는 자애로움.", "price": 100000000000, "color": "#00ffaa", "tier": 5},
    26: {"name": "26단계 : 자이온맘의 궁극 필살기", "desc": "우주 전체가 지온 향으로 뒤덮인다.", "price": 250000000000, "color": "#ccff00", "tier": 6},
    27: {"name": "27단계 : 자이온맘의 창조와 구원", "desc": "빅뱅 당시 터뜨린 절대 구원의 향기.", "price": 600000000000, "color": "#fffb00", "tier": 6},
    28: {"name": "28단계 : 자이온맘의 권능 지온냄새", "desc": "창조주도 고개를 숙이고 냄새를 맡는다.", "price": 1500000000000, "color": "#ffffff", "tier": 6},
    29: {"name": "29단계 : 만물의 어머니 ★자이온맘★", "desc": "우주 만물이 품으로 돌아가는 최종 오라.", "price": 4000000000000, "color": "#ff00aa", "tier": 6},
    30: {"name": "30단계 : ★태초의 자이온맘★ 절대신성", "desc": "우주를 지온으로 통일한 자이온맘의 완성.", "price": 10000000000000, "color": "#00ffff", "tier": 6}
}

PROB_TABLE = {
    0: (100, 0, 0), 1: (95, 5, 0), 2: (90, 10, 0), 3: (85, 15, 0), 4: (80, 20, 0),
    5: (75, 25, 0), 6: (70, 28, 2), 7: (65, 30, 5), 8: (60, 32, 8), 9: (55, 35, 10),
    10: (50, 38, 12), 11: (45, 40, 15), 12: (40, 42, 18), 13: (35, 45, 20), 14: (30, 48, 22),
    15: (25, 50, 25), 16: (20, 53, 27), 17: (15, 55, 30), 18: (12, 53, 35), 19: (10, 50, 40),
    20: (8, 47, 45), 21: (6, 44, 50), 22: (5, 40, 55), 23: (4, 36, 60), 24: (3, 32, 65),
    25: (2, 28, 70), 26: (1.5, 23.5, 75), 27: (1.0, 19.0, 80), 28: (0.5, 14.5, 85), 29: (0.1, 9.9, 90)
}

CRITICAL_RATE = 0.05

ACHIEVEMENTS_DB = {
    "first_try": {"title": "🌱 입문의 발걸음", "desc": "첫 강화를 시도하기", "reward_gold": 1000, "badge": "🌱"},
    "reach_10": {"title": "✨ 향수 파괴자", "desc": "10단계 달성하기", "reward_gold": 50000, "badge": "✨"},
    "reach_20": {"title": "🍳 자이온맘의 인정", "desc": "20단계 달성하기", "reward_gold": 500000, "badge": "🍳"},
    "reach_30": {"title": "👑 만물의 구원자", "desc": "30단계 최고 등급 달성하기", "reward_gold": 10000000, "badge": "👑"},
    "first_destroy": {"title": "💥 재가 되어버린 향기", "desc": "첫 번째 파괴 경험하기", "reward_gold": 20000, "badge": "💥"},
    "crit_master": {"title": "⚡ 럭키 가이", "desc": "크리티컬 대성공 3회 달성하기", "reward_gold": 100000, "badge": "⚡"},
    "shield_savior": {"title": "🛡️ 철통보안", "desc": "파괴 방지권으로 파괴 1회 막아내기", "reward_gold": 30000, "badge": "🛡️"}
}

TITLES_DB = {
    "none": {"name": "초보 연금술사", "buff": "없음"},
    "reach_10": {"name": "지온 수집가", "buff": "골드 보상 상승"},
    "reach_20": {"name": "자이온의 후계자", "buff": "멋짐 폭발"},
    "reach_30": {"name": "★태초의 지온마스터★", "buff": "절대 신성 오라"},
    "first_destroy": {"name": "불운의 아이콘", "buff": "동정표 획득"},
    "crit_master": {"name": "신의 손", "buff": "행운 기운 감돌음"}
}

# -----------------------------------------------------------------------------
# 3. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state: st.session_state.level = 0
if "money" not in st.session_state: st.session_state.money = 10000
if "status" not in st.session_state: st.session_state.status = "READY"
if "shield" not in st.session_state: st.session_state.shield = 0  
if "tears" not in st.session_state: st.session_state.tears = 0    
if "dev_mode" not in st.session_state: st.session_state.dev_mode = False

# 통계 및 업적 데이터
if "total_tries" not in st.session_state: st.session_state.total_tries = 0
if "total_destroys" not in st.session_state: st.session_state.total_destroys = 0
if "total_crits" not in st.session_state: st.session_state.total_crits = 0
if "shield_saves" not in st.session_state: st.session_state.shield_saves = 0
if "unlocked_achievements" not in st.session_state: st.session_state.unlocked_achievements = set()
if "equipped_title" not in st.session_state: st.session_state.equipped_title = "none"

# -----------------------------------------------------------------------------
# 4. 업적 및 강화 로직
# -----------------------------------------------------------------------------
def check_achievements():
    unlocked = st.session_state.unlocked_achievements
    
    if st.session_state.total_tries >= 1 and "first_try" not in unlocked:
        unlocked.add("first_try")
        st.session_state.money += ACHIEVEMENTS_DB["first_try"]["reward_gold"]
        st.toast("🎉 업적 달성: 입문의 발걸음! (+1,000 G)")
        
    if st.session_state.level >= 10 and "reach_10" not in unlocked:
        unlocked.add("reach_10")
        st.session_state.money += ACHIEVEMENTS_DB["reach_10"]["reward_gold"]
        st.toast("🎉 업적 달성: 향수 파괴자! (+50,000 G)")

    if st.session_state.level >= 20 and "reach_20" not in unlocked:
        unlocked.add("reach_20")
        st.session_state.money += ACHIEVEMENTS_DB["reach_20"]["reward_gold"]
        st.toast("🎉 업적 달성: 자이온맘의 인정! (+500,000 G)")

    if st.session_state.level >= 30 and "reach_30" not in unlocked:
        unlocked.add("reach_30")
        st.session_state.money += ACHIEVEMENTS_DB["reach_30"]["reward_gold"]
        st.toast("🎉 업적 달성: 만물의 구원자! (+10,000,000 G)")

    if st.session_state.total_destroys >= 1 and "first_destroy" not in unlocked:
        unlocked.add("first_destroy")
        st.session_state.money += ACHIEVEMENTS_DB["first_destroy"]["reward_gold"]
        st.toast("🎉 업적 달성: 재가 되어버린 향기! (+20,000 G)")

    if st.session_state.total_crits >= 3 and "crit_master" not in unlocked:
        unlocked.add("crit_master")
        st.session_state.money += ACHIEVEMENTS_DB["crit_master"]["reward_gold"]
        st.toast("🎉 업적 달성: 럭키 가이! (+100,000 G)")

    if st.session_state.shield_saves >= 1 and "shield_savior" not in unlocked:
        unlocked.add("shield_savior")
        st.session_state.money += ACHIEVEMENTS_DB["shield_savior"]["reward_gold"]
        st.toast("🎉 업적 달성: 철통보안! (+30,000 G)")

def enhance():
    curr = st.session_state.level
    if curr >= 30: return
    
    st.session_state.total_tries += 1
    
    if st.session_state.dev_mode:
        st.session_state.level += 1
        st.session_state.status = "SUCCESS"
        check_achievements()
        return

    sp, fp, dp = PROB_TABLE[curr]
    r = random.uniform(0, 100)
    
    if r < sp:
        if random.random() < CRITICAL_RATE and curr + 2 <= 30:
            st.session_state.level += 2
            st.session_state.status = "CRITICAL"
            st.session_state.total_crits += 1
        else:
            st.session_state.level += 1
            st.session_state.status = "SUCCESS"
    elif r < (sp + dp):
        if st.session_state.shield > 0:
            st.session_state.shield -= 1
            st.session_state.status = "SHIELD_SAVED"
            st.session_state.tears += 1
            st.session_state.shield_saves += 1
        else:
            st.session_state.level = 0
            st.session_state.status = "DESTROYED"
            st.session_state.tears += 2
            st.session_state.total_destroys += 1
    else:
        if curr > 0: st.session_state.level -= 1
        st.session_state.status = "FAILED"
        st.session_state.tears += 1

    check_achievements()

def sell():
    curr = st.session_state.level
    if curr == 0: return
    st.session_state.money += SMELL_DB[curr]['price']
    st.session_state.level = 0
    st.session_state.status = "READY"

# -----------------------------------------------------------------------------
# 5. 테마 CSS
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #180d24 0%, #2b1338 40%, #3d1b32 70%, #1c0a21 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    .glass-panel {
        background: rgba(43, 23, 56, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(236, 178, 255, 0.2);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    .stat-card {
        background: rgba(58, 28, 77, 0.5);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(245, 158, 11, 0.3);
        padding: 12px 10px;
        border-radius: 12px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .stat-card:hover {
        border-color: rgba(245, 158, 11, 0.7);
        box-shadow: 0 0 15px rgba(245, 158, 11, 0.3);
    }
    .stat-title {
        font-size: 13px;
        font-weight: 600;
        color: #fde68a;
        margin-bottom: 4px;
        letter-spacing: 0.5px;
    }
    .stat-value {
        font-size: 19px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
    }

    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease !important;
        border: 1px solid rgba(217, 119, 6, 0.3) !important;
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.4), rgba(217, 119, 6, 0.4)) !important;
        color: #ffffff !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(217, 119, 6, 0.4);
    }

    .badge-unlocked {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 6px;
        background: rgba(34, 197, 94, 0.2);
        border: 1px solid #22c55e;
        color: #86efac;
        font-size: 12px;
        font-weight: bold;
    }
    .badge-locked {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 6px;
        background: rgba(100, 116, 139, 0.2);
        border: 1px solid #64748b;
        color: #94a3b8;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. 상단 스탯 대시보드
# -----------------------------------------------------------------------------
curr_title_name = TITLES_DB[st.session_state.equipped_title]["name"]

col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
with col1:
    st.markdown(f'''
        <div class="stat-card">
            <div class="stat-title">💳 보유 골드</div>
            <div class="stat-value">{st.session_state.money:,} G</div>
        </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
        <div class="stat-card">
            <div class="stat-title">💧 지온의 눈물</div>
            <div class="stat-value">{st.session_state.tears} 개</div>
        </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
        <div class="stat-card">
            <div class="stat-title">👑 장착 칭호</div>
            <div class="stat-value" style="font-size: 15px; color: #fde68a;">[{curr_title_name}]</div>
        </div>
    ''', unsafe_allow_html=True)

with col4:
    sp, fp, dp = PROB_TABLE[st.session_state.level] if st.session_state.level < 30 else (0,0,0)
    crit_pct = int(CRITICAL_RATE * 100)
    prob_str = "100% (DEV)" if st.session_state.dev_mode else f"{sp}% / {crit_pct}% / {dp}%"
    st.markdown(f'''
        <div class="stat-card">
            <div class="stat-title">📊 성공 / ⚡크리 / 파괴</div>
            <div class="stat-value" style="font-size: 16px;">{prob_str}</div>
        </div>
    ''', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 7. 메인 2칼럼 레이아웃
# -----------------------------------------------------------------------------
left_col, right_col = st.columns([3, 7])

with left_col:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top:0; font-size: 20px; color:#fde68a;'>🏰 왕도 판타지 지온 강화</h3>", unsafe_allow_html=True)
    
    if st.button("🔥 GOD MODE 강화 실행", use_container_width=True, disabled=(st.session_state.level >= 30)):
        enhance()
        st.rerun()
        
    st.write("")
    if st.button("💰 현재 냄새 판매", use_container_width=True, disabled=(st.session_state.level == 0)):
        sell()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top:0; font-size: 16px; color:#e2e8f0;'>⚙️ 모드 설정</h4>", unsafe_allow_html=True)
    st.caption("🛡️ 파괴 방지권은 보유 시 파괴 실패 상황에서 자동으로 차감되어 방어됩니다.")
    st.session_state.dev_mode = st.toggle("🛠️ 개발자 테스트 모드 (100% 성공)", value=st.session_state.dev_mode)
    if st.session_state.dev_mode:
        st.caption("⚠️ 치트 모드가 활성화되었습니다.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top:0; font-size: 16px; color:#e2e8f0;'>🛒 상점 및 업적센터</h4>", unsafe_allow_html=True)
    
    tab_shop1, tab_shop2, tab_achieve, tab_title = st.tabs(["🛡️ 상점", "💧 눈물", "🏆 업적", "👑 칭호"])
    with tab_shop1:
        st.caption("파괴 방지권 (보유 시 자동 발동)")
        if st.button("구매 (50,000 G)", use_container_width=True):
            if st.session_state.money >= 50000:
                st.session_state.money -= 50000
                st.session_state.shield += 1
                st.success("보호권 보유 중!")
                st.rerun()
            else:
                st.error("골드가 부족합니다.")
                
    with tab_shop2:
        st.caption("눈물 15개로 1단계 확정 상승")
        if st.button("1단계 확정 상승 (15개)", use_container_width=True):
            if st.session_state.tears >= 15 and st.session_state.level < 30:
                st.session_state.tears -= 15
                st.session_state.level += 1
                st.session_state.status = "SUCCESS"
                st.success("확정 강화 성공!")
                check_achievements()
                st.rerun()
            else:
                st.error("조건이 부족합니다.")

    with tab_achieve:
        st.caption("업적을 달성하면 골드 보상을 받습니다.")
        for key, info in ACHIEVEMENTS_DB.items():
            is_unlocked = key in st.session_state.unlocked_achievements
            badge_html = f'<span class="badge-unlocked">달성 완료</span>' if is_unlocked else f'<span class="badge-locked">미달성</span>'
            st.markdown(f"""
            <div style="font-size:13px; margin-bottom:8px; padding:6px; background:rgba(0,0,0,0.2); border-radius:8px;">
                <b>{info['badge']} {info['title']}</b> {badge_html}<br/>
                <span style="color:#cbd5e1; font-size:11px;">{info['desc']} (+{info['reward_gold']:,} G)</span>
            </div>
            """, unsafe_allow_html=True)

    with tab_title:
        st.caption("해금된 칭호를 선택하여 착용하세요.")
        available_titles = ["none"] + [k for k in st.session_state.unlocked_achievements if k in TITLES_DB]
        selected_title = st.selectbox(
            "칭호 선택", 
            options=available_titles, 
            format_func=lambda x: f"{TITLES_DB[x]['name']}",
            index=available_titles.index(st.session_state.equipped_title) if st.session_state.equipped_title in available_titles else 0
        )
        if selected_title != st.session_state.equipped_title:
            st.session_state.equipped_title = selected_title
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    # -----------------------------------------------------------------------------
    # 8. 강화된 시각 연출 및 3D 연출 Three.js
    # -----------------------------------------------------------------------------
    curr_data = SMELL_DB[st.session_state.level]
    card_color = curr_data['color']
    card_title = curr_data['name']
    card_desc = curr_data['desc']
    card_price = f"{curr_data['price']:,} G"
    tier = curr_data['tier']
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
                bottom: 60px; 
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                text-align: center;
                z-index: 100;
                pointer-events: none;
            }}

            .equipped-title-badge {{
                display: inline-block;
                padding: 4px 16px;
                background: rgba(251, 191, 36, 0.2);
                border: 1px solid #fbbf24;
                border-radius: 20px;
                color: #fde68a;
                font-size: 14px;
                font-weight: 800;
                margin-bottom: 8px;
                box-shadow: 0 0 10px rgba(251, 191, 36, 0.4);
            }}

            .title-tier-1 {{ font-size: 38px; font-weight: 900; color: #fde68a; text-shadow: 0 0 25px #fde68a; }}
            .title-tier-2 {{ font-size: 44px; font-weight: 900; color: #f59e0b; text-shadow: 0 0 30px #f59e0b; letter-spacing: 1px; }}
            .title-tier-3 {{ font-size: 50px; font-weight: 900; color: #ef4444; text-shadow: 0 0 35px #ef4444; animation: pulse 1s infinite alternate; }}
            .title-tier-4 {{ font-size: 56px; font-weight: 900; color: #c084fc; text-shadow: 0 0 40px #c084fc; letter-spacing: 2px; }}
            .title-tier-5 {{ font-size: 62px; font-weight: 900; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 40px #ff7e5f); animation: shake 0.5s infinite alternate; }}
            .title-tier-6 {{ font-size: 68px; font-weight: 900; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; filter: drop-shadow(0 0 50px #ffffff); }}

            @keyframes pulse {{ 0% {{ transform: scale(1); }} 100% {{ transform: scale(1.04); }} }}
            @keyframes shake {{ 0% {{ transform: translate(2px, 2px); }} 100% {{ transform: translate(-2px, -2px); }} }}
            @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}

            .status-header {{ font-size: 20px; font-weight: 800; margin-bottom: 8px; letter-spacing: 4px; }}
            .desc-text {{ font-size: 15px; color: #f3e8ff; margin-top: 8px; text-shadow: 0 2px 10px rgba(0,0,0,0.8); }}
            .price-text {{ font-size: 22px; font-weight: 800; color: #fbbf24; margin-top: 8px; text-shadow: 0 0 20px rgba(251,191,36,0.6); }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="redFlashOverlay"></div>
        <div id="shieldFlashOverlay"></div>
        <div id="critFlashOverlay"></div>
        <div id="successFlashOverlay"></div>
        <div id="container"></div>

        <div class="cinematic-ui">
            <div class="equipped-title-badge">🎖️ {curr_title_name}</div>
            <div id="statusText" class="status-header">READY</div>
            <div class="title-tier-{tier}">
                {card_title}
            </div>
            <div class="desc-text">"{card_desc}"</div>
            <div class="price-text">예상 가치: {card_price}</div>
        </div>

        <script>
            const status = "{status}";
            const statusText = document.getElementById('statusText');
            const flashOverlay = document.getElementById('redFlashOverlay');
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
                statusText.innerText = "🔻 ENHANCE FAILED 🔻";
                statusText.style.color = "#f59e0b";
            }}

            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x231133, 0.025);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 1.2, 9);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.getElementById('container').appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xd8b4fe, 0.9);
            scene.add(ambientLight);

            const sunsetLight = new THREE.DirectionalLight(0xf59e0b, 1.5);
            sunsetLight.position.set(5, 5, 5);
            scene.add(sunsetLight);

            const cardPointLight = new THREE.PointLight("{card_color}", 6, 20);
            cardPointLight.position.set(0, 2, 4);
            scene.add(cardPointLight);

            // ✨ 황금빛 노을 입자
            const particleGroup = new THREE.Group();
            const pCount = 1500;
            const pGeo = new THREE.BufferGeometry();
            const pPos = new Float32Array(pCount * 3);

            for(let i=0; i<pCount; i++) {{
                pPos[i*3] = (Math.random() - 0.5) * 25;
                pPos[i*3 + 1] = Math.random() * 15 - 5;
                pPos[i*3 + 2] = (Math.random() - 0.5) * 25;
            }}

            pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
            const pMat = new THREE.PointsMaterial({{
                color: 0xfde68a, size: 0.18, transparent: true, opacity: 0.6, blending: THREE.AdditiveBlending
            }});
            const particles = new THREE.Points(pGeo, pMat);
            particleGroup.add(particles);
            scene.add(particleGroup);

            // 💳 아티팩트 카드
            const cardGroup = new THREE.Group();

            const frameGeo = new THREE.BoxGeometry(2.9, 4.3, 0.2);
            const frameMat = new THREE.MeshStandardMaterial({{ color: 0x2e1045, metalness: 0.85, roughness: 0.25 }});
            const frame = new THREE.Mesh(frameGeo, frameMat);
            cardGroup.add(frame);

            const bodyGeo = new THREE.BoxGeometry(2.6, 4.0, 0.22);
            const bodyMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", metalness: 0.65, roughness: 0.3 }});
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            cardGroup.add(body);

            const coreGeo = new THREE.OctahedronGeometry(0.6, 0);
            const coreMat = new THREE.MeshStandardMaterial({{
                color: 0xffffff, emissive: "{card_color}", emissiveIntensity: 1.2, roughness: 0.1
            }});
            const core = new THREE.Mesh(coreGeo, coreMat);
            core.position.z = 0.16;
            cardGroup.add(core);

            scene.add(cardGroup);

            // 🛡️ 파괴 방지 보호막
            const shieldGeo = new THREE.SphereGeometry(2.8, 32, 32);
            const shieldMat = new THREE.MeshStandardMaterial({{
                color: 0x60a5fa, emissive: 0x2563eb, emissiveIntensity: 0.8, transparent: true, opacity: 0.0, wireframe: true
            }});
            const shieldDome = new THREE.Mesh(shieldGeo, shieldMat);
            shieldDome.position.y = 0.8;
            scene.add(shieldDome);

            // 💥 3D 파편 및 이펙트 그룹
            let shardsGroup = new THREE.Group();
            scene.add(shardsGroup);
            let explosionParticles = null;
            let explosionVelocities = [];

            // -----------------------------------------------------------------
            // 강화 및 연출 비주얼 효과
            // -----------------------------------------------------------------
            if (status === "SHIELD_SAVED") {{
                gsap.fromTo(shieldOverlay, {{ opacity: 0.8 }}, {{ opacity: 0, duration: 1.0, ease: "power2.out" }});
                gsap.fromTo(shieldMat, {{ opacity: 0.9, wireframe: true }}, {{ opacity: 0, duration: 1.5, ease: "power2.inOut" }});
                gsap.fromTo(shieldDome.scale, {{ x: 0.2, y: 0.2, z: 0.2 }}, {{ x: 1.2, y: 1.2, z: 1.2, duration: 0.8, ease: "back.out(1.7)" }});
                gsap.to(cardGroup.position, {{ z: -2, duration: 0.15, yoyo: true, repeat: 5 }});
            }} else if (status === "CRITICAL") {{
                gsap.fromTo(critOverlay, {{ opacity: 0.9 }}, {{ opacity: 0, duration: 1.0, ease: "power2.out" }});
                gsap.fromTo(camera.position, {{ z: 3 }}, {{ z: 9, duration: 1.5, ease: "bounce.out" }});
                gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 6, z: Math.PI * 2 }}, {{ y: 0, z: 0, duration: 1.5, ease: "power3.out" }});
            }} else if (status === "DESTROYED") {{
                gsap.fromTo(flashOverlay, {{ opacity: 0.85 }}, {{ opacity: 0, duration: 1.2, ease: "power2.out" }});
                gsap.to(camera.position, {{ x: 0.4, y: 1.6, duration: 0.04, repeat: 10, yoyo: true, onComplete: () => {{ camera.position.set(0, 1.2, 9); }} }});
                cardGroup.visible = false; // 카드 비활성화 후 3D 조각 폭발

                // 💥 3D 카드 파편 조각 생성 연출
                const shardCount = 20;
                for(let i = 0; i < shardCount; i++) {{
                    const sGeo = new THREE.TetrahedronGeometry(Math.random() * 0.4 + 0.2);
                    const sMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", roughness: 0.2 }});
                    const shard = new THREE.Mesh(sGeo, sMat);
                    shard.position.set(0, 0.8, 0);
                    shardsGroup.add(shard);

                    gsap.to(shard.position, {{
                        x: (Math.random() - 0.5) * 6,
                        y: (Math.random() - 0.5) * 6,
                        z: (Math.random() - 0.5) * 6,
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
                gsap.fromTo(camera.position, {{ z: 4 }}, {{ z: 9, duration: 1.2, ease: "power2.out" }});
                gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 2 }}, {{ y: 0, duration: 1.2, ease: "power2.out" }});
            }}

            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();

                // 입자 움직임
                const pos = pGeo.attributes.position.array;
                for(let i=1; i<pCount*3; i+=3) {{
                    pos[i] += Math.sin(time + pos[i-1]) * 0.005 + 0.008;
                    if(pos[i] > 10) pos[i] = -5;
                }}
                pGeo.attributes.position.needsUpdate = true;

                if (cardGroup.visible) {{
                    cardGroup.rotation.y = Math.sin(time * 0.8) * 0.2;
                    cardGroup.position.y = Math.sin(time * 1.5) * 0.12 + 0.8;
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

    components.html(three_js_code, height=680, scrolling=False)
