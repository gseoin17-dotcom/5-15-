import random
import time
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="공들의 전쟁: 지온 vs 자이온", page_icon="⚽", layout="centered"
)

st.title("🔴🔵 공들의 전쟁 (Ball Battle Royale)")
st.write(
    "지온 진영과 자이온 진영의 피할 수 없는 대결! 각 캐릭터의 특수 스킬을 사용하여 승리를 이끌어보세요."
)

# 캐릭터 데이터 정의
CHARACTERS = {
    "지온": {
        "team": "지온",
        "hp": 100,
        "atk": 12,
        "speed": 10,
        "skill_name": "지온의 돌격",
        "desc": "빠른 속도로 적을 치고 지나갑니다.",
    },
    "지온맘": {
        "team": "지온",
        "hp": 120,
        "atk": 10,
        "speed": 8,
        "skill_name": "엄마의 보호막",
        "desc": "체력을 회복하고 보호막을 생성합니다.",
    },
    "지온왕": {
        "team": "지온",
        "hp": 150,
        "atk": 18,
        "speed": 6,
        "skill_name": "왕의 심판",
        "desc": "막대한 광역 피해를 입힙니다.",
    },
    "자이온": {
        "team": "자이온",
        "hp": 100,
        "atk": 14,
        "speed": 9,
        "skill_name": "자이온 스파크",
        "desc": "전격으로 적을 마비시키며 공격합니다.",
    },
    "자이온맘": {
        "team": "자이온",
        "hp": 120,
        "atk": 11,
        "speed": 7,
        "skill_name": "자애로운 파동",
        "desc": "적의 공격력을 낮추고 체력을 채웁니다.",
    },
    "자이온왕": {
        "team": "자이온",
        "hp": 160,
        "atk": 16,
        "speed": 5,
        "skill_name": "제왕의 진노",
        "desc": "분노를 터트려 연속 공격을 퍼붓습니다.",
    },
}

# 세션 상태 초기화
if "game_state" not in st.session_state:
    st.session_state.game_state = "SELECT"  # SELECT, FIGHT, END
    st.session_state.p1 = None
    st.session_state.p2 = None
    st.session_state.p1_hp = 0
    st.session_state.p2_hp = 0
    st.session_state.log = []

# 캐릭터 선택 화면
if st.session_state.game_state == "SELECT":
  st.subheader("캐릭터를 선택하세요")

  col1, col2 = st.columns(2)

  with col1:
    st.markdown("**🔴 지온 진영**")
    p1_choice = st.selectbox(
        "플레이어 1 선택", ["지온", "지온맘", "지온왕"], key="p1_select"
    )

  with col2:
    st.markdown("**🔵 자이온 진영**")
    p2_choice = st.selectbox(
        "플레이어 2 선택", ["자이온", "자이온맘", "자이온왕"], key="p2_select"
    )

  st.write("")
  if st.button("게임 시작!", type="primary", use_container_width=True):
    st.session_state.p1 = p1_choice
    st.session_state.p2 = p2_choice
    st.session_state.p1_hp = CHARACTERS[p1_choice]["hp"]
    st.session_state.p2_hp = CHARACTERS[p2_choice]["hp"]
    st.session_state.max_p1_hp = CHARACTERS[p1_choice]["hp"]
    st.session_state.max_p2_hp = CHARACTERS[p2_choice]["hp"]
    st.session_state.log = [
        f"게임 시작! {p1_choice} VS {p2_choice}의 대결이 시작됩니다!"
    ]
    st.session_state.game_state = "FIGHT"
    st.rerun()

# 전투 화면
elif st.session_state.game_state == "FIGHT":
  p1 = st.session_state.p1
  p2 = st.session_state.p2

  st.markdown("### ⚔️ 전투 현황")

  c1, c2 = st.columns(2)
  with c1:
    st.markdown(f"**🔴 {p1}** (지온 진영)")
    st.progress(
        max(0, st.session_state.p1_hp / st.session_state.max_p1_hp),
        text=f"HP: {st.session_state.p1_hp}/{st.session_state.max_p1_hp}",
    )
  with c2:
    st.markdown(f"**🔵 {p2}** (자이온 진영)")
    st.progress(
        max(0, st.session_state.p2_hp / st.session_state.max_p2_hp),
        text=f"HP: {st.session_state.p2_hp}/{st.session_state.max_p2_hp}",
    )

  st.divider()

  # 액션 버튼
  col_a, col_b = st.columns(2)
  with col_a:
    attack_btn = st.button(
        "🗡️ 일반 공격", use_container_width=True, type="primary"
    )
  with col_b:
    skill_btn = st.button(
        f"✨ 특수 스킬 ({CHARACTERS[p1]['skill_name']})",
        use_container_width=True,
    )

  if attack_btn or skill_btn:
    # 플레이어 1턴
    p1_data = CHARACTERS[p1]
    p2_data = CHARACTERS[p2]

    if skill_btn:
      # 스킬 사용 로직
      if "맘" in p1:
        heal = 25
        st.session_state.p1_hp = min(
            st.session_state.max_p1_hp, st.session_state.p1_hp + heal
        )
        st.session_state.log.insert(
            0,
            f"✨ {p1}이(가) [{p1_data['skill_name']}] 사용! 체력 {heal} 회복!",
        )
      else:
        damage = int(p1_data["atk"] * 1.8)
        st.session_state.p2_hp -= damage
        st.session_state.log.insert(
            0,
            f"✨ {p1}이(가) [{p1_data['skill_name']}] 적중! {p2}에게 {damage}의"
            " 대피해!",
        )
    else:
      # 일반 공격
      damage = random.randint(
          p1_data["atk"] - 3, p1_data["atk"] + 3
      )
      st.session_state.p2_hp -= damage
      st.session_state.log.insert(
          0, f"🗡️ {p1}의 공격! {p2}에게 {damage}의 피해를 입혔습니다."
      )

    # 승리 체크 (P2 패배)
    if st.session_state.p2_hp <= 0:
      st.session_state.p2_hp = 0
      st.session_state.log.insert(0, f"🏆 승리! {p1}이(가) 승리했습니다!")
      st.session_state.game_state = "END"
      st.rerun()

    # 컴퓨터(플레이어 2) 턴
    time.sleep(0.3)
    p2_action = random.choice(["attack", "skill"])
    if p2_action == "skill":
      if "맘" in p2:
        heal = 25
        st.session_state.p2_hp = min(
            st.session_state.max_p2_hp, st.session_state.p2_hp + heal
        )
        st.session_state.log.insert(
            0,
            f"✨ 상대 {p2}이(가) [{p2_data['skill_name']}] 사용! 체력 {heal}"
            " 회복!",
        )
      else:
        damage = int(p2_data["atk"] * 1.8)
        st.session_state.p1_hp -= damage
        st.session_state.log.insert(
            0,
            f"✨ 상대 {p2}이(가) [{p2_data['skill_name']}] 적중! {p1}에게"
            f" {damage}의 대피해!",
        )
    else:
      damage = random.randint(
          p2_data["atk"] - 3, p2_data["atk"] + 3
      )
      st.session_state.p1_hp -= damage
      st.session_state.log.insert(
          0, f"🗡️ 상대 {p2}의 반격! {p1}에게 {damage}의 피해를 입혔습니다."
      )

    # 승리 체크 (P1 패배)
    if st.session_state.p1_hp <= 0:
      st.session_state.p1_hp = 0
      st.session_state.log.insert(0, f"💀 패배... {p2}이(가) 승리했습니다!")
      st.session_state.game_state = "END"

    st.rerun()

  # 전투 로그 출력
  st.markdown("### 📜 전투 기록")
  for log in st.session_state.log[:5]:  # 최근 5개만 표시
    st.text(log)

# 게임 종료 화면
elif st.session_state.game_state == "END":
  st.subheader("🎉 게임 종료")
  for log in st.session_state.log[:2]:
    st.info(log)

  if st.button("다시 하기", use_container_width=True):
    st.session_state.game_state = "SELECT"
    st.rerun()
