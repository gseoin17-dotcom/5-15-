import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온 코어 전투력 측정기 - COSMIC EDITION",
    page_icon="🌌",
    layout="wide",
)

# -----------------------------------------------------------------------------
# 2. 유틸리티 함수 및 비용 설정
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
      0: 300,
      1: 300,
      2: 500,
      3: 500,
      4: 1000,
      5: 1500,
      6: 2000,
      7: 2000,
      8: 3000,
      9: 5000,
      10: 10900,
      11: 20000,
      12: 35000,
      13: 55000,
      14: 100000,
      15: 180000,
      16: 300000,
      17: 300000,
      18: 500000,
      19: 800000,
      20: 1500000,
      21: 2500000,
      22: 4000000,
      23: 6500000,
      24: 10000000,
      25: 16000000,
      26: 25000000,
      27: 40000000,
      28: 65000000,
      29: 100000000,
      30: 150000000,
  }
  return cost_table.get(level, 150000000)


def get_shield_cost(level):
  base_cost = get_enhance_cost(level)
  return max(50000, base_cost * 15)


# -----------------------------------------------------------------------------
# 3. 게임 데이터베이스 정의 (얼굴, 몸통, 다리 각 30단계 + 0단계)
# -----------------------------------------------------------------------------
def generate_core_db(part_name, base_colors):
  db = {}
  for i in range(31):
    if i == 0:
      db[i] = {
          "name": f"0단계 : 무취의 {part_name} 코어",
          "desc": f"아직 아무런 지온의 기운이 없는 {part_name}.",
          "price": 0,
          "color": "#4a5568",
          "tier": 1,
          "power": 0,
      }
    else:
      tier = (
          1
          if i <= 5
          else (2 if i <= 10 else (3 if i <= 15 else (4 if i <= 20 else 5)))
      )
      if i >= 26:
        tier = 6

      names = [
          f"{i}단계 : 스쳐가는 지온 {part_name}코어",
          f"{i}단계 : 은은한 자이온 {part_name}코어",
          f"{i}단계 : 습한 지온 {part_name}코어",
          f"{i}단계 : 진득한 자이온 {part_name}코어",
          f"{i}단계 : 자극적인 지온 {part_name}코어",
          f"{i}단계 : 풍부한 자이온 {part_name}코어",
          f"{i}단계 : 압도적인 지온 {part_name}코어",
          f"{i}단계 : 폭발하는 지온 {part_name}코어",
          f"{i}단계 : 시공을 뒤흔드는 지온 {part_name}코어",
          f"{i}단계 : 치명적인 자이온 {part_name}코어",
          f"{i}단계 : 환각을 부르는 지온 {part_name}코어",
          f"{i}단계 : 공간지배 자이온 {part_name}코어",
          f"{i}단계 : 전설의 지온 {part_name}코어",
          f"{i}단계 : 신성한 자이온 {part_name}코어",
          f"{i}단계 : 신화급 지온 {part_name}코어",
          f"{i}단계 : 우주관통 자이온 {part_name}코어",
          f"{i}단계 : 차원균열 자이온 {part_name}코어",
          f"{i}단계 : Absolute 자이온 {part_name}코어",
          f"{i}단계 : 초월적 지온 {part_name}코어",
          f"{i}단계 : 자이온맘의 포근한 {part_name} 코어",
          f"{i}단계 : 자이온맘의 엄격한 {part_name} 코어",
          f"{i}단계 : 자이온맘의 전설의 {part_name} 코어",
          f"{i}단계 : 자이온맘의 100년 숙성 {part_name} 코어",
          f"{i}단계 : 자이온맘의 지온스프레이 {part_name} 코어",
          f"{i}단계 : 자이온맘의 무한한 은혜 {part_name} 코어",
          f"{i}단계 : 자이온맘의 궁극 필살기 {part_name} 코어",
          f"{i}단계 : 자이온맘의 창조와 구원 {part_name} 코어",
          f"{i}단계 : 자이온맘의 권능 {part_name} 코어",
          f"{i}단계 : 만물의 어머니 ★자이온맘★ {part_name} 코어",
          f"{i}단계 : ★태초의 자이온맘★ 절대신성 {part_name} 코어",
      ]
      name = names[i - 1]
      price = int(150 * (1.65**i)) if i < 30 else float("inf")
      power = int(10 * (1.8**i))

      db[i] = {
          "name": name,
          "desc": f"강력한 지온 에너지가 응축된 {part_name} 부위 코어.",
          "price": price,
          "color": base_colors[(i - 1) % len(base_colors)],
          "tier": tier,
          "power": power,
      }
  return db


COLORS_FACE = [
    "#718096",
    "#38a169",
    "#276749",
    "#319795",
    "#2c7a7b",
    "#3182ce",
    "#2b6cb0",
    "#805ad5",
    "#6b46c1",
    "#d69e2e",
    "#b7791f",
    "#dd6b20",
    "#c05621",
    "#e53e3e",
    "#9b2c2c",
    "#00f0ff",
    "#ff00ea",
    "#ffe600",
    "#ff0055",
    "#ffaa00",
    "#ff4500",
    "#ff007f",
    "#7b00ff",
    "#0088ff",
    "#00ffaa",
    "#ccff00",
    "#fffb00",
    "#ffffff",
    "#ff00aa",
    "#00ffff",
]
COLORS_BODY = [
    "#38a169",
    "#276749",
    "#319795",
    "#2c7a7b",
    "#3182ce",
    "#2b6cb0",
    "#805ad5",
    "#6b46c1",
    "#d69e2e",
    "#b7791f",
    "#dd6b20",
    "#c05621",
    "#e53e3e",
    "#9b2c2c",
    "#00f0ff",
    "#ff00ea",
    "#ffe600",
    "#ff0055",
    "#ffaa00",
    "#ff4500",
    "#ff007f",
    "#7b00ff",
    "#0088ff",
    "#00ffaa",
    "#ccff00",
    "#fffb00",
    "#ffffff",
    "#ff00aa",
    "#00ffff",
    "#718096",
]
COLORS_LEGS = [
    "#276749",
    "#319795",
    "#2c7a7b",
    "#3182ce",
    "#2b6cb0",
    "#805ad5",
    "#6b46c1",
    "#d69e2e",
    "#b7791f",
    "#dd6b20",
    "#c05621",
    "#e53e3e",
    "#9b2c2c",
    "#00f0ff",
    "#ff00ea",
    "#ffe600",
    "#ff0055",
    "#ffaa00",
    "#ff4500",
    "#ff007f",
    "#7b00ff",
    "#0088ff",
    "#00ffaa",
    "#ccff00",
    "#fffb00",
    "#ffffff",
    "#ff00aa",
    "#00ffff",
    "#718096",
    "#38a169",
]

CORE_DB = {
    "얼굴": generate_core_db("얼굴", COLORS_FACE),
    "몸통": generate_core_db("몸통", COLORS_BODY),
    "다리": generate_core_db("다리", COLORS_LEGS),
}

PROB_TABLE = {
    0: (100.0, 0.0, 0.0, 0.0),
    1: (100.0, 0.0, 0.0, 0.0),
    2: (100.0, 0.0, 0.0, 0.0),
    3: (95.0, 5.0, 0.0, 0.0),
    4: (95.0, 5.0, 0.0, 0.0),
    5: (90.0, 10.0, 0.0, 0.0),
    6: (90.0, 8.0, 2.0, 0.0),
    7: (90.0, 5.0, 5.0, 0.0),
    8: (85.0, 10.0, 5.0, 0.0),
    9: (80.0, 15.0, 5.0, 0.0),
    10: (80.0, 15.0, 5.0, 0.0),
    11: (75.0, 15.0, 5.0, 5.0),
    12: (70.0, 15.0, 5.0, 10.0),
    13: (70.0, 15.0, 7.0, 8.0),
    14: (65.0, 15.0, 10.0, 10.0),
    15: (60.0, 20.0, 10.0, 10.0),
    16: (60.0, 18.0, 12.0, 10.0),
    17: (55.0, 20.0, 15.0, 10.0),
    18: (50.0, 20.0, 17.0, 13.0),
    19: (50.0, 20.0, 20.0, 10.0),
    20: (45.0, 22.0, 23.0, 10.0),
    21: (40.0, 25.0, 25.0, 10.0),
    22: (40.0, 23.0, 27.0, 10.0),
    23: (40.0, 20.0, 30.0, 10.0),
    24: (40.0, 18.0, 32.0, 10.0),
    25: (35.0, 25.0, 30.0, 10.0),
    26: (50.0, 20.0, 25.0, 5.0),
    27: (40.0, 25.0, 30.0, 5.0),
    28: (30.0, 30.0, 35.0, 5.0),
    29: (20.0, 35.0, 40.0, 5.0),
}

CRITICAL_RATE = 0.05
PITY_MAX = 5

# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "selected_part" not in st.session_state:
  st.session_state.selected_part = "얼굴"

if "levels" not in st.session_state:
  st.session_state.levels = {"얼굴": 0, "몸통": 0, "다리": 0}
if "max_levels" not in st.session_state:
  st.session_state.max_levels = {"얼굴": 0, "몸통": 0, "다리": 0}
if "money" not in st.session_state:
  st.session_state.money = 1000000
if "status" not in st.session_state:
  st.session_state.status = "READY"
if "shields" not in st.session_state:
  st.session_state.shields = {"얼굴": 0, "몸통": 0, "다리": 0}
if "tears" not in st.session_state:
  st.session_state.tears = 0
if "pity_counts" not in st.session_state:
  st.session_state.pity_counts = {"얼굴": 0, "몸통": 0, "다리": 0}

# -----------------------------------------------------------------------------
# 5. 강화 및 전투력 계산 로직
# -----------------------------------------------------------------------------


def get_total_power():
  return sum(
      CORE_DB[part][st.session_state.levels[part]]["power"]
      for part in ["얼굴", "몸통", "다리"]
  )


def run_enhance():
  part = st.session_state.selected_part
  curr = st.session_state.levels[part]
  if curr >= 30:
    return

  cost = get_enhance_cost(curr)
  if st.session_state.money < cost:
    st.session_state.status = "NOT_ENOUGH_MONEY"
    return

  st.session_state.money -= cost

  if st.session_state.pity_counts[part] >= PITY_MAX - 1:
    st.session_state.levels[part] += 1
    st.session_state.status = "PITY_SUCCESS"
    st.session_state.pity_counts[part] = 0
    if (
        st.session_state.levels[part]
        > st.session_state.max_levels[part]
    ):
      st.session_state.max_levels[part] = st.session_state.levels[part]
    return

  sp, down_p, dp, hold_p = PROB_TABLE[curr]
  r = random.uniform(0, 100)

  success_limit = sp
  down_limit = success_limit + down_p
  destroy_limit = down_limit + dp

  if r < success_limit:
    st.session_state.pity_counts[part] = 0
    if random.random() < CRITICAL_RATE and curr + 2 <= 30:
      st.session_state.levels[part] += 2
      st.session_state.status = "CRITICAL"
    else:
      st.session_state.levels[part] += 1
      st.session_state.status = "SUCCESS"
  elif r < down_limit:
    st.session_state.pity_counts[part] += 1
    if curr > 0:
      st.session_state.levels[part] -= 1
    st.session_state.status = "FAILED"
    st.session_state.tears = min(120, st.session_state.tears + 1)
  elif r < destroy_limit:
    if st.session_state.shields[part] > 0:
      st.session_state.shields[part] -= 1
      st.session_state.pity_counts[part] += 1
      st.session_state.status = "SHIELD_SAVED"
      st.session_state.tears = min(120, st.session_state.tears + 1)
    else:
      st.session_state.pity_counts[part] += 1
      st.session_state.levels[part] = 0
      st.session_state.status = "DESTROYED"
      st.session_state.tears = min(120, st.session_state.tears + 2)
  else:
    st.session_state.pity_counts[part] += 1
    st.session_state.status = "HOLD"
    st.session_state.tears = min(120, st.session_state.tears + 1)

  if (
      st.session_state.levels[part]
      > st.session_state.max_levels[part]
  ):
    st.session_state.max_levels[part] = st.session_state.levels[part]


def dev_force_success():
  part = st.session_state.selected_part
  curr = st.session_state.levels[part]
  if curr < 30:
    st.session_state.levels[part] += 1
    st.session_state.status = "SUCCESS"
    if (
        st.session_state.levels[part]
        > st.session_state.max_levels[part]
    ):
      st.session_state.max_levels[part] = st.session_state.levels[part]


def sell():
  part = st.session_state.selected_part
  curr = st.session_state.levels[part]
  if curr == 0:
    return
  price_val = CORE_DB[part][curr]["price"]
  if price_val == float("inf"):
    st.session_state.money = float("inf")
  else:
    st.session_state.money += price_val
  st.session_state.levels[part] = 0
  st.session_state.status = "READY"


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
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }
    .element-container, .stMarkdown {
        background: transparent !important;
    }
    
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
    </style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. 메인 레이아웃 및 엔딩 처리
# -----------------------------------------------------------------------------
all_max = all(st.session_state.levels[p] == 30 for p in ["얼굴", "몸통", "다리"])

if all_max:
  ending_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                overflow: hidden;
                background: #020617;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            }
            #container { width: 100vw; height: 100vh; position: absolute; top:0; left:0; }
            
            .credits-container {
                position: absolute;
                width: 100%;
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                z-index: 100;
                pointer-events: none;
                text-align: center;
                animation: fadeIn 2s ease-in-out forwards;
            }

            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            .ending-title {
                font-size: 52px;
                font-weight: 900;
                background: linear-gradient(90deg, #ffffff, #00ffff, #ff00aa, #fffb00);
                background-size: 300% auto;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: rainbowText 3s linear infinite;
                text-shadow: 0 0 30px rgba(0,255,255,0.6);
                margin-bottom: 10px;
            }

            @keyframes rainbowText {
                0% { background-position: 0% center; }
                100% { background-position: 300% center; }
            }

            .ending-subtitle {
                font-size: 20px;
                color: #cbd5e1;
                font-weight: 600;
                margin-bottom: 30px;
                letter-spacing: 2px;
            }

            .credit-box {
                background: rgba(15, 23, 42, 0.75);
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 20px 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 40px rgba(0, 255, 255, 0.3);
            }

            .credit-line {
                font-size: 15px;
                color: #fde68a;
                margin: 8px 0;
                font-weight: 700;
            }
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    </head>
    <body>
        <div id="container"></div>
        <div class="credits-container">
            <div class="ending-title">★ 완벽한 지온 코어 장착 완료 ★</div>
            <div class="ending-subtitle">얼굴, 몸통, 다리 3대 코어가 결합하여 우주 최강의 전투력에 도달했습니다!</div>
            <div class="credit-box">
                <div class="credit-line">🏆 CREATED BY : 자이온 팀</div>
            </div>
        </div>

        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0, 15);

            const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.getElementById('container').appendChild(renderer.domElement);

            const particleCount = 2000;
            const geo = new THREE.BufferGeometry();
            const positions = new Float32Array(particleCount * 3);
            const velocities = [];

            for(let i=0; i<particleCount; i++) {
                positions[i*3] = (Math.random() - 0.5) * 20;
                positions[i*3 + 1] = (Math.random() - 0.5) * 20;
                positions[i*3 + 2] = (Math.random() - 0.5) * 20;

                velocities.push({
                    x: (Math.random() - 0.5) * 0.05,
                    y: (Math.random() - 0.5) * 0.05,
                    z: (Math.random() - 0.5) * 0.05,
                    rot: Math.random() * 0.02
                });
            }
            geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

            const mat = new THREE.PointsMaterial({
                color: 0x00ffff,
                size: 0.2,
                transparent: true,
                opacity: 0.9,
                blending: THREE.AdditiveBlending
            });
            const starSystem = new THREE.Points(geo, mat);
            scene.add(starSystem);

            const coreGeo = new THREE.TorusKnotGeometry(3, 1, 128, 32, 2, 3);
            const coreMat = new THREE.MeshPhysicalMaterial({
                color: 0xff00aa,
                emissive: 0x00ffff,
                emissiveIntensity: 1.5,
                metalness: 0.9,
                roughness: 0.1,
                wireframe: true
            });
            const coreMesh = new THREE.Mesh(coreGeo, coreMat);
            scene.add(coreMesh);

            function animate() {
                requestAnimationFrame(animate);
                const time = Date.now() * 0.001;

                coreMesh.rotation.x = time * 0.5;
                coreMesh.rotation.y = time * 0.7;

                const posArr = geo.attributes.position.array;
                for(let i=0; i<particleCount; i++) {
                    posArr[i*3] += velocities[i].x;
                    posArr[i*3 + 1] += velocities[i].y;
                    posArr[i*3 + 2] += velocities[i].z;
                }
                geo.attributes.position.needsUpdate = true;

                renderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        </script>
    </body>
    </html>
    """
  components.html(ending_html, height=650, scrolling=False)

  st.write("")
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("🔄 우주 초기화 (처음부터 다시하기)", use_container_width=True):
      st.session_state.levels = {"얼굴": 0, "몸통": 0, "다리": 0}
      st.session_state.money = 1000000
      st.session_state.shields = {"얼굴": 0, "몸통": 0, "다리": 0}
      st.session_state.tears = 0
      st.session_state.pity_counts = {"얼굴": 0, "몸통": 0, "다리": 0}
      st.session_state.status = "READY"
      st.rerun()

else:
  # 상단에 캐릭터 종합 전투력 대시보드 표시
  total_power = get_total_power()
  st.markdown(
      f"""
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(255,255,255,0.2); border-radius: 12px; padding: 15px; text-align: center; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
            <div style="font-size: 14px; color: #fde68a; font-weight: 700; letter-spacing: 1px;">⚔️ 지온 캐릭터 종합 전투력 (POWER) ⚔️</div>
            <div style="font-size: 32px; font-weight: 900; color: #00ffff; text-shadow: 0 0 15px rgba(0,255,255,0.6); margin-top: 5px;">{total_power:,} CP</div>
            <div style="font-size: 12px; color: #cbd5e1; margin-top: 5px;">
                얼굴 코어 Lv.{st.session_state.levels['얼굴']} | 몸통 코어 Lv.{st.session_state.levels['몸통']} | 다리 코어 Lv.{st.session_state.levels['다리']}
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  left_col, right_col = st.columns([2.2, 7.8], gap="medium")

  with left_col:
    st.markdown(
        "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🎯 장착 파츠"
        " 선택</h4>",
        unsafe_allow_html=True,
    )
    selected_part = st.selectbox(
        "강화할 부위 선택",
        ["얼굴", "몸통", "다리"],
        key="selected_part_box",
        label_visibility="collapsed",
    )
    st.session_state.selected_part = selected_part

    st.markdown(
        "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🛠️ 시스템"
        " 설정</h4>",
        unsafe_allow_html=True,
    )
    dev_mode = st.toggle("💻 개발자 모드 활성화", value=False)

    st.markdown(
        "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🌌 코어 강화"
        " 제어</h4>",
        unsafe_allow_html=True,
    )

    curr_lvl = st.session_state.levels[st.session_state.selected_part]
    if st.button(
        f"🔥 {st.session_state.selected_part} 코어 강화",
        use_container_width=True,
        disabled=(curr_lvl >= 30),
    ):
      cost = get_enhance_cost(curr_lvl)
      if st.session_state.money < cost:
        st.error("강화 비용 부족!")
      else:
        run_enhance()
        st.rerun()

    if dev_mode:
      st.write("")
      if st.button(
          f"✨ [DEV] {st.session_state.selected_part} 무조건 성공",
          use_container_width=True,
          disabled=(curr_lvl >= 30),
      ):
        dev_force_success()
        st.rerun()

    st.write("")
    if st.button(
        f"💰 현재 {st.session_state.selected_part} 코어 판매",
        use_container_width=True,
        disabled=(curr_lvl == 0),
    ):
      sell()
      st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    s_col1, s_col2 = st.columns(2)

    with s_col1:
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px;"
          f" color:#fde68a;'>💳 보유 금액</div><div style='font-size:15px;"
          f" font-weight:800;"
          f" color:#ffffff;'>{format_gold(st.session_state.money)}</div></div>",
          unsafe_allow_html=True,
      )
      st.write("")
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px;"
          f" color:#fde68a;'>💧 눈물</div><div style='font-size:15px;"
          f" font-weight:800; color:#ffffff;'>{st.session_state.tears} /"
          " 120개</div></div>",
          unsafe_allow_html=True,
      )

    with s_col2:
      current_shield_count = st.session_state.shields[
          st.session_state.selected_part
      ]
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px;"
          f" color:#fde68a;'>🛡️ 방지권</div><div style='font-size:15px;"
          f" font-weight:800; color:#ffffff;'>{current_shield_count} /"
          " 3개</div></div>",
          unsafe_allow_html=True,
      )
      st.write("")

      pity_left = (
          PITY_MAX - st.session_state.pity_counts[st.session_state.selected_part]
      )
      st.markdown(
          f"<div style='text-align: center;'><div style='font-size:12px;"
          f" color:#fde68a;'>✨ 자이온맘의 가호</div><div style='font-size:13px;"
          f" font-weight:800;"
          f" color:#ffffff;'>실패까지 <b>{pity_left}회</b></div></div>",
          unsafe_allow_html=True,
      )

    st.markdown(
        "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )

    tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])

    with tab_shop1:
      current_shield_cost = get_shield_cost(curr_lvl)
      st.markdown(
          f"<div style='font-size:14px; color:#cbd5e1; margin-bottom:8px;'>"
          f"<b>조건:</b> 18단계 이상 | <b>보유한도:</b> 최대 3개<br><b>가격:</b>"
          f" <span style='font-size:16px; font-weight:bold; color:#fde68a;'>"
          f"{format_gold(current_shield_cost)}</span></div>",
          unsafe_allow_html=True,
      )

      can_buy_shield = curr_lvl >= 18 and current_shield_count < 3
      if st.button(
          "방지권 구매", use_container_width=True, disabled=not can_buy_shield
      ):
        if curr_lvl < 18:
          st.warning("18단계 이상부터 구매 가능합니다.")
        elif current_shield_count >= 3:
          st.warning("최대 3개까지만 보유 가능합니다.")
        elif st.session_state.money >= current_shield_cost:
          st.session_state.money -= current_shield_cost
          st.session_state.shields[st.session_state.selected_part] += 1
          st.success("파괴 방지권 구매 완료!")
          st.rerun()
        else:
          st.error("금액이 부족합니다.")

    with tab_shop2:
      if curr_lvl >= 28:
        st.markdown(
            "<div style='font-size:14px; color:#ef4444; font-weight:700;"
            " margin-bottom:8px;'>⚠️ 28단계 이상부터는 신성한 기운으로 인해 지온의"
            " 눈물을 사용할 수 없습니다!</div>",
            unsafe_allow_html=True,
        )
      else:
        st.markdown(
            f"<div style='font-size:14px; color:#cbd5e1;"
            f" margin-bottom:8px;'><b>효과:</b> 눈물 40개 소모 (50% 확률로 1~3단계"
            f" 상승)<br><b>현재보유:</b> <span style='font-weight:bold;"
            f" color:#38bdf8;'>{st.session_state.tears} / 120개</span></div>",
            unsafe_allow_html=True,
        )

      can_use_tears = curr_lvl < 28
      if st.button(
          "눈물 기적 가동", use_container_width=True, disabled=not can_use_tears
      ):
        if curr_lvl >= 28:
          st.warning("28단계부터는 눈물을 사용할 수 없습니다.")
        elif st.session_state.tears >= 40:
          st.session_state.tears -= 40
          if random.random() < 0.50:
            add_lvl = random.choice([1, 2, 3])
            st.session_state.levels[st.session_state.selected_part] = min(
                30, curr_lvl + add_lvl
            )
            st.session_state.status = (
                "CRITICAL" if add_lvl >= 2 else "SUCCESS"
            )
            st.success(f"눈물 기적 대성공! {add_lvl}단계 상승!")
          else:
            st.session_state.status = "FAILED"
            st.warning("눈물의 기적이 실패했습니다...")
          st.rerun()
        else:
          st.error("눈물 40개가 필요합니다.")

  with right_col:
    current_part = st.session_state.selected_part
    current_level = st.session_state.levels[current_part]
    curr_data = CORE_DB[current_part][current_level]
    card_color = curr_data["color"]
    card_title = curr_data["name"]
    card_desc = curr_data["desc"]
    card_price = format_gold(curr_data["price"])
    card_power = f"{curr_data['power']:,} CP"
    current_cost = format_gold(get_enhance_cost(current_level))
    tier = curr_data["tier"]
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

              .cinematic-ui {{
                  position: absolute;
                  bottom: 25px; 
                  left: 50%;
                  transform: translateX(-50%);
                  width: 100%;
                  text-align: center;
                  z-index: 100;
                  pointer-events: none;
                  opacity: 0;
                  transition: opacity 0.4s ease-in-out;
              }}

              .cinematic-ui.visible {{
                  opacity: 1;
              }}

              .title-tier-1 {{ font-size: 26px; font-weight: 800; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
              .title-tier-2 {{ font-size: 30px; font-weight: 800; color: #f59e0b; text-shadow: 0 0 22px #f59e0b; }}
              .title-tier-3 {{ font-size: 34px; font-weight: 800; color: #ef4444; text-shadow: 0 0 25px #ef4444; }}
              .title-tier-4 {{ font-size: 38px; font-weight: 800; color: #c084fc; text-shadow: 0 0 28px #c084fc; }}
              .title-tier-5 {{ font-size: 42px; font-weight: 800; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 12px rgba(255,126,95,0.6)); }}
              .title-tier-6 {{ font-size: 46px; font-weight: 800; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; filter: drop-shadow(0 0 15px rgba(255,255,255,0.8)); }}

              @keyframes rainbow {{ 0% {{ background-position: 0% center; }} 100% {{ background-position: 200% center; }} }}

              .shaking-text {{
                  animation: textVibe 0.18s infinite alternate ease-in-out;
              }}
              @keyframes textVibe {{
                  0% {{ transform: translate(0px, 0px) rotate(0deg); }}
                  25% {{ transform: translate(-1.5px, 1px) rotate(-0.5deg); }}
                  50% {{ transform: translate(1.5px, -1.5px) rotate(0.8deg); }}
                  75% {{ transform: translate(-1px, -1px) rotate(-0.3deg); }}
                  100% {{ transform: translate(1px, 1.5px) rotate(0.5deg); }}
              }}

              .status-header {{ font-size: 15px; font-weight: 800; margin-bottom: 2px; letter-spacing: 1px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
              .power-text {{ font-size: 16px; font-weight: 900; color: #00ffff; margin-top: 2px; text-shadow: 0 0 12px rgba(0,255,255,0.8); }}
              .desc-text {{ font-size: 12px; color: #cbd5e1; margin-top: 2px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); font-weight: 500; }}
              .price-text {{ font-size: 14px; font-weight: 800; color: #fbbf24; margin-top: 2px; text-shadow: 0 0 15px rgba(0,0,0,0.95); }}
              .cost-text {{ font-size: 11px; font-weight: 700; color: #f87171; margin-top: 2px; text-shadow: 0 0 12px rgba(0,0,0,0.95); }}
          </style>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
      </head>
      <body>
          <div id="container"></div>

          <div id="cinematicUi" class="cinematic-ui">
              <div id="statusText" class="status-header">READY</div>
              <div id="mainTitle" class="title-tier-{tier}">{card_title}</div>
              <div id="powerText" class="power-text">부위 전투력: {card_power}</div>
              <div id="descText" class="desc-text">"{card_desc}"</div>
              <div id="priceText" class="price-text">예상 가치: {card_price}</div>
              <div id="costText" class="cost-text">필요 강화 비용: {current_cost}</div>
          </div>

          <script>
              const uiElement = document.getElementById('cinematicUi');

              const currentLevel = {current_level};
              if (currentLevel >= 20) {{
                  document.getElementById('mainTitle').classList.add('shaking-text');
                  document.getElementById('powerText').classList.add('shaking-text');
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
                  statusText.innerText = "⚡ COSMIC CRITICAL HIT!! (+2단계 이상 대성공) ⚡";
                  statusColor = "#ffffff"; 
                  particleSize = 0.55;
                  particleSpeed = 2.5;
                  glowIntensity = 35;
              }} else if (status === "PITY_SUCCESS") {{
                  statusText.innerText = "✨ 자이온맘의 가호 발동! (천장 100% 성공) ✨";
                  statusColor = "#fde68a";
                  particleSize = 0.45;
                  particleSpeed = 2.0;
                  glowIntensity = 30;
              }} else if (status === "SUCCESS") {{
                  statusText.innerText = "✨ COSMIC SUCCESS (강화 성공) ✨";
                  statusColor = tierColor;
                  particleSize = 0.35;
                  particleSpeed = 1.5;
                  glowIntensity = 22;
              }} else if (status === "SHIELD_SAVED") {{
                  statusText.innerText = "🛡️ SHIELD PROTECTED! (우주 방어 발동) 🛡️";
                  statusColor = "#60a5fa";
              }} else if (status === "DESTROYED") {{
                  statusText.innerText = "💥 BLACKHOLE DESTROYED (코어 붕괴됨) 💥";
                  statusColor = "#ef4444";
                  particleSpeed = 1.2;
              }} else if (status === "FAILED") {{
                  statusText.innerText = "🔻 FAILED (에너지 하락) 🔻";
                  statusColor = "#64748b";
                  particleSpeed = 0.5;
                  glowIntensity = 6;
              }} else if (status === "HOLD") {{
                  statusText.innerText = "🔒 HOLD (에너지 동결) 🔒";
                  statusColor = "#94a3b8";
                  particleSpeed = 0.7;
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
              renderer.shadowMap.enabled = true;
              document.getElementById('container').appendChild(renderer.domElement);

              const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
              scene.add(ambientLight);

              const mainLight = new THREE.DirectionalLight(0xffffff, 2.5);
              mainLight.position.set(5, 8, 5);
              scene.add(mainLight);

              const pointLight = new THREE.PointLight(statusColor, glowIntensity, 40);
              pointLight.position.set(0, 0, 3);
              scene.add(pointLight);

              const particleCount = 850;
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
                  color: new THREE.Color(statusColor),
                  size: particleSize,
                  transparent: true,
                  opacity: status === "FAILED" ? 0.3 : 0.9,
                  blending: THREE.AdditiveBlending,
                  depthWrite: false
              }});
              const particleSystem = new THREE.Points(particleGeo, particleMat);
              scene.add(particleSystem);

              const objectGroup = new THREE.Group();
              objectGroup.position.y = -0.7;

              let baseGeo;
              const lvl = {current_level};
              const part = "{current_part}";

              if (part === "얼굴") {{
                  if (lvl <= 5) baseGeo = new THREE.SphereGeometry(2.0, 16, 16);
                  else if (lvl <= 10) baseGeo = new THREE.DodecahedronGeometry(2.1);
                  else if (lvl <= 20) baseGeo = new THREE.IcosahedronGeometry(2.2);
                  else baseGeo = new THREE.TorusKnotGeometry(1.4, 0.45, 64, 16, 2, 3);
              }} else if (part === "몸통") {{
                  if (lvl <= 5) baseGeo = new THREE.BoxGeometry(2.2, 2.5, 1.5);
                  else if (lvl <= 10) baseGeo = new THREE.CylinderGeometry(1.8, 2.2, 2.8, 6);
                  else if (lvl <= 20) baseGeo = new THREE.ConeGeometry(2.2, 3.2, 8);
                  else baseGeo = new THREE.OctahedronGeometry(2.6);
              }} else {{
                  if (lvl <= 5) baseGeo = new THREE.CylinderGeometry(1.5, 1.8, 3.0, 5);
                  else if (lvl <= 10) baseGeo = new THREE.CylinderGeometry(1.2, 2.0, 3.2, 7);
                  else if (lvl <= 20) baseGeo = new THREE.TorusGeometry(1.8, 0.6, 16, 32);
                  else baseGeo = new THREE.CylinderGeometry(0.8, 2.3, 3.5, 12);
              }}

              const outerMat = new THREE.MeshPhysicalMaterial({{
                  color: tierColor,
                  emissive: status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? statusColor : "#111111",
                  emissiveIntensity: status === "SUCCESS" ? 0.5 : (status === "CRITICAL" || status === "PITY_SUCCESS" ? 0.9 : 0.15),
                  metalness: 0.9,
                  roughness: 0.15,
                  transmission: 0.6,
                  transparent: true,
                  opacity: status === "FAILED" ? 0.5 : 0.95,
                  wireframe: false
              }});
              const outerMesh = new THREE.Mesh(baseGeo, outerMat);
              objectGroup.add(outerMesh);

              const coreGeo = new THREE.SphereGeometry(1.1, 32, 32);
              const coreMat = new THREE.MeshPhysicalMaterial({{
                  color: 0xffffff,
                  emissive: statusColor,
                  emissiveIntensity: status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? 3.0 : 1.2,
                  roughness: 0.05,
                  metalness: 0.95,
                  transmission: 0.8
              }});
              const coreMesh = new THREE.Mesh(coreGeo, coreMat);
              objectGroup.add(coreMesh);

              scene.add(objectGroup);

              uiElement.classList.add('visible');

              if (status === "DESTROYED") {{
                  outerMesh.visible = false;
                  coreMesh.visible = false;

                  const shardCount = 55;
                  const shards = [];
                  const shardGroup = new THREE.Group();
                  shardGroup.position.y = -0.7;

                  for(let i=0; i<shardCount; i++) {{
                      const sGeo = new THREE.BoxGeometry(0.3 + Math.random()*0.2, 0.3 + Math.random()*0.2, 0.3 + Math.random()*0.2);
                      const sMat = new THREE.MeshStandardMaterial({{
                          color: tierColor,
                          roughness: 0.2,
                          metalness: 0.9,
                          emissive: "#ef4444",
                          emissiveIntensity: 1.0
                      }});
                      const shard = new THREE.Mesh(sGeo, sMat);
                      shard.position.set(0, 0, 0);
                      
                      const u = Math.random();
                      const v = Math.random();
                      const theta = u * 2.0 * Math.PI;
                      const phi = Math.acos(2.0 * v - 1.0);
                      const speed = 4.0 + Math.random() * 5.0;
                      
                      shard.userData = {{
                          vx: speed * Math.sin(phi) * Math.cos(theta),
                          vy: speed * Math.sin(phi) * Math.sin(theta),
                          vz: speed * Math.cos(phi),
                          rx: (Math.random() - 0.5) * 20,
                          ry: (Math.random() - 0.5) * 20
                      }};

                      shardGroup.add(shard);
                      shards.push(shard);
                  }}
                  scene.add(shardGroup);

                  gsap.to(shardGroup.position, {{
                      duration: 1.2,
                      ease: "power2.out",
                      onUpdate: function() {{
                          const progress = this.progress();
                          shards.forEach(s => {{
                              s.position.x += s.userData.vx * 0.02;
                              s.position.y += s.userData.vy * 0.02 - 0.05;
                              s.position.z += s.userData.vz * 0.02;
                              s.rotation.x += s.userData.rx * 0.02;
                              s.rotation.y += s.userData.ry * 0.02;
                              s.material.opacity = 1.0 - progress;
                              s.material.transparent = true;
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
                      outerMesh.rotation.x = time * (0.5 * rotSpeed);
                      outerMesh.rotation.y = time * (0.75 * rotSpeed);
                      coreMesh.rotation.x = -time * (1.2 * rotSpeed);
                      coreMesh.rotation.y = -time * (1.5 * rotSpeed);
                      objectGroup.rotation.y = Math.sin(time * 0.7) * 0.25;
                  }}

                  const positions = particleGeo.attributes.position.array;
                  for(let i=0; i<particleCount; i++) {{
                      positions[i*3] += particleVelocities[i].x;
                      positions[i*3 + 1] += particleVelocities[i].y;
                      positions[i*3 + 2] += particleVelocities[i].z;

                      if(positions[i*3 + 1] > 3.0) {{
                          positions[i*3 + 1] = -5.0;
                          positions[i*3] = (Math.random() - 0.5) * 7.0;
                          positions[i*3 + 2] = (Math.random() - 0.5) * 7.0;
                      }}
                  }}
                  particleGeo.attributes.position.needsUpdate = true;

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

    components.html(three_js_code, height=580, scrolling=False)
