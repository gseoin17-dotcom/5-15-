/* 지온냄새 강화하기 — Streamlit 없는 순수 브라우저 버전 */
const GAME_DATA = {"POINT_REWARD_TABLE":{"1":100,"2":150,"3":200,"4":300,"5":500,"6":700,"7":900,"8":1200,"9":1500,"10":2000,"11":2500,"12":3000,"13":3500,"14":4000,"15":5000,"16":6000,"17":7000,"18":8000,"19":9000,"20":10000,"21":12000,"22":14000,"23":16000,"24":18000,"25":20000,"26":23000,"27":26000,"28":30000,"29":35000,"30":40000,"31":45000,"32":50000,"33":60000,"34":70000,"35":80000},"SMELL_DB":{"false":{"0":{"name":"0단계 : 무취 지온의 공간","desc":"아직은 아무 냄새도 안 남. 지온이가 씻었나 봄.","price":0,"color":"#4a5568","tier":1},"1":{"name":"1단계 : 스쳐가는 지온냄새","desc":"버스 옆자리에 앉은 지온이가 팔을 들 때 스치듯 나는 가벼운 암내.","price":150,"color":"#718096","tier":1},"2":{"name":"2단계 : 은은한 지온냄새","desc":"체육 시간이 끝난 뒤 지온이가 벗어던진 축축한 양말 냄새.","price":400,"color":"#38a169","tier":1},"3":{"name":"3단계 : 습한 지온냄새","desc":"사흘 동안 빨지 않은 지온이의 후드티 모자에 쩐내.","price":600,"color":"#276749","tier":1},"4":{"name":"4단계 : 진득한 지온냄새","desc":"여름철 밀폐된 방 안에서 지온이가 뒹굴다 난 땀에 쩐 이불 냄새.","price":800,"color":"#319795","tier":1},"5":{"name":"5단계 : 자극적인 지온냄새","desc":"지온이가 발가락을 긁은 손으로 코를 슥 만지게 만드는 향.","price":3000,"color":"#2c7a7b","tier":1},"6":{"name":"6단계 : 풍부한 지온냄새","desc":"신발장에 박아둔 지온이의 축구화 속에서 무르익은 발효 냄새.","price":3500,"color":"#3182ce","tier":2},"7":{"name":"7단계 : 압도적인 지온냄새","desc":"지온이가 다녀간 자리마다 코를 찌르는 시큼털털한 체취의 파도.","price":6100,"color":"#2b6cb0","tier":2},"8":{"name":"8단계 : 폭발하는 지온냄새","desc":"일주일 동안 안 감은 지온이 머리통에서 뿜어져 나오는 유분 폭탄.","price":10000,"color":"#805ad5","tier":2},"9":{"name":"9단계 : 시공을 뒤흔드는 지온냄새","desc":"화장실 문을 열자마자 지온이가 남기고 간 흔적의 생생함.","price":20000,"color":"#6b46c1","tier":2},"10":{"name":"10단계 : 치명적인 지온냄새","desc":"맡는 순간 안구실종을 유발하는 지온이의 살인적인 입냄새.","price":35100,"color":"#d69e2e","tier":2},"11":{"name":"11단계 : 환각을 부르는 지온냄새","desc":"썩은 청국장과 지온이의 발냄새가 콜라보를 이뤄 주마등이 스친다.","price":160000,"color":"#b7791f","tier":3},"12":{"name":"12단계 : 공간지배 지온냄새","desc":"방 문을 열기도 전에 복도까지 마중 나온 지온이의 찌든 내음.","price":350000,"color":"#dd6b20","tier":3},"13":{"name":"13단계 : 전성기 지온냄새","desc":"음식물 쓰레기통을 여름볕에 사흘간 방치한 것과 비견되는 향.","price":1000000,"color":"#c05621","tier":3},"14":{"name":"14단계 : 신성한 지온냄새","desc":"너무 지독해서 눈물마저 고이게 만드는 지온이의 꼬릿한 기운.","price":3000000,"color":"#e53e3e","tier":3},"15":{"name":"15단계 : 오리지널 지온냄새","desc":"하수구 역류 현상과 지온이의 입김이 만나 온 세상이 오염된다.","price":7500000,"color":"#9b2c2c","tier":3},"16":{"name":"16단계 : 우주관통 지온냄새","desc":"대기권을 뚫고 오존층마저 뻥 뚫어버리는 지온이의 겨드랑이 폭풍.","price":14200000,"color":"#00f0ff","tier":4},"17":{"name":"17단계 : 차원균열 지온냄새","desc":"지온이의 구린내가 너무 독해서 다른 평행세계의 코까지 썩힌다.","price":20000000,"color":"#ff00ea","tier":4},"18":{"name":"18단계 : Absolute 지온냄새","desc":"우주 만물의 원소를 전부 지온이의 체취로 치환해버리는 절대악취.","price":30000000,"color":"#ffe600","tier":4},"19":{"name":"19단계 : 초월 지온냄새","desc":"인간의 후각 세포를 단번에 파괴하는 초월적인 썩은 내.","price":47500000,"color":"#ff0055","tier":4},"20":{"name":"20단계 : 지온이의 정성이 들어간 포근한 집밥 냄새","desc":"지온맘이 끓여준 묵은지 김치찌개... 인 줄 알았으나 지온이 빨래 냄새.","price":68300000,"color":"#ffaa00","tier":4},"21":{"name":"21단계 : 지온이의 엄격한 샤우팅 냄새","desc":"안 씻고 버티는 지온이를 잡으려고 지온맘이 휘두른 등짝의 내음.","price":101000000,"color":"#ff4500","tier":5},"22":{"name":"22단계 : 지온이의 전설의 흙된장국 냄새","desc":"지온이의 발냄새 원액을 살짝 타서 깊은 맛을 낸 지온맘의 특제 국물.","price":160000000,"color":"#ff007f","tier":5},"23":{"name":"23단계 : 지온이의 100년 숙성 원액 냄새","desc":"지온이가 어릴 때부터 모아둔 꼬릿한 때를 장독대에 묻어 숙성시켰다.","price":230000000,"color":"#7b00ff","tier":5},"24":{"name":"24단계 : 지온이의 냄새 탈취 스프레이 냄새","desc":"방 안에 쩔어 있는 지온이의 체취를 탈취제로 잡으려다 역관람당함.","price":300000000,"color":"#0088ff","tier":5},"25":{"name":"25단계 : 지온이의 대인배적인 냄새","desc":"이런 지온이라도 품에 안아주는 지온맘의 대인배적 냄새 포용력.","price":400000000,"color":"#00ffaa","tier":5},"26":{"name":"26단계 : 지온이의 궁극 필살기 냄새","desc":"지온이 방 문을 강제로 열고 환기시키며 뿜어내는 지온맘의 분노.","price":1800000000,"color":"#ccff00","tier":6},"27":{"name":"27단계 : 지온이의 창조와 냄새","desc":"지온이의 모든 악취를 정화하려다 지온맘마저 구속당한 경지.","price":2500000000,"color":"#fffb00","tier":6},"28":{"name":"28단계 : 지온이의 우주창조설 냄새","desc":"우주 전체가 지온이의 발냄새 아래 무릎을 꿇고 헛구역질을 한다.","price":5500000000,"color":"#ffffff","tier":6},"29":{"name":"29단계 : 딥다크 지온냄새","desc":"모든 꼬릿한 냄새의 근원이자, 지온이를 낳고 기른 위대한 악취의 여신.","price":10500000000,"color":"#ff00aa","tier":6},"30":{"name":"30단계 : 태초의 지온냄새 ","desc":"우주 탄생 이전부터 존재했던 오리지널 태고의 구린내.","price":20000000000,"color":"#00ffff","tier":6},"31":{"name":"31단계 : 하이퍼 지온 싱귤래리티","desc":"냄새가 너무 묵직해서 블랙홀처럼 주변 모든 빛과 산소를 빨아들인다.","price":45000000000,"color":"#7000ff","tier":6},"32":{"name":"32단계 : 멀티버스 지온 에센스","desc":"모든 평행우주에 존재하는 지온이의 체취가 한곳으로 모이는 중.","price":90000000000,"color":"#ff00e1","tier":6},"33":{"name":"33단계 : 인피니티 지온 페트리코","desc":"영원히 끝나지 않는 지온이의 발효 비린내가 온 은하를 뒤덮음.","price":200000000000,"color":"#00ff66","tier":6},"34":{"name":"34단계 : 오메가 지온 제네시스","desc":"지온이의 냄새로 우주를 멸망시키고 다시 창조하는 종말의 향기.","price":500000000000,"color":"#ff6600","tier":6},"35":{"name":"35단계 : ★디 오리지널 앱솔루트 지온★","desc":"우주 만물을 통틀어 가장 지독하고 완벽한 궁극의 지온 냄새.","price":1000000000000,"color":"#ffffff","tier":6}},"true":{"0":{"name":"환생 0단계 : 초신성 핵폐기물 자이온","desc":"환생을 거쳐 새롭게 압축된 태초의 고밀도 방사능 악취.","price":1000000000,"color":"#ff0055","tier":1},"1":{"name":"환생 1단계 : 안드로메다 자이온 암모니아","desc":"안드로메다 은하 전체를 알칼리화시키는 암모니아 폭풍.","price":2500000000,"color":"#00ffff","tier":1},"2":{"name":"환생 2단계 : 화이트홀 자이온 하이드로겐","desc":"우주 백색왜성의 폭발과 함께 뿜어져 나오는 순백의 악취.","price":6000000000,"color":"#ffffff","tier":1},"3":{"name":"환생 3단계 : 쿼크 글루온 자이온 악취","desc":"소립자 수준에서부터 강하게 결합되어 떨어지지 않는 쿼크급 냄새.","price":15000000000,"color":"#ffaa00","tier":2},"4":{"name":"환생 4단계 : 차원왜곡 자이온 타임루프 찌든내 ","desc":"시간의 흐름마저 썩어버리게 만드는 과거와 미래의 냄새 집합체.","price":35000000000,"color":"#9b2c2c","tier":2},"5":{"name":"환생 5단계 : 네메시스 자이온 다크매터","desc":"빛조차 탈출하지 못하고 악취에 붙잡혀 빨려 들어가는 암흑물질.","price":80000000000,"color":"#38a169","tier":2},"6":{"name":"환생 6단계 : 메가 블랙홀 자이온 호라이즌","desc":"모든 물리 법칙이 붕괴하고 오직 자이온이의 체취만 남는 경계선.","price":180000000000,"color":"#805ad5","tier":3},"7":{"name":"환생 7단계 : 감마선 버스트 자이온 플레어","desc":"우주 끝까지 수십 광년 동안 일직선으로 뻗어 나가는 살인적 악취.","price":400000000000,"color":"#e53e3e","tier":3},"8":{"name":"환생 8단계 : 하이퍼노바 자이온 코어 붕괴","desc":"거대 항성이 생을 마감하며 방출하는 전설적인 폭발성 악취.","price":900000000000,"color":"#ff4500","tier":3},"9":{"name":"환생 9단계 : 엘더블루 제네시스 자이온","desc":"태초의 우주가 생성되기도 전에 존재했던 푸른빛의 시원(始源) 냄새.","price":2000000000000,"color":"#0088ff","tier":4},"10":{"name":"환생 10단계 : 카이퍼 자이온 벨트 코스믹 더스트","desc":"태양계 외곽의 얼어붙은 얼음 조각들에 스며든 미지의 원시 악취.","price":4500000000000,"color":"#cbd5e1","tier":4},"11":{"name":"환생 11단계 : 자이온오르트 클라우드 딥 프리즈","desc":"영원히 녹지 않을 것 같은 극저온 속에서 서서히 발효된 냉동 체취.","price":10000000000000,"color":"#319795","tier":4},"12":{"name":"환생 12단계 : 태양풍 플라즈마 자이온제트 스트림","desc":"태양 표면에서 뿜어져 나오는 고온다습한 초고속 플라즈마 냄새.","price":22000000000000,"color":"#f59e0b","tier":5},"13":{"name":"환생 13단계 : 마그네타 자이온자기장 폭풍","desc":"지구상의 모든 나침반을 고장 내고 정신을 아득하게 만드는 자기장.","price":50000000000000,"color":"#7000ff","tier":5},"14":{"name":"환생 14단계 : 펄서 자이온로테이션 시그널","desc":"일정한 주기로 우주 전체에 강력한 악취 전파를 송출하는 중성자별.","price":120000000000000,"color":"#00ff66","tier":5},"15":{"name":"환생 15단계 : 웜홀 크로스오버 자이온 디멘션","desc":"시공간의 통로를 열어 다른 차원의 구린내를 실시간으로 끌어온다.","price":280000000000000,"color":"#ff00ea","tier":6},"16":{"name":"환생 16단계 : 스트링 시스코어 자이온 엠피리어","desc":"초끈이론의 11차원을 진동시키며 울려 퍼지는 궁극의 우주 진동음.","price":600000000000000,"color":"#ccff00","tier":6},"17":{"name":"환생 17단계 : 센타우루스 자이온 알파 코어","desc":"가장 가까운 별무리의 기운을 통째로 오염시킨 강력한 은하수 향.","price":1300000000000000,"color":"#ff6600","tier":6},"18":{"name":"환생 18단계 : 페가수스 자이온 별자리 네뷸라","desc":"신화 속 날개 든 말의 질주를 따라 온 하늘에 퍼지는 거대 성운 향.","price":3000000000000000,"color":"#00f0ff","tier":6},"19":{"name":"환생 19단계 : 자이온세인트 오메가 얼티밋 에센스","desc":"우주의 수명이 다하는 순간까지 사라지지 않는 불멸의 성스러운 냄새.","price":7000000000000000,"color":"#ffe600","tier":6},"20":{"name":"환생 20단계 : 코스믹 인피니티 싱귤자이온래리티","desc":"모든 차원과 우주의 모든 존재가 하나로 응축된 무한대의 악취.","price":15000000000000000,"color":"#ff00aa","tier":6},"21":{"name":"환생 21단계 : 자이온트랜스센던탈 앱솔루트 가디언","desc":"차원의 벽을 넘어 초월적인 신위(神威)를 뿜어내는 가디언의 경지.","price":35000000000000000,"color":"#ffffff","tier":6},"22":{"name":"환생 22단계 : 하이퍼 자이온 디바인 코어","desc":"자이온이라는 존재 자체가 우주의 신성한 법칙으로 등용한 상태.","price":80000000000000000,"color":"#7b00ff","tier":6},"23":{"name":"환생 23단계 : 자이온옴니버스 마스터피스 악취","desc":"모든 평행세계를 통틀어 단 하나만 존재하는 완벽한 걸작 악취.","price":200000000000000000,"color":"#00ffff","tier":6},"24":{"name":"환생 24단계 : 이터널 제네시스 울티마자이온s","desc":"우주의 탄생과 종말을 영원히 반복하게 만드는 궁극의 고리.","price":500000000000000000,"color":"#ff4500","tier":6},"25":{"name":"환생 25단계 : ★심플 성지온★","desc":"문일중 3학년 5반의 냄새를 담당하는 그저 GOA.T","price":1000000000000000000,"color":"#ffffff","tier":6}}},"PROB_TABLE":{"false":{"0":[100.0,0.0,0.0,0.0],"1":[100.0,0.0,0.0,0.0],"2":[100.0,0.0,0.0,0.0],"3":[96.0,4.0,0.0,0.0],"4":[96.0,4.0,0.0,0.0],"5":[91.0,9.0,0.0,0.0],"6":[91.0,7.5,1.5,0.0],"7":[91.0,4.5,4.5,0.0],"8":[86.0,9.5,4.5,0.0],"9":[81.0,14.5,4.5,0.0],"10":[81.0,14.5,4.5,0.0],"11":[76.0,14.5,4.5,5.0],"12":[71.0,14.5,4.5,10.0],"13":[71.0,14.5,6.5,8.0],"14":[66.0,14.5,9.5,10.0],"15":[61.0,19.5,9.5,10.0],"16":[61.0,17.5,11.5,10.0],"17":[56.0,19.5,14.5,10.0],"18":[51.0,19.5,16.5,13.0],"19":[51.0,19.5,19.5,10.0],"20":[46.0,21.5,22.5,10.0],"21":[41.0,24.5,24.5,10.0],"22":[41.0,22.5,26.5,10.0],"23":[41.0,19.5,29.5,10.0],"24":[41.0,17.5,31.5,10.0],"25":[36.0,24.5,29.5,10.0],"26":[51.0,19.5,24.5,5.0],"27":[41.0,24.5,29.5,5.0],"28":[31.0,29.5,34.5,5.0],"29":[21.0,34.5,39.5,5.0],"30":[16.0,34.5,44.5,5.0],"31":[13.0,34.5,47.5,5.0],"32":[11.0,34.5,49.5,5.0],"33":[9.0,36.5,49.5,5.0],"34":[6.0,39.5,49.5,5.0]},"true":{"0":[100.0,0.0,0.0,0.0],"1":[96.0,4.0,0.0,0.0],"2":[91.0,7.5,1.5,0.0],"3":[86.0,9.5,4.5,0.0],"4":[81.0,14.5,4.5,0.0],"5":[76.0,14.5,4.5,5.0],"6":[71.0,14.5,6.5,8.0],"7":[66.0,17.5,9.5,7.0],"8":[61.0,19.5,9.5,10.0],"9":[56.0,19.5,14.5,10.0],"10":[51.0,21.5,17.5,10.0],"11":[46.0,24.5,19.5,10.0],"12":[41.0,24.5,24.5,10.0],"13":[39.0,24.5,26.5,10.0],"14":[36.0,24.5,29.5,10.0],"15":[33.0,27.5,29.5,10.0],"16":[31.0,29.5,34.5,5.0],"17":[26.0,31.5,37.5,5.0],"18":[21.0,34.5,39.5,5.0],"19":[19.0,34.5,41.5,5.0],"20":[16.0,34.5,44.5,5.0],"21":[13.0,37.5,44.5,5.0],"22":[11.0,39.5,44.5,5.0],"23":[9.0,41.5,44.5,5.0],"24":[6.0,44.5,44.5,5.0]}},"CRITICAL_RATE":0.05,"PITY_MAX":4,"ACHIEVEMENTS":{"first_enhance":{"name":"첫걸음","desc":"처음으로 강화를 시도하세요.","title":"지온 킁킁 견습생","reward":5000},"level_10":{"name":"10강 돌파","desc":"시즌 1에서 10단계에 도달하세요.","title":"지온 구린내 수련생","reward":20000},"level_20":{"name":"20강 돌파","desc":"시즌 1에서 20단계에 도달하세요.","title":"지온 베테랑 후각러","reward":100000},"level_30":{"name":"30강 돌파","desc":"시즌 1에서 30단계에 도달하세요.","title":"지온 악취 마스터","reward":500000},"level_35":{"name":"궁극의 지온","desc":"시즌 1 최종 35단계를 달성하세요.","title":"디 오리지널 지온","reward":1000000},"drop_to_0":{"name":"끝없는 추락","desc":"34단계에서 0단계로 돌아가세요.","title":"자이온 추락의 전설","reward":300000},"rebirth":{"name":"차원의 문","desc":"시즌 2 환생을 시작하세요.","title":"지온 차원 여행자","reward":5000000},"s2_level_10":{"name":"자이온 각성","desc":"시즌 2에서 10단계에 도달하세요.","title":"각성한 자이온","reward":10000000},"s2_level_20":{"name":"자이온 폭주","desc":"시즌 2에서 20단계에 도달하세요.","title":"폭주의 자이온","reward":30000000},"s2_level_25":{"name":"진정한 환생","desc":"시즌 2 최종 25단계를 달성하세요.","title":"TRUE REBIRTH 자이온","reward":100000000},"warp_1":{"name":"공간 이동","desc":"워프권을 처음 사용하세요.","title":"자이온 워프 개척자","reward":10000},"warp_5":{"name":"워프 중독","desc":"워프권을 5회 사용하세요.","title":"자이온 차원 도약자","reward":100000},"critical":{"name":"대성공","desc":"크리티컬 강화를 성공시키세요.","title":"우주의 지온 선택","reward":50000},"seller":{"name":"냄새 장사꾼","desc":"냄새를 판매해 돈을 획득하세요.","title":"지온 냄새 상인","reward":25000},"enhance_50":{"name":"강화광","desc":"강화를 총 50회 시도하세요.","title":"자이온 망치 중독자","reward":200000},"enhance_100":{"name":"강화의 끝","desc":"강화를 총 100회 시도하세요.","title":"단련의 지온 신","reward":1000000},"level_5":{"name":"첫 강화","desc":"5단계에 도달하세요.","title":"지온 입문 코끝러","reward":5000},"level_15":{"name":"중급 냄새꾼","desc":"15단계에 도달하세요.","title":"지온 향기 수집가","reward":50000},"level_25":{"name":"고급 냄새꾼","desc":"25단계에 도달하세요.","title":"자이온 악취 지배자","reward":250000},"s2_level_5":{"name":"자이온 입문","desc":"시즌 2에서 5단계에 도달하세요.","title":"자이온 견습생","reward":1000000},"s2_level_15":{"name":"자이온 숙련","desc":"시즌 2에서 15단계에 도달하세요.","title":"자이온 숙련자","reward":15000000},"warp_10":{"name":"워프 마스터","desc":"워프권을 10회 사용하세요.","title":"자이온 공간 지배자","reward":500000},"enhance_200":{"name":"강화는 계속된다","desc":"강화를 총 200회 시도하세요.","title":"자이온 강화의 초월자","reward":5000000},"rich":{"name":"부자 냄새","desc":"보유 금액 10억을 달성하세요.","title":"지온 재벌","reward":1000000},"seller_10":{"name":"장사의 신","desc":"판매를 10회 성공하세요.","title":"자이온 전설의 상인","reward":300000},"points_100k":{"name":"포인트 수집가","desc":"누적 획득 포인트 100,000P를 달성하세요.","title":"지온 포인트 수집가","reward":100000},"points_1m":{"name":"포인트 백만장자","desc":"누적 획득 포인트 1,000,000P를 달성하세요.","title":"자이온 포인트 부자","reward":1000000},"critical_5":{"name":"크리티컬 헌터","desc":"크리티컬 강화를 5회 성공하세요.","title":"지온 크리티컬 헌터","reward":500000},"survivor":{"name":"기적의 생존","desc":"20단계 이상에서 강화 실패 후 살아남으세요.","title":"불굴의 자이온","reward":300000}},"TITLE_THEMES":{"지온 킁킁 견습생":["#22d3ee","#0e7490","#083344","🫧"],"지온 구린내 수련생":["#a3e635","#4d7c0f","#1a2e05","🌿"],"지온 베테랑 후각러":["#60a5fa","#1d4ed8","#172554","🎯"],"지온 악취 마스터":["#f97316","#c2410c","#431407","🔥"],"디 오리지널 지온":["#facc15","#a16207","#422006","👑"],"자이온 추락의 전설":["#94a3b8","#475569","#0f172a","☄️"],"지온 차원 여행자":["#c084fc","#7e22ce","#2e1065","🌀"],"각성한 자이온":["#2dd4bf","#0f766e","#042f2e","⚡"],"폭주의 자이온":["#fb7185","#be123c","#4c0519","💢"],"TRUE REBIRTH 자이온":["#f0abfc","#c026d3","#4a044e","♾️"],"자이온 워프 개척자":["#38bdf8","#0369a1","#082f49","🚀"],"자이온 차원 도약자":["#818cf8","#4338ca","#1e1b4b","🌌"],"우주의 지온 선택":["#fde047","#ca8a04","#422006","✦"],"지온 냄새 상인":["#34d399","#047857","#022c22","💰"],"자이온 망치 중독자":["#fbbf24","#d97706","#451a03","🔨"],"단련의 지온 신":["#f8fafc","#64748b","#111827","⚔️"],"지온 입문 코끝러":["#67e8f9","#0891b2","#083344","👃"],"지온 향기 수집가":["#86efac","#16a34a","#052e16","🍃"],"자이온 악취 지배자":["#f472b6","#db2777","#500724","☠️"],"자이온 견습생":["#93c5fd","#2563eb","#172554","🔷"],"자이온 숙련자":["#a78bfa","#6d28d9","#2e1065","💠"],"자이온 공간 지배자":["#e879f9","#a21caf","#4a044e","🛸"],"자이온 강화의 초월자":["#fef08a","#ea580c","#431407","🌠"],"지온 재벌":["#fcd34d","#b45309","#451a03","💎"],"자이온 전설의 상인":["#5eead4","#0f766e","#042f2e","🏪"],"불굴의 자이온":["#f87171","#991b1b","#450a0a","🛡️"],"지온 포인트 수집가":["#fde047","#a16207","#422006","🪙"],"자이온 포인트 부자":["#67e8f9","#0891b2","#083344","💎"],"지온 크리티컬 헌터":["#fb7185","#9f1239","#4c0519","🎯"]},"TITLE_STYLES":{"지온 킁킁 견습생":"title-style-bubble","지온 구린내 수련생":"title-style-leaf","지온 베테랑 후각러":"title-style-target","지온 악취 마스터":"title-style-flame","디 오리지널 지온":"title-style-crown","자이온 추락의 전설":"title-style-meteor","지온 차원 여행자":"title-style-portal","각성한 자이온":"title-style-bolt","폭주의 자이온":"title-style-rage","TRUE REBIRTH 자이온":"title-style-infinity","자이온 워프 개척자":"title-style-rocket","자이온 차원 도약자":"title-style-galaxy","우주의 지온 선택":"title-style-star","지온 냄새 상인":"title-style-coin","자이온 망치 중독자":"title-style-hammer","단련의 지온 신":"title-style-blade","지온 입문 코끝러":"title-style-nose","지온 향기 수집가":"title-style-nature","자이온 악취 지배자":"title-style-skull","자이온 견습생":"title-style-diamond","자이온 숙련자":"title-style-crystal","자이온 공간 지배자":"title-style-ufo","자이온 강화의 초월자":"title-style-comet","지온 재벌":"title-style-gem","자이온 전설의 상인":"title-style-shop","불굴의 자이온":"title-style-shield","지온 포인트 수집가":"title-style-pointcoin","자이온 포인트 부자":"title-style-pointgem","지온 크리티컬 헌터":"title-style-crithunter"},"TITLE_DEFAULT":"칭호 없음"};

const DB = GAME_DATA.SMELL_DB;
const PROB = GAME_DATA.PROB_TABLE;
const ACH = GAME_DATA.ACHIEVEMENTS;
const THEMES = GAME_DATA.TITLE_THEMES;
const STYLES = GAME_DATA.TITLE_STYLES;
const DEFAULT_TITLE = GAME_DATA.TITLE_DEFAULT;
const CRITICAL_RATE = GAME_DATA.CRITICAL_RATE;
const PITY_MAX = GAME_DATA.PITY_MAX;
const POINTS = GAME_DATA.POINT_REWARD_TABLE;

const ENHANCE_COST_S1 = {
  0:300,1:300,2:500,3:500,4:1000,5:1500,6:2000,7:2000,8:3000,9:5000,
  10:10900,11:20000,12:35000,13:55000,14:100000,15:180000,16:300000,
  17:300000,18:500000,19:800000,20:1500000,21:2500000,22:4000000,
  23:6500000,24:10000000,25:16000000,26:25000000,27:40000000,28:65000000,
  29:100000000,30:150000000,31:250000000,32:400000000,33:700000000,
  34:1200000000,35:2000000000
};
const ENHANCE_COST_S2 = {
  0:1000000,1:2500000,2:5000000,3:10000000,4:20000000,5:40000000,
  6:80000000,7:150000000,8:300000000,9:600000000,10:1200000000,
  11:2500000000,12:5000000000,13:10000000000,14:20000000000,15:40000000000,
  16:80000000000,17:150000000000,18:300000000000,19:600000000000,
  20:1200000000000,21:2500000000000,22:5000000000000,23:10000000000000,
  24:25000000000000,25:100000000000000
};

const INITIAL = {
  currentSeason:1,
  rebirthCount:0,
  achievements:Object.fromEntries(Object.keys(ACH).map(k=>[k,false])),
  unlockedTitles:[],
  selectedTitle:DEFAULT_TITLE,
  enhanceAttempts:0, warpUses:0, sellCount:0,
  points:0,lastPointReward:0,pointsEarnedTotal:0,pointsSpentTotal:0,
  enhanceSuccesses:0,enhanceFailures:0,criticalCount:0,destroyCount:0,
  seasonData:{
    1:{level:0,prev_level:0,max_level:0,money:1000000,status:"READY",shield:0,tears:0,pity_count:0,
       unlocked_warps:{10:false,15:false,20:false,25:false,30:false}},
    2:{level:0,prev_level:0,max_level:0,money:1000000000,status:"READY",shield:0,tears:50,pity_count:0,
       unlocked_season2_warps:{5:false,10:false,15:false,20:false}}
  }
};

let state = loadState();
let sceneState = null;
let toastTimer = null;
// 개발자 모드: DEL 키를 짧은 시간 안에 5번 연타하면 ON/OFF 전환.
// 저장하지 않으므로 새로고침하면 기본적으로 꺼진 상태입니다.
let devMode = false;
let delPressCount = 0;
let delPressTimer = null;

function clone(o){ return JSON.parse(JSON.stringify(o)); }
function loadState(){
  try{
    const saved=JSON.parse(localStorage.getItem("jion_smell_game_v3"));
    if(!saved) return clone(INITIAL);
    const s=Object.assign(clone(INITIAL),saved);
    s.seasonData=Object.assign(clone(INITIAL.seasonData),saved.seasonData||{});
    s.achievements=Object.assign(clone(INITIAL.achievements),saved.achievements||{});
    return s;
  }catch(e){ return clone(INITIAL); }
}
function save(){ localStorage.setItem("jion_smell_game_v3",JSON.stringify(state)); }
function isS2(){ return state.currentSeason===2; }
function level(){ return state.seasonData[state.currentSeason].level; }
function data(){ return DB[isS2()][level()]; }
function maxLevel(){ return isS2()?25:35; }
function money(){ return state.seasonData[state.currentSeason].money; }
function setMoney(v){ state.seasonData[state.currentSeason].money=v; }
function tears(){ return state.seasonData[state.currentSeason].tears; }
function shield(){ return state.seasonData[state.currentSeason].shield; }
function pity(){ return state.seasonData[state.currentSeason].pity_count; }
function formatGold(amount){
  if(amount===0) return "0원";
  if(!Number.isFinite(amount)) return "무한대(INF)";
  // 금액이 너무 길어지지 않도록 조/경 단위 아래는 생략합니다.
  // 예: 201경4,910조6,296억4,199만9,104원 → 201경4,910조
  const units=["","만","억","조","경","해"];
  let result=[]; let n=Math.floor(amount), i=0;
  while(n>0 && i<units.length){
    const r=n%10000;
    if(r>0 && i<=4) result.unshift(r.toLocaleString("ko-KR")+units[i]);
    n=Math.floor(n/10000); i++;
  }
  return result.join("")+"원";
}
function enhanceCost(lvl,s2=isS2()){
  return (s2?ENHANCE_COST_S2:ENHANCE_COST_S1)[lvl] ?? 2000000000;
}
function pointReward(lvl){
  if(lvl<=0) return 0;
  return POINTS[lvl] ?? (80000+(lvl-35)*10000);
}
function warpPointCost(lvl){ return pointReward(lvl)*20; }
function warpMoneyCost(lvl){ return Number(DB[isS2()][lvl].price); }
function shieldPointCost(lvl){ return pointReward(lvl)*5; }
function shieldMoneyCost(lvl){
  if(isS2()) return Math.floor(Number(DB[true][lvl].price)/5);
  return Math.max(50000,enhanceCost(lvl,false)*15);
}
function showToast(msg){
  const el=document.getElementById("toast"); el.textContent=msg; el.classList.add("show");
  clearTimeout(toastTimer); toastTimer=setTimeout(()=>el.classList.remove("show"),2600);
}
function unlock(key){
  if(!ACH[key] || state.achievements[key]) return;
  state.achievements[key]=true;
  const title=ACH[key].title;
  if(!state.unlockedTitles.includes(title)) state.unlockedTitles.push(title);
  setMoney(money()+Number(ACH[key].reward));
  showToast(`🏆 업적 달성: ${ACH[key].name} | +${formatGold(ACH[key].reward)}`);
}
function checkAchievements(){
  const l=level();
  if(state.enhanceAttempts>=1) unlock("first_enhance");
  if(state.enhanceAttempts>=50) unlock("enhance_50");
  if(state.enhanceAttempts>=100) unlock("enhance_100");
  if(state.enhanceAttempts>=200) unlock("enhance_200");
  if(state.warpUses>=10) unlock("warp_10");
  if(state.sellCount>=10) unlock("seller_10");
  if(money()>=1000000000) unlock("rich");
  if(!isS2()&&l>=5) unlock("level_5");
  if(!isS2()&&l>=15) unlock("level_15");
  if(!isS2()&&l>=25) unlock("level_25");
  if(isS2()&&l>=5) unlock("s2_level_5");
  if(isS2()&&l>=15) unlock("s2_level_15");
  if(state.seasonData[state.currentSeason].status==="FAIL"&&l>=20) unlock("survivor");
  if(state.warpUses>=5) unlock("warp_5");
  if(!isS2()&&l===0&&state.seasonData[1].max_level>=34) unlock("drop_to_0");
  if(!isS2()&&l>=10) unlock("level_10");
  if(!isS2()&&l>=20) unlock("level_20");
  if(!isS2()&&l>=35) unlock("level_35");
  if(isS2()&&l>=10) unlock("s2_level_10");
  if(isS2()&&l>=20) unlock("s2_level_20");
  if(isS2()&&l>=25) unlock("s2_level_25");
  if(state.warpUses>=1) unlock("warp_1");
  if(state.seasonData[state.currentSeason].status==="CRITICAL") unlock("critical");
  if(state.pointsEarnedTotal>=100000) unlock("points_100k");
  if(state.pointsEarnedTotal>=1000000) unlock("points_1m");
  if(state.criticalCount>=5) unlock("critical_5");
}
function rewardPoints(lvl){
  const r=pointReward(lvl); state.points+=r; state.pointsEarnedTotal+=r; state.lastPointReward=r;
}
function enhance(){
  const d=state.seasonData[state.currentSeason], curr=d.level, max=maxLevel(), cost=enhanceCost(curr);
  if(curr>=max){ render(); return; }
  if(d.money<cost){ d.status="NOT_ENOUGH_MONEY"; showToast("강화 비용 부족!"); render(); return; }
  d.money-=cost; d.prev_level=curr; state.enhanceAttempts++;

  // 개발자 모드에서는 강화 결과가 항상 성공합니다.
  // 일반 강화처럼 비용은 차감되며, 개발자 모드는 저장되지 않습니다.
  if(devMode){
    d.level++;
    d.status="SUCCESS";
    d.pity_count=0;
    d.max_level=Math.max(d.max_level,d.level);
    state.enhanceSuccesses++;
    rewardPoints(d.level);
  }else if(d.pity_count>=PITY_MAX-1){
    d.level++; d.status="PITY_SUCCESS"; d.pity_count=0;
    d.max_level=Math.max(d.max_level,d.level); rewardPoints(d.level);
  }else{
    const [sp,downP,dp,holdP]=PROB[isS2()][curr] || [5,40,50,5];
    const r=Math.random()*100, success=sp, down=success+downP, destroy=down+dp;
    if(r<success){
      d.pity_count=0;
      if(Math.random()<CRITICAL_RATE && curr+2<=max){
        d.level+=2; d.status="CRITICAL"; state.enhanceSuccesses++; state.criticalCount++;
      }else{
        d.level++; d.status="SUCCESS"; state.enhanceSuccesses++;
      }
      rewardPoints(d.level);
    }else if(r<down){
      d.pity_count++; if(curr>0)d.level--; d.status="FAILED"; state.enhanceFailures++; d.tears=Math.min(60,d.tears+1);
    }else if(r<destroy){
      if(d.shield>0){
        d.shield--; d.pity_count++; d.status="SHIELD_SAVED"; state.enhanceFailures++; d.tears=Math.min(60,d.tears+1);
      }else{
        d.pity_count++; d.level=0; d.status="DESTROYED"; state.enhanceFailures++; state.destroyCount++; d.tears=Math.min(60,d.tears+2);
      }
    }else{
      d.pity_count++; d.status="HOLD"; state.enhanceFailures++; d.tears=Math.min(60,d.tears+1);
    }
    d.max_level=Math.max(d.max_level,d.level);
  }
  const warps=isS2()?[5,10,15,20]:[10,15,20,25,30];
  const key=isS2()?"unlocked_season2_warps":"unlocked_warps";
  for(const w of warps) if(d.level>=w) d[key][w]=true;
  checkAchievements(); save(); render(); animateResult(d.status);
}
function sell(){
  const d=state.seasonData[state.currentSeason], l=d.level;
  if(l===0) return;
  const price=Number(DB[isS2()][l].price);
  d.money=Number.isFinite(price)?d.money+price:Infinity;
  state.sellCount++; d.prev_level=l; d.level=0; d.status="READY";
  checkAchievements(); save(); render();
  showToast(`💰 ${l}단계 판매 완료!`);
}
function rebirth(){
  if(state.seasonData[1].level<35) return;
  unlock("rebirth");
  state.currentSeason=2; state.rebirthCount++;
  state.points=0; state.lastPointReward=0;
  state.seasonData[2].status="READY";
  save(); render();
  showToast("🌀 시즌 2 환생 완료!");
}
function switchSeason(n){
  if(n===2 && state.seasonData[1].max_level<35 && state.seasonData[1].level<35){
    showToast("시즌 1 35단계에 도달해야 시즌 2를 시작할 수 있습니다."); return;
  }
  state.currentSeason=n; save(); render();
}
function setTitle(t){ state.selectedTitle=t; save(); render(); }

function updateDevModeUI(){
  let badge=document.getElementById("devModeBadge");
  if(!badge){
    badge=document.createElement("div");
    badge.id="devModeBadge";
    badge.innerHTML="🛠️ DEV MODE <span>강화 100% 성공</span>";
    document.body.appendChild(badge);
  }
  badge.classList.toggle("active",devMode);
  document.body.classList.toggle("dev-mode-active",devMode);
}
function toggleDevMode(){
  devMode=!devMode;
  updateDevModeUI();
  showToast(devMode ? "🛠️ 개발자 모드 ON — 강화 100% 성공" : "🛠️ 개발자 모드 OFF — 일반 확률 적용");
}
window.addEventListener("keydown",e=>{
  if(e.key!=="Delete" && e.key!=="Del") return;
  e.preventDefault();
  if(e.repeat) return;
  delPressCount++;
  clearTimeout(delPressTimer);
  delPressTimer=setTimeout(()=>{delPressCount=0;},900);
  if(delPressCount>=5){
    delPressCount=0;
    clearTimeout(delPressTimer);
    toggleDevMode();
  }
});

function render(){
  const d=data(), l=level(), max=maxLevel(), s2=isS2();
  document.getElementById("money").textContent=formatGold(money());
  document.getElementById("points").textContent=state.points.toLocaleString("ko-KR")+"P";
  document.getElementById("tears").textContent=tears()+" / 60개";
  document.getElementById("pity").textContent="실패까지 "+(PITY_MAX-pity())+"회";
  document.getElementById("shield").textContent=shield()+" / 3개";
  document.getElementById("nextReward").textContent="다음 성공: +"+pointReward(Math.min(l+1,max)).toLocaleString("ko-KR")+"P";
  document.getElementById("modeTitle").textContent=s2?"🌀 [시즌 2] 얼티밋 자이온의 시작":"🌌 [시즌 1] 지온의 탄생과 시초";
  document.getElementById("probLevel").textContent=l;

  const p=PROB[s2][l] || [5,40,50,5];
  document.getElementById("probBox").innerHTML=
    `• 성공 확률: <b class="success">${p[0]}%</b> (크리티컬 5%)<br>`+
    `• 하락 확률: <b class="down">${p[1]}%</b><br>`+
    `• 파괴 확률: <b class="destroy">${p[2]}%</b><br>`+
    `• 유지 확률: <b class="hold">${p[3]}%</b>`;

  const eb=document.getElementById("enhanceBtn"), sb=document.getElementById("sellBtn");
  eb.disabled=(l>=max); sb.disabled=(l===0);
  sb.textContent=`💰 판매하기`;

  document.getElementById("season1Btn").classList.toggle("active",!s2);
  document.getElementById("season2Btn").classList.toggle("active",s2);
  document.getElementById("season2Btn").disabled=state.seasonData[1].max_level<35 && state.seasonData[1].level<35;

  document.getElementById("rebirthNotice").classList.toggle("hidden",s2||l<35);
  renderSceneText();
  renderEnhanceCard();
  renderEquippedTitle();
}
function renderSceneText(){
  const d=data(), l=level(), max=maxLevel(), s2=isS2(), status=state.seasonData[state.currentSeason].status;
  const tier=Math.min(6,d.tier||1);
  const main=document.getElementById("mainTitle");
  main.className="title-tier-"+tier;
  main.textContent=d.name;
  document.getElementById("descText").textContent=`"${d.desc}"`;
  document.getElementById("priceText").textContent="예상 가치: "+formatGold(Number(d.price));
  document.getElementById("pointText").textContent="획득 포인트: "+pointReward(l).toLocaleString("ko-KR")+"P";
  document.getElementById("costText").textContent="필요 강화 비용: "+formatGold(enhanceCost(l,s2));
  const st=document.getElementById("statusText");
  const labels={
    READY:s2?"REBIRTH READY - 블랙홀 차원 에너지가 집결합니다":"READY - 우주 에너지가 차분히 집중됩니다",
    SUCCESS:"✨ COSMIC SUCCESS (강화 성공) ✨",
    CRITICAL:"⚡ COSMIC CRITICAL HIT!! (+2단계 이상 대성공) ⚡",
    PITY_SUCCESS:"✨ 지온이의 가오 발동! (천장 100% 성공) ✨",
    SHIELD_SAVED:"🛡️ SHIELD PROTECTED! (우주 방어 발동) 🛡️",
    DESTROYED:"💥 BLACKHOLE CATACLYSM DESTROYED (코어 대폭발 붕괴됨!) 💥",
    FAILED:"🔻 FAILED (에너지 하락) 🔻",
    HOLD:"🔒 HOLD (에너지 동결) 🔒",
    NOT_ENOUGH_MONEY:"💰 강화 비용 부족"
  };
  st.textContent=labels[status]||status;
  const colors={READY:"#38bdf8",SUCCESS:d.color,CRITICAL:"#fff",PITY_SUCCESS:"#fde68a",SHIELD_SAVED:"#60a5fa",DESTROYED:"#f00",FAILED:"#64748b",HOLD:"#94a3b8",NOT_ENOUGH_MONEY:"#f87171"};
  st.style.color=colors[status]||"#38bdf8";
  const shouldShake=l>=15 || (l===max && ["SUCCESS","CRITICAL","PITY_SUCCESS"].includes(status));
  ["mainTitle","descText","priceText","pointText","costText"].forEach(id=>document.getElementById(id).classList.toggle("shaking-text",shouldShake));
}
function cardMeta(tier){
  const map={
    1:['RARE','title-tier-1'],2:['EPIC','title-tier-2'],3:['LEGEND','title-tier-3'],
    4:['MYTHIC','title-tier-4'],5:['COSMIC','title-tier-5'],6:['ABSOLUTE','title-tier-6']
  }; return map[Math.min(6,tier||1)]||map[1];
}
function renderEnhanceCard(){
  const d=data(), l=level(), s2=isS2(), max=maxLevel();
  const [rarity]=cardMeta(d.tier);
  const card=document.getElementById('enhanceCard'); if(!card)return;
  card.style.setProperty('--card',d.color); card.style.setProperty('--card2',d.color); card.style.setProperty('--card3',s2?'#10051d':'#071122');
  document.getElementById('cardSeason').textContent=s2?'SEASON 2 • REBIRTH':'SEASON 1 • ORIGIN';
  document.getElementById('cardRarity').textContent=rarity;
  document.getElementById('cardLevel').textContent='+'+l;
  card.className='enhance-card';
  card.dataset.level=String(l);
  card.dataset.season=s2?'2':'1';
  card.dataset.tier=String(d.tier||1);
  const art=document.getElementById('cardArt');
  if(art){ art.dataset.level=String(l); art.dataset.season=s2?'2':'1'; renderCardDesign(art,l,s2,d); }
  document.getElementById('cardStageLabel').textContent=(s2?'환생 ':'')+l+'단계'+(l===max?' • MAX':'');
  document.getElementById('cardName').textContent=d.name.replace(/^환생\s+\d+단계\s*:\s*/,'').replace(/^\d+단계\s*:\s*/,'');
  document.getElementById('cardDesc').textContent=d.desc;
  document.getElementById('cardPrice').textContent=formatGold(Number(d.price));
  document.getElementById('cardPoints').textContent=pointReward(l).toLocaleString('ko-KR')+'P';
  document.getElementById('cardCost').textContent=l>=max?'MAX':formatGold(enhanceCost(l,s2));
  document.getElementById('cardSerial').textContent=`JION • ${s2?'S2':'S1'} • ${String(l).padStart(2,'0')}`;
  document.getElementById('cardTier').textContent='TIER '+['I','II','III','IV','V','VI'][Math.min(5,(d.tier||1)-1)];
  const status=state.seasonData[state.currentSeason].status;
  const labels={READY:'READY',SUCCESS:'✦ COSMIC SUCCESS',CRITICAL:'✦✦ CRITICAL HIT',PITY_SUCCESS:'✦ PITY SUCCESS',SHIELD_SAVED:'◈ SHIELD SAVED',DESTROYED:'✕ DESTROYED',FAILED:'▼ FAILED',HOLD:'◆ HOLD',NOT_ENOUGH_MONEY:'INSUFFICIENT FUNDS'};
  const result=document.getElementById('cardResult'); result.textContent=labels[status]||status;
  const scene=document.getElementById('enhanceCardScene');
  scene.style.setProperty('--glow',d.color);
  scene.classList.remove('status-success','status-critical','status-failed','status-hold','status-destroyed','status-shield');
  if(status==='SUCCESS'||status==='PITY_SUCCESS'||status==='CRITICAL')scene.classList.add(status==='CRITICAL'?'status-critical':'status-success');
  else if(status==='FAILED')scene.classList.add('status-failed');
  else if(status==='HOLD')scene.classList.add('status-hold');
  else if(status==='DESTROYED')scene.classList.add('status-destroyed');
  else if(status==='SHIELD_SAVED')scene.classList.add('status-shield');
  result.style.color=status==='DESTROYED'?'#ff5757':status==='FAILED'?'#cbd5e1':status==='CRITICAL'?'#fff':d.color;
}
function cardBurst(color='#ffffff', count=70, power=260){
  const box=document.getElementById('cardParticles'); if(!box)return;
  box.innerHTML='';
  const frag=document.createDocumentFragment();
  for(let i=0;i<count;i++){
    const p=document.createElement('i'); p.className='card-particle'; p.style.color=color;
    const a=Math.random()*Math.PI*2, dist=power*(.35+Math.random()*.75);
    p.dataset.dx=Math.cos(a)*dist; p.dataset.dy=Math.sin(a)*dist;
    p.style.width=p.style.height=(2+Math.random()*6)+'px'; frag.appendChild(p);
  }
  box.appendChild(frag);
  [...box.children].forEach((p,i)=>{
    gsap.fromTo(p,{x:0,y:0,scale:.2,opacity:0},{x:+p.dataset.dx,y:+p.dataset.dy,scale:1.4,opacity:1,duration:.18+Math.random()*.22,delay:i*.004,ease:'power3.out',onComplete(){gsap.to(p,{opacity:0,duration:.55,ease:'power2.out'})}});
  });
}

function renderCardDesign(art,l,s2,d){
  const key=`${s2?'S2':'S1'}-${l}`;
  if(art.dataset.designKey===key)return;
  art.dataset.designKey=key;
  art.querySelectorAll('.dynamic-card-design').forEach(e=>e.remove());
  const frag=document.createDocumentFragment();
  const add=(cls,style='')=>{const e=document.createElement('i');e.className='dynamic-card-design '+cls;if(style)e.style.cssText=style;frag.appendChild(e);};
  // Every level gets a distinct silhouette language, not just a color swap.
  const type=l%10;
  const count=Math.min(12,2+Math.floor(l/4));
  if(type===0){ add('design-crown'); for(let i=0;i<3;i++)add('design-ring',`--i:${i}`); }
  else if(type===1){ add('design-diamond'); add('design-cross'); }
  else if(type===2){ add('design-hex'); for(let i=0;i<6;i++)add('design-node',`--i:${i}`); }
  else if(type===3){ add('design-reactor'); for(let i=0;i<4;i++)add('design-orbit',`--i:${i}`); }
  else if(type===4){ add('design-blade'); for(let i=0;i<5;i++)add('design-blade',`--i:${i}`); }
  else if(type===5){ add('design-portal'); add('design-portal-inner'); }
  else if(type===6){ add('design-prism'); add('design-prism-core'); }
  else if(type===7){ add('design-gear'); for(let i=0;i<8;i++)add('design-tooth',`--i:${i}`); }
  else if(type===8){ add('design-sun'); for(let i=0;i<8;i++)add('design-ray',`--i:${i}`); }
  else { add('design-singularity'); add('design-singularity-ring'); }
  for(let i=0;i<count;i++) add('design-particle',`--i:${i};--n:${count}`);
  art.appendChild(frag);
}

function renderEquippedTitle(){
  const t=state.selectedTitle, th=THEMES[t]||["#a78bfa","#6d28d9","#111827","🏷️"], style=STYLES[t]||"title-style-default";
  const el=document.getElementById("equippedTitle");
  el.className=`equipped-title title-design ${style}`;
  el.style.background=`linear-gradient(135deg,${th[2]},${th[1]}88,#020617)`;
  el.style.border=`1px solid ${th[0]}`;
  el.style.boxShadow=`0 0 22px ${th[0]}35,inset 0 1px rgba(255,255,255,.12)`;
  const titleAch=Object.values(ACH).find(a=>a.title===t);
  const obtain=titleAch ? `획득 방법 · ${titleAch.desc}` : (t===DEFAULT_TITLE ? '기본 칭호 · 별도의 획득 조건 없음' : '획득 방법 · 업적을 달성하면 획득할 수 있습니다.');
  el.innerHTML=`<div class="selected-title-label" style="color:${th[0]}">✦ EQUIPPED TITLE ✦</div><div class="selected-title-name" style="color:${th[0]}">${th[3]} ${t}</div><div class="selected-title-stage">${state.season2 ? "환생 " : ""}${state.level}단계</div><div class="selected-title-obtain">${obtain}</div>`;
}

/* --------------------------- MODALS --------------------------- */
function openModal(kind){
  const m=document.getElementById("modal"), c=document.getElementById("modalContent");
  if(kind==="shop") c.innerHTML=shopHTML();
  if(kind==="tears") c.innerHTML=tearsHTML();
  if(kind==="achievements") c.innerHTML=achievementsHTML();
  m.classList.remove("hidden");
  bindModal(kind);
}
function closeModal(){ document.getElementById("modal").classList.add("hidden"); }
function shopHTML(){
  const l=level(), s2=isS2(), sh=shield(), moneyCost=shieldMoneyCost(l), pointCost=shieldPointCost(l);
  const minShield=s2?16:20;
  const d=state.seasonData[state.currentSeason];
  const warpLevels=s2?[5,10,15,20]:[10,15,20,25,30];
  let warps=warpLevels.map(w=>{
    const unlocked=!!d[s2?"unlocked_season2_warps":"unlocked_warps"][w];
    return `<div class="flat-item" style="margin-top:9px">
      <b>🚀 ${w}단계 워프</b>
      <div class="modal-meta">${unlocked?"해금됨":"🔒 아직 도달하지 않음"} · 💰 ${formatGold(warpMoneyCost(w))} · ⭐ ${warpPointCost(w).toLocaleString("ko-KR")}P</div>
      <div class="two-buttons">
        <button class="glass-btn" data-buy-warp="money" data-warp="${w}" ${(!unlocked||l>=w||money()<warpMoneyCost(w))?"disabled":""}>💰 돈으로 구매</button>
        <button class="glass-btn" data-buy-warp="point" data-warp="${w}" ${(!unlocked||l>=w||state.points<warpPointCost(w))?"disabled":""}>⭐ 포인트로 구매</button>
      </div>
    </div>`;
  }).join("");
  return `<div class="modal-head shop"><h2>🛒 상점</h2><p>방지권과 워프권을 💰 돈 또는 ⭐ 포인트로 구매할 수 있습니다.</p></div>
    <div class="shop-grid"><div class="flat-item"><div>💰 보유 금액</div><b>${formatGold(money())}</b></div><div class="flat-item"><div>⭐ 보유 포인트</div><b>${state.points.toLocaleString("ko-KR")}P</b></div></div>
    <div class="modal-section flat-panel" style="margin-top:12px;border-left:4px solid #60a5fa">
      <h3 style="color:#60a5fa">🛡️ 파괴 방지권</h3>
      <div class="modal-meta"><b>보유:</b> ${sh} / 3개<br><b>구매 가능 단계:</b> ${minShield}단계 이상<br><b>💰 돈 가격:</b> ${formatGold(moneyCost)}<br><b>⭐ 포인트 가격:</b> ${pointCost.toLocaleString("ko-KR")}P</div>
      <div class="two-buttons">
        <button class="glass-btn" data-buy-shield="money" ${(l<minShield||sh>=3||money()<moneyCost)?"disabled":""}>💰 돈으로 구매</button>
        <button class="glass-btn" data-buy-shield="point" ${(l<minShield||sh>=3||state.points<pointCost)?"disabled":""}>⭐ 포인트로 구매</button>
      </div>
    </div>
    <div class="modal-section flat-panel" style="border-left:4px solid #c084fc">
      <h3 style="color:#c084fc">🚀 워프권</h3>
      <div class="modal-meta">이미 도달했던 단계로 즉시 이동합니다.</div>${warps}
    </div>`;
}
function tearsHTML(){
  const l=level(), max=maxLevel(), limit=isS2()?18:32;
  return `<div class="modal-head tear"><h2>💧 눈물</h2><p>눈물 20개를 사용해 1~3단계를 확정적으로 올립니다.</p></div>
    <div class="flat-panel"><div style="font-size:11px;color:#94a3b8">보유 눈물</div><div style="font-size:24px;font-weight:900;color:#38bdf8">${tears()} <span style="font-size:13px;color:#94a3b8">/ 60</span></div>
    <div class="modal-meta">사용 조건: <b>20개</b> · 상승 범위: <b>+1 ~ +3</b><br>${l>=limit?"⚠️ 고단계부터는 눈물을 사용할 수 없습니다!":""}</div>
    <button class="glass-btn" id="useTears" ${l>=limit||tears()<20||l>=max?"disabled":""}>눈물 기적 가동</button></div>`;
}
function achievementsHTML(){
  const arr=Object.entries(ACH), done=arr.filter(([k])=>state.achievements[k]).length, pct=arr.length?Math.floor(done/arr.length*100):0;
  const cards=arr.map(([k,a])=>{
    const ok=!!state.achievements[k], th=THEMES[a.title]||["#a78bfa","#6d28d9","#111827","🏷️"], style=STYLES[a.title]||"title-style-default";
    return `<div class="flat-ach-card title-design ${style}" style="border-color:${ok?th[0]:"#334155"}">
      <div style="padding:13px"><div style="font-size:10px;letter-spacing:1.5px;color:${ok?th[0]:"#64748b"};font-weight:800">${ok?"UNLOCKED":"LOCKED"}</div>
      <div style="font-size:15px;font-weight:900;margin-top:5px">${ok?"✅":"🔒"} ${a.name}</div>
      <div style="font-size:12px;color:#cbd5e1;margin-top:6px">${a.desc}</div>
      <div style="font-size:11px;color:${th[0]};margin-top:8px;font-weight:800">🏷️ ${a.title}</div>
      <div style="font-size:10px;color:#fde68a;margin-top:2px">💰 ${formatGold(a.reward)}</div></div></div>`;
  }).join("");
  const options=[DEFAULT_TITLE,...state.unlockedTitles].filter((v,i,a)=>a.indexOf(v)===i);
  return `<div class="modal-head ach"><h2>🏆 업적</h2></div>
    <b>업적 진행도:</b> ${done} / ${arr.length} · ${pct}%
    <div class="progress-track"><div class="progress-fill" style="width:${pct}%"></div></div>
    <div class="achievement-grid">${cards}</div>
    <div class="flat-panel" style="margin-top:12px"><b style="color:#e9d5ff">🏷️ 칭호 장착</b><div style="font-size:11px;color:#94a3b8;margin-top:3px">칭호를 선택하면 즉시 메인 화면에 적용됩니다.</div>
    <select id="titleSelect" class="title-select">${options.map(t=>`<option ${t===state.selectedTitle?"selected":""}>${t}</option>`).join("")}</select></div>`;
}
function bindModal(kind){
  document.querySelectorAll("[data-buy-shield]").forEach(b=>b.onclick=()=>{
    const type=b.dataset.buyShield,l=level(), min=isS2()?16:20,cost=type==="money"?shieldMoneyCost(l):shieldPointCost(l);
    if(l<min||shield()>=3){showToast("구매 조건을 만족하지 못했습니다.");return;}
    if(type==="money"){if(money()<cost){showToast("금액이 부족합니다.");return;}setMoney(money()-cost);}
    else{if(state.points<cost){showToast("포인트가 부족합니다.");return;}state.points-=cost;state.pointsSpentTotal+=cost;}
    state.seasonData[state.currentSeason].shield++; save(); render(); openModal("shop"); showToast("🛡️ 파괴 방지권 구매 완료!");
  });
  document.querySelectorAll("[data-buy-warp]").forEach(b=>b.onclick=()=>{
    const type=b.dataset.buyWarp,w=Number(b.dataset.warp),d=state.seasonData[state.currentSeason],key=isS2()?"unlocked_season2_warps":"unlocked_warps",cost=type==="money"?warpMoneyCost(w):warpPointCost(w);
    if(!d[key][w]||level()>=w){showToast("워프 조건을 만족하지 못했습니다.");return;}
    if(type==="money"){if(money()<cost){showToast("금액이 부족합니다.");return;}setMoney(money()-cost);}
    else{if(state.points<cost){showToast("포인트가 부족합니다.");return;}state.points-=cost;state.pointsSpentTotal+=cost;}
    state.warpUses++; d.prev_level=d.level; d.level=w; d.max_level=Math.max(d.max_level,w); d.status="SUCCESS";
    checkAchievements(); save(); render(); openModal("shop"); showToast(`🚀 ${w}단계로 워프 성공!`);
  });
  document.querySelectorAll("[data-buy-shield]").forEach(b=>b.disabled=b.disabled);
  const tearBtn=document.getElementById("useTears");
  if(tearBtn) tearBtn.onclick=()=>{
    const d=state.seasonData[state.currentSeason], limit=isS2()?18:32;
    if(d.tears<20||d.level>=limit)return;
    d.tears-=20; const add=[1,2,3][Math.floor(Math.random()*3)]; d.prev_level=d.level; d.level=Math.min(maxLevel(),d.level+add); d.status=add>=2?"CRITICAL":"SUCCESS";
    save(); render(); openModal("tears"); showToast(`눈물 기적 100% 성공! ${add}단계 상승!`);
  };
  const ts=document.getElementById("titleSelect");
  if(ts) ts.onchange=()=>{setTitle(ts.value);openModal("achievements");};
}
document.getElementById("closeModal").onclick=closeModal;
document.getElementById("modal").addEventListener("click",e=>{if(e.target.id==="modal")closeModal();});
document.querySelectorAll("[data-modal]").forEach(b=>b.onclick=()=>openModal(b.dataset.modal));
document.getElementById("enhanceBtn").onclick=enhance;
document.getElementById("sellBtn").onclick=sell;
document.getElementById("rebirthBtn").onclick=rebirth;
document.getElementById("season1Btn").onclick=()=>switchSeason(1);
document.getElementById("season2Btn").onclick=()=>switchSeason(2);

/* --------------------------- Three.js scene --------------------------- */
function initScene(){
  const canvas=document.getElementById("threeCanvas"), wrap=document.getElementById("threeWrap");
  const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});
  renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
  const scene=new THREE.Scene();
  const camera=new THREE.PerspectiveCamera(40,1,.1,1000);
  camera.position.set(0,.6,10);
  scene.add(new THREE.AmbientLight(0xffffff,.8));
  const dl=new THREE.DirectionalLight(0xffffff,2); dl.position.set(5,8,5); scene.add(dl);
  const coreLight=new THREE.PointLight(0x38bdf8,12,40); coreLight.position.set(0,0,3); scene.add(coreLight);

  const starsGeo=new THREE.BufferGeometry(), starCount=1000, sp=new Float32Array(starCount*3);
  for(let i=0;i<starCount;i++){sp[i*3]=(Math.random()-.5)*40;sp[i*3+1]=(Math.random()-.5)*40;sp[i*3+2]=(Math.random()-.5)*40-10;}
  starsGeo.setAttribute("position",new THREE.BufferAttribute(sp,3));
  const stars=new THREE.Points(starsGeo,new THREE.PointsMaterial({color:0xffffff,size:.07,transparent:true,opacity:.7,blending:THREE.AdditiveBlending}));
  scene.add(stars);

  const pg=new THREE.BufferGeometry(), pc=600, pp=new Float32Array(pc*3), pv=[];
  for(let i=0;i<pc;i++){pp[i*3]=(Math.random()-.5)*6;pp[i*3+1]=-4+Math.random()*2;pp[i*3+2]=(Math.random()-.5)*6;pv.push({x:(Math.random()-.5)*.006,y:.008+Math.random()*.025,z:(Math.random()-.5)*.006});}
  pg.setAttribute("position",new THREE.BufferAttribute(pp,3));
  const particles=new THREE.Points(pg,new THREE.PointsMaterial({color:0x67e8f9,size:.045,transparent:true,opacity:.55,blending:THREE.AdditiveBlending}));
  scene.add(particles);

  const group=new THREE.Group(); group.position.y=-.7; scene.add(group);
  sceneState={renderer,scene,camera,wrap,stars,particles,pp,pv,group,coreLight,outer:null,core:null};

  resizeScene();
  window.addEventListener("resize",resizeScene);
  requestAnimationFrame(loop);
}
function resizeScene(){
  if(!sceneState)return;
  const {renderer,camera,wrap}=sceneState;
  const w=wrap.clientWidth,h=wrap.clientHeight;
  renderer.setSize(w,h,false); camera.aspect=w/h; camera.updateProjectionMatrix();
}
function makeLevelModel(level, color, season2){
  const g = new THREE.Group();
  const c = new THREE.Color(color);
  const white = new THREE.Color(0xffffff);
  const glow = c.clone();
  const pct = Math.max(0, Math.min(1, level / 35));

  const mat = (opts={}) => new THREE.MeshStandardMaterial(Object.assign({
    color:c, roughness:.2, metalness:.72, emissive:glow,
    emissiveIntensity:.35 + pct*1.15, transparent:true, opacity:.9
  }, opts));
  const coreMat = () => new THREE.MeshStandardMaterial({
    color:white, roughness:.08, metalness:.9, emissive:glow,
    emissiveIntensity:2.2 + pct*3.2, transparent:true, opacity:.96
  });
  const add = (mesh,x=0,y=0,z=0) => { mesh.position.set(x,y,z); g.add(mesh); return mesh; };
  const torus = (r,t,rx=0,ry=0,rz=0,material=mat()) => {
    const m=add(new THREE.Mesh(new THREE.TorusGeometry(r,t,14,64),material));
    m.rotation.set(rx,ry,rz); m.userData.isAura=true; return m;
  };
  const ico = (r,d=1,material=mat()) => add(new THREE.Mesh(new THREE.IcosahedronGeometry(r,d),material));
  const sphere = (r,material=mat()) => add(new THREE.Mesh(new THREE.SphereGeometry(r,32,24),material));
  const box = (x,y,z,material=mat()) => add(new THREE.Mesh(new THREE.BoxGeometry(x,y,z),material));
  const cyl = (r,h,rs=12,material=mat()) => add(new THREE.Mesh(new THREE.CylinderGeometry(r,r,h,rs),material));
  const cone = (r,h,rs=8,material=mat()) => add(new THREE.Mesh(new THREE.ConeGeometry(r,h,rs),material));

  // The important visual progression: higher levels become larger, brighter and more complex.
  const mainR = .72 + pct*1.05;
  const coreR = .28 + pct*.38;
  const detail = level < 8 ? 1 : level < 20 ? 2 : 3;
  const core = ico(coreR, Math.min(detail,2), coreMat());
  core.userData.isCore = true;

  // Different silhouette for every level, while preserving a continuous power curve.
  if(level===0){ sphere(mainR*.9); }
  else if(level<=5){
    const shapes=[
      ()=>ico(mainR,1),
      ()=>box(mainR*1.45,mainR*.95,mainR*1.15),
      ()=>cyl(mainR*.72,mainR*1.9,8),
      ()=>cone(mainR*.95,mainR*2.0,6),
      ()=>ico(mainR,2)
    ];
    shapes[level-1]();
  } else if(level<=10){
    if(level===6){ box(mainR*1.5,mainR*1.5,mainR*1.5).rotation.set(.35,.45,.2); }
    if(level===7){ cyl(mainR*.78,mainR*1.8,10); }
    if(level===8){ cone(mainR,mainR*2.2,4); }
    if(level===9){ ico(mainR*1.08,2).scale.set(1,.72,1); }
    if(level===10){ sphere(mainR); for(let i=0;i<4;i++){ const t=torus(mainR*1.12,.055,Math.PI/2,0,i*Math.PI/4); t.scale.set(1,.72,1); } }
  } else if(level<=15){
    if(level===11){ for(let i=0;i<3;i++){const m=ico(mainR*.62,1);m.position.set((i-1)*mainR*.8,(i%2)*.25,0);} }
    if(level===12){ const b=box(mainR*1.55,mainR*1.15,mainR*1.55); b.rotation.y=.4; torus(mainR*1.05,.07,Math.PI/2); }
    if(level===13){ cyl(mainR*.7,mainR*2.1,12); for(let y of [-.45,0,.45]) torus(mainR*.83,.055,Math.PI/2,0,0).position.y=y; }
    if(level===14){ sphere(mainR*.9); for(let i=0;i<6;i++){let m=cone(mainR*.22,mainR*.8,6);let a=i*Math.PI/3;m.position.set(Math.cos(a)*mainR,Math.sin(a)*mainR,0);m.rotation.z=a-Math.PI/2;} }
    if(level===15){ const a=torus(mainR*1.05,.16,Math.PI/2);a.scale.set(1,.55,1); const b=ico(mainR*.68,2);b.rotation.set(.4,.2,.5); }
  } else if(level<=20){
    if(level===16){ for(let i=0;i<4;i++){let m=box(mainR*.25,mainR*1.8,mainR*.25);m.rotation.z=i*Math.PI/4;} }
    if(level===17){ ico(mainR,2).scale.set(1,.65,1); torus(mainR*1.2,.11,Math.PI/2); torus(mainR*1.2,.06,0,Math.PI/2); }
    if(level===18){ cyl(mainR*.7,mainR*2.1,16); for(let i=0;i<3;i++){let t=torus(mainR*.9,.065,Math.PI/2);t.position.y=-.55+i*.55;} }
    if(level===19){ for(let i=0;i<8;i++){let m=cone(mainR*.2,mainR*.9,5);let a=i*Math.PI/4;m.position.set(Math.cos(a)*mainR*.9,Math.sin(a)*mainR*.9,0);m.rotation.z=a-Math.PI/2;} ico(mainR*.65,2); }
    if(level===20){ const outer=ico(mainR*1.05,2); outer.material=mat({wireframe:true,opacity:.34}); torus(mainR*1.3,.09,Math.PI/2); torus(mainR*1.3,.09,0,Math.PI/2); }
  } else if(level<=25){
    if(level===21){ const b=box(mainR*1.65,mainR*.75,mainR*1.65);b.rotation.set(.4,.3,.2); for(let i=0;i<4;i++){let t=torus(mainR*1.05,.07,Math.PI/2);t.rotation.z=i*Math.PI/4;} }
    if(level===22){ const s=sphere(mainR*.9); for(let i=0;i<8;i++){let m=ico(mainR*.16,0);let a=i*Math.PI/4;m.position.set(Math.cos(a)*mainR*1.25,Math.sin(a)*mainR*1.25,Math.sin(a*2)*.35);} }
    if(level===23){ const o=torus(mainR*1.22,.19,Math.PI/2);o.scale.set(1,.62,1); for(let i=0;i<4;i++){let m=cone(mainR*.2,mainR*1.25,6);let a=i*Math.PI/2;m.position.set(Math.cos(a)*mainR*.95,Math.sin(a)*mainR*.95,0);m.rotation.z=a;} }
    if(level===24){ const s=ico(mainR*1.05,2); for(let i=0;i<3;i++){let t=torus(mainR*1.4,.065,Math.PI/2);t.rotation.z=i*Math.PI/3;} }
    if(level===25){ cyl(mainR*.72,mainR*1.2,16); const top=cone(mainR*1.0,mainR*1.2,6);top.position.y=mainR*.95; torus(mainR*1.05,.08,Math.PI/2); }
  } else if(level<=30){
    if(level===26){ const b=box(mainR*1.5,mainR*1.5,mainR*1.5);b.rotation.set(.7,.55,.25); for(let i=0;i<4;i++){let m=box(mainR*.18,mainR*2.2,mainR*.18);m.rotation.y=i*Math.PI/4;} }
    if(level===27){ const o=ico(mainR*1.05,2);o.scale.set(1,.62,1); for(let i=0;i<4;i++){let t=torus(mainR*1.45,.06,Math.PI/2);t.rotation.z=i*Math.PI/4;} }
    if(level===28){ sphere(mainR*.95); for(let i=0;i<10;i++){let m=cone(mainR*.17,mainR*.85,6);let a=i*Math.PI/5;m.position.set(Math.cos(a)*mainR*1.12,Math.sin(a)*mainR*1.12,Math.cos(a*2)*.3);m.rotation.z=a-Math.PI/2;} }
    if(level===29){ const a=torus(mainR*1.28,.22,Math.PI/2);a.scale.set(1,.5,1); const b=torus(mainR*1.28,.08,0,Math.PI/2);b.rotation.x=.7; ico(mainR*.72,2); }
    if(level===30){ const coreShell=ico(mainR*1.12,3);coreShell.material=mat({wireframe:true,opacity:.28}); for(let i=0;i<5;i++){let t=torus(mainR*1.5,.065,Math.PI/2);t.rotation.z=i*Math.PI/5;} }
  } else {
    if(level===31){ const s=ico(mainR*1.12,3); for(let i=0;i<6;i++){let m=cone(mainR*.15,mainR*1.0,6);let a=i*Math.PI/3;m.position.set(Math.cos(a)*mainR*1.1,Math.sin(a)*mainR*1.1,0);m.rotation.z=a-Math.PI/2;} }
    if(level===32){ const s=sphere(mainR*.95); for(let i=0;i<3;i++){let t=torus(mainR*1.45,.09,Math.PI/2);t.rotation.z=i*Math.PI/3;} }
    if(level===33){ const o=ico(mainR*1.15,3);o.rotation.set(.25,.5,.2); for(let i=0;i<8;i++){let t=torus(mainR*1.55,.055,Math.PI/2);t.rotation.z=i*Math.PI/8;} }
    if(level===34){ const outer=torus(mainR*1.55,.22,Math.PI/2); const inner=torus(mainR*.82,.10,Math.PI/2,0,0,coreMat()); for(let i=0;i<8;i++){let m=cone(mainR*.13,mainR*1.15,6);let a=i*Math.PI/4;m.position.set(Math.cos(a)*mainR*1.1,Math.sin(a)*mainR*1.1,0);m.rotation.z=a-Math.PI/2;} }
    if(level===35){
      const crown=ico(mainR*1.28,3); crown.material=mat({emissiveIntensity:2.0,opacity:.82});
      crown.scale.set(1,.72,1);
      for(let i=0;i<3;i++){let t=torus(mainR*(1.48+i*.18),.095-i*.01,Math.PI/2,0,i*Math.PI/3,coreMat());}
      for(let i=0;i<12;i++){let m=cone(mainR*.12,mainR*1.25,6,coreMat());let a=i*Math.PI/6;m.position.set(Math.cos(a)*mainR*1.12,Math.sin(a)*mainR*1.12,Math.sin(a*2)*.22);m.rotation.z=a-Math.PI/2;}
    }
  }

  // Power/aura effects scale with the enhancement level.
  const ringCount = level < 6 ? 0 : level < 12 ? 1 : level < 18 ? 2 : level < 24 ? 3 : level < 30 ? 4 : 5;
  for(let i=0;i<ringCount;i++){
    const r=mainR*(1.25 + i*.22);
    const ring=torus(r,.035 + pct*.035, i%2 ? .0 : Math.PI/2, i%2 ? Math.PI/2 : 0, (i*.55)%Math.PI, coreMat());
    ring.userData.auraSpeed=(.35+i*.12)*(level%2?1:-1);
  }

  // High levels get floating energy shards; low levels stay clean.
  const shardCount = level<10 ? 0 : Math.min(28, Math.floor((level-8)*1.15));
  for(let i=0;i<shardCount;i++){
    const a=i*Math.PI*2/shardCount;
    const rad=mainR*(1.35 + (i%3)*.16);
    const m=ico(.055 + pct*.055,0,coreMat());
    m.position.set(Math.cos(a)*rad, Math.sin(a)*rad*.72, Math.sin(a*2)*rad*.35);
    m.userData.orbit=true; m.userData.orbitAngle=a; m.userData.orbitRadius=rad; m.userData.orbitSpeed=.25+pct*.9;
  }

  // Level 1 starts compact; level 35 is dramatically larger.
  const finalScale=.78 + pct*1.15;
  g.scale.setScalar(finalScale);
  g.rotation.set((level%5)*.08,(level%7)*.13,(level%3)*.06);
  g.userData.level=level;
  g.userData.progress=pct;
  g.userData.isModel=true;
  return g;
}
function buildObject(){
  const {group}=sceneState;
  while(group.children.length)group.remove(group.children[0]);
  const d=data(), l=level(), s2=isS2();
  const model=makeLevelModel(l,d.color,s2);
  group.add(model);
  sceneState.model=model;
  sceneState.coreLight.color.set(d.color);
  sceneState.coreLight.intensity=12 + l*.55;
  sceneState.outer=model;
  sceneState.core=model.children.find(x=>x.userData && x.userData.isCore) || model;
}
function spawnEnhanceBurst(color, count=70, power=0.16, size=0.07, life=0.9){
  if(!sceneState) return;
  const burst=new THREE.Group(), arr=[];
  const c=new THREE.Color(color);
  for(let i=0;i<count;i++){
    const m=new THREE.Mesh(
      new THREE.IcosahedronGeometry(size*(.45+Math.random()*1.15),0),
      new THREE.MeshBasicMaterial({color:c,transparent:true,opacity:.95,blending:THREE.AdditiveBlending})
    );
    const a=Math.random()*Math.PI*2, z=Math.random()*2-1, r=Math.sqrt(1-z*z);
    m.position.set(0,0,0);
    m.userData={vx:Math.cos(a)*r*power*(.65+Math.random()), vy:z*power*(.65+Math.random()), vz:Math.sin(a)*r*power*(.65+Math.random()), spin:(Math.random()-.5)*.25};
    burst.add(m); arr.push(m);
  }
  sceneState.scene.add(burst);
  const proxy={v:0};
  gsap.to(proxy,{v:1,duration:life,ease:'power2.out',onUpdate:()=>{
    arr.forEach(m=>{
      m.position.x+=m.userData.vx;
      m.position.y+=m.userData.vy;
      m.position.z+=m.userData.vz;
      m.userData.vx*=.985; m.userData.vy*=.985; m.userData.vz*=.985;
      m.rotation.x+=m.userData.spin; m.rotation.y+=m.userData.spin*1.3;
      m.material.opacity=.95*(1-proxy.v);
    });
  },onComplete:()=>sceneState.scene.remove(burst)});
}
function screenShake(power=0.12, duration=.28){
  if(!sceneState)return;
  const {camera}=sceneState;
  const base={x:0,y:.6,z:10};
  const shake={n:0};
  gsap.to(shake,{n:1,duration,ease:'power2.out',onUpdate:()=>{
    const fall=1-shake.n;
    camera.position.x=base.x+(Math.random()-.5)*power*fall;
    camera.position.y=base.y+(Math.random()-.5)*power*fall;
  },onComplete:()=>{camera.position.set(base.x,base.y,base.z)}});
}
function impactFlash(opacity=.75){
  const flash=document.getElementById('flashOverlay');
  if(!flash)return;
  flash.style.opacity='0';
  gsap.to(flash,{opacity:opacity,duration:.045,ease:'power4.out',yoyo:true,repeat:1,onComplete:()=>flash.style.opacity='0'});
}
function finalStageCinematic(status, finish){
  const scene=document.getElementById('enhanceCardScene');
  const card=document.getElementById('enhanceCard');
  const wrap=document.getElementById('enhanceCardWrap');
  const glow=document.getElementById('cardStatusGlow');
  const flash=document.getElementById('flashOverlay');
  const shine=card?.querySelector('.card-shine');
  const result=document.getElementById('cardResult');
  if(!scene||!card||!wrap||!result) return false;

  scene.classList.add('final-stage-cinematic');
  const d=data(), color=d.color;
  const current=level();
  const finalMax=maxLevel();
  const destroyed=status==='DESTROYED';
  const power=Math.min(2.25,1.05+current*.032);

  // 결과를 잠시 숨겨 긴장감을 만들고, 카드 자체는 계속 보이게 유지합니다.
  gsap.set(result,{opacity:0,scale:.72,y:10});
  gsap.set(card,{scale:.98,filter:'brightness(.82) saturate(1.1)',transformOrigin:'50% 50%'});
  gsap.set(glow,{scale:.35,opacity:.02});
  if(shine) gsap.set(shine,{x:'-85%',opacity:.25});

  // 1) 에너지 집결: 0~1.25초
  cardBurst(color,90+Math.floor(current*2.2),260+current*8);
  cardBurst('#ffffff',40+Math.floor(current),210+current*5);
  gsap.to(glow,{scale:1.4+power*.35,opacity:.28,duration:1.05,ease:'power2.inOut'});
  gsap.to(card,{scale:1.015,duration:.9,ease:'sine.inOut',yoyo:true,repeat:1});

  // 2) 단계가 높을수록 더 강하게 진동
  const shakeObj={x:0,y:0,r:0};
  gsap.to(shakeObj,{x:power*5.5,y:power*3.2,r:power*1.15,duration:1.15,ease:'sine.inOut',yoyo:true,repeat:3,delay:.35,onUpdate:()=>{
    gsap.set(card,{x:(Math.random()-.5)*shakeObj.x,y:(Math.random()-.5)*shakeObj.y,rotation:(Math.random()-.5)*shakeObj.r});
  }});

  // 3) 절정 직전, 강한 플래시와 링/파티클
  gsap.delayedCall(2.05,()=>{
    cardBurst(color,150+Math.floor(current*2.8),430+current*10);
    cardBurst('#fff',70+Math.floor(current*1.5),360+current*7);
    gsap.to(glow,{scale:2.6,opacity:.62,duration:.32,ease:'power4.out',yoyo:true,repeat:1});
    impactFlash(destroyed?.92:0.72);
    screenShake(destroyed?.42:.25,.42);
  });

  // 4) 마지막 결과가 '팍' 나타나는 순간
  gsap.delayedCall(destroyed?2.72:2.42,()=>{
    if(destroyed){
      scene.classList.add('final-destroy-impact');
      createFinalCracks(card);
      createFinalShards(color,Math.min(90,48+current));
      gsap.to(card,{x:0,y:0,rotation:-2.5,scale:1.08,filter:'brightness(2.1) saturate(1.8)',duration:.13,ease:'power4.out',onComplete:()=>{
        gsap.to(card,{x:0,y:0,rotation:0,scale:.93,filter:'grayscale(.7) brightness(.7)',duration:.22,ease:'power3.in',onComplete:()=>{
          revealFinalResult(result,finish);
        }});
      }});
      impactFlash(1);
      return;
    }
    scene.classList.add('final-success-impact');
    gsap.to(card,{scale:1.17,y:-14,rotation:0,duration:.16,ease:'power4.out',onComplete:()=>{
      gsap.to(card,{scale:1,y:0,duration:.42,ease:'elastic.out(1,.42)',onComplete:()=>revealFinalResult(result,finish)});
    }});
    if(shine) gsap.to(shine,{x:'175%',opacity:1,duration:.42,ease:'power3.out'});
    impactFlash(.86);
  });
  return true;
}

function revealFinalResult(result,finish){
  gsap.fromTo(result,{opacity:0,scale:.55,y:18},{opacity:1,scale:1.16,y:0,duration:.24,ease:'back.out(2.2)',onComplete:()=>{
    gsap.to(result,{scale:1,duration:.3,ease:'power2.out',onComplete:finish});
  }});
}

function createFinalCracks(card){
  card.querySelectorAll('.final-crack').forEach(e=>e.remove());
  const frag=document.createDocumentFragment();
  for(let i=0;i<8;i++){
    const el=document.createElement('i'); el.className='final-crack';
    el.style.setProperty('--rx',(15+Math.random()*70)+'%');
    el.style.setProperty('--ry',(15+Math.random()*70)+'%');
    el.style.setProperty('--len',(45+Math.random()*95)+'px');
    el.style.setProperty('--ang',(Math.random()*160-80)+'deg');
    el.style.animationDelay=(i*.025)+'s'; frag.appendChild(el);
  }
  card.appendChild(frag);
  setTimeout(()=>card.querySelectorAll('.final-crack').forEach(e=>e.remove()),1100);
}

function createFinalShards(color,count=60){
  const box=document.getElementById('cardParticles'); if(!box)return;
  for(let i=0;i<count;i++){
    const p=document.createElement('i'); p.className='card-particle final-shard'; p.style.color=Math.random()<.7?color:'#ff3030';
    const a=Math.random()*Math.PI*2, dist=220+Math.random()*430;
    p.style.width=(3+Math.random()*9)+'px'; p.style.height=(2+Math.random()*12)+'px';
    box.appendChild(p);
    gsap.fromTo(p,{x:0,y:0,scale:.3,opacity:1,rotation:0},{x:Math.cos(a)*dist,y:Math.sin(a)*dist,scale:.2+Math.random()*.9,rotation:(Math.random()-.5)*900,opacity:0,duration:.65+Math.random()*.5,ease:'power3.out',onComplete:()=>p.remove()});
  }
}

function animateResult(status){
  const scene=document.getElementById('enhanceCardScene');
  const card=document.getElementById('enhanceCard');
  const wrap=document.getElementById('enhanceCardWrap');
  const glow=document.getElementById('cardStatusGlow');
  const flash=document.getElementById('flashOverlay');
  const shine=card?.querySelector('.card-shine');
  const layer=document.getElementById('card3dLayer');
  if(!scene||!card||!wrap)return;

  // 기존 CSS keyframe과 GSAP이 동시에 transform/opacity를 조작하면서
  // 카드가 기울거나 사라지는 현상을 방지한다.
  gsap.killTweensOf([card,wrap,glow,flash,shine,layer]);
  scene.classList.remove('status-success','status-critical','status-failed','status-hold','status-destroyed','status-shield');

  renderEnhanceCard();
  const color=data().color;
  glow.style.background=color;
  glow.style.opacity='.10';
  wrap.style.transform='translate3d(0,0,0)';
  gsap.set(wrap,{x:0,y:0,rotation:0,scale:1,opacity:1});
  if(layer) layer.style.transform='rotateX(0deg) rotateY(0deg) translateZ(0)';
  gsap.set(card,{x:0,y:0,rotation:0,rotationX:0,rotationY:0,scale:1,opacity:1,filter:'drop-shadow(0 28px 55px rgba(0,0,0,.42))'});
  if(shine) gsap.set(shine,{x:'-70%'});

  const finish=()=>{
    // 어떤 결과에서도 카드가 사라지지 않고 정면으로 고정되도록 최종값을 보정
    gsap.set(card,{x:0,y:0,rotation:0,rotationX:0,rotationY:0,scale:1,opacity:1,filter:'drop-shadow(0 28px 55px rgba(0,0,0,.42))'});
    gsap.set(wrap,{x:0,y:0,rotation:0,scale:1,opacity:1});
    renderEnhanceCard();
  };

  // 시즌 1 34→35 / 시즌 2 24→25는 최종 강화 전용 연출
  const prevLevel=state.seasonData[state.currentSeason].prev_level ?? level();
  const isFinalAttempt=prevLevel===maxLevel()-1;
  if(isFinalAttempt && (status==='SUCCESS'||status==='CRITICAL'||status==='PITY_SUCCESS'||status==='DESTROYED'||status==='SHIELD_SAVED')){
    if(finalStageCinematic(status,finish)) return;
  }

  if(status==='SUCCESS'||status==='PITY_SUCCESS'){
    scene.classList.add('status-success');
    cardBurst(color,status==='PITY_SUCCESS'?100:65,status==='PITY_SUCCESS'?320:240);
    if(status==='PITY_SUCCESS') cardBurst('#fff',65,290);
    gsap.fromTo(glow,{scale:.7,opacity:.03},{scale:1.65,opacity:status==='PITY_SUCCESS'?.30:.18,duration:.45,ease:'power2.out',yoyo:true,repeat:1});
    // 살짝 들어왔다가 정면에 안착. 회전/투명도는 사용하지 않는다.
    gsap.fromTo(card,{y:18,scale:.94},{y:-7,scale:1.035,duration:.22,ease:'power2.out',onComplete:()=>{
      gsap.to(card,{y:0,scale:1,duration:.28,ease:'back.out(1.8)',onComplete:finish});
    }});
    if(shine) gsap.to(shine,{x:'150%',duration:.9,ease:'power2.inOut',delay:.08});
    impactFlash(status==='PITY_SUCCESS'?.55:.28);
    return;
  }

  if(status==='CRITICAL'){
    scene.classList.add('status-critical');
    cardBurst('#ffffff',115,380); cardBurst(color,95,300);
    gsap.fromTo(glow,{scale:.55,opacity:.04},{scale:2.2,opacity:.34,duration:.6,ease:'power2.out',yoyo:true,repeat:1});
    // 크리티컬도 과도한 3D 회전 없이 확대/착지로 표현
    gsap.fromTo(card,{y:24,scale:.86},{y:-13,scale:1.10,duration:.25,ease:'power3.out',onComplete:()=>{
      gsap.to(card,{y:0,scale:1,duration:.38,ease:'elastic.out(1,.55)',onComplete:finish});
    }});
    if(shine) gsap.to(shine,{x:'170%',duration:.7,ease:'power2.inOut',delay:.04});
    impactFlash(.72);
    return;
  }

  if(status==='FAILED'||status==='HOLD'){
    scene.classList.add(status==='FAILED'?'status-failed':'status-hold');
    const shakeLevel=Math.max(1,Math.min(4.2,0.65+((state.seasonData[state.currentSeason].prev_level||0)*.075)));
    cardBurst(status==='FAILED'?'#ff4d5d':'#a78bfa',45+Math.floor(shakeLevel*10),180+shakeLevel*55);
    screenShake(.055+shakeLevel*.025,.16+shakeLevel*.035);
    gsap.to(card,{x:-9*shakeLevel,duration:.045,ease:'sine.inOut',yoyo:true,repeat:8+Math.floor(shakeLevel*2),onComplete:()=>{
      gsap.to(card,{x:0,duration:.14,ease:'power2.out',onComplete:finish});
    }});
    gsap.to(glow,{opacity:.20,duration:.16,yoyo:true,repeat:1});
    impactFlash(status==='FAILED'?.38:.20);
    return;
  }

  if(status==='SHIELD_SAVED'){
    scene.classList.add('status-shield');
    cardBurst('#60a5fa',85,270);
    gsap.fromTo(glow,{scale:.5,opacity:.04},{scale:1.9,opacity:.28,duration:.5,ease:'back.out(1.7)',yoyo:true,repeat:1});
    gsap.fromTo(card,{y:12,scale:.96},{y:-8,scale:1.055,duration:.2,ease:'power2.out',onComplete:()=>{
      gsap.to(card,{y:0,scale:1,duration:.3,ease:'back.out(1.8)',onComplete:finish});
    }});
    impactFlash(.42);
    return;
  }

  if(status==='DESTROYED'){
    scene.classList.add('status-destroyed');
    cardBurst('#ff2638',150,410); cardBurst('#ffb000',80,310);
    gsap.fromTo(glow,{scale:.45,opacity:.05},{scale:2.45,opacity:.38,duration:.5,ease:'power3.out',yoyo:true,repeat:1});
    // 파괴여도 카드를 완전히 숨기지 않는다. 붉게 어두워졌다가 다시 표시한다.
    gsap.fromTo(card,{scale:1,filter:'brightness(1)'},{scale:1.045,filter:'brightness(1.8)',duration:.18,ease:'power2.out',onComplete:()=>{
      gsap.to(card,{scale:.98,filter:'grayscale(.75) brightness(.65)',duration:.28,ease:'power2.in',onComplete:()=>{
        gsap.to(card,{scale:1,filter:'grayscale(.15) brightness(.9)',duration:.28,ease:'power2.out',onComplete:finish});
      }});
    }});
    impactFlash(.75);
    return;
  }

  gsap.fromTo(card,{y:10,scale:.97},{y:0,scale:1,duration:.32,ease:'back.out(1.6)',onComplete:finish});
}

function loop(){
  requestAnimationFrame(loop);
  if(!sceneState)return;
  const t=performance.now()/1000,{outer,core,stars,particles,pp,pv,renderer,scene,camera,group}=sceneState;
  const status=state.seasonData[state.currentSeason].status, final=level()===maxLevel()&&["SUCCESS","CRITICAL","PITY_SUCCESS"].includes(status);
  if(outer){
    outer.rotation.x+=.0025;
    outer.rotation.y+=.0055;
    if(core){core.rotation.x-=.006;core.rotation.y-=.008;}
    // Higher stages feel more energetic even while idle.
    const p=outer.userData?.progress||0;
    outer.children.forEach((m,i)=>{
      if(m.userData?.isAura){
        const sp=m.userData.auraSpeed||.4;
        m.rotation.z += sp*.003;
        m.rotation.x += sp*.0015;
        const pulse=1 + Math.sin(t*(2.2+p*4)+i)*(.018+p*.025);
        m.scale.setScalar(pulse);
      }
      if(m.userData?.orbit){
        m.userData.orbitAngle += m.userData.orbitSpeed*.008;
        const a=m.userData.orbitAngle, r=m.userData.orbitRadius;
        m.position.x=Math.cos(a)*r;
        m.position.y=Math.sin(a)*r*.72;
        m.position.z=Math.sin(a*2)*r*.35;
      }
    });
    const pulse=1 + Math.sin(t*(2+p*4))*(.012+p*.035);
    core.scale.setScalar(pulse);
  }
  if(final)group.rotation.z=Math.sin(t*2.5)*.2;
  stars.rotation.y=t*.01;
  for(let i=0;i<pp.length/3;i++){pp[i*3]+=pv[i].x;pp[i*3+1]+=pv[i].y;pp[i*3+2]+=pv[i].z;if(pp[i*3+1]>2.5){pp[i*3+1]=-4;pp[i*3]=(Math.random()-.5)*6;pp[i*3+2]=(Math.random()-.5)*6;}}
  particles.geometry.attributes.position.needsUpdate=true;
  renderer.render(scene,camera);
}

initScene();
updateDevModeUI();
render();
buildObject();


/* V9.1: interactive 3D card tilt. The tilt lives on a separate layer,
   so GSAP can safely animate the card itself without fighting the mouse effect. */
(function setupCard3D(){
  const scene=document.getElementById('enhanceCardScene');
  const layer=document.getElementById('card3dLayer');
  if(!scene||!layer)return;
  let tx=0,ty=0,rx=0,ry=0,raf=0;
  const reset=()=>{tx=0;ty=0;};
  scene.addEventListener('pointermove',e=>{
    if(e.pointerType==='touch')return;
    const r=scene.getBoundingClientRect();
    const nx=((e.clientX-r.left)/r.width-.5)*2;
    const ny=((e.clientY-r.top)/r.height-.5)*2;
    tx=Math.max(-1,Math.min(1,nx));
    ty=Math.max(-1,Math.min(1,ny));
    if(!raf) raf=requestAnimationFrame(update);
  });
  scene.addEventListener('pointerleave',()=>{reset(); if(!raf)raf=requestAnimationFrame(update);});
  function update(){
    raf=0;
    rx+=(ty* -7-rx)*.13;
    ry+=(tx* 9-ry)*.13;
    layer.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg) translateZ(0)`;
    if(Math.abs(rx)>0.02||Math.abs(ry)>0.02||tx||ty) raf=requestAnimationFrame(update);
  }
  update();
})();
