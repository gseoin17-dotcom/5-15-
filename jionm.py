import streamlit as st
import random
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - GOD MODE 3D",
    page_icon="👑",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. 게임 데이터베이스 및 강화 확률표
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
if "use_shield" not in st.session_state:
    st.session_state.use_shield = False
if "dev_mode" not in st.session_state:
    st.session_state.dev_mode = False

# -----------------------------------------------------------------------------
# 4. 강화 / 판매 로직
# -----------------------------------------------------------------------------
def enhance():
    curr = st.session_state.level
    if curr >= 30: return
    
    # 개발자 모드 켜진 경우 무조건 성공
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
        if st.session_state.use_shield and st.session_state.shield > 0:
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
# 5. 상단 대시보드 Style 및 현황
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp { background-color: #020403; color: #fff; }
    
    .stat-card {
        background: rgba(15, 23, 42, 0.95);
        border: 1.5px solid #00f0ff;
        padding: 8px 6px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 12px rgba(0, 240, 255, 0.3);
    }
    .stat-title {
        font-size: 13px;
        font-weight: 500;
        color: #cbd5e1;
        margin-bottom: 2px;
    }
    .stat-value {
        font-size: 18px;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 6px rgba(255, 255, 255, 0.4);
    }
    .ctrl-box {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 18px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
with col1:
    st.markdown(f'''
        <div class="stat-card">
            <div class="stat-title">💰 보유 골드</div>
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
            <div class="stat-title">🛡️ 파괴 방지권</div>
            <div class="stat-value">{st.session_state.shield} 개</div>
        </div>
    ''', unsafe_allow_html=True)

with col4:
    sp, fp, dp = PROB_TABLE[st.session_state.level] if st.session_state.level < 30 else (0,0,0)
    crit_pct = int(CRITICAL_RATE * 100)
    prob_str = "100% (DEV)" if st.session_state.dev_mode else f"{sp}% / {crit_pct}% / {dp}%"
    st.markdown(f'''
        <div class="stat-card">
            <div class="stat-title">📊 성공 / ⚡크리티컬 / 파괴</div>
            <div class="stat-value" style="font-size: 16px;">{prob_str}</div>
        </div>
    ''', unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 6. 메인 레이아웃 (왼쪽 조작 패널 / 오른쪽 3D 스테이지)
# -----------------------------------------------------------------------------
left_col, right_col = st.columns([3, 7])

with left_col:
    st.markdown("### 🎮 조작 컨트롤러")
    
    # 조작 버튼 그룹
    if st.button("🔥 GOD MODE 강화 실행", use_container_width=True, disabled=(st.session_state.level >= 30)):
        enhance()
        st.rerun()
        
    if st.button("💰 현재 냄새 판매", use_container_width=True, disabled=(st.session_state.level == 0)):
        sell()
        st.rerun()

    st.write("---")
    st.session_state.use_shield = st.checkbox("🛡️ 강화 시 파괴 방지권 자동 사용", value=st.session_state.use_shield)
    
    # 개발자 모드 토글 스위치
    st.session_state.dev_mode = st.toggle("🛠️ 개발자 모드: 무조건 성공", value=st.session_state.dev_mode)
    if st.session_state.dev_mode:
        st.caption("⚠️ 개발자 테스트 모드가 활성화되어 모든 강화가 100% 성공합니다.")

    st.write("---")
    st.markdown("#### 🛒 상점 & 아이템")
    
    tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])
    with tab_shop1:
        st.write("강화 실패 시 카드가 파괴되어 0단계가 되는 것을 막아줍니다.")
        if st.button("구매 (50,000 G)", use_container_width=True):
            if st.session_state.money >= 50000:
                st.session_state.money -= 50000
                st.session_state.shield += 1
                st.success("파괴 방지권 1개 구매 완료!")
                st.rerun()
            else:
                st.error("골드가 부족합니다.")
                
    with tab_shop2:
        st.write("강화 실패 시 쌓이는 눈물로 확정 상승시킵니다.")
        if st.button("1단계 확정 상승 (눈물 15개)", use_container_width=True):
            if st.session_state.tears >= 15 and st.session_state.level < 30:
                st.session_state.tears -= 15
                st.session_state.level += 1
                st.session_state.status = "SUCCESS"
                st.success("1단계 확정 강화 성공!")
                st.rerun()
            else:
                st.error("눈물이 부족하거나 최고 단계입니다.")

with right_col:
    # -----------------------------------------------------------------------------
    # 7. 3D Render & 오버레이 연출 (입체 아티팩트 코어 카드 + 워프 터널 배경)
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
            body {{ margin: 0; overflow: hidden; background: #000; font-family: 'Black Han Sans', 'Impact', sans-serif; }}
            #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}

            #redFlashOverlay {{
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(255, 0, 0, 0.85);
                box-shadow: inset 0 0 100px rgba(139, 0, 0, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            #critFlashOverlay {{
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(255, 215, 0, 0.85);
                box-shadow: inset 0 0 100px rgba(255, 140, 0, 0.9);
                z-index: 999; pointer-events: none; opacity: 0;
            }}

            .cinematic-ui {{
                position: absolute;
                bottom: 80px; 
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                text-align: center;
                z-index: 100;
                pointer-events: none;
            }}

            .title-tier-1 {{ font-size: 40px; font-weight: 900; color: #10b981; text-shadow: 0 0 25px #10b981, 0 0 50px #047857; }}
            .title-tier-2 {{ font-size: 46px; font-weight: 900; color: #f59e0b; text-shadow: 0 0 30px #f59e0b, 0 0 60px #d97706; letter-spacing: 1px; }}
            .title-tier-3 {{ font-size: 52px; font-weight: 900; color: #ef4444; text-shadow: 0 0 35px #ef4444, 0 0 70px #b91c1c; animation: pulse 1s infinite alternate; }}
            .title-tier-4 {{ font-size: 58px; font-weight: 900; color: #a855f7; text-shadow: 0 0 25px #a855f7, 0 0 50px #a855f7, 0 0 80px #7e22ce; letter-spacing: 2px; }}
            .title-tier-5 {{ font-size: 64px; font-weight: 900; background: linear-gradient(90deg, #ff007f, #00f0ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 40px #ff007f); animation: shake 0.5s infinite alternate; }}
            .title-tier-6 {{ font-size: 72px; font-weight: 900; background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #00ffff, #0000ff, #8b00ff); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite, superShake 0.1s infinite; filter: drop-shadow(0 0 50px #ffffff); }}

            @keyframes pulse {{ 0% {{ transform: scale(1); }} 100% {{ transform: scale(1.05); }} }}
            @keyframes shake {{ 0% {{ transform: translate(2px, 2px) rotate(0deg); }} 100% {{ transform: translate(-2px, -2px) rotate(-1deg); }} }}
            @keyframes superShake {{ 0% {{ transform: translate(3px, 1px); }} 50% {{ transform: translate(-3px, -2px); }} 100% {{ transform: translate(2px, -1px); }} }}
            @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}

            .status-header {{ font-size: 22px; font-weight: bold; margin-bottom: 6px; letter-spacing: 3px; }}
            .desc-text {{ font-size: 16px; color: #e2e8f0; margin-top: 6px; font-family: sans-serif; text-shadow: 0 0 10px #000; }}
            .price-text {{ font-size: 20px; font-weight: bold; color: #fbbf24; margin-top: 6px; text-shadow: 0 0 15px rgba(251,191,36,0.8); font-family: sans-serif; }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="redFlashOverlay"></div>
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
            const status = "{status}";
            const statusText = document.getElementById('statusText');
            const flashOverlay = document.getElementById('redFlashOverlay');
            const critOverlay = document.getElementById('critFlashOverlay');
            
            if (status === "CRITICAL") {{
                statusText.innerText = "⚡ CRITICAL HIT!! (+2단계 대성공) ⚡";
                statusText.style.color = "#ffe600";
            }} else if (status === "SUCCESS") {{
                statusText.innerText = "✨ ENHANCE SUCCESS ✨";
                statusText.style.color = "#10b981";
            }} else if (status === "SHIELD_SAVED") {{
                statusText.innerText = "🛡️ SHIELD PROTECTED! 🛡️";
                statusText.style.color = "#3b82f6";
            }} else if (status === "DESTROYED") {{
                statusText.innerText = "💥 DESTROYED 💥";
                statusText.style.color = "#ef4444";
            }} else if (status === "FAILED") {{
                statusText.innerText = "🔻 ENHANCE FAILED 🔻";
                statusText.style.color = "#f59e0b";
            }}

            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x020208, 0.015);

            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 1.2, 9);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.getElementById('container').appendChild(renderer.domElement);

            // 조명 세팅
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
            scene.add(ambientLight);

            const spotLight = new THREE.SpotLight("{card_color}", 8);
            spotLight.position.set(0, 12, 8);
            scene.add(spotLight);

            const blueLight = new THREE.PointLight(0x00f0ff, 4, 20);
            blueLight.position.set(-5, -2, 3);
            scene.add(blueLight);

            const purpleLight = new THREE.PointLight(0xff00ea, 4, 20);
            purpleLight.position.set(5, 5, -2);
            scene.add(purpleLight);

            // 사이버 워프 터널
            const tunnelGroup = new THREE.Group();
            const tunnelGeo = new THREE.CylinderGeometry(8, 8, 120, 16, 40, true);
            const tunnelMat = new THREE.MeshBasicMaterial({{
                color: 0x111827,
                wireframe: true,
                transparent: true,
                opacity: 0.15
            }});
            const tunnel = new THREE.Mesh(tunnelGeo, tunnelMat);
            tunnel.rotation.x = Math.PI / 2;
            tunnelGroup.add(tunnel);
            scene.add(tunnelGroup);

            // 바닥 사이버 그리드
            const gridHelper = new THREE.GridHelper(60, 40, 0x00f0ff, 0x1e1b4b);
            gridHelper.position.y = -4;
            scene.add(gridHelper);

            // 카드 모델링
            const cardGroup = new THREE.Group();

            const frameGeo = new THREE.BoxGeometry(2.9, 4.3, 0.2);
            const frameMat = new THREE.MeshStandardMaterial({{ 
                color: 0x1e293b, 
                metalness: 0.9, 
                roughness: 0.2 
            }});
            const frame = new THREE.Mesh(frameGeo, frameMat);
            cardGroup.add(frame);

            const bodyGeo = new THREE.BoxGeometry(2.6, 4.0, 0.22);
            const bodyMat = new THREE.MeshStandardMaterial({{ 
                color: "{card_color}", 
                metalness: 0.8, 
                roughness: 0.15 
            }});
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            cardGroup.add(body);

            const edgeGeo = new THREE.BoxGeometry(2.7, 4.1, 0.24);
            const edgeMat = new THREE.MeshBasicMaterial({{
                color: "{card_color}",
                wireframe: true
            }});
            const edge = new THREE.Mesh(edgeGeo, edgeMat);
            cardGroup.add(edge);

            const coreGeo = new THREE.OctahedronGeometry(0.55, 0);
            const coreMat = new THREE.MeshStandardMaterial({{
                color: 0xffffff,
                emissive: "{card_color}",
                emissiveIntensity: 0.8,
                roughness: 0.1,
                metalness: 0.9
            }});
            const core = new THREE.Mesh(coreGeo, coreMat);
            core.position.z = 0.16;
            cardGroup.add(core);

            const ringGeo = new THREE.TorusGeometry(1.2, 0.02, 16, 100);
            const ringMat = new THREE.MeshBasicMaterial({{ color: 0x00f0ff, transparent: true, opacity: 0.6 }});
            const ring1 = new THREE.Mesh(ringGeo, ringMat);
            ring1.position.z = 0.15;
            cardGroup.add(ring1);

            scene.add(cardGroup);

            // 파티클
            const particleCount = {tier * 200 + 100};
            const pGeo = new THREE.BufferGeometry();
            const pPos = new Float32Array(particleCount * 3);

            for(let i=0; i<particleCount*3; i+=3) {{
                pPos[i] = (Math.random() - 0.5) * 20;
                pPos[i+1] = Math.random() * 12 - 3;
                pPos[i+2] = (Math.random() - 0.5) * 20;
            }}

            pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
            const pMat = new THREE.PointsMaterial({{ color: "{card_color}", size: 0.1, transparent: true, opacity: 0.8 }});
            const particles = new THREE.Points(pGeo, pMat);
            scene.add(particles);

            let explosionParticles = null;
            let explosionVelocities = [];

            // 애니메이션 연출
            if (status === "CRITICAL") {{
                gsap.fromTo(critOverlay, 
                    {{ opacity: 0.9 }}, 
                    {{ opacity: 0, duration: 1.0, ease: "power2.out" }}
                );
                gsap.fromTo(camera.position, {{ z: 3 }}, {{ z: 9, duration: 1.5, ease: "bounce.out" }});
                gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 4, z: Math.PI * 2 }}, {{ y: 0, z: 0, duration: 1.5, ease: "power3.out" }});
            }} else if (status === "DESTROYED") {{
                gsap.fromTo(flashOverlay, 
                    {{ opacity: 0.85 }}, 
                    {{ opacity: 0, duration: 1.2, ease: "power2.out" }}
                );

                gsap.to(camera.position, {{ x: 0.4, y: 1.6, duration: 0.04, repeat: 10, yoyo: true, onComplete: () => {{
                    camera.position.set(0, 1.2, 9);
                }}}});

                gsap.to(cardGroup.scale, {{ x: 0, y: 0, z: 0, duration: 0.25, ease: "power4.in" }});

                const expCount = 600;
                const expGeo = new THREE.BufferGeometry();
                const expPos = new Float32Array(expCount * 3);

                for (let i = 0; i < expCount; i++) {{
                    expPos[i * 3] = 0;
                    expPos[i * 3 + 1] = 0.8;
                    expPos[i * 3 + 2] = 0;

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
                const expMat = new THREE.PointsMaterial({{
                    color: 0xff0055,
                    size: 0.22,
                    transparent: true,
                    opacity: 1.0
                }});

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

                tunnel.rotation.z += 0.003;
                gridHelper.position.z = (time * 2) % 1.5;

                cardGroup.rotation.y = Math.sin(time * 0.8) * 0.3;
                cardGroup.position.y = Math.sin(time * 1.8) * 0.15 + 0.8;
                
                core.rotation.x = time * 2;
                core.rotation.y = time * 2;
                ring1.rotation.z = -time * 1.5;

                const pos = pGeo.attributes.position.array;
                for(let i=1; i<particleCount*3; i+=3) {{
                    pos[i] -= 0.05;
                    if(pos[i] < -3) pos[i] = 9;
                }}
                pGeo.attributes.position.needsUpdate = true;

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

    components.html(three_js_code, height=650, scrolling=False)
