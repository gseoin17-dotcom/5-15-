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
# 3. 게임 데이터베이스 정의 (시즌1: 35단계 / 시즌2: 25단계 - 지온/자이온 테마 적용)
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
            "name": "6단계 : 풍부한 지온냄새",
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
            "desc": "소립자 수준에서부터 강하게 결합되어 떨어지지 않는 쿼크급 냄새.",
            "price": 15000000000,
            "color": "#ffaa00",
            "tier": 2,
        },
        4: {
            "name": "환생 4단계 : 차원왜곡 자이온 타임루프 찌든내 ",
            "desc": "시간의 흐름마저 썩어버리게 만드는 과거와 미래의 냄새 집합체.",
            "price": 35000000000,
            "color": "#9b2c2c",
            "tier": 2,
        },
        5: {
            "name": "환생 5단계 : 네메시스 자이온 다크매터",
            "desc": "빛조차 탈출하지 못하고 악취에 붙잡혀 빨려 들어가는 암흑물질.",
            "price": 80000000000,
            "color": "#38a169",
            "tier": 2,
        },
        6: {
            "name": "환생 6단계 : 메가 블랙홀 자이온 호라이즌",
            "desc": "모든 물리 법칙이 붕괴하고 오직 자이온이의 체취만 남는 경계선.",
            "price": 180000000000,
            "color": "#805ad5",
            "tier": 3,
        },
        7: {
            "name": "환생 7단계 : 감마선 버스트 자이온 플레어",
            "desc": "우주 끝까지 수십 광년 동안 일직선으로 뻗어 나가는 살인적 악취.",
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
            "desc": "태초의 우주가 생성되기도 전에 존재했던 푸른빛의 시원(始源) 냄새.",
            "price": 2000000000000,
            "color": "#0088ff",
            "tier": 4,
        },
        10: {
            "name": "환생 10단계 : 카이퍼 자이온 벨트 코스믹 더스트",
            "desc": "태양계 외곽의 얼어붙은 얼음 조각들에 스며든 미지의 원시 악취.",
            "price": 4500000000000,
            "color": "#cbd5e1",
            "tier": 4,
        },
        11: {
            "name": "환생 11단계 : 자이온오르트 클라우드 딥 프리즈",
            "desc": "영원히 녹지 않을 것 같은 극저온 속에서 서서히 발효된 냉동 체취.",
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
            "desc": "지구상의 모든 나침반을 고장 내고 정신을 아득하게 만드는 자기장.",
            "price": 50000000000000,
            "color": "#7000ff",
            "tier": 5,
        },
        14: {
            "name": "환생 14단계 : 펄서 자이온로테이션 시그널",
            "desc": "일정한 주기로 우주 전체에 강력한 악취 전파를 송출하는 중성자별.",
            "price": 120000000000000,
            "color": "#00ff66",
            "tier": 5,
        },
        15: {
            "name": "환생 15단계 : 웜홀 크로스오버 자이온 디멘션",
            "desc": "시공간의 통로를 열어 다른 차원의 구린내를 실시간으로 끌어온다.",
            "price": 280000000000000,
            "color": "#ff00ea",
            "tier": 6,
        },
        16: {
            "name": "환생 16단계 : 스트링 시스코어 자이온 엠피리어",
            "desc": "초끈이론의 11차원을 진동시키며 울려 퍼지는 궁극의 우주 진동음.",
            "price": 600000000000000,
            "color": "#ccff00",
            "tier": 6,
        },
        17: {
            "name": "환생 17단계 : 센타우루스 자이온 알파 코어",
            "desc": "가장 가까운 별무리의 기운을 통째로 오염시킨 강력한 은하수 향.",
            "price": 1300000000000000,
            "color": "#ff6600",
            "tier": 6,
        },
        18: {
            "name": "환생 18단계 : 페가수스 자이온 별자리 네뷸라",
            "desc": "신화 속 날개 든 말의 질주를 따라 온 하늘에 퍼지는 거대 성운 향.",
            "price": 3000000000000000,
            "color": "#00f0ff",
            "tier": 6,
        },
        19: {
            "name": "환생 19단계 : 자이온세인트 오메가 얼티밋 에센스",
            "desc": "우주의 수명이 다하는 순간까지 사라지지 않는 불멸의 성스러운 냄새.",
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
            "desc": "차원의 벽을 넘어 초월적인 신위(神威)를 뿜어내는 가디언의 경지.",
            "price": 35000000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
        22: {
            "name": "환생 22단계 : 하이퍼 자이온 디바인 코어",
            "desc": "자이온이라는 존재 자체가 우주의 신성한 법칙으로 등극한 상태.",
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
    "first_enhance": {"name": "첫걸음", "desc": "처음으로 강화를 시도하세요.", "title": "초보 강화러", "reward": 5000},
    "level_10": {"name": "10강 돌파", "desc": "시즌 1에서 10단계에 도달하세요.", "title": "냄새 수련생", "reward": 20000},
    "level_20": {"name": "20강 돌파", "desc": "시즌 1에서 20단계에 도달하세요.", "title": "냄새 전문가", "reward": 100000},
    "level_30": {"name": "30강 돌파", "desc": "시즌 1에서 30단계에 도달하세요.", "title": "냄새 마스터", "reward": 500000},
    "level_35": {"name": "궁극의 지온", "desc": "시즌 1 최종 35단계를 달성하세요.", "title": "디 오리지널 지온", "reward": 1000000},
    "drop_to_0": {"name": "끝없는 추락", "desc": "34단계에서 0단계로 돌아가세요.", "title": "추락의 전설", "reward": 3000000},
    "rebirth": {"name": "차원의 문", "desc": "시즌 2 환생을 시작하세요.", "title": "차원 여행자", "reward": 5000000},
    "s2_level_10": {"name": "자이온 각성", "desc": "시즌 2에서 10단계에 도달하세요.", "title": "자이온", "reward": 10000000},
    "s2_level_20": {"name": "자이온 폭주", "desc": "시즌 2에서 20단계에 도달하세요.", "title": "폭주의 자이온", "reward": 30000000},
    "s2_level_25": {"name": "진정한 환생", "desc": "시즌 2 최종 25단계를 달성하세요.", "title": "TRUE REBIRTH", "reward": 100000000},
    "warp_1": {"name": "공간 이동", "desc": "워프권을 처음 사용하세요.", "title": "워프 개척자", "reward": 10000},
    "warp_5": {"name": "워프 중독", "desc": "워프권을 5회 사용하세요.", "title": "워프 중독자", "reward": 100000},
    "critical": {"name": "대성공", "desc": "크리티컬 강화를 성공시키세요.", "title": "우주의 선택", "reward": 50000},
    "seller": {"name": "냄새 장사꾼", "desc": "냄새를 판매해 돈을 획득하세요.", "title": "냄새 상인", "reward": 25000},
    "enhance_50": {"name": "강화광", "desc": "강화를 총 50회 시도하세요.", "title": "강화 중독자", "reward": 200000},
    "enhance_100": {"name": "강화의 끝", "desc": "강화를 총 100회 시도하세요.", "title": "강화의 신", "reward": 1000000},
    "level_5": {"name": "첫 강화", "desc": "5단계에 도달하세요.", "title": "냄새 입문자", "reward": 5000},
    "level_15": {"name": "중급 냄새꾼", "desc": "15단계에 도달하세요.", "title": "냄새 수집가", "reward": 50000},
    "level_25": {"name": "고급 냄새꾼", "desc": "25단계에 도달하세요.", "title": "냄새 지배자", "reward": 250000},
    "s2_level_5": {"name": "자이온 입문", "desc": "시즌 2에서 5단계에 도달하세요.", "title": "자이온 견습생", "reward": 1000000},
    "s2_level_15": {"name": "자이온 숙련", "desc": "시즌 2에서 15단계에 도달하세요.", "title": "자이온 숙련자", "reward": 15000000},
    "warp_10": {"name": "워프 마스터", "desc": "워프권을 10회 사용하세요.", "title": "공간의 지배자", "reward": 500000},
    "enhance_200": {"name": "강화는 계속된다", "desc": "강화를 총 200회 시도하세요.", "title": "강화의 초월자", "reward": 5000000},
    "rich": {"name": "부자 냄새", "desc": "보유 금액 10억을 달성하세요.", "title": "지온 재벌", "reward": 1000000},
    "seller_10": {"name": "장사의 신", "desc": "판매를 10회 성공하세요.", "title": "전설의 상인", "reward": 300000},
    "survivor": {"name": "기적의 생존", "desc": "20단계 이상에서 강화 실패 후 살아남으세요.", "title": "불굴의 지온", "reward": 300000},
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
        st.toast(f"🏆 업적 달성: {ACHIEVEMENTS[key]['name']}  |  +{format_gold(ACHIEVEMENTS[key]['reward'])}")

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
    if not st.session_state.is_rebirth and level == 0 and st.session_state.max_level >= 34:
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
          "max_level": 0,
          "money": 1000000000,
          "status": "READY",
          "shield": 4,
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
    if random.random() < min(0.50, CRITICAL_RATE + st.session_state.get("crit_boost", 0.0)) and curr + 2 <= max_lvl:
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
# 6. 대규모 UI 개편 - ZION NEXUS
# -----------------------------------------------------------------------------
import time

if "enhance_history" not in st.session_state:
    st.session_state.enhance_history = []
if "auto_enhancing" not in st.session_state:
    st.session_state.auto_enhancing = False
if "auto_target" not in st.session_state:
    st.session_state.auto_target = 1
if "points" not in st.session_state:
    st.session_state.points = 0
if "crit_boost" not in st.session_state:
    st.session_state.crit_boost = 0.0
if "daily_claimed" not in st.session_state:
    st.session_state.daily_claimed = False
if "sound_enabled" not in st.session_state:
    st.session_state.sound_enabled = True
if "show_details" not in st.session_state:
    st.session_state.show_details = False


def record_history(before, after, status):
    st.session_state.enhance_history.insert(0, {
        "time": time.strftime("%H:%M:%S"),
        "before": before,
        "after": after,
        "status": status,
    })
    st.session_state.enhance_history = st.session_state.enhance_history[:20]


def do_enhance_once():
    before = st.session_state.level
    cost = get_enhance_cost(before, st.session_state.is_rebirth)
    if st.session_state.money < cost:
        st.session_state.status = "NOT_ENOUGH_MONEY"
        return False
    st.session_state.enhance_attempts += 1
    run_enhance()
    check_achievements()
    record_history(before, st.session_state.level, st.session_state.status)
    st.session_state.points += 10
    save_current_season_state()
    return True


def buy_crit_boost():
    cost = 150
    if st.session_state.points >= cost:
        st.session_state.points -= cost
        st.session_state.crit_boost = min(0.45, st.session_state.crit_boost + 0.10)
        st.toast("⚡ 크리티컬 확률 +10% 부스트 활성화")
        return True
    st.error("포인트가 부족합니다.")
    return False


def claim_daily_reward():
    if st.session_state.daily_claimed:
        st.info("오늘의 보상은 이미 받았습니다.")
        return
    st.session_state.daily_claimed = True
    st.session_state.money += 100000
    st.session_state.tears = min(80, st.session_state.tears + 5)
    st.session_state.points += 100
    save_current_season_state()
    st.toast("🎁 출석 보상 +100,000원 · 눈물 +5 · 100P")


# -----------------------------------------------------------------------------
# 7. NEXUS CSS
# -----------------------------------------------------------------------------
st.markdown("""
<style>
:root{--bg:#050914;--panel:#091426;--panel2:#0c1b32;--line:#1e4f91;--cyan:#39d8ff;--blue:#5d8dff;--violet:#9b5cff;--gold:#ffd45c;--muted:#7186a5}
.stApp{background:radial-gradient(circle at 50% 0%,rgba(55,92,255,.18),transparent 28%),radial-gradient(circle at 90% 70%,rgba(151,65,255,.14),transparent 32%),linear-gradient(145deg,#02050c,#07101f 48%,#02050b);color:#edf6ff}
.block-container{max-width:1540px!important;padding-top:1.2rem!important;padding-bottom:2rem!important}
section[data-testid="stVerticalBlock"]{gap:.45rem}
[data-testid="stHorizontalBlock"]{gap:.7rem}
.stButton>button{min-height:44px!important;border:1px solid rgba(72,143,238,.42)!important;border-radius:12px!important;background:linear-gradient(180deg,rgba(20,48,84,.96),rgba(7,18,34,.98))!important;color:#edf7ff!important;font-weight:850!important;box-shadow:inset 0 1px rgba(255,255,255,.08),0 10px 25px rgba(0,0,0,.24)!important;transition:.18s ease!important}
.stButton>button:hover{border-color:rgba(57,216,255,.85)!important;transform:translateY(-1px);box-shadow:0 0 22px rgba(57,216,255,.13)!important}
.stButton>button[kind="primary"]{background:linear-gradient(135deg,#6937e7,#3b6cff)!important;border-color:#a77aff!important;box-shadow:0 0 34px rgba(125,77,255,.28)!important}
[data-testid="stMetric"]{background:linear-gradient(145deg,rgba(12,28,51,.96),rgba(4,11,22,.98));border:1px solid rgba(66,137,230,.28);border-radius:15px;padding:12px 14px;box-shadow:inset 0 1px rgba(255,255,255,.05),0 12px 28px rgba(0,0,0,.25)}
[data-testid="stMetricLabel"]{color:#7890af!important;font-size:10px!important;font-weight:900!important;letter-spacing:1.4px!important}
[data-testid="stMetricValue"]{color:#f4f9ff!important;font-size:24px!important;font-weight:950!important}
[data-testid="stTabs"]{margin-top:8px}
[data-testid="stTabs"] button{font-weight:900!important;color:#7f94b2!important;border-radius:10px 10px 0 0!important}
[data-testid="stTabs"] [aria-selected="true"]{color:white!important;background:linear-gradient(180deg,rgba(109,65,224,.38),rgba(30,58,105,.16))!important;border-bottom:2px solid #8d63ff!important}
.stProgress>div>div>div{background:linear-gradient(90deg,#27c9ff,#765cff,#b86bff)!important}
hr{border-color:rgba(83,153,255,.16)!important}
.nx-card{border:1px solid rgba(65,137,229,.28);background:linear-gradient(145deg,rgba(10,25,45,.96),rgba(3,9,18,.98));border-radius:18px;padding:16px;box-shadow:inset 0 1px rgba(255,255,255,.05),0 18px 40px rgba(0,0,0,.22)}
.nx-label{font-size:10px;letter-spacing:2px;color:#4bdfff;font-weight:950}.nx-muted{color:#7890ad;font-size:11px}.nx-big{font-size:36px;font-weight:950;letter-spacing:-1px}.nx-title{font-size:18px;font-weight:950}.nx-pill{display:inline-block;padding:5px 9px;border-radius:999px;border:1px solid rgba(99,158,255,.3);background:rgba(36,72,126,.2);font-size:10px;font-weight:900;color:#a9c8ff}
.title-badge{padding:12px 16px;border-radius:14px;text-align:center;border:1px solid rgba(166,113,255,.45);background:radial-gradient(circle at 50% 20%,rgba(150,85,255,.28),rgba(7,13,25,.88));box-shadow:0 0 25px rgba(131,73,255,.12)}
.title-badge .name{font-size:18px;font-weight:950;color:#f1d9ff}.title-badge .sub{font-size:9px;letter-spacing:2px;color:#a78bfa;margin-bottom:4px}
.history-row{display:flex;justify-content:space-between;align-items:center;padding:8px 2px;border-bottom:1px solid rgba(100,130,170,.12);font-size:11px}.history-ok{color:#62e5ff}.history-bad{color:#ff718e}.history-neutral{color:#9aaac0}
</style>
""", unsafe_allow_html=True)


def _status_meta(status):
    return {
        "READY": ("READY", "#54d8ff", "에너지가 코어 중심으로 집결하고 있습니다."),
        "SUCCESS": ("SUCCESS", "#55e6ff", "강화 코어가 한 단계 진화했습니다."),
        "CRITICAL": ("CRITICAL", "#ffffff", "한계를 돌파한 초월 강화!"),
        "PITY_SUCCESS": ("PITY", "#ffd45c", "보호 코어가 작동해 확정 강화했습니다."),
        "FAILED": ("DOWN", "#8ea1bb", "코어 안정화에 실패했습니다."),
        "DESTROYED": ("DESTROYED", "#ff496f", "코어가 붕괴했습니다."),
        "SHIELD_SAVED": ("SHIELD", "#6fa8ff", "방지권이 코어를 보호했습니다."),
        "HOLD": ("HOLD", "#9aaac0", "현재 단계가 유지되었습니다."),
        "NOT_ENOUGH_MONEY": ("LOCKED", "#ffb86b", "강화 비용이 부족합니다."),
    }.get(status, (status, "#54d8ff", "코어가 대기 중입니다."))


def render_3d_core(level, max_lvl, data, status):
    color = data["color"]
    title = data["name"].replace("\\", "").replace("\"", "'")
    desc = data["desc"].replace("\\", "").replace("\"", "'")
    status_name, status_color, status_desc = _status_meta(status)
    safe_color = color if isinstance(color, str) and color.startswith("#") else "#39d8ff"
    rebirth = st.session_state.is_rebirth
    final = level >= max_lvl and status in {"SUCCESS","CRITICAL","PITY_SUCCESS"}
    model = min(7, level // 5)
    if rebirth: model = min(7, model + 1)
    js = f"""
<!doctype html><html><head><style>
html,body,#c{{width:100%;height:100%;margin:0;overflow:hidden;background:transparent}}
#c{{position:relative}}.hud{{position:absolute;left:0;right:0;top:12px;text-align:center;pointer-events:none;font-family:Arial,sans-serif}}
.k{{font-size:10px;letter-spacing:3px;color:#67e8f9;font-weight:900}}.lv{{font-size:34px;font-weight:950;color:#fff;text-shadow:0 0 18px {safe_color}}}.nm{{font-size:13px;font-weight:900;color:{safe_color};max-width:90%;margin:auto}}
.bottom{{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-family:Arial,sans-serif;pointer-events:none}}
.st{{font-size:14px;font-weight:950;color:{status_color};letter-spacing:1px;text-shadow:0 0 12px {status_color}}}.ds{{font-size:10px;color:#9eb0c8;margin-top:4px}}
</style><script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script></head><body><div id="c"></div>
<div class="hud"><div class="k">ZION NEXUS CORE</div><div class="lv">+{level}</div><div class="nm">{title}</div></div>
<div class="bottom"><div class="st">{status_name}{' · ULTIMATE' if final else ''}</div><div class="ds">{status_desc}</div></div>
<script>
const W=innerWidth,H=innerHeight, scene=new THREE.Scene();
const cam=new THREE.PerspectiveCamera(38,W/H,.1,100);cam.position.set(0,0.4,9);
const renderer=new THREE.WebGLRenderer({{antialias:true,alpha:true}});renderer.setSize(W,H);renderer.setPixelRatio(Math.min(devicePixelRatio,2));document.getElementById('c').appendChild(renderer.domElement);
scene.add(new THREE.AmbientLight(0xffffff,{2.2 if final else 1.0}));
const l=new THREE.PointLight(new THREE.Color('{safe_color}'),{45 if final else 18},40);l.position.set(0,1,4);scene.add(l);
const rim=new THREE.PointLight(0x4f78ff,10,28);rim.position.set(-4,2,2);scene.add(rim);
const group=new THREE.Group();group.position.y=-0.25;scene.add(group);
const mat=new THREE.MeshPhysicalMaterial({{color:'{safe_color}',metalness:.78,roughness:.12,emissive:'{safe_color}',emissiveIntensity:{1.1 if final else .35},transparent:true,opacity:.94,clearcoat:1,clearcoatRoughness:.12}});
let geo;
const m={model};
if(m===0) geo=new THREE.OctahedronGeometry(1.45,1);
else if(m===1) geo=new THREE.IcosahedronGeometry(1.55,1);
else if(m===2) geo=new THREE.BoxGeometry(2.25,2.25,2.25); 
else if(m===3) geo=new THREE.TorusKnotGeometry(1.15,.36,96,18,2,3);
else if(m===4) geo=new THREE.CylinderGeometry(1.25,1.7,2.7,8,1);
else if(m===5) geo=new THREE.DodecahedronGeometry(1.65,1);
else if(m===6) geo=new THREE.TorusGeometry(1.5,.24,20,80);
else geo=new THREE.IcosahedronGeometry(1.8,2);
const outer=new THREE.Mesh(geo,mat);group.add(outer);
const coreMat=new THREE.MeshPhysicalMaterial({{color:0xffffff,emissive:'{status_color}',emissiveIntensity:{5 if final else 2.2},metalness:.5,roughness:.02,transmission:.25}});
const core=new THREE.Mesh(new THREE.SphereGeometry({1.0 if final else .72},32,32),coreMat);group.add(core);
for(let i=0;i<4;i++){{const rg=new THREE.TorusGeometry(2.0+i*.22,.018,8,96);const rm=new THREE.MeshBasicMaterial({{color:'{status_color}',transparent:true,opacity:.35}});const rr=new THREE.Mesh(rg,rm);rr.rotation.x=Math.PI/2+i*.33;rr.rotation.y=i*.7;group.add(rr)}}
const starsGeo=new THREE.BufferGeometry(), N=700, pos=new Float32Array(N*3);for(let i=0;i<N;i++){{pos[i*3]=(Math.random()-.5)*18;pos[i*3+1]=(Math.random()-.5)*10;pos[i*3+2]=(Math.random()-.5)*12-2}}starsGeo.setAttribute('position',new THREE.BufferAttribute(pos,3));scene.add(new THREE.Points(starsGeo,new THREE.PointsMaterial({{color:'{status_color}',size:.045,transparent:true,opacity:.65,blending:THREE.AdditiveBlending}})));
const pGeo=new THREE.BufferGeometry(),PN={1000 if final else 360},pp=new Float32Array(PN*3);for(let i=0;i<PN;i++){{const a=Math.random()*Math.PI*2,r=1.8+Math.random()*2.2;pp[i*3]=Math.cos(a)*r;pp[i*3+1]=(Math.random()-.5)*3.8;pp[i*3+2]=Math.sin(a)*r}}pGeo.setAttribute('position',new THREE.BufferAttribute(pp,3));scene.add(new THREE.Points(pGeo,new THREE.PointsMaterial({{color:'{status_color}',size:{.075 if final else .045},transparent:true,opacity:.55,blending:THREE.AdditiveBlending}})));
const clock=new THREE.Clock();function anim(){{requestAnimationFrame(anim);const t=clock.getElapsedTime();outer.rotation.x=t*.25;outer.rotation.y=t*.38;core.rotation.y=-t*.7;group.children.forEach((o,i)=>{{if(i>=2){{o.rotation.z=t*(.18+i*.05);o.rotation.x=t*(.12+i*.03)}}}});group.position.y=-.25+Math.sin(t*1.4)*.07;renderer.render(scene,cam)}}anim();
addEventListener('resize',()=>{{cam.aspect=innerWidth/innerHeight;cam.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight)}});
</script></body></html>"""
    components.html(js, height=500, scrolling=False)


def render_title_badge(title):
    if title == TITLE_DEFAULT:
        return "<div class='title-badge'><div class='sub'>EQUIPPED TITLE</div><div class='name'>칭호 없음</div></div>"
    idx = st.session_state.unlocked_titles.index(title) if title in st.session_state.unlocked_titles else 0
    shapes = ["◆", "✦", "⬢", "✧", "✺", "◈", "✦", "✹"]
    return f"<div class='title-badge'><div class='sub'>EQUIPPED TITLE · RANK {idx+1}</div><div class='name'>{shapes[idx%len(shapes)]} {title} {shapes[idx%len(shapes)]}</div></div>"


# -----------------------------------------------------------------------------
# 8. 메인 화면
# -----------------------------------------------------------------------------
max_lvl = 25 if st.session_state.is_rebirth else 35
curr = st.session_state.level
data = SMELL_DB[st.session_state.is_rebirth][curr]
sp, down_p, destroy_p, hold_p = PROB_TABLE[st.session_state.is_rebirth].get(curr, (5.0,40.0,50.0,5.0))
cost = get_enhance_cost(curr, st.session_state.is_rebirth)
pity_left = max(0, PITY_MAX - st.session_state.pity_count)
status_name, status_color, status_desc = _status_meta(st.session_state.status)

# 자동 강화: 버튼을 누를 때마다 1회씩 처리하고 다시 렌더링
if st.session_state.auto_enhancing:
    if curr >= min(int(st.session_state.auto_target), max_lvl):
        st.session_state.auto_enhancing = False
    else:
        if do_enhance_once():
            time.sleep(0.15)
            st.rerun()
        st.session_state.auto_enhancing = False

season = "SEASON 02 · REBIRTH" if st.session_state.is_rebirth else "SEASON 01 · ORIGIN"

st.markdown(f"""
<div style='display:flex;justify-content:space-between;align-items:center;margin:2px 2px 14px'>
<div><div class='nx-label'>ZION // NEXUS ENHANCEMENT</div><div style='font-size:30px;font-weight:950;letter-spacing:-1.2px'>지온냄새 <span style='color:#8ea6c7'>NEXUS</span></div><div class='nx-muted'>강화 · 성장 · 업적 · 칭호 · 상점을 하나의 허브로 통합</div></div>
<div style='text-align:right'><span class='nx-pill'>● ONLINE</span><div style='font-size:10px;color:#657b99;margin-top:6px;letter-spacing:1.5px'>{season}</div></div>
</div>""", unsafe_allow_html=True)

# 상단 상태 바
m1,m2,m3,m4,m5 = st.columns(5)
with m1: st.metric("CURRENT LEVEL", f"+{curr}", f"MAX {max_lvl}")
with m2: st.metric("SUCCESS RATE", f"{sp:.1f}%", f"CRIT +{int(st.session_state.crit_boost*100)}%")
with m3: st.metric("NEXT COST", format_gold(cost), "강화 비용")
with m4: st.metric("PITY CORE", f"{pity_left}회", f"방지 {st.session_state.shield}")
with m5: st.metric("NEXUS POINT", f"{st.session_state.points:,}P", f"눈물 {st.session_state.tears}/80")

# 메인 탭
tab_enh, tab_title, tab_ach, tab_shop, tab_history = st.tabs(["⚡ 강화 코어", "✦ 칭호 아틀라스", "🏆 업적", "🛒 넥서스 상점", "📜 강화 기록"])

with tab_enh:
    left, center, right = st.columns([2.15, 5.4, 2.15], gap="medium")
    with left:
        st.markdown("<div class='nx-card'><div class='nx-label'>CURRENT CORE</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='nx-big'>+{curr} <span style='font-size:13px;color:#7186a5'>/ {max_lvl}</span></div>", unsafe_allow_html=True)
        st.progress(curr/max_lvl if max_lvl else 0, text=f"진행도 {curr/max_lvl*100:.1f}%")
        st.markdown(f"<div class='nx-title' style='color:{data['color']}'>{data['name']}</div><div class='nx-muted' style='line-height:1.65;margin-top:5px'>{data['desc']}</div></div>", unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div><div class='nx-label'>PROBABILITY MATRIX</div>", unsafe_allow_html=True)
        for label,val in [("SUCCESS",sp),("DOWN",down_p),("DESTROY",destroy_p),("HOLD",hold_p)]:
            cls={"SUCCESS":"#39d8ff","DOWN":"#ffd45c","DESTROY":"#ff5b78","HOLD":"#8ea1bb"}[label]
            st.markdown(f"<div style='display:flex;justify-content:space-between;margin:7px 0 3px;font-size:10px'><span style='color:#7186a5'>{label}</span><b style='color:{cls}'>{val:.1f}%</b></div><div style='height:5px;border-radius:99px;background:#0e1b2e'><div style='width:{min(100,val)}%;height:100%;background:{cls};box-shadow:0 0 10px {cls}'></div></div>", unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        a,b=st.columns(2)
        with a: st.metric("GOLD", format_gold(st.session_state.money))
        with b: st.metric("TEARS", f"{st.session_state.tears}/80")
        if st.button("🎁 오늘의 보급품", use_container_width=True, disabled=st.session_state.daily_claimed, key="daily_nexus"):
            claim_daily_reward(); st.rerun()
        if not st.session_state.is_rebirth and curr >= 35:
            if st.button("🌀 REBIRTH · 시즌 2", use_container_width=True, type="primary", key="rebirth_nexus"):
                trigger_rebirth(); st.rerun()

    with center:
        render_3d_core(curr, max_lvl, data, st.session_state.status)

    with right:
        st.markdown("<div class='nx-label'>CORE STATUS</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='nx-card' style='border-color:{status_color}55'><div style='font-size:22px;font-weight:950;color:{status_color}'>{status_name}</div><div class='nx-muted' style='margin-top:5px;line-height:1.5'>{status_desc}</div></div>", unsafe_allow_html=True)
        st.markdown("<div style='height:8px'></div><div class='nx-label'>CORE RESOURCES</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='nx-card'><div class='nx-muted'>🛡 방지권</div><div style='font-size:22px;font-weight:950'>{st.session_state.shield} <span class='nx-muted'>/ 3</span></div><hr><div class='nx-muted'>✨ 천장까지</div><div style='font-size:22px;font-weight:950'>{pity_left}<span class='nx-muted'> 회</span></div><hr><div class='nx-muted'>⚡ 강화 시도</div><div style='font-size:22px;font-weight:950'>{st.session_state.enhance_attempts:,}</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='nx-label' style='margin-top:6px'>ENHANCEMENT CONTROL</div>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns([1.05,1.05,3.0,1.7])
    with c1:
        if st.button("− 1", use_container_width=True, key="nx_minus"):
            st.session_state.level=max(0,curr-1); st.session_state.status="HOLD"; save_current_season_state(); st.rerun()
    with c2:
        if st.button("+ 1", use_container_width=True, key="nx_plus", disabled=curr>=max_lvl):
            st.session_state.level=min(max_lvl,curr+1); st.session_state.max_level=max(st.session_state.max_level,st.session_state.level); st.session_state.status="SUCCESS"; check_achievements(); save_current_season_state(); st.rerun()
    with c3:
        if st.button(f"⚡ CORE ENHANCE · {format_gold(cost)}", use_container_width=True, type="primary", disabled=curr>=max_lvl, key="nx_enhance"):
            if do_enhance_once(): st.rerun()
    with c4:
        target=st.number_input("자동 목표", min_value=min(max_lvl,curr+1), max_value=max_lvl, value=min(max_lvl,curr+5), step=1, key="nx_auto_target")
        label="⏹ 자동 강화 중지" if st.session_state.auto_enhancing else "▶ 자동 강화 시작"
        if st.button(label, use_container_width=True, disabled=curr>=max_lvl, key="nx_auto"):
            st.session_state.auto_enhancing=not st.session_state.auto_enhancing
            st.session_state.auto_target=int(target)
            st.rerun()

    with st.expander("🔧 코어 상세 정보", expanded=False):
        x1,x2,x3,x4=st.columns(4)
        x1.metric("현재 가치", format_gold(data["price"]))
        x2.metric("방지권", f"{st.session_state.shield}/3")
        x3.metric("크리티컬 부스트", f"+{int(st.session_state.crit_boost*100)}%")
        x4.metric("환생 횟수", f"{st.session_state.rebirth_count}회")

with tab_title:
    options=[TITLE_DEFAULT]+st.session_state.unlocked_titles
    if st.session_state.selected_title not in options: st.session_state.selected_title=TITLE_DEFAULT
    st.markdown("<div class='nx-label'>TITLE ATLAS // EQUIPMENT</div><div style='font-size:24px;font-weight:950;margin:3px 0 12px'>칭호를 장착하고 강화 기록에 개성을 추가하세요.</div>", unsafe_allow_html=True)
    col1,col2=st.columns([1.1,2.0])
    with col1:
        selected=st.selectbox("장착할 칭호", options, index=options.index(st.session_state.selected_title), key="nx_title_select")
        st.session_state.selected_title=selected
        st.markdown(render_title_badge(selected), unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='nx-card'><div class='nx-label'>UNLOCKED TITLES</div>", unsafe_allow_html=True)
        if not st.session_state.unlocked_titles:
            st.markdown("<div style='padding:24px 0;text-align:center;color:#7186a5'>아직 해금된 칭호가 없습니다.<br>업적을 달성하면 새로운 칭호가 열립니다.</div>", unsafe_allow_html=True)
        else:
            cols=st.columns(3)
            for i,t in enumerate(st.session_state.unlocked_titles):
                with cols[i%3]:
                    st.markdown(f"<div class='title-badge' style='margin-bottom:8px'><div style='font-size:20px'>{['◆','✦','⬢','✧','✺','◈'][i%6]}</div><div class='name' style='font-size:13px'>{t}</div></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

with tab_ach:
    achieved=sum(st.session_state.achievements.values())
    st.markdown(f"<div class='nx-label'>ACHIEVEMENT ARCHIVE</div><div style='font-size:24px;font-weight:950'>업적 {achieved} / {len(ACHIEVEMENTS)}</div>", unsafe_allow_html=True)
    st.progress(achieved/max(1,len(ACHIEVEMENTS)), text=f"전체 달성률 {achieved/max(1,len(ACHIEVEMENTS))*100:.1f}%")
    cols=st.columns(3)
    for i,(key,info) in enumerate(ACHIEVEMENTS.items()):
        done=st.session_state.achievements.get(key,False)
        border="#39d8ff" if done else "#1b3558"
        bg="rgba(31,93,130,.18)" if done else "rgba(8,16,29,.75)"
        with cols[i%3]:
            st.markdown(f"<div style='min-height:96px;margin:5px 0;padding:12px;border:1px solid {border}66;border-radius:14px;background:{bg}'><div style='font-size:12px;font-weight:950'>{'✓' if done else '○'} {info['name']}</div><div style='font-size:10px;color:#7f93ad;margin-top:5px;line-height:1.45'>{info['desc']}</div><div style='font-size:9px;color:#ffd45c;margin-top:7px'>보상 · {format_gold(info['reward'])} · {info['title']}</div></div>", unsafe_allow_html=True)

with tab_shop:
    st.markdown(f"<div class='nx-label'>NEXUS SHOP</div><div style='font-size:24px;font-weight:950'>보유 포인트 <span style='color:#ffd45c'>{st.session_state.points:,}P</span></div>", unsafe_allow_html=True)
    q1,q2,q3,q4=st.columns(4)
    with q1:
        st.markdown("<div class='nx-card'><div style='font-size:28px'>⚡</div><div class='nx-title'>CRITICAL CORE</div><div class='nx-muted'>크리티컬 +10%</div></div>", unsafe_allow_html=True)
        if st.button("150P 구매",use_container_width=True,key="shop_crit"):
            if buy_crit_boost(): st.rerun()
    with q2:
        st.markdown("<div class='nx-card'><div style='font-size:28px'>🛡️</div><div class='nx-title'>SHIELD MODULE</div><div class='nx-muted'>방지권 +1</div></div>", unsafe_allow_html=True)
        if st.button("200P 구매",use_container_width=True,key="shop_shield",disabled=st.session_state.shield>=3):
            if st.session_state.points>=200:
                st.session_state.points-=200;st.session_state.shield+=1;save_current_season_state();st.rerun()
            else: st.error("200P가 필요합니다.")
    with q3:
        st.markdown("<div class='nx-card'><div style='font-size:28px'>💧</div><div class='nx-title'>TEAR MODULE</div><div class='nx-muted'>눈물 +10</div></div>", unsafe_allow_html=True)
        if st.button("100P 구매",use_container_width=True,key="shop_tear",disabled=st.session_state.tears>=80):
            if st.session_state.points>=100:
                st.session_state.points-=100;st.session_state.tears=min(80,st.session_state.tears+10);save_current_season_state();st.rerun()
            else: st.error("100P가 필요합니다.")
    with q4:
        st.markdown("<div class='nx-card'><div style='font-size:28px'>🎁</div><div class='nx-title'>DAILY SUPPLY</div><div class='nx-muted'>무료 출석 보상</div></div>", unsafe_allow_html=True)
        if st.button("오늘의 보상 받기",use_container_width=True,disabled=st.session_state.daily_claimed,key="shop_daily"):
            claim_daily_reward();st.rerun()

with tab_history:
    st.markdown("<div class='nx-label'>ENHANCEMENT LOG</div><div style='font-size:24px;font-weight:950'>최근 강화 기록</div>", unsafe_allow_html=True)
    if not st.session_state.enhance_history:
        st.markdown("<div class='nx-card' style='text-align:center;padding:35px;color:#7186a5'>아직 기록이 없습니다.</div>", unsafe_allow_html=True)
    else:
        for h in st.session_state.enhance_history:
            icon={"SUCCESS":"✦","CRITICAL":"⚡","PITY_SUCCESS":"◈","FAILED":"▼","DESTROYED":"✕","SHIELD_SAVED":"🛡","HOLD":"•"}.get(h['status'],"•")
            cls="history-ok" if h['status'] in {"SUCCESS","CRITICAL","PITY_SUCCESS","SHIELD_SAVED"} else ("history-bad" if h['status'] in {"FAILED","DESTROYED"} else "history-neutral")
            st.markdown(f"<div class='history-row'><span class='{cls}'>{icon} +{h['before']} → <b>+{h['after']}</b> · {h['status']}</span><span style='color:#617590'>{h['time']}</span></div>",unsafe_allow_html=True)

# 하단 글로벌 컨트롤
st.markdown("<hr>", unsafe_allow_html=True)
footer1,footer2,footer3,footer4=st.columns([2.2,1.3,1.3,2.2])
with footer1:
    st.markdown(f"<span class='nx-muted'>현재 시즌</span> <b>{season}</b> · <span class='nx-muted'>선택 칭호</span> <b>{st.session_state.selected_title}</b>", unsafe_allow_html=True)
with footer2:
    st.caption(f"최고 기록 +{st.session_state.max_level}")
with footer3:
    st.caption(f"환생 {st.session_state.rebirth_count}회")
with footer4:
    st.caption("ZION NEXUS · Enhanced UI Edition")
