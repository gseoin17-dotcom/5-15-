import random
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# 1. 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="지이온냄새 강화하기 - TRIPLE UNIVERSE EDITION",
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


def get_enhance_cost(level, season):
  if season == 3:
    # 시즌 3 (15강 체제) 전용 비용 테이블
    cost_table = {
        0: 500000,
        1: 1500000,
        2: 4000000,
        3: 10000000,
        4: 25000000,
        5: 60000000,
        6: 150000000,
        7: 350000000,
        8: 800000000,
        9: 2000000000,
        10: 5000000000,
        11: 12000000000,
        12: 30000000000,
        13: 75000000000,
        14: 180000000000,
        15: 500000000000,
    }
    return cost_table.get(level, 500000000000)
  elif season == 2:
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


def get_shield_cost(level, season):
  base_cost = get_enhance_cost(level, season)
  return max(50000, base_cost * 15)


# -----------------------------------------------------------------------------
# 3. 게임 데이터베이스 정의 (모든 이름에 '지이온' 포함)
# -----------------------------------------------------------------------------
SMELL_DB = {
    1: {
        0: {
            "name": "0단계 : 무취 지이온의 공간",
            "desc": "아직은 아무 냄새도 안 남. 지이온이가 씻었나 봄.",
            "price": 0,
            "color": "#4a5568",
            "tier": 1,
        },
        1: {
            "name": "1단계 : 스쳐가는 지이온냄새",
            "desc": "버스 옆자리에 앉은 지이온이가 팔을 들 때 스치듯 나는 가벼운 암내.",
            "price": 150,
            "color": "#718096",
            "tier": 1,
        },
        2: {
            "name": "2단계 : 은은한 지이온냄새",
            "desc": "체육 시간이 끝난 뒤 지이온이가 벗어던진 축축한 양말 냄새.",
            "price": 400,
            "color": "#38a169",
            "tier": 1,
        },
        3: {
            "name": "3단계 : 습한 지이온냄새",
            "desc": "사흘 동안 빨지 않은 지이온이의 후드티 모자에 쩐내.",
            "price": 600,
            "color": "#276749",
            "tier": 1,
        },
        4: {
            "name": "4단계 : 진득한 지이온냄새",
            "desc": (
                "여름철 밀폐된 방 안에서 지이온이가 뒹굴다 난 땀에 쩐 이불 냄새."
            ),
            "price": 800,
            "color": "#319795",
            "tier": 1,
        },
        5: {
            "name": "5단계 : 자극적인 지이온냄새",
            "desc": "지이온이가 발가락을 긁은 손으로 코를 슥 만지게 만드는 향.",
            "price": 3000,
            "color": "#2c7a7b",
            "tier": 1,
        },
        6: {
            "name": "6단계 : 풍부한 지이온냄새",
            "desc": "신발장에 박아둔 지이온이의 축구화 속에서 무르익은 발효 냄새.",
            "price": 3500,
            "color": "#3182ce",
            "tier": 2,
        },
        7: {
            "name": "7단계 : 압도적인 지이온냄새",
            "desc": (
                "지이온이가 다녀간 자리마다 코를 찌르는 시큼털털한 체취의 파도."
            ),
            "price": 6100,
            "color": "#2b6cb0",
            "tier": 2,
        },
        8: {
            "name": "8단계 : 폭발하는 지이온냄새",
            "desc": (
                "일주일 동안 안 감은 지이온이 머리통에서 뿜어져 나오는 유분"
                " 폭탄."
            ),
            "price": 10000,
            "color": "#805ad5",
            "tier": 2,
        },
        9: {
            "name": "9단계 : 시공을 뒤흔드는 지이온냄새",
            "desc": "화장실 문을 열자마자 지이온이가 남기고 간 흔적의 생생함.",
            "price": 20000,
            "color": "#6b46c1",
            "tier": 2,
        },
        10: {
            "name": "10단계 : 치명적인 지이온냄새",
            "desc": "맡는 순간 안구실종을 유발하는 지이온이의 살인적인 입냄새.",
            "price": 35100,
            "color": "#d69e2e",
            "tier": 2,
        },
        11: {
            "name": "11단계 : 환각을 부르는 지이온냄새",
            "desc": (
                "썩은 청국장과 지이온이의 발냄새가 콜라보를 이뤄 주마등이"
                " 스친다."
            ),
            "price": 160000,
            "color": "#b7791f",
            "tier": 3,
        },
        12: {
            "name": "12단계 : 공간지배 지이온냄새",
            "desc": (
                "방 문을 열기도 전에 복도까지 마중 나온 지이온이의 찌든 내음."
            ),
            "price": 350000,
            "color": "#dd6b20",
            "tier": 3,
        },
        13: {
            "name": "13단계 : 전성기 지이온냄새",
            "desc": (
                "음식물 쓰레기통을 여름볕에 사흘간 방치한 것과 비견되는 향."
            ),
            "price": 1000000,
            "color": "#c05621",
            "tier": 3,
        },
        14: {
            "name": "14단계 : 신성한 지이온냄새",
            "desc": (
                "너무 지독해서 눈물마저 고이게 만드는 지이온이의 꼬릿한 기운."
            ),
            "price": 3000000,
            "color": "#e53e3e",
            "tier": 3,
        },
        15: {
            "name": "15단계 : 오리지널 지이온냄새",
            "desc": (
                "하수구 역류 현상과 지이온이의 입김이 만나 온 세상이 오염된다."
            ),
            "price": 7500000,
            "color": "#9b2c2c",
            "tier": 3,
        },
        16: {
            "name": "16단계 : 우주관통 지이온냄새",
            "desc": (
                "대기권을 뚫고 오존층마저 뻥 뚫어버리는 지이온이의 겨드랑이"
                " 폭풍."
            ),
            "price": 14200000,
            "color": "#00f0ff",
            "tier": 4,
        },
        17: {
            "name": "17단계 : 차원균열 지이온냄새",
            "desc": (
                "지이온이의 구린내가 너무 독해서 다른 평행세계의 코까지"
                " 썩힌다."
            ),
            "price": 20000000,
            "color": "#ff00ea",
            "tier": 4,
        },
        18: {
            "name": "18단계 : Absolute 지이온냄새",
            "desc": (
                "우주 만물의 원소를 전부 지이온이의 체취로 치환해버리는"
                " 절대악취."
            ),
            "price": 30000000,
            "color": "#ffe600",
            "tier": 4,
        },
        19: {
            "name": "19단계 : 초월 지이온냄새",
            "desc": "인간의 후각 세포를 단번에 파괴하는 초월적인 썩은 내.",
            "price": 47500000,
            "color": "#ff0055",
            "tier": 4,
        },
        20: {
            "name": "20단계 : 지이온이의 정성이 들어간 포근한 집밥 냄새",
            "desc": (
                "지이온맘이 끓여준 묵은지 김치찌개... 인 줄 알았으나 지이온이"
                " 빨래 냄새."
            ),
            "price": 68300000,
            "color": "#ffaa00",
            "tier": 4,
        },
        21: {
            "name": "21단계 : 지이온이의 엄격한 샤우팅 냄새",
            "desc": (
                "안 씻고 버티는 지이온이를 잡으려고 지이온맘이 휘두른 등짝의"
                " 내음."
            ),
            "price": 101000000,
            "color": "#ff4500",
            "tier": 5,
        },
        22: {
            "name": "22단계 : 지이온이의 전설의 흙된장국 냄새",
            "desc": (
                "지이온이의 발냄새 원액을 살짝 타서 깊은 맛을 낸 지이온맘의"
                " 특제 국물."
            ),
            "price": 160000000,
            "color": "#ff007f",
            "tier": 5,
        },
        23: {
            "name": "23단계 : 지이온이의 100년 숙성 원액 냄새",
            "desc": (
                "지이온이가 어릴 때부터 모아둔 꼬릿한 때를 장독대에 묻어"
                " 숙성시켰다."
            ),
            "price": 230000000,
            "color": "#7b00ff",
            "tier": 5,
        },
        24: {
            "name": "24단계 : 지이온이의 냄새 탈취 스프레이 냄새",
            "desc": (
                "방 안에 쩔어 있는 지이온이의 체취를 탈취제로 잡으려다"
                " 역관람당함."
            ),
            "price": 300000000,
            "color": "#0088ff",
            "tier": 5,
        },
        25: {
            "name": "25단계 : 지이온이의 대인배적인 냄새",
            "desc": (
                "이런 지이온이라도 품에 안아주는 지이온맘의 대인배적 냄새"
                " 포용력."
            ),
            "price": 400000000,
            "color": "#00ffaa",
            "tier": 5,
        },
        26: {
            "name": "26단계 : 지이온이의 궁극 필살기 냄새",
            "desc": (
                "지이온이 방 문을 강제로 열고 환기시키며 뿜어내는 지이온맘의"
                " 분노."
            ),
            "price": 1800000000,
            "color": "#ccff00",
            "tier": 6,
        },
        27: {
            "name": "27단계 : 지이온이의 창조와 냄새",
            "desc": (
                "지이온이의 모든 악취를 정화하려다 지이온맘마저 구속당한 경지."
            ),
            "price": 2500000000,
            "color": "#fffb00",
            "tier": 6,
        },
        28: {
            "name": "28단계 : 지이온이의 우주창조설 냄새",
            "desc": (
                "우주 전체가 지이온이의 발냄새 아래 무릎을 꿇고 헛구역질을"
                " 한다."
            ),
            "price": 5500000000,
            "color": "#ffffff",
            "tier": 6,
        },
        29: {
            "name": "29단계 : 딥다크 지이온냄새",
            "desc": (
                "모든 꼬릿한 냄새의 근원이자, 지이온이를 낳고 기른 위대한"
                " 악취의 여신."
            ),
            "price": 10500000000,
            "color": "#ff00aa",
            "tier": 6,
        },
        30: {
            "name": "30단계 : 태초의 지이온냄새 ",
            "desc": "우주 탄생 이전부터 존재했던 오리지널 태고의 구린내.",
            "price": 20000000000,
            "color": "#00ffff",
            "tier": 6,
        },
        31: {
            "name": "31단계 : 하이퍼 지이온 싱귤래리티",
            "desc": (
                "냄새가 너무 묵직해서 블랙홀처럼 주변 모든 빛과 산소를"
                " 빨아들인다."
            ),
            "price": 45000000000,
            "color": "#7000ff",
            "tier": 6,
        },
        32: {
            "name": "32단계 : 멀티버스 지이온 에센스",
            "desc": (
                "모든 평행우주에 존재하는 지이온이의 체취가 한곳으로 모이는"
                " 중."
            ),
            "price": 90000000000,
            "color": "#ff00e1",
            "tier": 6,
        },
        33: {
            "name": "33단계 : 인피니티 지이온 페트리코",
            "desc": (
                "영원히 끝나지 않는 지이온이의 발효 비린내가 온 은하를 뒤덮음."
            ),
            "price": 200000000000,
            "color": "#00ff66",
            "tier": 6,
        },
        34: {
            "name": "34단계 : 오메가 지이온 제네시스",
            "desc": (
                "지이온이의 냄새로 우주를 멸망시키고 다시 창조하는 종말의 향기."
            ),
            "price": 500000000000,
            "color": "#ff6600",
            "tier": 6,
        },
        35: {
            "name": "35단계 : ★디 오리지널 앱솔루트 지이온★",
            "desc": "우주 만물을 통틀어 가장 지독하고 완벽한 궁극의 지이온 냄새.",
            "price": 1000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
    },
    2: {
        0: {
            "name": "환생 0단계 : 초신성 핵폐기물 자이이온",
            "desc": "환생을 거쳐 새롭게 압축된 태초의 고밀도 지이온 방사능 악취.",
            "price": 1000000000,
            "color": "#ff0055",
            "tier": 1,
        },
        1: {
            "name": "환생 1단계 : 안드로메다 자이이온 암모니아",
            "desc": "안드로메다 은하 전체를 지이온 암모니아 폭풍으로 알칼리화.",
            "price": 2500000000,
            "color": "#00ffff",
            "tier": 1,
        },
        2: {
            "name": "환생 2단계 : 화이트홀 자이이온 하이드로겐",
            "desc": "우주 백색왜성과 지이온 체취가 결합된 순백의 악취 폭발.",
            "price": 6000000000,
            "color": "#ffffff",
            "tier": 1,
        },
        3: {
            "name": "환생 3단계 : 쿼크 글루온 자이이온 악취",
            "desc": "소립자 수준에서 지이온 입자와 강하게 결합된 쿼크급 냄새.",
            "price": 15000000000,
            "color": "#ffaa00",
            "tier": 2,
        },
        4: {
            "name": "환생 4단계 : 차원왜곡 자이이온 타임루프 찌든내",
            "desc": "지이온 체취로 인해 시간의 흐름마저 썩어버린 찌든내 집합체.",
            "price": 35000000000,
            "color": "#9b2c2c",
            "tier": 2,
        },
        5: {
            "name": "환생 5단계 : 네메시스 자이이온 다크매터",
            "desc": "빛조차 탈출하지 못하고 지이온 악취에 붙잡힌 암흑물질.",
            "price": 80000000000,
            "color": "#38a169",
            "tier": 2,
        },
        6: {
            "name": "환생 6단계 : 메가 블랙홀 자이이온 호라이즌",
            "desc": "모든 물리 법칙이 붕괴하고 오직 지이온 체취만 남는 경계선.",
            "price": 180000000000,
            "color": "#805ad5",
            "tier": 3,
        },
        7: {
            "name": "환생 7단계 : 감마선 버스트 자이이온 플레어",
            "desc": "우주 끝까지 수십 광년 동안 뻗어 나가는 지이온 살인 악취.",
            "price": 400000000000,
            "color": "#e53e3e",
            "tier": 3,
        },
        8: {
            "name": "환생 8단계 : 하이퍼노바 자이이온 코어 붕괴",
            "desc": "거대 항성이 지이온의 기운으로 생을 마감하며 방출하는 악취.",
            "price": 900000000000,
            "color": "#ff4500",
            "tier": 3,
        },
        9: {
            "name": "환생 9단계 : 엘더블루 제네시스 지이온",
            "desc": "태초의 우주 생성 전 존재했던 지이온 고유의 푸른 시원 냄새.",
            "price": 2000000000000,
            "color": "#0088ff",
            "tier": 4,
        },
        10: {
            "name": "환생 10단계 : 카이퍼 지이온 벨트 코스믹 더스트",
            "desc": "태양계 외곽의 얼어붙은 조각들에 스며든 지이온 원시 악취.",
            "price": 4500000000000,
            "color": "#cbd5e1",
            "tier": 4,
        },
        11: {
            "name": "환생 11단계 : 지이온오르트 클라우드 딥 프리즈",
            "desc": "극저온 속에서 서서히 발효된 냉동 지이온 체취.",
            "price": 10000000000000,
            "color": "#319795",
            "tier": 4,
        },
        12: {
            "name": "환생 12단계 : 태양풍 플라즈마 지이온제트",
            "desc": "태양 표면에서 뿜어져 나오는 고온다습 지이온 플라즈마 냄새.",
            "price": 22000000000000,
            "color": "#f59e0b",
            "tier": 5,
        },
        13: {
            "name": "환생 13단계 : 마그네타 지이온자기장 폭풍",
            "desc": "우주의 모든 나침반을 고장 내는 지이온 자기장 폭풍.",
            "price": 50000000000000,
            "color": "#7000ff",
            "tier": 5,
        },
        14: {
            "name": "환생 14단계 : 펄서 지이온로테이션 시그널",
            "desc": "강력한 지이온 악취 전파를 우주 전역에 송출하는 중성자별.",
            "price": 120000000000000,
            "color": "#00ff66",
            "tier": 5,
        },
        15: {
            "name": "환생 15단계 : 웜홀 크로스오버 지이온 디멘션",
            "desc": "시공간 통로를 열어 다른 차원의 지이온 구린내를 강제 소환.",
            "price": 280000000000000,
            "color": "#ff00ea",
            "tier": 6,
        },
        16: {
            "name": "환생 16단계 : 스트링 시스코어 지이온 엠피리어",
            "desc": "초끈이론의 11차원을 진동시키는 지이온 궁극의 우주 진동음.",
            "price": 600000000000000,
            "color": "#ccff00",
            "tier": 6,
        },
        17: {
            "name": "환생 17단계 : 센타우루스 지이온 알파 코어",
            "desc": "가장 가까운 별무리의 기운을 지이온 향기로 통째로 오염.",
            "price": 1300000000000000,
            "color": "#ff6600",
            "tier": 6,
        },
        18: {
            "name": "환생 18단계 : 페가수스 지이온 별자리 네뷸라",
            "desc": "날개 든 말의 질주를 따라 하늘에 퍼지는 지이온 성운 향.",
            "price": 3000000000000000,
            "color": "#00f0ff",
            "tier": 6,
        },
        19: {
            "name": "환생 19단계 : 지이온세인트 오메가 에센스",
            "desc": "우주의 수명이 다할 때까지 사라지지 않는 불멸의 지이온 냄새.",
            "price": 7000000000000000,
            "color": "#ffe600",
            "tier": 6,
        },
        20: {
            "name": "환생 20단계 : 코스믹 인피니티 싱귤지이온",
            "desc": "모든 평행우주와 차원의 지이온 존재가 응축된 무한대 악취.",
            "price": 15000000000000000,
            "color": "#ff00aa",
            "tier": 6,
        },
        21: {
            "name": "환생 21단계 : 지이온트랜스센던탈 가디언",
            "desc": "차원의 벽을 넘어 초월적인 신위를 뿜어내는 지이온 가디언.",
            "price": 35000000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
        22: {
            "name": "환생 22단계 : 하이퍼 지이온 디바인 코어",
            "desc": "지이온이라는 존재 자체가 우주의 신성한 법칙으로 등극.",
            "price": 80000000000000000,
            "color": "#7b00ff",
            "tier": 6,
        },
        23: {
            "name": "환생 23단계 : 지이온옴니버스 마스터피스",
            "desc": "모든 평행세계를 통틀어 단 하나뿐인 완벽한 지이온 걸작 악취.",
            "price": 200000000000000000,
            "color": "#00ffff",
            "tier": 6,
        },
        24: {
            "name": "환생 24단계 : 이터널 제네시스 울티마지이온",
            "desc": "우주의 탄생과 종말을 지이온 향기로 영원히 반복시키는 고리.",
            "price": 500000000000000000,
            "color": "#ff4500",
            "tier": 6,
        },
        25: {
            "name": "환생 25단계 : ★심플 성지이온★",
            "desc": "문일중 3학년 5반의 지이온 냄새를 담당하는 절대 GOA.T",
            "price": 1000000000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
    },
    3: {
        0: {
            "name": "시즌3 0단계 : 지이온의 태초의 입김",
            "desc": "시즌3의 시작을 알리는 맑고 청정한 지이온의 첫 숨결.",
            "price": 2000000,
            "color": "#3b82f6",
            "tier": 1,
        },
        1: {
            "name": "시즌3 1단계 : 미풍의 지이온 체취",
            "desc": "살랑이는 바람을 타고 은은하게 퍼지는 지이온의 체취.",
            "price": 5000000,
            "color": "#06b6d4",
            "tier": 1,
        },
        2: {
            "name": "시즌3 2단계 : 서늘한 지이온 수증기",
            "desc": "샤워 직후 지이온의 욕실 문틈으로 새어 나오는 습한 향기.",
            "price": 12000000,
            "color": "#10b981",
            "tier": 1,
        },
        3: {
            "name": "시즌3 3단계 : 진한 지이온 보리차 냄새",
            "desc": "지이온이 하루 종일 우려 마시고 방치한 구수한 보리차 향.",
            "price": 30000000,
            "color": "#84cc16",
            "tier": 2,
        },
        4: {
            "name": "시즌3 4단계 : 훈훈한 지이온 체온 향",
            "desc": "겨울날 지이온이 덮고 자던 두툼한 이불에서 나는 포근한 냄새.",
            "price": 70000000,
            "color": "#eab308",
            "tier": 2,
        },
        5: {
            "name": "시즌3 5단계 : 밀폐된 지이온 독방 훈연",
            "desc": "환기하지 않은 지이온의 방에서 무르익기 시작한 농밀한 향.",
            "price": 160000000,
            "color": "#f59e0b",
            "tier": 2,
        },
        6: {
            "name": "시즌3 6단계 : 숙성된 지이온 매직 발효액",
            "desc": "오랫동안 빨래통에 잠들어 있던 지이온의 양말 숙성 원액.",
            "price": 350000000,
            "color": "#f97316",
            "tier": 3,
        },
        7: {
            "name": "시즌3 7단계 : 강력한 지이온 스톰 브레스",
            "desc": "아침에 눈을 뜬 지이온이 내뱉는 강력하고 짜릿한 입김.",
            "price": 800000000,
            "color": "#ef4444",
            "tier": 3,
        },
        8: {
            "name": "시즌3 8단계 : 전설의 지이온 꼬릿한 레전드",
            "desc": "주변 사람들까지 코를 감싸게 만드는 지이온 고유의 꼬릿함.",
            "price": 1800000000,
            "color": "#dc2626",
            "tier": 3,
        },
        9: {
            "name": "시즌3 9단계 : 차원을 가르는 지이온 아로마",
            "desc": "후각의 한계를 아득하게 뛰어넘는 지이온 표 차원 아로마.",
            "price": 4000000000,
            "color": "#9333ea",
            "tier": 4,
        },
        10: {
            "name": "시즌3 10단계 : 하이퍼 지이온 플라즈마 코어",
            "desc": "지이온의 체취가 고압축되어 플라즈마 형태로 빛나는 경지.",
            "price": 9000000000,
            "color": "#a855f7",
            "tier": 4,
        },
        11: {
            "name": "시즌3 11단계 : 코스믹 지이온 싱귤래리티",
            "desc": "주변의 모든 공기를 지이온 향기로 정화(오염)시키는 특이점.",
            "price": 20000000000,
            "color": "#ec4899",
            "tier": 5,
        },
        12: {
            "name": "시즌3 12단계 : 인피니티 지이온 이클립스",
            "desc": "태양을 가리고 온 세상에 지이온의 그림자를 드리우는 일식.",
            "price": 45000000000,
            "color": "#f43f5e",
            "tier": 5,
        },
        13: {
            "name": "시즌3 13단계 : 앱솔루트 지이온 제네시스",
            "desc": "지이온의 악취 에너지로 새로운 우주의 법칙을 창조하는 향.",
            "price": 100000000000,
            "color": "#6366f1",
            "tier": 6,
        },
        14: {
            "name": "시즌3 14단계 : 오메가 지이온 디바인 오라",
            "desc": "신(神)의 경지에 도달한 지이온이 뿜어내는 거룩하고 진한 기운.",
            "price": 250000000000,
            "color": "#3b82f6",
            "tier": 6,
        },
        15: {
            "name": "시즌3 15단계 : ★디 얼티밋 트루 지이온갓★",
            "desc": "우주와 차원을 초월하여 완성된 단 하나의 완벽한 지이온 신(神).",
            "price": 1000000000000,
            "color": "#ffffff",
            "tier": 6,
        },
    },
}

PROB_TABLE = {
    1: {
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
    2: {
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
    3: {
        # 시즌 3 (최고 15강) 확률표
        0: (100.0, 0.0, 0.0, 0.0),
        1: (95.0, 5.0, 0.0, 0.0),
        2: (90.0, 8.0, 2.0, 0.0),
        3: (85.0, 10.0, 5.0, 0.0),
        4: (80.0, 12.0, 8.0, 0.0),
        5: (75.0, 15.0, 8.0, 2.0),
        6: (70.0, 18.0, 10.0, 2.0),
        7: (65.0, 20.0, 12.0, 3.0),
        8: (60.0, 22.0, 14.0, 4.0),
        9: (55.0, 25.0, 15.0, 5.0),
        10: (50.0, 25.0, 20.0, 5.0),
        11: (40.0, 30.0, 25.0, 5.0),
        12: (30.0, 35.0, 30.0, 5.0),
        13: (20.0, 40.0, 35.0, 5.0),
        14: (10.0, 45.0, 40.0, 5.0),
    },
}

CRITICAL_RATE = 0.05
PITY_MAX = 3

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
          "unlocked_warps": {5: False, 10: False, 15: False, 20: False},
      },
      3: {
          "level": 0,
          "max_level": 0,
          "money": 50000000000,
          "status": "READY",
          "shield": 4,
          "tears": 50,
          "pity_count": 0,
          "unlocked_warps": {5: False, 10: False},
      },
  }

if "auto_enhance" not in st.session_state:
  st.session_state.auto_enhance = False


def sync_session_state(target_season):
  st.session_state.current_season = target_season
  data = st.session_state.season_data[target_season]

  st.session_state.level = data["level"]
  st.session_state.max_level = data["max_level"]
  st.session_state.money = data["money"]
  st.session_state.status = data["status"]
  st.session_state.shield = data["shield"]
  st.session_state.tears = data["tears"]
  st.session_state.pity_count = data["pity_count"]
  st.session_state.unlocked_warps = data["unlocked_warps"]


def save_current_season_state():
  s = st.session_state.current_season
  st.session_state.season_data[s]["level"] = st.session_state.level
  st.session_state.season_data[s]["max_level"] = st.session_state.max_level
  st.session_state.season_data[s]["money"] = st.session_state.money
  st.session_state.season_data[s]["status"] = st.session_state.status
  st.session_state.season_data[s]["shield"] = st.session_state.shield
  st.session_state.season_data[s]["tears"] = st.session_state.tears
  st.session_state.season_data[s]["pity_count"] = st.session_state.pity_count
  st.session_state.season_data[s]["unlocked_warps"] = (
      st.session_state.unlocked_warps
  )


if "current_season" not in st.session_state:
  sync_session_state(1)

# -----------------------------------------------------------------------------
# 5. 강화 로직
# -----------------------------------------------------------------------------


def run_enhance():
  save_current_season_state()
  s = st.session_state.current_season
  max_lvl = 15 if s == 3 else (25 if s == 2 else 35)
  curr = st.session_state.level
  if curr >= max_lvl:
    save_current_season_state()
    return False

  cost = get_enhance_cost(curr, s)
  if st.session_state.money < cost:
    st.session_state.status = "NOT_ENOUGH_MONEY"
    save_current_season_state()
    return False

  st.session_state.money -= cost

  if st.session_state.pity_count >= PITY_MAX - 1:
    st.session_state.level += 1
    st.session_state.status = "PITY_SUCCESS"
    st.session_state.pity_count = 0
    if st.session_state.level > st.session_state.max_level:
      st.session_state.max_level = st.session_state.level
    save_current_season_state()
    return True

  current_prob = PROB_TABLE[s]
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

  for w_lvl in st.session_state.unlocked_warps.keys():
    if st.session_state.level >= w_lvl:
      st.session_state.unlocked_warps[w_lvl] = True

  save_current_season_state()
  return True


def sell():
  save_current_season_state()
  s = st.session_state.current_season
  curr = st.session_state.level
  if curr == 0:
    return
  price_val = SMELL_DB[s][curr]["price"]
  if price_val == float("inf"):
    st.session_state.money = float("inf")
  else:
    st.session_state.money += price_val
  st.session_state.level = 0
  st.session_state.status = "READY"
  save_current_season_state()


def change_season(new_season):
  save_current_season_state()
  sync_session_state(new_season)
  st.session_state.auto_enhance = False


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
        padding-top: 4rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
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
  # 시즌 선택 버튼 바
  st.markdown(
      "<h4 style='margin:0 0 8px 0; font-size: 15px;"
      " color:#fde68a;'>🌌 시즌 선택</h4>",
      unsafe_allow_html=True,
  )
  season_col1, season_col2, season_col3 = st.columns(3)
  with season_col1:
    if st.button(
        "시즌1",
        use_container_width=True,
        type=(
            "primary" if st.session_state.current_season == 1 else "secondary"
        ),
    ):
      change_season(1)
      st.rerun()
  with season_col2:
    if st.button(
        "시즌2",
        use_container_width=True,
        type=(
            "primary" if st.session_state.current_season == 2 else "secondary"
        ),
    ):
      change_season(2)
      st.rerun()
  with season_col3:
    if st.button(
        "시즌3",
        use_container_width=True,
        type=(
            "primary" if st.session_state.current_season == 3 else "secondary"
        ),
    ):
      change_season(3)
      st.rerun()

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  # 시즌별 완료 조건 및 다음 시즌 안내
  s = st.session_state.current_season
  max_limit_lvl = 15 if s == 3 else (25 if s == 2 else 35)
  if s < 3 and st.session_state.level >= max_limit_lvl:
    st.markdown(
        f"<div"
        f" style='background:rgba(220,38,38,0.2);border:2px solid"
        f" #ef4444;padding:10px;border-radius:8px;text-align:center;margin-bottom:10px;'>"
        f"<h4 style='color:#f87171; margin:0 0 4px 0;'>✨ 차원 한계 도달</h4>"
        f"<p style='font-size:12px; color:#f1f5f9; margin:0 0 8px"
        f" 0;'>최고 단계 도달! 다음 시즌으로 넘어가시겠습니까?</p>"
        f"</div>",
        unsafe_allow_html=True,
    )
    if st.button(f"🚀 시즌 {s+1}로 이동하기", use_container_width=True):
      change_season(s + 1)
      st.rerun()
    st.markdown(
        "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )

  mode_titles = {
      1: "🌌 [시즌 1] 솔라 시스템 (35강)",
      2: "🌀 [시즌 2] 얼티밋 블랙홀 (25강)",
      3: "⚡ [시즌 3] 지이온 디바인 코어 (15강)",
  }
  st.markdown(
      f"<h4 style='margin:0 0 8px 0; font-size: 14px;"
      f" color:#fde68a;'>{mode_titles[s]}</h4>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  s_col1, s_col2 = st.columns(2)
  with s_col1:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:11px;"
        f" color:#fde68a;'>💳 보유 금액</div><div style='font-size:13px;"
        f" font-weight:800; color:#ffffff;'>{format_gold(st.session_state.money)}</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:11px;"
        f" color:#fde68a;'>💧 눈물</div><div style='font-size:14px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.tears} /"
        " 80개</div></div>",
        unsafe_allow_html=True,
    )

  with s_col2:
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:11px;"
        f" color:#fde68a;'>🛡️ 방지권</div><div style='font-size:14px;"
        f" font-weight:800; color:#ffffff;'>{st.session_state.shield} /"
        " 4개</div></div>",
        unsafe_allow_html=True,
    )
    st.write("")
    pity_left = PITY_MAX - st.session_state.pity_count
    st.markdown(
        f"<div style='text-align: center;'><div style='font-size:11px;"
        f" color:#fde68a;'>✨ 지이온맘의 가호</div><div style='font-size:12px;"
        f" font-weight:800; color:#ffffff;'>실패까지 <b>{pity_left}회</b></div></div>",
        unsafe_allow_html=True,
    )

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  curr_lvl = st.session_state.level
  current_prob = PROB_TABLE[s]
  sp, down_p, dp, hold_p = current_prob.get(curr_lvl, (5.0, 40.0, 50.0, 5.0))
  st.markdown(
      f"<h4 style='margin:0 0 4px 0; font-size: 13px; color:#fde68a;'>📊 현재"
      f" 강화 확률 ({curr_lvl}단계)</h4>",
      unsafe_allow_html=True,
  )
  st.markdown(
      f"<div style='font-size:11px; color:#cbd5e1; background:rgba(255,255,255,0.05);"
      f" padding:6px; border-radius:6px;'>"
      f"• 성공: <b style='color:#38bdf8;'>{sp}%</b> (크리 5%)<br>"
      f"• 하락: <b style='color:#facc15;'>{down_p}%</b> | 파괴: <b"
      f" style='color:#ef4444;'>{dp}%</b> | 유지: <b"
      f" style='color:#94a3b8;'>{hold_p}%</b>"
      f"</div>",
      unsafe_allow_html=True,
  )

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  tab_shop1, tab_shop2, tab_warp, tab_dev = st.tabs(
      ["🛡️ 방지권", "💧 눈물", "🚀 워프권", "🛠️ 개발자"]
  )

  with tab_shop1:
    min_shield_level = 8 if s == 3 else (16 if s == 2 else 20)
    current_shield_cost = get_shield_cost(curr_lvl, s)
    if curr_lvl < min_shield_level:
      st.markdown(
          f"<div style='font-size:12px; color:#ef4444; font-weight:700;'>⚠️"
          f" {min_shield_level}단계 이상부터 구매 가능!</div>",
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          f"<div style='font-size:12px; color:#cbd5e1;'>가격: <b"
          f" style='color:#fde68a;'>{format_gold(current_shield_cost)}</b></div>",
          unsafe_allow_html=True,
      )

    can_buy_shield = (st.session_state.shield < 4) and (
        curr_lvl >= min_shield_level
    )
    if st.button(
        "방지권 구매", use_container_width=True, disabled=not can_buy_shield
    ):
      if st.session_state.money >= current_shield_cost:
        st.session_state.money -= current_shield_cost
        st.session_state.shield += 1
        save_current_season_state()
        st.success("구매 완료!")
        st.rerun()
      else:
        st.error("금액 부족!")

  with tab_shop2:
    limit_lvl = 12 if s == 3 else (18 if s == 2 else 32)
    if curr_lvl >= limit_lvl:
      st.markdown(
          "<div style='font-size:12px; color:#ef4444; font-weight:700;'>⚠️"
          " 고단계 사용 불가</div>",
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          "<div style='font-size:12px; color:#cbd5e1;'>눈물 20개 소모 (1정확"
          " 성공)</div>",
          unsafe_allow_html=True,
      )

    can_use_tears = curr_lvl < limit_lvl
    if st.button(
        "눈물 기적 가동", use_container_width=True, disabled=not can_use_tears
    ):
      if st.session_state.tears >= 20:
        st.session_state.tears -= 20
        add_lvl = random.choice([1, 2, 3])
        st.session_state.level = min(max_limit_lvl, curr_lvl + add_lvl)
        st.session_state.status = "CRITICAL"
        save_current_season_state()
        st.success("눈물 기적 성공!")
        st.rerun()
      else:
        st.error("눈물 부족!")

  with tab_warp:
    warp_targets = (
        {5: 50000000, 10: 200000000}
        if s == 3
        else (
            {5: 50000000, 10: 200000000, 15: 1000000000, 20: 5000000000}
            if s == 2
            else {
                10: 10000000,
                15: 50000000,
                20: 200000000,
                25: 1000000000,
                30: 5000000000,
            }
        )
    )
    for w_level, w_price in warp_targets.items():
      is_unlocked = (
          st.session_state.unlocked_warps.get(w_level, False)
          or st.session_state.max_level >= w_level
      )
      c1, c2 = st.columns([1.2, 1])
      with c1:
        st.markdown(
            f"<div style='font-size:12px; font-weight:bold;'>🚀"
            f" {w_level}강</div><div"
            f" style='font-size:10px; color:#fde68a;'>{format_gold(w_price)}</div>",
            unsafe_allow_html=True,
        )
      with c2:
        if st.button(
            "이동",
            key=f"warp_{s}_{w_level}",
            disabled=not is_unlocked or (curr_lvl >= w_level),
        ):
          if st.session_state.money >= w_price:
            st.session_state.money -= w_price
            st.session_state.level = w_level
            if w_level > st.session_state.max_level:
              st.session_state.max_level = w_level
            save_current_season_state()
            st.rerun()
          else:
            st.error("금액 부족")

  with tab_dev:
    if st.button("✨ 강제 성공 (+1)", use_container_width=True):
      if curr_lvl < max_limit_lvl:
        st.session_state.level += 1
        st.session_state.status = "SUCCESS"
        if st.session_state.level > st.session_state.max_level:
          st.session_state.max_level = st.session_state.level
        save_current_season_state()
        st.rerun()
    if st.button("💰 자금 충전 (+100경)", use_container_width=True):
      st.session_state.money += 1000000000000000000
      save_current_season_state()
      st.rerun()

  st.markdown(
      "<hr style='margin:10px 0; border-color:rgba(255,255,255,0.1);'>",
      unsafe_allow_html=True,
  )

  # -----------------------------------------------------------------------------
  # 자동 강화 시스템 구현 (토글 버튼 방식)
  # -----------------------------------------------------------------------------
  st.markdown(
      "<h4 style='margin:0 0 6px 0; font-size: 14px; color:#fde68a;'>⚡ 자동 강화"
      " 시스템</h4>",
      unsafe_allow_html=True,
  )

  auto_toggle = st.toggle("자동 강화 켜기/끄기", value=st.session_state.auto_enhance)
  if auto_toggle != st.session_state.auto_enhance:
    st.session_state.auto_enhance = auto_toggle
    st.rerun()

  st.write("")
  enhance_btn = st.button(
      "🔥 냄새 강화 실행",
      use_container_width=True,
      disabled=(curr_lvl >= max_limit_lvl),
  )

  if enhance_btn:
    run_enhance()
    st.rerun()

  st.write("")
  if st.button(
      "💰 현재 냄새 판매", use_container_width=True, disabled=(curr_lvl == 0)
  ):
    sell()
    st.rerun()

  # 자동 강화가 켜져 있고 최고 단계가 아니라면 자동으로 다음 강화 실행 후 새로고침
  if st.session_state.auto_enhance and curr_lvl < max_limit_lvl:
    cost = get_enhance_cost(curr_lvl, s)
    if st.session_state.money >= cost:
      run_enhance()
      st.rerun()
    else:
      st.session_state.auto_enhance = False
      st.warning("금액이 부족하여 자동 강화를 중단합니다.")

with right_col:
  curr_data = SMELL_DB[s][curr_lvl]
  card_color = curr_data["color"]
  card_title = curr_data["name"]
  card_desc = curr_data["desc"]
  card_price = format_gold(curr_data["price"])
  current_cost = format_gold(get_enhance_cost(curr_lvl, s))
  tier = curr_data["tier"]
  status = st.session_state.status

  three_js_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; overflow: hidden; background: transparent; font-family: sans-serif; }}
            #container {{ width: 100vw; height: 100vh; position: absolute; top:0; left:0; }}
            .cinematic-ui {{
                position: absolute; bottom: 25px; left: 50%;
                transform: translateX(-50%); width: 100%; text-align: center; z-index: 100;
            }}
            .title-tier-1 {{ font-size: 28px; font-weight: 800; color: #fde68a; text-shadow: 0 0 20px #fde68a; }}
            .title-tier-2 {{ font-size: 32px; font-weight: 800; color: #f59e0b; text-shadow: 0 0 22px #f59e0b; }}
            .title-tier-3 {{ font-size: 36px; font-weight: 800; color: #ef4444; text-shadow: 0 0 25px #ef4444; }}
            .title-tier-4 {{ font-size: 40px; font-weight: 800; color: #c084fc; text-shadow: 0 0 28px #c084fc; }}
            .title-tier-5 {{ font-size: 44px; font-weight: 800; color: #38bdf8; text-shadow: 0 0 30px #38bdf8; }}
            .title-tier-6 {{ font-size: 48px; font-weight: 800; color: #ffffff; text-shadow: 0 0 35px #ffffff; }}
            .status-header {{ font-size: 18px; font-weight: 800; margin-bottom: 5px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
            .desc-text {{ font-size: 16px; color: #cbd5e1; margin-top: 4px; text-shadow: 0 2px 8px rgba(0,0,0,0.95); font-weight: 600; }}
            .price-text {{ font-size: 18px; font-weight: 800; color: #fbbf24; margin-top: 5px; }}
            .cost-text {{ font-size: 15px; font-weight: 700; color: #f87171; margin-top: 4px; }}
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    </head>
    <body>
        <div id="container"></div>
        <div id="cinematicUi" class="cinematic-ui">
            <div id="statusText" class="status-header">READY</div>
            <div class="title-tier-{tier}">{card_title}</div>
            <div class="desc-text">"{card_desc}"</div>
            <div class="price-text">예상 가치: {card_price}</div>
            <div class="cost-text">필요 강화 비용: {current_cost}</div>
        </div>
        <script>
            const statusText = document.getElementById('statusText');
            const status = "{status}";
            statusText.innerText = status;
            
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 0.6, 10.0);

            const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.getElementById('container').appendChild(renderer.domElement);

            const ambientLight = new THREE.AmbientLight(0xffffff, 1.0);
            scene.add(ambientLight);
            const mainLight = new THREE.DirectionalLight(0xffffff, 2.0);
            mainLight.position.set(5, 8, 5);
            scene.add(mainLight);

            const geometry = new THREE.IcosahedronGeometry(2.3, 1);
            const material = new THREE.MeshPhysicalMaterial({{
                color: "{card_color}",
                metalness: 0.8,
                roughness: 0.2,
                transmission: 0.5,
                transparent: true,
                opacity: 0.9
            }});
            const mesh = new THREE.Mesh(geometry, material);
            scene.add(mesh);

            function animate() {{
                requestAnimationFrame(animate);
                mesh.rotation.x += 0.005;
                mesh.rotation.y += 0.008;
                renderer.render(scene, camera);
            }}
            animate();
        </script>
    </body>
    </html>
    """

  components.html(three_js_code, height=520, scrolling=False)
