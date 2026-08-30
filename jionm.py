import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지온냄새 강화하기 - SOLAR SYSTEM EDITION",
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
# 3. 게임 데이터베이스 정의 (시즌1: 35단계 / 시즌2 환생: 25단계)
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
            "desc": "버스 옆자리에 앉은 지온이가 팔을 들 때 스치듯 나는 가벼운 암내.",
            "price": 150,
            "color": "#718096",
            "tier": 1,
        },
        2: {
            "name": "2단계 : 은은한 자이온냄새",
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
            "name": "4단계 : 진득한 자이온냄새",
            "desc": "여름철 밀폐된 방 안에서 지온이가 뒹굴다 난 땀에 쩐 이불 냄새.",
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
            "name": "6단계 : 풍부한 자이온냄새",
            "desc": "신발장에 박아둔 지온이의 축구화 속에서 무르익은 발효 냄새.",
            "price": 3500,
            "color": "#3182ce",
            "tier": 2,
        },
        7: {
            "name": "7단계 : 압도적인 지온냄새",
            "desc": "지온이가 다녀간 자리마다 코를 찌르는 시큼털털한 체취의 파도.",
            "price": 6100,
            "color": "#2b6cb0",
            "tier": 2,
        },
        8: {
            "name": "8단계 : 폭발하는 지온냄새",
            "desc": "일주일 동안 안 감은 지온이 머리통에서 뿜어져 나오는 유분 폭탄.",
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
            "name": "10단계 : 치명적인 자이온냄새",
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
            "name": "12단계 : 공간지배 자이온냄새",
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
            "name": "14단계 : 신성한 자이온냄새",
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
            "name": "16단계 : 우주관통 자이온냄새",
            "desc": (
                "대기권을 뚫고 오존층마저 뻥 뚫어버리는 지온이의 겨드랑이"
                " 폭풍."
            ),
            "price": 14200000,
            "color": "#00f0ff",
            "tier": 4,
        },
        17: {
            "name": "17단계 : 차원균열 자이온냄새",
            "desc": (
                "지온이의 구린내가 너무 독해서 다른 평행세계의 코까지 썩힌다."
            ),
            "price": 20000000,
            "color": "#ff00ea",
            "tier": 4,
        },
        18: {
            "name": "18단계 : Absolute 자이온냄새",
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
            "name": "20단계 : 자이온맘의 포근한 집밥 냄새",
            "desc": (
                "자이온맘이 끓여준 묵은지 김치찌개... 인 줄 알았으나 지온이"
                " 빨래 냄새."
            ),
            "price": 68300000,
            "color": "#ffaa00",
            "tier": 4,
        },
        21: {
            "name": "21단계 : 자이온맘의 엄격한 등짝 스매싱 냄새",
            "desc": (
                "안 씻고 버티는 지온이를 잡으려고 자이온맘이 휘두른 등짝의"
                " 내음."
            ),
            "price": 101000000,
            "color": "#ff4500",
            "tier": 5,
        },
        22: {
            "name": "22단계 : 자이온맘의 전설의 흙된장국 냄새",
            "desc": (
                "지온이의 발냄새 원액을 살짝 타서 깊은 맛을 낸 자이온맘의"
                " 특제 국물."
            ),
            "price": 160000000,
            "color": "#ff007f",
            "tier": 5,
        },
        23: {
            "name": "23단계 : 자이온맘의 100년 숙성 원액 냄새",
            "desc": (
                "지온이가 어릴 때부터 모아둔 꼬릿한 때를 장독대에 묻어"
                " 숙성시켰다."
            ),
            "price": 230000000,
            "color": "#7b00ff",
            "tier": 5,
        },
        24: {
            "name": "24단계 : 자이온맘의 지온스프레이 냄새",
            "desc": (
                "방 안에 쩔어 있는 지온이의 체취를 탈취제로 잡으려다"
                " 역관람당함."
            ),
            "price": 300000000,
            "color": "#0088ff",
            "tier": 5,
        },
        25: {
            "name": "25단계 : 자이온맘의 대인배적인 냄새",
            "desc": (
                "이런 지온이라도 품에 안아주는 자이온맘의 대인배적 냄새"
                " 포용력."
            ),
            "price": 400000000,
            "color": "#00ffaa",
            "tier": 5,
        },
        26: {
            "name": "26단계 : 자이온맘의 궁극 필살기 냄새",
            "desc": (
                "지온이 방 문을 강제로 열고 환기시키며 뿜어내는 자이온맘의"
                " 분노."
            ),
            "price": 1800000000,
            "color": "#ccff00",
            "tier": 6,
        },
        27: {
            "name": "27단계 : 자이온맘의 창조와 냄새",
            "desc": "지온이의 모든 악취를 정화하려다 자이온맘마저 구속당한 경지.",
            "price": 2500000000,
            "color": "#fffb00",
            "tier": 6,
        },
        28: {
            "name": "28단계 : 자이온맘의 권능 클래식 지온냄새",
            "desc": (
                "우주 전체가 지온이의 발냄새 아래 무릎을 꿇고 헛구역질을 한다."
            ),
            "price": 5500000000,
            "color": "#ffffff",
            "tier": 6,
        },
        29: {
            "name": "29단계 : 클래식 자이온맘",
            "desc": (
                "모든 꼬릿한 냄새의 근원이자, 지온이를 낳고 기른 위대한 악취의"
                " 여신."
            ),
            "price": 10500000000,
            "color": "#ff00aa",
            "tier": 6,
        },
        30: {
            "name": "30단계 : 태초의 자이온맘 ",
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
            "name": "33단계 : 인피니티 자이온 페트리코",
            "desc": "영원히 끝나지 않는 지온이의 발효 비린내가 온 은하를 뒤덮음.",
            "price": 200000000000,
            "color": "#00ff66",
            "tier": 6,
        },
        34: {
            "name": "34단계 : 오메가 자이온 제네시스",
            "desc": "지온이의 냄새로 우주를 멸망시키고 다시 창조하는 종말의 향기.",
            "price": 500000000000,
            "color": "#ff6600",
            "tier": 6,
        },
        35: {
            "name": "35단계 : ★디 오리지널 앱솔루트 지온★",
            "desc": "우주 만물을 통틀어 가장 지독하고 완벽한 궁극의 지온 냄새.",
            "price": float("inf"),
            "color": "#ffffff",
            "tier": 6,
        },
    },
    True: {
        0: {
            "name": "환생 0단계 : 초신성 핵폐기물 지온",
            "desc": "환생을 거쳐 새롭게 압축된 태초의 고밀도 방사능 악취.",
            "price": 500000000,
            "color": "#ff0055",
            "tier": 1,
        },
        1: {
            "name": "환생 1단계 : 안드로메다 지온 암모니아",
            "desc": "안드로메다 은하 전체를 알칼리화시키는 암모니아 폭풍.",
            "price": 1200000000,
            "color": "#00ffff",
            "tier": 1,
        },
        2: {
            "name": "환생 2단계 : 화이트홀 지온 하이드로겐",
            "desc": "우주 백색왜성의 폭발과 함께 뿜어져 나오는 순백의 악취.",
            "price": 3000000000,
            "color": "#ffffff",
            "tier": 1,
        },
        3: {
            "name": "환생 3단계 : 쿼크 글루온 지온 악취",
            "desc": "소립자 수준에서부터 강하게 결합되어 떨어지지 않는 쿼크급 냄새.",
            "price": 7000000000,
            "color": "#ffaa00",
            "tier": 2,
        },
        4: {
            "name": "환생 4단계 : 차원왜곡 지온 타임루프 찌든내 ",
            "desc": "시간의 흐름마저 썩어버리게 만드는 과거와 미래의 냄새 집합체.",
            "price": 15000000000,
            "color": "#9b2c2c",
            "tier": 2,
        },
        5: {
            "name": "환생 5단계 : 네메시스 지온 다크매터",
            "desc": "빛조차 탈출하지 못하고 악취에 붙잡혀 빨려 들어가는 암흑물질.",
            "price": 35000000000,
            "color": "#38a169",
            "tier": 2,
        },
        6: {
            "name": "환생 6단계 : 메가 블랙홀 지온 호라이즌",
            "desc": "모든 물리 법칙이 붕괴하고 오직 지온이의 체취만 남는 경계선.",
            "price": 80000000000,
            "color": "#805ad5",
            "tier": 3,
        },
        7: {
            "name": "환생 7단계 : 감마선 버스트 지온 플레어",
            "desc": "우주 끝까지 수십 광년 동안 일직선으로 뻗어 나가는 살인적 악취.",
            "price": 180000000000,
            "color": "#e53e3e",
            "tier": 3,
        },
        8: {
            "name": "환생 8단계 : 하이퍼노바 지온 코어 붕괴",
            "desc": "거대 항성이 생을 마감하며 방출하는 전설적인 폭발성 악취.",
            "price": 400000000000,
            "color": "#ff4500",
            "tier": 3,
        },
        9: {
            "name": "환생 9단계 : 엘더블루 제네시스 지온",
            "desc": "태초의 우주가 생성되기도 전에 존재했던 푸른빛의 시원(始源) 냄새.",
            "price": 900000000000,
            "color": "#0088ff",
            "tier": 4,
        },
        10: {
            "name": "환생 10단계 : 카이퍼 지온 벨트 코스믹 더스트",
            "desc": "태양계 외곽의 얼어붙은 얼음 조각들에 스며든 미지의 원시 악취.",
            "price": 2000000000000,
            "color": "#cbd5e1",
            "tier": 4,
        },
        11: {
            "name": "환생 11단계 : 지온오르트 클라우드 딥 프리즈",
            "desc": "영원히 녹지 않을 것 같은 극저온 속에서 서서히 발효된 냉동 체취.",
            "price": 4500000000000,
            "color": "#319795",
            "tier": 4,
        },
        12: {
            "name": "환생 12단계 : 태양풍 플라즈마 지온제트 스트림",
            "desc": "태양 표면에서 뿜어져 나오는 고온다습한 초고속 플라즈마 냄새.",
            "price": 10000000000000,
            "color": "#f59e0b",
            "tier": 5,
        },
        13: {
            "name": "환생 13단계 : 마그네타 지온자기장 폭풍",
            "desc": "지구상의 모든 나침반을 고장 내고 정신을 아득하게 만드는 자기장.",
            "price": 25000000000000,
            "color": "#7000ff",
            "tier": 5,
        },
        14: {
            "name": "환생 14단계 : 펄서 지온로테이션 시그널",
            "desc": "일정한 주기로 우주 전체에 강력한 악취 전파를 송출하는 중성자별.",
            "price": 60000000000000,
            "color": "#00ff66",
            "tier": 5,
        },
        15: {
            "name": "환생 15단계 : 웜홀 크로스오버 지온 디멘션",
            "desc": "시공간의 통로를 열어 다른 차원의 구린내를 실시간으로 끌어온다.",
            "price": 150000000000000,
            "color": "#ff00ea",
            "tier": 6,
        },
        16: {
            "name": "환생 16단계 : 스트링 시스코어 지온 엠피리어",
            "desc": "초끈이론의 11차원을 진동시키며 울려 퍼지는 궁극의 우주 진동음.",
            "price": 350000000000000,
            "color": "#ccff00",
            "tier": 6,
        },
        17: {
            "name": "환생 17단계 : 센타우루스 지온 알파 코어",
            "desc": "가장 가까운 별무리의 기운을 통째로 오염시킨 강력한 은하수 향.",
            "price": 800000000000000,
            "color": "#ff6600",
            "tier": 6,
        },
        18: {
            "name": "환생 18단계 : 페가수스 지온 별자리 네뷸라",
            "desc": "신화 속 날개 든 말의 질주를 따라 온 하늘에 퍼지는 거대 성운 향.",
            "price": 2000000000000000,
            "color": "#00f0ff",
            "tier": 6,
        },
        19: {
            "name": "환생 19단계 : 지온세인트 오메가 얼티밋 에센스",
            "desc": "우주의 수명이 다하는 순간까지 사라지지 않는 불멸의 성스러운 냄새.",
            "price": 5000000000000000,
            "color": "#ffe600",
            "tier": 6,
        },
        20: {
            "name": "환생 20단계 : 코스믹 인피니티 싱귤지온래리티",
            "desc": "모든 차원과 우주의 모든 존재가 하나로 응축된 무한대의 악취.",
            "price": 12000000000000000,
            "color": "#ff00aa",
            "tier": 6,
        },
        21: {
            "name": "환생 21단계 : 지온트랜스센던탈 앱솔루트 가디언",
            "desc": "차원의 벽을 넘어 초월적인 신위(神威)를 뿜어내는 가디언의 경지.",
            "price": 30000000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
        22: {
            "name": "환생 22단계 : 하이퍼 자이온 디바인 코어",
            "desc": "지온이라는 존재 자체가 우주의 신성한 법칙으로 등극한 상태.",
            "price": 80000000000000000,
            "color": "#7b00ff",
            "tier": 6,
        },
        23: {
            "name": "환생 23단계 : 지온옴니버스 마스터피스 악취",
            "desc": "모든 평행세계를 통틀어 단 하나만 존재하는 완벽한 걸작 악취.",
            "price": 200000000000000000,
            "color": "#00ffff",
            "tier": 6,
        },
        24: {
            "name": "환생 24단계 : 이터널 제네시스 울티마지온s",
            "desc": "우주의 탄생과 종말을 영원히 반복하게 만드는 궁극의 고리.",
            "price": 500000000000000000,
            "color": "#ff4500",
            "tier": 6,
        },
        25: {
            "name": "환생 25단계 : ★그냥 성지온★",
            "desc": "모든 환생과 차원을 초월하여 완성된 전 우주 최강의 앱솔루트 향.",
            "price": float("inf"),
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
PITY_MAX = 3

# -----------------------------------------------------------------------------
# 4. 세션 상태 초기화
# -----------------------------------------------------------------------------
if "is_rebirth" not in st.session_state:
  st.session_state.is_rebirth = False
if "level" not in st.session_state:
  st.session_state.level = 0
if "max_level" not in st.session_state:
  st.session_state.max_level = 0
if "money" not in st.session_state:
  st.session_state.money = 1000000
if "status" not in st.session_state:
  st.session_state.status = "READY"
if "shield" not in st.session_state:
  st.session_state.shield = 0
if "tears" not in st.session_state:
  st.session_state.tears = 0
if "pity_count" not in st.session_state:
  st.session_state.pity_count = 0
if "rebirth_count" not in st.session_state:
  st.session_state.rebirth_count = 0

# -----------------------------------------------------------------------------
# 5. 강화 로직
# -----------------------------------------------------------------------------


def run_enhance():
  max_lvl = 25 if st.session_state.is_rebirth else 35
  curr = st.session_state.level
  if curr >= max_lvl:
    return

  cost = get_enhance_cost(curr, st.session_state.is_rebirth)
  if st.session_state.money < cost:
    st.session_state.status = "NOT_ENOUGH_MONEY"
    return

  st.session_state.money -= cost

  if st.session_state.pity_count >= PITY_MAX - 1:
    st.session_state.level += 1
    st.session_state.status = "PITY_SUCCESS"
    st.session_state.pity_count = 0
    if st.session_state.level > st.session_state.max_level:
      st.session_state.max_level = st.session_state.level
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


def sell():
  curr = st.session_state.level
  if curr == 0:
    return
  price_val = SMELL_DB[st.session_state.is_rebirth][curr]["price"]
  if price_val == float("inf"):
    st.session_state.money = float("inf")
  else:
    st.session_state.money += price_val
  st.session_state.level = 0
  st.session_state.status = "READY"


def trigger_rebirth():
  st.session_state.is_rebirth = True
  st.session_state.level = 0
  st.session_state.max_level = 0
  st.session_state.money += 100000000000  # 환생 보너스 골드
  st.session_state.shield = 4
  st.session_state.tears = 50
  st.session_state.pity_count = 0
  st.session_state.rebirth_count += 1
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
        padding-top: 5rem !important;
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
        " 0;'>최고 35단계에 도달했습니다!<br>새로운 차원으로 <b>환생</b>하시겠습니까?</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    b_col1, b_col2 = st.columns(2)
    with b_col1:
      if st.button("✨ 환생하기", use_container_width=True):
        trigger_rebirth()
        st.rerun()
    with b_col2:
      if st.button("🔒 아니오", use_container_width=True):
        st.info("현재 단계를 유지합니다.")
    st.markdown(
        "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )

  mode_title = (
      "🌀 [시즌 2] 얼티밋 블랙홀"
      if st.session_state.is_rebirth
      else "🌌 [시즌 1] 솔라 시스템"
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
        " 80개</div></div>",
        unsafe_allow_html=True,
    )

  with s_col2:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>🛡️ 방지권</div><div style='font-size:15px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.shield} /"
        " 4개</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")

    pity_left = PITY_MAX - st.session_state.pity_count
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:12px;"
        f" color:#fde68a;'>✨ 자이온맘의 가호</div><div style='font-size:13px;"
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
      f"<div style='font-size:12px; color:#cbd5e1; background:rgba(255,255,255,0.05);"
      f" padding:8px; border-radius:6px;'>"
      f"• 성공 확률: <b style='color:#38bdf8;'>{sp}%</b> (크리티컬 5%)<br>"
      f"• 하락 확률: <b style='color:#facc15;'>{down_p}%</b><br>"
      f"• 파괴 확률: <b style='color:#ef4444;'>{dp}%</b><br>"
      f"• 유지 확률: <b style='color:#94a3b8;'>{hold_p}%</b>"
      f"</div>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  tab_shop1, tab_shop2 = st.tabs(["🛡️ 방지권", "💧 눈물"])

  with tab_shop1:
    min_shield_level = 16 if st.session_state.is_rebirth else 20
    current_shield_cost = get_shield_cost(
        st.session_state.level, st.session_state.is_rebirth
    )

    if st.session_state.level < min_shield_level:
      st.markdown(
          f"<div style='font-size:13px; color:#ef4444; font-weight:700;"
          f" margin-bottom:8px;'>⚠️ 방지권은 {min_shield_level}단계 이상부터 구매할 수 있습니다!</div>",
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          f"<div style='font-size:13px; color:#cbd5e1; margin-bottom:8px;'>"
          f"<b>보유한도:</b> 최대 4개<br><b>가격:</b> <span"
          f" style='font-size:14px; font-weight:bold; color:#fde68a;'>"
          f"{format_gold(current_shield_cost)}</span></div>",
          unsafe_allow_html=True,
      )

    can_buy_shield = (st.session_state.shield < 4) and (
        st.session_state.level >= min_shield_level
    )
    if st.button(
        "방지권 구매", use_container_width=True, disabled=not can_buy_shield
    ):
      if st.session_state.level < min_shield_level:
        st.warning(f"방지권은 {min_shield_level}단계 이상부터 구매 가능합니다.")
      elif st.session_state.shield >= 4:
        st.warning("최대 4개까지만 보유 가능합니다.")
      elif st.session_state.money >= current_shield_cost:
        st.session_state.money -= current_shield_cost
        st.session_state.shield += 1
        st.success("파괴 방지권 구매 완료!")
        st.rerun()
      else:
        st.error("금액이 부족합니다.")

  with tab_shop2:
    max_lvl = 25 if st.session_state.is_rebirth else 35
    limit_lvl = 18 if st.session_state.is_rebirth else 32
    if st.session_state.level >= limit_lvl:
      st.markdown(
          "<div style='font-size:13px; color:#ef4444; font-weight:700;"
          " margin-bottom:8px;'>⚠️ 고단계부터는 눈물을 사용할 수"
          " 없습니다!</div>",
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          f"<div style='font-size:13px; color:#cbd5e1;"
          f" margin-bottom:8px;'><b>효과:</b> 눈물 20개 소모 (100% 확률로 1~3단계"
          f" 상승)<br><b>현재보유:</b> <span style='font-weight:bold;"
          f" color:#38bdf8;'>{st.session_state.tears} / 80개</span></div>",
          unsafe_allow_html=True,
      )

    can_use_tears = st.session_state.level < limit_lvl
    if st.button(
        "눈물 기적 가동", use_container_width=True, disabled=not can_use_tears
    ):
      if st.session_state.level >= limit_lvl:
        st.warning("고단계부터는 눈물을 사용할 수 없습니다.")
      elif st.session_state.tears >= 20:
        st.session_state.tears -= 20
        add_lvl = random.choice([1, 2, 3])
        st.session_state.level = min(
            max_lvl, st.session_state.level + add_lvl
        )
        st.session_state.status = "CRITICAL" if add_lvl >= 2 else "SUCCESS"
        st.success(f"눈물 기적 100% 성공! {add_lvl}단계 상승!")
        st.rerun()
      else:
        st.error("눈물 20개가 필요합니다.")

  st.markdown(
      "<hr style='margin:12px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 16px; color:#fde68a;'>🌌 자이온"
      " 강화 제어</h4>",
      unsafe_allow_html=True,
  )

  max_lvl = 25 if st.session_state.is_rebirth else 35
  if st.button(
      "🔥 냄새 강화 실행",
      use_container_width=True,
      disabled=(st.session_state.level >= max_lvl),
  ):
    cost = get_enhance_cost(st.session_state.level, st.session_state.is_rebirth)
    if st.session_state.money < cost:
      st.error("강화 비용 부족!")
    else:
      run_enhance()
      st.rerun()

  st.write("")
  if st.button(
      "💰 현재 냄새 판매",
      use_container_width=True,
      disabled=(st.session_state.level == 0),
  ):
    sell()
    st.rerun()

with right_col:
  current_level = st.session_state.level
  max_lvl = 25 if st.session_state.is_rebirth else 35
  curr_data = SMELL_DB[st.session_state.is_rebirth][current_level]
  card_color = curr_data["color"]
  card_title = curr_data["name"]
  card_desc = curr_data["desc"]
  card_price = format_gold(curr_data["price"])
  current_cost = format_gold(
      get_enhance_cost(current_level, st.session_state.is_rebirth)
  )
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
                opacity: 1;
                transition: opacity 0.1s ease-in-out;
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
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="container"></div>

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
            const isFinalSuccess = (currentLevel === maxLvl && (status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS"));

            if (currentLevel >= 15 || isFinalSuccess) {{
                document.getElementById('mainTitle').classList.add('shaking-text');
                document.getElementById('descText').classList.add('shaking-text');
                document.getElementById('priceText').classList.add('shaking-text');
                document.getElementById('costText').classList.add('shaking-text');
            }}

            const statusText = document.getElementById('statusText');
            const tierColor = "{card_color}";
            let statusColor = "#38bdf8";
            let particleSize = 0.25;
            let particleSpeed = 0.6;
            let glowIntensity = 12;

            if (isFinalSuccess) {{
                statusText.innerText = isRebirth ? "🌀👑 [ULTIMATE TRUE REBIRTH ZION] 환생 궁극 최종 성공!! 👑🌀" : "🌌👑 [ULTIMATE GOD ABSOLUTE ZION] 궁극의 최종 강화 성공!! 👑🌌";
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
                statusText.innerText = "✨ 자이온맘의 가호 발동! (천장 100% 성공) ✨";
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

            const particleCount = isFinalSuccess ? 1200 : 500;
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

            const tl = gsap.timeline();

            if (status === "DESTROYED") {{
                outerMesh.visible = false;
                coreMesh.visible = false;

                pointLight.color.set("#ff0000");
                pointLight.intensity = 80;

                const shardCount = 180;
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
                        emissiveIntensity: 2.5
                    }});
                    const shard = new THREE.Mesh(sGeo, sMat);
                    shard.position.set(0, 0, 0);
                    
                    const u = Math.random();
                    const v = Math.random();
                    const theta = u * 2.0 * Math.PI;
                    const phi = Math.acos(2.0 * v - 1.0);
                    const speed = 4.0 + Math.random() * 8.0;
                    
                    shard.userData = {{
                        vx: speed * Math.sin(phi) * Math.cos(theta),
                        vy: speed * Math.sin(phi) * Math.sin(theta),
                        vz: speed * Math.cos(phi),
                        rx: (Math.random() - 0.5) * 30,
                        ry: (Math.random() - 0.5) * 30
                    }};

                    shardGroup.add(shard);
                    shards.push(shard);
                }}
                scene.add(shardGroup);

                tl.to(shardGroup.position, {{
                    duration: 0.5,
                    ease: "power2.out",
                    onUpdate: function() {{
                        const progress = this.progress();
                        shards.forEach(s => {{
                            s.position.x += s.userData.vx * 0.02;
                            s.position.y += s.userData.vy * 0.02 - 0.04;
                            s.position.z += s.userData.vz * 0.02;
                            s.rotation.x += s.userData.rx * 0.02;
                            s.rotation.y += s.userData.ry * 0.02;
                            s.material.opacity = 1.0 - progress;
                            s.material.transparent = true;
                        }});
                    }}
                }});
            }} else {{
                const maxScale = isFinalSuccess ? 1.8 : 1.3;
                tl.to(objectGroup.scale, {{
                    x: maxScale, y: maxScale, z: maxScale,
                    duration: 0.12,
                    ease: "power1.inOut"
                }})
                .to(objectGroup.scale, {{
                    x: 1.0, y: 1.0, z: 1.0,
                    duration: 0.12,
                    ease: "power1.out"
                }});

                const basePosY = -0.7;
                tl.to(objectGroup.position, {{
                    duration: 0.25,
                    onUpdate: function() {{
                        const p = this.progress();
                        const shakeIntensity = (isFinalSuccess ? 0.35 : 0.12) * Math.sin(p * Math.PI);
                        objectGroup.position.x = (Math.random() - 0.5) * shakeIntensity;
                        objectGroup.position.y = basePosY + (Math.random() - 0.5) * shakeIntensity;
                        objectGroup.position.z = (Math.random() - 0.5) * shakeIntensity * 0.5;

                        objectGroup.rotation.x += (Math.random() - 0.5) * shakeIntensity;
                        objectGroup.rotation.y += (Math.random() - 0.5) * shakeIntensity;
                        objectGroup.rotation.z += (Math.random() - 0.5) * shakeIntensity;
                    }}
                }}, 0);
            }}

            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const time = clock.getElapsedTime();

                if (status !== "DESTROYED") {{
                    const rotSpeed = isFinalSuccess ? 1.8 : (status === "FAILED" ? 0.3 : (status === "SUCCESS" || status === "CRITICAL" || status === "PITY_SUCCESS" ? 0.8 : 0.5));
                    outerMesh.rotation.x += 0.005 * rotSpeed;
                    outerMesh.rotation.y += 0.008 * rotSpeed;
                    coreMesh.rotation.x -= 0.01 * rotSpeed;
                    coreMesh.rotation.y -= 0.012 * rotSpeed;

                    if (isFinalSuccess) {{
                        objectGroup.rotation.z = Math.sin(time * 2.0) * 0.15;
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
