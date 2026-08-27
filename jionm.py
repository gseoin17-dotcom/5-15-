import streamlit as st
import random
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - ZION EVOLUTION",
    page_icon="⚽",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. 지온 / 자이온 / 자이온맘 데이터베이스
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {"name": "무취의 공간", "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.", "price": 0, "stat": 60, "color": "#a7f3d0"},
    1: {"name": "스쳐가는 지온냄새", "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.", "price": 100, "stat": 65, "color": "#86efac"},
    2: {"name": "은은한 자이온냄새", "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.", "price": 300, "stat": 70, "color": "#4ade80"},
    3: {"name": "습한 지온냄새", "desc": "비 온 뒤 짙은 상록수 숲속에서 감오는 냄새.", "price": 700, "stat": 75, "color": "#22c55e"},
    4: {"name": "진득한 자이온냄새", "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.", "price": 1500, "stat": 80, "color": "#16a34a"},
    5: {"name": "자극적인 지온냄새", "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.", "price": 3500, "stat": 85, "color": "#15803d"},
    6: {"name": "풍부한 자이온냄새", "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.", "price": 8000, "stat": 90, "color": "#ca8a04"},
    7: {"name": "압도적인 지온냄새", "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.", "price": 18000, "stat": 95, "color": "#a16207"},
    8: {"name": "폭발하는 자이온냄새", "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.", "price": 40000, "stat": 100, "color": "#854d0e"},
    9: {"name": "시공을 뒤흔드는 지온냄새", "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.", "price": 90000, "stat": 105, "color": "#713f12"},
    10: {"name": "치명적인 자이온냄새", "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.", "price": 200000, "stat": 110, "color": "#65a30d"},
    11: {"name": "환각을 부르는 지온냄새", "desc": "태초의 지구 흙밭을 거니는 환각을 본다.", "price": 450000, "stat": 115, "color": "#4d7c0f"},
    12: {"name": "공간지배 자이온냄새", "desc": "방 안의 모든 산소를 지온 분자로 채운다.", "price": 1000000, "stat": 120, "color": "#3f6212"},
    13: {"name": "전설의 지온냄새", "desc": "역사서에서 언급되던 전설 속의 지구 향기.", "price": 2200000, "stat": 123, "color": "#d97706"},
    14: {"name": "신성한 자이온냄새", "desc": "마음이 경건해지며 흙과 하나가 되는 기분.", "price": 5000000, "stat": 126, "color": "#b45309"},
    15: {"name": "신화급 지온냄새", "desc": "신들이 세계를 창조할 때 맡았다는 향.", "price": 12000000, "stat": 130, "color": "#78350f"},
    16: {"name": "우주관통 자이온냄새", "desc": "성층권을 뚫고 우주선까지 퍼져나간다.", "price": 30000000, "stat": 134, "color": "#9333ea"},
    17: {"name": "차원균열 지온냄새", "desc": "평행세계의 흙냄새까지 끌어당긴다.", "price": 75000000, "stat": 138, "color": "#7e22ce"},
    18: {"name": "Absolute 자이온냄새", "desc": "만물의 요소를 지온 입자로 바꿔버린다.", "price": 180000000, "stat": 142, "color": "#6b21a8"},
    19: {"name": "초월적 지온냄새", "desc": "인간의 감각으로는 수용 불가능한 향기.", "price": 450000000, "stat": 146, "color": "#581c87"},
    20: {"name": "자이온맘의 포근한 집밥 냄새", "desc": "자이온맘의 강림! 따스하고 구수한 냄새.", "price": 1000000000, "stat": 150, "color": "#f43f5e"},
    21: {"name": "자이온맘의 등짝 스매싱", "desc": "매콤하면서 사랑이 깃든 자이온맘의 향.", "price": 2500000000, "stat": 155, "color": "#e11d48"},
    22: {"name": "자이온맘의 흙된장국", "desc": "극상의 흙내음과 깊은 손맛.", "price": 6000000000, "stat": 160, "color": "#be123c"},
    23: {"name": "자이온맘의 100년 숙성 원액", "desc": "몰래 아껴둔 냄새의 결정체.", "price": 15000000000, "stat": 165, "color": "#9f1239"},
    24: {"name": "자이온맘의 지온스프레이", "desc": "집안 가득 뿌리는 치명적인 청량함.", "price": 40000000000, "stat": 170, "color": "#881337"},
    25: {"name": "자이온맘의 무한한 은혜", "desc": "은하수 아이들에게 평화를 내리는 자애로움.", "price": 100000000000, "stat": 175, "color": "#4c1d95"},
    26: {"name": "자이온맘의 궁극 필살기", "desc": "우주 전체가 지온 향으로 뒤덮인다.", "price": 250000000000, "stat": 180, "color": "#3b0764"},
    27: {"name": "자이온맘의 창조와 구원", "desc": "빅뱅 당시 터뜨린 절대 구원의 향기.", "price": 600000000000, "stat": 185, "color": "#2e1065"},
    28: {"name": "자이온맘의 권능 지온냄새", "desc": "창조주도 고개를 숙이고 냄새를 맡는다.", "price": 1500000000000, "stat": 190, "color": "#1e1b4b"},
    29: {"name": "만물의 어머니 ★자이온맘★", "desc": "우주 만물이 품으로 돌아가는 최종 오라.", "price": 4000000000000, "stat": 195, "color": "#f43f5e"},
    30: {"name": "★태초의 자이온맘★ 절대신성", "desc": "우주를 지온으로 통일한 자이온맘의 완성.", "price": 8800000000000, "stat": 200, "color": "#000000"}
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
if "prev_level" not in st.session_state:
    st.session_state.prev_level = 0

# -----------------------------------------------------------------------------
# 4. 강화 / 초기화 로직
# -----------------------------------------------------------------------------
def enhance():
    curr = st.session_state.level
    if curr >= 30: return
    
    st.session_state.prev_level = curr
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

def reset_game():
    st.session_state.level = 0
    st.session_state.status = "READY"

# -----------------------------------------------------------------------------
# 5. UI Layout 및 컨트롤 버튼
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    .stApp { background-color: #080B10; color: #ffffff; }
    div.stButton > button {
        width: 100%;
        border-radius: 8px !important;
        font-weight: 800 !important;
        padding: 12px !important;
        background: linear-gradient(135deg, #eab308, #ca8a04) !important;
        color: #000000 !important;
        border: none !important;
        font-size: 16px !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #facc15, #eab308) !important;
        box-shadow: 0 0 15px rgba(234, 179, 8, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

col_ctrl1, col_ctrl2 = st.columns([8, 2])
with col_ctrl1:
    if st.button("🔥 강화 도전!", use_container_width=True, disabled=(st.session_state.level >= 30)):
        enhance()
        st.rerun()
with col_ctrl2:
    if st.button("🔄 초기화", use_container_width=True):
        reset_game()
        st.rerun()

# -----------------------------------------------------------------------------
# 6. FC 온라인 연출 메인 렌더링 (HTML/Three.js/Canvas)
# -----------------------------------------------------------------------------
curr_lvl = st.session_state.level
prev_lvl = st.session_state.prev_level
data = SMELL_DB[curr_lvl]
status = st.session_state.status

stat_diff = data['stat'] - SMELL_DB[prev_lvl]['stat'] if status == "SUCCESS" else 0
lvl_diff = curr_lvl - prev_lvl if status == "SUCCESS" else 0

formatted_price = f"{data['price']:,} G" if data['price'] < 10000 else f"{data['price']//10000:,}억 G" if data['price'] < 100000000 else f"{data['price']/100000000:.1f}조 G"

fc_stage_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            margin: 0;
            overflow: hidden;
            background: #000;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            user-select: none;
        }}
        #stage {{
            position: relative;
            width: 100vw;
            height: 85vh;
            background: radial-gradient(circle at 50% 30%, #1a2e1e 0%, #0a120c 60%, #020503 100%);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            box-sizing: border-box;
            border: 2px solid #2d4a34;
            border-radius: 12px;
            overflow: hidden;
        }}
        
        /* 천장 트러스 및 조명 */
        .truss-top {{
            position: absolute;
            top: 0; width: 100%; height: 60px;
            background: linear-gradient(180deg, rgba(22,101,52,0.8) 0%, rgba(0,0,0,0) 100%);
            border-bottom: 3px solid #22c55e;
            box-shadow: 0 0 20px #22c55e;
            z-index: 2;
        }}

        /* 양옆 무대 날개 (골드 패널) */
        .wing-left, .wing-right {{
            position: absolute;
            top: 15%; width: 28%; height: 65%;
            background: linear-gradient(135deg, rgba(217,119,6,0.15) 0%, rgba(0,0,0,0.8) 100%);
            border: 2px solid #ca8a04;
            z-index: 1;
        }}
        .wing-left {{ left: 2%; transform: skewY(-6deg); border-right: none; }}
        .wing-right {{ right: 2%; transform: skewY(6deg); border-left: none; }}

        /* 중앙 스포트라이트 배경 */
        .spotlight {{
            position: absolute;
            top: 0; left: 50%; transform: translateX(-50%);
            width: 60%; height: 100%;
            background: radial-gradient(ellipse at top, rgba(250,204,21,0.2) 0%, rgba(0,0,0,0) 70%);
            z-index: 1;
            pointer-events: none;
        }}

        /* 중앙 메인 구조 */
        .center-container {{
            position: relative;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 70%;
            margin-top: 40px;
        }}

        /* 선수 아바타 (좌측) */
        .avatar-box {{
            position: absolute;
            left: 20%;
            bottom: 10px;
            width: 140px;
            height: 260px;
            background: radial-gradient(circle, rgba(74,222,128,0.2) 0%, rgba(0,0,0,0) 70%);
            display: flex;
            justify-content: center;
            align-items: flex-end;
        }}
        .avatar-body {{
            width: 70px; height: 180px;
            background: linear-gradient(180deg, #22c55e 0%, #15803d 100%);
            border-radius: 35px 35px 10px 10px;
            position: relative;
            box-shadow: 0 0 15px #22c55e;
        }}
        .avatar-head {{
            width: 45px; height: 50px;
            background: #fde047;
            border-radius: 50%;
            position: absolute;
            top: -45px; left: 12.5px;
        }}

        /* 메인 카드 (중앙) */
        .card-frame {{
            width: 240px;
            height: 350px;
            background: linear-gradient(145deg, #1e1b4b, #31104b);
            border: 4px solid #facc15;
            border-radius: 16px;
            box-shadow: 0 0 30px rgba(250, 204, 21, 0.5), inset 0 0 15px rgba(250, 204, 21, 0.3);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 16px;
            box-sizing: border-box;
            position: relative;
            animation: cardFloat 3s ease-in-out infinite alternate;
        }}
        @keyframes cardFloat {{
            0% {{ transform: translateY(0px); }}
            100% {{ transform: translateY(-10px); }}
        }}

        .card-stat {{
            position: absolute;
            top: 15px; left: 15px;
            font-size: 32px; font-weight: 900; color: #ffffff;
            text-shadow: 0 0 10px #facc15;
        }}
        .card-badge {{
            position: absolute;
            top: 55px; left: 15px;
            font-size: 14px; font-weight: 800; color: #86efac;
        }}
        .card-level-badge {{
            position: absolute;
            bottom: 75px; left: 15px;
            background: #facc15; color: #000;
            font-size: 20px; font-weight: 900;
            padding: 2px 10px; border-radius: 4px;
        }}
        .card-image-placeholder {{
            width: 130px; height: 150px;
            background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, rgba(0,0,0,0.4) 100%);
            border-radius: 50%;
            margin-top: 20px;
            display: flex; justify-content: center; align-items: center;
            font-size: 60px;
        }}
        .card-name {{
            position: absolute;
            bottom: 25px;
            font-size: 18px; font-weight: 900; color: #ffffff;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            text-align: center;
            width: 90%;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
        }}

        /* 양옆 불꽃 스파클러 폭죽 파티클 Canvas */
        #sparklerCanvas {{
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 5;
            pointer-events: none;
        }}

        /* 성공 메세지 텍스트 */
        .status-banner {{
            position: absolute;
            bottom: 60px;
            z-index: 20;
            font-size: 26px;
            font-weight: 900;
            letter-spacing: 2px;
            text-shadow: 0 0 10px rgba(0,0,0,0.9);
        }}
        .status-success {{ color: #4ade80; text-shadow: 0 0 20px #22c55e; }}
        .status-fail {{ color: #f87171; text-shadow: 0 0 20px #ef4444; }}

        /* 하단 스탯 / 선수 가치 바 */
        .bottom-bar {{
            position: relative;
            z-index: 20;
            width: 100%;
            height: 50px;
            background: rgba(10, 15, 12, 0.95);
            border-top: 1px solid #22c55e;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 30px;
            box-sizing: border-box;
            font-size: 14px;
        }}
        .stat-group {{ display: flex; gap: 20px; align-items: center; }}
        .stat-item {{ display: flex; align-items: center; gap: 6px; }}
        .stat-label {{ color: #94a3b8; font-size: 12px; }}
        .stat-val {{ font-weight: 800; color: #ffffff; }}
        .stat-plus {{ color: #4ade80; font-weight: 800; font-size: 13px; }}
        .price-val {{ color: #facc15; font-weight: 900; font-size: 18px; }}

        /* 금빛 꽃가루 Confetti */
        .confetti {{
            position: absolute;
            width: 8px; height: 14px;
            background: #facc15;
            opacity: 0.8;
            z-index: 15;
            animation: fall 3s linear infinite;
        }}
        @keyframes fall {{
            0% {{ transform: translateY(-10px) rotate(0deg); opacity: 1; }}
            100% {{ transform: translateY(80vh) rotate(720deg); opacity: 0; }}
        }}
    </style>
</head>
<body>
    <div id="stage">
        <div class="truss-top"></div>
        <div class="wing-left"></div>
        <div class="wing-right"></div>
        <div class="spotlight"></div>
        
        <canvas id="sparklerCanvas"></canvas>

        <!-- 금빛 꽃가루 (강화 성공 시) -->
        {"".join([f'<div class="confetti" style="left:{random.randint(5,95)}%; animation-delay:{random.uniform(0,2.5)}s; background:{"#facc15" if i%2==0 else "#4ade80"};"></div>' for i in range(35)]) if status == "SUCCESS" else ""}

        <div class="center-container">
            <!-- 좌측 캐릭 아바타 -->
            <div class="avatar-box">
                <div class="avatar-body">
                    <div class="avatar-head"></div>
                </div>
            </div>

            <!-- 중앙 선수 카드 -->
            <div class="card-frame" style="border-color: {data['color']};">
                <div class="card-stat">{data['stat']}</div>
                <div class="card-badge">ZION</div>
                <div class="card-image-placeholder">🪰</div>
                <div class="card-level-badge">{curr_lvl}</div>
                <div class="card-name">{data['name']}</div>
            </div>
        </div>

        <!-- 강화 상태 문구 -->
        <div class="status-banner">
            {"<span class='status-success'>강화 성공</span>" if status == "SUCCESS" else "<span class='status-fail'>강화 파괴! (0단계)" if status == "DESTROYED" else "<span class='status-fail'>강화 실패" if status == "FAILED" else "강화 대기 중"}
        </div>

        <!-- 하단 스탯 및 가치 정보 바 -->
        <div class="bottom-bar">
            <div class="stat-group">
                <div class="stat-item">
                    <span class="stat-label">강화 등급</span>
                    <span class="stat-val">{curr_lvl}</span>
                    {"<span class='stat-plus'>+" + str(lvl_diff) + "</span>" if lvl_diff > 0 else ""}
                </div>
                <div class="stat-item">
                    <span class="stat-label">능력치</span>
                    <span class="stat-val">{data['stat']}</span>
                    {"<span class='stat-plus'>+" + str(stat_diff) + "</span>" if stat_diff > 0 else ""}
                </div>
            </div>
            <div class="stat-group">
                <span class="stat-label">예상 가치</span>
                <span class="price-val">{formatted_price}</span>
            </div>
        </div>
    </div>

    <script>
        // 양옆 불꽃 스파클러 폭죽 연출 Canvas
        const canvas = document.getElementById('sparklerCanvas');
        const ctx = canvas.getContext('2d');

        function resize() {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }}
        resize();
        window.addEventListener('resize', resize);

        const particles = [];
        const isSuccess = "{status}" === "SUCCESS";

        if (isSuccess) {{
            // 양쪽에 폭죽 발생 위치 지정
            const emitterLeft = {{ x: canvas.width * 0.18, y: canvas.height * 0.65 }};
            const emitterRight = {{ x: canvas.width * 0.82, y: canvas.height * 0.65 }};

            function createSpark(emitter) {{
                for(let i=0; i<4; i++) {{
                    particles.push({{
                        x: emitter.x,
                        y: emitter.y,
                        vx: (Math.random() - 0.5) * 6,
                        vy: -Math.random() * 12 - 4,
                        size: Math.random() * 3 + 1,
                        color: Math.random() > 0.3 ? '#facc15' : '#ffffff',
                        life: 1.0,
                        decay: Math.random() * 0.03 + 0.015
                    }});
                }}
            }}

            function animate() {{
                requestAnimationFrame(animate);
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                createSpark(emitterLeft);
                createSpark(emitterRight);

                for(let i = particles.length - 1; i >= 0; i--) {{
                    let p = particles[i];
                    p.x += p.vx;
                    p.y += p.vy;
                    p.vy += 0.25; // 중력 효과
                    p.life -= p.decay;

                    if(p.life <= 0) {{
                        particles.splice(i, 1);
                        continue;
                    }}

                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                    ctx.fillStyle = p.color;
                    ctx.globalAlpha = p.life;
                    ctx.fill();
                }}
            }}
            animate();
        }}
    </script>
</body>
</html>
"""

components.html(fc_stage_html, height=720, scrolling=False)
