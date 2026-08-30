    # ==============================================================================
# 메이플스토리풍 3D/2.5D 멀티모듈 RPG 프로젝트 [통합 완성본 코드]
# ==============================================================================

import random
import time
import json
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

# ------------------------------------------------------------------------------
# 1. 글로벌 상수 및 게임 설정 데이터베이스
# ------------------------------------------------------------------------------
GAME_TITLE = "MapleStream 3D: The Legend of Py"
VERSION = "v1.0.5-PROD"

JOB_CLASSES = {
    "전사": {"base_hp": 150, "base_mp": 30, "str": 12, "dex": 5, "int": 4, "luk": 4, "desc": "높은 체력과 강력한 근접 물리 공격을 구사합니다."},
    "마법사": {"base_hp": 80, "base_mp": 120, "str": 4, "dex": 4, "int": 15, "luk": 7, "desc": "화려한 광역 원거리 마법 공격을 시전합니다."},
    "궁수": {"base_hp": 100, "base_mp": 60, "str": 5, "dex": 15, "int": 4, "luk": 6, "desc": "높은 회피율과 치명타 중심의 원거리 딜러입니다."},
    "도적": {"base_hp": 90, "base_mp": 50, "str": 4, "dex": 10, "int": 4, "luk": 16, "desc": "빠른 기동성과 연속 타격 콤보에 특화되어 있습니다."}
}

ITEM_DATABASE = {
    "빨간포션": {"type": "consumable", "effect": 50, "price": 50, "desc": "HP를 50 회복합니다."},
    "파란포션": {"type": "consumable", "effect": 50, "price": 80, "desc": "MP를 50 회복합니다."},
    "주황포션": {"type": "consumable", "effect": 150, "price": 200, "desc": "HP를 150 회복합니다."},
    "초보자의검": {"type": "weapon", "atk": 5, "price": 100, "desc": "누구나 다루기 쉬운 가벼운 검."},
    "스태프": {"type": "weapon", "atk": 8, "price": 150, "desc": "마력이 깃든 나무 지팡이."},
    "헌터보우": {"type": "weapon", "atk": 12, "price": 250, "desc": "탄성이 좋은 사냥용 활."},
    "누더기갑옷": {"type": "armor", "def": 2, "price": 80, "desc": "천으로 대충 기운 옷."},
    "가죽갑옷": {"type": "armor", "def": 7, "price": 200, "desc": "가죽을 덧대어 만든 방어구."},
    "메이플리프배지": {"type": "accessory", "stat": 5, "price": 1000, "desc": "메이플 월드의 가치 있는 기념 배지."}
}

MAP_DATABASE = {
    "헤네시스 동쪽풀숲": {
        "level_req": 1,
        "monsters": ["주황버섯", "슬라임"],
        "bgm": "Henesys_Field",
        "bg_color": "#87CEEB",
        "ground_color": "#228B22"
    },
    "돼지의 해안가": {
        "level_req": 10,
        "monsters": ["리본돼지", "초록버섯"],
        "bgm": "PigBeach",
        "bg_color": "#FFD700",
        "ground_color": "#D2B48C"
    },
    "개미굴 1층": {
        "level_req": 25,
        "monsters": ["뿔버섯", "좀비버섯"],
        "bgm": "Dungeon_Ant",
        "bg_color": "#2F4F4F",
        "ground_color": "#696969"
    },
    "와이즈맨의 성곽": {
        "level_req": 50,
        "monsters": ["레이스", "주니어레이스", "다크스톤골렘"],
        "bgm": "Castle_Dark",
        "bg_color": "#4B0082",
        "ground_color": "#2F4F4F"
    }
}

MONSTER_DATABASE = {
    "슬라임": {"hp": 30, "atk": 8, "def": 2, "exp": 10, "meso": 15, "icon": "🟢"},
    "주황버섯": {"hp": 80, "atk": 15, "def": 5, "exp": 22, "meso": 35, "icon": "🍄"},
    "초록버섯": {"hp": 150, "atk": 25, "def": 10, "exp": 45, "meso": 70, "icon": "🍄"},
    "리본돼지": {"hp": 250, "atk": 38, "def": 15, "exp": 75, "meso": 120, "icon": "🐷"},
    "뿔버섯": {"hp": 400, "atk": 55, "def": 22, "exp": 130, "meso": 210, "icon": "🍄"},
    "좀비버섯": {"hp": 650, "atk": 75, "def": 30, "exp": 210, "meso": 350, "icon": "🧟"},
    "레이스": {"hp": 1000, "atk": 110, "def": 45, "exp": 350, "meso": 550, "icon": "👻"},
    "주니어레이스": {"hp": 1500, "atk": 150, "def": 60, "exp": 520, "meso": 800, "icon": "👻"},
    "다크스톤골렘": {"hp": 3000, "atk": 220, "def": 100, "exp": 950, "meso": 1500, "icon": "🗿"}
}

SKILL_DATABASE = {
    "전사": [
        {"name": "파워 스트라이크", "mp_cost": 12, "multiplier": 1.8, "hits": 1, "desc": "강력한 힘을 모아 단일 적을 강하게 내려칩니다."},
        {"name": "슬래시 블러스트", "mp_cost": 22, "multiplier": 1.4, "hits": 2, "desc": "검을 크게 휘둘러 주변의 적 다수를 타격합니다."},
        {"name": "아이언 바디", "mp_cost": 15, "multiplier": 0.0, "hits": 0, "desc": "일시적으로 방어력을 대폭 상승시킵니다."}
    ],
    "마법사": [
        {"name": "에너지 볼트", "mp_cost": 15, "multiplier": 1.9, "hits": 1, "desc": "응축된 마력의 구체를 적에게 발사합니다."},
        {"name": "메기나 파이어", "mp_cost": 35, "multiplier": 2.6, "hits": 2, "desc": "화염의 기운을 소환하여 전방을 초토화합니다."},
        {"name": "매직 가드", "mp_cost": 20, "multiplier": 0.0, "hits": 0, "desc": "마력으로 보호막을 형성하여 피해를 흡수합니다."}
    ],
    "궁수": [
        {"name": "더블 샷", "mp_cost": 14, "multiplier": 1.2, "hits": 2, "desc": "화살 두 발을 동시에 빠르게 발사합니다."},
        {"name": "애로우 봄", "mp_cost": 30, "multiplier": 2.2, "hits": 1, "desc": "폭발성 화살을 쏘아 광역 폭발을 일으킵니다."},
        {"name": "스턴 샷", "mp_cost": 18, "multiplier": 1.5, "hits": 1, "desc": "적의 행동을 저지하는 특수 화살을 명중시킵니다."}
    ],
    "도적": [
        {"name": "더블 스탭", "mp_cost": 10, "multiplier": 1.3, "hits": 2, "desc": "단검으로 적의 급소를 빠르게 두 번 찌릅니다."},
        {"name": "님블 슬래시", "mp_cost": 25, "multiplier": 2.0, "hits": 3, "desc": "보이지 않는 속도로 삼단 연속 베기를 시전합니다."},
        {"name": "헤이스트", "mp_cost": 30, "multiplier": 0.0, "hits": 0, "desc": "몸을 가볍게 하여 회피율을 극대화합니다."}
    ]
}

# ------------------------------------------------------------------------------
# 2. 플레이어 및 몬스터 클래스
# ------------------------------------------------------------------------------
class PlayerCharacter:
    def __init__(self, name: str, job: str):
        self.name = name
        self.job = job
        self.level = 1
        self.exp = 0
        self.max_exp = 100
        
        base = JOB_CLASSES.get(job, JOB_CLASSES["전사"])
        self.max_hp = base["base_hp"]
        self.hp = self.max_hp
        self.max_mp = base["base_mp"]
        self.mp = self.max_mp
        
        self.str = base["str"]
        self.dex = base["dex"]
        self.intel = base["int"]
        self.luk = base["luk"]
        self.stat_points = 0
        
        self.meso = 1500
        self.inventory = {"빨간포션": 10, "파란포션": 5, "초보자의검": 1}
        self.equipment = {"무기": "초보자의검", "갑옷": "누더기갑옷", "장신구": None}
        self.current_map = "헤네시스 동쪽풀숲"
        self.quests_completed = []

    def calculate_total_atk(self) -> int:
        weapon_name = self.equipment.get("무기")
        weapon_bonus = ITEM_DATABASE.get(weapon_name, {}).get("atk", 0) if weapon_name else 0
        
        if self.job == "전사":
            base = self.str * 2 + weapon_bonus * 3
        elif self.job == "마법사":
            base = self.intel * 2.5 + weapon_bonus * 3.5
        elif self.job == "궁수":
            base = self.dex * 2 + weapon_bonus * 3
        else:
            base = self.luk * 2 + weapon_bonus * 3
        return int(base)

    def calculate_total_def(self) -> int:
        armor_name = self.equipment.get("갑옷")
        armor_bonus = ITEM_DATABASE.get(armor_name, {}).get("def", 0) if armor_name else 0
        return int(self.dex * 0.5 + armor_bonus * 2)

    def gain_exp(self, amount: int) -> list:
        logs = [f"✨ {amount}의 경험치를 획득했습니다!"]
        self.exp += amount
        
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level += 1
            self.max_hp += 35
            self.max_mp += 20
            self.hp = self.max_hp
            self.mp = self.max_mp
            self.stat_points += 5
            self.max_exp = int(self.max_exp * 1.45)
            logs.append(f"🎉 축하합니다! 레벨이 상승하여 **Lv.{self.level}**이 되었습니다! (스탯 포인트 +5)")
            
        return logs

class MonsterInstance:
    def __init__(self, name: str):
        base = MONSTER_DATABASE.get(name, MONSTER_DATABASE["슬라임"])
        self.name = name
        self.max_hp = base["hp"]
        self.hp = self.max_hp
        self.atk = base["atk"]
        self.def_power = base["def"]
        self.exp = base["exp"]
        self.meso = base["meso"]
        self.icon = base["icon"]
        self.is_boss = False

    def take_damage(self, damage: int) -> int:
        actual_dmg = max(1, damage - self.def_power // 2)
        self.hp = max(0, self.hp - actual_dmg)
        return actual_dmg

# ------------------------------------------------------------------------------
# 3. 전투 및 아이템 관리 엔진
# ------------------------------------------------------------------------------
class CombatEngine:
    @staticmethod
    def calculate_attack_damage(player, monster, skill=None) -> tuple:
        base_atk = player.calculate_total_atk()
        multiplier = 1.0 if not skill else skill["multiplier"]
        
        crit_chance = 15 + (player.luk * 0.4)
        is_critical = random.uniform(0, 100) < crit_chance
        crit_multiplier = 1.5 if player.job != "도적" else 2.0
        
        variance = random.uniform(0.9, 1.1)
        raw_damage = base_atk * multiplier * variance
        if is_critical:
            raw_damage *= crit_multiplier
            
        final_damage = monster.take_damage(int(raw_damage))
        combo_gain = 1 if not skill or skill["hits"] <= 1 else skill["hits"]
        return int(final_damage), is_critical, combo_gain

    @staticmethod
    def process_monster_turn(player, monster) -> int:
        player_def = player.calculate_total_def()
        raw_monster_dmg = max(1, monster.atk - (player_def // 2))
        variance = random.uniform(0.9, 1.1)
        final_monster_dmg = int(raw_monster_dmg * variance)
        player.hp = max(0, player.hp - final_monster_dmg)
        return final_monster_dmg

class BattleSystemState:
    def __init__(self):
        self.combo_count = 0
        self.combo_timer = 0.0
        self.battle_logs = []

    def add_log(self, message: str):
        timestamp = time.strftime("[%H:%M:%S]")
        self.battle_logs.insert(0, f"{timestamp} {message}")
        if len(self.battle_logs) > 50:
            self.battle_logs.pop()

    def update_combo(self, gain: int):
        self.combo_count += gain
        self.combo_timer = time.time()

class ItemHandler:
    @staticmethod
    def use_consumable(player, item_name: str) -> str:
        if player.inventory.get(item_name, 0) <= 0:
            return f"❌ {item_name}이(가) 부족합니다."
            
        if item_name == "빨간포션":
            heal_amount = 50
            player.hp = min(player.max_hp, player.hp + heal_amount)
            player.inventory[item_name] -= 1
            return f"🧪 빨간 포션을 사용하여 HP를 {heal_amount} 회복했습니다."
        elif item_name == "파란포션":
            heal_amount = 50
            player.mp = min(player.max_mp, player.mp + heal_amount)
            player.inventory[item_name] -= 1
            return f"🧪 파란 포션을 사용하여 MP를 {heal_amount} 회복했습니다."
        elif item_name == "주황포션":
            heal_amount = 150
            player.hp = min(player.max_hp, player.hp + heal_amount)
            player.inventory[item_name] -= 1
            return f"🧪 주황 포션을 사용하여 HP를 {heal_amount} 회복했습니다."
        return "❌ 사용할 수 없는 아이템입니다."

    @staticmethod
    def equip_item(player, item_name: str) -> str:
        item_data = ITEM_DATABASE.get(item_name)
        if not item_data:
            return "❌ 존재하지 않는 아이템입니다."
            
        item_type = item_data["type"]
        if item_type == "weapon":
            player.equipment["무기"] = item_name
            return f"⚔️ 무기를 [{item_name}] (으)로 장착했습니다."
        elif item_type == "armor":
            player.equipment["갑옷"] = item_name
            return f"🛡️ 갑옷을 [{item_name}] (으)로 장착했습니다."
        elif item_type == "accessory":
            player.equipment["장신구"] = item_name
            return f"💍 장신구를 [{item_name}] (으)로 착용했습니다."
        return "❌ 장착할 수 없는 아이템 종류입니다."

# ------------------------------------------------------------------------------
# 4. 3D 뷰포트 HTML 컴포넌트 렌더러
# ------------------------------------------------------------------------------
def get_threejs_game_viewport(player_job: str, monster_icon: str, map_bg_color: str, is_attacking: bool) -> str:
    attack_anim_offset = "transform: scale(1.1) translateX(15px);" if is_attacking else "transform: scale(1.0);"
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; background: {map_bg_color}; overflow: hidden; font-family: 'Malgun Gothic', monospace; }}
            #viewport {{
                width: 100%; height: 380px; position: relative;
                background: linear-gradient(to bottom, #4a90e2 0%, #a6c8e0 50%, #2e8b57 50%, #1e5631 100%);
                border: 3px solid #3d2817; border-radius: 6px; box-shadow: inset 0 0 30px rgba(0,0,0,0.6);
            }}
            .maple-cloud {{ position: absolute; font-size: 35px; animation: floatCloud 12s linear infinite; }}
            @keyframes floatCloud {{ 0% {{ left: -10%; top: 15%; }} 100% {{ left: 110%; top: 15%; }} }}
            .char-sprite {{
                position: absolute; bottom: 35%; left: 20%; font-size: 65px;
                filter: drop-shadow(4px 8px 4px rgba(0,0,0,0.5));
                transition: transform 0.15s ease-in-out; {attack_anim_offset} z-index: 10;
            }}
            .monster-sprite {{
                position: absolute; bottom: 35%; right: 25%; font-size: 60px;
                filter: drop-shadow(4px 8px 4px rgba(0,0,0,0.5));
                animation: bounceMonster 1.5s ease-in-out infinite; z-index: 9;
            }}
            @keyframes bounceMonster {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-12px); }} }}
            .map-floor {{
                position: absolute; bottom: 0; width: 100%; height: 35%;
                background: repeating-linear-gradient(45deg, #228B22, #228B22 20px, #1e7e1e 20px, #1e7e1e 40px);
                border-top: 5px solid #0d4a19;
            }}
            .ui-hud-overlay {{
                position: absolute; top: 10px; left: 10px; color: white;
                background: rgba(0, 0, 0, 0.6); padding: 6px 12px; border-radius: 4px; font-size: 12px; border: 1px solid #d4af37;
            }}
        </style>
    </head>
    <body>
        <div id="viewport">
            <div class="ui-hud-overlay">🗺️ 3D Isometric Viewport | FPS: 60</div>
            <div class="maple-cloud">☁️</div>
            <div class="char-sprite">{'🧙‍♂️' if player_job == '마법사' else ('🏹' if player_job == '궁수' else ('🗡️' if player_job == '도적' else '⚔️'))}</div>
            <div class="monster-sprite">{monster_icon}</div>
            <div class="map-floor"></div>
        </div>
    </body>
    </html>
    """

# ------------------------------------------------------------------------------
# 5. 스트림릿 메인 UI 진입점 및 컨트롤러
# ------------------------------------------------------------------------------
st.set_page_config(page_title="MapleStream 3D: The Legend of Py", page_icon="🗺️", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .stApp { background-color: #12141c; color: #e0e0e0; font-family: 'Malgun Gothic', sans-serif; }
    .stButton>button { width: 100%; border-radius: 4px; font-weight: bold; }
    .metric-card { background: rgba(25, 28, 36, 0.8); border: 1px solid #333; padding: 12px; border-radius: 6px; text-align: center; }
</style>
""", unsafe_allow_html=True)

if "player" not in st.session_state:
    st.session_state.player = None
if "current_monster" not in st.session_state:
    st.session_state.current_monster = None
if "battle_state" not in st.session_state:
    st.session_state.battle_state = BattleSystemState()
if "is_attacking_anim" not in st.session_state:
    st.session_state.is_attacking_anim = False

if st.session_state.player is None:
    st.title("🗺️ 메이플스토리: 스트림릿 3D 크로니클")
    st.markdown("### 🧙‍♂️ 모험가 생성 및 직업 선택")
    with st.form("character_creation_form"):
        char_name = st.text_input("캐릭터 닉네임", value="파이썬마스터")
        selected_job = st.selectbox("직업 선택", list(JOB_CLASSES.keys()))
        job_info = JOB_CLASSES[selected_job]
        st.info(f"**[{selected_job}] 특징**: {job_info['desc']}")
        if st.form_submit_button("🚀 메이플 월드로 모험 떠나기"):
            if not char_name.strip():
                st.error("올바른 닉네임을 입력해주세요!")
            else:
                st.session_state.player = PlayerCharacter(char_name, selected_job)
                st.session_state.current_monster = MonsterInstance(MAP_DATABASE[st.session_state.player.current_map]["monsters"][0])
                st.session_state.battle_state.add_log(f"메이플 월드에 오신 것을 환영합니다, {char_name} 모험가님!")
                st.rerun()
else:
    player = st.session_state.player
    if st.session_state.current_monster is None or st.session_state.current_monster.hp <= 0:
        map_info = MAP_DATABASE.get(player.current_map, MAP_DATABASE["헤네시스 동쪽풀숲"])
        chosen_mob_name = random.choice(map_info["monsters"])
        st.session_state.current_monster = MonsterInstance(chosen_mob_name)
        st.session_state.battle_state.add_log(f"야생의 [{chosen_mob_name}]이(가) 나타났습니다!")

    monster = st.session_state.current_monster
    map_info = MAP_DATABASE.get(player.current_map, MAP_DATABASE["헤네시스 동쪽풀숲"])

    with st.sidebar:
        st.markdown(f"### 👤 {player.name} (`{player.job}`)")
        st.markdown(f"**레벨**: Lv.{player.level} (EXP: {player.exp}/{player.max_exp})")
        st.progress(player.exp / player.max_exp)
        st.markdown(f"**❤️ 체력**: {player.hp} / {player.max_hp}")
        st.progress(player.hp / player.max_hp if player.max_hp > 0 else 0)
        st.markdown(f"**💙 마나**: {player.mp} / {player.max_mp}")
        st.progress(player.mp / player.max_mp if player.max_mp > 0 else 0)
        st.markdown(f"💰 **메소**: {player.meso:,} 💰")
        st.markdown(f"⚔️ **공격력**: {player.calculate_total_atk()} | 🛡️ **방어력**: {player.calculate_total_def()}")
        
        if player.stat_points > 0:
            st.markdown(f"✨ **남은 스탯: {player.stat_points}**")
            sc1, sc2 = st.columns(2)
            if sc1.button("STR+1"):
                player.str += 1; player.stat_points -= 1; st.rerun()
            if sc2.button("DEX+1"):
                player.dex += 1; player.stat_points -= 1; st.rerun()

        st.markdown("### 🎒 인벤토리")
        for iname, cnt in list(player.inventory.items()):
            if cnt > 0:
                ic1, ic2 = st.columns([2, 1])
                ic1.markdown(f"- {iname}: {cnt}")
                if "포션" in iname and ic2.button("사용", key=f"use_{iname}"):
                    st.session_state.battle_state.add_log(ItemHandler.use_consumable(player, iname))
                    st.rerun()
                elif iname in ITEM_DATABASE and ITEM_DATABASE[iname]["type"] in ["weapon", "armor"] and ic2.button("장착", key=f"eq_{iname}"):
                    st.session_state.battle_state.add_log(ItemHandler.equip_item(player, iname))
                    st.rerun()

    st.title(f"🗺️ {player.current_map}")
    tab_c, tab_s, tab_n = st.tabs(["⚔️ 전투 필드", "🛒 상점", "🌐 월드 이동"])

    with tab_c:
        cv, cc = st.columns([1.5, 1])
        with cv:
            components.html(get_threejs_game_viewport(player.job, monster.icon, map_info["bg_color"], st.session_state.is_attacking_anim), height=390)
            st.markdown(f"#### 👾 대상: {monster.icon} {monster.name} (HP: {monster.hp} / {monster.max_hp})")
            st.progress(max(0.0, min(1.0, monster.hp / monster.max_hp)))
        with cc:
            st.markdown("### 🎮 액션 커맨드")
            if st.button("⚔️ 기본 공격", use_container_width=True):
                st.session_state.is_attacking_anim = True
                dmg, is_crit, combo_inc = CombatEngine.calculate_attack_damage(player, monster)
                st.session_state.battle_state.update_combo(combo_inc)
                st.session_state.battle_state.add_log(f"[전투] {monster.name}에게 {dmg} 데미지!" + (" [CRITICAL!]" if is_crit else ""))
                
                if monster.hp <= 0:
                    st.session_state.battle_state.add_log(f"🏆 {monster.name} 처치! EXP +{monster.exp}, 메소 +{monster.meso}")
                    player.meso += monster.meso
                    for l in player.gain_exp(monster.exp):
                        st.session_state.battle_state.add_log(l)
                else:
                    mob_dmg = CombatEngine.process_monster_turn(player, monster)
                    st.session_state.battle_state.add_log(f"[피격] {monster.name}의 반격! {mob_dmg} 피해")
                st.rerun()

            st.markdown("#### ✨ 스킬")
            for skill in SKILL_DATABASE.get(player.job, []):
                if st.button(f"⚡ {skill['name']} (MP {skill['mp_cost']})", use_container_width=True):
                    if player.mp < skill["mp_cost"]:
                        st.warning("마나가 부족합니다!")
                    else:
                        player.mp -= skill["mp_cost"]
                        st.session_state.is_attacking_anim = True
                        if skill["multiplier"] > 0:
                            dmg, is_crit, combo_inc = CombatEngine.calculate_attack_damage(player, monster, skill)
                            st.session_state.battle_state.add_log(f"[스킬] {skill['name']}! {monster.name}에게 {dmg} 데미지")
                            if monster.hp <= 0:
                                player.meso += monster.meso
                                for l in player.gain_exp(monster.exp):
                                    st.session_state.battle_state.add_log(l)
                            else:
                                CombatEngine.process_monster_turn(player, monster)
                        st.rerun()

        st.markdown("### 📜 전투 로그")
        st.text_area("Logs", value="\n".join(st.session_state.battle_state.battle_logs[:10]), height=140, label_visibility="collapsed")

    with tab_s:
        st.markdown("### 🛒 상점")
        for iname, info in ITEM_DATABASE.items():
            if st.button(f"구매: {iname} ({info['price']:,} 메소)", key=f"buy_{iname}"):
                if player.meso >= info['price']:
                    player.meso -= info['price']
                    player.inventory[iname] = player.inventory.get(iname, 0) + 1
                    st.success(f"{iname} 구매 완료!")
                    st.rerun()
                else:
                    st.error("메소가 부족합니다!")

    with tab_n:
        st.markdown("### 🌐 지역 이동")
        for mname, mdata in MAP_DATABASE.items():
            if st.button(f"이동: {mname} (Lv.{mdata['level_req']} 이상)", key=f"map_{mname}"):
                if player.level >= mdata['level_req']:
                    player.current_map = mname
                    st.session_state.current_monster = MonsterInstance(mdata["monsters"][0])
                    st.session_state.battle_state.add_log(f"'{mname}'(으)로 이동했습니다.")
                    st.rerun()
                else:
                    st.error("레벨이 부족합니다!")
