import streamlit as st
import random
import time
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - Ultra 3D",
    page_icon="👑",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. 게임 데이터베이스 및 강화 확률표
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 무취의 공간", "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.", "price": 0, "color": "#4a5568"},
    1: {"name": "1단계 : 스쳐가는 지온냄새", "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.", "price": 100, "color": "#718096"},
    2: {"name": "2단계 : 은은한 자이온냄새", "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.", "price": 300, "color": "#38a169"},
    3: {"name": "3단계 : 습한 지온냄새", "desc": "비 온 뒤 짙은 상록수 숲속에서 감도는 냄새.", "price": 700, "color": "#276749"},
    4: {"name": "4단계 : 진득한 자이온냄새", "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.", "price": 1500, "color": "#319795"},
    5: {"name": "5단계 : 자극적인 지온냄새", "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.", "price": 3500, "color": "#2c7a7b"},
    6: {"name": "6단계 : 풍부한 자이온냄새", "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.", "price": 8000, "color": "#3182ce"},
    7: {"name": "7단계 : 압도적인 지온냄새", "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.", "price": 18000, "color": "#2b6cb0"},
    8: {"name": "8단계 : 폭발하는 자이온냄새", "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.", "price": 40000, "color": "#805ad5"},
    9: {"name": "9단계 : 시공을 뒤흔드는 지온냄새", "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.", "price": 90000, "color": "#6b46c1"},
    10: {"name": "10단계 : 치명적인 자이온냄새", "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.", "price": 200000, "color": "#d69e2e"},
    11: {"name": "11단계 : 환각을 부르는 지온냄새", "desc": "태초의 지구 흙밭을 거니는 환각을 본다.", "price": 450000, "color": "#b7791f"},
    12: {"name": "12단계 : 공간지배 자이온냄새", "desc": "방 안의 모든 산소를 지온 분자로 채운다.", "price": 1000000, "color": "#dd6b20"},
    13: {"name": "13단계 : 전설의 지온냄새", "desc": "역사서에서 언급되던 전설 속의 지구 향기.", "price": 2200000, "color": "#c05621"},
    14: {"name": "14단계 : 신성한 자이온냄새", "desc": "마음이 경건해지며 흙과 하나가 되는 기분.", "price": 5000000, "color": "#e53e3e"},
    15: {"name": "15단계 : 신화급 지온냄새", "desc": "신들이 세계를 창조할 때 맡았다는 향.", "price": 12000000, "color": "#9b2c2c"},
    16: {"name": "16단계 : 우주관통 자이온냄새", "desc": "성층권을 뚫고 우주선까지 퍼져나간다.", "price": 30000000, "color": "#00f0ff"},
    17: {"name": "17단계 : 차원균열 지온냄새", "desc": "평행세계의 흙냄새까지 끌어당긴다.", "price": 75000000, "color": "#ff00ea"},
    18: {"name": "18단계 : Absolute 자이온냄새", "desc": "만물의 요소를 지온 입자로 바꿔버린다.", "price": 180000000, "color": "#ffe600"},
    19: {"name": "19단계 : 초월적 지온냄새", "desc": "인간의 감각으로는 수용 불가능한 향기.", "price": 450000000, "color": "#ff0055"},
    20: {"name": "20단계 : 자이온맘의 포근한 집밥 냄새", "desc": "자이온맘의 강림! 따스하고 구수한 냄새.", "price": 1000000000, "color": "#ffaa00"},
    21: {"name": "21단계 : 자이온맘의 엄격한 등짝 스매싱", "desc": "매콤하면서 사랑이 깃든 자이온맘의 향.", "price": 2500000000, "color": "#ff4500"},
    22: {"name": "22단계 : 자이온맘의 전설의 흙된장국", "desc": "극상의 흙내음과 깊은 손맛.", "price": 6000000000, "color": "#ff007f"},
    23: {"name": "23단계 : 자이온맘의 100년 숙성 원액", "desc": "몰래 아껴둔 냄새의 결정체.", "price": 15000000000, "color": "#7b00ff"},
    24: {"name": "24단계 : 자이온맘의 지온스프레이", "desc": "집안 가득 뿌리는 치명적인 청량함.", "price": 40000000000, "color": "#0088ff"},
    25: {"name": "25단계 : 자이온맘의 무한한 은혜", "desc": "은하수 아이들에게 평화를 내리는 자애로움.", "price": 100000000000, "color": "#00ffaa"},
    26: {"name": "26단계 : 자이온맘의 궁극 필살기", "desc": "우주 전체가 지온 향으로 뒤덮인다.", "price": 250000000000, "color": "#ccff00"},
    27: {"name": "27단계 : 자이온맘의 창조와 구원", "desc": "빅뱅 당시 터뜨린 절대 구원의 향기.", "price": 600000000000, "color": "#fffb00"},
    28: {"name": "28단계 : 자이온맘의 권능 지온냄새", "desc": "창조주도 고개를 숙이고 냄새를 맡는다.", "price": 1500000000000, "color": "#ffffff"},
    29: {"name": "29단계 : 만물의 어머니 ★자이온맘★", "desc": "우주 만물이 품으로 돌아가는 최종 오라.", "price": 4000000000000, "color": "#ff00aa"},
    30: {"name": "30단계 : ★태초의 자이온맘★ 절대신성", "desc": "우주를 지온으로 통일한 자이온맘의 완성.", "price": 10000000000000, "color": "#00ffff"}
}

PROB_TABLE = {
    0: (100, 0, 0), 1: (95, 5, 0), 2: (90, 10, 0), 3: (85, 15, 0), 4: (80, 20, 0),
    5: (75, 25, 0), 6: (70, 28, 2), 7: (65, 30, 5), 8: (60, 32, 8), 9: (55, 35, 10),
    10: (50, 38, 12), 11: (45, 40, 15), 12: (40, 42, 18), 13: (35, 45, 20), 14: (30, 48, 22),
    15: (25, 50, 25), 16: (20, 53, 27), 17: (15, 55, 30), 18: (12, 53, 35), 19: (10, 50, 40),
    20: (8, 47, 45), 21: (6, 44, 50), 22: (5, 40, 55), 23: (4, 36, 60), 24: (3, 32, 65),
    25: (2, 28, 70), 26: (1.5, 23.5, 75), 27: (1.0, 19.0, 80), 28: (0.5, 14.5, 85), 29: (0.1, 9.9, 90)
}

# -----------------------------------------------------------------------------
# 3. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
    st.session_state.level = 0
if "money" not in st.session_state:
    st.session_state.money = 10000
if "status" not in st.session_state:
    st.session_state.status = "READY"
if "anim_trigger" not in st.session_state:
    st.session_state.anim_trigger = 0

# -----------------------------------------------------------------------------
# 4. 강화 / 판매 함수
# -----------------------------------------------------------------------------
def enhance():
    curr = st.session_state.level
    if curr >= 30: return
    
    st.session_state.anim_trigger += 1
    sp, fp, dp = PROB_TABLE[curr]
    r = random.uniform(0, 100)
    
    if r < sp:
        st.session_state.level += 1
        st.session_state.status = "SUCCESS"
    elif r < (sp + dp):
        st.session_state.level = 0
        st.session_state.status = "DESTROYED"
    else:
        if curr > 0: st.session_state.level -= 1
        st.session_state.status = "FAILED"

def sell():
    curr = st.session_state.level
    if curr == 0: return
    st.session_state.money += SMELL_DB[curr]['price']
    st.session_state.level = 0
    st.session_state.status = "READY"

# -----------------------------------------------------------------------------
# 5. 상단 컨트롤 패널
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp { background-color: #030604; color: #fff; }
    .stat-card {
        background: rgba(10, 25, 15, 0.8);
        border: 1px solid #10b981;
        padding: 10px 20px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
with col1:
    st.markdown(f'<div class="stat-card">💰 보유 골드<br><b>{st.session_state.money:,} G</b></div>', unsafe_allow_html=True)
with col2:
    sp, fp, dp = PROB_TABLE[st.session_state.level] if st.session_state.level < 30 else (0,0,0)
    st.markdown(f'<div class="stat-card">📊 성공 확률<br><b>{sp}%</b> (파괴 {dp}%)</div>', unsafe_allow_html=True)

with col3:
    if st.button("🔥 시네마틱 강화 실행", use_container_width=True, disabled=(st.session_state.level >= 30)):
        enhance()
        st.rerun()

with col4:
    if st.button("💰 현재 냄새 판매", use_container_width=True, disabled=(st.session_state.level == 0)):
        sell()
        st.rerun()

# -----------------------------------------------------------------------------
# 6. Ultra 3D 시네마틱 렌더링 (Three.js 기반)
# -----------------------------------------------------------------------------
curr_data = SMELL_DB[st.session_state.level]
card_color = curr_data['color']
card_title = curr_data['name']
card_desc = curr_data['desc']
card_price = f"{curr_data['price']:,} G"
status = st.session_state.status

three_js_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; overflow: hidden; background: #000; font-family: 'Malgun Gothic', sans-serif; }}
        #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}
        
        /* FC 온라인 스타일 하단 시네마틱 바 */
        .cinematic-ui {{
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            width: 80%;
            background: linear-gradient(180deg, rgba(5,15,10,0.6) 0%, rgba(0,0,0,0.95) 100%);
            border: 2px solid #10b981;
            border-radius: 12px;
            padding: 20px 30px;
            box-shadow: 0 0 50px rgba(16, 185, 129, 0.4);
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(15px);
            z-index: 100;
        }}
        .status-title {{
            font-size: 32px;
            font-weight: 900;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        .succ-text {{ color: #10b981; text-shadow: 0 0 20px #10b981; }}
        .dest-text {{ color: #ef4444; text-shadow: 0 0 20px #ef4444; }}
        .fail-text {{ color: #f59e0b; text-shadow: 0 0 20px #f59e0b; }}
        
        .level-badge {{
            background: #10b981;
            color: #000;
            font-size: 18px;
            font-weight: 900;
            padding: 5px 15px;
            border-radius: 6px;
            display: inline-block;
            margin-right: 10px;
        }}
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
</head>
<body>
    <div id="container"></div>

    <div class="cinematic-ui">
        <div>
            <div id="statusText" class="status-title">READY</div>
            <div style="margin-top: 8px; font-size: 18px; color: #e2e8f0;">
                <span class="level-badge">{st.session_state.level} 강</span>
                <b>{card_title}</b>
            </div>
            <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">"{card_desc}"</div>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 14px; color: #94a3b8;">예상 냄새 가치</div>
            <div style="font-size: 26px; font-weight: 900; color: #fbbf24; text-shadow: 0 0 10px rgba(251,191,36,0.5);">
                {card_price}
            </div>
        </div>
    </div>

    <script>
        const status = "{status}";
        const statusText = document.getElementById('statusText');
        
        if (status === "SUCCESS") {{
            statusText.innerText = "✨ ENHANCE SUCCESS ✨";
            statusText.className = "status-title succ-text";
        }} else if (status === "DESTROYED") {{
            statusText.innerText = "💥 DESTROYED 💥";
            statusText.className = "status-title dest-text";
        }} else if (status === "FAILED") {{
            statusText.innerText = "🔻 ENHANCE FAILED 🔻";
            statusText.className = "status-title fail-text";
        }} else {{
            statusText.innerText = "READY FOR ENHANCE";
            statusText.className = "status-title";
        }}

        // 1. Scene setup
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x000000, 0.025);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 1.5, 9);

        const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.shadowMap.enabled = true;
        document.getElementById('container').appendChild(renderer.domElement);

        // 2. Lights (경기장 스포트라이트 연출)
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
        scene.add(ambientLight);

        const mainSpot = new THREE.SpotLight(0x10b981, 4);
        mainSpot.position.set(0, 12, 6);
        mainSpot.angle = Math.PI / 4;
        mainSpot.penumbra = 0.8;
        scene.add(mainSpot);

        const backSpot = new THREE.DirectionalLight("{card_color}", 2);
        backSpot.position.set(0, 5, -5);
        scene.add(backSpot);

        // 3. 3D 바닥 및 경기장 트러스 구조물
        const floorGeo = new THREE.PlaneGeometry(40, 40);
        const floorMat = new THREE.MeshStandardMaterial({{ color: 0x050a07, roughness: 0.1, metalness: 0.9 }});
        const floor = new THREE.Mesh(floorGeo, floorMat);
        floor.rotation.x = -Math.PI / 2;
        floor.position.y = -2;
        scene.add(floor);

        const grid = new THREE.GridHelper(40, 30, 0x10b981, 0x052e16);
        grid.position.y = -1.99;
        scene.add(grid);

        // 4. FC 온라인 3D 카드 오브젝트
        const cardGroup = new THREE.Group();

        // 메인 프레임
        const cardGeo = new THREE.BoxGeometry(2.6, 4.0, 0.1);
        const cardMat = new THREE.MeshStandardMaterial({{ color: "{card_color}", metalness: 0.8, roughness: 0.2 }});
        const card = new THREE.Mesh(cardGeo, cardMat);
        cardGroup.add(card);

        // 황금 베젤
        const borderGeo = new THREE.BoxGeometry(2.72, 4.12, 0.08);
        const borderMat = new THREE.MeshStandardMaterial({{ color: 0xfbbf24, metalness: 0.95, roughness: 0.05 }});
        const border = new THREE.Mesh(borderGeo, borderMat);
        border.position.z = -0.02;
        cardGroup.add(border);

        scene.add(cardGroup);

        // 5. 파티클 시스템 (성공 시 폭발 파티클)
        const pCount = 300;
        const pGeo = new THREE.BufferGeometry();
        const pPos = new Float32Array(pCount * 3);

        for(let i=0; i<pCount*3; i+=3) {{
            pPos[i] = (Math.random() - 0.5) * 15;
            pPos[i+1] = Math.random() * 10 - 2;
            pPos[i+2] = (Math.random() - 0.5) * 15;
        }}

        pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
        const pMat = new THREE.PointsMaterial({{ color: 0x10b981, size: 0.1, transparent: true, opacity: 0.8 }});
        const particles = new THREE.Points(pGeo, pMat);
        scene.add(particles);

        // 6. 시네마틱 GSAP 카메라 연출 (강화 성공/실패 시 드라마틱 카메라 워킹)
        if (status === "SUCCESS") {{
            gsap.fromTo(camera.position, {{ z: 3, y: 0.5 }}, {{ z: 9, y: 1.5, duration: 1.5, ease: "power3.out" }});
            gsap.fromTo(cardGroup.rotation, {{ y: Math.PI * 4 }}, {{ y: 0, duration: 1.5, ease: "power3.out" }});
        }} else if (status === "DESTROYED") {{
            gsap.to(cardGroup.position, {{ y: -5, duration: 0.5, ease: "bounce.in" }});
        }}

        // 7. Render Loop
        const clock = new THREE.Clock();

        function animate() {{
            requestAnimationFrame(animate);
            const time = clock.getElapsedTime();

            if (status !== "DESTROYED") {{
                cardGroup.rotation.y = Math.sin(time * 0.8) * 0.2;
                cardGroup.position.y = Math.sin(time * 2.0) * 0.1;
            }}

            const pos = pGeo.attributes.position.array;
            for(let i=1; i<pCount*3; i+=3) {{
                pos[i] -= 0.03;
                if(pos[i] < -2) pos[i] = 8;
            }}
            pGeo.attributes.position.needsUpdate = true;

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
