import streamlit as st
import random
import time
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="FC 지온 - 3D 지온냄새 강화하기",
    page_icon="👑",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. 게임 데이터베이스 및 강화 확률표
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "0단계 : 무취의 공간", "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.", "price": 0, "color": "#7f8c8d"},
    1: {"name": "1단계 : 스쳐가는 지온냄새", "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.", "price": 100, "color": "#bdc3c7"},
    2: {"name": "2단계 : 은은한 자이온냄새", "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.", "price": 300, "color": "#2ecc71"},
    3: {"name": "3단계 : 습한 지온냄새", "desc": "비 온 뒤 짙은 상록수 숲속에서 감도는 냄새.", "price": 700, "color": "#27ae60"},
    4: {"name": "4단계 : 진득한 자이온냄새", "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.", "price": 1500, "color": "#1abc9c"},
    5: {"name": "5단계 : 자극적인 지온냄새", "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.", "price": 3500, "color": "#16a085"},
    6: {"name": "6단계 : 풍부한 자이온냄새", "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.", "price": 8000, "color": "#3498db"},
    7: {"name": "7단계 : 압도적인 지온냄새", "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.", "price": 18000, "color": "#2980b9"},
    8: {"name": "8단계 : 폭발하는 자이온냄새", "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.", "price": 40000, "color": "#9b59b6"},
    9: {"name": "9단계 : 시공을 뒤흔드는 지온냄새", "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.", "price": 90000, "color": "#8e44ad"},
    10: {"name": "10단계 : 치명적인 자이온냄새", "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.", "price": 200000, "color": "#f1c40f"},
    11: {"name": "11단계 : 환각을 부르는 지온냄새", "desc": "태초의 지구 흙밭을 거니는 환각을 본다.", "price": 450000, "color": "#f39c12"},
    12: {"name": "12단계 : 공간지배 자이온냄새", "desc": "방 안의 모든 산소를 지온 분자로 채운다.", "price": 1000000, "color": "#e67e22"},
    13: {"name": "13단계 : 전설의 지온냄새", "desc": "역사서에서 언급되던 전설 속의 지구 향기.", "price": 2200000, "color": "#d35400"},
    14: {"name": "14단계 : 신성한 자이온냄새", "desc": "마음이 경건해지며 흙과 하나가 되는 기분.", "price": 5000000, "color": "#e74c3c"},
    15: {"name": "15단계 : 신화급 지온냄새", "desc": "신들이 세계를 창조할 때 맡았다는 향.", "price": 12000000, "color": "#c0392b"},
    16: {"name": "16단계 : 우주관통 자이온냄새", "desc": "성층권을 뚫고 우주선까지 퍼져나간다.", "price": 30000000, "color": "#00ffff"},
    17: {"name": "17단계 : 차원균열 지온냄새", "desc": "평행세계의 흙냄새까지 끌어당긴다.", "price": 75000000, "color": "#ff00ff"},
    18: {"name": "18단계 : Absolute 자이온냄새", "desc": "만물의 요소를 지온 입자로 바꿔버린다.", "price": 180000000, "color": "#ffff00"},
    19: {"name": "19단계 : 초월적 지온냄새", "desc": "인간의 감각으로는 수용 불가능한 향기.", "price": 450000000, "color": "#ff0000"},
    20: {"name": "20단계 : 자이온맘의 포근한 집밥 냄새", "desc": "자이온맘의 강림! 따스하고 구수한 냄새.", "price": 1000000000, "color": "#ffaa00"},
    21: {"name": "21단계 : 자이온맘의 엄격한 등짝 스매싱", "desc": "매콤하면서 사랑이 깃든 자이온맘의 향.", "price": 2500000000, "color": "#ff5500"},
    22: {"name": "22단계 : 자이온맘의 전설의 흙된장국", "desc": "극상의 흙내음과 깊은 손맛.", "price": 6000000000, "color": "#ff00aa"},
    23: {"name": "23단계 : 자이온맘의 100년 숙성 원액", "desc": "몰래 아껴둔 냄새의 결정체.", "price": 15000000000, "color": "#aa00ff"},
    24: {"name": "24단계 : 자이온맘의 지온스프레이", "desc": "집안 가득 뿌리는 치명적인 청량함.", "price": 40000000000, "color": "#00aaff"},
    25: {"name": "25단계 : 자이온맘의 무한한 은혜", "desc": "은하수 아이들에게 평화를 내리는 자애로움.", "price": 100000000000, "color": "#00ffaa"},
    26: {"name": "26단계 : 자이온맘의 궁극 필살기", "desc": "우주 전체가 지온 향으로 뒤덮인다.", "price": 250000000000, "color": "#aaff00"},
    27: {"name": "27단계 : 자이온맘의 창조와 구원", "desc": "빅뱅 당시 터뜨린 절대 구원의 향기.", "price": 600000000000, "color": "#ffffaa"},
    28: {"name": "28단계 : 자이온맘의 권능 지온냄새", "desc": "창조주도 고개를 숙이고 냄새를 맡는다.", "price": 1500000000000, "color": "#ffffff"},
    29: {"name": "29단계 : 만물의 어머니 ★자이온맘★", "desc": "우주 만물이 품으로 돌아가는 최종 오라.", "price": 4000000000000, "color": "#ff0055"},
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
    st.session_state.status = "READY"  # READY, SUCCESS, DESTROYED
if "last_level" not in st.session_state:
    st.session_state.last_level = 0

# -----------------------------------------------------------------------------
# 4. 강화 / 판매 함수
# -----------------------------------------------------------------------------
def enhance():
    curr = st.session_state.level
    if curr >= 30: return
    
    st.session_state.last_level = curr
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
# 5. UI 버튼 및 상단 레이아웃
# -----------------------------------------------------------------------------
st.markdown("<h2 style='text-align: center; color: #00ffaa;'>🎮 FC ONLINE STYLE 3D 지온냄새 강화하기</h2>", unsafe_allow_html=True)

col_info1, col_info2, col_btn1, col_btn2 = st.columns([2, 2, 2, 2])
with col_info1:
    st.subheader(f"💰 보유 골드: {st.session_state.money:,} G")
with col_info2:
    sp, fp, dp = PROB_TABLE[st.session_state.level] if st.session_state.level < 30 else (0,0,0)
    st.write(f"**강화 확률**: 성공 {sp}% | 파괴 {dp}%")

with col_btn1:
    if st.button("🔥 3D 강화 실행", use_container_width=True, disabled=(st.session_state.level >= 30)):
        enhance()
        st.rerun()

with col_btn2:
    if st.button("💰 냄새 판매", use_container_width=True, disabled=(st.session_state.level == 0)):
        sell()
        st.rerun()

# -----------------------------------------------------------------------------
# 6. Three.js 3D 렌더링 HTML/JS 생성
# -----------------------------------------------------------------------------
curr_data = SMELL_DB[st.session_state.level]
card_color = curr_data['color']
card_title = curr_data['name']
card_desc = curr_data['desc']
card_price = f"{curr_data['price']:,} G"
status_text = "강화 준비"
status_color = "#ffffff"

if st.session_state.status == "SUCCESS":
    status_text = "✨ 강화 성공! ✨"
    status_color = "#00ff88"
elif st.session_state.status == "DESTROYED":
    status_text = "💥 강화 파괴! 💥"
    status_color = "#ff3333"
elif st.session_state.status == "FAILED":
    status_text = "🌧️ 강화 실패 (등급 하락)"
    status_color = "#ffaa00"

three_js_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; overflow: hidden; background-color: #050806; font-family: 'Malgun Gothic', sans-serif; }}
        #canvas-container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}
        
        /* FC 온라인 스타일 하단 UI */
        .fc-ui {{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 85%;
            background: rgba(10, 20, 15, 0.85);
            border: 2px solid #33ff88;
            border-radius: 12px;
            padding: 15px 30px;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 0 30px rgba(0, 255, 136, 0.3);
            backdrop-filter: blur(10px);
        }}
        .fc-status {{
            font-size: 26px;
            font-weight: 900;
            color: {status_color};
            text-shadow: 0 0 15px {status_color};
            text-align: center;
            width: 100%;
        }}
        .fc-detail {{
            display: flex;
            gap: 20px;
            font-size: 16px;
        }}
        .fc-badge {{
            background: #00ff88;
            color: #000;
            padding: 4px 10px;
            border-radius: 5px;
            font-weight: bold;
        }}
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
    <div id="canvas-container"></div>
    
    <!-- FC 온라인 하단 연출 바 -->
    <div class="fc-ui">
        <div style="width: 100%;">
            <div class="fc-status">{status_text}</div>
            <div style="display: flex; justify-content: space-between; margin-top: 10px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 10px;">
                <div><span class="fc-badge">{st.session_state.level} 강</span> <b>{card_title}</b></div>
                <div>가치: <span style="color: #ffd700; font-weight: bold;">{card_price}</span></div>
            </div>
        </div>
    </div>

    <script>
        // 1. Scene, Camera, Renderer
        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x050806, 0.03);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 2, 8);

        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.shadowMap.enabled = true;
        container.appendChild(renderer.domElement);

        // 2. 조명 (스포트라이트 및 무대 조명)
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        scene.add(ambientLight);

        const spotLight = new THREE.SpotLight(0x00ff88, 2);
        spotLight.position.set(0, 10, 5);
        spotLight.angle = Math.PI / 4;
        spotLight.penumbra = 0.8;
        scene.add(spotLight);

        const goldLight = new THREE.PointLight(0xffd700, 1.5, 10);
        goldLight.position.set(0, 0, 2);
        scene.add(goldLight);

        // 3. 3D 무대 바닥 (FC 온라인 무대 오마주)
        const floorGeo = new THREE.PlaneGeometry(30, 30);
        const floorMat = new THREE.MeshStandardMaterial({{ color: 0x111a13, roughness: 0.2, metalness: 0.8 }});
        const floor = new THREE.Mesh(floorGeo, floorMat);
        floor.rotation.x = -Math.PI / 2;
        floor.position.y = -2;
        scene.add(floor);

        // 무대 황금 테두리 라인
        const gridHelper = new THREE.GridHelper(30, 20, 0x00ff88, 0x224422);
        gridHelper.position.y = -1.99;
        scene.add(gridHelper);

        // 4. 3D 카드 생성
        const cardGroup = new THREE.Group();
        
        // 카드 몸체
        const cardGeo = new THREE.BoxGeometry(2.4, 3.6, 0.08);
        const cardMat = new THREE.MeshStandardMaterial({{
            color: "{card_color}",
            metalness: 0.7,
            roughness: 0.2
        }});
        const card = new THREE.Mesh(cardGeo, cardMat);
        cardGroup.add(card);

        // 카드 황금 테두리
        const borderGeo = new THREE.BoxGeometry(2.5, 3.7, 0.06);
        const borderMat = new THREE.MeshStandardMaterial({{ color: 0xffd700, metalness: 0.9, roughness: 0.1 }});
        const border = new THREE.Mesh(borderGeo, borderMat);
        border.position.z = -0.01;
        cardGroup.add(border);

        scene.add(cardGroup);

        // 5. 황금 파티클 (축하 꽃가루 / 냄새 안개)
        const particleCount = 200;
        const particleGeo = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);

        for(let i=0; i<particleCount*3; i+=3) {{
            positions[i] = (Math.random() - 0.5) * 12;
            positions[i+1] = Math.random() * 8 - 2;
            positions[i+2] = (Math.random() - 0.5) * 12;
        }}

        particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const particleMat = new THREE.PointsMaterial({{ color: 0x00ff88, size: 0.08, transparent: true, opacity: 0.8 }});
        const particles = new THREE.Points(particleGeo, particleMat);
        scene.add(particles);

        // 6. 애니메이션 루프 (카드 회전 및 둥둥 뜨기)
        let clock = new THREE.Clock();

        function animate() {{
            requestAnimationFrame(animate);
            let time = clock.getElapsedTime();

            // 카드가 부드럽게 좌우로 회전하고 위아래로 떠오름
            cardGroup.rotation.y = Math.sin(time * 0.8) * 0.3;
            cardGroup.position.y = Math.sin(time * 1.5) * 0.15;

            // 파티클 떨어지는 연출
            const pos = particleGeo.attributes.position.array;
            for(let i=1; i<particleCount*3; i+=3) {{
                pos[i] -= 0.02;
                if(pos[i] < -2) pos[i] = 6;
            }}
            particleGeo.attributes.position.needsUpdate = true;

            renderer.render(scene, camera);
        }}

        animate();

        // 창 크기 조절 대응
        window.addEventListener('resize', () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }});
    </script>
</body>
</html>
"""

# HTML 컴포넌트로 3D 렌더링 출력 (높이 600px)
components.html(three_js_code, height=600, scrolling=False)
