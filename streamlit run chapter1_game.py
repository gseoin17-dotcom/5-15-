import streamlit as st
import random

st.set_page_config(page_title="지온 vs 자이온", page_icon="⚔️")

# =========================================================
# 데이터 정의
# =========================================================
CHAR_TEMPLATE = {
    "지온": {"hp": 100, "max_hp": 100, "atk": 15, "def": 8, "spd": 10, "gauge": 0},
    "지온맘": {"hp": 80, "max_hp": 80, "atk": 8, "def": 10, "spd": 9, "gauge": 0},
}

ENEMY_TEMPLATE = {
    "동네양아치 슬라임": {"hp": 30, "max_hp": 30, "atk": 6, "def": 2},
    "골목대장 몹씨": {"hp": 200, "max_hp": 200, "atk": 20, "def": 12},
}

# =========================================================
# 세션 상태 초기화
# =========================================================
def init_state():
    defaults = {
        "scene": "intro",
        "party": {"지온": dict(CHAR_TEMPLATE["지온"])},
        "log": [],
        "enemy_name": None,
        "enemy": None,
        "boss_phase": 1,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

def add_log(msg: str):
    st.session_state.log.append(msg)

def show_log(n=8):
    with st.container(border=True):
        for m in st.session_state.log[-n:]:
            st.write(m)

def start_battle(enemy_name: str):
    st.session_state.enemy_name = enemy_name
    st.session_state.enemy = dict(ENEMY_TEMPLATE[enemy_name])
    st.session_state.boss_phase = 1
    st.session_state.log = []
    st.session_state.scene = "battle"
    st.rerun()

# =========================================================
# 전투 로직
# =========================================================
def player_attack():
    지온 = st.session_state.party["지온"]
    enemy = st.session_state.enemy

    dmg = max(1, 지온["atk"] - enemy["def"] + random.randint(-2, 3))
    enemy["hp"] = max(0, enemy["hp"] - dmg)
    지온["gauge"] = min(100, 지온["gauge"] + 20)
    add_log(f"⚔️ 지온: \"일단 박아본다!\" → {dmg} 데미지! (남은 HP {enemy['hp']})")

    if enemy["hp"] <= 0:
        return True  # 전투 승리

    # 보스 페이즈 전환 체크
    if st.session_state.enemy_name == "골목대장 몹씨" and enemy["hp"] <= enemy["max_hp"] * 0.5 and st.session_state.boss_phase == 1:
        st.session_state.boss_phase = 2
        add_log("🔥 골목대장 몹씨: \"너 때문에 체면이 말이 아니잖아!!\" (공격력 상승)")

    enemy_turn()
    return False

def player_ultimate():
    지온 = st.session_state.party["지온"]
    enemy = st.session_state.enemy
    if 지온["gauge"] < 100:
        add_log("❗ 아직 허세력 게이지가 부족하다.")
        return False

    dmg = int((지온["atk"] * 3) - enemy["def"])
    dmg = max(5, dmg)
    enemy["hp"] = max(0, enemy["hp"] - dmg)
    지온["gauge"] = 0
    add_log(f"✨ 지온: \"이게 진짜다!!\" → {dmg} 데미지의 필살기 작렬!")

    if enemy["hp"] <= 0:
        return True

    enemy_turn()
    return False

def enemy_turn():
    지온 = st.session_state.party["지온"]
    enemy = st.session_state.enemy
    atk_mult = 1.5 if (st.session_state.enemy_name == "골목대장 몹씨" and st.session_state.boss_phase == 2) else 1.0

    dmg = max(1, int(enemy["atk"] * atk_mult - 지온["def"] + random.randint(-2, 2)))
    지온["hp"] = max(0, 지온["hp"] - dmg)
    add_log(f"💥 {st.session_state.enemy_name}의 반격! → 지온이 {dmg} 데미지를 입었다. (남은 HP {지온['hp']})")

# =========================================================
# 씬: 인트로
# =========================================================
def scene_intro():
    st.title("1장. 지온마을 — 여기가 어디게")
    st.markdown(
        """
        세상엔 원래 마을이 하나였다. 이름은 그냥 **"온"**.
        어느 날 하늘에 금이 가더니, 세상은 **지온**과 **자이온**, 두 세계로 갈라졌다.

        오늘의 주인공 **지온**은 그런 사정 따위 알 바 아니다.
        그는 오늘도 늦잠을 잤을 뿐이다.
        """
    )
    if st.button("▶ 이야기 시작하기", use_container_width=True):
        st.session_state.scene = "town"
        st.rerun()

# =========================================================
# 씬: 마을 (분기 선택 + 잡몹전 진입)
# =========================================================
def scene_town():
    st.header("🏘️ 지온마을 어귀")
    st.write("**동네 아저씨**: 지온아! 뒷골목에 '골목대장 몹씨'가 또 나타났어! 애들 간식을 다 뺏어갔다니까!")
    st.write("**지온**: ...그거 하나 갖고 온 마을이 이 난리라고요?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("😤 \"알겠어요, 제가 가볼게요.\"", use_container_width=True):
            st.session_state.party["지온"]["gauge"] += 5
            add_log("정의감 루트 선택! (허세력 +5)")
            start_battle("동네양아치 슬라임")
    with col2:
        if st.button("💰 \"뭐 주실 거예요?\"", use_container_width=True):
            add_log("실속 루트 선택! (골드 +20 — 추후 상점 시스템에 반영 예정)")
            start_battle("동네양아치 슬라임")

# =========================================================
# 씬: 전투 (잡몹 / 보스 공용)
# =========================================================
def scene_battle():
    지온 = st.session_state.party["지온"]
    enemy = st.session_state.enemy
    name = st.session_state.enemy_name

    st.header(f"⚔️ 전투 — {name}")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("지온")
        st.progress(지온["hp"] / 지온["max_hp"], text=f"HP {지온['hp']}/{지온['max_hp']}")
        st.progress(지온["gauge"] / 100, text=f"허세력 {지온['gauge']}%")
    with c2:
        st.subheader(name)
        st.progress(enemy["hp"] / enemy["max_hp"], text=f"HP {enemy['hp']}/{enemy['max_hp']}")

    show_log()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗡️ 공격하기", use_container_width=True, disabled=(지온["hp"] <= 0)):
            win = player_attack()
            if win:
                on_victory()
            elif 지온["hp"] <= 0:
                on_defeat()
            st.rerun()
    with col2:
        if st.button("✨ 필살기 (허세력 100% 필요)", use_container_width=True, disabled=(지온["gauge"] < 100 or 지온["hp"] <= 0)):
            win = player_ultimate()
            if win:
                on_victory()
            elif 지온["hp"] <= 0:
                on_defeat()
            st.rerun()

def on_victory():
    name = st.session_state.enemy_name
    add_log(f"🎉 {name} 격파!")
    if name == "동네양아치 슬라임":
        st.session_state.scene = "boss_intro"
    elif name == "골목대장 몹씨":
        st.session_state.scene = "ending"

def on_defeat():
    add_log("💀 지온이 쓰러졌다... (마을 사람들이 업어가서 마을 어귀로 후송)")
    st.session_state.scene = "town"
    st.session_state.party["지온"]["hp"] = st.session_state.party["지온"]["max_hp"]

# =========================================================
# 씬: 보스 등장 연출
# =========================================================
def scene_boss_intro():
    st.header("👑 뒷골목 끝, 낡은 왕좌 위의 그림자")
    st.write("**골목대장 몹씨**: 어이구, 이게 누구야. 마을 백수 아니신가?")
    st.write("**지온**: 프리랜서라니까요. 됐고, 애들 간식 내놔.")
    if st.button("⚔️ 보스전 시작", use_container_width=True):
        start_battle("골목대장 몹씨")

# =========================================================
# 씬: 엔딩 (지온맘 합류)
# =========================================================
def scene_ending():
    st.header("🌸 뜻밖의 지원군")
    st.write("**???**: 아이고, 이 난리를 혼자 다 치고 있었어?")
    st.write("**지온**: 어... 엄마?")
    st.write("**지온맘**: 오늘부터 나도 같이 다닌다. 잔말 말고.")

    if "지온맘" not in st.session_state.party:
        st.session_state.party["지온맘"] = dict(CHAR_TEMPLATE["지온맘"])
        st.success("🎊 지온맘이 파티에 합류했습니다! (스킬: 밥은 먹고 다니니 / 엄마 화나면 무섭다)")

    st.info("2장. 지온성 — '결재 좀 해주세요' 에서 계속됩니다.")
    if st.button("🔄 처음부터 다시하기", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

# =========================================================
# 라우터
# =========================================================
SCENES = {
    "intro": scene_intro,
    "town": scene_town,
    "battle": scene_battle,
    "boss_intro": scene_boss_intro,
    "ending": scene_ending,
}

SCENES[st.session_state.scene]()
