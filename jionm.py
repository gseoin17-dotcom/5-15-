import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - v2",
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


def get_enhance_cost(level, is_rebirth):
  if is_rebirth:
    cost_table = {
        0: 1000000,
        1: 2500000,
        2: 5000000,
        3: 10000000,
        4: 20000000,
        5: 40000000,
        6: 80000000,
        7: 150000000,
        8: 300000000,
        9: 600000000,
        10: 1200000000,
        11: 2500000000,
        12: 5000000000,
        13: 10000000000,
        14: 20000000000,
        15: 40000000000,
        16: 80000000000,
        17: 150000000000,
        18: 300000000000,
        19: 600000000000,
        20: 1200000000000,
        21: 2500000000000,
        22: 5000000000000,
        23: 10000000000000,
        24: 25000000000000,
        25: 100000000000000,
    }
    return cost_table.get(level, 100000000000000)
  else:
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
        31: 250000000,
        32: 400000000,
        33: 700000000,
        34: 1200000000,
        35: 2000000000,
    }
    return cost_table.get(level, 2000000000)


def get_shield_cost(level, is_rebirth):
  base_cost = get_enhance_cost(level, is_rebirth)
  return max(50000, base_cost * 15)


# 강화 성공 시 지급되는 포인트
# 강화 단계가 높아질수록 포인트 보상도 크게 증가합니다.
# 워프권 가격은 해당 단계 강화 성공 포인트의 20배입니다.
# 예: 20단계 성공 보상 10,000P -> 20단계 워프권 200,000P
POINT_REWARD_TABLE = {
    1: 100,
    2: 150,
    3: 200,
    4: 300,
    5: 500,
    6: 700,
    7: 900,
    8: 1200,
    9: 1500,
    10: 2000,
    11: 2500,
    12: 3000,
    13: 3500,
    14: 4000,
    15: 5000,
    16: 6000,
    17: 7000,
    18: 8000,
    19: 9000,
    20: 10000,
    21: 12000,
    22: 14000,
    23: 16000,
    24: 18000,
    25: 20000,
    26: 23000,
    27: 26000,
    28: 30000,
    29: 35000,
    30: 40000,
    31: 45000,
    32: 50000,
    33: 60000,
    34: 70000,
    35: 80000,
}

def get_enhance_point_reward(level):
  level = int(level)
  if level <= 0:
    return 0
  if level in POINT_REWARD_TABLE:
    return POINT_REWARD_TABLE[level]
  # 표 밖의 단계가 생겨도 마지막 보상 기준으로 자연스럽게 증가
  return POINT_REWARD_TABLE[35] + (level - 35) * 10000


def get_warp_point_cost(level):
  # 워프권은 해당 단계 강화 성공 포인트의 20배
  return get_enhance_point_reward(level) * 20


def get_warp_money_cost(level, is_rebirth):
  # 워프권을 돈으로 구매할 때의 가격
  # 해당 단계의 냄새 가치와 동일하게 설정
  return int(SMELL_DB[is_rebirth][level]["price"])


def get_shield_point_cost(level, is_rebirth):
  # 방지권 포인트 가격
  # 해당 단계 강화 성공 포인트의 5배
  return get_enhance_point_reward(level) * 5


# -----------------------------------------------------------------------------
# 3. 게임 데이터베이스 정의 (시즌1: 35단계 / 시즌2: 25단계)
# -----------------------------------------------------------------------------
SMELL_DB = {
    False: {
        0: {
            "name": "0단계 : 무취 지온의 공간",
            "desc": "아직은 아무 냄새도 안 남. 지온이가 씻었나 봄.",
            "price": 0,
            "color": "#4a5568",
            "tier": 1,
        },
        1: {
            "name": "1단계 : 스쳐가는 지온냄새",
            "desc": (
                "버스 옆자리에 앉은 지온이가 팔을 들 때 스치듯 나는 가벼운"
                " 암내."
            ),
            "price": 150,
            "color": "#718096",
            "tier": 1,
        },
        2: {
            "name": "2단계 : 은은한 지온냄새",
            "desc": "체육 시간이 끝난 뒤 지온이가 벗어던진 축축한 양말 냄새.",
            "price": 400,
            "color": "#38a169",
            "tier": 1,
        },
        3: {
            "name": "3단계 : 습한 지온냄새",
            "desc": "사흘 동안 빨지 않은 지온이의 후드티 모자에 쩐내.",
            "price": 600,
            "color": "#276749",
            "tier": 1,
        },
        4: {
            "name": "4단계 : 진득한 지온냄새",
            "desc": (
                "여름철 밀폐된 방 안에서 지온이가 뒹굴다 난 땀에 쩐 이불 냄새."
            ),
            "price": 800,
            "color": "#319795",
            "tier": 1,
        },
        5: {
            "name": "5단계 : 자극적인 지온냄새",
            "desc": "지온이가 발가락을 긁은 손으로 코를 슥 만지게 만드는 향.",
            "price": 3000,
            "color": "#2c7a7b",
            "tier": 1,
        },
        6: {
            "name": "6단계 : 풍부한 지온냄새",
            "desc": (
                "신발장에 박아둔 지온이의 축구화 속에서 무르익은 발효 냄새."
            ),
            "price": 3500,
            "color": "#3182ce",
            "tier": 2,
        },
        7: {
            "name": "7단계 : 압도적인 지온냄새",
            "desc": (
                "지온이가 다녀간 자리마다 코를 찌르는 시큼털털한 체취의 파도."
            ),
            "price": 6100,
            "color": "#2b6cb0",
            "tier": 2,
        },
        8: {
            "name": "8단계 : 폭발하는 지온냄새",
            "desc": (
                "일주일 동안 안 감은 지온이 머리통에서 뿜어져 나오는 유분 폭탄."
            ),
            "price": 10000,
            "color": "#805ad5",
            "tier": 2,
        },
        9: {
            "name": "9단계 : 시공을 뒤흔드는 지온냄새",
            "desc": "화장실 문을 열자마자 지온이가 남기고 간 흔적의 생생함.",
            "price": 20000,
            "color": "#6b46c1",
            "tier": 2,
        },
        10: {
            "name": "10단계 : 치명적인 지온냄새",
            "desc": "맡는 순간 안구실종을 유발하는 지온이의 살인적인 입냄새.",
            "price": 35100,
            "color": "#d69e2e",
            "tier": 2,
        },
        11: {
            "name": "11단계 : 환각을 부르는 지온냄새",
            "desc": (
                "썩은 청국장과 지온이의 발냄새가 콜라보를 이뤄 주마등이"
                " 스친다."
            ),
            "price": 160000,
            "color": "#b7791f",
            "tier": 3,
        },
        12: {
            "name": "12단계 : 공간지배 지온냄새",
            "desc": "방 문을 열기도 전에 복도까지 마중 나온 지온이의 찌든 내음.",
            "price": 350000,
            "color": "#dd6b20",
            "tier": 3,
        },
        13: {
            "name": "13단계 : 전성기 지온냄새",
            "desc": (
                "음식물 쓰레기통을 여름볕에 사흘간 방치한 것과 비견되는 향."
            ),
            "price": 1000000,
            "color": "#c05621",
            "tier": 3,
        },
        14: {
            "name": "14단계 : 신성한 지온냄새",
            "desc": "너무 지독해서 눈물마저 고이게 만드는 지온이의 꼬릿한 기운.",
            "price": 3000000,
            "color": "#e53e3e",
            "tier": 3,
        },
        15: {
            "name": "15단계 : 오리지널 지온냄새",
            "desc": "하수구 역류 현상과 지온이의 입김이 만나 온 세상이 오염된다.",
            "price": 7500000,
            "color": "#9b2c2c",
            "tier": 3,
        },
        16: {
            "name": "16단계 : 우주관통 지온냄새",
            "desc": (
                "대기권을 뚫고 오존층마저 뻥 뚫어버리는 지온이의 겨드랑이"
                " 폭풍."
            ),
            "price": 14200000,
            "color": "#00f0ff",
            "tier": 4,
        },
        17: {
            "name": "17단계 : 차원균열 지온냄새",
            "desc": (
                "지온이의 구린내가 너무 독해서 다른 평행세계의 코까지 썩힌다."
            ),
            "price": 20000000,
            "color": "#ff00ea",
            "tier": 4,
        },
        18: {
            "name": "18단계 : Absolute 지온냄새",
            "desc": (
                "우주 만물의 원소를 전부 지온이의 체취로 치환해버리는"
                " 절대악취."
            ),
            "price": 30000000,
            "color": "#ffe600",
            "tier": 4,
        },
        19: {
            "name": "19단계 : 초월 지온냄새",
            "desc": "인간의 후각 세포를 단번에 파괴하는 초월적인 썩은 내.",
            "price": 47500000,
            "color": "#ff0055",
            "tier": 4,
        },
        20: {
            "name": "20단계 : 지온이의 정성이 들어간 포근한 집밥 냄새",
            "desc": (
                "지온맘이 끓여준 묵은지 김치찌개... 인 줄 알았으나 지온이"
                " 빨래 냄새."
            ),
            "price": 68300000,
            "color": "#ffaa00",
            "tier": 4,
        },
        21: {
            "name": "21단계 : 지온이의 엄격한 샤우팅 냄새",
            "desc": (
                "안 씻고 버티는 지온이를 잡으려고 지온맘이 휘두른 등짝의"
                " 내음."
            ),
            "price": 101000000,
            "color": "#ff4500",
            "tier": 5,
        },
        22: {
            "name": "22단계 : 지온이의 전설의 흙된장국 냄새",
            "desc": (
                "지온이의 발냄새 원액을 살짝 타서 깊은 맛을 낸 지온맘의"
                " 특제 국물."
            ),
            "price": 160000000,
            "color": "#ff007f",
            "tier": 5,
        },
        23: {
            "name": "23단계 : 지온이의 100년 숙성 원액 냄새",
            "desc": (
                "지온이가 어릴 때부터 모아둔 꼬릿한 때를 장독대에 묻어"
                " 숙성시켰다."
            ),
            "price": 230000000,
            "color": "#7b00ff",
            "tier": 5,
        },
        24: {
            "name": "24단계 : 지온이의 냄새 탈취 스프레이 냄새",
            "desc": (
                "방 안에 쩔어 있는 지온이의 체취를 탈취제로 잡으려다"
                " 역관람당함."
            ),
            "price": 300000000,
            "color": "#0088ff",
            "tier": 5,
        },
        25: {
            "name": "25단계 : 지온이의 대인배적인 냄새",
            "desc": (
                "이런 지온이라도 품에 안아주는 지온맘의 대인배적 냄새"
                " 포용력."
            ),
            "price": 400000000,
            "color": "#00ffaa",
            "tier": 5,
        },
        26: {
            "name": "26단계 : 지온이의 궁극 필살기 냄새",
            "desc": (
                "지온이 방 문을 강제로 열고 환기시키며 뿜어내는 지온맘의"
                " 분노."
            ),
            "price": 1800000000,
            "color": "#ccff00",
            "tier": 6,
        },
        27: {
            "name": "27단계 : 지온이의 창조와 냄새",
            "desc": "지온이의 모든 악취를 정화하려다 지온맘마저 구속당한 경지.",
            "price": 2500000000,
            "color": "#fffb00",
            "tier": 6,
        },
        28: {
            "name": "28단계 : 지온이의 우주창조설 냄새",
            "desc": (
                "우주 전체가 지온이의 발냄새 아래 무릎을 꿇고 헛구역질을 한다."
            ),
            "price": 5500000000,
            "color": "#ffffff",
            "tier": 6,
        },
        29: {
            "name": "29단계 : 딥다크 지온냄새",
            "desc": (
                "모든 꼬릿한 냄새의 근원이자, 지온이를 낳고 기른 위대한 악취의"
                " 여신."
            ),
            "price": 10500000000,
            "color": "#ff00aa",
            "tier": 6,
        },
        30: {
            "name": "30단계 : 태초의 지온냄새 ",
            "desc": "우주 탄생 이전부터 존재했던 오리지널 태고의 구린내.",
            "price": 20000000000,
            "color": "#00ffff",
            "tier": 6,
        },
        31: {
            "name": "31단계 : 하이퍼 지온 싱귤래리티",
            "desc": (
                "냄새가 너무 묵직해서 블랙홀처럼 주변 모든 빛과 산소를"
                " 빨아들인다."
            ),
            "price": 45000000000,
            "color": "#7000ff",
            "tier": 6,
        },
        32: {
            "name": "32단계 : 멀티버스 지온 에센스",
            "desc": "모든 평행우주에 존재하는 지온이의 체취가 한곳으로 모이는 중.",
            "price": 90000000000,
            "color": "#ff00e1",
            "tier": 6,
        },
        33: {
            "name": "33단계 : 인피니티 지온 페트리코",
            "desc": "영원히 끝나지 않는 지온이의 발효 비린내가 온 은하를 뒤덮음.",
            "price": 200000000000,
            "color": "#00ff66",
            "tier": 6,
        },
        34: {
            "name": "34단계 : 오메가 지온 제네시스",
            "desc": "지온이의 냄새로 우주를 멸망시키고 다시 창조하는 종말의 향기.",
            "price": 500000000000,
            "color": "#ff6600",
            "tier": 6,
        },
        35: {
            "name": "35단계 : ★디 오리지널 앱솔루트 지온★",
            "desc": "우주 만물을 통틀어 가장 지독하고 완벽한 궁극의 지온 냄새.",
            "price": 1000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
    },
    True: {
        0: {
            "name": "환생 0단계 : 초신성 핵폐기물 자이온",
            "desc": "환생을 거쳐 새롭게 압축된 태초의 고밀도 방사능 악취.",
            "price": 1000000000,
            "color": "#ff0055",
            "tier": 1,
        },
        1: {
            "name": "환생 1단계 : 안드로메다 자이온 암모니아",
            "desc": "안드로메다 은하 전체를 알칼리화시키는 암모니아 폭풍.",
            "price": 2500000000,
            "color": "#00ffff",
            "tier": 1,
        },
        2: {
            "name": "환생 2단계 : 화이트홀 자이온 하이드로겐",
            "desc": "우주 백색왜성의 폭발과 함께 뿜어져 나오는 순백의 악취.",
            "price": 6000000000,
            "color": "#ffffff",
            "tier": 1,
        },
        3: {
            "name": "환생 3단계 : 쿼크 글루온 자이온 악취",
            "desc": (
                "소립자 수준에서부터 강하게 결합되어 떨어지지 않는 쿼크급"
                " 냄새."
            ),
            "price": 15000000000,
            "color": "#ffaa00",
            "tier": 2,
        },
        4: {
            "name": "환생 4단계 : 차원왜곡 자이온 타임루프 찌든내 ",
            "desc": (
                "시간의 흐름마저 썩어버리게 만드는 과거와 미래의 냄새 집합체."
            ),
            "price": 35000000000,
            "color": "#9b2c2c",
            "tier": 2,
        },
        5: {
            "name": "환생 5단계 : 네메시스 자이온 다크매터",
            "desc": (
                "빛조차 탈출하지 못하고 악취에 붙잡혀 빨려 들어가는 암흑물질."
            ),
            "price": 80000000000,
            "color": "#38a169",
            "tier": 2,
        },
        6: {
            "name": "환생 6단계 : 메가 블랙홀 자이온 호라이즌",
            "desc": (
                "모든 물리 법칙이 붕괴하고 오직 자이온이의 체취만 남는"
                " 경계선."
            ),
            "price": 180000000000,
            "color": "#805ad5",
            "tier": 3,
        },
        7: {
            "name": "환생 7단계 : 감마선 버스트 자이온 플레어",
            "desc": (
                "우주 끝까지 수십 광년 동안 일직선으로 뻗어 나가는 살인적"
                " 악취."
            ),
            "price": 400000000000,
            "color": "#e53e3e",
            "tier": 3,
        },
        8: {
            "name": "환생 8단계 : 하이퍼노바 자이온 코어 붕괴",
            "desc": "거대 항성이 생을 마감하며 방출하는 전설적인 폭발성 악취.",
            "price": 900000000000,
            "color": "#ff4500",
            "tier": 3,
        },
        9: {
            "name": "환생 9단계 : 엘더블루 제네시스 자이온",
            "desc": (
                "태초의 우주가 생성되기도 전에 존재했던 푸른빛의 시원(始源)"
                " 냄새."
            ),
            "price": 2000000000000,
            "color": "#0088ff",
            "tier": 4,
        },
        10: {
            "name": "환생 10단계 : 카이퍼 자이온 벨트 코스믹 더스트",
            "desc": (
                "태양계 외곽의 얼어붙은 얼음 조각들에 스며든 미지의 원시 악취."
            ),
            "price": 4500000000000,
            "color": "#cbd5e1",
            "tier": 4,
        },
        11: {
            "name": "환생 11단계 : 자이온오르트 클라우드 딥 프리즈",
            "desc": (
                "영원히 녹지 않을 것 같은 극저온 속에서 서서히 발효된 냉동"
                " 체취."
            ),
            "price": 10000000000000,
            "color": "#319795",
            "tier": 4,
        },
        12: {
            "name": "환생 12단계 : 태양풍 플라즈마 자이온제트 스트림",
            "desc": "태양 표면에서 뿜어져 나오는 고온다습한 초고속 플라즈마 냄새.",
            "price": 22000000000000,
            "color": "#f59e0b",
            "tier": 5,
        },
        13: {
            "name": "환생 13단계 : 마그네타 자이온자기장 폭풍",
            "desc": (
                "지구상의 모든 나침반을 고장 내고 정신을 아득하게 만드는"
                " 자기장."
            ),
            "price": 50000000000000,
            "color": "#7000ff",
            "tier": 5,
        },
        14: {
            "name": "환생 14단계 : 펄서 자이온로테이션 시그널",
            "desc": (
                "일정한 주기로 우주 전체에 강력한 악취 전파를 송출하는"
                " 중성자별."
            ),
            "price": 120000000000000,
            "color": "#00ff66",
            "tier": 5,
        },
        15: {
            "name": "환생 15단계 : 웜홀 크로스오버 자이온 디멘션",
            "desc": (
                "시공간의 통로를 열어 다른 차원의 구린내를 실시간으로 끌어온다."
            ),
            "price": 280000000000000,
            "color": "#ff00ea",
            "tier": 6,
        },
        16: {
            "name": "환생 16단계 : 스트링 시스코어 자이온 엠피리어",
            "desc": (
                "초끈이론의 11차원을 진동시키며 울려 퍼지는 궁극의 우주"
                " 진동음."
            ),
            "price": 600000000000000,
            "color": "#ccff00",
            "tier": 6,
        },
        17: {
            "name": "환생 17단계 : 센타우루스 자이온 알파 코어",
            "desc": (
                "가장 가까운 별무리의 기운을 통째로 오염시킨 강력한 은하수 향."
            ),
            "price": 1300000000000000,
            "color": "#ff6600",
            "tier": 6,
        },
        18: {
            "name": "환생 18단계 : 페가수스 자이온 별자리 네뷸라",
            "desc": (
                "신화 속 날개 든 말의 질주를 따라 온 하늘에 퍼지는 거대 성운"
                " 향."
            ),
            "price": 3000000000000000,
            "color": "#00f0ff",
            "tier": 6,
        },
        19: {
            "name": "환생 19단계 : 자이온세인트 오메가 얼티밋 에센스",
            "desc": (
                "우주의 수명이 다하는 순간까지 사라지지 않는 불멸의 성스러운"
                " 냄새."
            ),
            "price": 7000000000000000,
            "color": "#ffe600",
            "tier": 6,
        },
        20: {
            "name": "환생 20단계 : 코스믹 인피니티 싱귤자이온래리티",
            "desc": "모든 차원과 우주의 모든 존재가 하나로 응축된 무한대의 악취.",
            "price": 15000000000000000,
            "color": "#ff00aa",
            "tier": 6,
        },
        21: {
            "name": "환생 21단계 : 자이온트랜스센던탈 앱솔루트 가디언",
            "desc": (
                "차원의 벽을 넘어 초월적인 신위(神威)를 뿜어내는 가디언의"
                " 경지."
            ),
            "price": 35000000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
        22: {
            "name": "환생 22단계 : 하이퍼 자이온 디바인 코어",
            "desc": (
                "자이온이라는 존재 자체가 우주의 신성한 법칙으로 등용한 상태."
            ),
            "price": 80000000000000000,
            "color": "#7b00ff",
            "tier": 6,
        },
        23: {
            "name": "환생 23단계 : 자이온옴니버스 마스터피스 악취",
            "desc": "모든 평행세계를 통틀어 단 하나만 존재하는 완벽한 걸작 악취.",
            "price": 200000000000000000,
            "color": "#00ffff",
            "tier": 6,
        },
        24: {
            "name": "환생 24단계 : 이터널 제네시스 울티마자이온s",
            "desc": "우주의 탄생과 종말을 영원히 반복하게 만드는 궁극의 고리.",
            "price": 500000000000000000,
            "color": "#ff4500",
            "tier": 6,
        },
        25: {
            "name": "환생 25단계 : ★심플 성지온★",
            "desc": "문일중 3학년 5반의 냄새를 담당하는 그저 GOA.T",
            "price": 1000000000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
    },
}

PROB_TABLE = {
    False: {
        0: (100.0, 0.0, 0.0, 0.0),
        1: (100.0, 0.0, 0.0, 0.0),
        2: (100.0, 0.0, 0.0, 0.0),
        3: (96.0, 4.0, 0.0, 0.0),
        4: (96.0, 4.0, 0.0, 0.0),
        5: (91.0, 9.0, 0.0, 0.0),
        6: (91.0, 7.5, 1.5, 0.0),
        7: (91.0, 4.5, 4.5, 0.0),
        8: (86.0, 9.5, 4.5, 0.0),
        9: (81.0, 14.5, 4.5, 0.0),
        10: (81.0, 14.5, 4.5, 0.0),
        11: (76.0, 14.5, 4.5, 5.0),
        12: (71.0, 14.5, 4.5, 10.0),
        13: (71.0, 14.5, 6.5, 8.0),
        14: (66.0, 14.5, 9.5, 10.0),
        15: (61.0, 19.5, 9.5, 10.0),
        16: (61.0, 17.5, 11.5, 10.0),
        17: (56.0, 19.5, 14.5, 10.0),
        18: (51.0, 19.5, 16.5, 13.0),
        19: (51.0, 19.5, 19.5, 10.0),
        20: (46.0, 21.5, 22.5, 10.0),
        21: (41.0, 24.5, 24.5, 10.0),
        22: (41.0, 22.5, 26.5, 10.0),
        23: (41.0, 19.5, 29.5, 10.0),
        24: (41.0, 17.5, 31.5, 10.0),
        25: (36.0, 24.5, 29.5, 10.0),
        26: (51.0, 19.5, 24.5, 5.0),
        27: (41.0, 24.5, 29.5, 5.0),
        28: (31.0, 29.5, 34.5, 5.0),
        29: (21.0, 34.5, 39.5, 5.0),
        30: (16.0, 34.5, 44.5, 5.0),
        31: (13.0, 34.5, 47.5, 5.0),
        32: (11.0, 34.5, 49.5, 5.0),
        33: (9.0, 36.5, 49.5, 5.0),
        34: (6.0, 39.5, 49.5, 5.0),
    },
    True: {
        0: (100.0, 0.0, 0.0, 0.0),
        1: (96.0, 4.0, 0.0, 0.0),
        2: (91.0, 7.5, 1.5, 0.0),
        3: (86.0, 9.5, 4.5, 0.0),
        4: (81.0, 14.5, 4.5, 0.0),
        5: (76.0, 14.5, 4.5, 5.0),
        6: (71.0, 14.5, 6.5, 8.0),
        7: (66.0, 17.5, 9.5, 7.0),
        8: (61.0, 19.5, 9.5, 10.0),
        9: (56.0, 19.5, 14.5, 10.0),
        10: (51.0, 21.5, 17.5, 10.0),
        11: (46.0, 24.5, 19.5, 10.0),
        12: (41.0, 24.5, 24.5, 10.0),
        13: (39.0, 24.5, 26.5, 10.0),
        14: (36.0, 24.5, 29.5, 10.0),
        15: (33.0, 27.5, 29.5, 10.0),
        16: (31.0, 29.5, 34.5, 5.0),
        17: (26.0, 31.5, 37.5, 5.0),
        18: (21.0, 34.5, 39.5, 5.0),
        19: (19.0, 34.5, 41.5, 5.0),
        20: (16.0, 34.5, 44.5, 5.0),
        21: (13.0, 37.5, 44.5, 5.0),
        22: (11.0, 39.5, 44.5, 5.0),
        23: (9.0, 41.5, 44.5, 5.0),
        24: (6.0, 44.5, 44.5, 5.0),
    },
}

CRITICAL_RATE = 0.05
PITY_MAX = 4

# -----------------------------------------------------------------------------
# 업적 / 칭호 시스템
# -----------------------------------------------------------------------------
ACHIEVEMENTS = {
    "first_enhance": {
        "name": "첫걸음",
        "desc": "처음으로 강화를 시도하세요.",
        "title": "지온 킁킁 견습생",
        "reward": 5000,
    },
    "level_10": {
        "name": "10강 돌파",
        "desc": "시즌 1에서 10단계에 도달하세요.",
        "title": "지온 구린내 수련생",
        "reward": 20000,
    },
    "level_20": {
        "name": "20강 돌파",
        "desc": "시즌 1에서 20단계에 도달하세요.",
        "title": "지온 베테랑 후각러",
        "reward": 100000,
    },
    "level_30": {
        "name": "30강 돌파",
        "desc": "시즌 1에서 30단계에 도달하세요.",
        "title": "지온 악취 마스터",
        "reward": 500000,
    },
    "level_35": {
        "name": "궁극의 지온",
        "desc": "시즌 1 최종 35단계를 달성하세요.",
        "title": "디 오리지널 지온",
        "reward": 1000000,
    },
    "drop_to_0": {
        "name": "끝없는 추락",
        "desc": "34단계에서 0단계로 돌아가세요.",
        "title": "자이온 추락의 전설",
        "reward": 300000,
    },
    "rebirth": {
        "name": "차원의 문",
        "desc": "시즌 2 환생을 시작하세요.",
        "title": "지온 차원 여행자",
        "reward": 5000000,
    },
    "s2_level_10": {
        "name": "자이온 각성",
        "desc": "시즌 2에서 10단계에 도달하세요.",
        "title": "각성한 자이온",
        "reward": 10000000,
    },
    "s2_level_20": {
        "name": "자이온 폭주",
        "desc": "시즌 2에서 20단계에 도달하세요.",
        "title": "폭주의 자이온",
        "reward": 30000000,
    },
    "s2_level_25": {
        "name": "진정한 환생",
        "desc": "시즌 2 최종 25단계를 달성하세요.",
        "title": "TRUE REBIRTH 자이온",
        "reward": 100000000,
    },
    "warp_1": {
        "name": "공간 이동",
        "desc": "워프권을 처음 사용하세요.",
        "title": "자이온 워프 개척자",
        "reward": 10000,
    },
    "warp_5": {
        "name": "워프 중독",
        "desc": "워프권을 5회 사용하세요.",
        "title": "자이온 차원 도약자",
        "reward": 100000,
    },
    "critical": {
        "name": "대성공",
        "desc": "크리티컬 강화를 성공시키세요.",
        "title": "우주의 지온 선택",
        "reward": 50000,
    },
    "seller": {
        "name": "냄새 장사꾼",
        "desc": "냄새를 판매해 돈을 획득하세요.",
        "title": "지온 냄새 상인",
        "reward": 25000,
    },
    "enhance_50": {
        "name": "강화광",
        "desc": "강화를 총 50회 시도하세요.",
        "title": "자이온 망치 중독자",
        "reward": 200000,
    },
    "enhance_100": {
        "name": "강화의 끝",
        "desc": "강화를 총 100회 시도하세요.",
        "title": "단련의 지온 신",
        "reward": 1000000,
    },
    "level_5": {
        "name": "첫 강화",
        "desc": "5단계에 도달하세요.",
        "title": "지온 입문 코끝러",
        "reward": 5000,
    },
    "level_15": {
        "name": "중급 냄새꾼",
        "desc": "15단계에 도달하세요.",
        "title": "지온 향기 수집가",
        "reward": 50000,
    },
    "level_25": {
        "name": "고급 냄새꾼",
        "desc": "25단계에 도달하세요.",
        "title": "자이온 악취 지배자",
        "reward": 250000,
    },
    "s2_level_5": {
        "name": "자이온 입문",
        "desc": "시즌 2에서 5단계에 도달하세요.",
        "title": "자이온 견습생",
        "reward": 1000000,
    },
    "s2_level_15": {
        "name": "자이온 숙련",
        "desc": "시즌 2에서 15단계에 도달하세요.",
        "title": "자이온 숙련자",
        "reward": 15000000,
    },
    "warp_10": {
        "name": "워프 마스터",
        "desc": "워프권을 10회 사용하세요.",
        "title": "자이온 공간 지배자",
        "reward": 500000,
    },
    "enhance_200": {
        "name": "강화는 계속된다",
        "desc": "강화를 총 200회 시도하세요.",
        "title": "자이온 강화의 초월자",
        "reward": 5000000,
    },
    "rich": {
        "name": "부자 냄새",
        "desc": "보유 금액 10억을 달성하세요.",
        "title": "지온 재벌",
        "reward": 1000000,
    },
    "seller_10": {
        "name": "장사의 신",
        "desc": "판매를 10회 성공하세요.",
        "title": "자이온 전설의 상인",
        "reward": 300000,
    },
    "points_100k": {
        "name": "포인트 수집가",
        "desc": "누적 획득 포인트 100,000P를 달성하세요.",
        "title": "지온 포인트 수집가",
        "reward": 100000,
    },
    "points_1m": {
        "name": "포인트 백만장자",
        "desc": "누적 획득 포인트 1,000,000P를 달성하세요.",
        "title": "자이온 포인트 부자",
        "reward": 1000000,
    },
    "critical_5": {
        "name": "크리티컬 헌터",
        "desc": "크리티컬 강화를 5회 성공하세요.",
        "title": "지온 크리티컬 헌터",
        "reward": 500000,
    },
    "survivor": {
        "name": "기적의 생존",
        "desc": "20단계 이상에서 강화 실패 후 살아남으세요.",
        "title": "불굴의 자이온",
        "reward": 300000,
    },
}

TITLE_THEMES = {
    "지온 킁킁 견습생": ('#22d3ee', '#0e7490', '#083344', '🫧'),
    "지온 구린내 수련생": ('#a3e635', '#4d7c0f', '#1a2e05', '🌿'),
    "지온 베테랑 후각러": ('#60a5fa', '#1d4ed8', '#172554', '🎯'),
    "지온 악취 마스터": ('#f97316', '#c2410c', '#431407', '🔥'),
    "디 오리지널 지온": ('#facc15', '#a16207', '#422006', '👑'),
    "자이온 추락의 전설": ('#94a3b8', '#475569', '#0f172a', '☄️'),
    "지온 차원 여행자": ('#c084fc', '#7e22ce', '#2e1065', '🌀'),
    "각성한 자이온": ('#2dd4bf', '#0f766e', '#042f2e', '⚡'),
    "폭주의 자이온": ('#fb7185', '#be123c', '#4c0519', '💢'),
    "TRUE REBIRTH 자이온": ('#f0abfc', '#c026d3', '#4a044e', '♾️'),
    "자이온 워프 개척자": ('#38bdf8', '#0369a1', '#082f49', '🚀'),
    "자이온 차원 도약자": ('#818cf8', '#4338ca', '#1e1b4b', '🌌'),
    "우주의 지온 선택": ('#fde047', '#ca8a04', '#422006', '✦'),
    "지온 냄새 상인": ('#34d399', '#047857', '#022c22', '💰'),
    "자이온 망치 중독자": ('#fbbf24', '#d97706', '#451a03', '🔨'),
    "단련의 지온 신": ('#f8fafc', '#64748b', '#111827', '⚔️'),
    "지온 입문 코끝러": ('#67e8f9', '#0891b2', '#083344', '👃'),
    "지온 향기 수집가": ('#86efac', '#16a34a', '#052e16', '🍃'),
    "자이온 악취 지배자": ('#f472b6', '#db2777', '#500724', '☠️'),
    "자이온 견습생": ('#93c5fd', '#2563eb', '#172554', '🔷'),
    "자이온 숙련자": ('#a78bfa', '#6d28d9', '#2e1065', '💠'),
    "자이온 공간 지배자": ('#e879f9', '#a21caf', '#4a044e', '🛸'),
    "자이온 강화의 초월자": ('#fef08a', '#ea580c', '#431407', '🌠'),
    "지온 재벌": ('#fcd34d', '#b45309', '#451a03', '💎'),
    "자이온 전설의 상인": ('#5eead4', '#0f766e', '#042f2e', '🏪'),
    "불굴의 자이온": ('#f87171', '#991b1b', '#450a0a', '🛡️'),
    "지온 포인트 수집가": ('#fde047', '#a16207', '#422006', '🪙'),
    "자이온 포인트 부자": ('#67e8f9', '#0891b2', '#083344', '💎'),
    "지온 크리티컬 헌터": ('#fb7185', '#9f1239', '#4c0519', '🎯'),
}

def get_title_theme(title):
    return TITLE_THEMES.get(title, ("#a78bfa", "#6d28d9", "#111827", "🏷️"))

TITLE_STYLES = {
    "지온 킁킁 견습생": "title-style-bubble",
    "지온 구린내 수련생": "title-style-leaf",
    "지온 베테랑 후각러": "title-style-target",
    "지온 악취 마스터": "title-style-flame",
    "디 오리지널 지온": "title-style-crown",
    "자이온 추락의 전설": "title-style-meteor",
    "지온 차원 여행자": "title-style-portal",
    "각성한 자이온": "title-style-bolt",
    "폭주의 자이온": "title-style-rage",
    "TRUE REBIRTH 자이온": "title-style-infinity",
    "자이온 워프 개척자": "title-style-rocket",
    "자이온 차원 도약자": "title-style-galaxy",
    "우주의 지온 선택": "title-style-star",
    "지온 냄새 상인": "title-style-coin",
    "자이온 망치 중독자": "title-style-hammer",
    "단련의 지온 신": "title-style-blade",
    "지온 입문 코끝러": "title-style-nose",
    "지온 향기 수집가": "title-style-nature",
    "자이온 악취 지배자": "title-style-skull",
    "자이온 견습생": "title-style-diamond",
    "자이온 숙련자": "title-style-crystal",
    "자이온 공간 지배자": "title-style-ufo",
    "자이온 강화의 초월자": "title-style-comet",
    "지온 재벌": "title-style-gem",
    "자이온 전설의 상인": "title-style-shop",
    "불굴의 자이온": "title-style-shield",
    "지온 포인트 수집가": "title-style-pointcoin",
    "자이온 포인트 부자": "title-style-pointgem",
    "지온 크리티컬 헌터": "title-style-crithunter",
}

def get_title_style(title):
    return TITLE_STYLES.get(title, "title-style-default")


TITLE_DEFAULT = "칭호 없음"


def init_progress():
  if "achievements" not in st.session_state:
    st.session_state.achievements = {k: False for k in ACHIEVEMENTS}
  if "unlocked_titles" not in st.session_state:
    st.session_state.unlocked_titles = []
  if "selected_title" not in st.session_state:
    st.session_state.selected_title = TITLE_DEFAULT
  if "enhance_attempts" not in st.session_state:
    st.session_state.enhance_attempts = 0
  if "warp_uses" not in st.session_state:
    st.session_state.warp_uses = 0
  if "sell_count" not in st.session_state:
    st.session_state.sell_count = 0
  if "points" not in st.session_state:
    st.session_state.points = 0
  if "last_point_reward" not in st.session_state:
    st.session_state.last_point_reward = 0
  if "points_earned_total" not in st.session_state:
    st.session_state.points_earned_total = 0
  if "points_spent_total" not in st.session_state:
    st.session_state.points_spent_total = 0
  if "enhance_successes" not in st.session_state:
    st.session_state.enhance_successes = 0
  if "enhance_failures" not in st.session_state:
    st.session_state.enhance_failures = 0
  if "critical_count" not in st.session_state:
    st.session_state.critical_count = 0
  if "destroy_count" not in st.session_state:
    st.session_state.destroy_count = 0


def unlock_achievement(key):
  if key in ACHIEVEMENTS and not st.session_state.achievements.get(key, False):
    st.session_state.achievements[key] = True
    title = ACHIEVEMENTS[key]["title"]
    if title not in st.session_state.unlocked_titles:
      st.session_state.unlocked_titles.append(title)
    st.session_state.money += ACHIEVEMENTS[key]["reward"]
    st.toast(
        f"🏆 업적 달성: {ACHIEVEMENTS[key]['name']} |"
        f" +{format_gold(ACHIEVEMENTS[key]['reward'])}"
    )


def check_achievements():
  level = st.session_state.level
  if st.session_state.enhance_attempts >= 1:
    unlock_achievement("first_enhance")
  if st.session_state.enhance_attempts >= 50:
    unlock_achievement("enhance_50")
  if st.session_state.enhance_attempts >= 100:
    unlock_achievement("enhance_100")
  if st.session_state.enhance_attempts >= 200:
    unlock_achievement("enhance_200")
  if st.session_state.warp_uses >= 10:
    unlock_achievement("warp_10")
  if st.session_state.sell_count >= 10:
    unlock_achievement("seller_10")
  if st.session_state.money >= 1_000_000_000:
    unlock_achievement("rich")
  if not st.session_state.is_rebirth and level >= 5:
    unlock_achievement("level_5")
  if not st.session_state.is_rebirth and level >= 15:
    unlock_achievement("level_15")
  if not st.session_state.is_rebirth and level >= 25:
    unlock_achievement("level_25")
  if st.session_state.is_rebirth and level >= 5:
    unlock_achievement("s2_level_5")
  if st.session_state.is_rebirth and level >= 15:
    unlock_achievement("s2_level_15")
  if st.session_state.status == "FAIL" and level >= 20:
    unlock_achievement("survivor")
  if st.session_state.warp_uses >= 5:
    unlock_achievement("warp_5")
  if (
      not st.session_state.is_rebirth
      and level == 0
      and st.session_state.max_level >= 34
  ):
    unlock_achievement("drop_to_0")
  if not st.session_state.is_rebirth and level >= 10:
    unlock_achievement("level_10")
  if not st.session_state.is_rebirth and level >= 20:
    unlock_achievement("level_20")
  if not st.session_state.is_rebirth and level >= 35:
    unlock_achievement("level_35")
  if st.session_state.is_rebirth and level >= 10:
    unlock_achievement("s2_level_10")
  if st.session_state.is_rebirth and level >= 20:
    unlock_achievement("s2_level_20")
  if st.session_state.is_rebirth and level >= 25:
    unlock_achievement("s2_level_25")
  if st.session_state.warp_uses >= 1:
    unlock_achievement("warp_1")
  if st.session_state.status == "CRITICAL":
    unlock_achievement("critical")
  if st.session_state.points_earned_total >= 100_000:
    unlock_achievement("points_100k")
  if st.session_state.points_earned_total >= 1_000_000:
    unlock_achievement("points_1m")
  if st.session_state.critical_count >= 5:
    unlock_achievement("critical_5")


# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "current_season" not in st.session_state:
  st.session_state.current_season = 1

if "season_data" not in st.session_state:
  st.session_state.season_data = {
      1: {
          "level": 0,
          "prev_level": 0,
          "max_level": 0,
          "money": 1000000,
          "status": "READY",
          "shield": 0,
          "tears": 0,
          "pity_count": 0,
          "unlocked_warps": {
              10: False,
              15: False,
              20: False,
              25: False,
              30: False,
          },
      },
      2: {
          "level": 0,
          "prev_level": 0,
          "max_level": 0,
          "money": 1000000000,
          "status": "READY",
          "shield": 0,
          "tears": 50,
          "pity_count": 0,
          "unlocked_season2_warps": {5: False, 10: False, 15: False, 20: False},
      },
  }

if "rebirth_count" not in st.session_state:
  st.session_state.rebirth_count = 0

init_progress()


def sync_session_state(target_season):
  st.session_state.current_season = target_season
  st.session_state.is_rebirth = target_season == 2
  data = st.session_state.season_data[target_season]

  st.session_state.level = data["level"]
  st.session_state.prev_level = data.get("prev_level", data["level"])
  st.session_state.max_level = data["max_level"]
  st.session_state.money = data["money"]
  st.session_state.status = data["status"]
  st.session_state.shield = data["shield"]
  st.session_state.tears = min(60, data["tears"])
  st.session_state.pity_count = data["pity_count"]

  if target_season == 1:
    st.session_state.unlocked_warps = data["unlocked_warps"]
  else:
    st.session_state.unlocked_season2_warps = data["unlocked_season2_warps"]


def save_current_season_state():
  s = 2 if st.session_state.get("is_rebirth", False) else 1
  st.session_state.season_data[s]["level"] = st.session_state.level
  st.session_state.season_data[s]["prev_level"] = st.session_state.prev_level
  st.session_state.season_data[s]["max_level"] = st.session_state.max_level
  st.session_state.season_data[s]["money"] = st.session_state.money
  st.session_state.season_data[s]["status"] = st.session_state.status
  st.session_state.season_data[s]["shield"] = st.session_state.shield
  st.session_state.season_data[s]["tears"] = min(60, st.session_state.tears)
  st.session_state.season_data[s]["pity_count"] = st.session_state.pity_count

  if s == 1:
    st.session_state.season_data[1]["unlocked_warps"] = (
        st.session_state.unlocked_warps
    )
  else:
    st.session_state.season_data[2]["unlocked_season2_warps"] = (
        st.session_state.unlocked_season2_warps
    )


if "is_rebirth" not in st.session_state:
  sync_session_state(1)

# -----------------------------------------------------------------------------
# 5. 강화 로직
# -----------------------------------------------------------------------------


def reward_enhance_points(level):
  reward = get_enhance_point_reward(level)
  st.session_state.points += reward
  st.session_state.points_earned_total += reward
  st.session_state.last_point_reward = reward
  return reward


def run_enhance():
  save_current_season_state()
  max_lvl = 25 if st.session_state.is_rebirth else 35
  curr = st.session_state.level
  if curr >= max_lvl:
    save_current_season_state()
    return

  cost = get_enhance_cost(curr, st.session_state.is_rebirth)
  if st.session_state.money < cost:
    st.session_state.status = "NOT_ENOUGH_MONEY"
    save_current_season_state()
    return

  st.session_state.money -= cost
  st.session_state.prev_level = curr  # 이전 단계 저장

  if st.session_state.pity_count >= PITY_MAX - 1:
    st.session_state.level += 1
    st.session_state.status = "PITY_SUCCESS"
    st.session_state.pity_count = 0
    if st.session_state.level > st.session_state.max_level:
      st.session_state.max_level = st.session_state.level
    reward_enhance_points(st.session_state.level)
    save_current_season_state()
    return

  current_prob = PROB_TABLE[st.session_state.is_rebirth]
  sp, down_p, dp, hold_p = current_prob.get(curr, (5.0, 40.0, 50.0, 5.0))
  r = random.uniform(0, 100)

  success_limit = sp
  down_limit = success_limit + down_p
  destroy_limit = down_limit + dp

  if r < success_limit:
    st.session_state.pity_count = 0
    if random.random() < CRITICAL_RATE and curr + 2 <= max_lvl:
      st.session_state.level += 2
      st.session_state.status = "CRITICAL"
      st.session_state.enhance_successes += 1
      st.session_state.critical_count += 1
    else:
      st.session_state.level += 1
      st.session_state.status = "SUCCESS"
      st.session_state.enhance_successes += 1
    reward_enhance_points(st.session_state.level)
  elif r < down_limit:
    st.session_state.pity_count += 1
    if curr > 0:
      st.session_state.level -= 1
    st.session_state.status = "FAILED"
    st.session_state.enhance_failures += 1
    st.session_state.tears = min(60, st.session_state.tears + 1)
  elif r < destroy_limit:
    if st.session_state.shield > 0:
      st.session_state.shield -= 1
      st.session_state.pity_count += 1
      st.session_state.status = "SHIELD_SAVED"
      st.session_state.enhance_failures += 1
      st.session_state.tears = min(60, st.session_state.tears + 1)
    else:
      st.session_state.pity_count += 1
      st.session_state.level = 0
      st.session_state.status = "DESTROYED"
      st.session_state.enhance_failures += 1
      st.session_state.destroy_count += 1
      st.session_state.tears = min(60, st.session_state.tears + 2)
  else:
    st.session_state.pity_count += 1
    st.session_state.status = "HOLD"
    st.session_state.enhance_failures += 1
    st.session_state.tears = min(60, st.session_state.tears + 1)

  if st.session_state.level > st.session_state.max_level:
    st.session_state.max_level = st.session_state.level

  if not st.session_state.is_rebirth:
    for w_lvl in [10, 15, 20, 25, 30]:
      if st.session_state.level >= w_lvl:
        st.session_state.unlocked_warps[w_lvl] = True
  else:
    for w_lvl in [5, 10, 15, 20]:
      if st.session_state.level >= w_lvl:
        st.session_state.unlocked_season2_warps[w_lvl] = True

  save_current_season_state()


def sell():
  save_current_season_state()
  curr = st.session_state.level
  if curr == 0:
    return
  price_val = SMELL_DB[st.session_state.is_rebirth][curr]["price"]
  st.session_state.sell_count += 1
  if price_val == float("inf"):
    st.session_state.money = float("inf")
  else:
    st.session_state.money += price_val
  st.session_state.prev_level = curr
  st.session_state.level = 0
  st.session_state.status = "READY"
  save_current_season_state()


def trigger_rebirth():
  unlock_achievement("rebirth")
  save_current_season_state()
  sync_session_state(2)
  st.session_state.rebirth_count += 1
  # 환생하면 보유 포인트를 초기화한다.
  st.session_state.points = 0
  st.session_state.last_point_reward = 0
  st.session_state.status = "READY"
  save_current_season_state()


# -----------------------------------------------------------------------------
# 6. 테마 CSS
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Apple-inspired Liquid Glass UI */
    :root { --glass: rgba(255,255,255,.10); --glass-strong: rgba(255,255,255,.16); --stroke: rgba(255,255,255,.22); }
    .stApp {
        background: radial-gradient(circle at 15% 15%, rgba(90,120,255,.24), transparent 32%),
                    radial-gradient(circle at 85% 75%, rgba(180,100,255,.20), transparent 34%),
                    linear-gradient(135deg,#070b16,#101827 55%,#070a12);
        color:#f5f7fb; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    }
    .block-container { padding-top: 3.2rem !important; padding-bottom:2rem !important; max-width:94% !important; }
    .element-container, .stMarkdown { background:transparent !important; }
    div.stButton > button {
        border:1px solid var(--stroke) !important; border-radius:16px !important;
        padding:11px 16px !important; font-weight:650 !important; color:#fff !important;
        background:linear-gradient(135deg,rgba(255,255,255,.15),rgba(255,255,255,.06)) !important;
        backdrop-filter:blur(24px) saturate(150%); -webkit-backdrop-filter:blur(24px) saturate(150%);
        box-shadow:inset 0 1px rgba(255,255,255,.20),0 10px 30px rgba(0,0,0,.22) !important;
        transition:transform .2s ease,background .2s ease,box-shadow .2s ease !important;
    }
    div.stButton > button:hover { transform:translateY(-1px) scale(1.01); background:rgba(255,255,255,.20) !important; box-shadow:inset 0 1px rgba(255,255,255,.3),0 14px 35px rgba(0,0,0,.28) !important; }
    div.stButton > button:active { transform:scale(.98); }
    [data-testid="stTabs"] button { border-radius:14px !important; }
    [data-testid="stTabs"] [aria-selected="true"] { background:rgba(255,255,255,.13) !important; backdrop-filter:blur(18px); }
    [data-testid="stMetric"], [data-testid="stExpander"] { border:1px solid var(--stroke); border-radius:22px; background:var(--glass); backdrop-filter:blur(24px) saturate(150%); box-shadow:inset 0 1px rgba(255,255,255,.14),0 18px 45px rgba(0,0,0,.18); }

    .title-design { position:relative; overflow:hidden; min-height:116px; }
    .title-design::before,.title-design::after { content:""; position:absolute; pointer-events:none; }
    .title-style-bubble::before { width:70px;height:70px;border:2px solid rgba(34,211,238,.45);border-radius:50%;right:-18px;top:-25px;box-shadow:0 0 25px #22d3ee55; }
    .title-style-bubble::after { width:18px;height:18px;border:2px solid #67e8f9;border-radius:50%;right:28px;bottom:12px; }
    .title-style-leaf::before { width:100px;height:35px;right:-15px;bottom:4px;border:2px solid #a3e63566;border-radius:100% 0 100% 0;transform:rotate(-28deg); }
    .title-style-leaf::after { width:65px;height:2px;right:15px;bottom:28px;background:#a3e63588;transform:rotate(-28deg); }
    .title-style-target::before { width:66px;height:66px;right:-2px;top:16px;border:2px solid #60a5fa66;border-radius:50%;box-shadow:0 0 0 9px #60a5fa22,0 0 0 18px #60a5fa12; }
    .title-style-target::after { width:82px;height:2px;right:-8px;top:48px;background:#60a5fa66;transform:rotate(45deg); }
    .title-style-flame::before { width:52px;height:74px;right:10px;bottom:-24px;border-radius:60% 40% 60% 40%;background:linear-gradient(#f97316aa,#ef444400);transform:rotate(18deg);filter:blur(2px); }
    .title-style-flame::after { width:20px;height:40px;right:28px;bottom:-6px;border-radius:70% 30% 60% 40%;background:#facc15aa;transform:rotate(18deg); }
    .title-style-crown::before { content:"♛";right:16px;top:8px;font-size:62px;color:#facc1544;transform:rotate(8deg); }
    .title-style-crown::after { left:0;right:0;bottom:0;height:3px;background:linear-gradient(90deg,transparent,#facc15,#fff,#facc15,transparent); }
    .title-style-meteor::before { width:130px;height:2px;right:-25px;top:35px;background:linear-gradient(90deg,transparent,#94a3b8);transform:rotate(-25deg);box-shadow:0 14px 0 #94a3b833,0 28px 0 #94a3b822; }
    .title-style-meteor::after { width:11px;height:11px;border-radius:50%;right:34px;top:28px;background:#fff;box-shadow:0 0 18px 5px #94a3b866; }
    .title-style-portal::before { width:80px;height:80px;right:-10px;top:15px;border:8px double #c084fc55;border-radius:50%;transform:rotate(20deg); }
    .title-style-portal::after { width:35px;height:35px;right:13px;top:38px;border:1px solid #fff4;border-radius:50%;box-shadow:0 0 20px #c084fc88; }
    .title-style-bolt::before { content:"ϟ";right:18px;top:2px;font-size:76px;color:#2dd4bf55;transform:skew(-8deg); }
    .title-style-bolt::after { left:0;top:0;width:5px;height:100%;background:#2dd4bf;box-shadow:0 0 18px #2dd4bf; }
    .title-style-rage::before { left:-20px;right:-20px;bottom:14px;height:16px;background:repeating-linear-gradient(135deg,#fb718522 0 8px,transparent 8px 16px);transform:skewX(-25deg); }
    .title-style-rage::after { width:12px;height:75px;right:24px;top:10px;background:#fb718533;transform:rotate(38deg);box-shadow:18px 0 #fb718522; }
    .title-style-infinity::before { content:"∞";right:5px;top:-18px;font-size:110px;color:#f0abfc30;font-weight:900; }
    .title-style-infinity::after { left:8px;right:8px;top:8px;bottom:8px;border:1px dashed #f0abfc66;border-radius:12px; }
    .title-style-rocket::before { content:"➤";right:18px;top:18px;font-size:48px;color:#38bdf866;transform:rotate(-25deg); }
    .title-style-rocket::after { width:100px;height:3px;right:4px;top:65px;background:linear-gradient(90deg,transparent,#38bdf8aa);transform:rotate(-25deg); }
    .title-style-galaxy::before { width:95px;height:45px;right:-5px;top:30px;border:8px solid #818cf844;border-radius:50%;transform:rotate(-28deg);box-shadow:0 0 22px #818cf855; }
    .title-style-galaxy::after { width:7px;height:7px;border-radius:50%;right:42px;top:47px;background:#fff;box-shadow:20px -18px 0 #c4b5fd, -22px 15px 0 #818cfdaa; }
    .title-style-star::before { content:"✦";right:17px;top:4px;font-size:72px;color:#fde04755;text-shadow:0 0 22px #fde047; }
    .title-style-star::after { width:100%;height:1px;left:0;bottom:17px;background:linear-gradient(90deg,transparent,#fde04788,transparent); }
    .title-style-coin::before { width:58px;height:58px;right:15px;top:21px;border:5px solid #34d39955;border-radius:50%;box-shadow:inset 0 0 0 4px #34d39922,0 0 18px #34d39944; }
    .title-style-coin::after { content:"₩";right:31px;top:28px;font-size:28px;color:#34d39977;font-weight:900; }
    .title-style-hammer::before { content:"⚒";right:12px;top:13px;font-size:58px;color:#fbbf2466;transform:rotate(-20deg); }
    .title-style-hammer::after { left:0;right:0;bottom:0;height:5px;background:repeating-linear-gradient(90deg,#fbbf24 0 18px,#d97706 18px 36px);opacity:.45; }
    .title-style-blade::before { width:110px;height:5px;right:-8px;top:25px;background:linear-gradient(90deg,transparent,#f8fafc,#94a3b8);transform:rotate(-35deg);box-shadow:0 28px 0 #f8faf822; }
    .title-style-blade::after { width:28px;height:28px;right:30px;top:42px;border:2px solid #f8fafc66;border-radius:50%; }
    .title-style-nose::before { content:"〰";right:8px;top:20px;font-size:70px;color:#67e8f955;transform:rotate(-8deg); }
    .title-style-nose::after { width:70px;height:20px;right:18px;bottom:14px;border-bottom:3px dotted #67e8f966;border-radius:50%; }
    .title-style-nature::before { width:95px;height:95px;right:-20px;top:-20px;border:1px solid #86efac55;border-radius:50%;box-shadow:inset 0 0 0 12px #86efac11,0 0 25px #86efac22; }
    .title-style-nature::after { width:70px;height:2px;right:10px;top:58px;background:#86efac66;transform:rotate(-45deg); }
    .title-style-skull::before { content:"☠";right:12px;top:7px;font-size:65px;color:#f472b655;filter:drop-shadow(0 0 12px #f472b8); }
    .title-style-skull::after { left:0;right:0;bottom:0;height:2px;background:#f472b866;box-shadow:0 -8px 0 #f472b822,0 -16px 0 #f472b811; }
    .title-style-diamond::before { width:58px;height:58px;right:20px;top:25px;border:3px solid #93c5fd88;transform:rotate(45deg);box-shadow:0 0 25px #93c5fd55; }
    .title-style-diamond::after { width:28px;height:28px;right:35px;top:40px;background:#93c5fd22;transform:rotate(45deg); }
    .title-style-crystal::before { width:45px;height:70px;right:24px;top:17px;background:linear-gradient(135deg,#a78bfa55,transparent);clip-path:polygon(50% 0,100% 25%,75% 100%,25% 100%,0 25%); }
    .title-style-crystal::after { width:2px;height:78px;right:46px;top:13px;background:#fff8;transform:rotate(20deg); }
    .title-style-ufo::before { width:86px;height:32px;right:3px;top:35px;border:3px solid #e879f966;border-radius:50%;box-shadow:0 0 20px #e879f955; }
    .title-style-ufo::after { width:34px;height:18px;right:29px;top:27px;border:2px solid #f0abfc55;border-radius:50% 50% 35% 35%; }
    .title-style-comet::before { width:105px;height:14px;right:-4px;top:34px;border-radius:50%;background:linear-gradient(90deg,transparent,#fef08a44,#fff);transform:rotate(-22deg);filter:blur(1px); }
    .title-style-comet::after { width:20px;height:20px;border-radius:50%;right:20px;top:28px;background:#fff;box-shadow:0 0 22px 7px #fef08a77; }
    .title-style-gem::before { width:52px;height:52px;right:21px;top:25px;border:4px solid #fcd34d77;transform:rotate(45deg) skew(8deg,8deg);box-shadow:0 0 24px #fcd34d55; }
    .title-style-gem::after { left:0;right:0;top:0;height:4px;background:linear-gradient(90deg,#fcd34d,transparent,#fcd34d); }
    .title-style-shop::before { content:"▣";right:16px;top:8px;font-size:62px;color:#5eead455; }
    .title-style-shop::after { left:10px;right:10px;bottom:12px;height:10px;border-top:2px solid #5eead466;border-bottom:2px solid #5eead466; }
    .title-style-shield::before { width:60px;height:70px;right:18px;top:18px;border:3px solid #f8717188;clip-path:polygon(50% 0,90% 18%,82% 72%,50% 100%,18% 72%,10% 18%);box-shadow:0 0 20px #f8717155; }
    .title-style-shield::after { content:"✦";right:37px;top:36px;font-size:22px;color:#fff8; }
    .title-style-pointcoin::before { width:58px;height:58px;right:18px;top:22px;border:5px double #fde04788;border-radius:50%;box-shadow:0 0 24px #fde04755; }
    .title-style-pointcoin::after { content:"P";right:37px;top:31px;font-size:25px;font-weight:900;color:#fff9; }
    .title-style-pointgem::before { width:52px;height:62px;right:21px;top:18px;background:linear-gradient(135deg,#67e8f955,#0891b055);clip-path:polygon(50% 0,100% 28%,78% 100%,22% 100%,0 28%);box-shadow:0 0 24px #67e8f855; }
    .title-style-pointgem::after { width:2px;height:54px;right:47px;top:22px;background:#fff9;transform:rotate(25deg); }
    .title-style-crithunter::before { width:72px;height:72px;right:10px;top:14px;border:2px solid #fb718866;border-radius:50%;box-shadow:0 0 0 8px #fb718822,0 0 0 16px #fb718811; }
    .title-style-crithunter::after { content:"✦";right:35px;top:31px;font-size:28px;color:#fff;transform:rotate(15deg);text-shadow:0 0 16px #fb7188; }
    hr { border-color:rgba(255,255,255,.10) !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. 메인 레이아웃
# -----------------------------------------------------------------------------
left_col, right_col = st.columns([2.4, 7.6], gap="medium")

with left_col:
  if not st.session_state.is_rebirth and st.session_state.level >= 35:
    st.markdown(
        "<div"
        " style='background:rgba(220,38,38,0.2);border:2px solid"
        " #ef4444;padding:12px;border-radius:8px;text-align:center;margin-bottom:12px;'>"
        "<h3 style='color:#f87171; margin:0 0 6px 0;'>🌌 차원 한계 도달</h3>"
        "<p style='font-size:13px; color:#f1f5f9; margin:0 0 10px"
        " 0;'>최고 35단계에 도달했습니다!<br>새로운 차원으로 <b>환생(시즌2)</b>하시겠습니까?</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    if st.button("✨ 환생하기", use_container_width=True):
      trigger_rebirth()
      st.rerun()
    st.markdown(
        "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )

  mode_title = (
      "🌀 [시즌 2] 얼티밋 자이온의 시작"
      if st.session_state.is_rebirth
      else "🌌 [시즌 1] 지온의 탄생과 시초"
  )
  st.markdown(
      f"<h4 style='margin:0 0 8px 0; font-size: 15px;"
      f" color:#fde68a;'>{mode_title}</h4>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  s_col1, s_col2 = st.columns(2)

  with s_col1:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>💳 보유 금액</div><div style='font-size:14px;"
        f" font-weight:800; color:#ffffff;'>{format_gold(st.session_state.money)}</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>💧 눈물</div><div style='font-size:15px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.tears} /"
        " 60개</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>⭐ 포인트</div><div style='font-size:15px;"
        f" font-weight:800; color:#facc15;'>{st.session_state.points:,}P</div>"
        f"<div style='font-size:10px; color:#cbd5e1;'>다음 성공: +{get_enhance_point_reward(min(st.session_state.level + 1, 35 if not st.session_state.is_rebirth else 25)):,}P</div></div>",
        unsafe_allow_html=True,
    )

  with s_col2:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>🛡️ 방지권</div><div style='font-size:15px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.shield} /"
        " 3개</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")

    pity_left = PITY_MAX - st.session_state.pity_count
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>✨ 지온이의 가오</div><div style='font-size:13px;"
        f" font-weight:800; color:#ffffff;'>실패까지 <b>{pity_left}회</b></div></div>",
        unsafe_allow_html=True,
    )

  st.markdown(
      "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  curr_lvl = st.session_state.level
  current_prob = PROB_TABLE[st.session_state.is_rebirth]
  sp, down_p, dp, hold_p = current_prob.get(curr_lvl, (5.0, 40.0, 50.0, 5.0))
  st.markdown(
      f"<h4 style='margin:0 0 4px 0; font-size: 14px; color:#fde68a;'>📊 현재"
      f" 강화 확률 ({curr_lvl}단계)</h4>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<div style='font-size:12px; color:#cbd5e1;"
      f" background:rgba(255,255,255,0.05); padding:8px; border-radius:6px;'>•"
      f" 성공 확률: <b style='color:#38bdf8;'>{sp}%</b> (크리티컬 5%)<br>•"
      f" 하락 확률: <b style='color:#facc15;'>{down_p}%</b><br>• 파괴 확률: <b"
      f" style='color:#ef4444;'>{dp}%</b><br>• 유지 확률: <b"
      f" style='color:#94a3b8;'>{hold_p}%</b></div>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  # ---------------------------------------------------------------------------
  # 🛒 상점 / 💧 눈물 / 🏆 업적
  # 각각 버튼을 누르면 큰 전체 화면형 대화창으로 표시
  # ---------------------------------------------------------------------------
  @st.dialog("🛒 상점", width="large")
  def show_shop():
    st.markdown(
        """
        <div style="
            padding:14px;
            border-radius:18px;
            background:linear-gradient(135deg,rgba(250,204,21,.12),rgba(15,23,42,.78));
            border:1px solid rgba(250,204,21,.25);
            margin-bottom:12px;
        ">
            <div style="font-size:18px;font-weight:900;color:#fde68a;">
                🛒 상점
            </div>
            <div style="font-size:12px;color:#94a3b8;margin-top:4px;">
                방지권과 워프권을 💰 돈 또는 ⭐ 포인트로 구매할 수 있습니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    money_col, point_col = st.columns(2)
    
    with money_col:
      st.markdown(
          f"""
          <div style="text-align:center;padding:10px;border-radius:14px;
          background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10);">
              <div style="font-size:11px;color:#94a3b8;">💰 보유 금액</div>
              <div style="font-size:17px;font-weight:900;color:#fde68a;">
                  {format_gold(st.session_state.money)}
              </div>
          </div>
          """,
          unsafe_allow_html=True,
      )
    
    with point_col:
      st.markdown(
          f"""
          <div style="text-align:center;padding:10px;border-radius:14px;
          background:rgba(255,255,255,.05);border:1px solid rgba(250,204,21,.20);">
              <div style="font-size:11px;color:#94a3b8;">⭐ 보유 포인트</div>
              <div style="font-size:17px;font-weight:900;color:#facc15;">
                  {st.session_state.points:,}P
              </div>
          </div>
          """,
          unsafe_allow_html=True,
      )
    
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    
    # -----------------------------------------------------------------------
    # 🛡️ 방지권
    # -----------------------------------------------------------------------
    st.markdown(
        """
        <div style="
            padding:12px;
            border-radius:16px;
            background:linear-gradient(135deg,rgba(59,130,246,.12),rgba(15,23,42,.80));
            border:1px solid rgba(96,165,250,.25);
        ">
            <div style="font-size:16px;font-weight:900;color:#60a5fa;">
                🛡️ 파괴 방지권
            </div>
            <div style="font-size:11px;color:#94a3b8;margin-top:4px;">
                강화 파괴 확률에 당첨되었을 때 파괴를 한 번 막아줍니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    min_shield_level = 16 if st.session_state.is_rebirth else 20
    
    if st.session_state.is_rebirth:
      shield_money_cost = int(
          SMELL_DB[True][st.session_state.level]["price"] / 5
      )
    else:
      shield_money_cost = get_shield_cost(
          st.session_state.level,
          st.session_state.is_rebirth,
      )
    
    shield_point_cost = get_shield_point_cost(
        st.session_state.level,
        st.session_state.is_rebirth,
    )
    
    st.markdown(
        f"""
        <div style="font-size:12px;color:#cbd5e1;margin:9px 0;">
            <b>보유:</b> <span style="color:#60a5fa;font-weight:900;">
            {st.session_state.shield} / 3개</span><br>
            <b>구매 가능 단계:</b> {min_shield_level}단계 이상<br>
            <b>💰 돈 가격:</b> <span style="color:#fde68a;font-weight:900;">
            {format_gold(shield_money_cost)}</span><br>
            <b>⭐ 포인트 가격:</b> <span style="color:#facc15;font-weight:900;">
            {shield_point_cost:,}P</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    shield_money_col, shield_point_col = st.columns(2)
    
    with shield_money_col:
      can_buy_shield_money = (
          st.session_state.level >= min_shield_level
          and st.session_state.shield < 3
          and st.session_state.money >= shield_money_cost
      )
    
      if st.button(
          "💰 돈으로 구매",
          key="shop_shield_money",
          use_container_width=True,
          disabled=not can_buy_shield_money,
      ):
        if st.session_state.level < min_shield_level:
          st.warning(f"방지권은 {min_shield_level}단계 이상부터 구매 가능합니다.")
        elif st.session_state.shield >= 3:
          st.warning("방지권은 최대 3개까지 보유할 수 있습니다.")
        elif st.session_state.money < shield_money_cost:
          st.error("금액이 부족합니다.")
        else:
          st.session_state.money -= shield_money_cost
          st.session_state.shield += 1
          save_current_season_state()
          st.success("🛡️ 파괴 방지권 구매 완료!")
          st.rerun()
    
    with shield_point_col:
      can_buy_shield_point = (
          st.session_state.level >= min_shield_level
          and st.session_state.shield < 3
          and st.session_state.points >= shield_point_cost
      )
    
      if st.button(
          "⭐ 포인트로 구매",
          key="shop_shield_point",
          use_container_width=True,
          disabled=not can_buy_shield_point,
      ):
        if st.session_state.level < min_shield_level:
          st.warning(f"방지권은 {min_shield_level}단계 이상부터 구매 가능합니다.")
        elif st.session_state.shield >= 3:
          st.warning("방지권은 최대 3개까지 보유할 수 있습니다.")
        elif st.session_state.points < shield_point_cost:
          st.error(f"포인트가 부족합니다! (필요: {shield_point_cost:,}P)")
        else:
          st.session_state.points -= shield_point_cost
          st.session_state.points_spent_total += shield_point_cost
          st.session_state.shield += 1
          save_current_season_state()
          st.success(f"⭐ 방지권 구매 완료! (-{shield_point_cost:,}P)")
          st.rerun()
    
    st.markdown(
        "<hr style='margin:16px 0;border-color:rgba(255,255,255,.10);'>",
        unsafe_allow_html=True,
    )
    
    # -----------------------------------------------------------------------
    # 🚀 워프권
    # -----------------------------------------------------------------------
    st.markdown(
        """
        <div style="
            padding:12px;
            border-radius:16px;
            background:linear-gradient(135deg,rgba(168,85,247,.12),rgba(15,23,42,.80));
            border:1px solid rgba(168,85,247,.25);
        ">
            <div style="font-size:16px;font-weight:900;color:#c084fc;">
                🚀 워프권
            </div>
            <div style="font-size:11px;color:#94a3b8;margin-top:4px;">
                이미 도달했던 단계로 즉시 이동합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    warp_levels = (
        [5, 10, 15, 20]
        if st.session_state.is_rebirth
        else [10, 15, 20, 25, 30]
    )
    
    for w_level in warp_levels:
      if not st.session_state.is_rebirth:
        is_unlocked = (
            st.session_state.unlocked_warps.get(w_level, False)
            or st.session_state.max_level >= w_level
        )
      else:
        is_unlocked = (
            st.session_state.unlocked_season2_warps.get(w_level, False)
            or st.session_state.max_level >= w_level
        )
    
      warp_point_cost = get_warp_point_cost(w_level)
      warp_money_cost = get_warp_money_cost(
          w_level,
          st.session_state.is_rebirth,
      )
    
      st.markdown(
          f"""
          <div style="
              margin-top:9px;
              padding:11px 12px;
              border-radius:14px;
              background:rgba(255,255,255,.045);
              border:1px solid rgba(255,255,255,.10);
          ">
              <div style="font-size:14px;font-weight:900;">
                  🚀 {w_level}강 워프권
              </div>
              <div style="font-size:11px;color:#cbd5e1;margin-top:4px;">
                  💰 {format_gold(warp_money_cost)}
                  &nbsp;&nbsp;|&nbsp;&nbsp;
                  ⭐ {warp_point_cost:,}P
              </div>
              <div style="
                  font-size:10px;
                  margin-top:3px;
                  color:{'#4ade80' if is_unlocked else '#ef4444'};
              ">
                  {'구매 가능' if is_unlocked else f'{w_level}단계 도달 후 구매 가능'}
              </div>
          </div>
          """,
          unsafe_allow_html=True,
      )
    
      warp_money_col, warp_point_col = st.columns(2)
    
      # 워프권 - 돈으로 구매
      with warp_money_col:
        can_buy_warp_money = (
            is_unlocked
            and st.session_state.level < w_level
            and st.session_state.money >= warp_money_cost
        )
    
        if st.button(
            "💰 돈으로 구매",
            key=f"shop_warp_money_{st.session_state.is_rebirth}_{w_level}",
            use_container_width=True,
            disabled=not can_buy_warp_money,
        ):
          if not is_unlocked:
            st.warning(f"아직 {w_level}단계에 도달한 적이 없습니다!")
          elif st.session_state.level >= w_level:
            st.warning(f"현재 단계가 이미 {w_level}단계 이상입니다.")
          elif st.session_state.money < warp_money_cost:
            st.error(f"금액이 부족합니다! (필요: {format_gold(warp_money_cost)})")
          else:
            st.session_state.money -= warp_money_cost
            st.session_state.warp_uses += 1
            st.session_state.prev_level = st.session_state.level
            st.session_state.level = w_level
            if w_level > st.session_state.max_level:
              st.session_state.max_level = w_level
            st.session_state.status = "SUCCESS"
            save_current_season_state()
            check_achievements()
            st.success(f"🚀 {w_level}단계로 워프 성공!")
            st.rerun()
    
      # 워프권 - 포인트로 구매
      with warp_point_col:
        can_buy_warp_point = (
            is_unlocked
            and st.session_state.level < w_level
            and st.session_state.points >= warp_point_cost
        )
    
        if st.button(
            "⭐ 포인트로 구매",
            key=f"shop_warp_point_{st.session_state.is_rebirth}_{w_level}",
            use_container_width=True,
            disabled=not can_buy_warp_point,
        ):
          if not is_unlocked:
            st.warning(f"아직 {w_level}단계에 도달한 적이 없습니다!")
          elif st.session_state.level >= w_level:
            st.warning(f"현재 단계가 이미 {w_level}단계 이상입니다.")
          elif st.session_state.points < warp_point_cost:
            st.error(f"포인트가 부족합니다! (필요: {warp_point_cost:,}P)")
          else:
            st.session_state.points -= warp_point_cost
            st.session_state.points_spent_total += warp_point_cost
            st.session_state.warp_uses += 1
            st.session_state.prev_level = st.session_state.level
            st.session_state.level = w_level
            if w_level > st.session_state.max_level:
              st.session_state.max_level = w_level
            st.session_state.status = "SUCCESS"
            save_current_season_state()
            check_achievements()
            st.success(f"🚀 {w_level}단계로 워프 성공! (-{warp_point_cost:,}P)")
            st.rerun()
    
      # ---------------------------------------------------------------------------
      # 💧 눈물
      # ---------------------------------------------------------------------------

  @st.dialog("💧 눈물", width="large")
  def show_tears():
    max_lvl = 25 if st.session_state.is_rebirth else 35
    limit_lvl = 18 if st.session_state.is_rebirth else 32
    
    if st.session_state.level >= limit_lvl:
      st.markdown(
          "<div style='font-size:13px;color:#ef4444;font-weight:700;margin-bottom:8px;'>"
          "⚠️ 고단계부터는 눈물을 사용할 수 없습니다!</div>",
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          f"<div style='font-size:13px;color:#cbd5e1;margin-bottom:8px;'>"
          f"<b>효과:</b> 눈물 20개 소모 (100% 확률로 1~3단계 상승)<br>"
          f"<b>현재보유:</b> <span style='font-weight:bold;color:#38bdf8;'>"
          f"{st.session_state.tears} / 60개</span></div>",
          unsafe_allow_html=True,
      )
    
    can_use_tears = st.session_state.level < limit_lvl
    
    if st.button(
        "눈물 기적 가동",
        use_container_width=True,
        disabled=not can_use_tears,
    ):
      if st.session_state.level >= limit_lvl:
        st.warning("고단계부터는 눈물을 사용할 수 없습니다.")
      elif st.session_state.tears >= 20:
        st.session_state.tears -= 20
        add_lvl = random.choice([1, 2, 3])
        st.session_state.prev_level = st.session_state.level
        st.session_state.level = min(
            max_lvl,
            st.session_state.level + add_lvl,
        )
        st.session_state.status = "CRITICAL" if add_lvl >= 2 else "SUCCESS"
        save_current_season_state()
        st.success(f"눈물 기적 100% 성공! {add_lvl}단계 상승!")
        st.rerun()
      else:
        st.error("눈물 20개가 필요합니다.")

  @st.dialog("🏆 업적", width="large")
  def show_achievements():
    achieved = sum(st.session_state.achievements.values())
    pct = int((achieved / len(ACHIEVEMENTS)) * 100) if ACHIEVEMENTS else 0
    st.markdown(f"**업적 진행도:** {achieved} / {len(ACHIEVEMENTS)} · {pct}%")
    st.progress(pct / 100)
    achievement_items = list(ACHIEVEMENTS.items())
    ach_cols = st.columns(3)
    for i, (key, info) in enumerate(achievement_items):
      done = st.session_state.achievements.get(key, False)
      icon = "✅" if done else "🔒"
      accent, accent2, deep, title_icon = get_title_theme(info["title"])
      title_style = get_title_style(info["title"])
      bg = (f"linear-gradient(135deg,{deep},{accent2}55,#020617)" if done
            else "linear-gradient(135deg,rgba(15,23,42,.96),rgba(2,6,23,.99))")
      border = accent if done else "rgba(148,163,184,.22)"
      with ach_cols[i % 3]:
        st.markdown(
            f"<div class='title-design {title_style}' style='background:{bg};border:1px solid {border};"
            f"box-shadow:0 0 22px {accent}25;border-radius:16px;padding:13px;"
            f"margin:0 0 10px 0;min-height:116px;'>"
            f"<div style='font-size:10px;letter-spacing:1.5px;color:{accent if done else '#64748b'}'>"
            f"{('UNLOCKED' if done else 'LOCKED')}</div>"
            f"<div style='font-size:15px;font-weight:900;margin-top:5px'>{icon} {info['name']}</div>"
            f"<div style='font-size:12px;color:#cbd5e1;margin-top:6px'>{info['desc']}</div>"
            f"<div style='font-size:11px;color:{accent};margin-top:8px;font-weight:800'>🏷️ {info['title']}</div>"
            f"<div style='font-size:10px;color:#fde68a;margin-top:2px'>💰 {format_gold(info['reward'])}</div></div>",
            unsafe_allow_html=True,
        )
    options = [TITLE_DEFAULT] + st.session_state.unlocked_titles
    if st.session_state.selected_title not in options:
      st.session_state.selected_title = TITLE_DEFAULT
    selected = st.selectbox(
        "현재 칭호", options, index=options.index(st.session_state.selected_title),
    )
    st.session_state.selected_title = selected


  menu_shop, menu_tears, menu_ach = st.columns(3)
  with menu_shop:
    if st.button("🛒 상점", key="open_shop", use_container_width=True):
      show_shop()
  with menu_tears:
    if st.button("💧 눈물", key="open_tears", use_container_width=True):
      show_tears()
  with menu_ach:
    if st.button("🏆 업적", key="open_achievements", use_container_width=True):
      show_achievements()


  st.markdown(
      "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🌌 지온"
      " 강화 제어</h4>",
      unsafe_allow_html=True,
  )

  max_lvl = 25 if st.session_state.is_rebirth else 35
  action_enhance, action_sell = st.columns(2, gap="small")
  with action_enhance:
    if st.button("🔥 강화하기", use_container_width=True, disabled=(st.session_state.level >= max_lvl)):
      cost = get_enhance_cost(st.session_state.level, st.session_state.is_rebirth)
      if st.session_state.money < cost:
        st.error("강화 비용 부족!")
      else:
        st.session_state.enhance_attempts += 1
        run_enhance()
        check_achievements()
        save_current_season_state()
        st.rerun()
  with action_sell:
    sell_price = SMELL_DB[st.session_state.is_rebirth][st.session_state.level]["price"]
    if st.button(f"💰 판매하기  +{format_gold(sell_price)}", use_container_width=True, disabled=(st.session_state.level == 0)):
      sell()
      unlock_achievement("seller")
      check_achievements()
      st.rerun()

with right_col:
  current_level = st.session_state.level
  prev_level = getattr(st.session_state, "prev_level", current_level)
  max_lvl = 25 if st.session_state.is_rebirth else 35
  curr_data = SMELL_DB[st.session_state.is_rebirth][current_level]
  card_color = curr_data["color"]
  card_title = curr_data["name"]
  card_desc = curr_data["desc"]
  card_price = format_gold(curr_data["price"])
  current_cost = format_gold(
      get_enhance_cost(current_level, st.session_state.is_rebirth)
  )
  current_point_reward = get_enhance_point_reward(current_level)
  tier = curr_data["tier"]
  status = st.session_state.status

  # 마지막 강화 시도 여부 판별 (S1: 34->35 혹은 S1 35성공, S2: 24->25 혹은 S2 25성공)
  target_last_lvl = max_lvl - 1
  is_last_attempt = (
      prev_level == target_last_lvl
      and status
      in ["SUCCESS", "CRITICAL", "PITY_SUCCESS", "FAILED", "DESTROYED", "HOLD"]
  ) or (
      current_level == max_lvl
      and status in ["SUCCESS", "CRITICAL", "PITY_SUCCESS"]
  )

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

            .selected-title-ui {{
                 position: absolute;
                 top: 18px;
                 left: 50%;
                 transform: translateX(-50%);
                 z-index: 120;
                 pointer-events: none;
                 width: min(380px, 82vw);
                 min-height: 82px;
                 box-sizing: border-box;
                 padding: 13px 18px;
                 border-radius: 16px;
                 overflow: hidden;
                 text-align: left;
                 font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                 box-shadow: inset 0 1px rgba(255,255,255,.14), 0 12px 30px rgba(0,0,0,.35);
             }}
             .selected-title-ui::before, .selected-title-ui::after {{
                 content: "";
                 position: absolute;
                 pointer-events: none;
             }}
             .selected-title-label {{
                 position: relative;
                 z-index: 2;
                 font-size: 9px;
                 letter-spacing: 1.8px;
                 font-weight: 800;
                 opacity: .72;
                 margin-bottom: 5px;
             }}
             .selected-title-name {{
                 position: relative;
                 z-index: 2;
                 font-size: 21px;
                 line-height: 1.25;
                 font-weight: 900;
                 white-space: nowrap;
                 overflow: hidden;
                 text-overflow: ellipsis;
                 text-shadow: 0 0 12px currentColor, 0 2px 5px rgba(0,0,0,.9);
             }}

            .cinematic-ui {{
                position: absolute;
                bottom: 25px; 
                left: 50%;
                transform: translateX(-50%);
                width: 100%;
                text-align: center;
                z-index: 100;
                pointer-events: none;
                opacity: 1;
                transition: opacity 0.3s ease-in-out;
            }}

            .title-tier-1 {{ font-size: 28px; font-weight: 800; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
            .title-tier-2 {{ font-size: 32px; font-weight: 800; color: #f59e0b; text-shadow: 0 0 22px #f59e0b; }}
            .title-tier-3 {{ font-size: 36px; font-weight: 800; color: #ef4444; text-shadow: 0 0 25px #ef4444; }}
            .title-tier-4 {{ font-size: 40px; font-weight: 800; color: #c084fc; text-shadow: 0 0 28px #c084fc; }}
            .title-tier-5 {{ font-size: 44px; font-weight: 800; background: linear-gradient(90deg, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 12px rgba(255,126,95,0.6)); }}
            .title-tier-6 {{ font-size: 48px; font-weight: 800; background: linear-gradient(90deg, #ffffff, #fde68a, #c084fc, #f43f5e); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: rainbow 1.5s linear infinite; filter: drop-shadow(0 0 15px rgba(255,255,255,0.8)); }}

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

            .status-header {{ font-size: 20px; font-weight: 800; margin-bottom: 5px; letter-spacing: 1px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
            .desc-text {{ font-size: 17px; color: #cbd5e1; margin-top: 4px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); font-weight: 600; }}
            .price-text {{ font-size: 19px; font-weight: 800; color: #fbbf24; margin-top: 5px; text-shadow: 0 0 15px rgba(0,0,0,0.95); }}
            .point-text {{ font-size: 17px; font-weight: 800; color: #67e8f9; margin-top: 5px; text-shadow: 0 0 14px rgba(0,0,0,0.95); letter-spacing: .2px; }}
            .cost-text {{ font-size: 16px; font-weight: 700; color: #f87171; margin-top: 4px; text-shadow: 0 0 12px rgba(0,0,0,0.95); }}

            /* 연출용 찰나의 화면 비치는 광원 덮개 */
            #flashOverlay {{
                position: absolute;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: white;
                opacity: 0;
                pointer-events: none;
                z-index: 200;
                transition: opacity 0.15s ease-out;
            }}
        .stats-header {{
            font-family: inherit;
            font-size: 22px;
            font-weight: 900;
            letter-spacing: 1.2px;
            color: #f8fafc;
            text-shadow: 0 2px 12px rgba(0,0,0,.9);
            margin: 2px 0 2px;
        }}
        .stats-header-icon {{
            display:inline-block;
            margin-right:7px;
            filter: drop-shadow(0 0 8px rgba(250,204,21,.35));
        }}
        .stats-subtitle {{
            font-family: inherit;
            font-size: 12px;
            font-weight: 700;
            color: #94a3b8;
            letter-spacing: .35px;
            margin-bottom: 12px;
        }}
        .stats-card {{
            font-family: inherit;
            min-height: 108px;
            margin-bottom: 12px;
            padding: 13px 14px;
            border: 1px solid rgba(148,163,184,.18);
            border-radius: 15px;
            background: linear-gradient(145deg, rgba(30,41,59,.78), rgba(2,6,23,.9));
            box-shadow: inset 0 1px rgba(255,255,255,.06), 0 8px 22px rgba(0,0,0,.18);
        }}
        .stats-card-top {{ display:flex; align-items:center; justify-content:space-between; }}
        .stats-icon {{ font-size: 19px; line-height:1; }}
        .stats-small {{ font-size: 9px; font-weight: 800; letter-spacing: 1px; color:#64748b; }}
        .stats-label {{ margin-top: 10px; font-size: 12px; font-weight: 800; color:#cbd5e1; }}
        .stats-value {{ margin-top: 2px; font-size: 23px; font-weight: 900; letter-spacing:.2px; color:#f8fafc; text-shadow:0 0 12px rgba(255,255,255,.08); }}
        .stats-points-panel {{
            font-family: inherit;
            margin-top: 3px; padding: 14px 15px; border-radius: 15px;
            border: 1px solid rgba(250,204,21,.20);
            background: linear-gradient(135deg, rgba(250,204,21,.07), rgba(15,23,42,.78));
            box-shadow: inset 0 1px rgba(255,255,255,.05), 0 8px 22px rgba(0,0,0,.16);
        }}
        .stats-points-title {{ font-size: 11px; font-weight: 900; letter-spacing: 1.2px; color:#facc15; margin-bottom:10px; }}
        .stats-points-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }}
        .stats-points-grid div {{ display:flex; flex-direction:column; gap:3px; }}
        .stats-points-grid span {{ font-size:10px; font-weight:700; color:#94a3b8; }}
        .stats-points-grid b {{ font-size:15px; font-weight:900; color:#fde68a; }}
        @media (max-width: 700px) {{ .stats-points-grid {{ grid-template-columns:1fr; }} }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="container"></div>
        <div id="flashOverlay"></div>
        <div class="selected-title-ui title-design {get_title_style(st.session_state.selected_title)}" style="background:linear-gradient(135deg,{get_title_theme(st.session_state.selected_title)[2]},{get_title_theme(st.session_state.selected_title)[1]}88,#020617);border:1px solid {get_title_theme(st.session_state.selected_title)[0]};box-shadow:0 0 22px {get_title_theme(st.session_state.selected_title)[0]}35,inset 0 1px rgba(255,255,255,.12);">
            <div class="selected-title-label" style="color:{get_title_theme(st.session_state.selected_title)[0]};">EQUIPPED TITLE</div>
            <div class="selected-title-name" style="color:{get_title_theme(st.session_state.selected_title)[0]};">{get_title_theme(st.session_state.selected_title)[3]} {st.session_state.selected_title}</div>
        </div>

        <div id="cinematicUi" class="cinematic-ui visible">
            <div id="statusText" class="status-header">READY</div>
            <div id="mainTitle" class="title-tier-{tier}">{card_title}</div>
            <div id="descText" class="desc-text">"{card_desc}"</div>
            <div id="priceText" class="price-text">예상 가치: {card_price}</div>
            <div id="pointText" class="point-text">획득 포인트: {current_point_reward:,}P</div>
            <div id="costText" class="cost-text">필요 강화 비용: {current_cost}</div>
        </div>

        <script>
            const currentLevel = {current_level};
            const maxLvl = {max_lvl};
            const isRebirth = {"true" if st.session_state.is_rebirth else "false"};
            const status = "{status}";
            const isLastAttempt = {"true" if is_last_attempt else "false"};
            const isFinalSuccess = (currentLevel === maxLvl && (status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS"));

            if (currentLevel >= 15 || isFinalSuccess) {{
                document.getElementById('mainTitle').classList.add('shaking-text');
                document.getElementById('descText').classList.add('shaking-text');
                document.getElementById('priceText').classList.add('shaking-text');
                document.getElementById('pointText').classList.add('shaking-text');
                document.getElementById('costText').classList.add('shaking-text');
            }}

            const statusText = document.getElementById('statusText');
            const cinematicUi = document.getElementById('cinematicUi');
            const flashOverlay = document.getElementById('flashOverlay');
            const tierColor = "{card_color}";
            let statusColor = "#38bdf8";
            let particleSize = 0.25;
            let particleSpeed = 0.6;
            let glowIntensity = 12;

            function applyStatusText() {{
                if (isFinalSuccess) {{
                    statusText.innerText = isRebirth ? "🌀👑 [ULTIMATE TRUE REBIRTH ZION] 시즌 2 최종 성공!! 👑🌀" : "🌌👑 [ULTIMATE GOD ABSOLUTE ZION] 시즌 1 최종 강화 성공!! 👑🌌";
                    statusColor = "#ffffff";
                    particleSize = 0.6;
                    particleSpeed = 2.5;
                    glowIntensity = 50;
                }} else if (status === "CRITICAL") {{
                    statusText.innerText = "⚡ COSMIC CRITICAL HIT!! (+2단계 이상 대성공) ⚡";
                    statusColor = "#ffffff"; 
                    particleSize = 0.35;
                    particleSpeed = 1.2;
                    glowIntensity = 22;
                }} else if (status === "PITY_SUCCESS") {{
                    statusText.innerText = "✨ 지온이의 가오 발동! (천장 100% 성공) ✨";
                    statusColor = "#fde68a";
                    particleSize = 0.3;
                    particleSpeed = 1.0;
                    glowIntensity = 20;
                }} else if (status === "SUCCESS") {{
                    statusText.innerText = "✨ COSMIC SUCCESS (강화 성공) ✨";
                    statusColor = tierColor;
                    particleSize = 0.28;
                    particleSpeed = 0.8;
                    glowIntensity = 16;
                }} else if (status === "SHIELD_SAVED") {{
                    statusText.innerText = "🛡️ SHIELD PROTECTED! (우주 방어 발동) 🛡️";
                    statusColor = "#60a5fa";
                }} else if (status === "DESTROYED") {{
                    statusText.innerText = "💥 BLACKHOLE CATACLYSM DESTROYED (코어 대폭발 붕괴됨!) 💥";
                    statusColor = "#ff0000";
                    particleSpeed = 2.0;
                }} else if (status === "FAILED") {{
                    statusText.innerText = "🔻 FAILED (에너지 하락) 🔻";
                    statusColor = "#64748b";
                    particleSpeed = 0.3;
                    glowIntensity = 5;
                }} else if (status === "HOLD") {{
                    statusText.innerText = "🔒 HOLD (에너지 동결) 🔒";
                    statusColor = "#94a3b8";
                    particleSpeed = 0.4;
                }} else {{
                    statusText.innerText = isRebirth ? "REBIRTH READY - 블랙홀 차원 에너지가 집결합니다" : "READY - 우주 에너지가 차분히 집중됩니다";
                }}
                statusText.style.color = statusColor;
            }}

            applyStatusText();

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0.6, 10.0);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            renderer.shadowMap.enabled = true;
            document.getElementById('container').appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xffffff, isFinalSuccess ? 2.0 : 0.8);
            scene.add(ambientLight);

            const mainLight = new THREE.DirectionalLight(0xffffff, isFinalSuccess ? 4.0 : 2.0);
            mainLight.position.set(5, 8, 5);
            scene.add(mainLight);

            const pointLight = new THREE.PointLight(statusColor, glowIntensity, isFinalSuccess ? 60 : 40);
            pointLight.position.set(0, 0, 3);
            scene.add(pointLight);

            const starCount = 1000;
            const starGeo = new THREE.BufferGeometry();
            const starPositions = new Float32Array(starCount * 3);
            for(let i=0; i<starCount; i++) {{
                starPositions[i*3] = (Math.random() - 0.5) * 40;
                starPositions[i*3 + 1] = (Math.random() - 0.5) * 40;
                starPositions[i*3 + 2] = (Math.random() - 0.5) * 40 - 10;
            }}
            starGeo.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
            const starMat = new THREE.PointsMaterial({{
                color: isFinalSuccess ? 0xffd700 : (isRebirth ? 0x00f0ff : 0xffffff),
                size: isFinalSuccess ? 0.12 : 0.07,
                transparent: true,
                opacity: 0.7,
                blending: THREE.AdditiveBlending
            }});
            const starField = new THREE.Points(starGeo, starMat);
            scene.add(starField);

            const particleCount = isFinalSuccess ? 2000 : 500;
            const particleGeo = new THREE.BufferGeometry();
            const particlePositions = new Float32Array(particleCount * 3);
            const particleVelocities = [];

            for(let i=0; i<particleCount; i++) {{
                particlePositions[i*3] = (Math.random() - 0.5) * 6.0;
                particlePositions[i*3 + 1] = -4.0 + Math.random() * 2.0;
                particlePositions[i*3 + 2] = (Math.random() - 0.5) * 6.0;
                
                let spd = particleSpeed;
                if (status === "FAILED") spd = 0.2;

                particleVelocities.push({{
                    x: (Math.random() - 0.5) * 0.01 * spd,
                    y: (0.008 + Math.random() * 0.025) * spd,
                    z: (Math.random() - 0.5) * 0.01 * spd,
                }});
            }}
            particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
            
            const particleMat = new THREE.PointsMaterial({{
                color: new THREE.Color(statusColor),
                size: particleSize,
                transparent: true,
                opacity: status === "FAILED" ? 0.2 : 0.8,
                blending: THREE.AdditiveBlending,
                depthWrite: false
            }});
            const particleSystem = new THREE.Points(particleGeo, particleMat);
            scene.add(particleSystem);

            const objectGroup = new THREE.Group();
            objectGroup.position.y = -0.7;

            let baseGeo;
            const lvl = {current_level};

            if (isRebirth) {{
                if (lvl <= 3) {{
                    baseGeo = new THREE.OctahedronGeometry(2.3);
                }} else if (lvl <= 6) {{
                    baseGeo = new THREE.DodecahedronGeometry(2.2);
                }} else if (lvl <= 9) {{
                    baseGeo = new THREE.IcosahedronGeometry(2.3);
                }} else if (lvl <= 12) {{
                    baseGeo = new THREE.TorusGeometry(1.8, 0.6, 16, 32);
                }} else if (lvl <= 15) {{
                    baseGeo = new THREE.TorusKnotGeometry(1.4, 0.45, 64, 16, 3, 5);
                }} else if (lvl <= 18) {{
                    baseGeo = new THREE.ConeGeometry(2.2, 3.2, 7);
                }} else if (lvl <= 21) {{
                    baseGeo = new THREE.CylinderGeometry(1.5, 2.3, 3.0, 10);
                }} else if (lvl <= 24) {{
                    baseGeo = new THREE.IcosahedronGeometry(2.6, 2);
                }} else {{
                    baseGeo = new THREE.TorusKnotGeometry(2.1, 0.75, 128, 32, 4, 7);
                }}
            }} else {{
                if (lvl <= 2) {{
                    baseGeo = new THREE.TetrahedronGeometry(2.3);
                }} else if (lvl <= 5) {{
                    baseGeo = new THREE.BoxGeometry(2.1, 2.1, 2.1);
                }} else if (lvl <= 8) {{
                    baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 5);
                }} else if (lvl <= 11) {{
                    baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 6);
                }} else if (lvl <= 14) {{
                    baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 7);
                }} else if (lvl <= 17) {{
                    baseGeo = new THREE.CylinderGeometry(1.9, 1.9, 2.4, 8);
                }} else if (lvl == 18) {{
                    baseGeo = new THREE.OctahedronGeometry(2.5);
                }} else if (lvl == 19) {{
                    baseGeo = new THREE.DodecahedronGeometry(2.4);
                }} else if (lvl == 20) {{
                    baseGeo = new THREE.IcosahedronGeometry(2.4);
                }} else if (lvl == 21) {{
                    baseGeo = new THREE.ConeGeometry(2.1, 3.1, 6);
                }} else if (lvl == 22) {{
                    baseGeo = new THREE.TorusGeometry(1.7, 0.65, 16, 32);
                }} else if (lvl == 23) {{
                    baseGeo = new THREE.TorusKnotGeometry(1.4, 0.45, 64, 16, 2, 3);
                }} else if (lvl == 24) {{
                    baseGeo = new THREE.CylinderGeometry(0.5, 2.1, 2.9, 12);
                }} else if (lvl == 25) {{
                    baseGeo = new THREE.SphereGeometry(2.2, 16, 16);
                }} else if (lvl == 26) {{
                    baseGeo = new THREE.ConeGeometry(2.3, 3.3, 8);
                }} else if (lvl == 27) {{
                    baseGeo = new THREE.TorusKnotGeometry(1.5, 0.55, 96, 24, 3, 4);
                }} else if (lvl == 28) {{
                    baseGeo = new THREE.IcosahedronGeometry(2.5, 1);
                }} else if (lvl == 29) {{
                    baseGeo = new THREE.DodecahedronGeometry(2.6, 1);
                }} else if (lvl == 30) {{
                    baseGeo = new THREE.TorusKnotGeometry(1.5, 0.55, 128, 32, 2, 5);
                }} else if (lvl == 31) {{
                    baseGeo = new THREE.OctahedronGeometry(2.7, 2);
                }} else if (lvl == 32) {{
                    baseGeo = new THREE.IcosahedronGeometry(2.7, 2);
                }} else if (lvl == 33) {{
                    baseGeo = new THREE.TorusKnotGeometry(1.6, 0.6, 128, 32, 3, 5);
                }} else if (lvl == 34) {{
                    baseGeo = new THREE.SphereGeometry(2.8, 32, 32);
                }} else {{
                    baseGeo = new THREE.TorusKnotGeometry(2.2, 0.8, 200, 50, 5, 8);
                }}
            }}

            const outerMat = new THREE.MeshPhysicalMaterial({{
                color: tierColor,
                emissive: isFinalSuccess ? "#ffffff" : (status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? statusColor : "#111111"),
                emissiveIntensity: isFinalSuccess ? 1.5 : (status === "SUCCESS" ? 0.3 : (status === "CRITICAL" || status === "PITY_SUCCESS" ? 0.6 : 0.1)),
                metalness: 0.9,
                roughness: 0.1,
                transmission: 0.6,
                transparent: true,
                opacity: status === "FAILED" ? 0.5 : 0.95,
                wireframe: false
            }});
            const outerMesh = new THREE.Mesh(baseGeo, outerMat);
            objectGroup.add(outerMesh);

            const coreGeo = new THREE.SphereGeometry(isFinalSuccess ? 1.6 : 1.2, 32, 32);
            const coreMat = new THREE.MeshPhysicalMaterial({{
                color: 0xffffff,
                emissive: statusColor,
                emissiveIntensity: isFinalSuccess ? 5.0 : (status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? 2.0 : 0.8),
                roughness: 0.02,
                metalness: 0.95,
                transmission: 0.8
            }});
            const coreMesh = new THREE.Mesh(coreGeo, coreMat);
            objectGroup.add(coreMesh);

            scene.add(objectGroup);

            // -----------------------------------------------------------------
            // 애니메이션 연출 로직 (마지막 단계 강화 시 5초간 길고 화려한 시네마틱)
            // -----------------------------------------------------------------
            const mainTl = gsap.timeline();

            if (isLastAttempt) {{
                // UI 잠시 숨기기
                cinematicUi.style.opacity = "0";

                // 연출 초기화
                objectGroup.scale.set(0.5, 0.5, 0.5);
                pointLight.intensity = 5;

                // 5초간 화려한 진동, 카메라 서서히 줌인, 오브젝트 수퍼 스케일업 & 초고속 회전 연출
                mainTl.to(camera.position, {{
                    z: 4.2,
                    duration: 4.8,
                    ease: "power3.in"
                }}, 0);

                mainTl.to(objectGroup.scale, {{
                    x: 3.5, y: 3.5, z: 3.5,
                    duration: 4.8,
                    ease: "power3.in"
                }}, 0);

                mainTl.to(pointLight, {{
                    intensity: 200,
                    duration: 4.8,
                    ease: "power4.in"
                }}, 0);

                // 빛의 서라운드 라이트 컬러 왜곡 (무지개빛 색상 트랜지션)
                const colors = ["#ff0055", "#00ffff", "#ffaa00", "#7000ff", "#ffffff"];
                colors.forEach((col, idx) => {{
                    mainTl.to(pointLight.color, {{
                        r: new THREE.Color(col).r,
                        g: new THREE.Color(col).g,
                        b: new THREE.Color(col).b,
                        duration: 0.9,
                        ease: "linear"
                    }}, idx * 0.9);
                }});

                // 카메라 & 코어 가속 및 극적인 시공간 시각적 왜곡 진동
                const basePosY = -0.7;
                mainTl.to(objectGroup.position, {{
                    duration: 4.8,
                    onUpdate: function() {{
                        const p = this.progress(); // 0 ~ 1
                        const shake = Math.pow(p, 2) * 0.8; // 진행될수록 가속되는 진동 폭
                        objectGroup.position.x = (Math.random() - 0.5) * shake;
                        objectGroup.position.y = basePosY + (Math.random() - 0.5) * shake;
                        objectGroup.position.z = (Math.random() - 0.5) * shake;

                        // 회전 가속 연출
                        const speedMult = 1 + p * 15;
                        objectGroup.rotation.x += 0.05 * speedMult;
                        objectGroup.rotation.y += 0.08 * speedMult;
                        objectGroup.rotation.z += 0.03 * speedMult;
                    }}
                }}, 0);

                // 4.8초 시점에 극적인 화면 가득 차는 섬광 연출 (Flash explosion)
                mainTl.to(flashOverlay, {{
                    opacity: 1.0,
                    duration: 0.2,
                    ease: "power4.in",
                    onComplete: function() {{
                        cinematicUi.style.opacity = "1";
                        camera.position.set(0, 0.6, 10.0);
                        
                        // 결과 연출 (파괴 or 성공 or 실패)
                        triggerResultAnimation();
                    }}
                }}, 4.8);

                mainTl.to(flashOverlay, {{
                    opacity: 0,
                    duration: 1.0,
                    ease: "power2.out"
                }}, 5.0);

            }} else {{
                // 일반 단계 시도 시 즉시 결과 연출
                triggerResultAnimation();
            }}

            function triggerResultAnimation() {{
                const resultTl = gsap.timeline();

                if (status === "DESTROYED") {{
                    outerMesh.visible = false;
                    coreMesh.visible = false;

                    pointLight.color.set("#ff0000");
                    pointLight.intensity = 100;

                    const shardCount = 250;
                    const shards = [];
                    const shardGroup = new THREE.Group();
                    shardGroup.position.y = -0.7;

                    for(let i=0; i<shardCount; i++) {{
                        const sGeo = new THREE.BoxGeometry(0.2 + Math.random()*0.4, 0.2 + Math.random()*0.4, 0.2 + Math.random()*0.4);
                        const sMat = new THREE.MeshStandardMaterial({{
                            color: tierColor,
                            roughness: 0.1,
                            metalness: 0.9,
                            emissive: "#ff2200",
                            emissiveIntensity: 3.5
                        }});
                        const shard = new THREE.Mesh(sGeo, sMat);
                        shard.position.set(0, 0, 0);
                        
                        const u = Math.random();
                        const v = Math.random();
                        const theta = u * 2.0 * Math.PI;
                        const phi = Math.acos(2.0 * v - 1.0);
                        const speed = 6.0 + Math.random() * 12.0;
                        
                        shard.userData = {{
                            vx: speed * Math.sin(phi) * Math.cos(theta),
                            vy: speed * Math.sin(phi) * Math.sin(theta),
                            vz: speed * Math.cos(phi),
                            rx: (Math.random() - 0.5) * 40,
                            ry: (Math.random() - 0.5) * 40
                        }};

                        shardGroup.add(shard);
                        shards.push(shard);
                    }}
                    scene.add(shardGroup);

                    resultTl.to(shardGroup.position, {{
                        duration: 0.8,
                        ease: "power2.out",
                        onUpdate: function() {{
                            const progress = this.progress();
                            shards.forEach(s => {{
                                s.position.x += s.userData.vx * 0.02;
                                s.position.y += s.userData.vy * 0.02 - 0.03;
                                s.position.z += s.userData.vz * 0.02;
                                s.rotation.x += s.userData.rx * 0.02;
                                s.rotation.y += s.userData.ry * 0.02;
                                s.material.opacity = 1.0 - progress;
                                s.material.transparent = true;
                            }});
                        }}
                    }});
                }} else {{
                    const maxScale = isFinalSuccess ? 2.0 : 1.3;
                    resultTl.to(objectGroup.scale, {{
                        x: maxScale, y: maxScale, z: maxScale,
                        duration: 0.2,
                        ease: "back.out(2)"
                    }})
                    .to(objectGroup.scale, {{
                        x: 1.0, y: 1.0, z: 1.0,
                        duration: 0.25,
                        ease: "power2.out"
                    }});

                    const basePosY = -0.7;
                    resultTl.to(objectGroup.position, {{
                        duration: 0.35,
                        onUpdate: function() {{
                            const p = this.progress();
                            const shakeIntensity = (isFinalSuccess ? 0.45 : 0.12) * Math.sin(p * Math.PI);
                            objectGroup.position.x = (Math.random() - 0.5) * shakeIntensity;
                            objectGroup.position.y = basePosY + (Math.random() - 0.5) * shakeIntensity;
                            objectGroup.position.z = (Math.random() - 0.5) * shakeIntensity * 0.5;

                            objectGroup.rotation.x += (Math.random() - 0.5) * shakeIntensity;
                            objectGroup.rotation.y += (Math.random() - 0.5) * shakeIntensity;
                            objectGroup.rotation.z += (Math.random() - 0.5) * shakeIntensity;
                        }}
                    }}, 0);
                }}
            }}

            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();

                if (status !== "DESTROYED") {{
                    const rotSpeed = isFinalSuccess ? 2.2 : (status === "FAILED" ? 0.3 : (status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? 0.8 : 0.5));
                    outerMesh.rotation.x += 0.005 * rotSpeed;
                    outerMesh.rotation.y += 0.008 * rotSpeed;
                    coreMesh.rotation.x -= 0.01 * rotSpeed;
                    coreMesh.rotation.y -= 0.012 * rotSpeed;

                    if (isFinalSuccess) {{
                        objectGroup.rotation.z = Math.sin(time * 2.5) * 0.2;
                    }}
                }}

                starField.rotation.y = time * 0.01;

                const positions = particleGeo.attributes.position.array;
                for(let i=0; i<particleCount; i++) {{
                    positions[i*3] += particleVelocities[i].x;
                    positions[i*3 + 1] += particleVelocities[i].y;
                    positions[i*3 + 2] += particleVelocities[i].z;

                    if(positions[i*3 + 1] > 2.5) {{
                        positions[i*3 + 1] = -4.0;
                        positions[i*3] = (Math.random() - 0.5) * 6.0;
                        positions[i*3 + 2] = (Math.random() - 0.5) * 6.0;
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
