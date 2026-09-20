/* 지온냄새 강화하기 V17.45 · RESTORED CARD DESIGN + CURRENT FINAL CINEMATIC */
const GAME_DATA = {"POINT_REWARD_TABLE":{"1":100,"2":150,"3":200,"4":300,"5":500,"6":700,"7":900,"8":1200,"9":1500,"10":2000,"11":2500,"12":3000,"13":3500,"14":4000,"15":5000,"16":6000,"17":7000,"18":8000,"19":9000,"20":10000,"21":12000,"22":14000,"23":16000,"24":18000,"25":20000,"26":23000,"27":26000,"28":30000,"29":35000,"30":40000,"31":45000,"32":50000,"33":60000,"34":70000,"35":80000,"36":90000,"37":105000,"38":120000,"39":135000,"40":150000,"41":165000,"42":180000,"43":195000,"44":210000,"45":225000,"46":240000,"47":255000,"48":270000,"49":285000,"50":300000,"51":315000,"52":330000,"53":345000,"54":360000,"55":375000,"56":390000,"57":405000,"58":420000,"59":435000,"60":450000},"SMELL_DB":{"0":{"name":"0단계 : 무취 지온의 공간","desc":"아직은 아무 냄새도 안 남. 지온이가 씻었나 봄.","price":0,"color":"#4a5568","tier":1},"1":{"name":"1단계 : 스쳐가는 지온냄새","desc":"버스 옆자리에 앉은 지온이가 팔을 들 때 스치듯 나는 가벼운 암내.","price":500,"color":"#718096","tier":1},"2":{"name":"2단계 : 은은한 지온냄새","desc":"체육 시간이 끝난 뒤 지온이가 벗어던진 축축한 양말 냄새.","price":800,"color":"#38a169","tier":1},"3":{"name":"3단계 : 습한 지온냄새","desc":"사흘 동안 빨지 않은 지온이의 후드티 모자에 쩐내.","price":1200,"color":"#276749","tier":1},"4":{"name":"4단계 : 진득한 지온냄새","desc":"여름철 밀폐된 방 안에서 지온이가 뒹굴다 난 땀에 쩐 이불 냄새.","price":1900,"color":"#319795","tier":1},"5":{"name":"5단계 : 자극적인 지온냄새","desc":"지온이가 발가락을 긁은 손으로 코를 슥 만지게 만드는 향.","price":3000,"color":"#2c7a7b","tier":1},"6":{"name":"6단계 : 풍부한 지온냄새","desc":"신발장에 박아둔 지온이의 축구화 속에서 무르익은 발효 냄새.","price":4100,"color":"#3182ce","tier":2},"7":{"name":"7단계 : 압도적인 지온냄새","desc":"지온이가 다녀간 자리마다 코를 찌르는 시큼털털한 체취의 파도.","price":5700,"color":"#2b6cb0","tier":2},"8":{"name":"8단계 : 폭발하는 지온냄새","desc":"일주일 동안 안 감은 지온이 머리통에서 뿜어져 나오는 유분 폭탄.","price":7900,"color":"#805ad5","tier":2},"9":{"name":"9단계 : 시공을 뒤흔드는 지온냄새","desc":"화장실 문을 열자마자 지온이가 남기고 간 흔적의 생생함.","price":11000,"color":"#6b46c1","tier":2},"10":{"name":"10단계 : 치명적인 지온냄새","desc":"맡는 순간 안구실종을 유발하는 지온이의 살인적인 입냄새.","price":15000,"color":"#d69e2e","tier":2},"11":{"name":"11단계 : 환각을 부르는 지온냄새","desc":"썩은 청국장과 지온이의 발냄새가 콜라보를 이뤄 주마등이 스친다.","price":20000,"color":"#b7791f","tier":3},"12":{"name":"12단계 : 공간지배 지온냄새","desc":"방 문을 열기도 전에 복도까지 마중 나온 지온이의 찌든 내음.","price":26000,"color":"#dd6b20","tier":3},"13":{"name":"13단계 : 전성기 지온냄새","desc":"음식물 쓰레기통을 여름볕에 사흘간 방치한 것과 비견되는 향.","price":34000,"color":"#c05621","tier":3},"14":{"name":"14단계 : 신성한 지온냄새","desc":"너무 지독해서 눈물마저 고이게 만드는 지온이의 꼬릿한 기운.","price":45000,"color":"#e53e3e","tier":3},"15":{"name":"15단계 : 오리지널 지온냄새","desc":"하수구 역류 현상과 지온이의 입김이 만나 온 세상이 오염된다.","price":60000,"color":"#9b2c2c","tier":3},"16":{"name":"16단계 : 우주관통 지온냄새","desc":"대기권을 뚫고 오존층마저 뻥 뚫어버리는 지온이의 겨드랑이 폭풍.","price":76000,"color":"#00f0ff","tier":4},"17":{"name":"17단계 : 차원균열 지온냄새","desc":"지온이의 구린내가 너무 독해서 다른 평행세계의 코까지 썩힌다.","price":97000,"color":"#ff00ea","tier":4},"18":{"name":"18단계 : Absolute 지온냄새","desc":"우주 만물의 원소를 전부 지온이의 체취로 치환해버리는 절대악취.","price":125000,"color":"#ffe600","tier":4},"19":{"name":"19단계 : 초월 지온냄새","desc":"인간의 후각 세포를 단번에 파괴하는 초월적인 썩은 내.","price":155000,"color":"#ff0055","tier":4},"20":{"name":"20단계 : 지온이의 정성이 들어간 포근한 집밥 냄새","desc":"지온맘이 끓여준 묵은지 김치찌개... 인 줄 알았으나 지온이 빨래 냄새.","price":200000,"color":"#ffaa00","tier":4},"21":{"name":"21단계 : 지온이의 엄격한 샤우팅 냄새","desc":"안 씻고 버티는 지온이를 잡으려고 지온맘이 휘두른 등짝의 내음.","price":260000,"color":"#ff4500","tier":5},"22":{"name":"22단계 : 지온이의 전설의 흙된장국 냄새","desc":"지온이의 발냄새 원액을 살짝 타서 깊은 맛을 낸 지온맘의 특제 국물.","price":340000,"color":"#ff007f","tier":5},"23":{"name":"23단계 : 지온이의 100년 숙성 원액 냄새","desc":"지온이가 어릴 때부터 모아둔 꼬릿한 때를 장독대에 묻어 숙성시켰다.","price":440000,"color":"#7b00ff","tier":5},"24":{"name":"24단계 : 지온이의 냄새 탈취 스프레이 냄새","desc":"방 안에 쩔어 있는 지온이의 체취를 탈취제로 잡으려다 역관람당함.","price":575000,"color":"#0088ff","tier":5},"25":{"name":"25단계 : 지온이의 대인배적인 냄새","desc":"이런 지온이라도 품에 안아주는 지온맘의 대인배적 냄새 포용력.","price":750000,"color":"#00ffaa","tier":5},"26":{"name":"26단계 : 지온이의 궁극 필살기 냄새","desc":"지온이 방 문을 강제로 열고 환기시키며 뿜어내는 지온맘의 분노.","price":955000,"color":"#ccff00","tier":6},"27":{"name":"27단계 : 지온이의 창조와 냄새","desc":"지온이의 모든 악취를 정화하려다 지온맘마저 구속당한 경지.","price":1200000,"color":"#fffb00","tier":6},"28":{"name":"28단계 : 지온이의 우주창조설 냄새","desc":"우주 전체가 지온이의 발냄새 아래 무릎을 꿇고 헛구역질을 한다.","price":1550000,"color":"#ffffff","tier":6},"29":{"name":"29단계 : 딥다크 지온냄새","desc":"모든 꼬릿한 냄새의 근원이자, 지온이를 낳고 기른 위대한 악취의 여신.","price":1950000,"color":"#ff00aa","tier":6},"30":{"name":"30단계 : 태초의 지온냄새 ","desc":"우주 탄생 이전부터 존재했던 오리지널 태고의 구린내.","price":2500000,"color":"#00ffff","tier":6},"31":{"name":"31단계 : 하이퍼 지온 싱귤래리티","desc":"냄새가 너무 묵직해서 블랙홀처럼 주변 모든 빛과 산소를 빨아들인다.","price":3150000,"color":"#7000ff","tier":6},"32":{"name":"32단계 : 멀티버스 지온 에센스","desc":"모든 평행우주에 존재하는 지온이의 체취가 한곳으로 모이는 중.","price":4000000,"color":"#ff00e1","tier":6},"33":{"name":"33단계 : 인피니티 지온 페트리코","desc":"영원히 끝나지 않는 지온이의 발효 비린내가 온 은하를 뒤덮음.","price":5000000,"color":"#00ff66","tier":6},"34":{"name":"34단계 : 오메가 지온 제네시스","desc":"지온이의 냄새로 우주를 멸망시키고 다시 창조하는 종말의 향기.","price":6350000,"color":"#ff6600","tier":6},"35":{"name":"35단계 : ★디 오리지널 앱솔루트 지온★","desc":"우주 만물을 통틀어 가장 지독하고 완벽한 궁극의 지온 냄새.","price":8000000,"color":"#ffffff","tier":6},"36":{"name":"36단계 : 안드로메다 자이온 암모니아","desc":"안드로메다 은하 전체를 알칼리화시키는 암모니아 폭풍.","price":10000000,"color":"#00ffff","tier":6},"37":{"name":"37단계 : 화이트홀 자이온 하이드로겐","desc":"우주 백색왜성의 폭발과 함께 뿜어져 나오는 순백의 악취.","price":12500000,"color":"#ffffff","tier":6},"38":{"name":"38단계 : 쿼크 글루온 자이온 악취","desc":"소립자 수준에서부터 강하게 결합되어 떨어지지 않는 쿼크급 냄새.","price":16000000,"color":"#ffaa00","tier":6},"39":{"name":"39단계 : 차원왜곡 자이온 타임루프 찌든내","desc":"시간의 흐름마저 썩어버리게 만드는 과거와 미래의 냄새 집합체.","price":20000000,"color":"#9b2c2c","tier":6},"40":{"name":"40단계 : 네메시스 자이온 다크매터","desc":"빛조차 탈출하지 못하고 악취에 붙잡혀 빨려 들어가는 암흑물질.","price":25000000,"color":"#38a169","tier":6},"41":{"name":"41단계 : 메가 블랙홀 자이온 호라이즌","desc":"모든 물리 법칙이 붕괴하고 오직 자이온이의 체취만 남는 경계선.","price":31500000,"color":"#805ad5","tier":6},"42":{"name":"42단계 : 감마선 버스트 자이온 플레어","desc":"우주 끝까지 수십 광년 동안 일직선으로 뻗어 나가는 살인적 악취.","price":40000000,"color":"#e53e3e","tier":6},"43":{"name":"43단계 : 하이퍼노바 자이온 코어 붕괴","desc":"거대 항성이 생을 마감하며 방출하는 전설적인 폭발성 악취.","price":50000000,"color":"#ff4500","tier":6},"44":{"name":"44단계 : 엘더블루 제네시스 자이온","desc":"태초의 우주가 생성되기도 전에 존재했던 푸른빛의 시원(始源) 냄새.","price":63500000,"color":"#0088ff","tier":6},"45":{"name":"45단계 : 카이퍼 자이온 벨트 코스믹 더스트","desc":"태양계 외곽의 얼어붙은 얼음 조각들에 스며든 미지의 원시 악취.","price":80000000,"color":"#cbd5e1","tier":6},"46":{"name":"46단계 : 자이온오르트 클라우드 딥 프리즈","desc":"영원히 녹지 않을 것 같은 극저온 속에서 서서히 발효된 냉동 체취.","price":105000000,"color":"#319795","tier":6},"47":{"name":"47단계 : 태양풍 플라즈마 자이온제트 스트림","desc":"태양 표면에서 뿜어져 나오는 고온다습한 초고속 플라즈마 냄새.","price":135000000,"color":"#f59e0b","tier":6},"48":{"name":"48단계 : 마그네타 자이온자기장 폭풍","desc":"지구상의 모든 나침반을 고장 내고 정신을 아득하게 만드는 자기장.","price":175000000,"color":"#7000ff","tier":6},"49":{"name":"49단계 : 펄서 자이온로테이션 시그널","desc":"일정한 주기로 우주 전체에 강력한 악취 전파를 송출하는 중성자별.","price":230000000,"color":"#00ff66","tier":6},"50":{"name":"50단계 : 웜홀 크로스오버 자이온 디멘션","desc":"시공간의 통로를 열어 다른 차원의 구린내를 실시간으로 끌어온다.","price":300000000,"color":"#ff00ea","tier":6},"51":{"name":"51단계 : 스트링 시스코어 자이온 엠피리어","desc":"초끈이론의 11차원을 진동시키며 울려 퍼지는 궁극의 우주 진동음.","price":415000000,"color":"#ccff00","tier":6},"52":{"name":"52단계 : 센타우루스 자이온 알파 코어","desc":"가장 가까운 별무리의 기운을 통째로 오염시킨 강력한 은하수 향.","price":570000000,"color":"#ff6600","tier":6},"53":{"name":"53단계 : 페가수스 자이온 별자리 네뷸라","desc":"신화 속 날개 든 말의 질주를 따라 온 하늘에 퍼지는 거대 성운 향.","price":790000000,"color":"#00f0ff","tier":6},"54":{"name":"54단계 : 자이온세인트 오메가 얼티밋 에센스","desc":"우주의 수명이 다하는 순간까지 사라지지 않는 불멸의 성스러운 냄새.","price":1100000000,"color":"#ffe600","tier":6},"55":{"name":"55단계 : 코스믹 인피니티 싱귤자이온래리티","desc":"모든 차원과 우주의 모든 존재가 하나로 응축된 무한대의 악취.","price":1500000000,"color":"#ff00aa","tier":6},"56":{"name":"56단계 : 자이온트랜스센던탈 앱솔루트 가디언","desc":"차원의 벽을 넘어 초월적인 신위(神威)를 뿜어내는 가디언의 경지.","price":2200000000,"color":"#ffffff","tier":6},"57":{"name":"57단계 : 하이퍼 자이온 디바인 코어","desc":"자이온이라는 존재 자체가 우주의 신성한 법칙으로 등용한 상태.","price":3200000000,"color":"#7b00ff","tier":6},"58":{"name":"58단계 : 자이온옴니버스 마스터피스 악취","desc":"모든 평행세계를 통틀어 단 하나만 존재하는 완벽한 걸작 악취.","price":4700000000,"color":"#00ffff","tier":6},"59":{"name":"59단계 : 이터널 제네시스 울티마자이온s","desc":"우주의 탄생과 종말을 영원히 반복하게 만드는 궁극의 고리.","price":6850000000,"color":"#ff4500","tier":6},"60":{"name":"60단계 : ★심플 성지온★","desc":"문일중 3학년 5반의 냄새를 담당하는 그저 GOA.T","price":10000000000,"color":"#ffffff","tier":6}},"PROB_TABLE":{"0":[100.0,0.0,0.0,0.0],"1":[100.0,0.0,0.0,0.0],"2":[100.0,0.0,0.0,0.0],"3":[96.0,4.0,0.0,0.0],"4":[96.0,4.0,0.0,0.0],"5":[91.0,9.0,0.0,0.0],"6":[91.0,7.5,1.5,0.0],"7":[91.0,4.5,4.5,0.0],"8":[86.0,9.5,4.5,0.0],"9":[81.0,14.5,4.5,0.0],"10":[81.0,14.5,4.5,0.0],"11":[76.0,14.5,4.5,5.0],"12":[71.0,14.5,4.5,10.0],"13":[71.0,14.5,6.5,8.0],"14":[66.0,14.5,9.5,10.0],"15":[61.0,19.5,9.5,10.0],"16":[61.0,17.5,11.5,10.0],"17":[56.0,19.5,14.5,10.0],"18":[51.0,19.5,16.5,13.0],"19":[51.0,19.5,19.5,10.0],"20":[46.0,21.5,22.5,10.0],"21":[41.0,24.5,24.5,10.0],"22":[41.0,22.5,26.5,10.0],"23":[41.0,19.5,29.5,10.0],"24":[41.0,17.5,31.5,10.0],"25":[36.0,24.5,29.5,10.0],"26":[51.0,19.5,24.5,5.0],"27":[41.0,24.5,29.5,5.0],"28":[31.0,29.5,34.5,5.0],"29":[21.0,34.5,39.5,5.0],"30":[16.0,34.5,44.5,5.0],"31":[13.0,34.5,47.5,5.0],"32":[11.0,34.5,49.5,5.0],"33":[9.0,36.5,49.5,5.0],"34":[6.0,39.5,49.5,5.0],"35":[38.0,39.0,18.0,5.0],"36":[36.8,39.1,19.1,5.0],"37":[35.5,39.2,20.3,5.0],"38":[34.2,39.4,21.4,5.0],"39":[33.0,39.4,22.6,5.0],"40":[31.8,39.4,23.8,5.0],"41":[30.5,39.6,24.9,5.0],"42":[29.2,39.8,26.0,5.0],"43":[28.0,39.8,27.2,5.0],"44":[26.8,39.8,28.4,5.0],"45":[25.5,40.0,29.5,5.0],"46":[24.2,40.2,30.6,5.0],"47":[23.0,40.2,31.8,5.0],"48":[21.8,40.2,33.0,5.0],"49":[20.5,40.4,34.1,5.0],"50":[19.2,40.6,35.2,5.0],"51":[18.0,40.6,36.4,5.0],"52":[16.8,40.7,37.5,5.0],"53":[15.5,40.8,38.7,5.0],"54":[14.2,41.0,39.8,5.0],"55":[13.0,41.0,41.0,5.0],"56":[11.8,41.1,42.1,5.0],"57":[10.5,41.2,43.3,5.0],"58":[9.2,41.3,44.5,5.0],"59":[8.0,41.4,45.6,5.0]},"CRITICAL_RATE":0.05,"PITY_MAX":4};

const DB = GAME_DATA.SMELL_DB;
const PROB = GAME_DATA.PROB_TABLE;
const CRITICAL_RATE = GAME_DATA.CRITICAL_RATE;
const PITY_MAX = GAME_DATA.PITY_MAX;
const POINTS = GAME_DATA.POINT_REWARD_TABLE;
const MAX_LEVEL = 55;
const SHIELD_MAX = 5;
const TEARS_MAX = 80;
const TEARS_USE_LIMIT = 50;
const ENHANCE_COST = {"0":100,"1":100,"2":150,"3":200,"4":350,"5":450,"6":650,"7":950,"8":1300,"9":1800,"10":2400,"11":3200,"12":4200,"13":5600,"14":7500,"15":9600,"16":12000,"17":16000,"18":20000,"19":26000,"20":34000,"21":45000,"22":59000,"23":78000,"24":100000,"25":130000,"26":165000,"27":215000,"28":275000,"29":355000,"30":450000,"31":575000,"32":725000,"33":930000,"34":1200000,"35":1500000,"36":1850000,"37":2400000,"38":3050000,"39":3800000,"40":4850000,"41":6200000,"42":7800000,"43":10000000,"44":12500000,"45":16500000,"46":21500000,"47":28500000,"48":37500000,"49":49000000,"50":68500000,"51":94500000,"52":130000000,"53":185000000,"54":255000000,"55":375000000,"56":550000000,"57":810000000,"58":1200000000,"59":1750000000,"60":1750000000};

const AUX_ITEMS = {
  luck:{name:"지온의 행운가루",icon:"🍀",desc:"장착 후 강화 성공 판정이 나올 때까지 성공 확률을 +10%p 올립니다. 성공하면 효과가 발동하며 소모됩니다.",type:"enhance",moneyMult:1,pointMult:5,max:9},
  freeze:{name:"냄새 동결제",icon:"🧊",desc:"강화에서 하락 판정이 나오면 단계를 잃지 않고 유지로 바꿉니다. 하락이 나올 때까지 장착 상태가 유지됩니다.",type:"enhance",moneyMult:2,pointMult:8,max:9},
  volatile:{name:"광기의 냄새 원액",icon:"💣",desc:"일반 강화에서 성공하면 +2단계, 크리티컬이면 +3단계가 되고 성공하지 못하면 파괴로 바뀝니다. 실제 효과가 적용되면 소모됩니다.",type:"enhance",moneyMult:3,pointMult:12,max:9},
  gaoh:{name:"가오 충전제",icon:"✨",desc:"즉시 지온이의 가오를 +1 충전합니다. 천장 직전까지 사용할 수 있습니다.",type:"instant",moneyMult:2,pointMult:6,max:9},
  perfume:{name:"상인의 향수",icon:"💰",desc:"다음 판매 가격을 1.5배로 만듭니다. 한 번 판매하면 효과가 사라집니다.",type:"sale",moneyMult:2,pointMult:6,max:9},
  tear:{name:"눈물 농축액",icon:"💧",desc:"다음 눈물 기적의 상승량을 무조건 +3단계로 고정합니다.",type:"tear",moneyMult:3,pointMult:8,max:9}
};
const LEGACY_V13_PRICE = {"0":0,"1":150,"2":400,"3":600,"4":800,"5":3000,"6":3500,"7":6100,"8":10000,"9":20000,"10":35100,"11":160000,"12":350000,"13":1000000,"14":3000000,"15":7500000,"16":14200000,"17":20000000,"18":30000000,"19":47500000,"20":68300000,"21":101000000,"22":160000000,"23":230000000,"24":300000000,"25":400000000,"26":1800000000,"27":2500000000,"28":5500000000,"29":10500000000,"30":20000000000,"31":45000000000,"32":90000000000,"33":200000000000,"34":500000000000,"35":1000000000000,"36":2500000000000,"37":6000000000000,"38":15000000000000,"39":35000000000000,"40":80000000000000,"41":180000000000000,"42":400000000000000,"43":900000000000000,"44":2000000000000000,"45":4500000000000000,"46":10000000000000000,"47":22000000000000000,"48":50000000000000000,"49":120000000000000000,"50":280000000000000000,"51":600000000000000000,"52":1300000000000000000,"53":3000000000000000000,"54":7000000000000000000,"55":15000000000000000000,"56":35000000000000000000,"57":80000000000000000000,"58":200000000000000000000,"59":500000000000000000000,"60":1000000000000000000000};
const MILESTONE_STAGES = [10,20,30,40,50];
const STAGE_BONUSES = {
  stable:{icon:"🛡️",name:"안정의 길",desc:"파괴 확률 -3%p · 감소한 확률은 유지로 이동",short:"안정"},
  fury:{icon:"⚡",name:"폭주의 길",desc:"크리티컬 확률 +2%p",short:"폭주"},
  merchant:{icon:"💰",name:"장사의 길",desc:"판매가 +15% · 강화 포인트 +10%",short:"장사"}
};
function emptyStageChoices(){return {10:null,20:null,30:null,40:null,50:null};}

const INITIAL = {
  schemaVersion:20,
  enhanceAttempts:0,warpUses:0,sellCount:0,
  points:0,lastPointReward:0,pointsEarnedTotal:0,pointsSpentTotal:0,
  enhanceSuccesses:0,enhanceFailures:0,criticalCount:0,destroyCount:0,
  runData:{level:0,prev_level:0,max_level:0,money:"50000",status:"READY",shield:0,reviveTickets:0,tears:0,pity_count:0,combo:0,best_combo:0,feverFree:0,last_aux_effect:"",activeEnhanceItem:null,saleBoost:0,tearBoost:0,stageChoices:emptyStageChoices(),
    auxInventory:{luck:0,freeze:0,volatile:0,gaoh:0,perfume:0,tear:0},unlocked_warps:{10:false,20:false,30:false,40:false,45:false,50:false}}
};

let state = loadState();
let toastTimer = null;
let actionLocked = false;
let lastSceneObjectKey = "";
const feedbackSettings = { sound:false, haptic:false };
let audioCtx = null;
let devMode = false;
let delPressCount = 0;
let delPressTimer = null;
let pendingParticleOverride = null;
let pendingAnimationOverride = null;
const RESULT_PARTICLE_COLORS = {
  SUCCESS:'#22c55e',
  PITY_SUCCESS:'#22c55e',
  FAILED:'#f97316',
  DESTROYED:'#ef4444',
  HOLD:'#a855f7',
  CRITICAL:'#facc15',
  SHIELD_SAVED:'#3b82f6',
  TEARS:'#050505'
};
function resultParticleColor(status){ return pendingParticleOverride || RESULT_PARTICLE_COLORS[status] || '#ffffff'; }

function clone(o){ return JSON.parse(JSON.stringify(o)); }
function toMoneyInt(value){
  if(typeof value === "bigint") return value;
  if(typeof value === "string" && /^-?\d+$/.test(value.trim())) return BigInt(value.trim());
  const n=Number(value); if(!Number.isFinite(n)) return 0n; return BigInt(Math.trunc(n));
}
function mergeInventory(a={},b={}){
  const out=clone(INITIAL.runData.auxInventory);
  for(const k of Object.keys(out)) out[k]=Math.min(9,Math.max(0,Number(a?.[k]||0)+Number(b?.[k]||0)));
  return out;
}
function normalizeRunData(d){
  const out=Object.assign(clone(INITIAL.runData),d||{});
  out.money=toMoneyInt(out.money).toString();
  out.auxInventory=Object.assign(clone(INITIAL.runData.auxInventory),out.auxInventory||{});
  out.unlocked_warps=Object.assign(clone(INITIAL.runData.unlocked_warps),out.unlocked_warps||{});
  out.level=Math.max(0,Math.min(MAX_LEVEL,Number(out.level)||0)); out.prev_level=Math.max(0,Math.min(MAX_LEVEL,Number(out.prev_level)||0));
  out.max_level=Math.max(out.level,Math.min(MAX_LEVEL,Number(out.max_level)||0)); for(const w of [10,20,30,40,45,50]) if(out.max_level>=w||out.level>=w) out.unlocked_warps[w]=true; out.shield=Math.max(0,Math.min(SHIELD_MAX,Number(out.shield)||0));
  out.tears=Math.max(0,Math.min(TEARS_MAX,Number(out.tears)||0)); out.pity_count=Math.max(0,Math.min(Math.max(1,PITY_MAX-1),Number(out.pity_count)||0));
  out.combo=Math.max(0,Number(out.combo)||0); out.best_combo=Math.max(out.combo,Number(out.best_combo)||0); out.feverFree=Math.max(0,Math.min(1,Number(out.feverFree)||0));
  out.saleBoost=Math.max(0,Number(out.saleBoost)||0); out.tearBoost=Math.max(0,Number(out.tearBoost)||0);
  out.stageChoices=Object.assign(emptyStageChoices(),out.stageChoices||{}); for(const st of MILESTONE_STAGES) if(!STAGE_BONUSES[out.stageChoices[st]]) out.stageChoices[st]=null;
  delete out.randomEvent;
  if(!AUX_ITEMS[out.activeEnhanceItem]) out.activeEnhanceItem=null;
  return out;
}
function scaleLegacyMoney(rawMoney,lvl){
  const old=toMoneyInt(rawMoney),ref=Math.max(1,Math.min(MAX_LEVEL,Number(lvl)||1));
  const oldPrice=toMoneyInt(LEGACY_V13_PRICE[String(ref)]||1),newPrice=toMoneyInt(DB[String(ref)]?.price||500);
  if(old<=0n)return 50000n;
  if(oldPrice<=0n)return old>50000n?old:50000n;
  const scaled=old*newPrice/oldPrice;
  return scaled>50000n?scaled:50000n;
}
function cleanRemovedSystems(s){
  delete s.discoveredSmells; delete s.collectionRewards; delete s.tower;
  delete s.achievements; delete s.unlockedTitles; delete s.selectedTitle;
  delete s.raid;
  return s;
}
function loadState(){
  try{
    const saved=JSON.parse(localStorage.getItem("jion_smell_game_v3"));
    if(!saved)return clone(INITIAL);
    if(saved.schemaVersion>=15&&saved.runData){
      const s=Object.assign(clone(INITIAL),saved);s.runData=normalizeRunData(saved.runData);s.schemaVersion=20;
      return cleanRemovedSystems(s);
    }
    if(saved.schemaVersion>=13&&saved.runData){
      const s=Object.assign(clone(INITIAL),saved);s.runData=normalizeRunData(saved.runData);
      if(saved.schemaVersion<14)s.runData.money=scaleLegacyMoney(saved.runData.money,s.runData.max_level||s.runData.level).toString();
      s.schemaVersion=20;return cleanRemovedSystems(s);
    }
    const s=Object.assign(clone(INITIAL),saved),a=(saved.seasonData||{})[1]||{},b=(saved.seasonData||{})[2]||{};
    const bMax=Math.max(0,Number(b.max_level)||0),bLevel=Math.max(0,Number(b.level)||0),hadSecond=Number(saved.rebirthCount)>0||bMax>0||bLevel>0||Number(saved.currentSeason)===2;
    const maxUnified=Math.min(MAX_LEVEL,Math.max(Number(a.max_level)||0,hadSecond?35+bMax:0)),currentUnified=Math.min(MAX_LEVEL,Number(saved.currentSeason)===2?35+bLevel:(Number(a.level)||0)),src=Number(saved.currentSeason)===2?b:a;
    s.runData=normalizeRunData(Object.assign({},src,{level:currentUnified,prev_level:currentUnified,max_level:maxUnified}));
    const oldCombined=toMoneyInt(a.money||0)+toMoneyInt(b.money||0);s.runData.money=scaleLegacyMoney(oldCombined,maxUnified||currentUnified).toString();s.runData.shield=Math.min(SHIELD_MAX,(Number(a.shield)||0)+(Number(b.shield)||0));s.runData.tears=Math.max(Number(a.tears)||0,Number(b.tears)||0);s.runData.auxInventory=mergeInventory(a.auxInventory,b.auxInventory);s.runData.unlocked_warps=clone(INITIAL.runData.unlocked_warps);for(const w of [10,20,30,40,45,50])if(maxUnified>=w)s.runData.unlocked_warps[w]=true;
    s.schemaVersion=20;return cleanRemovedSystems(s);
  }catch(e){return clone(INITIAL);}
}
function save(){ localStorage.setItem("jion_smell_game_v3",JSON.stringify(state)); }
function level(){ return state.runData.level; }
function data(){ return DB[String(level())]||DB["0"]; }
function maxLevel(){ return MAX_LEVEL; }
function money(){ return toMoneyInt(state.runData.money); }
function setMoney(v){ state.runData.money=toMoneyInt(v).toString(); }
function tears(){ return state.runData.tears; }
function shield(){ return state.runData.shield; }
function pity(){ return state.runData.pity_count; }
function combo(){ return state.runData.combo||0; }
function comboMultiplier(v=combo()){ if(v>=10)return 3;if(v>=5)return 2;if(v>=3)return 1.2;if(v>=2)return 1.1;return 1; }
function comboDestroyProtection(v=combo(), destroyChance=null){
  const comboCount=Math.max(0, Number(v)||0);
  if(comboCount < 5) return 0;
  const reduction = comboCount;
  if(destroyChance===null || destroyChance===undefined) return reduction;
  return Math.min(Math.max(0, Number(destroyChance)||0), reduction);
}
function stageBonusCounts(d=state.runData){const c={stable:0,fury:0,merchant:0};for(const st of MILESTONE_STAGES){const k=d.stageChoices?.[st];if(c[k]!==undefined)c[k]++;}return c;}
function stagePointMultiplier(d=state.runData){return 1+stageBonusCounts(d).merchant*.10;}
function stageSellPercent(d=state.runData){return 100+stageBonusCounts(d).merchant*15;}
function criticalRateFor(d=state.runData,lvl=level()){if(Number(lvl)>=50)return 0;const b=stageBonusCounts(d);let r=CRITICAL_RATE+b.fury*.02;if((d.combo||0)>=10)r+=.10;else if((d.combo||0)>=5)r+=.05;return Math.min(.50,r);}
function resetCombo(d=state.runData){ d.combo=0; d.feverFree=0; }
function activeAuxItem(d=state.runData){ return d.activeEnhanceItem&&AUX_ITEMS[d.activeEnhanceItem]?d.activeEnhanceItem:null; }
function baseEnhanceCost(lvl){ return toMoneyInt(ENHANCE_COST[Number(lvl)] ?? ENHANCE_COST[59]); }
function enhanceCost(lvl){ const base=baseEnhanceCost(lvl); return (base*50n+99n)/100n; }
function effectiveEnhanceCost(mode="normal",d=state.runData){
  if((d.feverFree||0)>0) return 0n;
  let cost=enhanceCost(d.level);
  if((d.combo||0)>=10) cost=cost*70n/100n; else if((d.combo||0)>=5) cost=cost*85n/100n;
  if(mode==='berserk') cost*=2n;
  return cost;
}
function pointReward(lvl){ if(lvl<=0)return 0; return Number(POINTS[String(lvl)]??(90000+(lvl-36)*15000)); }
function dbPrice(a,b){ const lvl=b===undefined?Number(a):Number(b); return toMoneyInt(DB[String(lvl)]?.price||0); }
function warpPointCost(lvl){ return Math.round(pointReward(lvl)*23); }
function warpMoneyCost(lvl){ return (dbPrice(lvl)*115n+99n)/100n; }
function shieldPointCost(lvl){ return Math.round(pointReward(lvl)*4.0); }
function shieldMoneyCost(lvl){ const scaled=(baseEnhanceCost(lvl)*225n+99n)/100n; return scaled>42500n?scaled:42500n; }
function auxMoneyCost(key){
  const item=AUX_ITEMS[key],l=Math.min(level(),MAX_LEVEL-1),base=baseEnhanceCost(l);
  const raw=base*BigInt(item?.moneyMult||1),v=(raw*102n+99n)/100n,floor=3800n;
  return v>floor?v:floor;
}
function auxPointCost(key){
  const item=AUX_ITEMS[key],target=Math.min(level()+1,MAX_LEVEL);
  return Math.max(120,Math.round(pointReward(target)*(item?.pointMult||1)*1.02));
}
function finalBalanceProbabilities(base,lvl=level()){
  let [success,down,destroy,hold]=base.map(Number);
  const l=Math.max(0,Number(lvl)||0);
  let soften=0;
  if(l>=50&&l<=54) soften=2;
  else if(l>=45) soften=1.5;
  else if(l>=35) soften=1;
  if(soften>0){
    const moved=Math.min(destroy,soften);
    destroy-=moved;
    hold+=moved;
  }
  return [success,down,destroy,hold];
}
function effectiveProbabilities(base,itemKey=activeAuxItem(),opts={}){
  let [success,down,destroy,hold]=finalBalanceProbabilities(base,opts.level ?? level());
  const shiftToSuccess=(amount)=>{let add=Math.min(amount,100-success);success+=add;for(const name of ['destroy','down','hold']){if(add<=0)break;const cur=name==='destroy'?destroy:name==='down'?down:hold,used=Math.min(cur,add);add-=used;if(name==='destroy')destroy-=used;else if(name==='down')down-=used;else hold-=used;}};
  if(itemKey==='luck')shiftToSuccess(10);
  else if(itemKey==='freeze'){hold+=down;down=0;} else if(itemKey==='volatile'){destroy=Math.max(0,100-success);down=0;hold=0;}
  const stable=stageBonusCounts().stable;if(stable>0){const moved=Math.min(destroy,stable*3);destroy-=moved;hold+=moved;}
  if(opts.mode!=='berserk'){
    const comboGuard = comboDestroyProtection(opts.combo ?? combo());
    if(comboGuard>0){
      const moved=Math.min(destroy, comboGuard);
      destroy-=moved;
      hold+=moved;
    }
  }
  if(opts.mode==='berserk'){success=Math.max(1,success-10);destroy=100-success;down=0;hold=0;}
  return [success,down,destroy,hold].map(v=>Math.round(v*10)/10);
}

function formatMoneyParts(amount){const units=["","만","억","조","경","해","자","양","구","간","정","재","극"];let n=toMoneyInt(amount);if(n<0n)n=-n;const parts=[];let i=0;while(n>0n&&i<units.length){const r=n%10000n;if(r>0n)parts.unshift(r.toLocaleString("ko-KR")+units[i]);n/=10000n;i++;}return parts.slice(0,2);}
function formatGoldCompact(amount){const n=toMoneyInt(amount);if(n===0n)return "0";return (n<0n?"-":"")+formatMoneyParts(n).join(" ");}
function formatGold(amount){const n=toMoneyInt(amount);if(n===0n)return "0원";return (n<0n?"-":"")+formatMoneyParts(n).join(" ")+"원";}
function showToast(msg){const el=document.getElementById("toast");el.textContent=msg;el.classList.add("show");clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.classList.remove("show"),2600);}
function setActionLocked(locked){actionLocked=!!locked;document.body.classList.toggle("action-locked",actionLocked);syncActionButtons();}
function syncActionButtons(){
  const l=level(),eb=document.getElementById("enhanceBtn"),sb=document.getElementById("sellBtn"),bb=document.getElementById("berserkBtn");
  if(eb){
    eb.disabled=actionLocked||l>=MAX_LEVEL;
    eb.classList.toggle('final-hold-ready',l===MAX_LEVEL-1&&!actionLocked);
    if(l===MAX_LEVEL-1) eb.textContent='👑 길게 눌러 FINAL 강화';
    else if(l>=MAX_LEVEL) eb.textContent='55단계 MAX';
    else eb.textContent='강화하기';
  }
  if(sb)sb.disabled=actionLocked||l===0;
  if(bb){
    const available=l>=35&&l<=48;
    bb.disabled=actionLocked||!available;
    bb.textContent=l<35?'☠️ 광폭 강화 · 35단계 해금':l>48?'☠️ 광폭 강화 · 35~48단계 전용':`☠️ 광폭 강화 · ${formatGold(effectiveEnhanceCost('berserk'))}`;
  }
  const bi=document.getElementById('berserkInfo');
  if(bi){
    bi.classList.remove('hidden');
    if(l<35) bi.textContent='35단계부터 사용 가능 · 성공 시 +2~6단계 랜덤 상승';
    else if(l>48) bi.textContent='35~48단계에서만 사용 가능 · 성공 시 +2~6단계 랜덤 상승';
    else if(pity()>=PITY_MAX-1) bi.innerHTML='<b class="berserk-success-rate">성공 100%</b> · <b class="berserk-destroy-rate">파괴 0%</b> · 성공 시 <strong>+2~6단계 랜덤 상승</strong>';
    else{
      const raw=PROB[String(l)]||[8,40,47,5];
      const bp=effectiveProbabilities(raw,activeAuxItem(),{mode:'berserk'});
      bi.innerHTML=`<b class="berserk-success-rate">성공 ${bp[0]}%</b> · <b class="berserk-destroy-rate">파괴 ${bp[2]}%</b> · 성공 시 <strong>+2~6단계 랜덤 상승</strong>`;
    }
  }
  document.querySelectorAll("[data-modal]").forEach(b=>b.disabled=actionLocked);
  const reset=document.getElementById("resetBtn");if(reset)reset.disabled=actionLocked;
}
function ensureAudio(){ return null; }function tone(){}function noiseHit(){}function playSound(){}function vibrate(){}
function feedbackForStatus(status, forcedColor=null){
  const color=forcedColor||RESULT_PARTICLE_COLORS[status]||'#ffffff';
  const black=color.toLowerCase()==='#050505'||color.toLowerCase()==='#000000';
  if(status==='CRITICAL')spawnEnhanceBurst(color,112,.19,.068,.92,black?'normal':'add');
  else if(status==='DESTROYED')spawnEnhanceBurst(color,150,.23,.078,1.08,black?'normal':'add');
  else if(status==='SHIELD_SAVED')spawnEnhanceBurst(color,92,.15,.064,.84,black?'normal':'add');
  else if(status==='FAILED')spawnEnhanceBurst(color,72,.13,.058,.76,black?'normal':'add');
  else if(status==='HOLD')spawnEnhanceBurst(color,58,.10,.054,.70,black?'normal':'add');
  else spawnEnhanceBurst(color,86,.15,.060,.82,black?'normal':'add');
}


/* --------------------------- Developer mode --------------------------- */
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

function updateFeedbackControls(){}function bindFeedbackControls(){}
function rewardPoints(lvl,multiplier=1){const r=Math.max(0,Math.round(pointReward(lvl)*multiplier*stagePointMultiplier()));state.points+=r;state.pointsEarnedTotal+=r;state.lastPointReward=r;}
function registerEnhanceSuccess(d){const prev=d.combo||0;d.combo=prev+1;d.best_combo=Math.max(d.best_combo||0,d.combo);if(prev<10&&d.combo>=10)d.feverFree=1;return comboMultiplier(d.combo);}
function registerEnhanceFailure(d){resetCombo(d);}
function unlockReachedWarps(d=state.runData){for(const w of [10,20,30,40,45,50])if(d.max_level>=w||d.level>=w)d.unlocked_warps[w]=true;}

function nextMilestoneChoice(prevLvl,newLvl,d=state.runData){return MILESTONE_STAGES.find(st=>prevLvl<st&&newLvl>=st&&!d.stageChoices?.[st])||null;}
function applyStageChoice(stage,key){const d=state.runData,st=Number(stage);if(!MILESTONE_STAGES.includes(st)||!STAGE_BONUSES[key])return false;if((d.max_level||0)<st&&(d.level||0)<st)return false;d.stageChoices=d.stageChoices||emptyStageChoices();const prev=d.stageChoices[st]||null;d.stageChoices[st]=key;save();render();return prev!==key;}
function showStageChoiceOverlay(stage,done=()=>{}){
  const overlay=document.createElement('div');overlay.className='system-choice-overlay';
  overlay.innerHTML=`<div class="system-choice-box"><small>MILESTONE ${stage}</small><h2>🎯 ${stage}단계 선택 보너스</h2><p>선택 후에도 🎯 보너스 메뉴에서 언제든 다른 보너스로 변경할 수 있습니다. 같은 계열을 여러 단계에서 선택하면 효과가 중첩됩니다.</p><div class="choice-card-grid">${Object.entries(STAGE_BONUSES).map(([key,b])=>`<button class="choice-card ${key}" data-system-choice="${key}"><span>${b.icon}</span><b>${b.name}</b><small>${b.desc}</small></button>`).join('')}</div></div>`;
  document.body.appendChild(overlay);requestAnimationFrame(()=>overlay.classList.add('show'));
  overlay.querySelectorAll('[data-system-choice]').forEach(btn=>btn.onclick=()=>{const key=btn.dataset.systemChoice;if(!applyStageChoice(stage,key))return;overlay.classList.remove('show');setTimeout(()=>{overlay.remove();showToast(`${STAGE_BONUSES[key].icon} ${stage}단계 · ${STAGE_BONUSES[key].name} 선택!`);done();},220);});
}
function runPostEnhanceFlow(prevLvl,newLvl,done=()=>{}){
  runMilestoneOnly(prevLvl,newLvl,()=>{setActionLocked(false);done();});
}
function runMilestoneOnly(prevLvl,newLvl,done=()=>{}){const milestone=nextMilestoneChoice(prevLvl,newLvl);if(milestone)showStageChoiceOverlay(milestone,()=>runMilestoneOnly(milestone,newLvl,done));else done();}


function showBerserkRoulette(finalGain,done=()=>{}){
  const gain=Math.max(2,Math.min(6,Number(finalGain)||2));
  document.querySelectorAll('.berserk-roulette-overlay').forEach(e=>e.remove());
  const overlay=document.createElement('div');
  overlay.className='berserk-roulette-overlay';
  overlay.innerHTML=`<div class="berserk-roulette-box">
    <small>☠ BERSERK ASCENSION</small>
    <div class="berserk-roulette-kicker">RANDOM STAGE BOOST</div>
    <div class="berserk-roulette-window"><span id="berserkRouletteValue">+2</span></div>
    <div class="berserk-roulette-range">+2 · +3 · +4 · +5 · +6</div>
    <b class="berserk-roulette-result">ROLLING...</b>
  </div>`;
  document.body.appendChild(overlay);
  requestAnimationFrame(()=>overlay.classList.add('show'));
  const value=overlay.querySelector('#berserkRouletteValue'),result=overlay.querySelector('.berserk-roulette-result'),box=overlay.querySelector('.berserk-roulette-box');
  let tick=0;const sequence=[];
  for(let i=0;i<20;i++)sequence.push(2+((i*3+gain*2+i*i)%5));
  sequence.push(gain);
  const step=()=>{
    if(!overlay.isConnected)return;
    const v=sequence[tick];value.textContent=`+${v}`;
    gsap.fromTo(value,{scale:.74,y:-14,opacity:.45,rotationX:-55},{scale:1,y:0,opacity:1,rotationX:0,duration:.075,ease:'power3.out'});
    if(tick<sequence.length-1){tick++;setTimeout(step,55+tick*7);return;}
    overlay.classList.add('locked');result.textContent=`☠ BERSERK +${gain}`;
    cardBurst('#ef4444',gain===6?170:120,gain===6?320:235);impactFlash(gain===6?.68:.38);
    gsap.fromTo(box,{scale:.94},{scale:gain===6?1.09:1.05,duration:.14,ease:'power4.out',yoyo:true,repeat:1});
    gsap.fromTo(value,{scale:1},{scale:gain===6?1.36:1.20,duration:.16,ease:'back.out(2.4)',yoyo:true,repeat:1});
    setTimeout(()=>{overlay.classList.remove('show');setTimeout(()=>{overlay.remove();done();},210);},gain===6?760:580);
  };
  setTimeout(step,150);
}



function showTearRoulette(finalGain,done=()=>{}){
  const gain=Math.max(1,Math.min(3,Number(finalGain)||1));
  document.querySelectorAll('.tear-roulette-overlay').forEach(e=>e.remove());
  const overlay=document.createElement('div');
  overlay.className='berserk-roulette-overlay tear-roulette-overlay';
  overlay.innerHTML=`<div class="berserk-roulette-box tear-roulette-box">
    <small>💧 JION TEARS MIRACLE</small>
    <div class="berserk-roulette-kicker">GUARANTEED ASCENSION</div>
    <div class="berserk-roulette-window tear-roulette-window"><span id="tearRouletteValue">+1</span></div>
    <div class="berserk-roulette-range">+1 · +2 · +3</div>
    <b class="berserk-roulette-result">MIRACLE ROLL...</b>
  </div>`;
  document.body.appendChild(overlay);
  requestAnimationFrame(()=>overlay.classList.add('show'));
  const value=overlay.querySelector('#tearRouletteValue');
  const result=overlay.querySelector('.berserk-roulette-result');
  const box=overlay.querySelector('.berserk-roulette-box');
  let tick=0;
  const sequence=[];
  for(let i=0;i<15;i++) sequence.push(1+((i*2+gain+i*i)%3));
  sequence.push(gain);
  const finishSafe=()=>{
    try{done();}catch(err){console.error('tear animation callback failed',err);setActionLocked(false);}
  };
  const step=()=>{
    if(!overlay.isConnected){finishSafe();return;}
    const v=sequence[tick];
    value.textContent=`+${v}`;
    gsap.fromTo(value,{scale:.70,y:-18,opacity:.35,rotationX:-65},{scale:1,y:0,opacity:1,rotationX:0,duration:.082,ease:'power3.out'});
    if(tick<sequence.length-1){
      const delay=48+tick*7;
      tick++;
      setTimeout(step,delay);
      return;
    }
    value.textContent=`+${gain}`;
    result.textContent=gain===3?'MIRACLE MAX +3':`MIRACLE +${gain}`;
    overlay.classList.add('locked','tear-locked');
    cardBurst('#050505',gain===3?145:110,gain===3?285:225);
    impactFlash(gain===3?.56:.34);
    gsap.fromTo(box,{scale:.94},{scale:1.05,duration:.14,ease:'power4.out',yoyo:true,repeat:1});
    gsap.fromTo(value,{scale:1},{scale:gain===3?1.30:1.18,duration:.16,ease:'back.out(2.4)',yoyo:true,repeat:1});
    setTimeout(()=>{
      overlay.classList.remove('show');
      setTimeout(()=>{overlay.remove();finishSafe();},210);
    },gain===3?700:560);
  };
  setTimeout(step,150);
}

let pendingDestroySnapshot=null;
function clearDestroySnapshot(){
  if(!pendingDestroySnapshot)return;
  try{pendingDestroySnapshot.layer?.remove();}catch(e){}
  pendingDestroySnapshot=null;
}
function captureDestroySnapshot(){
  clearDestroySnapshot();
  const scene=document.getElementById('enhanceCardScene');
  const card=document.getElementById('enhanceCard');
  const art=card?.querySelector('.card-art');
  if(!scene||!card||!art)return null;
  const sr=scene.getBoundingClientRect(),ar=art.getBoundingClientRect();
  if(!ar.width||!ar.height)return null;
  const layer=document.createElement('div');
  layer.className='destroy-snapshot-layer destroy-art-layer';
  layer.style.left=`${ar.left-sr.left}px`;
  layer.style.top=`${ar.top-sr.top}px`;
  layer.style.width=`${ar.width}px`;
  layer.style.height=`${ar.height}px`;
  const clone=art.cloneNode(true);
  clone.removeAttribute('id');
  clone.querySelectorAll('[id]').forEach(el=>el.removeAttribute('id'));
  clone.classList.add('destroy-visual-card','destroy-art-only');
  layer.appendChild(clone);
  scene.appendChild(layer);
  pendingDestroySnapshot={layer,card:clone};
  return pendingDestroySnapshot;
}
function addDestroyCracks(card,count=14){
  const frag=document.createDocumentFragment();
  for(let i=0;i<count;i++){
    const crack=document.createElement('i');
    crack.className='destruction-crack';
    crack.style.setProperty('--cx',`${18+Math.random()*64}%`);
    crack.style.setProperty('--cy',`${12+Math.random()*72}%`);
    crack.style.setProperty('--cl',`${52+Math.random()*115}px`);
    crack.style.setProperty('--ca',`${-80+Math.random()*160}deg`);
    crack.style.setProperty('--cd',`${i*.018}s`);
    frag.appendChild(crack);
  }
  card.appendChild(frag);
}
function spawnDestroyShards(layer,color='#ef4444',count=28){
  const scene=document.getElementById('enhanceCardScene');
  if(!scene||!layer)return;
  const lr=layer.getBoundingClientRect(),sr=scene.getBoundingClientRect();
  const cx=lr.left-sr.left+lr.width/2,cy=lr.top-sr.top+lr.height/2;
  const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const maxCount=reduced?10:(window.innerWidth<700?18:count);
  const frag=document.createDocumentFragment(),shards=[];
  for(let i=0;i<maxCount;i++){
    const shard=document.createElement('i');
    shard.className='destruction-shard';
    shard.style.left=`${cx}px`; shard.style.top=`${cy}px`;
    shard.style.setProperty('--shard-color',color);
    shard.style.width=`${18+Math.random()*44}px`;
    shard.style.height=`${10+Math.random()*34}px`;
    shard.style.clipPath=`polygon(${Math.floor(Math.random()*25)}% 0, 100% ${Math.floor(15+Math.random()*45)}%, ${Math.floor(45+Math.random()*45)}% 100%, 0 ${Math.floor(55+Math.random()*40)}%)`;
    frag.appendChild(shard); shards.push(shard);
  }
  scene.appendChild(frag);
  shards.forEach((shard,i)=>{
    const a=Math.random()*Math.PI*2,dist=120+Math.random()*280;
    gsap.fromTo(shard,{x:0,y:0,z:0,rotation:0,rotationX:0,rotationY:0,scale:.6,opacity:1},{
      x:Math.cos(a)*dist,y:Math.sin(a)*dist+60+Math.random()*90,z:80+Math.random()*260,
      rotation:(Math.random()-.5)*720,rotationX:(Math.random()-.5)*520,rotationY:(Math.random()-.5)*520,
      scale:.18+Math.random()*.55,opacity:0,duration:.72+Math.random()*.35,delay:i*.004,ease:'power3.out',onComplete:()=>shard.remove()
    });
  });
}
function playDestroyedCardSequence(actualCard,glow,finish,particleColor,commitVisual){
  const snap=pendingDestroySnapshot;
  pendingDestroySnapshot=null;
  const layer=snap?.layer,ghost=snap?.card;
  const scene=document.getElementById('enhanceCardScene');
  if(!scene||!actualCard||!layer||!ghost){
    clearDestroySnapshot();
    gsap.set(actualCard,{opacity:1,scale:1});
    finish();
    return;
  }
  actualCard.style.visibility='hidden';
  ghost.classList.add('destroy-phase-active');
  addDestroyCracks(ghost,15);
  const core=document.createElement('i');core.className='destruction-core-collapse';layer.appendChild(core);
  const voidRing=document.createElement('i');voidRing.className='destruction-void-ring';scene.appendChild(voidRing);
  const tl=gsap.timeline({onComplete:()=>{
    layer.remove();voidRing.remove();
    actualCard.style.visibility='visible';
    gsap.set(actualCard,{opacity:1,scale:1,x:0,y:0,rotation:0,filter:'drop-shadow(0 28px 55px rgba(0,0,0,.42))'});
    finish();
  }});
  gsap.set(actualCard,{opacity:0,scale:.34,y:18});
  gsap.set(voidRing,{opacity:0,scale:.2});
  tl.to(ghost,{x:-11,rotation:-3.2,filter:'brightness(1.7) saturate(1.65)',duration:.055,ease:'power4.out'})
    .to(ghost,{x:13,rotation:4.2,duration:.055})
    .to(ghost,{x:-10,rotation:-3.4,duration:.055})
    .to(ghost,{x:9,rotation:2.8,duration:.055})
    .to(ghost,{x:0,rotation:0,scale:1.025,filter:'brightness(2.25) saturate(1.9)',duration:.09,ease:'power3.out'})
    .add(()=>{impactFlash(.92);screenShake(.34,.32);spawnDestroyShards(layer,particleColor,32);cardBurst(particleColor,120,300);},'<')
    .to(core,{scale:2.6,opacity:0,duration:.28,ease:'power4.out'},'<')
    .to(ghost,{scale:.72,rotationX:16,rotationY:-10,opacity:0,filter:'blur(8px) brightness(.25) saturate(.25)',duration:.24,ease:'power4.in'},'<+.04')
    .fromTo(voidRing,{opacity:.85,scale:.15},{opacity:0,scale:2.9,duration:.46,ease:'power3.out'},'<-.02')
    .to({}, {duration:.12})
    .add(()=>{if(typeof commitVisual==='function')commitVisual();actualCard.style.visibility='visible';},'>')
    .fromTo(actualCard,{opacity:0,scale:.28,y:28,rotationY:-18,filter:'brightness(2.0) saturate(.2) blur(6px)'},{opacity:1,scale:1.075,y:-8,rotationY:4,filter:'brightness(1.35) saturate(1.1) blur(0px)',duration:.32,ease:'back.out(2.15)'})
    .to(actualCard,{scale:1,y:0,rotationY:0,filter:'brightness(1) saturate(1)',duration:.28,ease:'elastic.out(1,.48)'})
    .add(()=>cardBurst('#94a3b8',52,150),'<-.18');
  if(glow)gsap.fromTo(glow,{scale:.8,opacity:.08},{scale:2.2,opacity:.65,duration:.16,yoyo:true,repeat:1,ease:'power4.out'});
}

let finalHoldAuthorized=false;
function enhance(mode="normal"){
  if(actionLocked)return;
  const d=state.runData,curr=d.level;
  if(curr===MAX_LEVEL-1&&mode==='normal'&&!finalHoldAuthorized){showToast('👑 FINAL 강화는 강화 버튼을 길게 눌러야 합니다.');return;}
  if(mode==='berserk'&&(curr<35||curr>48)){showToast('☠️ 광폭 강화는 35~48단계에서만 사용할 수 있습니다.');return;}
  const cost=effectiveEnhanceCost(mode,d);
  if(curr>=MAX_LEVEL){render();return;}
  const cash=money();if(cash<cost){d.status="NOT_ENOUGH_MONEY";showToast("강화 비용 부족!");render();return;}
  setActionLocked(true);finalHoldAuthorized=false;setMoney(cash-cost);
  const useFeverFree=(d.feverFree||0)>0;if(useFeverFree)d.feverFree=0;d.prev_level=curr;state.enhanceAttempts++;
  const aux=activeAuxItem(d);d.last_aux_effect="";let berserkGain=0;
  const appendAuxEffect=(msg)=>{if(!msg)return;d.last_aux_effect=d.last_aux_effect?`${d.last_aux_effect} · ${msg}`:msg;};
  const consumeActiveAux=(msg)=>{
    if(aux&&d.activeEnhanceItem===aux)d.activeEnhanceItem=null;
    appendAuxEffect(msg);
  };
  const successResult=(baseAdd=1,status="SUCCESS",isCritical=false)=>{
    let add=baseAdd;
    if(mode==='berserk'){add=2+Math.floor(Math.random()*5);berserkGain=add;appendAuxEffect(`☠️ 광폭 +${add}단계`);}
    if(aux==='volatile'&&mode!=='berserk'){
      add=isCritical?Math.max(3,add):Math.max(2,add);
      consumeActiveAux(isCritical?"💣 원액 크리티컬 발동":"💣 원액 성공 발동");
    }else if(aux==='luck'){
      consumeActiveAux("🍀 행운가루 성공 발동");
    }
    d.level=Math.min(MAX_LEVEL,d.level+add);d.status=status;d.pity_count=0;d.max_level=Math.max(d.max_level,d.level);state.enhanceSuccesses++;if(isCritical)state.criticalCount++;
    const mult=registerEnhanceSuccess(d);rewardPoints(d.level,mult);
  };
  const destroyResult=()=>{
    if(aux==='volatile'&&mode!=='berserk')consumeActiveAux("💣 원액 폭발 발동");
    if(d.shield>0){d.shield--;d.pity_count++;d.status="SHIELD_SAVED";state.enhanceFailures++;d.tears=Math.min(TEARS_MAX,d.tears+1);appendAuxEffect(mode==='berserk'?'☠️ 광폭 폭발 · 방지권 생존':'');}
    else{d.pity_count++;d.level=0;d.status="DESTROYED";state.enhanceFailures++;state.destroyCount++;d.tears=Math.min(TEARS_MAX,d.tears+2);appendAuxEffect(mode==='berserk'?'☠️ 광폭 강화 폭발':'');}
    registerEnhanceFailure(d);
  };
  const guaranteed=devMode||d.pity_count>=PITY_MAX-1;
  if(guaranteed){successResult(1,devMode?"SUCCESS":"PITY_SUCCESS",false);}
  else{
    const raw=PROB[String(curr)]||[8,40,47,5];
    // 동결제는 표시 확률상 하락→유지지만, 실제 원래 판정이 하락인지 확인한 뒤 그 순간에만 소모한다.
    const rollAux=aux==='freeze'?null:aux;
    const [sp,downP,dp]=effectiveProbabilities(raw,rollAux,{mode});
    const r=Math.random()*100,down=sp+downP,destroy=down+dp;
    if(r<sp){const critRate=criticalRateFor(d,curr),critical=Math.random()<critRate&&curr+2<=MAX_LEVEL;successResult(critical?2:1,critical?"CRITICAL":"SUCCESS",critical);}
    else if(mode==='berserk')destroyResult();
    else if(r<down){
      d.pity_count++;state.enhanceFailures++;d.tears=Math.min(TEARS_MAX,d.tears+1);
      if(aux==='freeze'){
        d.status="HOLD";consumeActiveAux("🧊 동결 발동 · 하락 → 유지");
      }else{
        if(curr>0)d.level--;d.status="FAILED";
      }
      registerEnhanceFailure(d);
    }
    else if(r<destroy)destroyResult();
    else{d.pity_count++;d.status="HOLD";state.enhanceFailures++;d.tears=Math.min(TEARS_MAX,d.tears+1);registerEnhanceFailure(d);}
  }
  unlockReachedWarps(d);const newLvl=d.level,isFinalAttempt=curr===MAX_LEVEL-1;if(d.status==="DESTROYED"&&!isFinalAttempt)captureDestroySnapshot();save();
  const normalPost=()=>{
    const done=()=>runPostEnhanceFlow(curr,newLvl);
    // 54 → 55 FINAL attempt: every outcome shares the exact same cinematic.
    // The result is intentionally hidden until the common impact/reveal beat.
    if(isFinalAttempt&&mode==='normal') animateFinal54To55(d.status,done);
    else animateResult(d.status,done);
  };
  if(mode==='berserk'&&berserkGain>0) showBerserkRoulette(berserkGain,normalPost);
  else normalPost();
}
function sell(){if(actionLocked)return;const d=state.runData,l=d.level;if(l===0)return;const basePrice=dbPrice(l),perfume=d.saleBoost>0;let price=basePrice*BigInt(stageSellPercent(d))/100n;if(perfume)price=price*3n/2n;d.saleBoost=0;setMoney(money()+price);state.sellCount++;d.prev_level=l;d.level=0;d.status="READY";d.last_aux_effect="";resetCombo(d);save();render();const tags=[stageBonusCounts(d).merchant?`장사 보너스 +${stageBonusCounts(d).merchant*15}%`:"",perfume?"향수 1.5배":""].filter(Boolean).join(" · ");showToast(`💰 ${l}단계 판매 완료! +${formatGold(price)}${tags?` · ${tags}`:""}`);}
function updateStageBackground(l=level()){
  const bg=document.getElementById('stageBackdrop');
  if(!bg)return;
  const lv=Math.max(0,Math.min(MAX_LEVEL,Number(l)||0));
  const hue=lv===0?220:(lv*43+117)%360;
  const hue2=(hue+58+(lv%7)*9)%360;
  const hue3=(hue+154+(lv%5)*13)%360;
  const sat1=64+(lv%5)*5, sat2=68+(lv%4)*6;
  const light1=14+Math.min(10,Math.floor(lv/6));
  const light2=17+Math.min(12,Math.floor(lv/5));
  const intensity=(.42+lv/Math.max(1,MAX_LEVEL)*.34).toFixed(2);
  const x1=12+(lv*17)%72, y1=10+(lv*29)%68;
  const x2=18+(lv*31)%68, y2=14+(lv*23)%66;
  const x3=20+(lv*13)%62, y3=18+(lv*37)%58;
  bg.dataset.level=String(lv);
  bg.dataset.pattern=String(lv%6);
  bg.style.setProperty('--stage-c1',`hsl(${hue} ${sat1}% ${light1}%)`);
  bg.style.setProperty('--stage-c2',`hsl(${hue2} ${sat2}% ${light2}%)`);
  bg.style.setProperty('--stage-c3',`hsl(${hue3} 78% ${12+Math.floor(lv/8)}%)`);
  bg.style.setProperty('--stage-glow',`hsla(${hue2} 92% 65% / ${intensity})`);
  bg.style.setProperty('--stage-x1',x1+'%'); bg.style.setProperty('--stage-y1',y1+'%');
  bg.style.setProperty('--stage-x2',x2+'%'); bg.style.setProperty('--stage-y2',y2+'%');
  bg.style.setProperty('--stage-x3',x3+'%'); bg.style.setProperty('--stage-y3',y3+'%');
  bg.style.setProperty('--stage-angle',`${(lv*19)%360}deg`);
  bg.style.setProperty('--stage-scale',String(1+Math.min(.38,lv/180)));
  bg.style.setProperty('--stage-opacity',String(.56+Math.min(.28,lv/120)));
  document.body.dataset.stage=String(lv);
}

function render(){
  const d=data(),sd=state.runData,l=level();
  updateStageBackground(l);
  const mainStage=document.getElementById("threeWrap"),actionGrid=document.getElementById("mainActionGrid");
  if(mainStage)mainStage.classList.remove("hidden");if(actionGrid)actionGrid.classList.remove("hidden");
  const tearsLabel=document.getElementById('tearsLabel'),pityLabel=document.getElementById('pityLabel'),comboLabel=document.getElementById('comboLabel'),auxLabel=document.getElementById('auxLabel');
  if(tearsLabel)tearsLabel.textContent='💧 눈물';if(pityLabel)pityLabel.textContent='✨ 지온이의 가오';if(comboLabel)comboLabel.textContent='🔥 연속 콤보';if(auxLabel)auxLabel.textContent='🧪 장착 보조';
  document.getElementById("money").textContent=formatGoldCompact(money());document.getElementById("points").textContent=state.points.toLocaleString("ko-KR")+"P";document.getElementById("shield").textContent=shield()+` / ${SHIELD_MAX}개`;
  const pityTarget=Math.max(1,PITY_MAX-1);document.getElementById("tears").textContent=tears()+` / ${TEARS_MAX}개`;document.getElementById("pity").textContent=pity()>=pityTarget?"다음 강화 확정":"천장까지 "+(pityTarget-pity())+"회";
  const comboNow=sd.combo||0,comboEl=document.getElementById("combo"),comboBonus=document.getElementById("comboBonus");
  if(comboEl)comboEl.textContent=comboNow>=10?`⚡ OVER FEVER · ${comboNow}`:comboNow>=5?`🔥 FEVER · ${comboNow}`:`${comboNow} COMBO`;
  if(comboBonus){const currentMult=comboMultiplier(comboNow),multText=Number.isInteger(currentMult)?String(currentMult):currentMult.toFixed(1),comboGuard=comboDestroyProtection(comboNow),guardText=comboGuard>0?` · 파괴 -${comboGuard}%`:'';comboBonus.textContent=`포인트 x${multText}${guardText}`;comboBonus.classList.remove("hidden");}
  document.body.classList.toggle('combo-fever',comboNow>=5);document.body.classList.toggle('combo-over-fever',comboNow>=10);document.body.classList.toggle("smell-frenzy",comboNow>=5);
  const modBar=document.getElementById('runModifierBar');if(modBar){const counts=stageBonusCounts(sd),tags=[];if(counts.stable)tags.push(`🛡️ 안정 x${counts.stable}`);if(counts.fury)tags.push(`⚡ 폭주 x${counts.fury}`);if(counts.merchant)tags.push(`💰 장사 x${counts.merchant}`);if(sd.feverFree)tags.push('⚡ 다음 강화 무료');modBar.innerHTML=tags.map(t=>`<span>${t}</span>`).join('');modBar.classList.toggle('hidden',!tags.length);}
  const active=activeAuxItem(sd),activeEl=document.getElementById("auxActive"),activeHint=document.getElementById("auxHint"),activeEffects=[];if(active)activeEffects.push(`${AUX_ITEMS[active].icon} ${AUX_ITEMS[active].name}`);if(sd.saleBoost)activeEffects.push("💰 상인의 향수");if(sd.tearBoost)activeEffects.push("💧 눈물 농축액");if(activeEl)activeEl.textContent=activeEffects.length?activeEffects.join(" · "):"없음";if(activeHint){activeHint.textContent=active?"발동 조건이 나올 때까지 장착 유지 · 직접 해제 가능":activeEffects.length?`${activeEffects.length}개 효과 활성화 중`:"상점에서 장착 가능";activeHint.classList.remove("hidden");}
  const modeTitle=document.getElementById("modeTitle"),probTitle=document.querySelector(".prob-title"),probBox=document.getElementById("probBox"),nextReward=document.getElementById("nextReward");
  if(modeTitle){modeTitle.textContent="";modeTitle.classList.add("hidden");}
  if(probTitle)probTitle.innerHTML=`📊 현재 강화 확률 (<span id="probLevel">${l}</span>단계)`;
  const rawP=l>=MAX_LEVEL?[100,0,0,0]:(PROB[String(l)]||[8,40,47,5]),p=effectiveProbabilities(rawP,activeAuxItem(sd)),comboGuardNow=comboDestroyProtection(sd.combo, rawP[2]),comboProbNote=comboGuardNow>0?`<div class="prob-aux combo-guard-note">🔥 콤보 안정화 · 파괴 -${comboGuardNow}% → 유지로 전환</div>`:'',auxProbNote=activeAuxItem(sd)?`<div class="prob-aux">${AUX_ITEMS[activeAuxItem(sd)].icon} ${AUX_ITEMS[activeAuxItem(sd)].name} 적용 예정</div>`:"",critPct=Math.round(criticalRateFor(sd,l)*1000)/10,critCopy=l>=50?'✦ 50단계 이후 크리티컬 비활성':'✦ 성공 시 크리티컬 확률';
  if(probBox)probBox.innerHTML=`<div class="prob-row success-row"><span><i></i>성공</span><b class="success">${p[0]}%</b></div><div class="prob-row down-row"><span><i></i>하락</span><b class="down">${p[1]}%</b></div><div class="prob-row destroy-row"><span><i></i>파괴</span><b class="destroy">${p[2]}%</b></div><div class="prob-row hold-row"><span><i></i>유지</span><b class="hold">${p[3]}%</b></div><div class="prob-critical ${l>=50?'disabled-critical':''}">${critCopy} <b>${critPct}%</b></div>${comboProbNote}${auxProbNote}`;
  if(nextReward){nextReward.textContent="";nextReward.classList.add("hidden");}
  const sb=document.getElementById("sellBtn");if(sb)sb.textContent="판매하기";syncActionButtons();renderSceneText();renderEnhanceCard();
}
function renderSceneText(){
  const d=data(),l=level(),status=state.runData.status,tier=Math.min(6,d.tier||1),main=document.getElementById("mainTitle");
  main.className="title-tier-"+tier;main.textContent=d.name;document.getElementById("descText").textContent=`"${d.desc}"`;
  document.getElementById("priceText").textContent="예상 가치: "+formatGold(dbPrice(l));document.getElementById("pointText").textContent="획득 포인트: "+pointReward(l).toLocaleString("ko-KR")+"P";
  document.getElementById("costText").textContent=l>=MAX_LEVEL?"강화 완성 · FINAL STAGE 55":"필요 강화 비용: "+(effectiveEnhanceCost("normal")===0n?"무료":formatGold(effectiveEnhanceCost("normal")));
  const st=document.getElementById("statusText"),labels={READY:"READY - 55단계를 향한 냄새 에너지가 집중됩니다",SUCCESS:"✨ COSMIC SUCCESS (강화 성공) ✨",CRITICAL:"⚡ COSMIC CRITICAL HIT!! (+2단계 이상 대성공) ⚡",PITY_SUCCESS:"✨ 지온이의 가오 발동! (천장 100% 성공) ✨",SHIELD_SAVED:"🛡️ SHIELD PROTECTED! (파괴 방지권 발동) 🛡️",DESTROYED:"💥 ODOR CAPSULE BREACHED (캡슐 대폭발 붕괴!) 💥",FAILED:"🔻 FAILED (단계 하락) 🔻",HOLD:"🔒 HOLD (단계 유지) 🔒",NOT_ENOUGH_MONEY:"💰 강화 비용 부족"};
  st.textContent=labels[status]||status;const colors={READY:"#38bdf8",SUCCESS:d.color,CRITICAL:"#fff",PITY_SUCCESS:"#fde68a",SHIELD_SAVED:"#60a5fa",DESTROYED:"#f00",FAILED:"#64748b",HOLD:"#94a3b8",NOT_ENOUGH_MONEY:"#f87171"};st.style.color=colors[status]||"#38bdf8";
  const shouldShake=l>=15||(l===MAX_LEVEL&&["SUCCESS","CRITICAL","PITY_SUCCESS"].includes(status));["mainTitle","descText","priceText","pointText","costText"].forEach(id=>document.getElementById(id).classList.toggle("shaking-text",shouldShake));
}
function cardMeta(tier){
  const map={
    1:['RARE','title-tier-1'],2:['EPIC','title-tier-2'],3:['LEGEND','title-tier-3'],
    4:['MYTHIC','title-tier-4'],5:['COSMIC','title-tier-5'],6:['ABSOLUTE','title-tier-6']
  }; return map[Math.min(6,tier||1)]||map[1];
}
function renderEnhanceCard(){
  const d=data(),l=level(),[rarity]=cardMeta(d.tier),card=document.getElementById('enhanceCard');if(!card)return;
  card.style.setProperty('--card',d.color);card.style.setProperty('--card2',d.color);card.style.setProperty('--card3',l>=36?'#160625':'#071122');
  document.getElementById('cardRoute').textContent='JION ODOR CAPSULE • 0–55';document.getElementById('cardRarity').textContent=rarity;document.getElementById('cardLevel').textContent='+'+l;
  card.className='enhance-card';card.dataset.level=String(l);card.dataset.tier=String(d.tier||1);
  const tremor=document.getElementById('stageTremorLayer');if(tremor){const high=l>30;const prog=Math.max(0,Math.min(25,l-30));tremor.classList.toggle('high-stage-tremor',high);const tx=0.18+prog*.055,ty=0.12+prog*.042,tr=0.025+prog*.012;tremor.style.setProperty('--tremor-x',tx.toFixed(2)+'px');tremor.style.setProperty('--tremor-x-neg',(-tx).toFixed(2)+'px');tremor.style.setProperty('--tremor-y',ty.toFixed(2)+'px');tremor.style.setProperty('--tremor-y-neg',(-ty).toFixed(2)+'px');tremor.style.setProperty('--tremor-r',tr.toFixed(3)+'deg');tremor.style.setProperty('--tremor-r-neg',(-tr).toFixed(3)+'deg');tremor.style.setProperty('--tremor-speed',Math.max(.105,.34-prog*.0085).toFixed(3)+'s');}
  const stageSpec=stageDesignSpec(l);card.dataset.milestone=stageSpec.milestone?String(stageSpec.milestone):'';const art=document.getElementById('cardArt');if(art){art.dataset.level=String(l);art.dataset.milestone=stageSpec.milestone?String(stageSpec.milestone):'';renderCardDesign(art,l,d);updateOdorCapsuleVisual(art,l,d);}
  const bossOverlay=document.getElementById('bossStageOverlay'),bossBadge=document.getElementById('bossStageBadge'),bossCopy=document.getElementById('bossStageCopy'),bossInfo=MILESTONE_BOSS_COPY[stageSpec.milestone];
  if(bossOverlay&&bossBadge&&bossCopy){if(bossInfo){bossOverlay.classList.remove('hidden');bossBadge.textContent=bossInfo.badge;bossCopy.textContent=bossInfo.copy;}else{bossOverlay.classList.add('hidden');bossBadge.textContent='';bossCopy.textContent='';}}
  document.getElementById('cardStageLabel').textContent=l+'단계'+(l===MAX_LEVEL?' • MAX':'');document.getElementById('cardName').textContent=d.name.replace(/^\d+단계\s*:\s*/,'');document.getElementById('cardDesc').textContent=d.desc;
  document.getElementById('cardPrice').textContent=formatGold(dbPrice(l));document.getElementById('cardPoints').textContent=pointReward(l).toLocaleString('ko-KR')+'P';document.getElementById('cardCost').textContent=l>=MAX_LEVEL?'MAX':(effectiveEnhanceCost('normal')===0n?'무료':formatGold(effectiveEnhanceCost('normal')));
  document.getElementById('cardSerial').textContent=`JION • CAPSULE • ${String(l).padStart(2,'0')}`;document.getElementById('cardTier').textContent='TIER '+['I','II','III','IV','V','VI'][Math.min(5,(d.tier||1)-1)];
  const status=state.runData.status,result=document.getElementById('cardResult');if(result)result.textContent='';
  const scene=document.getElementById('enhanceCardScene');scene.style.setProperty('--glow',d.color);scene.classList.remove('status-success','status-critical','status-failed','status-hold','status-destroyed','status-shield');if(status==='SUCCESS'||status==='PITY_SUCCESS'||status==='CRITICAL')scene.classList.add(status==='CRITICAL'?'status-critical':'status-success');else if(status==='FAILED')scene.classList.add('status-failed');else if(status==='HOLD')scene.classList.add('status-hold');else if(status==='DESTROYED')scene.classList.add('status-destroyed');else if(status==='SHIELD_SAVED')scene.classList.add('status-shield');if(result)result.style.color=status==='DESTROYED'?'#ff5757':status==='FAILED'?'#cbd5e1':status==='CRITICAL'?'#fff':d.color;
}
function cardBurst(color='#ffffff', count=70, power=260){

  const box=document.getElementById('cardParticles'); if(!box)return;
  const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const mobile=window.innerWidth<700;
  const actualCount=reduced?Math.min(20,Math.ceil(count*.20)):Math.min(count,mobile?80:160);
  while(box.childElementCount>260) box.firstElementChild?.remove();
  const created=[];
  const frag=document.createDocumentFragment();
  for(let i=0;i<actualCount;i++){
    const p=document.createElement('i'); p.className='card-particle'; p.style.color=color; if(['#050505','#000000'].includes(String(color).toLowerCase()))p.classList.add('dark-particle');
    const a=Math.random()*Math.PI*2, dist=power*(.35+Math.random()*.75);
    p.dataset.dx=Math.cos(a)*dist; p.dataset.dy=Math.sin(a)*dist;
    p.style.width=p.style.height=(2+Math.random()*6)+'px'; frag.appendChild(p); created.push(p);
  }
  box.appendChild(frag);
  created.forEach((p,i)=>{
    gsap.fromTo(p,{x:0,y:0,scale:.2,opacity:0},{x:+p.dataset.dx,y:+p.dataset.dy,scale:1.4,opacity:1,duration:.18+Math.random()*.22,delay:i*.0025,ease:'power3.out',onComplete(){gsap.to(p,{opacity:0,duration:.48,ease:'power2.out',onComplete:()=>p.remove()})}});
  });
}

const MILESTONE_BOSS_COPY = {
  10:{badge:"FIRST ASCENSION",copy:"왕관이 각성했다 · 첫 번째 보스 등급 진입"},
  20:{badge:"OVERDRIVE REACTOR",copy:"과충전 코어 개방 · 에너지 한계 돌파"},
  25:{badge:"ABSOLUTE PRISM",copy:"절대 프리즘 완성 · 성역급 광휘 발현"},
  30:{badge:"DARK DOMINION",copy:"심연 지배권 개방 · 군주급 카드로 진화"},
  35:{badge:"TRANSCENDENT THRONE",copy:"초월 왕좌 · 상위 단계 진입"},
  40:{badge:"COSMIC GATE",copy:"40단계 우주 관문 개방"},
  50:{badge:"OMNIVERSE CORE",copy:"50단계 옴니버스 코어 각성"},
  55:{badge:"INFINITE SUMMIT",copy:"55단계 완성 · FINAL ODOR CAPSULE"}
};

const STAGE_ART_LIBRARY = {
  0:{name:"Dormant Prototype", primary:"diamond", secondary:"frame", tertiary:"runes", particles:4, sigil:"PROTO 00", rune:"P-00"},
  1:{name:"Dawn Sigil", primary:"diamond", secondary:"halo", tertiary:"runes", particles:5, sigil:"DAWN 01", rune:"S-01"},
  2:{name:"Hex Bloom", primary:"hex", secondary:"lattice", tertiary:"shards", particles:5, sigil:"BLOOM 02", rune:"S-02"},
  3:{name:"Reactor Trace", primary:"reactor", secondary:"frame", tertiary:"beacons", particles:6, sigil:"TRACE 03", rune:"S-03"},
  4:{name:"Blade Crest", primary:"blades", secondary:"chevrons", tertiary:"halo", particles:6, sigil:"CREST 04", rune:"S-04"},
  5:{name:"Portal Seed", primary:"portal", secondary:"wave", tertiary:"runes", particles:6, sigil:"SEED 05", rune:"S-05"},
  6:{name:"Prism Pulse", primary:"prism", secondary:"arcs", tertiary:"frame", particles:7, sigil:"PULSE 06", rune:"S-06"},
  7:{name:"Gear Orbit", primary:"gear", secondary:"rings", tertiary:"meteor", particles:7, sigil:"ORBIT 07", rune:"S-07"},
  8:{name:"Solar Veil", primary:"sun", secondary:"beacons", tertiary:"halo", particles:7, sigil:"VEIL 08", rune:"S-08"},
  9:{name:"Singularity Echo", primary:"singularity", secondary:"cross", tertiary:"runes", particles:8, sigil:"ECHO 09", rune:"S-09"},
  10:{name:"First Ascension", primary:"crown", secondary:"rings", tertiary:"beacons", particles:10, sigil:"ASCENT X", rune:"S-10", milestone:10, special:"ascension"},
  11:{name:"Moon Ward", primary:"moon", secondary:"lattice", tertiary:"frame", particles:8, sigil:"WARD 11", rune:"S-11"},
  12:{name:"Fan Spiral", primary:"fan", secondary:"wave", tertiary:"runes", particles:8, sigil:"SPIRAL 12", rune:"S-12"},
  13:{name:"Diamond Lattice", primary:"diamond", secondary:"lattice", tertiary:"halo", particles:9, sigil:"LATTICE 13", rune:"S-13"},
  14:{name:"Reactor Crest", primary:"reactor", secondary:"chevrons", tertiary:"arcs", particles:9, sigil:"CREST 14", rune:"S-14"},
  15:{name:"Portal Cascade", primary:"portal", secondary:"shards", tertiary:"meteor", particles:9, sigil:"CASCADE 15", rune:"S-15"},
  16:{name:"Prism Sanctuary", primary:"prism", secondary:"frame", tertiary:"beacons", particles:10, sigil:"SANCTUARY 16", rune:"S-16"},
  17:{name:"Gear Dominion", primary:"gear", secondary:"wave", tertiary:"runes", particles:10, sigil:"DOMINION 17", rune:"S-17"},
  18:{name:"Solar Spear", primary:"sun", secondary:"chevrons", tertiary:"meteor", particles:10, sigil:"SPEAR 18", rune:"S-18"},
  19:{name:"Void Chorus", primary:"singularity", secondary:"arcs", tertiary:"runes", particles:11, sigil:"CHORUS 19", rune:"S-19"},
  20:{name:"Overdrive Reactor", primary:"reactor", secondary:"beacons", tertiary:"arcs", particles:12, sigil:"OVERDRIVE XX", rune:"S-20", milestone:20, special:"overdrive"},
  21:{name:"Lunar Archive", primary:"moon", secondary:"frame", tertiary:"runes", particles:11, sigil:"ARCHIVE 21", rune:"S-21"},
  22:{name:"Beacon Fan", primary:"fan", secondary:"beacons", tertiary:"lattice", particles:11, sigil:"BEACON 22", rune:"S-22"},
  23:{name:"Royal Current", primary:"crown", secondary:"wave", tertiary:"meteor", particles:12, sigil:"CURRENT 23", rune:"S-23"},
  24:{name:"Hex Citadel", primary:"hex", secondary:"frame", tertiary:"rings", particles:12, sigil:"CITADEL 24", rune:"S-24"},
  25:{name:"Absolute Prism", primary:"prism", secondary:"shards", tertiary:"halo", particles:13, sigil:"ABSOLUTE XXV", rune:"S-25", milestone:25, special:"absolute"},
  26:{name:"Blade Beacon", primary:"blades", secondary:"beacons", tertiary:"chevrons", particles:12, sigil:"BEACON 26", rune:"S-26"},
  27:{name:"Portal Script", primary:"portal", secondary:"runes", tertiary:"arcs", particles:13, sigil:"SCRIPT 27", rune:"S-27"},
  28:{name:"Gear Halo", primary:"gear", secondary:"halo", tertiary:"frame", particles:13, sigil:"HALO 28", rune:"S-28"},
  29:{name:"Void Vault", primary:"singularity", secondary:"frame", tertiary:"beacons", particles:14, sigil:"VAULT 29", rune:"S-29"},
  30:{name:"Dark Dominion", primary:"singularity", secondary:"arcs", tertiary:"beacons", particles:15, sigil:"DOMINION XXX", rune:"S-30", milestone:30, special:"dominion"},
  31:{name:"Solar Lattice", primary:"sun", secondary:"lattice", tertiary:"shards", particles:14, sigil:"LATTICE 31", rune:"S-31"},
  32:{name:"Prism Comet", primary:"prism", secondary:"meteor", tertiary:"beacons", particles:14, sigil:"COMET 32", rune:"S-32"},
  33:{name:"Crown Reliquary", primary:"crown", secondary:"shards", tertiary:"runes", particles:15, sigil:"RELIQUARY 33", rune:"S-33"},
  34:{name:"Moon Gate", primary:"moon", secondary:"arcs", tertiary:"halo", particles:15, sigil:"GATE 34", rune:"S-34"},
  35:{name:"Transcendent Throne", primary:"portal", secondary:"rings", tertiary:"runes", particles:18, sigil:"TRANSCENDENT XXXV", rune:"S-35", milestone:35, special:"transcendent"},
};
function stageDesignSpec(l){
  const visualLevel=l<=35?l:10+((l-36)%26),base=STAGE_ART_LIBRARY[Math.max(0,Math.min(35,visualLevel))]||STAGE_ART_LIBRARY[0];
  const spec={name:base.name,primary:base.primary,secondary:base.secondary,tertiary:base.tertiary,particles:Math.min(22,base.particles+(l>=36?3:0)),sigil:l>=36?`COSMIC • ${String(l).padStart(2,'0')}`:base.sigil,rune:l>=36?`C-${String(l).padStart(2,'0')}`:base.rune,milestone:[10,20,25,30,35,40,50,55].includes(l)?l:(base.milestone||0),special:base.special||'',rings:2+(l%4),orbits:3+(l%3),teeth:6+(l%4),rays:6+(l%6),blades:5+(l%3),fan:4+(l%5),shards:4+(l%5),seed:l+97};
  if(l===40)spec.special='ascension';if(l===50)spec.special='overdrive';if(l===55)spec.special='transcendent';if(spec.milestone){spec.rings=Math.max(spec.rings,4);spec.shards=Math.max(spec.shards,6);}return spec;
}
function renderCardDesign(art,l,d){
  const key=`CORE-${l}`;
  if(art.dataset.designKey===key)return;
  art.dataset.designKey=key;
  art.querySelectorAll('.dynamic-card-design').forEach(e=>e.remove());
  const frag=document.createDocumentFragment();
  const spec=stageDesignSpec(l);
  art.dataset.stageTheme=spec.name;
  art.dataset.special=spec.special||'';
  art.style.setProperty('--design-rotation', `${(spec.seed*17)%360}deg`);
  art.style.setProperty('--design-glow', titleRgba(d?.color||'#a78bfa', .38));
  art.style.setProperty('--design-soft', titleRgba(d?.color||'#a78bfa', .18));

  const add=(cls,style='',text='')=>{
    const e=document.createElement('i');
    e.className='dynamic-card-design '+cls;
    if(style)e.style.cssText=style;
    if(text)e.textContent=text;
    frag.appendChild(e);
    return e;
  };

  const addMain=(name)=>{
    switch(name){
      case 'crown':
        add('design-crown');
        for(let i=0;i<spec.rings;i++) add('design-ring',`--i:${i}`);
        break;
      case 'diamond':
        add('design-diamond');
        add('design-prism-core',`transform:translate(-50%,-50%) translateZ(48px) scale(${1 + (l%3)*.12});`);
        break;
      case 'hex':
        add('design-hex');
        for(let i=0;i<6;i++) add('design-node',`--i:${i}`);
        break;
      case 'reactor':
        add('design-reactor');
        for(let i=0;i<spec.orbits;i++) add('design-orbit',`--i:${i}`);
        break;
      case 'blades':
        for(let i=0;i<spec.blades;i++) add('design-blade',`--i:${i};--blade-count:${spec.blades}`);
        add('design-halo');
        break;
      case 'portal':
        add('design-portal');
        add('design-portal-inner');
        break;
      case 'prism':
        add('design-prism');
        add('design-prism-core');
        break;
      case 'gear':
        add('design-gear');
        for(let i=0;i<spec.teeth;i++) add('design-tooth',`--i:${i};--tooth-count:${spec.teeth}`);
        break;
      case 'sun':
        add('design-sun');
        for(let i=0;i<spec.rays;i++) add('design-ray',`--i:${i};--ray-count:${spec.rays}`);
        break;
      case 'singularity':
        add('design-singularity');
        add('design-singularity-ring');
        break;
      case 'moon':
        add('design-moon');
        add('design-halo');
        break;
      case 'fan':
        add('design-sun',`opacity:.35;transform:translate(-50%,-50%) translateZ(25px) scale(.85)`);
        for(let i=0;i<spec.fan;i++) add('design-fan-blade',`--i:${i};--fan-count:${spec.fan}`);
        break;
    }
  };

  const addAccent=(name)=>{
    switch(name){
      case 'halo': add('design-halo'); break;
      case 'frame': add('design-frame'); break;
      case 'lattice': add('design-lattice'); break;
      case 'wave': add('design-wave'); break;
      case 'chevrons': for(let i=0;i<4;i++) add('design-chevron',`--i:${i}`); break;
      case 'shards': for(let i=0;i<spec.shards;i++) add('design-shard',`--i:${i};--shard-count:${spec.shards}`); break;
      case 'meteor': add('design-comet'); break;
      case 'cross': add('design-cross',`transform:translate(-50%,-50%) rotate(${(l%4)*45}deg) translateZ(20px);`); break;
      case 'rings': for(let i=0;i<Math.max(2,spec.rings-1);i++) add('design-ring',`--i:${i};opacity:${.22 + i*.08}`); break;
      case 'arcs': for(let i=0;i<3;i++) add('design-arc',`--i:${i}`); break;
      case 'runes': add('design-runes','',spec.rune); break;
      case 'beacons': add('design-beacon beacon-left'); add('design-beacon beacon-right'); break;
    }
  };

  const addSpecial=(name)=>{
    switch(name){
      case 'ascension':
        add('design-throne');
        add('design-wing',`--side:-1`); add('design-wing',`--side:1`);
        add('design-radiant-crown');
        break;
      case 'overdrive':
        add('design-helix');
        add('design-over-core');
        for(let i=0;i<4;i++) add('design-arc',`--i:${i};opacity:.95`);
        break;
      case 'absolute':
        add('design-cathedral');
        add('design-cathedral-core');
        add('design-halo',`opacity:.72;transform:translate(-50%,-50%) translateZ(18px) scale(1.15)`);
        break;
      case 'dominion':
        add('design-vortex-gate');
        add('design-abyss-crown');
        add('design-throne',`opacity:.7;transform:translate(-50%,18px) translateZ(26px) scale(1.08)`);
        break;
      case 'transcendent':
        add('design-nova-gate');
        add('design-throne',`opacity:.88;transform:translate(-50%,18px) translateZ(30px) scale(1.16)`);
        add('design-wing',`--side:-1;--wing-scale:1.18`); add('design-wing',`--side:1;--wing-scale:1.18`);
        add('design-starburst');
        break;
    }
  };

  addMain(spec.primary);
  addAccent(spec.secondary);
  addAccent(spec.tertiary);
  if(spec.special) addSpecial(spec.special);
  add('design-sigil','',spec.sigil);
  for(let i=0;i<spec.particles;i++) add('design-particle',`--i:${i};--n:${spec.particles}`);
  art.appendChild(frag);
}

function updateOdorCapsuleVisual(art,l,d){
  if(!art)return;
  const normalized=Math.max(0,Math.min(1,l/MAX_LEVEL));
  const fill=14 + normalized*74;
  const density=.35 + normalized*.65;
  const bubbleScale=.8 + normalized*.9;
  const pulse=1 + normalized*.22;
  art.style.setProperty('--odor-fill', `${fill.toFixed(1)}%`);
  art.style.setProperty('--odor-density', density.toFixed(2));
  art.style.setProperty('--odor-bubble-scale', bubbleScale.toFixed(2));
  art.style.setProperty('--odor-pulse', pulse.toFixed(3));
  art.style.setProperty('--odor-glow', titleRgba(d?.color||'#a78bfa', .62));
  art.style.setProperty('--odor-soft', titleRgba(d?.color||'#a78bfa', .18));
  art.dataset.intensity=l>=45?'omega':l>=30?'high':l>=15?'mid':'low';
}

function titleRgba(hex,alpha){
  const h=String(hex||'#64748b').replace('#','');
  const full=h.length===3?h.split('').map(x=>x+x).join(''):h.padEnd(6,'0').slice(0,6);
  const n=parseInt(full,16);
  const r=(n>>16)&255,g=(n>>8)&255,b=n&255;
  return `rgba(${r},${g},${b},${alpha})`;
}

/* V17.11: EARLY FIRST PAINT
   Run the real renderer before modal/event wiring. This intentionally happens
   much earlier than the legacy hydration block, so a later runtime problem can
   never leave the first screen blank. */
(function hardFirstPaint(){
  try{
    state.runData=normalizeRunData(state.runData);
    unlockReachedWarps(state.runData);
    updateDevModeUI();
    render();
    document.documentElement.dataset.jionFirstPaint='done';
  }catch(err){
    console.error('[JION] hard first paint failed',err);
  }
})();

/* --------------------------- MODALS --------------------------- */
function openModal(kind){
  const m=document.getElementById("modal"),c=document.getElementById("modalContent");
  if(kind==="shop")c.innerHTML=shopHTML();
  else if(kind==="tears")c.innerHTML=tearsHTML();
  else if(kind==="bonuses")c.innerHTML=bonusesHTML();
  else if(kind==="stats")c.innerHTML=statsHTML();
  else return;
  m.classList.remove("hidden","is-closing");
  c.classList.remove("modalContent-enter");
  void c.offsetWidth;
  c.classList.add("modalContent-enter");
  requestAnimationFrame(()=>m.classList.add("is-open"));
  bindModal(kind);
}
function closeModal(){
  const m=document.getElementById("modal");
  if(!m||(!m.classList.contains("is-open")&&m.classList.contains("hidden")))return;
  m.classList.remove("is-open");m.classList.add("is-closing");
  clearTimeout(closeModal._timer);
  closeModal._timer=setTimeout(()=>{m.classList.add("hidden");m.classList.remove("is-closing");},230);
}
function shopHTML(){
  const l=level(),sh=shield(),moneyCost=shieldMoneyCost(l),pointCost=shieldPointCost(l),minShield=20,d=state.runData,warpLevels=[10,20,30,40,45,50],pityNow=pity(),inv=d.auxInventory||{};
  const auxCards=Object.entries(AUX_ITEMS).map(([key,item])=>{const count=Number(inv[key]||0),active=(d.activeEnhanceItem===key)||(key==='perfume'&&d.saleBoost>0)||(key==='tear'&&d.tearBoost>0),moneyPrice=auxMoneyCost(key),pointPrice=auxPointCost(key),rawNow=PROB[String(l)]||[100,0,0,0],pityReady=d.pity_count>=Math.max(1,PITY_MAX-1),noUsefulEffect=(key==='luck'&&(rawNow[0]>=100||pityReady))||(key==='freeze'&&(rawNow[1]<=0||pityReady)),canUse=count>0&&!active&&!noUsefulEffect&&!(key==='gaoh'&&pityReady),useText=item.type==='enhance'?'장착':item.type==='instant'?'즉시 사용':'효과 활성화';return `<article class="aux-item-card ${active?'active':''}"><div class="aux-item-head"><span>${item.icon}</span><div><small>${item.type.toUpperCase()}</small><h4>${item.name}</h4></div><b>x${count}</b></div><p>${item.desc}</p><div class="aux-price-row"><span>💰 ${formatGold(moneyPrice)}</span><span>⭐ ${pointPrice.toLocaleString('ko-KR')}P</span></div><div class="aux-actions"><button class="glass-btn money-buy" data-buy-aux="${key}" data-pay="money" ${(count>=item.max||money()<moneyPrice)?'disabled':''}>돈 구매</button><button class="glass-btn point-buy" data-buy-aux="${key}" data-pay="point" ${(count>=item.max||state.points<pointPrice)?'disabled':''}>P 구매</button><button class="glass-btn aux-use" data-use-aux="${key}" ${canUse?'':'disabled'}>${active?'적용 중':useText}</button>${d.activeEnhanceItem===key?`<button class="glass-btn aux-cancel" data-cancel-aux="${key}">장착 해제</button>`:''}</div></article>`;}).join("");
  const warps=warpLevels.map(w=>{const unlocked=!!d.unlocked_warps[w],passed=l>=w,moneyPrice=warpMoneyCost(w),pointPrice=warpPointCost(w),stateClass=!unlocked?'locked':passed?'passed':'ready',badge=!unlocked?'LOCKED':passed?'PASSED':'READY';return `<div class="warp-card ${stateClass}"><div class="warp-card-top"><div class="warp-target"><span class="warp-icon">${unlocked?'🚀':'🔒'}</span><div><small>TARGET STAGE</small><b>${w}단계 워프</b></div></div><span class="warp-badge">${badge}</span></div><div class="warp-route"><span>현재 +${l}</span><i></i><strong>+${w}</strong></div><div class="warp-costs"><div><small>💰 MONEY</small><b>${formatGold(moneyPrice)}</b></div><div><small>⭐ POINT</small><b>${pointPrice.toLocaleString('ko-KR')}P</b></div></div><div class="warp-note">워프 사용 시 <b>✨ 지온이의 가오가 0으로 초기화</b>됩니다.</div><div class="warp-actions"><button class="glass-btn warp-buy money-buy" data-buy-warp="money" data-warp="${w}" ${(!unlocked||passed||money()<moneyPrice)?'disabled':''}>💰 돈으로 워프</button><button class="glass-btn warp-buy point-buy" data-buy-warp="point" data-warp="${w}" ${(!unlocked||passed||state.points<pointPrice)?'disabled':''}>⭐ 포인트로 워프</button></div></div>`;}).join('');
  return `<div class="modal-head shop shop-hero"><div class="shop-hero-icon">🛒</div><div><h2>지온 상점</h2><p>0~55 강화에 필요한 보호 장비, 보조 아이템과 워프를 구매하세요.</p></div></div><div class="shop-wallet"><div class="wallet-card money"><small>보유 금액</small><b>${formatGold(money())}</b></div><div class="wallet-card point"><small>보유 포인트</small><b>${state.points.toLocaleString('ko-KR')}P</b></div><div class="wallet-card gaoh"><small>현재 지온이의 가오</small><b>${pityNow} / ${Math.max(1,PITY_MAX-1)}</b></div></div><div class="modal-section shop-section shield-section"><div class="section-heading"><div><span>🛡️</span><div><small>PROTECTION</small><h3>파괴 방지권</h3></div></div><b>${sh} / ${SHIELD_MAX}</b></div><p class="section-copy">파괴 결과를 한 번 막아주는 안전장치입니다. ${minShield}단계부터 구매할 수 있습니다.</p><div class="shield-price-grid"><div><small>💰 돈 가격</small><b>${formatGold(moneyCost)}</b></div><div><small>⭐ 포인트 가격</small><b>${pointCost.toLocaleString('ko-KR')}P</b></div></div><div class="warp-actions"><button class="glass-btn money-buy" data-buy-shield="money" ${(l<minShield||sh>=SHIELD_MAX||money()<moneyCost)?'disabled':''}>💰 돈으로 구매</button><button class="glass-btn point-buy" data-buy-shield="point" ${(l<minShield||sh>=SHIELD_MAX||state.points<pointCost)?'disabled':''}>⭐ 포인트로 구매</button></div></div><div class="modal-section shop-section aux-section"><div class="section-heading"><div><span>🧪</span><div><small>BOOST ITEMS</small><h3>강화 보조 아이템</h3></div></div><b>최대 9개</b></div><p class="section-copy">강화 보조 아이템은 장착 후 실제 발동 조건이 나올 때까지 유지됩니다. 원하면 직접 장착 해제할 수 있습니다.</p><div class="aux-item-grid">${auxCards}</div></div><div class="modal-section shop-section warp-section"><div class="section-heading"><div><span>🚀</span><div><small>STAGE WARP</small><h3>워프권</h3></div></div><b>${l}단계</b></div><p class="section-copy">한 번 도달했던 주요 체크포인트로 즉시 이동합니다. 45단계 워프도 포함됩니다.</p><div class="warp-list">${warps}</div></div>`;
}
function tearsHTML(){const l=level(),limit=TEARS_USE_LIMIT;return `<div class="modal-head tear"><h2>💧 눈물</h2><p>눈물 20개를 사용해 1~3단계를 확정적으로 올립니다.</p><p class="tear-limit-notice">⚠️ ${limit}단계부터 지온의 눈물을 사용할 수 없습니다.</p></div><div class="flat-panel"><div style="font-size:11px;color:#94a3b8">보유 눈물</div><div style="font-size:24px;font-weight:900;color:#38bdf8">${tears()} <span style="font-size:13px;color:#94a3b8">/ ${TEARS_MAX}</span></div><div class="modal-meta">사용 조건: <b>20개</b> · 상승 범위: <b>+1 ~ +3</b>${l>=limit?`<br><b class="tear-disabled-copy">현재 ${l}단계 · 사용 불가</b>`:''}</div><button class="glass-btn" id="useTears" ${l>=limit||tears()<20||l>=MAX_LEVEL?'disabled':''}>${l>=limit?`${limit}단계부터 사용 불가`:'눈물 기적 가동'}</button></div>`;}

function statsHTML(){
  const d=state.runData;
  const attempts=Math.max(0,Number(state.enhanceAttempts)||0);
  const successes=Math.max(0,Number(state.enhanceSuccesses)||0);
  const failures=Math.max(0,Number(state.enhanceFailures)||0);
  const destroys=Math.max(0,Number(state.destroyCount)||0);
  const criticals=Math.max(0,Number(state.criticalCount)||0);
  const sells=Math.max(0,Number(state.sellCount)||0);
  const warps=Math.max(0,Number(state.warpUses)||0);
  const bestCombo=Math.max(Number(d.best_combo)||0,Number(d.combo)||0);
  const successRate=attempts?successes/attempts*100:0;
  const failRate=attempts?failures/attempts*100:0;
  const destroyRate=attempts?destroys/attempts*100:0;
  const critRate=successes?criticals/successes*100:0;
  const earned=Math.max(0,Number(state.pointsEarnedTotal)||0);
  const spent=Math.max(0,Number(state.pointsSpentTotal)||0);
  const progress=Math.max(0,Math.min(100,(Number(d.max_level)||0)/MAX_LEVEL*100));
  const fmtPct=v=>`${v.toFixed(v>=10?1:2)}%`;
  const fmtNum=v=>Math.round(Number(v)||0).toLocaleString('ko-KR');
  const finalReached=(Number(d.max_level)||0)>=MAX_LEVEL;
  return `<div class="modal-head stats-head"><div class="stats-head-icon">📈</div><div><h2>플레이 통계</h2><p>현재 세이브의 강화 기록을 한눈에 확인합니다.</p></div></div>
    <div class="stats-hero">
      <div class="stats-stage-ring" style="--stats-progress:${progress.toFixed(1)}%"><div><small>MAX STAGE</small><b>${d.max_level} / ${MAX_LEVEL}</b><span>${finalReached?'FINAL COMPLETE':'진행 '+progress.toFixed(1)+'%'}</span></div></div>
      <div class="stats-hero-copy"><small>CURRENT RUN</small><h3>${level()}단계 · ${DB[String(level())]?.name?.replace(/^\d+단계\s*:\s*/,'')||'지온 캡슐'}</h3><p>현재 콤보 <b>${d.combo||0}</b> · 최고 콤보 <b>${bestCombo}</b> · 보유 금액 <b>${formatGold(money())}</b></p></div>
    </div>
    <div class="stats-section-title"><span>⚙️</span><div><small>ENHANCEMENT</small><b>강화 기록</b></div></div>
    <div class="stats-grid stats-grid-4">
      <article><small>총 강화 시도</small><b>${fmtNum(attempts)}</b></article>
      <article><small>강화 성공</small><b class="stats-good">${fmtNum(successes)}</b><span>${fmtPct(successRate)}</span></article>
      <article><small>실패/유지/파괴</small><b>${fmtNum(failures)}</b><span>${fmtPct(failRate)}</span></article>
      <article><small>파괴 횟수</small><b class="stats-danger">${fmtNum(destroys)}</b><span>${fmtPct(destroyRate)}</span></article>
      <article><small>크리티컬</small><b class="stats-gold">${fmtNum(criticals)}</b><span>성공 중 ${fmtPct(critRate)}</span></article>
      <article><small>최고 콤보</small><b>${fmtNum(bestCombo)}</b><span>현재 ${fmtNum(d.combo||0)}</span></article>
      <article><small>판매 횟수</small><b>${fmtNum(sells)}</b></article>
      <article><small>워프 사용</small><b>${fmtNum(warps)}</b></article>
    </div>
    <div class="stats-section-title"><span>⭐</span><div><small>POINT ECONOMY</small><b>포인트 기록</b></div></div>
    <div class="stats-grid stats-grid-3">
      <article><small>누적 획득</small><b class="stats-gold">${fmtNum(earned)}P</b></article>
      <article><small>누적 사용</small><b>${fmtNum(spent)}P</b></article>
      <article><small>현재 보유</small><b class="stats-good">${fmtNum(state.points)}P</b></article>
    </div>
    `;
}

function bonusesHTML(){
  const d=state.runData,counts=stageBonusCounts(d);
  const rows=MILESTONE_STAGES.map(st=>{
    const chosen=d.stageChoices?.[st],unlocked=d.max_level>=st;
    if(!unlocked)return `<article class="bonus-review locked"><div><small>${st} STAGE</small><h4>🔒 아직 잠김</h4><p>${st}단계에 도달하면 선택할 수 있습니다.</p></div></article>`;
    const current=chosen?STAGE_BONUSES[chosen]:null;
    return `<article class="bonus-review configurable ${chosen?'chosen':'available'}"><div class="bonus-current"><small>${st} STAGE ${chosen?'· CURRENT':'· CHOOSE'}</small><h4>${current?`${current.icon} ${current.name}`:'🎯 보너스를 선택하세요'}</h4><p>${current?current.desc:'아래 세 가지 중 하나를 선택할 수 있습니다. 선택 후에도 언제든 변경할 수 있습니다.'}</p></div><div class="bonus-mini-grid">${Object.entries(STAGE_BONUSES).map(([key,b])=>`<button class="${chosen===key?'active':''}" data-choose-bonus="${key}" data-stage="${st}"><span>${b.icon}</span><b>${b.short}</b><small>${chosen===key?'현재 적용 중':b.desc}</small></button>`).join('')}</div></article>`;
  }).join('');
  return `<div class="modal-head bonus-head"><h2>🎯 단계별 선택 보너스</h2><p>10 / 20 / 30 / 40 / 50단계 슬롯마다 하나를 적용합니다. 잠금 해제 후에는 언제든 다른 보너스로 변경할 수 있습니다.</p></div><div class="bonus-summary"><span>🛡️ 안정 x${counts.stable}</span><span>⚡ 폭주 x${counts.fury}</span><span>💰 장사 x${counts.merchant}</span></div><div class="bonus-review-list">${rows}</div>`;
}

function bindModal(kind){
  document.querySelectorAll("[data-choose-bonus]").forEach(b=>b.onclick=()=>{const st=Number(b.dataset.stage),key=b.dataset.chooseBonus;const before=state.runData.stageChoices?.[st]||null;if(before===key){showToast("이미 적용 중인 보너스입니다.");return;}if(applyStageChoice(st,key)){showToast(`${STAGE_BONUSES[key].icon} ${st}단계 보너스를 ${before?"변경":"선택"}했습니다!`);openModal("bonuses");}});
  document.querySelectorAll("[data-buy-aux]").forEach(b=>b.onclick=()=>{const key=b.dataset.buyAux,pay=b.dataset.pay,item=AUX_ITEMS[key],d=state.runData;if(!item)return;d.auxInventory=d.auxInventory||{};if((d.auxInventory[key]||0)>=item.max){showToast("해당 아이템은 최대 9개까지 보유할 수 있습니다.");return;}const cost=pay==='money'?auxMoneyCost(key):auxPointCost(key);if(pay==='money'){if(money()<cost){showToast("금액이 부족합니다.");return;}setMoney(money()-cost);}else{if(state.points<cost){showToast("포인트가 부족합니다.");return;}state.points-=cost;state.pointsSpentTotal+=cost;}d.auxInventory[key]=(d.auxInventory[key]||0)+1;save();render();openModal("shop");showToast(`${item.icon} ${item.name} 구매 완료!`);});
  document.querySelectorAll("[data-use-aux]").forEach(b=>b.onclick=()=>{const key=b.dataset.useAux,item=AUX_ITEMS[key],d=state.runData;if(!item||!d.auxInventory?.[key])return;if(item.type==='enhance'){if(d.activeEnhanceItem){showToast("이미 강화 보조 아이템이 장착되어 있습니다. 먼저 해제하세요.");return;}d.activeEnhanceItem=key;d.auxInventory[key]--;}else if(item.type==='instant'){const target=Math.max(1,PITY_MAX-1);if(d.pity_count>=target){showToast("이미 지온이의 가오가 최대입니다.");return;}d.auxInventory[key]--;d.pity_count=Math.min(target,d.pity_count+1);}else if(item.type==='sale'){if(d.saleBoost){showToast("상인의 향수가 이미 활성화되어 있습니다.");return;}d.auxInventory[key]--;d.saleBoost=1;}else if(item.type==='tear'){if(d.tearBoost){showToast("눈물 농축액이 이미 활성화되어 있습니다.");return;}d.auxInventory[key]--;d.tearBoost=1;}save();render();openModal("shop");showToast(`${item.icon} ${item.name} ${item.type==='enhance'?'장착':'활성화'} 완료!`);});
  document.querySelectorAll("[data-cancel-aux]").forEach(b=>b.onclick=()=>{const key=b.dataset.cancelAux,d=state.runData;if(d.activeEnhanceItem!==key)return;d.activeEnhanceItem=null;d.auxInventory[key]=(d.auxInventory[key]||0)+1;save();render();openModal("shop");showToast(`${AUX_ITEMS[key].icon} 장착을 해제했습니다.`);});
  document.querySelectorAll("[data-buy-shield]").forEach(b=>b.onclick=()=>{const type=b.dataset.buyShield,l=level(),min=20,cost=type==="money"?shieldMoneyCost(l):shieldPointCost(l);if(l<min||shield()>=SHIELD_MAX){showToast(shield()>=SHIELD_MAX?`방지권은 최대 ${SHIELD_MAX}개까지 보유할 수 있습니다.`:"구매 조건을 만족하지 못했습니다.");return;}if(type==="money"){if(money()<cost){showToast("금액이 부족합니다.");return;}setMoney(money()-cost);}else{if(state.points<cost){showToast("포인트가 부족합니다.");return;}state.points-=cost;state.pointsSpentTotal+=cost;}state.runData.shield++;save();render();openModal("shop");showToast("🛡️ 파괴 방지권 구매 완료!");});
  document.querySelectorAll("[data-buy-warp]").forEach(b=>b.onclick=()=>{
    if(actionLocked)return;
    const type=b.dataset.buyWarp,w=Number(b.dataset.warp),d=state.runData,cost=type==="money"?warpMoneyCost(w):warpPointCost(w);
    if(!d.unlocked_warps[w]||level()>=w){showToast("워프 조건을 만족하지 못했습니다.");return;}
    if(type==="money"&&money()<cost){showToast("금액이 부족합니다.");return;}
    if(type!=="money"&&state.points<cost){showToast("포인트가 부족합니다.");return;}
    closeModal();
    setActionLocked(true);
    playWarpAnimation(w,()=>{
      if(type==="money")setMoney(money()-cost);
      else{state.points-=cost;state.pointsSpentTotal+=cost;}
      state.warpUses++;const prevWarp=d.level;d.prev_level=prevWarp;d.level=w;d.max_level=Math.max(d.max_level,w);d.status="SUCCESS";d.pity_count=0;d.last_aux_effect="";resetCombo(d);d._warpPrev=prevWarp;
      unlockReachedWarps(d);save();render();
      spawnEnhanceBurst('#22d3ee',90,.18,.06,.70,'add');
      setTimeout(()=>spawnEnhanceBurst('#a855f7',70,.15,.055,.65,'add'),100);
    },()=>{
      const prevWarp=Number(d._warpPrev??w);delete d._warpPrev;save();showToast(`🚀 ${w}단계 워프 완료 · ✨ 지온이의 가오 초기화!`);
      runMilestoneOnly(prevWarp,w,()=>setActionLocked(false));
    });
  });
  const tearBtn=document.getElementById("useTears");if(tearBtn)tearBtn.onclick=()=>{
    const d=state.runData,limit=TEARS_USE_LIMIT;if(d.tears<20||d.level>=limit){if(d.level>=limit)showToast(`💧 지온의 눈물은 ${limit}단계부터 사용할 수 없습니다.`);return;}
    d.tears-=20;const boosted=d.tearBoost>0,add=boosted?3:[1,2,3][Math.floor(Math.random()*3)];if(boosted)d.tearBoost=0;
    const prevTear=d.level;d.prev_level=prevTear;d.level=Math.min(MAX_LEVEL,d.level+add);d.status="SUCCESS";d.last_aux_effect=boosted?"💧 농축 눈물 +3":`💧 눈물 +${add}단계`;
    resetCombo(d);d.max_level=Math.max(d.max_level,d.level);
    unlockReachedWarps(d);save();closeModal();setActionLocked(true);syncActionButtons();
    showToast(`💧 눈물 기적! ${add}단계 상승!${boosted?" · 농축액 MAX 효과":""}`);
    pendingParticleOverride=RESULT_PARTICLE_COLORS.TEARS;
    pendingAnimationOverride='TEARS';
    const finishTear=()=>runMilestoneOnly(prevTear,d.level,()=>setActionLocked(false));
    try{
      showTearRoulette(add,()=>{
        try{animateResult(d.status,finishTear);}
        catch(err){console.error('tear result animation failed',err);finishTear();}
      });
    }catch(err){
      console.error('tear roulette failed',err);
      try{animateResult(d.status,finishTear);}
      catch(inner){console.error('tear fallback animation failed',inner);finishTear();}
    }
  };
}
document.getElementById("closeModal").onclick=closeModal;
document.getElementById("modal").addEventListener("click",e=>{if(e.target.id==="modal")closeModal();});
window.addEventListener("keydown",e=>{if(e.key==="Escape")closeModal();});
document.querySelectorAll("[data-modal]").forEach(b=>b.onclick=()=>{if(!actionLocked)openModal(b.dataset.modal);});
const enhanceButton=document.getElementById("enhanceBtn");
(function bindFinalHoldEnhance(){
  if(!enhanceButton)return;
  const HOLD_MS=1500;let holding=false,start=0,raf=0,completed=false;
  const resetHold=(cancelled=false)=>{
    if(raf)cancelAnimationFrame(raf);raf=0;holding=false;start=0;
    enhanceButton.style.setProperty('--final-hold','0');enhanceButton.classList.remove('final-holding','final-hold-complete');
    if(cancelled&&level()===MAX_LEVEL-1&&!actionLocked)showToast('👑 FINAL 강화 취소 · 끝까지 길게 눌러주세요.');
  };
  const beginHold=(e)=>{
    if(level()!==MAX_LEVEL-1||actionLocked||enhanceButton.disabled)return;
    if(e?.pointerType&&e.button!==undefined&&e.button!==0)return;
    e?.preventDefault?.();holding=true;completed=false;start=performance.now();enhanceButton.classList.add('final-holding');
    const tick=(now)=>{
      if(!holding)return;const progress=Math.min(1,(now-start)/HOLD_MS);enhanceButton.style.setProperty('--final-hold',String(progress*100));
      enhanceButton.textContent=progress<1?`👑 FINAL CAPSULE CHARGING ${Math.floor(progress*100)}%`:'⚡ FINAL ASCENSION';
      if(progress>=1){holding=false;completed=true;enhanceButton.classList.add('final-hold-complete');finalHoldAuthorized=true;impactFlash(.38);cardBurst('#fde047',82,190);setTimeout(()=>{resetHold(false);enhance('normal');},90);return;}
      raf=requestAnimationFrame(tick);
    };raf=requestAnimationFrame(tick);
  };
  const cancelHold=()=>{if(!holding)return;resetHold(true);render();};
  enhanceButton.addEventListener('click',e=>{if(level()===MAX_LEVEL-1){e.preventDefault();return;}enhance('normal');});
  enhanceButton.addEventListener('pointerdown',beginHold);enhanceButton.addEventListener('pointerup',cancelHold);enhanceButton.addEventListener('pointercancel',cancelHold);enhanceButton.addEventListener('pointerleave',cancelHold);
  enhanceButton.addEventListener('keydown',e=>{if(level()===MAX_LEVEL-1&&(e.key===' '||e.key==='Enter')&&!e.repeat)beginHold(e);});
  enhanceButton.addEventListener('keyup',e=>{if(level()===MAX_LEVEL-1&&(e.key===' '||e.key==='Enter'))cancelHold();});
  window.addEventListener('blur',()=>{if(holding)resetHold(false);});
})();
document.getElementById("berserkBtn")?.addEventListener("click",()=>enhance("berserk"));
document.getElementById("sellBtn").onclick=sell;

/* --------------------------- Lightweight visual compatibility ---------------------------
   V17.14 QA: the legacy Three.js path had no canvas and was never initialized.
   Keep only tiny compatibility helpers used by older call sites. */
function syncSceneObject(){}
function spawnEnhanceBurst(){ /* CSS/DOM cardBurst is the active particle renderer. */ }

function playWarpAnimation(targetLevel,onShift,onComplete){
  const old=document.getElementById('warpFxOverlay');if(old)old.remove();
  const overlay=document.createElement('div');overlay.id='warpFxOverlay';overlay.className='warp-fx-overlay';
  overlay.innerHTML=`
    <div class="warp-fx-space"></div>
    <div class="warp-fx-streaks">${Array.from({length:24},(_,i)=>`<i style="--i:${i};--a:${i*15}deg"></i>`).join('')}</div>
    <div class="warp-fx-portal">
      <i class="warp-ring r1"></i><i class="warp-ring r2"></i><i class="warp-ring r3"></i><i class="warp-ring r4"></i>
      <div class="warp-core"><small>JION WARP</small><strong>+${targetLevel}</strong><span>DIMENSION SHIFT</span></div>
    </div>
    <div class="warp-fx-flash"></div>`;
  document.body.appendChild(overlay);
  const portal=overlay.querySelector('.warp-fx-portal'),core=overlay.querySelector('.warp-core'),flash=overlay.querySelector('.warp-fx-flash'),streaks=[...overlay.querySelectorAll('.warp-fx-streaks i')],rings=[...overlay.querySelectorAll('.warp-ring')];
  gsap.set(overlay,{opacity:0});gsap.set(portal,{scale:.18,rotation:-28,opacity:0});gsap.set(core,{scale:.55,opacity:0});gsap.set(streaks,{scaleY:.15,opacity:0});
  const tl=gsap.timeline({onComplete:()=>{overlay.remove();if(typeof onComplete==='function')onComplete();}});
  tl.to(overlay,{opacity:1,duration:.14,ease:'power2.out'})
    .to(portal,{scale:1,rotation:0,opacity:1,duration:.34,ease:'back.out(1.8)'},0.04)
    .to(rings,{rotation:'+=240',duration:.72,ease:'power2.inOut',stagger:.035},0.08)
    .to(streaks,{scaleY:1,opacity:.85,duration:.22,ease:'power3.out',stagger:.006},0.10)
    .to(core,{scale:1,opacity:1,duration:.20,ease:'back.out(2)'},0.22)
    .to(portal,{scale:1.42,duration:.20,ease:'power3.in'},0.44)
    .to(flash,{opacity:1,duration:.07,ease:'power4.out',onStart:()=>{if(typeof onShift==='function')onShift();}},0.57)
    .to(flash,{opacity:0,duration:.15,ease:'power2.out'},0.64)
    .to(portal,{scale:3.2,opacity:0,duration:.32,ease:'power4.in'},0.60)
    .to(streaks,{scaleY:2.4,opacity:0,duration:.28,ease:'power2.in'},0.60)
    .to(overlay,{opacity:0,duration:.18,ease:'power2.in'},0.82);
}

function screenShake(power=0.12, duration=.28){
  const target=document.getElementById('threeWrap');
  if(!target||window.matchMedia?.('(prefers-reduced-motion: reduce)').matches)return;
  const px=Math.max(2,Math.min(10,power*24));
  gsap.killTweensOf(target);
  gsap.fromTo(target,{x:-px,y:px*.45},{x:px,y:-px*.45,duration:.038,repeat:Math.max(3,Math.round(duration/.076)),yoyo:true,ease:'none',onComplete:()=>gsap.set(target,{x:0,y:0})});
}
function impactFlash(opacity=.75){
  const flash=document.getElementById('flashOverlay');
  if(!flash)return;
  flash.style.opacity='0';
  gsap.to(flash,{opacity:opacity,duration:.045,ease:'power4.out',yoyo:true,repeat:1,onComplete:()=>flash.style.opacity='0'});
}
/* V17.14 QA: removed unused legacy finalStageCinematic path. */

/* V17.38 — 54→55 unified FINAL cinematic (countdown removed).
   SUCCESS / FAILED / DESTROYED / HOLD / SHIELD_SAVED all use the same
   anticipation, timing, camera motion, particles and impact. Only after the
   final impact do we commit the already-calculated result to the screen. */
function animateFinal54To55(status, afterFinish=null){
  const scene=document.getElementById('enhanceCardScene');
  const card=document.getElementById('enhanceCard');
  const motion=document.getElementById('cardResultMotionLayer')||card;
  const glow=document.getElementById('cardStatusGlow');
  const flash=document.getElementById('flashOverlay');
  const shine=card?.querySelector('.card-shine');
  if(!scene||!card||!motion){animateResult(status,afterFinish);return;}

  document.querySelectorAll('.final-common-cinematic').forEach(e=>e.remove());
  clearResultFx();
  clearDestroySnapshot();
  gsap.killTweensOf([motion,glow,flash,shine]);
  if(typeof window.jionCardTiltSettle==='function')window.jionCardTiltSettle();

  // Remove every prior result tint before the FINAL sequence starts so the
  // animation cannot leak the outcome early.
  scene.classList.remove('status-success','status-critical','status-failed','status-hold','status-destroyed','status-shield','final-success-impact','final-destroy-impact');
  scene.classList.add('final-stage-cinematic','final-common-active');
  card.classList.remove('card-motion-success','card-motion-down','card-motion-destroyed','card-motion-hold','card-motion-critical','card-motion-shield','card-motion-tears');

  const rays=Array.from({length:28},(_,i)=>`<i class="final-common-ray" style="--i:${i}"></i>`).join('');
  const ticks=Array.from({length:36},(_,i)=>`<i class="final-common-tick" style="--i:${i}"></i>`).join('');
  const overlay=document.createElement('div');
  overlay.className='final-common-cinematic';
  overlay.innerHTML=`
    <div class="final-common-vignette"></div>
    <div class="final-common-aurora a1"></div><div class="final-common-aurora a2"></div>
    <div class="final-common-grid"></div>
    <div class="final-common-ray-field">${rays}</div>
    <div class="final-common-gate g1"></div><div class="final-common-gate g2"></div><div class="final-common-gate g3"></div><div class="final-common-gate g4"></div>
    <div class="final-common-ticks">${ticks}</div>
    <div class="final-common-core"></div>
    <div class="final-common-copy">
      <small>JION ODOR // FINAL PROTOCOL</small>
      <b>54 → ?</b>
      <span class="final-common-phase">FINAL CAPSULE LINK</span>
      <em>결과 신호 차단 · 동기화 진행 중</em>
      <div class="final-common-meter"><i></i></div>
    </div>
    <div class="final-common-whiteout"></div>
    <div class="final-common-result-stamp"><b></b><span></span><small>FINAL RESULT</small></div>
  `;
  scene.appendChild(overlay);

  const gates=overlay.querySelectorAll('.final-common-gate');
  const rayEls=overlay.querySelectorAll('.final-common-ray');
  const tickEls=overlay.querySelectorAll('.final-common-tick');
  const core=overlay.querySelector('.final-common-core');
  const copy=overlay.querySelector('.final-common-copy');
  const phase=overlay.querySelector('.final-common-phase');
  const meter=overlay.querySelector('.final-common-meter i');
  const whiteout=overlay.querySelector('.final-common-whiteout');
  const stamp=overlay.querySelector('.final-common-result-stamp');
  const stampTitle=stamp?.querySelector('b');
  const stampSub=stamp?.querySelector('span');

  const meta={
    SUCCESS:['55단계 강화 성공','FINAL ASCENSION COMPLETE','#ffffff'],
    PITY_SUCCESS:['55단계 강화 성공','지온이의 가오 · FINAL ASCENSION','#ffffff'],
    FAILED:['강화 하락',`${state.runData.level}단계로 하락`,'#ffffff'],
    DESTROYED:['캡슐 파괴','0단계로 붕괴','#ffffff'],
    HOLD:['강화 유지','54단계 유지','#ffffff'],
    SHIELD_SAVED:['방지권 발동','파괴 방어 · 54단계 유지','#ffffff'],
    CRITICAL:['55단계 강화 성공','FINAL CRITICAL ASCENSION','#ffffff']
  }[status]||['강화 결과',String(status||'RESULT'),'#ffffff'];

  let committed=false;
  const commitResult=()=>{
    if(committed)return;
    committed=true;
    // This is the first moment the player is allowed to see the outcome.
    render();
    if(stamp){
      stamp.style.setProperty('--final-result-color',meta[2]);
      stamp.classList.add('is-revealed');
    }
    if(stampTitle)stampTitle.textContent=meta[0];
    if(stampSub)stampSub.textContent=meta[1];
    impactFlash(.98);
    screenShake(.56,.42);
    cardBurst('#ffffff',156,330);
  };

  const cleanup=()=>{
    gsap.killTweensOf([motion,overlay,...Array.from(gates),...Array.from(rayEls),...Array.from(tickEls),core,copy,meter,whiteout,stamp]);
    overlay.remove();
    scene.classList.remove('final-stage-cinematic','final-common-active');
    gsap.set(motion,{x:0,y:0,z:0,rotation:0,rotationX:0,rotationY:0,scale:1,opacity:1,filter:'none'});
    if(glow)gsap.set(glow,{x:0,y:0,scale:.82,opacity:.06});
    if(typeof afterFinish==='function')afterFinish();
  };

  gsap.set(motion,{x:0,y:0,z:0,rotation:0,rotationX:0,rotationY:0,scale:1,opacity:1,filter:'none',transformOrigin:'50% 52%'});
  if(glow)gsap.set(glow,{scale:.82,opacity:.08,background:'#ffffff',x:0,y:0});
  if(shine)gsap.set(shine,{x:'-80%'});
  gsap.set(overlay,{opacity:0});
  gsap.set(copy,{opacity:0,y:18,scale:.96});
  gsap.set(gates,{opacity:0,scale:1.58,rotation:-42});
  gsap.set(rayEls,{opacity:0,scaleY:.08});
  gsap.set(tickEls,{opacity:0,scaleY:.12});
  gsap.set(core,{opacity:0,scale:.12});
  gsap.set(meter,{scaleX:0,transformOrigin:'0 50%'});
  gsap.set(whiteout,{opacity:0});
  gsap.set(stamp,{opacity:0,scale:.42,y:18,filter:'blur(12px)'});

  // One shared timeline for every possible FINAL outcome.
  const tl=gsap.timeline({defaults:{overwrite:'auto'},onComplete:cleanup});
  tl.to(overlay,{opacity:1,duration:.18,ease:'power2.out'},0)
    .to(copy,{opacity:1,y:0,scale:1,duration:.40,ease:'power3.out'},.12)
    .to(gates,{opacity:.78,scale:1,rotation:0,duration:.82,stagger:.07,ease:'power3.out'},.08)
    .to(tickEls,{opacity:.72,scaleY:1,duration:.46,stagger:.008,ease:'power2.out'},.20)
    .to(rayEls,{opacity:.34,scaleY:.72,duration:.72,stagger:.012,ease:'power2.out'},.18)
    .to(core,{opacity:.76,scale:1,duration:.68,ease:'back.out(1.8)'},.28)
    .to(motion,{y:-7,scale:1.022,duration:.82,ease:'sine.inOut'},.26)
    .to(meter,{scaleX:1,duration:3.30,ease:'power1.inOut'},.36)
    .add(()=>{phase.textContent='ODOR CORE PRESSURE';cardBurst('#ffffff',28,100);},1.15)
    .to(core,{scale:1.18,opacity:.94,duration:.26,yoyo:true,repeat:1,ease:'sine.inOut'},1.18)
    .to(motion,{y:-12,scale:1.035,duration:.42,ease:'sine.inOut',yoyo:true,repeat:1},1.28)
    .add(()=>{phase.textContent='DIMENSION LOCK';cardBurst('#ffffff',34,125);},2.05)
    .to(gates,{rotation:'+=72',scale:.92,duration:.75,ease:'power1.inOut'},1.90)
    .to(rayEls,{opacity:.58,scaleY:1.02,duration:.64,ease:'power2.inOut'},2.00)
    .add(()=>{phase.textContent='SEAL BREAK SEQUENCE';cardBurst('#ffffff',42,145);},2.78)
    .to(core,{scale:1.34,opacity:1,duration:.34,ease:'sine.inOut',yoyo:true,repeat:1},2.80)
    .to(gates,{scale:.84,duration:.32,ease:'power2.inOut',yoyo:true,repeat:1},2.84)
    .to(rayEls,{opacity:.82,scaleY:1.28,duration:.34,ease:'power2.inOut',yoyo:true,repeat:1},2.90)
    .add(()=>{phase.textContent='FINAL PRESSURE MAX';cardBurst('#ffffff',54,175);},3.38)
    .to(gates,{rotation:'+=150',scale:.70,opacity:1,duration:.54,ease:'power3.in'},3.36)
    .to(rayEls,{opacity:1,scaleY:1.85,duration:.50,ease:'power3.in'},3.40)
    .to(tickEls,{opacity:1,scaleY:1.6,duration:.42,ease:'power3.in'},3.42)
    .to(motion,{y:9,scale:.955,filter:'brightness(.72) saturate(.72)',duration:.25,ease:'power3.in'},3.62)
    .add(()=>{phase.textContent='RESULT SIGNAL LOCKED';},3.66)
    .to(whiteout,{opacity:.96,duration:.13,ease:'power4.in'},3.90)
    .to(core,{scale:.20,opacity:1,duration:.14,ease:'power4.in'},3.90)
    .add(commitResult,4.04)
    .to(motion,{y:-22,scale:1.115,filter:'brightness(1.72) saturate(1.18)',duration:.16,ease:'power4.out'},4.04)
    .to(whiteout,{opacity:0,duration:.24,ease:'power3.out'},4.06)
    .to(stamp,{opacity:1,scale:1,y:0,filter:'blur(0px)',duration:.22,ease:'back.out(2.9)'},4.05)
    .to(gates,{scale:1.34,opacity:.20,duration:.40,ease:'power3.out'},4.06)
    .to(rayEls,{opacity:.12,scaleY:2.35,duration:.42,ease:'power3.out'},4.06)
    .to(motion,{y:0,scale:1,filter:'none',duration:.48,ease:'elastic.out(1,.48)'},4.20)
    .to(stamp,{scale:1.045,duration:.13,yoyo:true,repeat:1,ease:'power2.inOut'},4.42)
    .to(overlay,{opacity:0,duration:.34,ease:'power2.in'},5.08);

  if(glow){
    gsap.to(glow,{scale:1.45,opacity:.28,duration:1.0,ease:'sine.inOut',yoyo:true,repeat:3});
  }
  if(shine){
    gsap.to(shine,{x:'190%',duration:1.05,delay:2.80,ease:'power2.inOut'});
  }
}

function clearResultFx(){
  document.querySelectorAll('.result-fx-layer').forEach(e=>e.remove());
}
function makeResultFx(className, html=''){
  clearResultFx();
  const scene=document.getElementById('enhanceCardScene');
  if(!scene)return null;
  const fx=document.createElement('div');
  fx.className=`result-fx-layer ${className}`;
  fx.innerHTML=html;
  scene.appendChild(fx);
  return fx;
}

const HOLD_STYLE_LABELS={
  SUCCESS:'SUCCESS',
  PITY_SUCCESS:'SUCCESS',
  FAILED:'DOWN',
  DESTROYED:'DESTROYED',
  HOLD:'HOLD',
  CRITICAL:'CRITICAL',
  SHIELD_SAVED:'SHIELD',
  TEARS:'TEARS'
};

function resultFxHoldStyle(label,color,kind='hold'){
  const normalizedKind=String(kind).toLowerCase();
  const rings=Array.from({length:5},(_,i)=>`<div class="hold-ring h${i+1}"></div>`).join('');
  const ticks=Array.from({length:24},(_,i)=>`<i class="hold-tick" style="--i:${i}"></i>`).join('');
  const fx=makeResultFx(`fx-hold fx-unified fx-unified-${normalizedKind}`,
    `<div class="hold-vignette"></div>`+
    `<div class="hold-shock shock-a"></div><div class="hold-shock shock-b"></div>`+
    `<div class="hold-cross cross-x"></div><div class="hold-cross cross-y"></div>`+
    rings+
    `<div class="hold-lock"><b>${label}</b><small>JION SYSTEM</small></div>`+
    ticks
  );
  if(!fx)return null;
  fx.style.setProperty('--fx',color);
  const ringEls=fx.querySelectorAll('.hold-ring');
  const tickEls=fx.querySelectorAll('.hold-tick');
  const lock=fx.querySelector('.hold-lock');
  const shocks=fx.querySelectorAll('.hold-shock');
  const crosses=fx.querySelectorAll('.hold-cross');
  const vignette=fx.querySelector('.hold-vignette');

  gsap.fromTo(fx,{opacity:0},{opacity:1,duration:.035});
  gsap.fromTo(vignette,{opacity:0},{opacity:.72,duration:.09,ease:'power3.out'});
  gsap.fromTo(shocks,
    {scale:.12,opacity:.95},
    {scale:2.15,opacity:0,duration:.48,stagger:.075,ease:'power3.out'}
  );
  gsap.fromTo(ringEls,
    {scale:1.82,rotation:-95,opacity:0},
    {scale:1,rotation:0,opacity:.94,duration:.34,stagger:.028,ease:'back.out(1.95)'}
  );
  gsap.fromTo(crosses,
    {scaleX:.08,opacity:0},
    {scaleX:1,opacity:.88,duration:.16,delay:.075,ease:'power4.out',yoyo:true,repeat:1,repeatDelay:.11}
  );
  gsap.fromTo(lock,
    {scale:.20,opacity:0,filter:'blur(15px)',letterSpacing:'0.36em'},
    {scale:1,opacity:1,filter:'blur(0px)',letterSpacing:'0.16em',duration:.20,delay:.105,ease:'back.out(2.6)'}
  );
  gsap.fromTo(tickEls,
    {opacity:0,scaleY:.12},
    {opacity:1,scaleY:1,duration:.14,stagger:.006,delay:.04,ease:'power3.out'}
  );
  gsap.to(tickEls,{rotation:'+=52',duration:.62,ease:'steps(8)'});
  gsap.to(ringEls,{rotation:'+=22',duration:.7,ease:'none'});
  gsap.to(lock,{scale:1.055,duration:.12,delay:.30,yoyo:true,repeat:1,ease:'power2.inOut'});
  gsap.to(fx,{opacity:0,duration:.22,delay:.86,onComplete:()=>fx.remove()});
  return fx;
}
function resultFxSuccess(color){return resultFxHoldStyle('SUCCESS',color,'success');}
function resultFxDown(color){return resultFxHoldStyle('DOWN',color,'down');}
function resultFxHold(color){return resultFxHoldStyle('HOLD',color,'hold');}
function resultFxCritical(color){return resultFxHoldStyle('CRITICAL',color,'critical');}
function resultFxShield(color){return resultFxHoldStyle('SHIELD',color,'shield');}
function resultFxDestroyed(color){return resultFxHoldStyle('DESTROYED',color,'destroyed');}
function resultFxTears(){return resultFxHoldStyle('TEARS',RESULT_PARTICLE_COLORS.TEARS,'tears');}

function animateResult(status, afterFinish=null){
  const scene=document.getElementById('enhanceCardScene');
  const card=document.getElementById('enhanceCard');
  const wrap=document.getElementById('enhanceCardWrap');
  const motion=document.getElementById('cardResultMotionLayer')||card;
  const glow=document.getElementById('cardStatusGlow');
  const flash=document.getElementById('flashOverlay');
  const shine=card?.querySelector('.card-shine');
  if(!scene||!card||!wrap||!motion){if(typeof afterFinish==='function')afterFinish();return;}

  // Result movement owns one dedicated wrapper. Mouse tilt and high-stage tremor
  // stay on their own layers, preventing competing transform animations.
  gsap.killTweensOf([motion,glow,flash,shine]);
  if(typeof window.jionCardTiltSettle==='function')window.jionCardTiltSettle();
  scene.classList.remove('status-success','status-critical','status-failed','status-hold','status-destroyed','status-shield','final-stage-cinematic','final-success-impact','final-destroy-impact');
  card.classList.remove('card-motion-success','card-motion-down','card-motion-destroyed','card-motion-hold','card-motion-critical','card-motion-shield','card-motion-tears');

  const particleColor=pendingParticleOverride||RESULT_PARTICLE_COLORS[status]||'#ffffff';
  const animationType=pendingAnimationOverride||status;
  pendingParticleOverride=null;
  pendingAnimationOverride=null;
  clearResultFx();

  const visualStatus=animationType==='TEARS'?'TEARS':status;
  if(visualStatus!=='DESTROYED'&&pendingDestroySnapshot)clearDestroySnapshot();
  const label=HOLD_STYLE_LABELS[visualStatus]||String(visualStatus||'RESULT');
  const kind=visualStatus==='PITY_SUCCESS'?'SUCCESS':visualStatus;
  const sceneClass={
    SUCCESS:'status-success',PITY_SUCCESS:'status-success',CRITICAL:'status-critical',
    FAILED:'status-failed',HOLD:'status-hold',DESTROYED:'status-destroyed',SHIELD_SAVED:'status-shield',TEARS:'status-hold'
  }[visualStatus];

  let visualCommitted=false,feedbackShown=false;
  const commitVisual=()=>{
    if(visualCommitted)return;
    visualCommitted=true;
    render();
    if(sceneClass)scene.classList.add(sceneClass);
  };
  const showImpactFeedback=(burstCount=0,burstPower=180,flashAmount=0)=>{
    if(feedbackShown)return;
    feedbackShown=true;
    commitVisual();
    resultFxHoldStyle(label,particleColor,kind);
    feedbackForStatus(status,particleColor);
    if(burstCount)cardBurst(particleColor,burstCount,burstPower);
    if(flashAmount)impactFlash(flashAmount);
  };

  gsap.set(motion,{x:0,y:0,z:0,rotation:0,rotationX:0,rotationY:0,scale:1,opacity:1,filter:'none',transformOrigin:'50% 52%'});
  if(glow)gsap.set(glow,{scale:.82,opacity:.06,background:particleColor,x:0,y:0});
  if(shine)gsap.set(shine,{x:'-70%'});

  const finish=()=>{
    commitVisual();
    gsap.set(motion,{x:0,y:0,z:0,rotation:0,rotationX:0,rotationY:0,scale:1,opacity:1,filter:'none'});
    card.classList.remove('card-motion-success','card-motion-down','card-motion-destroyed','card-motion-hold','card-motion-critical','card-motion-shield','card-motion-tears');
    if(typeof afterFinish==='function')afterFinish();
  };

  // Destruction keeps the pre-result card until the shatter is complete, then
  // commits the 0-stage card exactly at the reboot/reveal beat.
  if(visualStatus==='DESTROYED'){
    card.classList.add('card-motion-destroyed');
    if(sceneClass)scene.classList.add(sceneClass);
    resultFxHoldStyle(label,particleColor,kind);
    feedbackForStatus(status,particleColor);
    playDestroyedCardSequence(card,glow,finish,particleColor,commitVisual);
    return;
  }

  const tl=gsap.timeline({defaults:{overwrite:'auto'},onComplete:finish});

  switch(visualStatus){
    case 'SUCCESS':
    case 'PITY_SUCCESS':
      card.classList.add('card-motion-success');
      // anticipation → impact/update → smooth lift → weighted settle
      tl.to(motion,{y:6,scale:.985,duration:.09,ease:'power2.in'})
        .add(()=>showImpactFeedback(96,220,.22))
        .to(motion,{y:-24,scale:1.055,duration:.20,ease:'power3.out'})
        .to(motion,{y:-5,scale:1.012,duration:.18,ease:'sine.inOut'})
        .to(motion,{y:0,scale:1,duration:.22,ease:'power2.out'});
      if(glow)gsap.to(glow,{scale:1.56,opacity:.40,duration:.20,yoyo:true,repeat:1,ease:'power2.out',delay:.09});
      if(shine)gsap.to(shine,{x:'170%',duration:.46,delay:.11,ease:'power2.out'});
      gsap.delayedCall(.28,()=>cardBurst(particleColor,44,145));
      break;

    case 'FAILED':
      card.classList.add('card-motion-down');
      tl.to(motion,{y:-5,scale:1.012,duration:.08,ease:'power2.out'})
        .add(()=>showImpactFeedback(76,190,.12))
        .to(motion,{y:30,rotation:-1.15,scale:.978,duration:.22,ease:'power3.in'})
        .to(motion,{y:8,rotation:.38,scale:.993,duration:.17,ease:'power2.out'})
        .to(motion,{y:0,rotation:0,scale:1,duration:.22,ease:'power2.out'});
      if(glow)gsap.to(glow,{y:20,scale:1.26,opacity:.31,duration:.21,yoyo:true,repeat:1,delay:.11});
      break;

    case 'HOLD':
      card.classList.add('card-motion-hold');
      tl.to(motion,{scale:.982,y:2,duration:.10,ease:'power2.in'})
        .add(()=>showImpactFeedback(58,145,.08))
        .to(motion,{scale:1.018,y:-2,duration:.14,ease:'power2.out'})
        .to(motion,{scale:1,y:0,duration:.24,ease:'sine.out'});
      if(glow)gsap.to(glow,{scale:1.30,opacity:.26,duration:.18,yoyo:true,repeat:1,delay:.10});
      break;

    case 'CRITICAL':
      card.classList.add('card-motion-critical');
      tl.to(motion,{y:7,scale:.975,rotationX:1.8,duration:.08,ease:'power2.in'})
        .add(()=>showImpactFeedback(128,270,.72))
        .to(motion,{y:-18,z:60,scale:1.115,rotationY:7,rotationX:-3,duration:.18,ease:'power4.out'})
        .to(motion,{y:-6,z:18,scale:1.035,rotationY:-2.2,rotationX:.8,duration:.18,ease:'sine.inOut'})
        .to(motion,{y:0,z:0,scale:1,rotationY:0,rotationX:0,duration:.26,ease:'power2.out'});
      if(glow)gsap.to(glow,{scale:2.0,opacity:.66,duration:.16,yoyo:true,repeat:1,ease:'power3.out',delay:.08});
      if(shine)gsap.to(shine,{x:'190%',duration:.34,delay:.10,ease:'power3.out'});
      gsap.delayedCall(.23,()=>cardBurst('#fff7b2',60,195));
      break;

    case 'SHIELD_SAVED':
      card.classList.add('card-motion-shield');
      tl.to(motion,{y:4,scale:.955,rotationY:-4.5,duration:.11,ease:'power3.in'})
        .add(()=>showImpactFeedback(96,220,.26))
        .to(motion,{y:-9,scale:1.055,rotationY:3,duration:.18,ease:'power3.out'})
        .to(motion,{y:0,scale:1,rotationY:0,duration:.26,ease:'power2.out'});
      if(glow)gsap.to(glow,{scale:1.72,opacity:.52,duration:.18,yoyo:true,repeat:1,delay:.10});
      break;

    case 'TEARS':
      card.classList.add('card-motion-tears');
      tl.to(motion,{y:18,scale:.965,opacity:.78,filter:'brightness(.62) saturate(.62)',duration:.18,ease:'power2.in'})
        .add(()=>showImpactFeedback(96,175,.12))
        .to(motion,{y:-13,scale:1.045,opacity:1,filter:'brightness(1.14) saturate(.92)',duration:.24,ease:'power3.out'})
        .to(motion,{y:0,scale:1,filter:'none',duration:.28,ease:'sine.out'});
      if(glow)gsap.to(glow,{scale:1.55,opacity:.35,duration:.21,yoyo:true,repeat:1,delay:.17});
      break;

    default:
      tl.to(motion,{scale:.985,duration:.09,ease:'power2.in'})
        .add(()=>showImpactFeedback(68,170,.08))
        .to(motion,{scale:1.025,duration:.14,ease:'power2.out'})
        .to(motion,{scale:1,duration:.22,ease:'power2.out'});
  }
}



document.getElementById("resetBtn")?.addEventListener("click",resetGame);


/* V17.14 QA: lean UI re-sync.
   The inline first-paint bootstrap + hardFirstPaint already draw synchronously.
   Keep only one next-frame verification and lifecycle re-syncs. */
function syncGameUI(reason='sync'){
  try{
    state.runData=normalizeRunData(state.runData);
    unlockReachedWarps(state.runData);
    updateDevModeUI();
    render();
  }catch(err){console.error(`[JION] UI sync failed (${reason})`,err);}
}
requestAnimationFrame(()=>syncGameUI('first-frame'));
window.addEventListener('pageshow',()=>syncGameUI('pageshow'));
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')syncGameUI('visible');});

/* V9.1: interactive 3D card tilt. The tilt lives on a separate layer,
   so GSAP can safely animate the card itself without fighting the mouse effect. */
(function setupCard3D(){
  const scene=document.getElementById('enhanceCardScene');
  const layer=document.getElementById('card3dLayer');
  if(!scene||!layer)return;
  let tx=0,ty=0,rx=0,ry=0,raf=0;
  const reset=()=>{tx=0;ty=0;};
  window.jionCardTiltSettle=()=>{tx=0;ty=0;if(!raf)raf=requestAnimationFrame(update);};
  scene.addEventListener('pointermove',e=>{
    if(actionLocked||e.pointerType==='touch'||window.matchMedia?.('(prefers-reduced-motion: reduce)').matches)return;
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
    rx+=(ty* -11-rx)*.14;
    ry+=(tx* 14-ry)*.14;
    const depth=Math.min(26,(Math.abs(rx)+Math.abs(ry))*.85);
    layer.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg) translateZ(${depth}px)`;
    scene.classList.toggle('card-tilting',Math.abs(rx)>0.35||Math.abs(ry)>0.35);
    if(Math.abs(rx)>0.02||Math.abs(ry)>0.02||tx||ty) raf=requestAnimationFrame(update);
  }
  update();
})();


/* =========================================================
   V17.12 — PREMIUM UI MICRO INTERACTIONS
   ========================================================= */
(function initPremiumPolish(){
  const bindButtonFx=(root=document)=>{
    root.querySelectorAll('.glass-btn,.reset-btn').forEach(btn=>{
      if(btn.dataset.premiumFx==='1')return;
      btn.dataset.premiumFx='1';
      btn.addEventListener('pointermove',e=>{
        const r=btn.getBoundingClientRect();
        btn.style.setProperty('--mx',`${e.clientX-r.left}px`);
        btn.style.setProperty('--my',`${e.clientY-r.top}px`);
      },{passive:true});
      btn.addEventListener('pointerleave',()=>{btn.style.removeProperty('--mx');btn.style.removeProperty('--my');},{passive:true});
      btn.addEventListener('pointerdown',e=>{
        if(btn.disabled)return;
        const r=btn.getBoundingClientRect(),rip=document.createElement('span');
        rip.className='btn-ripple';rip.style.left=`${e.clientX-r.left}px`;rip.style.top=`${e.clientY-r.top}px`;
        btn.appendChild(rip);setTimeout(()=>rip.remove(),560);
      },{passive:true});
    });
  };
  bindButtonFx();

  const numericIds=['money','points','tears','pity','shield','combo','cardLevel','cardPrice','cardPoints','cardCost'];
  numericIds.forEach(id=>{
    const el=document.getElementById(id);if(!el)return;
    let prev=el.textContent;
    new MutationObserver(()=>{
      const now=el.textContent;if(now===prev)return;prev=now;
      el.classList.remove('value-pop');void el.offsetWidth;el.classList.add('value-pop');
    }).observe(el,{childList:true,subtree:true,characterData:true});
  });

  const modalContent=document.getElementById('modalContent');
  if(modalContent)new MutationObserver(()=>bindButtonFx(modalContent)).observe(modalContent,{childList:true,subtree:true});

  // Small ambient parallax for the card stage without affecting gameplay animations.
  const stage=document.getElementById('threeWrap');
  if(stage){
    let tx=0,ty=0,raf=0;
    const apply=()=>{raf=0;stage.style.setProperty('--ambient-x',tx.toFixed(2));stage.style.setProperty('--ambient-y',ty.toFixed(2));};
    stage.addEventListener('pointermove',e=>{
      const r=stage.getBoundingClientRect();tx=((e.clientX-r.left)/r.width-.5);ty=((e.clientY-r.top)/r.height-.5);
      if(!raf)raf=requestAnimationFrame(apply);
    },{passive:true});
    stage.addEventListener('pointerleave',()=>{tx=0;ty=0;if(!raf)raf=requestAnimationFrame(apply);},{passive:true});
  }
})();
