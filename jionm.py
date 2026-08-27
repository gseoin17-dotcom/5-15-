import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - PURE EDITION",
    page_icon="🏰",
    layout="wide",
)

# -----------------------------------------------------------------------------
# 2. 냄새 데이터베이스 (비용/가격 제거)
# -----------------------------------------------------------------------------
SMELL_DB = {
    0: {
        "name": "0단계 : 무취의 공간",
        "desc": "아직 아무런 지온의 기운도 느껴지지 않는다.",
        "tier": 1,
    },
    1: {
        "name": "1단계 : 스쳐가는 지온냄새",
        "desc": "코끝을 살짝 스치는 은은한 흙과 이끼의 기운.",
        "tier": 1,
    },
    2: {
        "name": "2단계 : 은은한 자이온냄새",
        "desc": "마른 땅에 단비가 내려 피어나는 쾌적한 냄새.",
        "tier": 1,
    },
    3: {
        "name": "3단계 : 습한 지온냄새",
        "desc": "비 온 뒤 짙은 상록수 숲속에서 감오는 냄새.",
        "tier": 1,
    },
    4: {
        "name": "4단계 : 진득한 자이온냄새",
        "desc": "공기가 묵직해지며 호흡할 때마다 흙냄새가 파고든다.",
        "tier": 1,
    },
    5: {
        "name": "5단계 : 자극적인 지온냄새",
        "desc": "방선균의 대사물질이 코를 강렬하게 자극한다.",
        "tier": 1,
    },
    6: {
        "name": "6단계 : 풍부한 자이온냄새",
        "desc": "주변 공기를 감싸는 진하고 기분 좋은 대지의 향.",
        "tier": 2,
    },
    7: {
        "name": "7단계 : 압도적인 지온냄새",
        "desc": "주위 10m 안의 인공 향수를 완벽히 압도한다.",
        "tier": 2,
    },
    8: {
        "name": "8단계 : 폭발하는 지온냄새",
        "desc": "페트리코 입자의 대폭발로 눈이 번쩍 뜨인다.",
        "tier": 2,
    },
    9: {
        "name": "9단계 : 시공을 뒤흔드는 지온냄새",
        "desc": "냄새만으로 눈앞에 고대 대륙이 일렁인다.",
        "tier": 2,
    },
    10: {
        "name": "10단계 : 치명적인 자이온냄새",
        "desc": "한 번 맡으면 다른 향은 밋밋하게 느껴진다.",
        "tier": 2,
    },
    11: {
        "name": "11단계 : 환각을 부르는 지온냄새",
        "desc": "태초의 지구 흙밭을 거니는 환각을 본다.",
        "tier": 3,
    },
    12: {
        "name": "12단계 : 공간지배 자이온냄새",
        "desc": "방 안의 모든 산소를 지온 분자로 채운다.",
        "tier": 3,
    },
    13: {
        "name": "13단계 : 전설의 지온냄새",
        "desc": "역사서에서 언급되던 전설 속의 지구 향기.",
        "tier": 3,
    },
    14: {
        "name": "14단계 : 신성한 자이온냄새",
        "desc": "마음이 경건해지며 흙과 하나가 되는 기분.",
        "tier": 3,
    },
    15: {
        "name": "15단계 : 신화급 지온냄새",
        "desc": "신들이 세계를 창조할 때 맡았다는 향.",
        "tier": 3,
    },
    16: {
        "name": "16단계 : 우주관통 자이온냄새",
        "desc": "성층권을 뚫고 우주선까지 퍼져나간다.",
        "tier": 4,
    },
    17: {
        "name": "17단계 : 차원균열 자이온냄새",
        "desc": "평행세계의 흙냄새까지 끌어당긴다.",
        "tier": 4,
    },
    18: {
        "name": "18단계 : Absolute 자이온냄새",
        "desc": "만물의 요소를 지온 입자로 바꿔버린다.",
        "tier": 4,
    },
    19: {
        "name": "19단계 : 초월적 지온냄새",
        "desc": "인간의 감각으로는 수용 불가능한 향기.",
        "tier": 4,
    },
    20: {
        "name": "20단계 : 자이온맘의 포근한 집밥 냄새",
        "desc": "자이온맘의 강림! 따스하고 구수한 냄새.",
        "tier": 4,
    },
    21: {
        "name": "21단계 : 자이온맘의 엄격한 등짝 스매싱",
        "desc": "매콤하면서 사랑이 깃든 자이온맘의 향.",
        "tier": 5,
    },
    22: {
        "name": "22단계 : 자이온맘의 전설의 흙된장국",
        "desc": "극상의 흙내음과 깊은 손맛.",
        "tier": 5,
    },
    23: {
        "name": "23단계 : 자이온맘의 100년 숙성 원액",
        "desc": "몰래 아껴둔 냄새의 결정체.",
        "tier": 5,
    },
    24: {
        "name": "24단계 : 자이온맘의 지온스프레이",
        "desc": "집안 가득 뿌리는 치명적인 청량함.",
        "tier": 5,
    },
    25: {
        "name": "25단계 : 자이온맘의 무한한 은혜",
        "desc": "은하수 아이들에게 평화를 내리는 자애로움.",
        "tier": 5,
    },
    26: {
        "name": "26단계 : 자이온맘의 궁극 필살기",
        "desc": "우주 전체가 지온 향으로 뒤덮인다.",
        "tier": 6,
    },
    27: {
        "name": "27단계 : 자이온맘의 창조와 구원",
        "desc": "빅뱅 당시 터뜨린 절대 구원의 향기.",
        "tier": 6,
    },
    28: {
        "name": "28단계 : 자이온맘의 권능 지온냄새",
        "desc": "창조주도 고개를 숙이고 냄새를 맡는다.",
        "tier": 6,
    },
    29: {
        "name": "29단계 : 만물의 어머니 ★자이온맘★",
        "desc": "우주 만물이 품으로 돌아가는 최종 오라.",
        "tier": 6,
    },
    30: {
        "name": "30단계 : ★태초의 자이온맘★ 절대신성",
        "desc": "우주를 지온으로 통일한 자이온맘의 완성.",
        "tier": 6,
    },
}

# (성공 확률, 방지권 소모 개수) 테이블
PROB_TABLE = {
    0: (100.0, 0),
    1: (100.0, 0),
    2: (100.0, 0),
    3: (95.0, 0),
    4: (95.0, 0),
    5: (90.0, 0),
    6: (90.0, 1),
    7: (90.0, 1),
    8: (85.0, 1),
    9: (80.0, 1),
    10: (80.0, 1),
    11: (75.0, 1),
    12: (70.0, 1),
    13: (70.0, 2),
    14: (65.0, 3),
    15: (60.0, 4),
    16: (60.0, 7),
    17: (55.0, 9),
    18: (50.0, 10),
    19: (50.0, 12),
    20: (45.0, 15),
    21: (40.0, 17),
    22: (40.0, 20),
    23: (40.0, 22),
    24: (40.0, 23),
    25: (35.0, 23),
    26: (50.0, 0),
    27: (40.0, 0),
    28: (15.0, 0),
    29: (0.0, 0),
}

CRITICAL_RATE = 0.05

# -----------------------------------------------------------------------------
# 3. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "level" not in st.session_state:
  st.session_state.level = 0
if "status" not in st.session_state:
  st.session_state.status = "READY"
if "shield" not in st.session_state:
  st.session_state.shield = 10
if "tears" not in st.session_state:
  st.session_state.tears = 0
if "dev_mode" not in st.session_state:
  st.session_state.dev_mode = False

# -----------------------------------------------------------------------------
# 4. 강화 로직
# -----------------------------------------------------------------------------


def enhance():
  curr = st.session_state.level
  if curr >= 30:
    return

  if st.session_state.dev_mode:
    st.session_state.level += 1
    st.session_state.status = "SUCCESS"
    return

  sp, required_shield = PROB_TABLE.get(curr, (50.0, 0))
  r = random.uniform(0, 100)

  if r < sp:
    if random.random() < CRITICAL_RATE and curr + 2 <= 30:
      st.session_state.level += 2
      st.session_state.status = "CRITICAL"
    else:
      st.session_state.level += 1
      st.session_state.status = "SUCCESS"
  else:
    if curr < 26 and required_shield > 0 and st.session_state.shield >= required_shield:
      st.session_state.shield -= required_shield
      st.session_state.status = "SHIELD_SAVED"
      st.session_state.tears += 1
    else:
      if curr >= 26 or required_shield == 0 or st.session_state.shield < required_shield:
        if random.random() < 0.5:
          st.session_state.level = 0
          st.session_state.status = "DESTROYED"
        else:
          if curr > 0:
            st.session_state.level -= 1
          st.session_state.status = "FAILED"
      else:
        if curr > 0:
          st.session_state.level -= 1
        st.session_state.status = "FAILED"
      st.session_state.tears += 1


# -----------------------------------------------------------------------------
# 5. 테마 CSS
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }
    .glass-panel {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
    }
    .stat-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(245, 158, 11, 0.4);
        padding: 12px 10px;
        border-radius: 10px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .stat-title {
        font-size: 14px;
        font-weight: 600;
        color: #fde68a;
        margin-bottom: 4px;
    }
    .stat-value {
        font-size: 20px;
        font-weight: 800;
        color: #ffffff;
    }
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 10px 18px !important;
        border: 1px solid rgba(217, 119, 6, 0.4) !important;
        background: linear-gradient(135deg, rgba(147, 51, 234, 0.6), rgba(217, 119, 6, 0.6)) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(217, 119, 6, 0.6);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 6. 메인 레이아웃
# -----------------------------------------------------------------------------
left_col, right_col = st.columns([2.2, 7.8], gap="medium")

with left_col:
  st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h3 style='margin:0 0 12px 0; font-size: 20px; color:#fde68a;'>🏰 지온냄새"
      " 강화</h3>",
      unsafe_allow_html=True,
  )

  if st.button(
      "🔥 강화 실행", use_container_width=True, disabled=(st.session_state.level >= 30)
  ):
    enhance()
    st.rerun()

  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#e2e8f0;'>⚙️ 설정</h4>",
      unsafe_allow_html=True,
  )
  st.session_state.dev_mode = st.toggle(
      "🛠️ 개발자 모드 (100% 성공)", value=st.session_state.dev_mode
  )
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#e2e8f0;'>🛒 상점</h4>",
      unsafe_allow_html=True,
  )
  if st.button("🛡️ 방지권 10개 충전", use_container_width=True):
    st.session_state.shield += 10
    st.success("방지권 충전 완료!")
    st.rerun()
  st.markdown("</div>", unsafe_allow_html=True)

with right_col:
  curr_data = SMELL_DB[st.session_state.level]
  card_title = curr_data["name"]
  card_desc = curr_data["desc"]
  tier = curr_data["tier"]
  status = st.session_state.status
  sp, req_shield = PROB_TABLE.get(st.session_state.level, (50.0, 0))

  three_js_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; overflow: hidden; background: transparent; font-family: sans-serif; }}
            #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}
            .cinematic-ui {{
                position: absolute; bottom: 35px; left: 50%; transform: translateX(-50%);
                width: 100%; text-align: center; z-index: 100; pointer-events: none;
            }}
            .title-tier {{ font-size: 48px; font-weight: 900; color: #fde68a; text-shadow: 0 0 25px #fde68a; }}
            .status-header {{ font-size: 22px; font-weight: 800; margin-bottom: 6px; letter-spacing: 2px; }}
            .desc-text {{ font-size: 16px; color: #f3e8ff; margin-top: 6px; text-shadow: 0 2px 10px rgba(0,0,0,0.9); }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    </head>
    <body>
        <div id="container"></div>
        <div class="cinematic-ui">
            <div id="statusText" class="status-header">{status}</div>
            <div class="title-tier">{card_title}</div>
            <div class="desc-text">"{card_desc}"</div>
        </div>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0.4, 9.5);
            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('container').appendChild(renderer.domElement);

            scene.add(new THREE.AmbientLight(0xffffff, 1.2));
            const dirLight = new THREE.DirectionalLight(0xffffff, 1.5);
            dirLight.position.set(5, 8, 5);
            scene.add(dirLight);

            const cardGroup = new THREE.Group();
            const frameGeo = new THREE.BoxGeometry(4.0, 5.9, 0.22);
            const frameMat = new THREE.MeshStandardMaterial({{ color: 0xfbbf24, metalness: 0.9, roughness: 0.2 }});
            cardGroup.add(new THREE.Mesh(frameGeo, frameMat));

            const bodyGeo = new THREE.BoxGeometry(3.3, 3.3, 0.26);
            const bodyMat = new THREE.MeshStandardMaterial({{ color: 0x38a169, metalness: 0.7, roughness: 0.3 }});
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            body.position.y = 0.85;
            cardGroup.add(body);
            scene.add(cardGroup);

            const clock = new THREE.Clock();
            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();
                cardGroup.rotation.y = Math.sin(time * 0.8) * 0.2;
                renderer.render(scene, camera);
            }}
            animate();
        </script>
    </body>
    </html>
    """
  components.html(three_js_code, height=600, scrolling=False)

# -----------------------------------------------------------------------------
# 7. 하단 대시보드
# -----------------------------------------------------------------------------
st.write("")
b_col1, b_col2, b_col3 = st.columns([1, 1, 1], gap="small")

with b_col1:
  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">🛡️ 방지권 보유</div>
            <div class="stat-value">{st.session_state.shield}개</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with b_col2:
  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">💧 지온의 눈물</div>
            <div class="stat-value">{st.session_state.tears}개</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with b_col3:
  st.markdown(
      f"""
        <div class="stat-card">
            <div class="stat-title">📊 성공률 / 방지권 소모</div>
            <div class="stat-value" style="font-size: 14px;">{sp}% / {req_shield}개</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
