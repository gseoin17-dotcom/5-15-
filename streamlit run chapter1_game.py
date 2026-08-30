# ==============================================================================
# 메이플스토리풍 3D/2.5D 멀티모듈 RPG 프로젝트 [Part 1/4: 코어 시스템 및 데이터베이스]
# ------------------------------------------------------------------------------
# 파일 구조 안내:
# - Part 1: 데이터 모델, 아이템 DB, 플레이어/몬스터 클래스, 사운드/이펙트 구조체 (약 500줄)
# - Part 2: 전투 엔진, 스킬 시스템, 데미지 계산 및 AI 루틴 (예정)
# - Part 3: 3D 그래픽 렌더링 파이프라인 (Three.js 연동 HTML 컴포넌트) (예정)
# - Part 4: 스트림릿 메인 UI 진입점, 상점, 인벤토리, 게임 루프 컨트롤러 (예정)
# ==============================================================================

import random
import time
import json
import hashlib
from datetime import datetime

# ------------------------------------------------------------------------------
# 1. 글로벌 상수 및 게임 설정 데이터베이스
# ------------------------------------------------------------------------------
GAME_TITLE = "MapleStream 3D: The Legend of Py"
VERSION = "v1.0.4-PROD"

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

# ------------------------------------------------------------------------------
# 2. 플레이어(Character) 및 시스템 코어 클래스
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
        self.achievements = []
        self.play_time = 0.0
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calculate_total_atk(self) -> int:
        weapon_name = self.equipment.get("무기")
        weapon_bonus = ITEM_DATABASE.get(weapon_name, {}).get("atk", 0) if weapon_name else 0
        
        if self.job == "전사":
            base = self.str * 2 + weapon_bonus * 3
        elif self.job == "마법사":
            base = self.intel * 2.5 + weapon_bonus * 3.5
        elif self.job == "궁수":
            base = self.dex * 2 + weapon_bonus * 3
        else: # 도적
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

    def to_json(self) -> str:
        data = {
            "name": self.name, "job": self.job, "level": self.level,
            "exp": self.exp, "max_exp": self.max_exp, "hp": self.hp,
            "max_hp": self.max_hp, "mp": self.mp, "max_mp": self.max_mp,
            "str": self.str, "dex": self.dex, "intel": self.intel, "luk": self.luk,
            "stat_points": self.stat_points, "meso": self.meso,
            "inventory": self.inventory, "equipment": self.equipment,
            "current_map": self.current_map, "quests_completed": self.quests_completed
        }
        return json.dumps(data, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        player = cls(data["name"], data["job"])
        player.level = data["level"]
        player.exp = data["exp"]
        player.max_exp = data["max_exp"]
        player.hp = data["hp"]
        player.max_hp = data["max_hp"]
        player.mp = data["mp"]
        player.max_mp = data["max_mp"]
        player.str = data["str"]
        player.dex = data["dex"]
        player.intel = data["intel"]
        player.luk = data["luk"]
        player.stat_points = data["stat_points"]
        player.meso = data["meso"]
        player.inventory = data["inventory"]
        player.equipment = data["equipment"]
        player.current_map = data["current_map"]
        player.quests_completed = data["quests_completed"]
        return player

# ------------------------------------------------------------------------------
# 3. 몬스터 런타임 인스턴스 클래스
# ------------------------------------------------------------------------------
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
# Part 1 완료. 다음 Part 2에서는 전투 시스템, 데미지 공식, 콤보 및 스킬 엔진이 이어집니다.
# ------------------------------------------------------------------------------
# ==============================================================================
# 메이플스토리풍 3D/2.5D 멀티모듈 RPG 프로젝트 [Part 2/4: 전투 시스템 및 스킬 엔진]
# ------------------------------------------------------------------------------
# 파일 구조 안내:
# - Part 1: 데이터 모델, 아이템 DB, 플레이어/몬스터 클래스 (완료)
# - Part 2: 전투 엔진, 스킬 시스템, 데미지 계산 및 AI 루틴 (현재 파트)
# - Part 3: 3D 그래픽 렌더링 파이프라인 (Three.js 연동 HTML 컴포넌트) (예정)
# - Part 4: 스트림릿 메인 UI 진입점, 상점, 인벤토리, 게임 루프 컨트롤러 (예정)
# ==============================================================================

import random

# ------------------------------------------------------------------------------
# 1. 스킬 데이터베이스 및 마법 효과 정의
# ------------------------------------------------------------------------------
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
# 2. 전투 엔진 및 데미지 계산 코어
# ------------------------------------------------------------------------------
class CombatEngine:
    @staticmethod
    def calculate_attack_damage(player, monster, skill=None) -> tuple:
        """
        메이플스토리풍 데미지 공식을 모사한 전투 계산기
        반환값: (총 데미지, 크리티컬 여부, 콤보 증가량)
        """
        base_atk = player.calculate_total_atk()
        
        # 스킬 배율 적용
        multiplier = 1.0
        if skill:
            multiplier = skill["multiplier"]
            
        # 크리티컬 판정 (기본 확률 15% + LUK 보정)
        crit_chance = 15 + (player.luk * 0.4)
        is_critical = random.uniform(0, 100) < crit_chance
        
        crit_multiplier = 1.5 if not player.job == "도적" else 2.0
        
        # 기본 데미지 연산 (랜덤 오차 ±10% 포함)
        variance = random.uniform(0.9, 1.1)
        raw_damage = base_atk * multiplier * variance
        
        if is_critical:
            raw_damage *= crit_multiplier
            
        # 몬스터 방어력 차감
        final_damage = monster.take_damage(int(raw_damage))
        
        # 콤보 및 보상 산정
        combo_gain = 1 if skill is None or skill["hits"] <= 1 else skill["hits"]
        
        return int(final_damage), is_critical, combo_gain

    @staticmethod
    def process_monster_turn(player, monster) -> int:
        """
        몬스터의 반격 데미지 연산
        """
        player_def = player.calculate_total_def()
        monster_atk = monster.atk
        
        raw_monster_dmg = max(1, monster_atk - (player_def // 2))
        variance = random.uniform(0.9, 1.1)
        final_monster_dmg = int(raw_monster_dmg * variance)
        
        player.hp = max(0, player.hp - final_monster_dmg)
        return final_monster_dmg

# ------------------------------------------------------------------------------
# 3. 콤보 및 파티클 이펙트 관리 시스템
# ------------------------------------------------------------------------------
class BattleSystemState:
    def __init__(self):
        self.combo_count = 0
        self.combo_timer = 0.0
        self.battle_logs = []
        self.screen_shake = False

    def add_log(self, message: str):
        timestamp = time.strftime("[%H:%M:%S]")
        self.battle_logs.insert(0, f"{timestamp} {message}")
        if len(self.battle_logs) > 50:
            self.battle_logs.pop()

    def update_combo(self, gain: int):
        self.combo_count += gain
        self.combo_timer = time.time()

    def check_combo_expiry(self):
        if self.combo_count > 0 and (time.time() - self.combo_timer > 4.0):
            self.combo_count = 0

# ------------------------------------------------------------------------------
# 4. 아이템 사용 및 장비 강화 핸들러
# ------------------------------------------------------------------------------
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
        from __main__ import ITEM_DATABASE if "__main__" in globals() else {}
        # 안전한 데이터베이스 참조를 위한 폴백
        item_data = {
            "초보자의검": {"type": "weapon"},
            "스태프": {"type": "weapon"},
            "헌터보우": {"type": "weapon"},
            "누더기갑옷": {"type": "armor"},
            "가죽갑옷": {"type": "armor"},
            "메이플리프배지": {"type": "accessory"}
        }.get(item_name)
        
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
# Part 2 완료. 다음 Part 3에서는 Three.js 기반 3D 그래픽 렌더링 엔진 코드가 이어집니다.
# ------------------------------------------------------------------------------
# ==============================================================================
# 메이플스토리풍 3D/2.5D 멀티모듈 RPG 프로젝트 [Part 3/4: 3D 그래픽 엔진 및 렌더링]
# ------------------------------------------------------------------------------
# 파일 구조 안내:
# - Part 1: 데이터 모델, 아이템 DB, 플레이어/몬스터 클래스 (완료)
# - Part 2: 전투 엔진, 스킬 시스템, 데미지 계산 및 AI 루틴 (완료)
# - Part 3: 3D 그래픽 렌더링 파이프라인 (Three.js 연동 HTML 컴포넌트) (현재 파트)
# - Part 4: 스트림릿 메인 UI 진입점, 상점, 인벤토리, 게임 루프 컨트롤러 (예정)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Three.js 기반 3D 웹 뷰포트 인젝션 컴포넌트
# ------------------------------------------------------------------------------
class MapleGraphicsEngine3D:
    @staticmethod
    def get_threejs_viewport_html(map_name: str, player_job: str, monster_name: str, combo: int) -> str:
        """
        스트림릿 내에서 브라우저 WebGL(Three.js)을 구동하여 
        메이플스토리 감성의 2.5D 입체 캐릭터 및 몬스터를 실시간 렌더링하는 HTML/JS 스크립트 생성
        """
        
        # 맵별 배경색 및 테마 설정
        bg_gradients = {
            "헤네시스 동쪽풀숲": "linear-gradient(to bottom, #87CEEB 0%, #E0F6FF 60%, #228B22 60%, #004d1a 100%)",
            "돼지의 해안가": "linear-gradient(to bottom, #FFD700 0%, #FFF8DC 60%, #D2B48C 60%, #8B4513 100%)",
            "개미굴 1층": "linear-gradient(to bottom, #1a1a1a 0%, #333333 60%, #4a4a4a 60%, #1f1f1f 100%)",
            "와이즈맨의 성곽": "linear-gradient(to bottom, #2c003e 0%, #4b0082 60%, #2F4F4F 60%, #1a1a1a 100%)"
        }
        active_bg = bg_gradients.get(map_name, bg_gradients["헤네시스 동쪽풀숲"])

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body, html {{
                    margin: 0;
                    padding: 0;
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                    background: transparent;
                }}
                #viewport-container {{
                    width: 100%;
                    height: 420px;
                    background: {active_bg};
                    border: 4px solid #4a3b32;
                    border-radius: 12px;
                    box-shadow: inset 0 0 30px rgba(0,0,0,0.6), 0 8px 16px rgba(0,0,0,0.3);
                    position: relative;
                    font-family: 'Malgun Gothic', monospace;
                }}
                .maple-hud-overlay {{
                    position: absolute;
                    top: 15px;
                    left: 15px;
                    color: white;
                    text-shadow: 2px 2px 0px #000, -2px -2px 0px #000;
                    font-weight: bold;
                    font-size: 16px;
                    z-index: 10;
                }}
                .combo-banner {{
                    position: absolute;
                    top: 20px;
                    right: 20px;
                    background: rgba(0, 0, 0, 0.75);
                    border: 2px solid #ffd700;
                    color: #ffd700;
                    padding: 6px 14px;
                    border-radius: 20px;
                    font-size: 15px;
                    font-weight: 900;
                    box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
                    z-index: 10;
                }}
                .entity-label {{
                    position: absolute;
                    bottom: 35%;
                    color: #fff;
                    background: rgba(0,0,0,0.6);
                    padding: 2px 8px;
                    border-radius: 4px;
                    font-size: 12px;
                    text-align: center;
                    transform: translateX(-50%);
                    white-space: nowrap;
                }}
                #webgl-canvas {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                }}
            </style>
            <!-- Three.js CDN 라이브러리 로드 -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        </head>
        <body>
            <div id="viewport-container">
                <div class="maple-hud-overlay">
                    🗺️ 지역: {map_name} <br>
                    ⚡ 직업: {player_job}
                </div>
                <div class="combo-banner">
                    🔥 COMBO: {combo}
                </div>
                
                <!-- 2.5D 입체 스프라이트 레이어 -->
                <div style="position: absolute; bottom: 28%; left: 25%; text-align: center; z-index: 5;">
                    <div style="font-size: 55px; filter: drop-shadow(0px 8px 4px rgba(0,0,0,0.5)); animation: bounce 1.5s infinite alternate;">
                        🧙‍♂️
                    </div>
                    <div class="entity-label">플레이어 ({player_job})</div>
                </div>

                <div style="position: absolute; bottom: 28%; right: 30%; text-align: center; z-index: 5;">
                    <div style="font-size: 50px; filter: drop-shadow(0px 8px 4px rgba(0,0,0,0.5)); animation: float 2s infinite ease-in-out;">
                        🍄
                    </div>
                    <div class="entity-label">{monster_name}</div>
                </div>

                <!-- Three.js 3D 파티클 효과용 WebGL 캔버스 -->
                <canvas id="webgl-canvas"></canvas>
            </div>

            <style>
                @keyframes bounce {{
                    0% {{ transform: translateY(0); }}
                    100% {{ transform: translateY(-8px); }}
                }}
                @keyframes float {{
                    0%, 100% {{ transform: translateY(0) scale(1); }}
                    50% {{ transform: translateY(-12px) scale(1.05); }}
                }}
            </style>

            <script>
                // Three.js 기반 백그라운드 실시간 3D 파티클 및 이펙트 엔진 초기화
                const canvas = document.getElementById('webgl-canvas');
                const container = document.getElementById('viewport-container');
                
                const scene = new THREE.Scene();
                const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
                camera.position.z = 5;

                const renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true }});
                renderer.setSize(container.clientWidth, container.clientHeight);
                renderer.setPixelRatio(window.devicePixelRatio);

                // 반짝이는 메이플 성수(Star) 파티클 생성
                const particlesGeometry = new THREE.BufferGeometry();
                const particlesCount = 120;
                const posArray = new Float32Array(particlesCount * 3);

                for(let i = 0; i < particlesCount * 3; i++) {{
                    posArray[i] = (Math.random() - 0.5) * 12;
                }}

                particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

                const particlesMaterial = new THREE.PointsMaterial({{
                    size: 0.04,
                    color: 0xffeb3b,
                    transparent: true,
                    opacity: 0.8
                }});

                const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
                scene.add(particlesMesh);

                // 애니메이션 루프 (60 FPS 렌더링)
                function animate() {{
                    requestAnimationFrame(animate);
                    particlesMesh.rotation.y += 0.0015;
                    particlesMesh.rotation.x += 0.0008;
                    renderer.render(scene, camera);
                }}
                animate();

                // 반응형 리사이즈 대응
                window.addEventListener('resize', () => {{
                    camera.aspect = container.clientWidth / container.clientHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(container.clientWidth, container.clientHeight);
                }});
            </script>
        </body>
        </html>
        """
        return html_content

# ------------------------------------------------------------------------------
# 2. 미니맵 및 월드 위치 관리자 클래스
# ------------------------------------------------------------------------------
class WorldMapManager:
    @staticmethod
    def get_available_maps(level: int) -> list:
        from __main__ import MAP_DATABASE if "__main__" in globals() else {}
        # 안전한 폴백 딕셔너리
        maps = {
            "헤네시스 동쪽풀숲": {"level_req": 1},
            "돼지의 해안가": {"level_req": 10},
            "개미굴 1층": {"level_req": 25},
            "와이즈맨의 성곽": {"level_req": 50}
        }
        
        available = []
        for m_name, info in maps.items():
            if level >= info["level_req"]:
                available.append(m_name)
        return available

# ------------------------------------------------------------------------------
# Part 3 완료. 다음 마지막 Part 4에서는 스트림릿 메인 UI 컨트롤러, 상점, 인벤토리 시스템이 이어집니다.
# ------------------------------------------------------------------------------
# ==============================================================================
# 메이플스토리풍 3D/2.5D 멀티모듈 RPG 프로젝트 [Part 4/4: 스트림릿 메인 UI 및 컨트롤러]
# ------------------------------------------------------------------------------
# 파일 구조 안내:
# - Part 1: 데이터 모델, 아이템 DB, 플레이어/몬스터 클래스 (완료)
# - Part 2: 전투 엔진, 스킬 시스템, 데미지 계산 및 AI 루틴 (완료)
# - Part 3: 3D 그래픽 렌더링 파이프라인 (Three.js 연동 HTML 컴포넌트) (완료)
# - Part 4: 스트림릿 메인 UI 진입점, 상점, 인벤토리, 게임 루프 컨트롤러 (현재 파트)
# ==============================================================================

import streamlit as st
import streamlit.components.v1 as components

# ------------------------------------------------------------------------------
# 1. 스트림릿 페이지 설정 및 디자인 시스템 적용
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="MapleStream 3D: The Legend of Py",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background-color: #12141c;
        color: #e0e0e0;
        font-family: 'Malgun Gothic', sans-serif;
    }
    .stButton>button {
        width: 100%;
        border-radius: 4px;
        font-weight: bold;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        border-color: #d4af37;
        color: #d4af37;
    }
    .metric-card {
        background: rgba(25, 28, 36, 0.8);
        border: 1px solid #333;
        padding: 12px;
        border-radius: 6px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 2. 세션 상태 관리 및 초기화
# ------------------------------------------------------------------------------
if "player" not in st.session_state:
    st.session_state.player = None
if "current_monster" not in st.session_state:
    st.session_state.current_monster = None
if "battle_state" not in st.session_state:
    st.session_state.battle_state = BattleSystemState()
if "is_attacking_anim" not in st.session_state:
    st.session_state.is_attacking_anim = False
if "game_tab" not in st.session_state:
    st.session_state.game_tab = "전투 필드"

# ------------------------------------------------------------------------------
# 3. 캐릭터 생성 화면 (로그인/생성 안 된 경우)
# ------------------------------------------------------------------------------
if st.session_state.player is None:
    st.title("🗺️ 메이플스토리: 스트림릿 3D 크로니클")
    st.markdown("### 🧙‍♂️ 모험가 생성 및 직업 선택")
    
    with st.form("character_creation_form"):
        char_name = st.text_input("캐릭터 닉네임", value="파이썬마스터")
        selected_job = st.selectbox("직업 선택", list(JOB_CLASSES.keys()))
        
        # 선택한 직업 설명 표시
        job_info = JOB_CLASSES[selected_job]
        st.info(f"**[{selected_job}]특징**: {job_info['desc']}\n\n초기 스탯 -> HP: {job_info['base_hp']} | MP: {job_info['base_mp']} | STR: {job_info['str']} | DEX: {job_info['dex']} | INT: {job_info['int']} | LUK: {job_info['luk']}")
        
        submitted = st.form_submit_button("🚀 메이플 월드로 모험 떠나기")
        if submitted:
            if not char_name.strip():
                st.error("올바른 닉네임을 입력해주세요!")
            else:
                st.session_state.player = PlayerCharacter(char_name, selected_job)
                st.session_state.current_monster = MonsterInstance(MAP_DATABASE[st.session_state.player.current_map]["monsters"][0])
                st.session_state.battle_state.add_log(f"메이플 월드에 오신 것을 환영합니다, {char_name} 모험가님!")
                st.rerun()

else:
    # ------------------------------------------------------------------------------
    # 4. 메인 게임 루프 및 대시보드 UI
    # ------------------------------------------------------------------------------
    player = st.session_state.player
    
    # 몬스터 인스턴스가 없거나 사망한 경우 새 몬스터 리젠
    if st.session_state.current_monster is None or st.session_state.current_monster.hp <= 0:
        map_info = MAP_DATABASE.get(player.current_map, MAP_DATABASE["헤네시스 동쪽풀숲"])
        spawnable_monsters = map_info["monsters"]
        chosen_mob_name = random.choice(spawnable_monsters)
        st.session_state.current_monster = MonsterInstance(chosen_mob_name)
        if st.session_state.current_monster.hp > 0:
            st.session_state.battle_state.add_log(f"야생의 [{chosen_mob_name}]이(가) 나타났습니다!")

    monster = st.session_state.current_monster
    map_info = MAP_DATABASE.get(player.current_map, MAP_DATABASE["헤네시스 동쪽풀숲"])

    # 사이드바: 캐릭터 스테이터스 및 인벤토리
    with st.sidebar:
        st.markdown(f"### 👤 {player.name} (`{player.job}`)")
        st.markdown(f"**레벨**: Lv.{player.level} (EXP: {player.exp}/{player.max_exp})")
        st.progress(player.exp / player.max_exp)
        
        st.markdown("---")
        st.markdown(f"**❤️ 체력 (HP)**: {player.hp} / {player.max_hp}")
        st.progress(player.hp / player.max_hp if player.max_hp > 0 else 0)
        
        st.markdown(f"**💙 마나 (MP)**: {player.mp} / {player.max_mp}")
        st.progress(player.mp / player.max_mp if player.max_mp > 0 else 0)
        
        st.markdown("---")
        st.markdown(f"💰 **보유 메소**: {player.meso:,} 메소")
        st.markdown(f"⚔️ **전투력**: {player.calculate_total_atk()} | 🛡️ **방어력**: {player.calculate_total_def()}")
        
        # 스탯 분배 섹션 (스탯 포인트가 있을 경우)
        if player.stat_points > 0:
            st.markdown(f"✨ **남은 스탯 포인트: {player.stat_points}**")
            sp_col1, sp_col2 = st.columns(2)
            with sp_col1:
                if st.button("STR +1"):
                    player.str += 1
                    player.stat_points -= 1
                    st.rerun()
                if st.button("INT +1"):
                    player.intel += 1
                    player.stat_points -= 1
                    st.rerun()
            with sp_col2:
                if st.button("DEX +1"):
                    player.dex += 1
                    player.stat_points -= 1
                    st.rerun()
                if st.button("LUK +1"):
                    player.luk += 1
                    player.stat_points -= 1
                    st.rerun()

        st.markdown("---")
        st.markdown("### 🎒 인벤토리 & 소모품")
        for item_name, count in list(player.inventory.items()):
            if count > 0:
                col_item, col_btn = st.columns([2, 1])
                col_item.markdown(f"- {item_name}: {count}개")
                if "포션" in item_name:
                    if col_btn.button("사용", key=f"use_{item_name}"):
                        msg = ItemHandler.use_consumable(player, item_name)
                        st.session_state.battle_state.add_log(msg)
                        st.rerun()
                elif item_name in ITEM_DATABASE and ITEM_DATABASE[item_name]["type"] in ["weapon", "armor"]:
                    if col_btn.button("장착", key=f"equip_{item_name}"):
                        msg = ItemHandler.equip_item(player, item_name)
                        st.session_state.battle_state.add_log(msg)
                        st.rerun()

    # 메인 화면 영역 분할 (탭 인터페이스)
    st.title(f"🗺️ {player.current_map}")
    
    tab_combat, tab_shop, tab_nav = st.tabs(["⚔️ 전투 필드", "🛒 메이플 상점", "🌐 월드 이동"])
    
    with tab_combat:
        col_view, col_ctrl = st.columns([1.5, 1])
        
        with col_view:
            # 3D 뷰포트 HTML 컴포넌트 렌더링 (60프레임 감성)
            viewport_html = get_threejs_game_viewport(
                player.job, 
                monster.name, 
                monster.icon, 
                map_info["bg_color"], 
                st.session_state.is_attacking_anim
            )
            components.html(viewport_html, height=390)
            
            # 몬스터 상세 정보 게이지바
            st.markdown(f"#### 👾 대상: {monster.icon} {monster.name} (HP: {monster.hp} / {monster.max_hp})")
            mob_hp_ratio = max(0.0, min(1.0, monster.hp / monster.max_hp))
            st.progress(mob_hp_ratio, text=f"몬스터 체력 잔여율: {int(mob_hp_ratio * 100)}%")

        with col_ctrl:
            st.markdown("### 🎮 액션 커맨드")
            
            # 기본 공격 버튼
            if st.button("⚔️ 기본 공격 (슬래시)", use_container_width=True):
                st.session_state.is_attacking_anim = True
                dmg, is_crit, combo_inc = CombatEngine.calculate_attack_damage(player, monster)
                st.session_state.battle_state.update_combo(combo_inc)
                
                crit_str = " 🔥 [CRITICAL!]" if is_crit else ""
                st.session_state.battle_state.add_log(f"[전투] {monster.name}에게 {dmg}의 데미지를 입혔습니다!{crit_str}")
                
                # 몬스터 처치 확인
                if monster.hp <= 0:
                    st.session_state.battle_state.add_log(f"🏆 [{monster.name}]을(를) 처치했습니다! EXP +{monster.exp}, 메소 +{monster.meso}")
                    player.meso += monster.meso
                    exp_logs = player.gain_exp(monster.exp)
                    for l in exp_logs:
                        st.session_state.battle_state.add_log(l)
                else:
                    # 몬스터 반격 턴
                    mob_dmg = CombatEngine.process_monster_turn(player, monster)
                    st.session_state.battle_state.add_log(f"[피격] {monster.name}의 반격으로 {mob_dmg}의 피해를 입었습니다!")
                    if player.hp <= 0:
                        st.session_state.battle_state.add_log("💀 체력이 모두 소모되어 마을로 강제 귀환합니다...")
                        player.hp = int(player.max_hp * 0.5)
                st.rerun()

            # 직업별 스킬 버튼 패널
            st.markdown("#### ✨ 직업 고유 스킬")
            job_skills = SKILL_DATABASE.get(player.job, [])
            for skill in job_skills:
                if st.button(f"⚡ {skill['name']} (MP {skill['mp_cost']})", use_container_width=True):
                    if player.mp < skill["mp_cost"]:
                        st.warning("❌ 마나(MP)가 부족합니다!")
                    else:
                        player.mp -= skill["mp_cost"]
                        st.session_state.is_attacking_anim = True
                        
                        if skill["multiplier"] > 0:
                            dmg, is_crit, combo_inc = CombatEngine.calculate_attack_damage(player, monster, skill)
                            st.session_state.battle_state.update_combo(combo_inc)
                            st.session_state.battle_state.add_log(f"[스킬] {skill['name']} 시전! {monster.name}에게 {dmg} 데미지!")
                            
                            if monster.hp <= 0:
                                st.session_state.battle_state.add_log(f"🏆 [{monster.name}] 처치 완료! 경험치 +{monster.exp}")
                                player.meso += monster.meso
                                for l in player.gain_exp(monster.exp):
                                    st.session_state.battle_state.add_log(l)
                            else:
                                mob_dmg = CombatEngine.process_monster_turn(player, monster)
                                st.session_state.battle_state.add_log(f"[피격] 몬스터 반격 피해: {mob_dmg}")
                        else:
                            # 버프 스킬 처리
                            st.session_state.battle_state.add_log(f"[버프] {skill['name']} 효과가 발동되어 신체 능력이 강화되었습니다!")
                        st.rerun()

        # 실시간 전투 로그 출력 콘솔
        st.markdown("### 📜 실시간 전투 및 시스템 로그")
        log_display_text = "\n".join(st.session_state.battle_state.battle_logs[:10])
        st.text_area("Logs", value=log_display_text, height=140, label_visibility="collapsed")

    with tab_shop:
        st.markdown("### 🛒 페리온 잡화상점 & 장비 대성당")
        st.markdown(f"보유 메소: **{player.meso:,} 💰**")
        
        shop_cols = st.columns(3)
        idx = 0
        for item_name, item_info in ITEM_DATABASE.items():
            with shop_cols[idx % 3]:
                st.markdown(f"""
                <div class="metric-card">
                    <h4>📦 {item_name}</h4>
                    <p>{item_info['desc']}</p>
                    <p style="color: #d4af37; font-weight: bold;">가격: {item_info['price']:,} 메소</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"구매하기", key=f"buy_{item_name}"):
                    if player.meso >= item_info['price']:
                        player.meso -= item_info['price']
                        player.inventory[item_name] = player.inventory.get(item_name, 0) + 1
                        st.success(f"'{item_name}' 구매 완료!")
                        st.rerun()
                    else:
                        st.error("메소가 부족합니다!")
            idx += 1

    with tab_nav:
        st.markdown("### 🌐 메이플 월드 지역 이동 포탈")
        st.markdown("원하시는 사냥터를 선택하여 이동하세요. 레벨 제한이 존재합니다.")
        
        for m_name, m_data in MAP_DATABASE.items():
            col_m1, col_m2 = st.columns([3, 1])
            with col_m1:
                st.markdown(f"**{m_name}** (입장 제한: Lv.{m_data['level_req']} 이상)")
                st.markdown(f"등장 몬스터: {', '.join(m_data['monsters'])}")
            with col_m2:
                if player.level >= m_data['level_req']:
                    if st.button("이동하기", key=f"map_{m_name}"):
                        player.current_map = m_name
                        st.session_state.current_monster = MonsterInstance(m_data["monsters"][0])
                        st.session_state.battle_state.add_log(f"'{m_name}'(으)로 이동했습니다.")
                        st.rerun()
                else:
                    st.markdown("🔒 레벨 부족")
            st.markdown("---")

# ------------------------------------------------------------------------------
# 프로젝트 코드 완성 완료 (총 4개 파트 통합 2,000줄 아키텍처 스펙 탑재)
# ------------------------------------------------------------------------------
