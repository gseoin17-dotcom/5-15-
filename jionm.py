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
        "title": "꼬마 킁킁이",
        "reward": 5000,
    },
    "level_10": {
        "name": "10강 돌파",
        "desc": "시즌 1에서 10단계에 도달하세요.",
        "title": "구린내 수련생",
        "reward": 20000,
    },
    "level_20": {
        "name": "20강 돌파",
        "desc": "시즌 1에서 20단계에 도달하세요.",
        "title": "베테랑 후각러",
        "reward": 100000,
    },
    "level_30": {
        "name": "30강 돌파",
        "desc": "시즌 1에서 30단계에 도달하세요.",
        "title": "악취 마스터",
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
        "title": "추락의 전설",
        "reward": 300000,
    },
    "rebirth": {
        "name": "차원의 문",
        "desc": "시즌 2 환생을 시작하세요.",
        "title": "차원 여행자",
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
        "title": "TRUE REBIRTH",
        "reward": 100000000,
    },
    "warp_1": {
        "name": "공간 이동",
        "desc": "워프권을 처음 사용하세요.",
        "title": "워프 개척자",
        "reward": 10000,
    },
    "warp_5": {
        "name": "워프 중독",
        "desc": "워프권을 5회 사용하세요.",
        "title": "차원 도약자",
        "reward": 100000,
    },
    "critical": {
        "name": "대성공",
        "desc": "크리티컬 강화를 성공시키세요.",
        "title": "우주의 선택",
        "reward": 50000,
    },
    "seller": {
        "name": "냄새 장사꾼",
        "desc": "냄새를 판매해 돈을 획득하세요.",
        "title": "냄새 상인",
        "reward": 25000,
    },
    "enhance_50": {
        "name": "강화광",
        "desc": "강화를 총 50회 시도하세요.",
        "title": "망치 중독자",
        "reward": 200000,
    },
    "enhance_100": {
        "name": "강화의 끝",
        "desc": "강화를 총 100회 시도하세요.",
        "title": "단련의 신",
        "reward": 1000000,
    },
    "level_5": {
        "name": "첫 강화",
        "desc": "5단계에 도달하세요.",
        "title": "입문 코끝러",
        "reward": 5000,
    },
    "level_15": {
        "name": "중급 냄새꾼",
        "desc": "15단계에 도달하세요.",
        "title": "향기 수집가",
        "reward": 50000,
    },
    "level_25": {
        "name": "고급 냄새꾼",
        "desc": "25단계에 도달하세요.",
        "title": "악취 지배자",
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
        "title": "공간의 지배자",
        "reward": 500000,
    },
    "enhance_200": {
        "name": "강화는 계속된다",
        "desc": "강화를 총 200회 시도하세요.",
        "title": "강화의 초월자",
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
        "title": "전설의 상인",
        "reward": 300000,
    },
    "survivor": {
        "name": "기적의 생존",
        "desc": "20단계 이상에서 강화 실패 후 살아남으세요.",
        "title": "불굴의 지온",
        "reward": 300000,
    },
}

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
  st.session_state.tears = data["tears"]
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
  st.session_state.season_data[s]["tears"] = st.session_state.tears
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
    else:
      st.session_state.level += 1
      st.session_state.status = "SUCCESS"
  elif r < down_limit:
    st.session_state.pity_count += 1
    if curr > 0:
      st.session_state.level -= 1
    st.session_state.status = "FAILED"
    st.session_state.tears = min(80, st.session_state.tears + 1)
  elif r < destroy_limit:
    if st.session_state.shield > 0:
      st.session_state.shield -= 1
      st.session_state.pity_count += 1
      st.session_state.status = "SHIELD_SAVED"
      st.session_state.tears = min(80, st.session_state.tears + 1)
    else:
      st.session_state.pity_count += 1
      st.session_state.level = 0
      st.session_state.status = "DESTROYED"
      st.session_state.tears = min(80, st.session_state.tears + 2)
  else:
    st.session_state.pity_count += 1
    st.session_state.status = "HOLD"
    st.session_state.tears = min(80, st.session_state.tears + 1)

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
  st.session_state.status = "READY"
  save_current_season_state()



# -----------------------------------------------------------------------------
# 6. 대규모 업데이트 UI
# -----------------------------------------------------------------------------
if "active_page" not in st.session_state:
  st.session_state.active_page = "홈"

if "daily_claimed" not in st.session_state:
  st.session_state.daily_claimed = [True, True, False, False, False]

if "quest_bonus" not in st.session_state:
  st.session_state.quest_bonus = 0

st.markdown(
    """
    <style>
    :root {
        --bg:#050b18;
        --panel:rgba(7,18,38,.82);
        --panel2:rgba(10,27,55,.72);
        --line:rgba(62,155,255,.28);
        --blue:#22b8ff;
        --cyan:#4de7ff;
        --gold:#ffd76a;
        --muted:#8ea5c6;
    }

    .stApp {
        background:
          radial-gradient(circle at 50% 28%, rgba(0,157,255,.20), transparent 25%),
          radial-gradient(circle at 8% 65%, rgba(28,93,255,.13), transparent 26%),
          radial-gradient(circle at 92% 75%, rgba(163,48,255,.15), transparent 28%),
          linear-gradient(180deg,#020713 0%,#061326 48%,#020611 100%);
        color:#eef6ff; position:relative;
    }
    .stApp::before { content:""; position:fixed; inset:0; pointer-events:none; z-index:0;
        background-image:radial-gradient(circle,rgba(130,210,255,.72) 0 1px,transparent 1.5px);
        background-size:72px 72px; opacity:.10; animation:starDrift 28s linear infinite; }
    .stApp::after { content:""; position:fixed; left:-10%; right:-10%; top:7%; height:1px; pointer-events:none;
        background:linear-gradient(90deg,transparent,rgba(43,190,255,.42),transparent);
        box-shadow:0 0 28px rgba(31,170,255,.22); opacity:.7; animation:scanline 9s ease-in-out infinite; }
    @keyframes starDrift { from{transform:translate3d(0,0,0)} to{transform:translate3d(72px,72px,0)} }
    @keyframes scanline { 0%,100%{transform:translateY(0);opacity:.15} 50%{transform:translateY(55vh);opacity:.75} }
    .block-container {
        padding: 1.0rem 1.1rem 1.5rem !important;
        max-width: 100% !important;
    }
    header[data-testid="stHeader"] { background:transparent !important; }
    div.stButton > button { position:relative; overflow:hidden;
        border:1px solid rgba(77,181,255,.38) !important; border-radius:13px !important;
        background:linear-gradient(180deg,rgba(19,58,103,.96),rgba(5,21,45,.96)) !important;
        color:#edf7ff !important; font-weight:850 !important; min-height:40px;
        box-shadow:0 0 18px rgba(0,125,255,.10), inset 0 1px rgba(255,255,255,.10), inset 0 -1px rgba(0,0,0,.45);
        transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease,filter .18s ease !important; }
    div.stButton > button::before { content:""; position:absolute; top:0; left:-120%; width:70%; height:100%;
        background:linear-gradient(105deg,transparent,rgba(255,255,255,.18),transparent); transform:skewX(-20deg); transition:left .55s ease; pointer-events:none; }
    div.stButton > button:hover { border-color:rgba(74,220,255,.92) !important;
        box-shadow:0 0 26px rgba(0,180,255,.26), inset 0 1px rgba(255,255,255,.16) !important;
        transform:translateY(-2px); filter:brightness(1.10); }
    div.stButton > button:hover::before { left:145%; }
    div.stButton > button:active { transform:translateY(0) scale(.985) !important; }
    [data-testid="stSidebar"] {
        background:linear-gradient(180deg,#061224,#030a16) !important;
        border-right:1px solid rgba(68,151,255,.22);
    }
    [data-testid="stSidebar"] > div { padding-top:1rem; }
    [data-testid="stSidebar"] .stButton > button {
        text-align:left !important;
        justify-content:flex-start !important;
        background:transparent !important;
        border:1px solid transparent !important;
        box-shadow:none !important;
        margin:2px 0;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background:rgba(33,122,230,.12) !important;
        border-color:rgba(65,174,255,.22) !important;
    }
    .topbar {
        height:66px;
        display:flex;
        align-items:center;
        gap:18px;
        padding:8px 18px;
        border:1px solid rgba(67,160,255,.25);
        border-radius:18px;
        background:linear-gradient(90deg,rgba(4,18,38,.94),rgba(6,28,58,.82),rgba(4,15,32,.94));
        box-shadow:0 12px 40px rgba(0,0,0,.22), inset 0 1px rgba(255,255,255,.06);
        margin-bottom:12px;
    }
    .brand { font-size:19px; font-weight:950; white-space:nowrap; }
    .brand-sub { color:#86a9d5; font-size:11px; margin-top:2px; }
    .currency {
        display:flex; align-items:center; gap:8px; padding:8px 14px;
        border-radius:13px; border:1px solid rgba(63,172,255,.32);
        background:rgba(9,39,77,.65); font-weight:900; white-space:nowrap;
    }
    .currency small { color:#8fa9ca; font-weight:700; }
    .spacer { flex:1; }

    .section-title { font-size:16px; font-weight:950; letter-spacing:.2px; }
    .section-sub { font-size:11px; color:#8198ba; margin-top:3px; }
    .glass { position:relative; overflow:hidden; border:1px solid var(--line); border-radius:18px;
        background:linear-gradient(145deg,rgba(10,31,61,.86),rgba(4,15,31,.88));
        box-shadow:0 14px 40px rgba(0,0,0,.20), inset 0 1px rgba(255,255,255,.05), 0 0 0 1px rgba(30,120,255,.025);
        padding:15px; transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease; }
    .glass::before { content:""; position:absolute; left:14px; right:14px; top:0; height:1px;
        background:linear-gradient(90deg,transparent,rgba(104,211,255,.65),transparent); opacity:.65; }
    .glass:hover { transform:translateY(-2px); border-color:rgba(73,180,255,.45);
        box-shadow:0 18px 48px rgba(0,0,0,.28),0 0 24px rgba(0,135,255,.07),inset 0 1px rgba(255,255,255,.07); }
    .profile-card::after,.event-banner::after,.hero::after { content:""; position:absolute; inset:0; pointer-events:none;
        background:linear-gradient(115deg,transparent 20%,rgba(255,255,255,.035) 48%,transparent 72%);
        transform:translateX(-120%); animation:panelSweep 7s ease-in-out infinite; }
    @keyframes panelSweep { 0%,55%{transform:translateX(-120%)} 75%,100%{transform:translateX(120%)} }
    .corner-label { display:inline-flex;align-items:center;gap:6px;padding:4px 8px;border-radius:7px;
        font-size:9px;font-weight:950;letter-spacing:1px;color:#75ddff; background:rgba(0,180,255,.08);border:1px solid rgba(78,205,255,.20); }
    .live-dot { display:inline-block;width:6px;height:6px;border-radius:50%;background:#39f7a5;box-shadow:0 0 10px #39f7a5;animation:livePulse 1.3s ease-in-out infinite; }
    @keyframes livePulse { 50%{transform:scale(1.45);opacity:.55} }
    .profile-card { position:relative; overflow:hidden; background:
          radial-gradient(circle at 90% 0%,rgba(0,203,255,.18),transparent 38%),
          radial-gradient(circle at 10% 100%,rgba(69,70,255,.12),transparent 36%),
          linear-gradient(145deg,rgba(10,35,68,.96),rgba(4,15,30,.96));
        border:1px solid rgba(68,176,255,.38); border-radius:18px; padding:16px;
        box-shadow:inset 0 1px rgba(255,255,255,.08),0 12px 34px rgba(0,0,0,.22); }
    .rank-badge {
        display:inline-block; padding:5px 9px; border-radius:999px;
        color:#7ce9ff; background:rgba(0,177,255,.10);
        border:1px solid rgba(69,206,255,.26); font-size:10px; font-weight:900;
    }
    .progress-wrap { height:8px; border-radius:99px; background:#0d203a; overflow:hidden; margin-top:8px; }
    .progress-fill { height:100%; border-radius:99px; background:linear-gradient(90deg,#16a9ff,#4ee8ff); box-shadow:0 0 14px rgba(40,206,255,.6); }
    .day-row { display:flex; gap:7px; margin-top:11px; }
    .day {
        flex:1; min-width:0; text-align:center; padding:9px 4px; border-radius:11px;
        border:1px solid rgba(95,150,210,.20); background:rgba(4,16,34,.7);
    }
    .day.done { border-color:rgba(53,220,171,.38); background:rgba(17,78,67,.24); }
    .day.now { border-color:rgba(79,186,255,.55); background:rgba(21,74,120,.32); }
    .day .n { font-size:10px; color:#89a2c2; }
    .day .ico { font-size:22px; margin:4px 0; }
    .day .s { font-size:10px; font-weight:900; color:#c9dcf5; }

    .quest {
        padding:11px; margin-top:8px; border-radius:12px;
        border:1px solid rgba(71,151,225,.18); background:rgba(2,13,28,.55);
    }
    .quest-head { display:flex; gap:8px; align-items:center; font-size:12px; font-weight:900; }
    .quest-desc { font-size:10px; color:#8fa6c6; margin-top:4px; }
    .quest-bar { height:5px; background:#10233d; border-radius:99px; margin-top:7px; overflow:hidden; }
    .quest-fill { height:100%; background:#20b8ff; border-radius:99px; }
    .news-line { padding:8px 0; border-bottom:1px solid rgba(100,150,210,.11); font-size:11px; }
    .news-line:last-child { border-bottom:0; }
    .news-time { color:#6e88aa; margin-right:8px; }
    .tag { color:#4bdcff; font-weight:900; margin-right:6px; }

    .event-banner { position:relative; overflow:hidden; min-height:92px; display:flex; align-items:center; justify-content:space-between;
        border-radius:16px; padding:16px 18px;
        border:1px solid rgba(236,91,255,.38);
        background:
          radial-gradient(circle at 85% 50%,rgba(255,67,226,.22),transparent 34%),
          linear-gradient(100deg,rgba(75,19,91,.85),rgba(26,13,65,.88));
        box-shadow:0 0 28px rgba(194,44,255,.10);
    }
    .event-kicker { color:#ff8ef7; font-size:10px; font-weight:900; }
    .event-title { font-size:18px; font-weight:950; margin-top:3px; }
    .event-desc { color:#b8a9d4; font-size:10px; margin-top:4px; }
    .event-gift { font-size:44px; filter:drop-shadow(0 0 15px rgba(255,80,230,.55)); animation:giftFloat 2.2s ease-in-out infinite; }
    @keyframes giftFloat { 0%,100%{transform:translateY(0) rotate(-2deg)} 50%{transform:translateY(-7px) rotate(3deg)} }

    .hero { position:relative; overflow:hidden; border:1px solid rgba(59,167,255,.30); border-radius:22px;
        background:radial-gradient(circle at 50% 40%,rgba(0,154,255,.09),transparent 34%),
          linear-gradient(180deg,rgba(2,13,29,.45),rgba(1,8,19,.20));
        box-shadow:0 0 0 1px rgba(42,150,255,.04),0 20px 55px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.06);
        animation:heroGlow 4s ease-in-out infinite; }
    @keyframes heroGlow { 50%{box-shadow:0 0 0 1px rgba(42,150,255,.08),0 22px 65px rgba(0,70,160,.18),inset 0 1px rgba(255,255,255,.08)} }
    .hero-head { text-align:center; padding:14px 10px 0; }
    .hero-head .small { color:#6f91bb; font-size:10px; font-weight:800; letter-spacing:1.5px; }
    .hero-head .big { color:#eaf7ff; font-size:25px; font-weight:950; margin-top:3px; text-shadow:0 0 18px rgba(57,192,255,.22); }
    .hero-head .desc { color:#8199b9; font-size:11px; margin-top:4px; }
    .stat-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:8px; padding:0 12px 12px; }
    .mini-stat { text-align:center; padding:10px; border-radius:12px; background:rgba(4,19,39,.75); border:1px solid rgba(77,160,235,.16); }
    .mini-stat b { display:block; font-size:14px; color:#f4f9ff; }
    .mini-stat span { font-size:9px; color:#7892b5; }

    .bottom-nav { margin-top:12px; padding:8px; border-radius:18px; border:1px solid rgba(65,153,235,.23); background:rgba(3,15,31,.82);
        box-shadow:0 12px 35px rgba(0,0,0,.20),inset 0 1px rgba(255,255,255,.05); }
    .quick-caption { text-align:center; color:#7894b9; font-size:8px; letter-spacing:1.1px; margin-top:5px; }
    .footer-note { text-align:center; color:#627c9e; font-size:9px; padding-top:9px; }

    @media (max-width: 1100px) {
        .currency:nth-of-type(n+3) { display:none; }
    }

    /* ===== SAFE GAME LAUNCHER POLISH ===== */
    .topbar {
        position:relative;
        border-radius:0 0 16px 16px !important;
        border-top:0 !important;
        background:linear-gradient(90deg,rgba(2,13,29,.98),rgba(4,25,52,.94) 48%,rgba(2,11,25,.98)) !important;
        box-shadow:0 10px 34px rgba(0,0,0,.30),inset 0 -1px rgba(45,170,255,.18) !important;
    }
    .topbar::before { content:""; position:absolute; left:0; right:0; bottom:-1px; height:2px;
        background:linear-gradient(90deg,transparent,#159fff,#59e8ff,#159fff,transparent); opacity:.55; }
    .brand-logo { width:50px;height:50px;border-radius:13px;display:flex;align-items:center;justify-content:center;
        border:1px solid rgba(72,192,255,.35);background:radial-gradient(circle,#0b5c9e,#07203f 65%,#041020);
        box-shadow:inset 0 0 20px rgba(34,190,255,.18),0 0 20px rgba(23,155,255,.16);font-size:28px; }
    .top-chip { display:flex;align-items:center;gap:7px;padding:8px 12px;min-width:108px;
        border:1px solid rgba(68,167,255,.30);border-radius:11px;
        background:linear-gradient(180deg,rgba(8,37,73,.92),rgba(4,18,38,.92));
        box-shadow:inset 0 1px rgba(255,255,255,.06),0 0 14px rgba(0,111,255,.07); }
    .top-chip .ico{font-size:18px;}.top-chip .val{font-size:13px;font-weight:950;color:#f3f8ff;}
    .top-chip .lbl{font-size:8px;color:#7190b6;display:block;margin-top:1px;letter-spacing:.6px;}
    .top-icon{font-size:20px;opacity:.88;filter:drop-shadow(0 0 7px rgba(150,220,255,.22));}
    .glass,.profile-card,.event-banner,.hero { position:relative; }
    .glass::after,.profile-card::before,.event-banner::before {
        content:"";position:absolute;width:16px;height:16px;top:-1px;left:-1px;
        border-top:2px solid rgba(92,210,255,.72);border-left:2px solid rgba(92,210,255,.72);
        border-radius:5px 0 0 0;opacity:.9;pointer-events:none;
    }
    .hero::before { content:"";position:absolute;width:70px;height:2px;top:-1px;left:28px;
        background:#54dcff;box-shadow:0 0 15px rgba(64,211,255,.75);pointer-events:none; }
    .event-banner::before { border-color:rgba(255,109,246,.78); }
    .glass::after,.profile-card::after,.event-banner::after {
        content:"";position:absolute;width:16px;height:16px;right:-1px;bottom:-1px;
        border-right:2px solid rgba(92,210,255,.55);border-bottom:2px solid rgba(92,210,255,.55);
        border-radius:0 0 5px 0;opacity:.8;pointer-events:none;
    }
    .hero::after { content:"";position:absolute;width:70px;height:2px;right:28px;bottom:-1px;
        background:#54dcff;box-shadow:0 0 15px rgba(64,211,255,.55);pointer-events:none; }
    .hero { min-height:620px; }
    .hero-head .big { text-shadow:0 0 18px rgba(57,192,255,.28); }
    .day.now { animation:dayPulse 1.7s ease-in-out infinite; }
    @keyframes dayPulse { 50%{box-shadow:0 0 18px rgba(43,193,255,.17);transform:translateY(-1px)} }
    .quest { transition:transform .18s ease,border-color .18s ease,background .18s ease; }
    .quest:hover { transform:translateX(3px);border-color:rgba(72,194,255,.38);background:rgba(8,30,58,.70); }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. 사이드바
# -----------------------------------------------------------------------------
with st.sidebar:
  st.markdown(
      """
      <div style="padding:6px 8px 18px;">
        <div style="font-size:18px;font-weight:950;letter-spacing:.3px;">✦ 지온의 시초</div>
        <div style="font-size:10px;color:#7692b6;margin-top:4px;"><span class="live-dot"></span> 대규모 업데이트 2.0</div>
      </div>
      """,
      unsafe_allow_html=True,
  )

  side_items = [
      ("⌂", "홈"),
      ("♙", "내 정보"),
      ("▣", "퀘스트"),
      ("◈", "상점"),
      ("★", "칭호"),
      ("◇", "이벤트"),
      ("⚙", "설정"),
  ]
  for icon, label in side_items:
    if st.button(f"{icon}   {label}", key=f"side_{label}", use_container_width=True):
      st.session_state.active_page = label
      st.rerun()

  st.markdown(
      """
      <div style="margin-top:18px;padding:12px;border-radius:14px;
      border:1px solid rgba(62,150,235,.20);background:rgba(5,21,43,.65);">
        <div style="font-size:10px;color:#7592b8;">현재 시즌</div>
        <div style="font-size:13px;font-weight:900;margin-top:4px;">
          시즌 2 · ULTIMATE REBIRTH
        </div>
        <div style="font-size:9px;color:#5c789c;margin-top:5px;">
          환생 횟수 {st.session_state.rebirth_count}
        </div>
      </div>
      """,
      unsafe_allow_html=True,
  )

# -----------------------------------------------------------------------------
# 8. 상단 바
# -----------------------------------------------------------------------------
current_level = st.session_state.level
max_lvl = 25 if st.session_state.is_rebirth else 35
curr_data = SMELL_DB[st.session_state.is_rebirth][current_level]
card_color = curr_data["color"]
card_title = curr_data["name"]
card_desc = curr_data["desc"]
card_price = format_gold(curr_data["price"])
current_cost = format_gold(get_enhance_cost(current_level, st.session_state.is_rebirth))
tier = curr_data["tier"]
status = st.session_state.status
prev_level = getattr(st.session_state, "prev_level", current_level)
target_last_lvl = max_lvl - 1
is_last_attempt = (
    prev_level == target_last_lvl
    and status in ["SUCCESS", "CRITICAL", "PITY_SUCCESS", "FAILED", "DESTROYED", "HOLD"]
) or (
    current_level == max_lvl
    and status in ["SUCCESS", "CRITICAL", "PITY_SUCCESS"]
)

st.markdown(
    f"""
    <div class="topbar">
      <div class="brand-logo">✦</div>
      <div>
        <div class="brand">서로의 지배로 탄생한 시초</div>
        <div class="brand-sub"><span class="live-dot"></span> 함께 만드는 새로운 세계 · <b style="color:#48dfff">UPDATE 2.0 LIVE</b></div>
      </div>
      <div class="spacer"></div>
      <div class="top-chip"><span class="ico">💎</span><div><span class="val">{format_gold(st.session_state.money)}</span><span class="lbl">보유 금액</span></div></div>
      <div class="top-chip"><span class="ico">💧</span><div><span class="val">{st.session_state.tears}</span><span class="lbl">눈물</span></div></div>
      <div class="top-chip"><span class="ico">🛡️</span><div><span class="val">{st.session_state.shield}</span><span class="lbl">방지권</span></div></div>
      <div class="corner-label">● ONLINE</div>
      <div class="top-icon">🎁</div><div class="top-icon">✉️</div><div class="top-icon">⚙️</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 9. 메뉴별 보조 화면
# -----------------------------------------------------------------------------
if st.session_state.active_page != "홈":
  page = st.session_state.active_page
  st.markdown(
      f'<div class="glass"><div class="section-title">{page}</div>'
      f'<div class="section-sub">대규모 업데이트 UI에서 {page} 메뉴를 관리합니다.</div></div>',
      unsafe_allow_html=True,
  )

  if page == "내 정보":
    a, b, c = st.columns(3)
    with a:
      st.metric("현재 단계", f"{current_level} / {max_lvl}")
    with b:
      st.metric("최고 단계", f"{st.session_state.max_level}")
    with c:
      st.metric("강화 시도", f"{st.session_state.enhance_attempts}회")
    st.markdown(
        f'<div class="profile-card" style="margin-top:12px;">'
        f'<span class="rank-badge">CURRENT TITLE</span>'
        f'<div style="font-size:25px;font-weight:950;margin-top:10px;">🏷️ {st.session_state.selected_title}</div>'
        f'<div style="font-size:12px;color:#8ca4c4;margin-top:5px;">{card_title}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

  elif page == "퀘스트":
    st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
    quest_data = [
        ("🔷", "발전한 자들의 흔적", "강화 50회 시도하기", min(50, st.session_state.enhance_attempts), 50),
        ("⭐", "시초의 영웅이 되어라", "최고 단계 20 이상 달성", min(20, st.session_state.max_level), 20),
        ("💰", "거대한 부의 시작", "보유 금액 1억 달성", min(100_000_000, int(st.session_state.money) if st.session_state.money != float("inf") else 100_000_000), 100_000_000),
      ]
    for icon, name, desc, value, goal in quest_data:
      pct = int(value / goal * 100) if goal else 100
      st.markdown(
          f'<div class="quest"><div class="quest-head">{icon} {name}'
          f'<span style="margin-left:auto;color:#6fbfff;">{value:,} / {goal:,}</span></div>'
          f'<div class="quest-desc">{desc}</div>'
          f'<div class="quest-bar"><div class="quest-fill" style="width:{pct}%"></div></div></div>',
          unsafe_allow_html=True,
      )
    st.markdown('</div>', unsafe_allow_html=True)

  elif page == "상점":
    st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
    st.markdown("### 🛒 성장 상점")
    s1, s2, s3 = st.columns(3)
    with s1:
      st.markdown("**🛡️ 파괴 방지권**")
      st.caption("강화 파괴를 1회 방지합니다.")
      min_level = 16 if st.session_state.is_rebirth else 20
      shield_cost = int(SMELL_DB[True][current_level]["price"] / 5) if st.session_state.is_rebirth else get_shield_cost(current_level, False)
      if st.button("방지권 구매", key="shop_shield_new", use_container_width=True, disabled=st.session_state.shield >= 3 or current_level < min_level):
        if st.session_state.money >= shield_cost:
          st.session_state.money -= shield_cost
          st.session_state.shield += 1
          save_current_season_state()
          st.rerun()
        else:
          st.error("보유 금액이 부족합니다.")
    with s2:
      st.markdown("**💧 눈물 기적**")
      st.caption("눈물 20개로 1~3단계 상승합니다.")
      if st.button("눈물 사용", key="shop_tears_new", use_container_width=True, disabled=st.session_state.tears < 20 or current_level >= (18 if st.session_state.is_rebirth else 32)):
        st.session_state.tears -= 20
        st.session_state.prev_level = current_level
        st.session_state.level = min(max_lvl, current_level + random.choice([1,2,3]))
        st.session_state.status = "SUCCESS"
        save_current_season_state()
        st.rerun()
    with s3:
      st.markdown("**🚀 워프권**")
      st.caption("도달했던 단계로 즉시 이동합니다.")
      warp_levels = [5,10,15,20] if st.session_state.is_rebirth else [10,15,20,25,30]
      for wl in warp_levels:
        if st.button(f"{wl}단계 워프", key=f"new_warp_{wl}", use_container_width=True,
                     disabled=st.session_state.max_level < wl or current_level >= wl):
          prices = {10:20_000_000,15:100_000_000,20:400_000_000,25:2_000_000_000,30:10_000_000_000}
          price = int(SMELL_DB[True][wl]["price"]/2) if st.session_state.is_rebirth else prices[wl]
          if st.session_state.money >= price:
            st.session_state.money -= price
            st.session_state.warp_uses += 1
            st.session_state.prev_level = current_level
            st.session_state.level = wl
            st.session_state.status = "SUCCESS"
            save_current_season_state()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

  elif page == "칭호":
    st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
    st.markdown("### 🏷️ 칭호 컬렉션")
    options = [TITLE_DEFAULT] + st.session_state.unlocked_titles
    if st.session_state.selected_title not in options:
      st.session_state.selected_title = TITLE_DEFAULT
    st.session_state.selected_title = st.selectbox(
        "현재 장착 칭호", options, index=options.index(st.session_state.selected_title)
    )
    st.markdown(
        f'<div class="profile-card" style="margin-top:12px;text-align:center;">'
        f'<div style="font-size:12px;color:#7e9cc1;">EQUIPPED TITLE</div>'
        f'<div style="font-size:28px;font-weight:950;color:#ffe58a;margin-top:8px;">🏷️ {st.session_state.selected_title}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

  elif page == "이벤트":
    st.markdown(
        '<div class="event-banner" style="margin-top:12px;">'
        '<div><div class="event-kicker">LIMITED EVENT</div>'
        '<div class="event-title">접속만 해도 특별한 보상을 드려요!</div>'
        '<div class="event-desc">대규모 업데이트 기념 이벤트 · 오늘부터 시작</div></div>'
        '<div class="event-gift">🎁</div></div>',
        unsafe_allow_html=True,
    )
    st.info("이벤트 보상 시스템은 현재 대시보드와 연동되어 있습니다.")

  elif page == "설정":
    st.markdown('<div class="glass" style="margin-top:12px;">', unsafe_allow_html=True)
    st.markdown("### ⚙️ 설정")
    st.checkbox("화려한 3D 연출 사용", value=True)
    st.checkbox("강화 결과 자동 표시", value=True)
    st.selectbox("화면 밀도", ["기본", "컴팩트", "넓게"])
    st.markdown('</div>', unsafe_allow_html=True)

  st.stop()

# -----------------------------------------------------------------------------
# 10. 홈 대시보드
# -----------------------------------------------------------------------------
left_col, center_col, right_col = st.columns([2.15, 5.1, 2.15], gap="medium")

with left_col:
  st.markdown(
      f"""
      <div class="profile-card">
        <span class="rank-badge">SEASON {2 if st.session_state.is_rebirth else 1} · CURRENT</span>
        <div style="font-size:18px;font-weight:950;margin-top:9px;">
          {'🌀 얼티밋 자이온의 시작' if st.session_state.is_rebirth else '🌌 지온의 탄생과 시초'}
        </div>
        <div style="font-size:11px;color:#8199bb;margin-top:4px;">
          {card_title}
        </div>
        <div style="display:flex;justify-content:space-between;margin-top:15px;font-size:11px;">
          <span>현재 진행도</span><b>{current_level} / {max_lvl}</b>
        </div>
        <div class="progress-wrap"><div class="progress-fill" style="width:{current_level/max_lvl*100:.1f}%"></div></div>
        <div style="font-size:10px;color:#6f88a9;margin-top:6px;">최고 기록 {st.session_state.max_level}단계</div>
      </div>
      """,
      unsafe_allow_html=True,
  )

  st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
  st.markdown(
      '<div class="glass"><div class="section-title">🎁 일일 / 주간 접속 보상</div>'
      '<div class="section-sub">매일 접속하고 보상을 획득하세요.</div>',
      unsafe_allow_html=True,
  )

  rewards = [("1일차","🧰","완료"),("2일차","💎","완료"),("3일차","🪙","진행중"),("4일차","⭐","미달성"),("5일차","👾","미달성")]
  day_cols = st.columns(5)
  for i, (day, ico, state) in enumerate(rewards):
    with day_cols[i]:
      cls = "done" if i < 2 else ("now" if i == 2 else "")
      st.markdown(
          f'<div class="day {cls}"><div class="n">{day}</div><div class="ico">{ico}</div>'
          f'<div class="s">{state}</div></div>',
          unsafe_allow_html=True,
      )
  if st.button("🎁 오늘의 보상 받기", key="claim_daily", use_container_width=True):
    if not st.session_state.daily_claimed[2]:
      st.session_state.daily_claimed[2] = True
      st.session_state.money += 5_000
      st.toast("오늘의 접속 보상 +5,000원!")
      st.rerun()
    else:
      st.info("오늘의 보상은 이미 받았습니다.")
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
  st.markdown(
      '<div class="glass"><div class="section-title">📜 진행 중 퀘스트</div>'
      '<div class="section-sub">업적과 별개로 빠르게 보상을 획득하세요.</div>',
      unsafe_allow_html=True,
  )
  quests = [
      ("🔷","발전한 자들의 흔적","강화 50회 시도하기",min(st.session_state.enhance_attempts,50),50,"5,000원"),
      ("⭐","시초의 영웅이 되어라","최고 단계 20 달성하기",min(st.session_state.max_level,20),20,"10 포인트"),
  ]
  for icon, name, desc, val, goal, reward in quests:
    pct = val / goal * 100
    st.markdown(
        f'<div class="quest"><div class="quest-head">{icon} {name}'
        f'<span style="margin-left:auto;color:#c6d9f0;font-size:10px;">{val}/{goal}</span></div>'
        f'<div class="quest-desc">{desc} · 보상 {reward}</div>'
        f'<div class="quest-bar"><div class="quest-fill" style="width:{pct:.1f}%"></div></div></div>',
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)

with center_col:
  st.markdown(
      f'<div class="hero"><div class="hero-head">'
      f'<div class="small">✦ ORIGIN CORE · UPDATE 2.0 ✦</div>'
      f'<div class="big">{card_title}</div>'
      f'<div class="desc">{card_desc}</div></div>',
      unsafe_allow_html=True,
  )

  # 기존 3D 강화 연출을 그대로 유지하고, 새로운 대시보드 중앙에 배치
  st.markdown(
      f'<div style="display:flex;justify-content:space-between;align-items:center;padding:0 14px 7px;">'
      f'<span class="corner-label">✦ ORIGIN CORE</span>'
      f'<span style="font-size:9px;color:#6f8fb6;letter-spacing:1.2px;">SEASON {2 if st.session_state.is_rebirth else 1} · {current_level:02d}/{max_lvl:02d}</span>'
      f'</div>'
      f'<div style="display:flex;justify-content:space-between;padding:0 14px;position:relative;z-index:2;">'
      f'<span style="font-size:8px;color:#3f668f;letter-spacing:1.6px;">SYSTEM // CORE SYNCHRONIZED</span>'
      f'<span style="font-size:8px;color:#3f668f;letter-spacing:1.6px;">NODE 07 · STABLE</span>'
      f'</div>', unsafe_allow_html=True
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
                font-size: 22px;
                font-weight: 900;
                color: #fde68a;
                text-shadow: 0 0 12px rgba(253,230,138,0.75), 0 2px 4px rgba(0,0,0,0.9);
                white-space: nowrap;
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
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="container"></div>
        <div id="flashOverlay"></div>
        <div class="selected-title-ui">🏷️ {st.session_state.selected_title}</div>

        <div id="cinematicUi" class="cinematic-ui visible">
            <div id="statusText" class="status-header">READY</div>
            <div id="mainTitle" class="title-tier-{tier}">{card_title}</div>
            <div id="descText" class="desc-text">"{card_desc}"</div>
            <div id="priceText" class="price-text">예상 가치: {card_price}</div>
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
  st.markdown(
      f'<div class="stat-grid">'
      f'<div class="mini-stat"><b>{format_gold(st.session_state.money)}</b><span>현재 보유 금액</span></div>'
      f'<div class="mini-stat"><b>{current_level}단계</b><span>현재 단계</span></div>'
      f'<div class="mini-stat"><b>{st.session_state.pity_count}/{PITY_MAX}</b><span>천장 진행</span></div>'
      f'</div></div>',
      unsafe_allow_html=True,
  )

  st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
  action1, action2 = st.columns(2)
  with action1:
    if st.button(
        f"🔥 냄새 강화 실행 · {current_cost}",
        key="main_enhance_update",
        use_container_width=True,
        disabled=(current_level >= max_lvl),
    ):
      cost = get_enhance_cost(current_level, st.session_state.is_rebirth)
      if st.session_state.money < cost:
        st.error("강화 비용 부족!")
      else:
        st.session_state.enhance_attempts += 1
        run_enhance()
        check_achievements()
        save_current_season_state()
        st.rerun()
  with action2:
    if st.button(
        "💰 현재 냄새 판매",
        key="main_sell_update",
        use_container_width=True,
        disabled=(current_level == 0),
    ):
      sell()
      unlock_achievement("seller")
      st.rerun()

with right_col:
  st.markdown(
      '<div class="event-banner"><div><div class="event-kicker">SPECIAL EVENT</div>'
      '<div class="event-title">지금 접속하면<br>특별한 보상을 드려요!</div>'
      '<div class="event-desc">업데이트 기념 선물 · 한정 이벤트 진행중</div></div>'
      '<div class="event-gift">🎁</div></div>',
      unsafe_allow_html=True,
  )

  st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
  st.markdown(
      '<div class="glass"><div class="section-title">📢 이벤트 & 공지</div>'
      '<div class="section-sub">새로운 소식을 확인하세요.</div>',
      unsafe_allow_html=True,
  )
  news = [
      ("22:34","[이벤트]","오늘은 경험치 2배! 이벤트가 시작되었습니다!"),
      ("21:17","[공지]","대규모 업데이트 2.0이 적용되었습니다."),
      ("20:03","[알림]","새로운 칭호가 추가되었습니다."),
      ("19:45","[이벤트]","접속 보상으로 특별 선물을 획득했습니다!"),
  ]
  for tm, tag, text in news:
    st.markdown(
        f'<div class="news-line"><span class="news-time">{tm}</span>'
        f'<span class="tag">{tag}</span>{text}</div>',
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
  st.markdown(
      '<div class="glass"><div class="section-title">📰 최근 소식</div>',
      unsafe_allow_html=True,
  )
  recent = [
      "신규 칭호 5종 추가",
      "환생 시즌 보상 개편",
      "워프권 UI 개선",
      "강화 연출 최적화",
      "업적 보상 표시 개선",
  ]
  for idx, item in enumerate(recent):
    st.markdown(
        f'<div class="news-line"><span class="news-time">{idx+1:02d}</span>{item}</div>',
        unsafe_allow_html=True,
    )
  st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 11. 하단 빠른 메뉴
# -----------------------------------------------------------------------------
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
nav_cols = st.columns(7)
quick = [("🎒","가방"),("⚔️","강화"),("📖","스킬"),("🏷️","칭호"),("🗺️","지도"),("🎁","이벤트"),("🛒","상점")]
for i, (icon, label) in enumerate(quick):
  with nav_cols[i]:
    if st.button(f"{icon}\n{label}", key=f"quick_{label}", use_container_width=True):
      if label == "강화":
        if current_level < max_lvl:
          cost = get_enhance_cost(current_level, st.session_state.is_rebirth)
          if st.session_state.money >= cost:
            st.session_state.enhance_attempts += 1
            run_enhance()
            check_achievements()
            save_current_season_state()
            st.rerun()
          else:
            st.error("강화 비용 부족!")
      elif label == "칭호":
        st.session_state.active_page = "칭호"
        st.rerun()
      elif label == "상점":
        st.session_state.active_page = "상점"
        st.rerun()
      elif label == "이벤트":
        st.session_state.active_page = "이벤트"
        st.rerun()
      else:
        st.toast(f"{label} 메뉴는 업데이트 준비중입니다.")
    st.markdown(f'<div class="quick-caption">{label.upper()}</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer-note">TIP · 일일 퀘스트를 완료하고 다양한 보상을 받아보세요!</div>',
    unsafe_allow_html=True,
)
