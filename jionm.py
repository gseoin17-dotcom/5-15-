import streamlit as st
import random
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="꼬질이 냄새 강화하기 - 1~30LV SMELL EVOLUTION",
    page_icon="🪰",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. 1~30단계 냄새 데이터베이스 (점진적 냄새 강화 설정)
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 씻고 나온 꼬질이", "desc": "아직은 비누 향이 살짝 남아있는 깨끗한 상태.", "price": 0, "color": "#a7f3d0", "tier": 1},
    1: {"name": "1단계 : 약간 땀 흘린 꼬질이", "desc": "가볍게 산책하고 온 정도. 약간 꿉꿉하다.", "price": 100, "color": "#86efac", "tier": 1},
    2: {"name": "2단계 : 꼬리꼬리한 발냄새", "desc": "신발을 벗으면 살짝 신경 쓰이는 냄새가 피어오른다.", "price": 300, "color": "#4ade80", "tier": 1},
    3: {"name": "3단계 : 안 씻은 지 3일째", "desc": "머리 기름이 지기 시작하며 냄새 연기가 피어난다.", "price": 700, "color": "#22c55e", "tier": 1},
    4: {"name": "4단계 : 묵힌 옷 장롱 냄새", "desc": "습기 찬 옷장에서 꺼내 입은 듯한 퀴퀴함.", "price": 1500, "color": "#16a34a", "tier": 1},
    5: {"name": "5단계 : 젖은 누더기 옷", "desc": "비에 젖은 채 말리지 않은 옷 냄새가 진동한다.", "price": 3500, "color": "#15803d", "tier": 1},
    6: {"name": "6단계 : 초파리 1기 유입", "desc": "주변에 초파리 한두 마리가 꼬이기 시작한다.", "price": 8000, "color": "#ca8a04", "tier": 2},
    7: {"name": "7단계 : 상한 우유 오염", "desc": "옷에 쏟은 상한 우유가 찌들어 시큼한 냄새가 난다.", "price": 18000, "color": "#a16207", "tier": 2},
    8: {"name": "8단계 : 음식물 쓰레기 봉투", "desc": "여름철 하루 동안 방치된 음쓰의 진한 향기.", "price": 40000, "color": "#854d0e", "tier": 2},
    9: {"name": "9단계 : 퀴퀴한 하수구 악취", "desc": "하수도 깊은 곳에서 올라오는 유황 악취.", "price": 90000, "color": "#713f12", "tier": 2},
    10: {"name": "10단계 : 초파리 군단 형성", "desc": "꼬질이 주위에 초파리 떼가 둥둥 떠다닌다.", "price": 200000, "color": "#65a30d", "tier": 2},
    11: {"name": "11단계 : 청국장 축제장", "desc": "사방 10미터까지 구수하다 못해 매운 청국장 향.", "price": 450000, "color": "#4d7c0f", "tier": 3},
    12: {"name": "12단계 : 방치된 청어 통조림", "desc": "수르스트뢰밍을 개봉한 것 같은 충격적인 악취.", "price": 1000000, "color": "#3f6212", "tier": 3},
    13: {"name": "13단계 : 녹색 구름 생성기", "desc": "냄새가 시각화되어 녹색 악취 구름이 뿜어져 나온다.", "price": 2200000, "color": "#365314", "tier": 3},
    14: {"name": "14단계 : 생화학 테러급 폭탄", "desc": "스쳐 지나가기만 해도 눈물이 고이고 코가 찡하다.", "price": 5000000, "color": "#d97706", "tier": 3},
    15: {"name": "15단계 : 눈이 매워지는 독성 악취", "desc": "눈을 뜰 수 없을 정도의 가스가 주변을 채운다.", "price": 12000000, "color": "#b45309", "tier": 3},
    16: {"name": "16단계 : 초파리 대염공 스웜", "desc": "수십 마리의 초파리가 소용돌이치며 열풍을 만든다.", "price": 30000000, "color": "#78350f", "tier": 4},
    17: {"name": "17단계 : 보랏빛 오염 지대", "desc": "냄새 입자가 변이하여 보랏빛 독성 오라가 된다.", "price": 75000000, "color": "#9333ea", "tier": 4},
    18: {"name": "18단계 : 만물 부패 촉진제", "desc": "꼬질이가 닿는 모든 물건이 썩기 시작한다.", "price": 180000000, "color": "#7e22ce", "tier": 4},
    19: {"name": "19단계 : 시공간 왜곡 악취", "desc": "냄새가 너무 심해 주변 공간이 왜곡되어 일렁인다.", "price": 450000000, "color": "#6b21a8", "tier": 4},
    20: {"name": "20단계 : ★재앙급 꼬질이★", "desc": "도시 하나를 마비시킬 수 있는 절대적 악취 대폭발.", "price": 1000000000, "color": "#581c87", "tier": 4},
    21: {"name": "21단계 : 대륙 봉쇄급 냄새", "desc": "인공위성에서도 관측되는 커다란 냄새 구름.", "price": 2500000000, "color": "#f43f5e", "tier": 5},
    22: {"name": "22단계 : 썩은 달걀의 권능", "desc": "황화수소 입자가 우주까지 퍼져나간다.", "price": 6000000000, "color": "#e11d48", "tier": 5},
    23: {"name": "23단계 : 방사능 꼬질이 오염", "desc": "형광 초록빛 유독 가스가 시야를 완전히 가린다.", "price": 15000000000, "color": "#be123c", "tier": 5},
    24: {"name": "24단계 : 은하계 악취 유성우", "desc": "파리 떼가 은하수처럼 캐릭터 주위를 선회한다.", "price": 40000000000, "color": "#9f1239", "tier": 5},
    25: {"name": "25단계 : 자이온맘도 도망친 악취", "desc": "자이온맘조차 코를 막고 뒷걸음질 치는 냄새.", "price": 100000000000, "color": "#881337", "tier": 5},
    26: {"name": "26단계 : 차원 파괴급 꼬질 기운", "desc": "차원의 벽을 뚫고 이세계로 악취가 뿜어져 나온다.", "price": 250000000000, "color": "#4c1d95", "tier": 6},
    27: {"name": "27단계 : 코마 상태 유발 폭풍", "desc": "냄새를 맡은 모든 생명체가 즉시 기절한다.", "price": 600000000000, "color": "#3b0764", "tier": 6},
    28: {"name": "28단계 : 멸망의 꼬질이 오라", "desc": "지구 행성 전체가 보랏빛 냄새 구름에 잠긴다.", "price": 1500000000000, "color": "#2e1065", "tier": 6},
    29: {"name": "29단계 : 태초의 부패 신", "desc": "우주가 생겨나기 전 존재했던 태초의 냄새.", "price": 4000000000000, "color": "#f43f5e", "tier": 6},
    30: {"name": "30단계 : ★악취의 절대신 꼬질이★", "desc": "모든 우주 공간을 단 하나의 꼬질이 냄새로 통일!", "price": 10000000000000, "color": "#000000", "tier": 6}
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

# -----------------------------------------------------------------------------
# 3. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
    st.session_state.level = 0
if "money" not in st.session_state:
    st.session_state.money = 10000
if "status" not in st.session_state:
    st.session_state.status = "READY"
if "shield" not in st.session_state:
    st.session_state.shield = 0  
if "tears" not in st.session_state:
    st.session_state.tears = 0    
if "dev_mode" not in st.session_state:
    st.session_state.dev_mode = False

# -----------------------------------------------------------------------------
# 4. 강화 / 판매 로직
# -----------------------------------------------------------------------------
def enhance():
    curr = st.session_state.level
    if curr >= 30: return
    
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
        if curr > 0: st.session_state.level -= 1
        st.session_state.status = "FAILED"
        st.session_state.tears += 1

def sell():
    curr = st.session_state.level
    if curr == 0: return
    st.session_state.money += SMELL_DB[curr]['price']
    st.session_state.level = 0
    st.session_state.status = "READY"

# -----------------------------------------------------------------------------
# 5. UI CSS
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 30%, #152219 0%, #0b140e 60%, #030805 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    .glass-panel {
        background: rgba(18, 35, 24, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(74, 222, 128, 0.2);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
    }

    .stat-card {
        background: rgba(22, 45, 30, 0.5);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(74, 222, 128, 0.3);
        padding: 12px 10px;
        border-radius: 12px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .stat-card:hover {
        border-color: rgba(74, 222, 128, 0.7);
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.3);
    }
    .stat-title {
        font-size: 13px;
        font-weight: 600;
        color: #86efac;
        margin-bottom: 4px;
        letter-spacing: 0.5px;
    }
    .stat-value {
        font-size: 19px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(74, 222, 128, 0.4);
    }

    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease !important;
        border: 1px solid rgba(74, 222, 128, 0.3) !important;
        background: linear-gradient(135deg, rgba(22, 101, 52, 0.6), rgba(101, 163, 13, 0.6)) !important;
        color: #ffffff !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(74, 222, 128, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. 상단 스탯 대시보드
# -----------------------------------------------------------------------------
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
            <div class="stat-title">🛡️ 파괴 방지권 (자동사용)</div>
            <div class="stat-value">{st.session_state.shield} 개</div>
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
    st.markdown("<h3 style='margin-top:0; font-size: 20px; color:#86efac;'>🪰 꼬질이 냄새 강화</h3>", unsafe_allow_html=True)
    
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
    st.caption("🛡️ 파괴 방지권은 보유 시 실패 시 자동으로 작동합니다.")
    st.session_state.dev_mode = st.toggle("🛠️ 개발자 테스트 모드 (100% 성공)", value=st.session_state.dev_mode)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top:0; font-size: 16px; color:#e2e8f0;'>🛒 상점</h4>", unsafe_allow_html=True)
    
    tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])
    with tab_shop1:
        if st.button("구매 (50,000 G)", use_container_width=True):
            if st.session_state.money >= 50000:
                st.session_state.money -= 50000
                st.session_state.shield += 1
                st.success("보호권 보유 중!")
                st.rerun()
            else:
                st.error("골드가 부족합니다.")
                
    with tab_shop2:
        if st.button("1단계 확정 상승 (15개)", use_container_width=True):
            if st.session_state.tears >= 15 and st.session_state.level < 30:
                st.session_state.tears -= 15
                st.session_state.level += 1
                st.session_state.status = "SUCCESS"
                st.success("확정 강화 성공!")
                st.rerun()
            else:
                st.error("조건이 부족합니다.")
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    # -----------------------------------------------------------------------------
    # 8. 꼬질이 3D 그래픽 및단계별 냄새 파티클 스웜 연출 Three.js
    # -----------------------------------------------------------------------------
    curr_level = st.session_state.level
    curr_data = SMELL_DB[curr_level]
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
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(239, 68, 68, 0.85);
                box-shadow: inset 0 0 120px rgba(185, 28, 28, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            #shieldFlashOverlay {{
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(59, 130, 246, 0.7);
                box-shadow: inset 0 0 100px rgba(37, 99, 235, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            #critFlashOverlay {{
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(245, 158, 11, 0.85);
                box-shadow: inset 0 0 120px rgba(217, 119, 6, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            .cinematic-ui {{
                position: absolute;
                bottom: 50px; 
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                text-align: center;
                z-index: 100;
                pointer-events: none;
            }}

            .title-tier-1 {{ font-size: 36px; font-weight: 900; color: #86efac; text-shadow: 0 0 25px #86efac; }}
            .title-tier-2 {{ font-size: 42px; font-weight: 900; color: #facc15; text-shadow: 0 0 30px #facc15; letter-spacing: 1px; }}
            .title-tier-3 {{ font-size: 48px; font-weight: 900; color: #ca8a04; text-shadow: 0 0 35px #ca8a04; animation: pulse 1s infinite alternate; }}
            .title-tier-4 {{ font-size: 54px; font-weight: 900; color: #a855f7; text-shadow: 0 0 40px #a855f7; letter-spacing: 2px; }}
            .title-tier-5 {{ font-size: 60px; font-weight: 900; background: linear-gradient(90deg, #f43f5e, #be123c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 40px #f43f5e); animation: shake 0.5s infinite alternate; }}
            .title-tier-6 {{ font-size: 66px; font-weight: 900; background: linear-gradient(90deg, #ffffff, #a855f7, #f43f5e, #22c55e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; filter: drop-shadow(0 0 50px #ffffff); }}

            @keyframes pulse {{ 0% {{ transform: scale(1); }} 100% {{ transform: scale(1.04); }} }}
            @keyframes shake {{ 0% {{ transform: translate(2px, 2px); }} 100% {{ transform: translate(-2px, -2px); }} }}
            @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}

            .status-header {{ font-size: 20px; font-weight: 800; margin-bottom: 8px; letter-spacing: 4px; }}
            .desc-text {{ font-size: 15px; color: #e2e8f0; margin-top: 8px; text-shadow: 0 2px 10px rgba(0,0,0,0.8); }}
            .price-text {{ font-size: 22px; font-weight: 800; color: #fbbf24; margin-top: 8px; text-shadow: 0 0 20px rgba(251,191,36,0.6); }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="redFlashOverlay"></div>
        <div id="shieldFlashOverlay"></div>
        <div id="critFlashOverlay"></div>
        <div id="container"></div>

        <div class="cinematic-ui">
            <div id="statusText" class="status-header">READY</div>
            <div class="title-tier-{tier}">
                {card_title}
            </div>
            <div class="desc-text">"{card_desc}"</div>
            <div class="price-text">예상 가치: {card_price}</div>
        </div>

        <script>
            const level = {curr_level};
            const status = "{status}";
            const statusText = document.getElementById('statusText');
            const flashOverlay = document.getElementById('redFlashOverlay');
            const shieldOverlay = document.getElementById('shieldFlashOverlay');
            const critOverlay = document.getElementById('critFlashOverlay');
            
            if (status === "CRITICAL") {{
                statusText.innerText = "⚡ CRITICAL HIT!! (+2단계 대성공) ⚡";
                statusText.style.color = "#ffe600";
            }} else if (status === "SUCCESS") {{
                statusText.innerText = "✨ ENHANCE SUCCESS ✨";
                statusText.style.color = "#4ade80";
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
            scene.fog = new THREE.FogExp2(0x0c1a11, 0.035);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 1.2, 9);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.getElementById('container').appendChild(renderer.domElement);

            // 조명
            const ambientLight = new THREE.AmbientLight(0xdcfce7, 0.9);
            scene.add(ambientLight);

            const cardLight = new THREE.PointLight("{card_color}", 5 + (level * 0.3), 20);
            cardLight.position.set(0, 2, 4);
            scene.add(cardLight);

            // -----------------------------------------------------------------
            // 🪰 1~30단계 점진적 냄새 파티클 시스템
            // -----------------------------------------------------------------
            const smellParticlesCount = Math.min(80 + (level * 50), 1600); // LV30 -> 1600개
            const pGeo = new THREE.BufferGeometry();
            const pPos = new Float32Array(smellParticlesCount * 3);
            const pSpeeds = [];

            for(let i=0; i<smellParticlesCount; i++) {{
                pPos[i*3] = (Math.random() - 0.5) * (4 + level * 0.3);
                pPos[i*3 + 1] = (Math.random() - 0.5) * (5 + level * 0.3);
                pPos[i*3 + 2] = (Math.random() - 0.5) * (4 + level * 0.3);
                pSpeeds.push({{
                    x: (Math.random() - 0.5) * (0.005 + level * 0.001),
                    y: Math.random() * (0.01 + level * 0.002) + 0.005,
                    z: (Math.random() - 0.5) * (0.005 + level * 0.001)
                }});
            }}

            pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
            
            // 단계가 올라갈수록 연두 -> 황록 -> 자줏빛 독성 오라로 변이
            const pMat = new THREE.PointsMaterial({{
                color: "{card_color}",
                size: 0.15 + (level * 0.012),
                transparent: true,
                opacity: Math.min(0.3 + (level * 0.02), 0.85),
                blending: THREE.AdditiveBlending
            }});
            const smellCloud = new THREE.Points(pGeo, pMat);
            scene.add(smellCloud);

            // -----------------------------------------------------------------
            // 🪰 초파리 스웜 (LV 6 이상부터 등장, LV 30에서 대군단)
            # -----------------------------------------------------------------
            const flyCount = level >= 6 ? Math.min((level - 5) * 2, 50) : 0;
            const flyGroup = new THREE.Group();
            const flyData = [];

            if (flyCount > 0) {{
                const flyGeo = new THREE.BoxGeometry(0.06, 0.04, 0.06);
                const flyMat = new THREE.MeshBasicMaterial({{ color: 0x111111 }});

                for(let i=0; i<flyCount; i++) {{
                    const fly = new THREE.Mesh(flyGeo, flyMat);
                    flyGroup.add(fly);
                    flyData.push({{
                        mesh: fly,
                        angle: Math.random() * Math.PI * 2,
                        radius: 1.5 + Math.random() * 2.0,
                        speed: 0.03 + Math.random() * 0.05,
                        heightSpeed: 0.02 + Math.random() * 0.03,
                        heightOffset: Math.random() * Math.PI * 2
                    }});
                }}
                scene.add(flyGroup);
            }}

            // -----------------------------------------------------------------
            // 🖼️ 3D 꼬질이 캔버스 텍스처 생성기
            // -----------------------------------------------------------------
            function createGgojilTexture() {{
                const canvas = document.createElement('canvas');
                canvas.width = 512; canvas.height = 768;
                const ctx = canvas.getContext('2d');

                // 캐릭터 배경
                ctx.fillStyle = "#e2e8f0";
                ctx.fillRect(0, 0, 512, 768);

                // 꼬질이 몸체
                ctx.fillStyle = "#86efac";
                ctx.beginPath();
                ctx.ellipse(256, 420, 160, 220, 0, 0, Math.PI * 2);
                ctx.fill();
                ctx.lineWidth = 10; ctx.strokeStyle = "#166534"; ctx.stroke();

                // 꼬질이 눈
                ctx.fillStyle = "#ffffff";
                ctx.beginPath(); ctx.ellipse(200, 360, 35, 20, 0, 0, Math.PI*2); ctx.fill(); ctx.stroke();
                ctx.beginPath(); ctx.ellipse(312, 360, 35, 20, 0, 0, Math.PI*2); ctx.fill(); ctx.stroke();

                ctx.fillStyle = "#1e293b";
                ctx.beginPath(); ctx.arc(200, 365, 12, 0, Math.PI*2); ctx.fill();
                ctx.beginPath(); ctx.arc(312, 365, 12, 0, Math.PI*2); ctx.fill();

                // 메롱 입
                ctx.fillStyle = "#f43f5e";
                ctx.beginPath(); ctx.arc(256, 420, 30, 0, Math.PI); ctx.fill(); ctx.stroke();

                // 얼룩 때 (단계에 따라 증가)
                ctx.fillStyle = "rgba(101, 67, 33, 0.6)";
                for(let i=0; i < 5 + level; i++) {{
                    ctx.beginPath();
                    ctx.arc(150 + (i*45)%200, 250 + (i*60)%350, 15 + (i%5)*8, 0, Math.PI*2);
                    ctx.fill();
                }}

                return new THREE.CanvasTexture(canvas);
            }}

            const cardTexture = createGgojilTexture();

            // -----------------------------------------------------------------
            // 💳 3D 카드 메시
            // -----------------------------------------------------------------
            const cardGroup = new THREE.Group();

            const frameGeo = new THREE.BoxGeometry(2.9, 4.3, 0.2);
            const frameMat = new THREE.MeshStandardMaterial({{ color: 0x14281d, metalness: 0.85, roughness: 0.25 }});
            const frame = new THREE.Mesh(frameGeo, frameMat);
            cardGroup.add(frame);

            const bodyGeo = new THREE.BoxGeometry(2.6, 4.0, 0.22);
            const bodyMat = new THREE.MeshStandardMaterial({{ map: cardTexture, roughness: 0.4 }});
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            cardGroup.add(body);

            scene.add(cardGroup);

            // 🛡️ 방어막
            const shieldGeo = new THREE.SphereGeometry(2.8, 32, 32);
            const shieldMat = new THREE.MeshStandardMaterial({{
                color: 0x60a5fa,
                emissive: 0x2563eb,
                emissiveIntensity: 0.8,
                transparent: true,
                opacity: 0.0,
                wireframe: true
            }});
            const shieldDome = new THREE.Mesh(shieldGeo, shieldMat);
            shieldDome.position.y = 0.8;
            scene.add(shieldDome);

            let explosionParticles = null;
            let explosionVelocities = [];

            // -----------------------------------------------------------------
            // 강화 연출
            // -----------------------------------------------------------------
            if (status === "SHIELD_SAVED") {{
                gsap.fromTo(shieldOverlay, {{ opacity: 0.8 }}, {{ opacity: 0, duration: 1.0, ease: "power2.out" }});
                gsap.fromTo(shieldMat, 
                    {{ opacity: 0.9, wireframe: true }}, 
                    {{ opacity: 0, duration: 1.5, ease: "power2.inOut" }}
                );
                gsap.fromTo(shieldDome.scale, 
                    {{ x: 0.2, y: 0.2, z: 0.2 }}, 
                    {{ x: 1.2, y: 1.2, z: 1.2, duration: 0.8, ease: "back.out(1.7)" }}
                );
                gsap.to(cardGroup.position, {{ z: -2, duration: 0.15, yoyo: true, repeat: 5 }});
            }} else if (status === "CRITICAL") {{
                gsap.fromTo(critOverlay, {{ opacity: 0.9 }}, {{ opacity: 0, duration: 1.0, ease: "power2.out" }});
                gsap.fromTo(camera.position, {{ z: 3 }}, {{ z: 9, duration: 1.5, ease: "bounce.out" }});
                gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 4, z: Math.PI * 2 }}, {{ y: 0, z: 0, duration: 1.5, ease: "power3.out" }});
            }} else if (status === "DESTROYED") {{
                gsap.fromTo(flashOverlay, {{ opacity: 0.85 }}, {{ opacity: 0, duration: 1.2, ease: "power2.out" }});
                gsap.to(camera.position, {{ x: 0.4, y: 1.6, duration: 0.04, repeat: 10, yoyo: true, onComplete: () => {{ camera.position.set(0, 1.2, 9); }} }});
                gsap.to(cardGroup.scale, {{ x: 0, y: 0, z: 0, duration: 0.25, ease: "power4.in" }});

                const expCount = 600;
                const expGeo = new THREE.BufferGeometry();
                const expPos = new Float32Array(expCount * 3);

                for (let i = 0; i < expCount; i++) {{
                    expPos[i * 3] = 0; expPos[i * 3 + 1] = 0.8; expPos[i * 3 + 2] = 0;
                    const theta = Math.random() * Math.PI * 2;
                    const phi = Math.acos((Math.random() * 2) - 1);
                    const speed = Math.random() * 0.35 + 0.1;
                    explosionVelocities.push({{
                        x: speed * Math.sin(phi) * Math.cos(theta),
                        y: speed * Math.sin(phi) * Math.sin(theta),
                        z: speed * Math.cos(phi)
                    }});
                }}

                expGeo.setAttribute('position', new THREE.BufferAttribute(expPos, 3));
                const expMat = new THREE.PointsMaterial({{ color: 0xef4444, size: 0.22, transparent: true, opacity: 1.0 }});
                explosionParticles = new THREE.Points(expGeo, expMat);
                scene.add(explosionParticles);
            }} else if (status === "SUCCESS") {{
                gsap.fromTo(camera.position, {{ z: 4 }}, {{ z: 9, duration: 1.2, ease: "power2.out" }});
                gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 2 }}, {{ y: 0, duration: 1.2, ease: "power2.out" }});
            }}

            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();

                // 냄새 파티클 상승 및 무작위 이동
                const pos = pGeo.attributes.position.array;
                for(let i=0; i<smellParticlesCount; i++) {{
                    pos[i*3] += pSpeeds[i].x;
                    pos[i*3 + 1] += pSpeeds[i].y;
                    pos[i*3 + 2] += pSpeeds[i].z;

                    if(pos[i*3 + 1] > 3.5) {{
                        pos[i*3 + 1] = -2.5;
                        pos[i*3] = (Math.random() - 0.5) * (4 + level * 0.3);
                    }}
                }}
                pGeo.attributes.position.needsUpdate = true;

                // 초파리 스웜 회전 회오리 연출
                flyData.forEach(fd => {{
                    fd.angle += fd.speed;
                    fd.mesh.position.x = Math.cos(fd.angle) * fd.radius;
                    fd.mesh.position.z = Math.sin(fd.angle) * fd.radius;
                    fd.mesh.position.y = Math.sin(time * 5 + fd.heightOffset) * 0.8 + 0.8;
                }});

                // 고단계 악취 시 왜곡 흔들림 효과
                if(level >= 18) {{
                    cardGroup.rotation.z = Math.sin(time * 12) * (level * 0.003);
                }} else {{
                    cardGroup.rotation.z = 0;
                }}

                cardGroup.rotation.y = Math.sin(time * 0.8) * 0.2;
                cardGroup.position.y = Math.sin(time * 1.5) * 0.12 + 0.8;

                if (explosionParticles) {{
                    const ePos = explosionParticles.geometry.attributes.position.array;
                    for (let i = 0; i < explosionVelocities.length; i++) {{
                        ePos[i * 3] += explosionVelocities[i].x;
                        ePos[i * 3 + 1] += explosionVelocities[i].y;
                        ePos[i * 3 + 2] += explosionVelocities[i].z;
                    }}
                    explosionParticles.geometry.attributes.position.needsUpdate = true;
                    explosionParticles.material.opacity *= 0.95;
                }}

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
