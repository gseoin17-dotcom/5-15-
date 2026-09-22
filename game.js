/* 지온냄새 강화하기 V17.68 · GRAPHICS TIERS + LOW MOTION OPTIMIZATION */
const GAME_DATA = {"POINT_REWARD_TABLE":{"1":100,"2":150,"3":200,"4":300,"5":500,"6":700,"7":900,"8":1200,"9":1500,"10":2000,"11":2500,"12":3000,"13":3500,"14":4000,"15":5000,"16":6000,"17":7000,"18":8000,"19":9000,"20":10000,"21":12000,"22":14000,"23":16000,"24":18000,"25":20000,"26":23000,"27":26000,"28":30000,"29":35000,"30":40000,"31":45000,"32":50000,"33":60000,"34":70000,"35":80000,"36":90000,"37":105000,"38":120000,"39":135000,"40":150000,"41":165000,"42":180000,"43":195000,"44":210000,"45":225000,"46":240000,"47":255000,"48":270000,"49":285000,"50":300000,"51":315000,"52":330000,"53":345000,"54":360000,"55":375000,"56":390000,"57":405000,"58":420000,"59":435000,"60":450000},"SMELL_DB":{"0":{"name":"0단계 : 무취 지온의 공간","desc":"아직은 아무 냄새도 안 남. 지온이가 씻었나 봄.","price":0,"color":"#4a5568","tier":1},"1":{"name":"1단계 : 스쳐가는 지온냄새","desc":"버스 옆자리에 앉은 지온이가 팔을 들 때 스치듯 나는 가벼운 암내.","price":500,"color":"#718096","tier":1},"2":{"name":"2단계 : 은은한 지온냄새","desc":"체육 시간이 끝난 뒤 지온이가 벗어던진 축축한 양말 냄새.","price":800,"color":"#38a169","tier":1},"3":{"name":"3단계 : 습한 지온냄새","desc":"사흘 동안 빨지 않은 지온이의 후드티 모자에 쩐내.","price":1200,"color":"#276749","tier":1},"4":{"name":"4단계 : 진득한 지온냄새","desc":"여름철 밀폐된 방 안에서 지온이가 뒹굴다 난 땀에 쩐 이불 냄새.","price":1900,"color":"#319795","tier":1},"5":{"name":"5단계 : 자극적인 지온냄새","desc":"지온이가 발가락을 긁은 손으로 코를 슥 만지게 만드는 향.","price":3000,"color":"#2c7a7b","tier":1},"6":{"name":"6단계 : 풍부한 지온냄새","desc":"신발장에 박아둔 지온이의 축구화 속에서 무르익은 발효 냄새.","price":4100,"color":"#3182ce","tier":2},"7":{"name":"7단계 : 압도적인 지온냄새","desc":"지온이가 다녀간 자리마다 코를 찌르는 시큼털털한 체취의 파도.","price":5700,"color":"#2b6cb0","tier":2},"8":{"name":"8단계 : 폭발하는 지온냄새","desc":"일주일 동안 안 감은 지온이 머리통에서 뿜어져 나오는 유분 폭탄.","price":7900,"color":"#805ad5","tier":2},"9":{"name":"9단계 : 시공을 뒤흔드는 지온냄새","desc":"화장실 문을 열자마자 지온이가 남기고 간 흔적의 생생함.","price":11000,"color":"#6b46c1","tier":2},"10":{"name":"10단계 : 치명적인 지온냄새","desc":"맡는 순간 안구실종을 유발하는 지온이의 살인적인 입냄새.","price":15000,"color":"#d69e2e","tier":2},"11":{"name":"11단계 : 환각을 부르는 지온냄새","desc":"썩은 청국장과 지온이의 발냄새가 콜라보를 이뤄 주마등이 스친다.","price":20000,"color":"#b7791f","tier":3},"12":{"name":"12단계 : 공간지배 지온냄새","desc":"방 문을 열기도 전에 복도까지 마중 나온 지온이의 찌든 내음.","price":26000,"color":"#dd6b20","tier":3},"13":{"name":"13단계 : 전성기 지온냄새","desc":"음식물 쓰레기통을 여름볕에 사흘간 방치한 것과 비견되는 향.","price":34000,"color":"#c05621","tier":3},"14":{"name":"14단계 : 신성한 지온냄새","desc":"너무 지독해서 눈물마저 고이게 만드는 지온이의 꼬릿한 기운.","price":45000,"color":"#e53e3e","tier":3},"15":{"name":"15단계 : 오리지널 지온냄새","desc":"하수구 역류 현상과 지온이의 입김이 만나 온 세상이 오염된다.","price":60000,"color":"#9b2c2c","tier":3},"16":{"name":"16단계 : 우주관통 지온냄새","desc":"대기권을 뚫고 오존층마저 뻥 뚫어버리는 지온이의 겨드랑이 폭풍.","price":76000,"color":"#00f0ff","tier":4},"17":{"name":"17단계 : 차원균열 지온냄새","desc":"지온이의 구린내가 너무 독해서 다른 평행세계의 코까지 썩힌다.","price":97000,"color":"#ff00ea","tier":4},"18":{"name":"18단계 : Absolute 지온냄새","desc":"우주 만물의 원소를 전부 지온이의 체취로 치환해버리는 절대악취.","price":125000,"color":"#ffe600","tier":4},"19":{"name":"19단계 : 초월 지온냄새","desc":"인간의 후각 세포를 단번에 파괴하는 초월적인 썩은 내.","price":155000,"color":"#ff0055","tier":4},"20":{"name":"20단계 : 지온이의 정성이 들어간 포근한 집밥 냄새","desc":"지온맘이 끓여준 묵은지 김치찌개... 인 줄 알았으나 지온이 빨래 냄새.","price":200000,"color":"#ffaa00","tier":4},"21":{"name":"21단계 : 지온이의 엄격한 샤우팅 냄새","desc":"안 씻고 버티는 지온이를 잡으려고 지온맘이 휘두른 등짝의 내음.","price":260000,"color":"#ff4500","tier":5},"22":{"name":"22단계 : 지온이의 전설의 흙된장국 냄새","desc":"지온이의 발냄새 원액을 살짝 타서 깊은 맛을 낸 지온맘의 특제 국물.","price":340000,"color":"#ff007f","tier":5},"23":{"name":"23단계 : 지온이의 100년 숙성 원액 냄새","desc":"지온이가 어릴 때부터 모아둔 꼬릿한 때를 장독대에 묻어 숙성시켰다.","price":440000,"color":"#7b00ff","tier":5},"24":{"name":"24단계 : 지온이의 냄새 탈취 스프레이 냄새","desc":"방 안에 쩔어 있는 지온이의 체취를 탈취제로 잡으려다 역관람당함.","price":575000,"color":"#0088ff","tier":5},"25":{"name":"25단계 : 지온이의 대인배적인 냄새","desc":"이런 지온이라도 품에 안아주는 지온맘의 대인배적 냄새 포용력.","price":750000,"color":"#00ffaa","tier":5},"26":{"name":"26단계 : 지온이의 궁극 필살기 냄새","desc":"지온이 방 문을 강제로 열고 환기시키며 뿜어내는 지온맘의 분노.","price":955000,"color":"#ccff00","tier":6},"27":{"name":"27단계 : 지온이의 창조와 냄새","desc":"지온이의 모든 악취를 정화하려다 지온맘마저 구속당한 경지.","price":1200000,"color":"#fffb00","tier":6},"28":{"name":"28단계 : 지온이의 우주창조설 냄새","desc":"우주 전체가 지온이의 발냄새 아래 무릎을 꿇고 헛구역질을 한다.","price":1550000,"color":"#ffffff","tier":6},"29":{"name":"29단계 : 딥다크 지온냄새","desc":"모든 꼬릿한 냄새의 근원이자, 지온이를 낳고 기른 위대한 악취의 여신.","price":1950000,"color":"#ff00aa","tier":6},"30":{"name":"30단계 : 태초의 지온냄새 ","desc":"우주 탄생 이전부터 존재했던 오리지널 태고의 구린내.","price":2500000,"color":"#00ffff","tier":6},"31":{"name":"31단계 : 하이퍼 지온 싱귤래리티","desc":"냄새가 너무 묵직해서 블랙홀처럼 주변 모든 빛과 산소를 빨아들인다.","price":3150000,"color":"#7000ff","tier":6},"32":{"name":"32단계 : 멀티버스 지온 에센스","desc":"모든 평행우주에 존재하는 지온이의 체취가 한곳으로 모이는 중.","price":4000000,"color":"#ff00e1","tier":6},"33":{"name":"33단계 : 인피니티 지온 페트리코","desc":"영원히 끝나지 않는 지온이의 발효 비린내가 온 은하를 뒤덮음.","price":5000000,"color":"#00ff66","tier":6},"34":{"name":"34단계 : 오메가 지온 제네시스","desc":"지온이의 냄새로 우주를 멸망시키고 다시 창조하는 종말의 향기.","price":6350000,"color":"#ff6600","tier":6},"35":{"name":"35단계 : ★디 오리지널 앱솔루트 지온★","desc":"우주 만물을 통틀어 가장 지독하고 완벽한 궁극의 지온 냄새.","price":8000000,"color":"#ffffff","tier":6},"36":{"name":"36단계 : 안드로메다 자이온 암모니아","desc":"안드로메다 은하 전체를 알칼리화시키는 암모니아 폭풍.","price":10000000,"color":"#00ffff","tier":6},"37":{"name":"37단계 : 화이트홀 자이온 하이드로겐","desc":"우주 백색왜성의 폭발과 함께 뿜어져 나오는 순백의 악취.","price":12500000,"color":"#ffffff","tier":6},"38":{"name":"38단계 : 쿼크 글루온 자이온 악취","desc":"소립자 수준에서부터 강하게 결합되어 떨어지지 않는 쿼크급 냄새.","price":16000000,"color":"#ffaa00","tier":6},"39":{"name":"39단계 : 차원왜곡 자이온 타임루프 찌든내","desc":"시간의 흐름마저 썩어버리게 만드는 과거와 미래의 냄새 집합체.","price":20000000,"color":"#9b2c2c","tier":6},"40":{"name":"40단계 : 네메시스 자이온 다크매터","desc":"빛조차 탈출하지 못하고 악취에 붙잡혀 빨려 들어가는 암흑물질.","price":25000000,"color":"#38a169","tier":6},"41":{"name":"41단계 : 메가 블랙홀 자이온 호라이즌","desc":"모든 물리 법칙이 붕괴하고 오직 자이온이의 체취만 남는 경계선.","price":31500000,"color":"#805ad5","tier":6},"42":{"name":"42단계 : 감마선 버스트 자이온 플레어","desc":"우주 끝까지 수십 광년 동안 일직선으로 뻗어 나가는 살인적 악취.","price":40000000,"color":"#e53e3e","tier":6},"43":{"name":"43단계 : 하이퍼노바 자이온 코어 붕괴","desc":"거대 항성이 생을 마감하며 방출하는 전설적인 폭발성 악취.","price":50000000,"color":"#ff4500","tier":6},"44":{"name":"44단계 : 엘더블루 제네시스 자이온","desc":"태초의 우주가 생성되기도 전에 존재했던 푸른빛의 시원(始源) 냄새.","price":63500000,"color":"#0088ff","tier":6},"45":{"name":"45단계 : 카이퍼 자이온 벨트 코스믹 더스트","desc":"태양계 외곽의 얼어붙은 얼음 조각들에 스며든 미지의 원시 악취.","price":80000000,"color":"#cbd5e1","tier":6},"46":{"name":"46단계 : 자이온오르트 클라우드 딥 프리즈","desc":"영원히 녹지 않을 것 같은 극저온 속에서 서서히 발효된 냉동 체취.","price":105000000,"color":"#319795","tier":6},"47":{"name":"47단계 : 태양풍 플라즈마 자이온제트 스트림","desc":"태양 표면에서 뿜어져 나오는 고온다습한 초고속 플라즈마 냄새.","price":135000000,"color":"#f59e0b","tier":6},"48":{"name":"48단계 : 마그네타 자이온자기장 폭풍","desc":"지구상의 모든 나침반을 고장 내고 정신을 아득하게 만드는 자기장.","price":175000000,"color":"#7000ff","tier":6},"49":{"name":"49단계 : 펄서 자이온로테이션 시그널","desc":"일정한 주기로 우주 전체에 강력한 악취 전파를 송출하는 중성자별.","price":230000000,"color":"#00ff66","tier":6},"50":{"name":"50단계 : 웜홀 크로스오버 자이온 디멘션","desc":"시공간의 통로를 열어 다른 차원의 구린내를 실시간으로 끌어온다.","price":300000000,"color":"#ff00ea","tier":6},"51":{"name":"51단계 : 스트링 시스코어 자이온 엠피리어","desc":"초끈이론의 11차원을 진동시키며 울려 퍼지는 궁극의 우주 진동음.","price":415000000,"color":"#ccff00","tier":6},"52":{"name":"52단계 : 센타우루스 자이온 알파 코어","desc":"가장 가까운 별무리의 기운을 통째로 오염시킨 강력한 은하수 향.","price":570000000,"color":"#ff6600","tier":6},"53":{"name":"53단계 : 페가수스 자이온 별자리 네뷸라","desc":"신화 속 날개 든 말의 질주를 따라 온 하늘에 퍼지는 거대 성운 향.","price":790000000,"color":"#00f0ff","tier":6},"54":{"name":"54단계 : 자이온세인트 오메가 얼티밋 에센스","desc":"우주의 수명이 다하는 순간까지 사라지지 않는 불멸의 성스러운 냄새.","price":1100000000,"color":"#ffe600","tier":6},"55":{"name":"55단계 : 코스믹 인피니티 싱귤자이온래리티","desc":"모든 차원과 우주의 모든 존재가 하나로 응축된 무한대의 악취.","price":1500000000,"color":"#ff00aa","tier":6},"56":{"name":"56단계 : 자이온트랜스센던탈 앱솔루트 가디언","desc":"차원의 벽을 넘어 초월적인 신위(神威)를 뿜어내는 가디언의 경지.","price":2200000000,"color":"#ffffff","tier":6},"57":{"name":"57단계 : 하이퍼 자이온 디바인 코어","desc":"자이온이라는 존재 자체가 우주의 신성한 법칙으로 등용한 상태.","price":3200000000,"color":"#7b00ff","tier":6},"58":{"name":"58단계 : 자이온옴니버스 마스터피스 악취","desc":"모든 평행세계를 통틀어 단 하나만 존재하는 완벽한 걸작 악취.","price":4700000000,"color":"#00ffff","tier":6},"59":{"name":"59단계 : 이터널 제네시스 울티마자이온s","desc":"우주의 탄생과 종말을 영원히 반복하게 만드는 궁극의 고리.","price":6850000000,"color":"#ff4500","tier":6},"60":{"name":"60단계 : ★심플 성지온★","desc":"문일중 3학년 5반의 냄새를 담당하는 그저 GOA.T","price":10000000000,"color":"#ffffff","tier":6}},"PROB_TABLE":{"0":[100.0,0.0,0.0,0.0],"1":[100.0,0.0,0.0,0.0],"2":[100.0,0.0,0.0,0.0],"3":[97.0,3.0,0.0,0.0],"4":[94.0,6.0,0.0,0.0],"5":[91.0,9.0,0.0,0.0],"6":[88.0,10.0,1.0,1.0],"7":[85.0,11.0,3.0,1.0],"8":[82.0,12.0,3.0,3.0],"9":[79.0,13.0,5.0,3.0],"10":[76.0,14.0,7.0,3.0],"11":[73.0,15.0,7.0,5.0],"12":[70.0,16.0,9.0,5.0],"13":[67.0,17.0,11.0,5.0],"14":[64.0,18.0,13.0,5.0],"15":[61.0,19.0,15.0,5.0],"16":[58.0,20.0,17.0,5.0],"17":[55.0,21.0,19.0,5.0],"18":[52.0,22.0,21.0,5.0],"19":[49.0,23.0,23.0,5.0],"20":[46.0,24.0,25.0,5.0],"21":[44.0,25.0,26.0,5.0],"22":[42.0,26.0,27.0,5.0],"23":[40.0,27.0,28.0,5.0],"24":[38.0,28.0,29.0,5.0],"25":[36.0,29.0,30.0,5.0],"26":[34.0,30.0,31.0,5.0],"27":[32.0,31.0,32.0,5.0],"28":[30.0,32.0,33.0,5.0],"29":[28.0,33.0,34.0,5.0],"30":[26.0,34.0,35.0,5.0],"31":[24.0,35.0,36.0,5.0],"32":[22.0,36.0,37.0,5.0],"33":[20.0,37.0,38.0,5.0],"34":[18.0,38.0,39.0,5.0],"35":[17.0,39.0,39.0,5.0],"36":[16.5,39.0,39.5,5.0],"37":[16.0,39.0,40.0,5.0],"38":[15.5,39.0,40.5,5.0],"39":[15.0,39.0,41.0,5.0],"40":[14.5,39.0,41.5,5.0],"41":[14.0,39.0,42.0,5.0],"42":[13.5,39.0,42.5,5.0],"43":[13.0,39.0,43.0,5.0],"44":[12.5,39.0,43.5,5.0],"45":[12.0,39.0,44.0,5.0],"46":[11.5,39.0,44.5,5.0],"47":[11.0,39.0,45.0,5.0],"48":[10.5,39.0,45.5,5.0],"49":[10.0,39.0,46.0,5.0],"50":[9.5,39.0,46.5,5.0],"51":[9.0,39.0,47.0,5.0],"52":[8.5,39.0,47.5,5.0],"53":[8.0,39.0,48.0,5.0],"54":[7.5,39.0,48.5,5.0],"55":[7.0,39.0,49.0,5.0],"56":[6.5,39.0,49.5,5.0],"57":[6.0,39.0,50.0,5.0],"58":[5.5,39.0,50.5,5.0],"59":[5.0,39.0,51.0,5.0]},"CRITICAL_RATE":0.05};

/* V17.49 · MOBILE PERFORMANCE PROFILE
   Keeps desktop visuals intact while reducing GPU/DOM pressure on phones. */
const JION_PERF = (()=>{
  const coarse=window.matchMedia?.('(pointer: coarse)').matches ?? false;
  const narrow=window.matchMedia?.('(max-width: 760px)').matches ?? (window.innerWidth<=760);
  const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches ?? false;
  const memory=Number(navigator.deviceMemory||0);
  const cores=Number(navigator.hardwareConcurrency||0);
  const saveData=!!navigator.connection?.saveData;
  const mobile=coarse||narrow;
  const lowPower=mobile&&(saveData||(memory>0&&memory<=4)||(cores>0&&cores<=4));
  const root=document.documentElement;
  root.classList.toggle('jion-mobile-perf',mobile);
  root.classList.toggle('jion-low-perf',lowPower);
  root.classList.toggle('jion-reduced-motion',reduced);
  return Object.freeze({mobile,lowPower,reduced,coarse,saveData});
})();
function perfCount(desktop,mobile,low){
  const preset=graphicsPreset();
  if(preset==='low')return Math.max(1,low);
  if(preset==='medium')return Math.max(1,mobile);
  return Math.max(1,desktop);
}
document.documentElement.classList.toggle('jion-page-hidden',document.hidden);
document.addEventListener('visibilitychange',()=>document.documentElement.classList.toggle('jion-page-hidden',document.hidden));
/* Runtime safety: if the CDN animation library is unavailable, keep gameplay
   functional with instant visual commits instead of letting enhancement logic crash. */
if(!window.gsap){
  const _targets=t=>Array.isArray(t)?t:(t&&typeof t.length==='number'&&!t.style?[...t]:[t]).filter(Boolean);
  const _apply=(target,vars={})=>{
    for(const el of _targets(target)){
      if(!el||!el.style)continue;
      const transforms=[];
      for(const [k,v] of Object.entries(vars)){
        if(['duration','delay','ease','repeat','yoyo','stagger','overwrite','onComplete','onStart'].includes(k))continue;
        if(k==='opacity')el.style.opacity=String(v);
        else if(k==='filter')el.style.filter=String(v);
        else if(k==='background')el.style.background=String(v);
        else if(k==='x')transforms.push(`translateX(${typeof v==='number'?v+'px':v})`);
        else if(k==='y')transforms.push(`translateY(${typeof v==='number'?v+'px':v})`);
        else if(k==='z')transforms.push(`translateZ(${typeof v==='number'?v+'px':v})`);
        else if(k==='scale')transforms.push(`scale(${v})`);
        else if(k==='scaleX')transforms.push(`scaleX(${v})`);
        else if(k==='scaleY')transforms.push(`scaleY(${v})`);
        else if(k==='rotation')transforms.push(`rotate(${typeof v==='number'?v+'deg':v})`);
        else if(k==='rotationX')transforms.push(`rotateX(${typeof v==='number'?v+'deg':v})`);
        else if(k==='rotationY')transforms.push(`rotateY(${typeof v==='number'?v+'deg':v})`);
        else if(k==='transformOrigin')el.style.transformOrigin=String(v);
      }
      if(transforms.length)el.style.transform=transforms.join(' ');
    }
    try{vars.onStart?.();}catch(e){}
  };
  const _timeline=(opts={})=>{
    const api={
      to(t,v){_apply(t,v);try{v?.onComplete?.();}catch(e){}return api;},
      fromTo(t,a,b){_apply(t,a);_apply(t,b);try{b?.onComplete?.();}catch(e){}return api;},
      set(t,v){_apply(t,v);return api;},
      add(fn){if(typeof fn==='function')fn();return api;}
    };
    queueMicrotask(()=>{try{opts.onComplete?.();}catch(e){}});
    return api;
  };
  window.gsap={
    set:_apply,
    to(t,v){_apply(t,v);setTimeout(()=>{try{v?.onComplete?.();}catch(e){}},0);return {};},
    fromTo(t,a,b){_apply(t,a);_apply(t,b);setTimeout(()=>{try{b?.onComplete?.();}catch(e){}},0);return {};},
    timeline:_timeline,
    delayedCall(_delay,fn){const id=setTimeout(()=>{try{fn?.();}catch(e){}},0);return {kill:()=>clearTimeout(id)};},
    killTweensOf(){},
  };
  document.documentElement.classList.add('jion-no-gsap');
}

const DB = GAME_DATA.SMELL_DB;
const PROB = GAME_DATA.PROB_TABLE;
const CRITICAL_RATE = GAME_DATA.CRITICAL_RATE;
const POINTS = GAME_DATA.POINT_REWARD_TABLE;
const MAX_LEVEL = 55;
const SHIELD_MAX = 6;
const ENHANCE_COST = {"0":20,"1":20,"2":30,"3":50,"4":70,"5":100,"6":150,"7":200,"8":300,"9":400,"10":500,"11":700,"12":900,"13":1200,"14":1600,"15":2100,"16":2800,"17":3700,"18":4700,"19":6100,"20":7900,"21":10500,"22":13500,"23":18000,"24":23500,"25":30500,"26":40500,"27":52000,"28":65000,"29":83000,"30":110000,"31":140000,"32":175000,"33":225000,"34":290000,"35":370000,"36":470000,"37":610000,"38":765000,"39":970000,"40":1250000,"41":1600000,"42":2000000,"43":2550000,"44":3300000,"45":4300000,"46":5600000,"47":7400000,"48":9900000,"49":13000000,"50":18000000,"51":25000000,"52":34000000,"53":47000000,"54":65000000,"55":65000000,"56":65000000,"57":65000000,"58":65000000,"59":65000000,"60":65000000};

const LAB_PART_EQUIP_MAX = 9;
const LEGACY_AUX_TO_RESEARCH = {
  luck:"luckCore",
  freeze:"freezeMatrix",
  volatile:"volatileCore",
  perfume:"recoveryCatalyst",
  tear:"frenzyInjector"
};
const LEGACY_V13_PRICE = {"0":0,"1":150,"2":400,"3":600,"4":800,"5":3000,"6":3500,"7":6100,"8":10000,"9":20000,"10":35100,"11":160000,"12":350000,"13":1000000,"14":3000000,"15":7500000,"16":14200000,"17":20000000,"18":30000000,"19":47500000,"20":68300000,"21":101000000,"22":160000000,"23":230000000,"24":300000000,"25":400000000,"26":1800000000,"27":2500000000,"28":5500000000,"29":10500000000,"30":20000000000,"31":45000000000,"32":90000000000,"33":200000000000,"34":500000000000,"35":1000000000000,"36":2500000000000,"37":6000000000000,"38":15000000000000,"39":35000000000000,"40":80000000000000,"41":180000000000000,"42":400000000000000,"43":900000000000000,"44":2000000000000000,"45":4500000000000000,"46":10000000000000000,"47":22000000000000000,"48":50000000000000000,"49":120000000000000000,"50":280000000000000000,"51":600000000000000000,"52":1300000000000000000,"53":3000000000000000000,"54":7000000000000000000,"55":15000000000000000000,"56":35000000000000000000,"57":80000000000000000000,"58":200000000000000000000,"59":500000000000000000000,"60":1000000000000000000000};
const MILESTONE_STAGES = [];
const STAGE_BONUSES = {};
const RESEARCH_MAX=5;
const RESEARCH_DATA={
  catalyst:{icon:"🧬",slot:"CORE",name:"악취 촉매 코어",desc:"강화 성공 확률을 높이는 고농축 촉매 코어.",effect:"성공 확률",unit:"+0.5%p",cost:[3000,9000,27000,80000,240000]},
  safety:{icon:"🛡️",slot:"ARMOR",name:"안정화 실드 플레이트",desc:"파괴 에너지를 흡수해 일부를 유지 판정으로 전환합니다.",effect:"파괴 확률",unit:"-0.5%p",cost:[2500,7500,22000,65000,195000]},
  economy:{icon:"⚙️",slot:"DRIVE",name:"저전력 압축 터빈",desc:"강화 장치의 에너지 손실을 줄여 강화 비용을 절감합니다.",effect:"강화 비용",unit:"-2%",cost:[2000,6000,18000,54000,162000]},
  insight:{icon:"📡",slot:"SENSOR",name:"냄새 분석 센서",desc:"강화 성공 데이터를 분석해 획득 포인트를 늘립니다.",effect:"성공 포인트",unit:"+4%",cost:[1500,4500,13500,40500,121500]},
  resale:{icon:"💹",slot:"VALVE",name:"회수 증폭 밸브",desc:"캡슐 판매 시 냄새 에너지를 추가 회수해 판매 가격을 높입니다.",effect:"판매 가격",unit:"+3%",cost:[1800,5400,16000,48000,144000]},
  capacitor:{icon:"🔥",slot:"FRENZY",name:"폭주 축전기",desc:"실패 에너지 회수 효율을 높여 냄새 폭주 게이지를 더 빠르게 충전합니다.",effect:"폭주 충전",unit:"+8%",cost:[2200,6600,19800,59400,178000]},
  precision:{icon:"🎯",slot:"OPTIC",name:"정밀 판정 렌즈",desc:"성공 후 크리티컬 판정을 정밀 보정해 크리티컬 확률을 높입니다.",effect:"크리티컬",unit:"+1%p",cost:[2800,8400,25200,75600,226800]},
  shieldTech:{icon:"🔧",slot:"SHIELD",name:"방지권 재생 모듈",desc:"방지권 제작 공정을 개선해 돈·포인트 구매 가격을 낮춥니다.",effect:"방지권 가격",unit:"-4%",cost:[2400,7200,21600,64800,194400]},
  warpTech:{icon:"🌀",slot:"WARP",name:"차원 좌표 보정기",desc:"워프 좌표 계산 효율을 높여 워프 비용을 절감합니다.",effect:"워프 가격",unit:"-3%",cost:[3200,9600,28800,86400,259200]},
  fusion:{icon:"🧪",slot:"FUSION",name:"실험 융합 컨트롤러",desc:"기존 실험 설비를 상시 장착형 파츠 제어기로 개조해 강화비와 판매 효율을 함께 보정합니다.",effect:"융합 효율",unit:"강화비 -1% · 판매 +1%",cost:[2100,6300,18900,56700,170100]},
  luckCore:{icon:"🍀",slot:"LUCK",name:"확률 촉매 코어",desc:"기존 확률 촉매 앰플을 영구 파츠로 통합. 장착 중 강화 성공 확률이 상승합니다.",effect:"성공 확률",unit:"+0.6%p",cost:[3500,10500,31500,94500,283500]},
  freezeMatrix:{icon:"🧊",slot:"STABLE",name:"단계 안정 매트릭스",desc:"기존 단계 안정제를 영구 파츠로 통합. 하락 확률 일부를 유지 확률로 바꿉니다.",effect:"하락 방어",unit:"8% 변환",cost:[3200,9600,28800,86400,259200]},
  volatileCore:{icon:"💣",slot:"OUTPUT",name:"고출력 변이 코어",desc:"기존 변이 코어를 영구 파츠로 통합. 성공 시 일정 확률로 +1단계를 추가 획득합니다.",effect:"추가 상승",unit:"+4% 확률",cost:[4500,13500,40500,121500,364500]},
  recoveryCatalyst:{icon:"💰",slot:"RECYCLE",name:"회수 촉매 모듈",desc:"기존 회수 촉매를 영구 파츠로 통합. 판매 회수율을 추가로 높입니다.",effect:"판매 가격",unit:"+4%",cost:[2600,7800,23400,70200,210600]},
  frenzyInjector:{icon:"🔥",slot:"INJECT",name:"폭주 촉진 인젝터",desc:"기존 폭주 촉진제를 영구 파츠로 통합. 실패 계열 판정의 폭주 충전량을 늘립니다.",effect:"폭주 충전",unit:"+7%",cost:[3000,9000,27000,81000,243000]}
};
const FRENZY_MAX=100;
const FRENZY_EVENT_TYPES=['surge','success','guard','free','points','critical'];
function emptyStageChoices(){return {};}
function emptyResearch(){return Object.fromEntries(Object.keys(RESEARCH_DATA).map(key=>[key,0]));}
function normalizeUiSettings(input){
  const allowed=['high','medium','low'];
  return {
    graphics: allowed.includes(input?.graphics)?input.graphics:'high',
    motion: allowed.includes(input?.motion)?input.motion:'high'
  };
}

const INITIAL = {
  schemaVersion:26,
  enhanceAttempts:0,warpUses:0,sellCount:0,finalClears:0,frenzyTriggers:0,
  points:0,lastPointReward:0,pointsEarnedTotal:0,pointsSpentTotal:0,
  enhanceSuccesses:0,enhanceFailures:0,criticalCount:0,destroyCount:0,
  uiSettings:normalizeUiSettings({graphics:'high',motion:'high'}),
  runData:{level:0,prev_level:0,max_level:0,money:"50000",status:"READY",shield:0,reviveTickets:0,combo:0,best_combo:0,last_aux_effect:"",stageChoices:emptyStageChoices(),research:emptyResearch(),equippedParts:[],frenzyGauge:0,frenzyEvent:null,
    unlocked_warps:{10:false,20:false,30:false,40:false,45:false,50:false}}
};

let state = loadState();
applyUserQualitySettings();
let toastTimer = null;
let actionLocked = false;
let currentGameView = "enhance";
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
  const out={luck:0,freeze:0,volatile:0,perfume:0,tear:0};
  for(const k of Object.keys(out)) out[k]=Math.min(9,Math.max(0,Number(a?.[k]||0)+Number(b?.[k]||0)));
  return out;
}
function normalizeRunData(d){
  const hadExplicitEquipped=Array.isArray(d?.equippedParts);
  const legacyAux=Object.assign({luck:0,freeze:0,volatile:0,perfume:0,tear:0},d?.auxInventory||{});
  if(d?.activeEnhanceItem&&Object.prototype.hasOwnProperty.call(legacyAux,d.activeEnhanceItem)) legacyAux[d.activeEnhanceItem]=(Number(legacyAux[d.activeEnhanceItem])||0)+1;
  if(Number(d?.saleBoost)||0) legacyAux.perfume=(Number(legacyAux.perfume)||0)+1;

  const out=Object.assign(clone(INITIAL.runData),d||{});
  out.money=toMoneyInt(out.money).toString();
  out.unlocked_warps=Object.assign(clone(INITIAL.runData.unlocked_warps),out.unlocked_warps||{});
  out.level=Math.max(0,Math.min(MAX_LEVEL,Number(out.level)||0)); out.prev_level=Math.max(0,Math.min(MAX_LEVEL,Number(out.prev_level)||0));
  out.max_level=Math.max(out.level,Math.min(MAX_LEVEL,Number(out.max_level)||0)); for(const w of [10,20,30,40,45,50]) if(out.max_level>=w||out.level>=w) out.unlocked_warps[w]=true; out.shield=Math.max(0,Math.min(SHIELD_MAX,Number(out.shield)||0));
  delete out.tears; delete out.pity_count; delete out.feverFree;
  out.combo=Math.max(0,Number(out.combo)||0); out.best_combo=Math.max(out.combo,Number(out.best_combo)||0);
  if(out.status==='PITY_SUCCESS')out.status='SUCCESS';
  out.stageChoices=emptyStageChoices();

  out.research=Object.assign(emptyResearch(),out.research||{});
  if(Number(out.research.auxlab)>0) out.research.fusion=Math.max(Number(out.research.fusion)||0,Number(out.research.auxlab)||0);
  delete out.research.auxlab;
  for(const [legacyKey,newKey] of Object.entries(LEGACY_AUX_TO_RESEARCH)){
    const count=Math.max(0,Number(legacyAux[legacyKey])||0);
    if(count>0) out.research[newKey]=Math.max(Number(out.research[newKey])||0,Math.min(RESEARCH_MAX,Math.ceil(count/2)));
  }
  for(const key of Object.keys(RESEARCH_DATA)) out.research[key]=Math.max(0,Math.min(RESEARCH_MAX,Number(out.research[key])||0));
  for(const key of Object.keys(out.research)) if(!RESEARCH_DATA[key]) delete out.research[key];

  const validOwned=Object.keys(RESEARCH_DATA).filter(key=>out.research[key]>0);
  const requested=hadExplicitEquipped?d.equippedParts:validOwned;
  out.equippedParts=[...new Set((requested||[]).filter(key=>RESEARCH_DATA[key]&&out.research[key]>0))].slice(0,LAB_PART_EQUIP_MAX);

  out.frenzyGauge=Math.max(0,Math.min(FRENZY_MAX,Number(out.frenzyGauge)||0));
  const ev=out.frenzyEvent;if(!ev||!FRENZY_EVENT_TYPES.includes(ev.type)||Number(ev.turns||0)<=0)out.frenzyEvent=null;else out.frenzyEvent={type:ev.type,turns:Math.max(1,Math.min(6,Number(ev.turns)||1)),label:String(ev.label||''),desc:String(ev.desc||'')};
  delete out.pendingFinalEnding;
  delete out.frenzyTurns;
  delete out.randomEvent;
  delete out.auxInventory;
  delete out.activeEnhanceItem;
  delete out.saleBoost;
  delete out.tearBoost;
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
  if(s.runData){delete s.runData.pity_count;delete s.runData.feverFree;}
  return s;
}
function loadState(){
  try{
    const saved=JSON.parse(localStorage.getItem("jion_smell_game_v3"));
    if(!saved)return clone(INITIAL);
    if(saved.schemaVersion>=15&&saved.runData){
      const s=Object.assign(clone(INITIAL),saved);s.runData=normalizeRunData(saved.runData);s.uiSettings=normalizeUiSettings(saved.uiSettings);s.schemaVersion=26;
      return cleanRemovedSystems(s);
    }
    if(saved.schemaVersion>=13&&saved.runData){
      const s=Object.assign(clone(INITIAL),saved);s.runData=normalizeRunData(saved.runData);s.uiSettings=normalizeUiSettings(saved.uiSettings);
      if(saved.schemaVersion<14)s.runData.money=scaleLegacyMoney(saved.runData.money,s.runData.max_level||s.runData.level).toString();
      s.schemaVersion=26;return cleanRemovedSystems(s);
    }
    const s=Object.assign(clone(INITIAL),saved),a=(saved.seasonData||{})[1]||{},b=(saved.seasonData||{})[2]||{};
    const bMax=Math.max(0,Number(b.max_level)||0),bLevel=Math.max(0,Number(b.level)||0),hadSecond=Number(saved.rebirthCount)>0||bMax>0||bLevel>0||Number(saved.currentSeason)===2;
    const maxUnified=Math.min(MAX_LEVEL,Math.max(Number(a.max_level)||0,hadSecond?35+bMax:0)),currentUnified=Math.min(MAX_LEVEL,Number(saved.currentSeason)===2?35+bLevel:(Number(a.level)||0)),src=Number(saved.currentSeason)===2?b:a;
    const legacyAux=mergeInventory(a.auxInventory,b.auxInventory);
    s.runData=normalizeRunData(Object.assign({},src,{level:currentUnified,prev_level:currentUnified,max_level:maxUnified,auxInventory:legacyAux}));
    const oldCombined=toMoneyInt(a.money||0)+toMoneyInt(b.money||0);s.runData.money=scaleLegacyMoney(oldCombined,maxUnified||currentUnified).toString();s.runData.shield=Math.min(SHIELD_MAX,(Number(a.shield)||0)+(Number(b.shield)||0));s.runData.unlocked_warps=clone(INITIAL.runData.unlocked_warps);for(const w of [10,20,30,40,45,50])if(maxUnified>=w)s.runData.unlocked_warps[w]=true;
    s.uiSettings=normalizeUiSettings(saved.uiSettings);
    s.schemaVersion=26;return cleanRemovedSystems(s);
  }catch(e){return clone(INITIAL);}
}
function save(){ localStorage.setItem("jion_smell_game_v3",JSON.stringify(state)); }
function graphicsPreset(){ return normalizeUiSettings(state?.uiSettings).graphics; }
function motionPreset(){ return normalizeUiSettings(state?.uiSettings).motion; }
function applyUserQualitySettings(){
  const root=document.documentElement;
  const {graphics,motion}=normalizeUiSettings(state?.uiSettings);
  root.classList.remove('jion-graphics-high','jion-graphics-medium','jion-graphics-low','jion-motion-high','jion-motion-medium','jion-motion-low');
  root.classList.add('jion-graphics-'+graphics,'jion-motion-'+motion);
}
function updateUiSetting(group,value){
  state.uiSettings=normalizeUiSettings(Object.assign({},state.uiSettings,{[group]:value}));
  save();
  applyUserQualitySettings();
}
function level(){ return state.runData.level; }
function data(){ return DB[String(level())]||DB["0"]; }
function maxLevel(){ return MAX_LEVEL; }
function money(){ return toMoneyInt(state.runData.money); }
function setMoney(v){ state.runData.money=toMoneyInt(v).toString(); }
function shield(){ return state.runData.shield; }
function combo(){ return state.runData.combo||0; }
function comboMultiplier(v=combo()){
  const c=Math.max(0,Number(v)||0);
  if(c>=15)return 3;
  if(c>=10)return 2.25;
  if(c>=7)return 1.75;
  if(c>=5)return 1.5;
  if(c>=3)return 1.25;
  if(c>=2)return 1.1;
  return 1;
}
function comboSuccessBoost(v=combo()){const c=Math.max(0,Number(v)||0);return c>=15?5:c>=7?2:0;}
function comboCriticalBoost(v=combo()){const c=Math.max(0,Number(v)||0);return c>=15?.10:c>=10?.06:c>=5?.03:0;}
function comboCostDiscount(v=combo()){const c=Math.max(0,Number(v)||0);return c>=15?15:c>=10?10:c>=5?5:0;}
function comboDestroyProtection(v=combo(), destroyChance=null){
  const c=Math.max(0,Number(v)||0);
  const reduction=c>=15?8:c>=10?5:0;
  if(destroyChance===null||destroyChance===undefined)return reduction;
  return Math.min(Math.max(0,Number(destroyChance)||0),reduction);
}
function comboTierMeta(v=combo()){
  const c=Math.max(0,Number(v)||0);
  if(c>=15)return {name:'MAX FEVER',next:null,from:15,to:15};
  if(c>=10)return {name:'OVER FEVER',next:15,from:10,to:15};
  if(c>=7)return {name:'HOT STREAK',next:10,from:7,to:10};
  if(c>=5)return {name:'FEVER',next:7,from:5,to:7};
  if(c>=3)return {name:'CHAIN',next:5,from:3,to:5};
  if(c>=2)return {name:'WARM UP',next:3,from:2,to:3};
  return {name:'READY',next:2,from:0,to:2};
}
function comboEffectText(v=combo()){
  const c=Math.max(0,Number(v)||0),parts=[];
  const mult=comboMultiplier(c);if(mult>1)parts.push(`포인트 x${Number.isInteger(mult)?mult:mult.toFixed(2).replace(/0$/,'')}`);
  const success=comboSuccessBoost(c);if(success)parts.push(`성공 +${success}%p`);
  const crit=comboCriticalBoost(c);if(crit)parts.push(`크리티컬 +${Math.round(crit*100)}%p`);
  const cost=comboCostDiscount(c);if(cost)parts.push(`비용 -${cost}%`);
  const guard=comboDestroyProtection(c);if(guard)parts.push(`파괴 -${guard}%p`);
  return parts.join(' · ')||'성공을 이어가면 콤보 보너스가 해금됩니다';
}
function stageBonusCounts(){return {stable:0,fury:0,merchant:0};}
function researchLevel(key,d=state.runData){return Math.max(0,Math.min(RESEARCH_MAX,Number(d.research?.[key])||0));}
function isResearchEquipped(key,d=state.runData){return researchLevel(key,d)>0&&Array.isArray(d.equippedParts)&&d.equippedParts.includes(key);}
function activeResearchLevel(key,d=state.runData){return isResearchEquipped(key,d)?researchLevel(key,d):0;}
function equippedPartCount(d=state.runData){return Array.isArray(d.equippedParts)?d.equippedParts.filter(key=>RESEARCH_DATA[key]&&researchLevel(key,d)>0).length:0;}
function researchCost(key,d=state.runData){const lv=researchLevel(key,d),cfg=RESEARCH_DATA[key];return (!cfg||lv>=RESEARCH_MAX)?null:Number(cfg.cost[lv]||0);}
function currentFrenzyEvent(d=state.runData){const ev=d.frenzyEvent;return ev&&FRENZY_EVENT_TYPES.includes(ev.type)&&Number(ev.turns||0)>0?ev:null;}
function frenzyActive(d=state.runData){return !!currentFrenzyEvent(d);}
function frenzyEventIs(type,d=state.runData){return currentFrenzyEvent(d)?.type===type;}
function stagePointMultiplier(d=state.runData){return (1+activeResearchLevel('insight',d)*.04)*(frenzyEventIs('points',d)?2:1);}
function stageSellPercent(d=state.runData){return 100+activeResearchLevel('resale',d)*3+activeResearchLevel('recoveryCatalyst',d)*4+activeResearchLevel('fusion',d);}
function criticalRateFor(d=state.runData,lvl=level()){
  if(Number(lvl)>=50)return 0;
  let r=CRITICAL_RATE+activeResearchLevel('precision',d)*.01;
  r+=comboCriticalBoost(d.combo||0);
  if(frenzyEventIs('critical',d))r+=.10;
  return Math.min(.50,r);
}
function resetCombo(d=state.runData){ d.combo=0; }
function baseEnhanceCost(lvl){ return toMoneyInt(ENHANCE_COST[Number(lvl)] ?? ENHANCE_COST[55]); }
function enhanceCost(lvl){ return baseEnhanceCost(lvl); }
function effectiveEnhanceCost(mode="normal",d=state.runData){
  if(frenzyEventIs('free',d)) return 0n;
  let cost=enhanceCost(d.level);
  const comboDiscount=comboCostDiscount(d.combo||0);if(comboDiscount>0)cost=cost*BigInt(100-comboDiscount)/100n;
  if(mode==='berserk') cost*=2n;
  const economy=Math.max(0,100-activeResearchLevel('economy',d)*2-activeResearchLevel('fusion',d));
  cost=(cost*BigInt(economy)+99n)/100n;
  return cost;
}
function pointReward(lvl){ if(lvl<=0)return 0; return Number(POINTS[String(lvl)]??(90000+(lvl-36)*15000)); }
function dbPrice(a,b){ const lvl=b===undefined?Number(a):Number(b); return toMoneyInt(DB[String(lvl)]?.price||0); }
function researchDiscountPercent(key,perLevel,d=state.runData){return Math.max(0,100-activeResearchLevel(key,d)*perLevel);}
function warpPointCost(lvl){ return Math.max(1,Math.round(pointReward(lvl)*19.5*researchDiscountPercent('warpTech',3)/100)); }
function warpMoneyCost(lvl){ return dbPrice(lvl)*BigInt(researchDiscountPercent('warpTech',3))/100n; }
function shieldPointCost(lvl){ return Math.max(1,Math.round(pointReward(lvl)*1.5*researchDiscountPercent('shieldTech',4)/100)); }
function shieldMoneyCost(lvl){ const scaled=(baseEnhanceCost(lvl)*75n+99n)/100n,base=scaled>10000n?scaled:10000n;return base*BigInt(researchDiscountPercent('shieldTech',4))/100n; }
function finalBalanceProbabilities(base,lvl=level()){
  return base.map(Number);
}
function effectiveProbabilities(base,opts={}){
  const d=opts.data||state.runData;
  let [success,down,destroy,hold]=finalBalanceProbabilities(base,opts.level ?? level());
  const shiftToSuccess=(amount)=>{let add=Math.min(amount,100-success);success+=add;for(const name of ['destroy','down','hold']){if(add<=0)break;const cur=name==='destroy'?destroy:name==='down'?down:hold,used=Math.min(cur,add);add-=used;if(name==='destroy')destroy-=used;else if(name==='down')down-=used;else hold-=used;}};
  shiftToSuccess(activeResearchLevel('catalyst',d)*.5);
  shiftToSuccess(activeResearchLevel('luckCore',d)*.6);
  const freezeRate=activeResearchLevel('freezeMatrix',d)*.08;if(freezeRate>0&&down>0){const moved=down*freezeRate;down-=moved;hold+=moved;}
  const safety=activeResearchLevel('safety',d)*.5;if(safety>0){const moved=Math.min(destroy,safety);destroy-=moved;hold+=moved;}
  if(opts.mode!=='berserk'){
    const comboSuccess=comboSuccessBoost(opts.combo ?? d.combo ?? combo());if(comboSuccess>0)shiftToSuccess(comboSuccess);
    const comboGuard = comboDestroyProtection(opts.combo ?? d.combo ?? combo());
    if(comboGuard>0){const moved=Math.min(destroy,comboGuard);destroy-=moved;hold+=moved;}
  }
  if(frenzyEventIs('success',d))shiftToSuccess(10);
  if(frenzyEventIs('guard',d)){const moved=Math.min(destroy,8);destroy-=moved;hold+=moved;}
  if(opts.mode==='berserk'){success=Math.max(1,success-10);destroy=100-success;down=0;hold=0;}
  return [success,down,destroy,hold].map(v=>Math.round(v*10)/10);
}

function activateRandomFrenzyEvent(d=state.runData){
  // FINAL 54→55는 반드시 전용 FINAL 강화로만 진입한다.
  const pool=d.level>=MAX_LEVEL-1?FRENZY_EVENT_TYPES.filter(v=>v!=='surge'):FRENZY_EVENT_TYPES;
  const type=pool[Math.floor(Math.random()*pool.length)];
  state.frenzyTriggers=Math.max(0,Number(state.frenzyTriggers)||0)+1;
  if(type==='surge'){
    const add=1+Math.floor(Math.random()*3),before=d.level;
    d.level=Math.min(MAX_LEVEL-1,d.level+add);d.max_level=Math.max(d.max_level,d.level);unlockReachedWarps(d);
    return {type,label:`🚀 폭주 도약 +${d.level-before}`,desc:`냄새 에너지가 폭발해 즉시 ${d.level-before}단계 상승했습니다.`,instant:true};
  }
  const cfg={
    success:{turns:3,label:'🎯 확률 과충전',desc:'강화 성공 확률 +10%p'},
    guard:{turns:3,label:'🛡️ 안정장 폭주',desc:'일반 강화 파괴 확률 -8%p'},
    free:{turns:2,label:'⚡ 무상 출력',desc:'강화 비용 0원'},
    points:{turns:3,label:'⭐ 데이터 폭증',desc:'성공 포인트 x2'},
    critical:{turns:3,label:'💥 임계 공명',desc:'크리티컬 확률 +10%p'}
  }[type];
  d.frenzyEvent={type,turns:cfg.turns,label:cfg.label,desc:cfg.desc};
  return {type,label:cfg.label,desc:cfg.desc,turns:cfg.turns,instant:false};
}
function consumeFrenzyEventTurn(previousEvent,d=state.runData){
  if(!previousEvent||!d.frenzyEvent||d.frenzyEvent.type!==previousEvent.type)return;
  d.frenzyEvent.turns=Math.max(0,Number(d.frenzyEvent.turns||0)-1);
  if(d.frenzyEvent.turns<=0)d.frenzyEvent=null;
}
function addFrenzyCharge(amount,d=state.runData){
  if(amount<=0)return null;
  d.frenzyGauge=Math.min(FRENZY_MAX,(Number(d.frenzyGauge)||0)+amount);
  if(d.frenzyGauge>=FRENZY_MAX&&!currentFrenzyEvent(d)){
    d.frenzyGauge=0;
    return activateRandomFrenzyEvent(d);
  }
  return null;
}
function updateFrenzyAfterEnhance(status,previousEvent,d=state.runData){
  consumeFrenzyEventTurn(previousEvent,d);
  if(Number(d.frenzyGauge||0)>=FRENZY_MAX&&!currentFrenzyEvent(d)){d.frenzyGauge=0;return activateRandomFrenzyEvent(d);}
  const gainMap={HOLD:25,FAILED:30,SHIELD_SAVED:38,DESTROYED:50};
  const baseGain=gainMap[status]||0;
  const chargeMult=1+activeResearchLevel('capacitor',d)*.08+activeResearchLevel('frenzyInjector',d)*.07;
  const gain=baseGain>0?Math.max(1,Math.round(baseGain*chargeMult)):0;
  return addFrenzyCharge(gain,d);
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
    const available=l>=20&&l<=48;
    bb.disabled=actionLocked||!available;
    bb.textContent=l<20?'☠️ 광폭 강화 · 20단계 해금':l>48?'☠️ 광폭 강화 · 20~48단계 전용':`☠️ 광폭 강화 · ${formatGold(effectiveEnhanceCost('berserk'))}`;
  }
  const bi=document.getElementById('berserkInfo');
  if(bi){
    bi.classList.remove('hidden');
    if(l<20) bi.textContent='20단계부터 사용 가능 · 성공 시 +2~6단계 랜덤 상승';
    else if(l>48) bi.textContent='20~48단계에서만 사용 가능 · 성공 시 +2~6단계 랜덤 상승';
    else{
      const raw=PROB[String(l)]||[8,40,47,5];
      const bp=effectiveProbabilities(raw,{mode:'berserk'});
      bi.innerHTML=`<b class="berserk-success-rate">성공 ${bp[0]}%</b> · <b class="berserk-destroy-rate">파괴 ${bp[2]}%</b> · 성공 시 <strong>+2~6단계 랜덤 상승</strong>`;
    }
  }
  document.querySelectorAll("[data-modal]").forEach(b=>b.disabled=actionLocked);
  document.querySelectorAll("[data-game-view]").forEach(b=>b.disabled=actionLocked);
  const reset=document.getElementById("resetBtn");if(reset)reset.disabled=actionLocked;
}
function ensureAudio(){ return null; }function tone(){}function noiseHit(){}function playSound(){}function vibrate(){}
function feedbackForStatus(status, forcedColor=null){
  if(motionPreset()==='low'||graphicsPreset()==='low')return;
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
  // Developer mode stays functional without a persistent screen badge.
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
function registerEnhanceSuccess(d){const prev=d.combo||0;d.combo=prev+1;d.best_combo=Math.max(d.best_combo||0,d.combo);const crossed=[2,3,5,7,10,15].find(t=>prev<t&&d.combo>=t);if(crossed)d.last_combo_milestone=crossed;return comboMultiplier(d.combo);}
function registerEnhanceFailure(d){resetCombo(d);}
function unlockReachedWarps(d=state.runData){for(const w of [10,20,30,40,45,50])if(d.max_level>=w||d.level>=w)d.unlocked_warps[w]=true;}

function runPostEnhanceFlow(prevLvl,newLvl,done=()=>{}){
  setActionLocked(false);done();
}
function runMilestoneOnly(prevLvl,newLvl,done=()=>{}){done();}

function pruneCardParticles(){
  const box=document.getElementById('cardParticles');if(!box)return;
  const gp=graphicsPreset();
  const cap=gp==='low'?0:gp==='medium'?(JION_PERF.mobile?14:36):(JION_PERF.lowPower?20:(JION_PERF.mobile?36:120));
  while(box.childElementCount>cap)box.firstElementChild?.remove();
}
function cleanupTransientEffects(){
  clearDestroySnapshot();
  document.querySelectorAll('.berserk-roulette-overlay,.card-draw-overlay,.frenzy-event-overlay,.result-fx-layer,.destruction-shard,.destruction-void-ring').forEach(e=>e.remove());
  pruneCardParticles();
}
document.addEventListener('visibilitychange',()=>{if(document.hidden)pruneCardParticles();});
window.addEventListener('pagehide',()=>{pruneCardParticles();},{passive:true});

function showBerserkRoulette(finalGain,done=()=>{}){
  const gain=Math.max(2,Math.min(6,Number(finalGain)||2));
  const motion=motionPreset();
  if(motion==='low'){if(typeof done==='function')requestAnimationFrame(done);return;}
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
  for(let i=0;i<(motion==='medium'?8:20);i++)sequence.push(2+((i*3+gain*2+i*i)%5));
  sequence.push(gain);
  const step=()=>{
    if(!overlay.isConnected)return;
    const v=sequence[tick];value.textContent=`+${v}`;
    gsap.fromTo(value,{scale:.74,y:-14,opacity:.45,rotationX:-55},{scale:1,y:0,opacity:1,rotationX:0,duration:.075,ease:'power3.out'});
    if(tick<sequence.length-1){tick++;setTimeout(step,(motion==='medium'?35:55)+tick*(motion==='medium'?3:7));return;}
    overlay.classList.add('locked');result.textContent=`☠ BERSERK +${gain}`;
    cardBurst('#ef4444',gain===6?170:120,gain===6?320:235);impactFlash(gain===6?.68:.38);
    gsap.fromTo(box,{scale:.94},{scale:gain===6?1.09:1.05,duration:.14,ease:'power4.out',yoyo:true,repeat:1});
    gsap.fromTo(value,{scale:1},{scale:gain===6?1.36:1.20,duration:.16,ease:'back.out(2.4)',yoyo:true,repeat:1});
    setTimeout(()=>{overlay.classList.remove('show');setTimeout(()=>{overlay.remove();done();},motion==='medium'?120:210);},motion==='medium'?260:(gain===6?760:580));
  };
  setTimeout(step,motion==='medium'?70:150);
}



let pendingDestroySnapshot=null;
function clearDestroySnapshot(){
  if(!pendingDestroySnapshot)return;
  try{pendingDestroySnapshot.layer?.remove();}catch(e){}
  pendingDestroySnapshot=null;
}
function captureDestroySnapshot(){
  clearDestroySnapshot();
  if(motionPreset()==='low'||graphicsPreset()==='low')return null;
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
  const reduced=JION_PERF.reduced;
  const maxCount=reduced?4:Math.min(count,perfCount(count,6,3));
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
  addDestroyCracks(ghost,perfCount(15,5,3));
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

function showCardDrawReveal(lvl,done=()=>{}){
  const motion=motionPreset();
  if(JION_PERF.reduced||motion==='low'||lvl<=0||lvl>=MAX_LEVEL){done();return;}
  const item=DB[String(lvl)];if(!item){done();return;}
  document.querySelectorAll('.card-draw-overlay').forEach(e=>e.remove());
  const host=document.getElementById('threeWrap')||document.body,overlay=document.createElement('div');overlay.className='card-draw-overlay';overlay.style.setProperty('--draw-color',item.color||'#38bdf8');
  overlay.innerHTML=`<div class="card-draw-pack"><small>NEW ODOR CARD</small><div class="draw-card"><div class="draw-card-back">JION<br>CAPSULE</div><div class="draw-card-front"><span>NEW</span><b>+${lvl}</b><strong>${String(item.name).replace(/^\d+단계\s*:\s*/,'')}</strong><em>TIER ${item.tier||1}</em></div></div><p>새 최고 단계 카드 획득!</p></div>`;
  host.appendChild(overlay);requestAnimationFrame(()=>overlay.classList.add('show'));
  const revealDelay=motion==='medium'?(JION_PERF.mobile?70:90):(JION_PERF.mobile?90:130);
  const dismissDelay=motion==='medium'?(JION_PERF.mobile?420:560):(JION_PERF.mobile?620:820);
  setTimeout(()=>overlay.classList.add('reveal'),revealDelay);
  setTimeout(()=>{overlay.classList.remove('show');setTimeout(()=>{overlay.remove();done();},120);},dismissDelay);
}

function showFrenzyEventOverlay(event,done=()=>{}){
  const motion=motionPreset();
  if(!event||motion==='low'){done();return;}
  document.querySelectorAll('.frenzy-event-overlay').forEach(e=>e.remove());
  const overlay=document.createElement('div');overlay.className='frenzy-event-overlay';
  overlay.innerHTML=`<div class="frenzy-event-card"><small>🔥 ODOR FRENZY EVENT</small><h2>${event.label}</h2><p>${event.desc}</p><div>${event.instant?'INSTANT EVENT':`${event.turns||0} ENHANCE CHARGES`}</div></div>`;
  document.body.appendChild(overlay);requestAnimationFrame(()=>overlay.classList.add('show'));
  const delay=motion==='medium'?(JION_PERF.mobile?420:560):(JION_PERF.mobile?650:820);
  setTimeout(()=>{overlay.classList.remove('show');setTimeout(()=>{overlay.remove();done();},140);},delay);
}

let finalHoldAuthorized=false;
function enhance(mode="normal"){
  if(actionLocked)return;
  cleanupTransientEffects();
  const d=state.runData,curr=d.level;
  if(curr===MAX_LEVEL-1&&mode==='normal'&&!finalHoldAuthorized){showToast('👑 FINAL 강화는 강화 버튼을 길게 눌러야 합니다.');return;}
  if(mode==='berserk'&&(curr<20||curr>48)){showToast('☠️ 광폭 강화는 20~48단계에서만 사용할 수 있습니다.');return;}
  const cost=effectiveEnhanceCost(mode,d);
  if(curr>=MAX_LEVEL){render();return;}
  const cash=money();if(cash<cost){d.status="NOT_ENOUGH_MONEY";showToast("강화 비용 부족!");render();return;}
  const prevMax=Number(d.max_level)||0,frenzyEventBefore=currentFrenzyEvent(d)?{...currentFrenzyEvent(d)}:null;
  setActionLocked(true);finalHoldAuthorized=false;setMoney(cash-cost);
  d.prev_level=curr;state.enhanceAttempts++;
  d.last_aux_effect="";let berserkGain=0;
  const appendAuxEffect=(msg)=>{if(!msg)return;d.last_aux_effect=d.last_aux_effect?`${d.last_aux_effect} · ${msg}`:msg;};
  const successResult=(baseAdd=1,status="SUCCESS",isCritical=false)=>{
    let add=baseAdd;
    if(mode==='berserk'){add=2+Math.floor(Math.random()*5);berserkGain=add;appendAuxEffect(`☠️ 광폭 +${add}단계`);}
    const volatileLv=activeResearchLevel('volatileCore',d);
    if(mode!=='berserk'&&volatileLv>0&&Math.random()<volatileLv*.04&&d.level+add<MAX_LEVEL){
      add+=1;appendAuxEffect("💣 변이 코어 추가 +1단계");
    }
    d.level=Math.min(MAX_LEVEL,d.level+add);d.status=status;d.max_level=Math.max(d.max_level,d.level);state.enhanceSuccesses++;if(isCritical)state.criticalCount++;
    const mult=registerEnhanceSuccess(d);
    if(d.last_combo_milestone){appendAuxEffect(`🔥 ${comboTierMeta(d.combo).name} 해금 · ${comboEffectText(d.combo)}`);delete d.last_combo_milestone;}
    rewardPoints(d.level,mult);
  };
  const destroyResult=()=>{
    if(d.shield>0){d.shield--;d.status="SHIELD_SAVED";state.enhanceFailures++;appendAuxEffect(mode==='berserk'?'☠️ 광폭 폭발 · 방지권 생존':'');}
    else{d.level=0;d.status="DESTROYED";state.enhanceFailures++;state.destroyCount++;appendAuxEffect(mode==='berserk'?'☠️ 광폭 강화 폭발':'');}
    registerEnhanceFailure(d);
  };
  if(devMode){successResult(1,"SUCCESS",false);}
  else{
    const raw=PROB[String(curr)]||[8,40,47,5];
    const [sp,downP,dp]=effectiveProbabilities(raw,{mode});
    const r=Math.random()*100,down=sp+downP,destroy=down+dp;
    if(r<sp){const critRate=criticalRateFor(d,curr),critical=Math.random()<critRate&&curr+2<=MAX_LEVEL;successResult(critical?2:1,critical?"CRITICAL":"SUCCESS",critical);}
    else if(mode==='berserk')destroyResult();
    else if(r<down){
      state.enhanceFailures++;
      if(curr>0)d.level--;d.status="FAILED";
      registerEnhanceFailure(d);
    }
    else if(r<destroy)destroyResult();
    else{d.status="HOLD";state.enhanceFailures++;registerEnhanceFailure(d);}
  }
  const frenzyEvent=updateFrenzyAfterEnhance(d.status,frenzyEventBefore,d);if(frenzyEvent)appendAuxEffect(`🔥 ${frenzyEvent.label.replace(/^\S+\s*/,'')}`);
  unlockReachedWarps(d);
  const newLvl=d.level,isFinalAttempt=curr===MAX_LEVEL-1,newCardUnlocked=newLvl>prevMax;
  const finalCleared=isFinalAttempt&&newLvl===MAX_LEVEL&&['SUCCESS','CRITICAL'].includes(d.status);
  if(finalCleared){state.finalClears=Math.max(0,Number(state.finalClears)||0)+1;}
  if(d.status==="DESTROYED"&&!isFinalAttempt)captureDestroySnapshot();save();
  const normalPost=()=>{
    const done=()=>{
      const afterEvent=()=>{const afterCard=()=>runPostEnhanceFlow(curr,newLvl);if(newCardUnlocked&&!isFinalAttempt)showCardDrawReveal(newLvl,afterCard);else afterCard();};
      if(frenzyEvent)showFrenzyEventOverlay(frenzyEvent,afterEvent);else afterEvent();
    };
    if(isFinalAttempt&&mode==='normal') animateFinal54To55(d.status,done);
    else animateResult(d.status,done);
  };
  if(mode==='berserk'&&berserkGain>0)showBerserkRoulette(berserkGain,normalPost);else normalPost();
}
function sell(){if(actionLocked)return;const d=state.runData,l=d.level;if(l===0)return;const basePrice=dbPrice(l);let price=basePrice*BigInt(stageSellPercent(d))/100n;setMoney(money()+price);state.sellCount++;d.prev_level=l;d.level=0;d.status="READY";d.last_aux_effect="";resetCombo(d);save();render();showToast(`💰 ${l}단계 판매 완료! +${formatGold(price)}`);}
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
  if(currentGameView==='lab')renderLabView();
  if(currentGameView==='shop')renderShopView();
  const mainStage=document.getElementById("threeWrap"),actionGrid=document.getElementById("mainActionGrid");
  if(mainStage)mainStage.classList.remove("hidden");if(actionGrid)actionGrid.classList.remove("hidden");
  const comboLabel=document.getElementById('comboLabel'),auxLabel=document.getElementById('auxLabel');
  if(comboLabel)comboLabel.textContent='🔥 연속 콤보';if(auxLabel)auxLabel.textContent='🔬 장착 파츠';
  document.getElementById("money").textContent=formatGoldCompact(money());document.getElementById("points").textContent=state.points.toLocaleString("ko-KR")+"P";document.getElementById("shield").textContent=shield()+` / ${SHIELD_MAX}개`;
  const frenzyMeter=document.getElementById('frenzyMeter'),frenzyFill=document.getElementById('frenzyFill'),frenzyValue=document.getElementById('frenzyValue'),frenzyHint=document.getElementById('frenzyHint'),activeFrenzy=currentFrenzyEvent(sd);
  const frenzyPct=Math.max(0,Math.min(FRENZY_MAX,Number(sd.frenzyGauge)||0));
  if(frenzyFill)frenzyFill.style.width=frenzyPct+'%';
  if(frenzyValue)frenzyValue.textContent=activeFrenzy?`ACTIVE · ${activeFrenzy.turns}회`:`${Math.round(frenzyPct)}%`;
  if(frenzyHint)frenzyHint.textContent=activeFrenzy?`${activeFrenzy.label.replace(/^\S+\s*/,'')} · ${activeFrenzy.desc}`:'실패·유지·파괴 시 충전 · 100%에서 랜덤 이벤트';
  if(frenzyMeter)frenzyMeter.classList.toggle('active',!!activeFrenzy);document.body.classList.toggle('odor-frenzy-active',!!activeFrenzy);
  const comboNow=sd.combo||0,comboEl=document.getElementById("combo"),comboBonus=document.getElementById("comboBonus"),comboFill=document.getElementById("comboFill"),comboMeter=document.getElementById("comboMeter"),comboMeta=comboTierMeta(comboNow);
  if(comboEl)comboEl.textContent=comboNow>=15?`👑 MAX FEVER · ${comboNow}`:comboNow>=10?`⚡ OVER FEVER · ${comboNow}`:comboNow>=5?`🔥 ${comboMeta.name} · ${comboNow}`:`${comboNow} COMBO`;
  if(comboBonus){comboBonus.textContent=comboEffectText(comboNow);comboBonus.classList.remove("hidden");}
  if(comboFill){const span=Math.max(1,comboMeta.to-comboMeta.from),progress=comboMeta.next?Math.max(0,Math.min(100,((comboNow-comboMeta.from)/span)*100)):100;comboFill.style.width=`${progress}%`;}
  if(comboMeter){comboMeter.dataset.comboTier=comboNow>=15?'max':comboNow>=10?'over':comboNow>=5?'fever':comboNow>=2?'chain':'ready';}
  document.body.classList.toggle('combo-fever',comboNow>=5);document.body.classList.toggle('combo-over-fever',comboNow>=10);document.body.classList.toggle('combo-max-fever',comboNow>=15);document.body.classList.toggle("smell-frenzy",comboNow>=5);
  const modBar=document.getElementById('runModifierBar');if(modBar){const tags=[];const ev=currentFrenzyEvent(sd);if(ev)tags.push(`🔥 ${ev.label.replace(/^\S+\s*/,'')} ${ev.turns}회`);modBar.innerHTML=tags.map(t=>`<span>${t}</span>`).join('');modBar.classList.toggle('hidden',!tags.length);}
  const activeEl=document.getElementById("auxActive"),activeHint=document.getElementById("auxHint"),equippedCount=equippedPartCount(sd);if(activeEl)activeEl.textContent=`${equippedCount} / ${LAB_PART_EQUIP_MAX}개`;if(activeHint){activeHint.textContent=equippedCount>=LAB_PART_EQUIP_MAX?"장착 슬롯 가득 참":"연구소에서 파츠 장착 가능";activeHint.classList.remove("hidden");}
  const modeTitle=document.getElementById("modeTitle"),probTitle=document.querySelector(".prob-title"),probBox=document.getElementById("probBox"),nextReward=document.getElementById("nextReward");
  if(modeTitle){modeTitle.textContent="";modeTitle.classList.add("hidden");}
  if(probTitle)probTitle.innerHTML=`📊 현재 강화 확률 (<span id="probLevel">${l}</span>단계)`;
  const rawP=l>=MAX_LEVEL?[100,0,0,0]:(PROB[String(l)]||[8,40,47,5]),p=effectiveProbabilities(rawP,{data:sd}),comboGuardNow=comboDestroyProtection(sd.combo, rawP[2]),comboSuccessNow=comboSuccessBoost(sd.combo),comboProbNote=(comboGuardNow>0||comboSuccessNow>0)?`<div class="prob-aux combo-guard-note">🔥 콤보 효과${comboSuccessNow?` · 성공 +${comboSuccessNow}%p`:''}${comboGuardNow?` · 파괴 -${comboGuardNow}%p`:''}</div>`:'',labNotes=[],luckLv=activeResearchLevel('luckCore',sd),freezeLv=activeResearchLevel('freezeMatrix',sd);if(luckLv)labNotes.push(`🍀 성공 +${(luckLv*.6).toFixed(1)}%p`);if(freezeLv)labNotes.push(`🧊 하락 ${freezeLv*8}% 유지 전환`);const auxProbNote=labNotes.length?`<div class="prob-aux">${labNotes.join(' · ')}</div>`:"",critPct=Math.round(criticalRateFor(sd,l)*1000)/10,critCopy=l>=50?'✦ 50단계 이후 크리티컬 비활성':'✦ 성공 시 크리티컬 확률';
  if(probBox)probBox.innerHTML=`<div class="prob-row success-row"><span><i></i>성공</span><b class="success">${p[0]}%</b></div><div class="prob-row down-row"><span><i></i>하락</span><b class="down">${p[1]}%</b></div><div class="prob-row destroy-row"><span><i></i>파괴</span><b class="destroy">${p[2]}%</b></div><div class="prob-row hold-row"><span><i></i>유지</span><b class="hold">${p[3]}%</b></div><div class="prob-critical ${l>=50?'disabled-critical':''}">${critCopy} <b>${critPct}%</b></div>${comboProbNote}${auxProbNote}`;
  if(nextReward){nextReward.textContent="";nextReward.classList.add("hidden");}
  const sb=document.getElementById("sellBtn");if(sb)sb.textContent="판매하기";syncActionButtons();renderSceneText();renderEnhanceCard();
}
function renderSceneText(){
  const d=data(),l=level(),status=state.runData.status,tier=Math.min(6,d.tier||1),main=document.getElementById("mainTitle");
  main.className="title-tier-"+tier;main.textContent=d.name;document.getElementById("descText").textContent=`"${d.desc}"`;
  document.getElementById("priceText").textContent="예상 가치: "+formatGold(dbPrice(l));document.getElementById("pointText").textContent="획득 포인트: "+pointReward(l).toLocaleString("ko-KR")+"P";
  document.getElementById("costText").textContent=l>=MAX_LEVEL?"강화 완성 · FINAL STAGE 55":"필요 강화 비용: "+(effectiveEnhanceCost("normal")===0n?"무료":formatGold(effectiveEnhanceCost("normal")));
  const st=document.getElementById("statusText"),labels={READY:"READY - 55단계를 향한 냄새 에너지가 집중됩니다",SUCCESS:"✨ COSMIC SUCCESS (강화 성공) ✨",CRITICAL:"⚡ COSMIC CRITICAL HIT!! (+2단계 이상 대성공) ⚡",SHIELD_SAVED:"🛡️ SHIELD PROTECTED! (파괴 방지권 발동) 🛡️",DESTROYED:"💥 ODOR CAPSULE BREACHED (캡슐 대폭발 붕괴!) 💥",FAILED:"🔻 FAILED (단계 하락) 🔻",HOLD:"🔒 HOLD (단계 유지) 🔒",NOT_ENOUGH_MONEY:"💰 강화 비용 부족"};
  st.textContent=labels[status]||status;const colors={READY:"#38bdf8",SUCCESS:d.color,CRITICAL:"#fff",SHIELD_SAVED:"#60a5fa",DESTROYED:"#f00",FAILED:"#64748b",HOLD:"#94a3b8",NOT_ENOUGH_MONEY:"#f87171"};st.style.color=colors[status]||"#38bdf8";
  const shouldShake=l>=15||(l===MAX_LEVEL&&["SUCCESS","CRITICAL"].includes(status));["mainTitle","descText","priceText","pointText","costText"].forEach(id=>document.getElementById(id).classList.toggle("shaking-text",shouldShake));
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
  const tremor=document.getElementById('stageTremorLayer');if(tremor){const high=l>30;const prog=Math.max(0,Math.min(25,l-30));tremor.classList.toggle('high-stage-tremor',high&&motionPreset()==='high'&&graphicsPreset()!=='low'&&!JION_PERF.mobile&&!JION_PERF.reduced);const tx=0.18+prog*.055,ty=0.12+prog*.042,tr=0.025+prog*.012;tremor.style.setProperty('--tremor-x',tx.toFixed(2)+'px');tremor.style.setProperty('--tremor-x-neg',(-tx).toFixed(2)+'px');tremor.style.setProperty('--tremor-y',ty.toFixed(2)+'px');tremor.style.setProperty('--tremor-y-neg',(-ty).toFixed(2)+'px');tremor.style.setProperty('--tremor-r',tr.toFixed(3)+'deg');tremor.style.setProperty('--tremor-r-neg',(-tr).toFixed(3)+'deg');tremor.style.setProperty('--tremor-speed',Math.max(.105,.34-prog*.0085).toFixed(3)+'s');}
  const stageSpec=stageDesignSpec(l);card.dataset.milestone=stageSpec.milestone?String(stageSpec.milestone):'';const art=document.getElementById('cardArt');if(art){art.dataset.level=String(l);art.dataset.milestone=stageSpec.milestone?String(stageSpec.milestone):'';renderCardDesign(art,l,d);updateOdorCapsuleVisual(art,l,d);}
  const bossOverlay=document.getElementById('bossStageOverlay'),bossBadge=document.getElementById('bossStageBadge'),bossCopy=document.getElementById('bossStageCopy'),bossInfo=MILESTONE_BOSS_COPY[stageSpec.milestone];
  if(bossOverlay&&bossBadge&&bossCopy){if(bossInfo){bossOverlay.classList.remove('hidden');bossBadge.textContent=bossInfo.badge;bossCopy.textContent=bossInfo.copy;}else{bossOverlay.classList.add('hidden');bossBadge.textContent='';bossCopy.textContent='';}}
  document.getElementById('cardStageLabel').textContent=l+'단계'+(l===MAX_LEVEL?' • MAX':'');document.getElementById('cardName').textContent=d.name.replace(/^\d+단계\s*:\s*/,'');document.getElementById('cardDesc').textContent=d.desc;
  document.getElementById('cardPrice').textContent=formatGold(dbPrice(l));document.getElementById('cardPoints').textContent=pointReward(l).toLocaleString('ko-KR')+'P';document.getElementById('cardCost').textContent=l>=MAX_LEVEL?'MAX':(effectiveEnhanceCost('normal')===0n?'무료':formatGold(effectiveEnhanceCost('normal')));
  document.getElementById('cardSerial').textContent=`JION • CAPSULE • ${String(l).padStart(2,'0')}`;document.getElementById('cardTier').textContent='TIER '+['I','II','III','IV','V','VI'][Math.min(5,(d.tier||1)-1)];
  const status=state.runData.status,result=document.getElementById('cardResult');if(result)result.textContent='';
  const scene=document.getElementById('enhanceCardScene');scene.style.setProperty('--glow',d.color);scene.classList.remove('status-success','status-critical','status-failed','status-hold','status-destroyed','status-shield');if(status==='SUCCESS'||status==='CRITICAL')scene.classList.add(status==='CRITICAL'?'status-critical':'status-success');else if(status==='FAILED')scene.classList.add('status-failed');else if(status==='HOLD')scene.classList.add('status-hold');else if(status==='DESTROYED')scene.classList.add('status-destroyed');else if(status==='SHIELD_SAVED')scene.classList.add('status-shield');if(result)result.style.color=status==='DESTROYED'?'#ff5757':status==='FAILED'?'#cbd5e1':status==='CRITICAL'?'#fff':d.color;
}
function cardBurst(color='#ffffff', count=70, power=260){
  const box=document.getElementById('cardParticles'); if(!box)return;
  const gp=graphicsPreset(),mp=motionPreset();
  if(gp==='low'||mp==='low'||JION_PERF.reduced){pruneCardParticles();return;}
  const density=gp==='medium'?.42:1;
  const mobileCap=JION_PERF.lowPower?12:(gp==='medium'?16:28);
  const desktopCap=gp==='medium'?54:160;
  const actualCount=Math.max(1,Math.min(Math.round(count*density),JION_PERF.mobile?mobileCap:desktopCap));
  const childCap=JION_PERF.mobile?(gp==='medium'?28:64):(gp==='medium'?90:260);
  const maxExisting=Math.max(0,childCap-actualCount);
  while(box.childElementCount>maxExisting) box.firstElementChild?.remove();
  const created=[];
  const frag=document.createDocumentFragment();
  for(let i=0;i<actualCount;i++){
    const p=document.createElement('i'); p.className='card-particle'; p.style.color=color; if(['#050505','#000000'].includes(String(color).toLowerCase()))p.classList.add('dark-particle');
    const a=Math.random()*Math.PI*2, dist=power*(gp==='medium'?.72:1)*(.35+Math.random()*.75);
    p.dataset.dx=Math.cos(a)*dist; p.dataset.dy=Math.sin(a)*dist;
    p.style.width=p.style.height=(2+Math.random()*(gp==='medium'?4:6))+'px'; frag.appendChild(p); created.push(p);
  }
  box.appendChild(frag);
  created.forEach((p,i)=>{
    gsap.fromTo(p,{x:0,y:0,scale:.2,opacity:0},{x:+p.dataset.dx,y:+p.dataset.dy,scale:gp==='medium'?1.05:1.4,opacity:1,duration:(gp==='medium'?.14:.18)+Math.random()*(gp==='medium'?.14:.22),delay:i*.0025,ease:'power3.out',onComplete(){gsap.to(p,{opacity:0,duration:gp==='medium'?.26:.48,ease:'power2.out',onComplete:()=>p.remove()})}});
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
  const designParticleCount=Math.min(spec.particles,perfCount(spec.particles,4,2));
  for(let i=0;i<designParticleCount;i++) add('design-particle',`--i:${i};--n:${designParticleCount}`);
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
  else if(kind==="stats")c.innerHTML=statsHTML();
  else if(kind==="lab")c.innerHTML=researchHTML();
  else if(kind==="probabilities")c.innerHTML=probabilitiesHTML();
  else if(kind==="graphics")c.innerHTML=graphicsHTML();
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
  const l=level(),sh=shield(),moneyCost=shieldMoneyCost(l),pointCost=shieldPointCost(l),minShield=15,d=state.runData,warpLevels=[10,20,30,40,45,50];
  const warps=warpLevels.map(w=>{const unlocked=!!d.unlocked_warps[w],passed=l>=w,moneyPrice=warpMoneyCost(w),pointPrice=warpPointCost(w),stateClass=!unlocked?'locked':passed?'passed':'ready',badge=!unlocked?'LOCKED':passed?'PASSED':'READY';return `<div class="warp-card ${stateClass}"><div class="warp-card-top"><div class="warp-target"><span class="warp-icon">${unlocked?'🚀':'🔒'}</span><div><small>TARGET STAGE</small><b>${w}단계 워프</b></div></div><span class="warp-badge">${badge}</span></div><div class="warp-route"><span>현재 +${l}</span><i></i><strong>+${w}</strong></div><div class="warp-costs"><div><small>💰 MONEY</small><b>${formatGold(moneyPrice)}</b></div><div><small>⭐ POINT</small><b>${pointPrice.toLocaleString('ko-KR')}P</b></div></div><div class="warp-actions"><button class="glass-btn warp-buy money-buy" data-buy-warp="money" data-warp="${w}" ${(!unlocked||passed||money()<moneyPrice)?'disabled':''}>💰 돈으로 워프</button><button class="glass-btn warp-buy point-buy" data-buy-warp="point" data-warp="${w}" ${(!unlocked||passed||state.points<pointPrice)?'disabled':''}>⭐ 포인트로 워프</button></div></div>`;}).join('');
  return `<div class="modal-head shop shop-hero"><div class="shop-hero-icon">🛒</div><div><h2>지온 상점</h2><p>파괴 방지권과 해금된 체크포인트 워프를 구매할 수 있습니다. 연구소 파츠는 최대 9개까지 장착할 수 있습니다.</p></div></div><div class="shop-wallet"><div class="wallet-card money"><small>보유 금액</small><b>${formatGold(money())}</b></div><div class="wallet-card point"><small>보유 포인트</small><b>${state.points.toLocaleString('ko-KR')}P</b></div></div><div class="modal-section shop-section shield-section"><div class="section-heading"><div><span>🛡️</span><div><small>PROTECTION</small><h3>파괴 방지권</h3></div></div><b>${sh} / ${SHIELD_MAX}</b></div><p class="section-copy">파괴 결과를 한 번 막아주는 안전장치입니다. ${minShield}단계부터 구매할 수 있습니다.</p><div class="shield-price-grid"><div><small>💰 돈 가격</small><b>${formatGold(moneyCost)}</b></div><div><small>⭐ 포인트 가격</small><b>${pointCost.toLocaleString('ko-KR')}P</b></div></div><div class="warp-actions"><button class="glass-btn money-buy" data-buy-shield="money" ${(l<minShield||sh>=SHIELD_MAX||money()<moneyCost)?'disabled':''}>💰 돈으로 구매</button><button class="glass-btn point-buy" data-buy-shield="point" ${(l<minShield||sh>=SHIELD_MAX||state.points<pointCost)?'disabled':''}>⭐ 포인트로 구매</button></div></div><div class="modal-section shop-section warp-section"><div class="section-heading"><div><span>🚀</span><div><small>STAGE WARP</small><h3>워프권</h3></div></div><b>${l}단계</b></div><p class="section-copy">한 번 도달했던 주요 체크포인트로 즉시 이동합니다. 45단계 워프도 포함됩니다.</p><div class="warp-list">${warps}</div></div>`;
}

function renderShopView(){
  const host=document.getElementById('shopPageContent');
  if(!host)return;
  host.innerHTML=shopHTML();
  bindModal('shop');
}

function partCurrentText(key,lv){
  const cfg=RESEARCH_DATA[key];
  if(!cfg||lv<=0)return '미보유';
  const n=key==='catalyst'||key==='safety' ? (lv*.5).toFixed(1)+'%p'
    : key==='economy' ? '-'+(lv*2)+'%'
    : key==='insight' ? '+'+(lv*4)+'%'
    : key==='resale' ? '+'+(lv*3)+'%'
    : key==='capacitor' ? '+'+(lv*8)+'%'
    : key==='precision' ? '+'+lv+'%p'
    : key==='shieldTech' ? '-'+(lv*4)+'%'
    : key==='warpTech' ? '-'+(lv*3)+'%'
    : key==='fusion' ? `강화비 -${lv}% · 판매 +${lv}%`
    : key==='luckCore' ? '+'+(lv*.6).toFixed(1)+'%p'
    : key==='freezeMatrix' ? (lv*8)+'% 변환'
    : key==='volatileCore' ? '+'+(lv*4)+'% 확률'
    : key==='recoveryCatalyst' ? '+'+(lv*4)+'%'
    : key==='frenzyInjector' ? '+'+(lv*7)+'%'
    : 'Lv.'+lv;
  return `${cfg.effect} ${n}`;
}
function labPartsHTML(){
  const d=state.runData,equippedCount=equippedPartCount(d);
  return Object.entries(RESEARCH_DATA).map(([key,cfg])=>{
    const lv=researchLevel(key,d),cost=researchCost(key,d),maxed=lv>=RESEARCH_MAX,equipped=isResearchEquipped(key,d),canBuy=!maxed&&state.points>=cost,canEquip=lv>0&&(equipped||equippedCount<LAB_PART_EQUIP_MAX);
    const bars=Array.from({length:RESEARCH_MAX},(_,i)=>`<i class="${i<lv?'on':''}"></i>`).join('');
    const status=equipped?'장착 중':lv>0?'보유':'미보유';
    return `<article class="lab-part-card ${lv>0?'installed':''} ${equipped?'equipped':''} ${maxed?'maxed':''}">
      <div class="lab-part-top"><span class="lab-part-icon">${cfg.icon}</span><div><small>${cfg.slot} PART · LV.${lv}/${RESEARCH_MAX}</small><h3>${cfg.name}</h3></div><b>${status}</b></div>
      <p>${cfg.desc}</p>
      <div class="lab-part-levels">${bars}</div>
      <div class="lab-part-spec"><span>${equipped?'적용 효과':'보유 효과'}</span><strong>${partCurrentText(key,lv)}</strong></div>
      <div class="lab-part-actions">
        <button class="glass-btn lab-part-buy" data-research-upgrade="${key}" ${canBuy?'':'disabled'}>${maxed?'MAX 업그레이드':`⭐ ${Number(cost).toLocaleString('ko-KR')}P · ${lv?'업그레이드':'구매'}`}</button>
        <button class="glass-btn lab-part-toggle ${equipped?'is-equipped':''}" data-toggle-part="${key}" ${canEquip?'':'disabled'}>${lv<=0?'구매 필요':equipped?'장착 해제':equippedCount>=LAB_PART_EQUIP_MAX?'9개 장착됨':'장착하기'}</button>
      </div>
    </article>`;
  }).join('');
}
function renderLabView(){
  const grid=document.getElementById('labPartsGrid');
  if(!grid)return;
  const d=state.runData,total=Object.keys(RESEARCH_DATA).reduce((sum,key)=>sum+researchLevel(key,d),0),maxTotal=Object.keys(RESEARCH_DATA).length*RESEARCH_MAX,owned=Object.keys(RESEARCH_DATA).filter(k=>researchLevel(k,d)>0).length,equipped=equippedPartCount(d);
  const wallet=document.getElementById('labPointWallet'),moneyWallet=document.getElementById('labMoneyWallet');if(wallet)wallet.textContent=state.points.toLocaleString('ko-KR')+'P';if(moneyWallet)moneyWallet.textContent=formatGoldCompact(money());
  const summary=document.getElementById('labMachineSummary');
  if(summary)summary.innerHTML=`<div><small>장착 파츠</small><b>${equipped} / ${LAB_PART_EQUIP_MAX}</b></div><div><small>보유 파츠</small><b>${owned} / ${Object.keys(RESEARCH_DATA).length}</b></div><div><small>총 파츠 레벨</small><b>${total} / ${maxTotal}</b></div><div><small>현재 강화 단계</small><b>+${level()}</b></div>`;
  grid.innerHTML=labPartsHTML();
  bindLabButtons();
}
function buyLabPart(key){
  const cfg=RESEARCH_DATA[key],d=state.runData;if(!cfg)return;
  d.research=Object.assign(emptyResearch(),d.research||{});
  d.equippedParts=Array.isArray(d.equippedParts)?d.equippedParts:[];
  const lv=researchLevel(key,d),cost=researchCost(key,d);
  if(lv>=RESEARCH_MAX||cost===null){showToast('이미 최대 업그레이드 상태입니다.');return;}
  if(state.points<cost){showToast('포인트가 부족합니다.');return;}
  state.points-=cost;state.pointsSpentTotal+=cost;d.research[key]=lv+1;
  if(lv===0&&equippedPartCount(d)<LAB_PART_EQUIP_MAX)d.equippedParts.push(key);
  save();render();
  showToast(`${cfg.icon} ${cfg.name} ${lv===0?'구매':'업그레이드'} 완료 · Lv.${lv+1}${lv===0&&isResearchEquipped(key,d)?' · 자동 장착':''}`);
}
function toggleLabPart(key){
  const cfg=RESEARCH_DATA[key],d=state.runData;if(!cfg||researchLevel(key,d)<=0)return;
  d.equippedParts=Array.isArray(d.equippedParts)?d.equippedParts:[];
  if(isResearchEquipped(key,d)){
    d.equippedParts=d.equippedParts.filter(v=>v!==key);
    save();render();showToast(`${cfg.icon} ${cfg.name} 장착 해제`);
    return;
  }
  if(equippedPartCount(d)>=LAB_PART_EQUIP_MAX){showToast(`연구소 파츠는 최대 ${LAB_PART_EQUIP_MAX}개만 장착할 수 있습니다.`);return;}
  d.equippedParts.push(key);save();render();showToast(`${cfg.icon} ${cfg.name} 장착 완료 · ${equippedPartCount(d)}/${LAB_PART_EQUIP_MAX}`);
}
function bindLabButtons(){
  document.querySelectorAll('#labView [data-research-upgrade]').forEach(b=>b.onclick=()=>buyLabPart(b.dataset.researchUpgrade));
  document.querySelectorAll('#labView [data-toggle-part]').forEach(b=>b.onclick=()=>toggleLabPart(b.dataset.togglePart));
}

function setGameView(view){
  if(actionLocked)return;
  currentGameView=['enhance','shop','lab'].includes(view)?view:'enhance';
  closeModal();
  const main=document.querySelector('main.layout'),shop=document.getElementById('shopView'),lab=document.getElementById('labView');
  if(main)main.classList.toggle('hidden',currentGameView!=='enhance');
  if(shop)shop.classList.toggle('hidden',currentGameView!=='shop');
  if(lab)lab.classList.toggle('hidden',currentGameView!=='lab');
  document.body.classList.toggle('shop-view-active',currentGameView==='shop');
  document.body.classList.toggle('lab-view-active',currentGameView==='lab');
  document.querySelectorAll('[data-game-view]').forEach(btn=>{const active=btn.dataset.gameView===currentGameView;btn.classList.toggle('active',active);btn.setAttribute('aria-selected',active?'true':'false');});
  if(currentGameView==='shop')renderShopView();
  if(currentGameView==='lab')renderLabView();
}
function researchHTML(){return `<div class="modal-head research-modal-head"><div class="research-head-icon">🔬</div><div><h2>냄새 연구소</h2><p>연구소 파츠는 최대 9개까지 선택 장착할 수 있습니다.</p></div></div><button class="glass-btn" data-open-lab-view>연구소로 이동</button>`;}

function probabilitiesHTML(){
  const current=level();
  const fmt=v=>Number.isInteger(Number(v))?String(Number(v)):Number(v).toFixed(1);
  const rows=[];
  for(let l=1;l<=MAX_LEVEL;l++){
    const sellText=formatGold(dbPrice(l));
    const costText=l>=MAX_LEVEL?'MAX':formatGold(baseEnhanceCost(l));
    const pointText=l>=MAX_LEVEL?'-':pointReward(l+1).toLocaleString('ko-KR')+'P';
    if(l===MAX_LEVEL){
      rows.push(`<tr class="prob-table-row max-row ${current===l?'current-row':''}"><td><b>+${l}</b></td><td colspan="4" class="max-cell">MAX · 강화 완료</td><td class="pt-cost">${costText}</td><td class="pt-sell">${sellText}</td><td class="pt-point">${pointText}</td></tr>`);
      continue;
    }
    const p=PROB[String(l)]||[0,0,0,0];
    rows.push(`<tr class="prob-table-row ${current===l?'current-row':''}"><td><b>+${l} → +${l+1}</b></td><td class="pt-success">${fmt(p[0])}%</td><td class="pt-down">${fmt(p[1])}%</td><td class="pt-destroy">${fmt(p[2])}%</td><td class="pt-hold">${fmt(p[3])}%</td><td class="pt-cost">${costText}</td><td class="pt-sell">${sellText}</td><td class="pt-point">${pointText}</td></tr>`);
  }
  return `<div class="modal-head probability-head"><div class="probability-head-icon">📊</div><div><h2>강화 확률표</h2><p>1~55단계 기본 일반 강화 기준입니다. 강화 비용, 판매 금액, 성공 시 획득 포인트까지 함께 표시됩니다.</p></div></div>
    <div class="probability-subnote">※ 강화 비용은 연구소 할인 전 기본값, 판매 금액은 현재 단계 판매 시 기준 금액, 포인트는 성공으로 다음 단계에 도달했을 때 획득하는 기본 포인트입니다.</div>
    <div class="probability-table-wrap"><table class="probability-table"><thead><tr><th>강화 구간</th><th>성공</th><th>하락</th><th>파괴</th><th>유지</th><th>강화 비용</th><th>판매 금액</th><th>획득 포인트</th></tr></thead><tbody>${rows.join('')}</tbody></table></div>`;
}

function graphicsHTML(){
  const settings=normalizeUiSettings(state.uiSettings);
  const choice=(group,value,title,desc)=>`<button class="graphics-choice-btn ${settings[group]===value?'active':''}" type="button" data-setting-group="${group}" data-setting-value="${value}"><strong>${title}</strong><span>${desc}</span></button>`;
  return `<div class="modal-head graphics-head"><div class="graphics-head-icon">🎛️</div><div><h2>그래픽 설정</h2><p>기기 성능과 취향에 맞게 그래픽 품질과 모션 강도를 직접 조절할 수 있습니다.</p></div></div>
    <div class="graphics-current-note">현재 설정 · 그래픽 <b>${settings.graphics==='high'?'상':settings.graphics==='medium'?'중':'하'}</b> · 모션 <b>${settings.motion==='high'?'상':settings.motion==='medium'?'중':'하'}</b></div>
    <div class="graphics-settings-grid">
      <section class="graphics-setting-card"><small>GRAPHICS QUALITY</small><h3>그래픽 품질</h3><p class="graphics-setting-desc">상: 풀 블러·광원·파티클 · 중: 광원/파티클 축소 · 하: 정적 배경 중심, 고비용 필터 최소화</p><div class="graphics-choice-grid">${choice('graphics','high','상','풀 효과 · 최대 품질')}${choice('graphics','medium','중','효과 밀도 약 40~60%')}${choice('graphics','low','하','정적 효과 · 저부하')}</div></section>
      <section class="graphics-setting-card"><small>MOTION STRENGTH</small><h3>모션 강도</h3><p class="graphics-setting-desc">상: 전체 시네마틱 · 중: 짧고 가벼운 연출 · 하: 강화 결과 즉시 반영, 워프/룰렛/카드 공개 연출 생략</p><div class="graphics-choice-grid">${choice('motion','high','상','전체 연출')}${choice('motion','medium','중','축약 연출')}${choice('motion','low','하','즉시 처리 · 최고 성능')}</div></section>
    </div>`;
}

function statsHTML(){
  const d=state.runData;
  const attempts=Math.max(0,Number(state.enhanceAttempts)||0);
  const successes=Math.max(0,Number(state.enhanceSuccesses)||0);
  const failures=Math.max(0,Number(state.enhanceFailures)||0);
  const destroys=Math.max(0,Number(state.destroyCount)||0);
  const criticals=Math.max(0,Number(state.criticalCount)||0);
  const sells=Math.max(0,Number(state.sellCount)||0);
  const warps=Math.max(0,Number(state.warpUses)||0);
  const finalClears=Math.max(0,Number(state.finalClears)||0);
  const frenzyTriggers=Math.max(0,Number(state.frenzyTriggers)||0);
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
      <article><small>FINAL 클리어</small><b class="stats-gold">${fmtNum(finalClears)}</b></article>
      <article><small>폭주 발동</small><b>${fmtNum(frenzyTriggers)}</b></article>
    </div>
    <div class="stats-section-title"><span>⭐</span><div><small>POINT ECONOMY</small><b>포인트 기록</b></div></div>
    <div class="stats-grid stats-grid-3">
      <article><small>누적 획득</small><b class="stats-gold">${fmtNum(earned)}P</b></article>
      <article><small>누적 사용</small><b>${fmtNum(spent)}P</b></article>
      <article><small>현재 보유</small><b class="stats-good">${fmtNum(state.points)}P</b></article>
    </div>
    `;
}

function bindModal(kind){
  document.querySelectorAll("[data-open-lab-view]").forEach(b=>b.onclick=()=>{closeModal();setGameView('lab');});
  document.querySelectorAll("[data-buy-shield]").forEach(b=>b.onclick=()=>{
    const type=b.dataset.buyShield,l=level(),min=15,cost=type==="money"?shieldMoneyCost(l):shieldPointCost(l);
    if(l<min||shield()>=SHIELD_MAX){showToast(shield()>=SHIELD_MAX?`방지권은 최대 ${SHIELD_MAX}개까지 보유할 수 있습니다.`:"구매 조건을 만족하지 못했습니다.");return;}
    if(type==="money"){if(money()<cost){showToast("금액이 부족합니다.");return;}setMoney(money()-cost);}else{if(state.points<cost){showToast("포인트가 부족합니다.");return;}state.points-=cost;state.pointsSpentTotal+=cost;}
    state.runData.shield++;save();render();if(currentGameView==='shop')renderShopView();else openModal("shop");showToast("🛡️ 파괴 방지권 구매 완료!");
  });
  document.querySelectorAll("[data-setting-group]").forEach(b=>b.onclick=()=>{
    updateUiSetting(b.dataset.settingGroup,b.dataset.settingValue);
    openModal('graphics');
    showToast(`🎛️ ${b.dataset.settingGroup==='graphics'?'그래픽':'모션'} 설정이 적용되었습니다.`);
  });
  document.querySelectorAll("[data-buy-warp]").forEach(b=>b.onclick=()=>{
    if(actionLocked)return;
    const type=b.dataset.buyWarp,w=Number(b.dataset.warp),d=state.runData,cost=type==="money"?warpMoneyCost(w):warpPointCost(w);
    if(!d.unlocked_warps[w]||level()>=w){showToast("워프 조건을 만족하지 못했습니다.");return;}
    if(type==="money"&&money()<cost){showToast("금액이 부족합니다.");return;}
    if(type!=="money"&&state.points<cost){showToast("포인트가 부족합니다.");return;}
    if(currentGameView==='shop')setGameView('enhance');else closeModal();setActionLocked(true);
    playWarpAnimation(w,()=>{
      if(type==="money")setMoney(money()-cost);else{state.points-=cost;state.pointsSpentTotal+=cost;}
      state.warpUses++;const prevWarp=d.level;d.prev_level=prevWarp;d.level=w;d.max_level=Math.max(d.max_level,w);d.status="SUCCESS";d.last_aux_effect="";resetCombo(d);d._warpPrev=prevWarp;
      unlockReachedWarps(d);save();render();spawnEnhanceBurst('#22d3ee',90,.18,.06,.70,'add');setTimeout(()=>spawnEnhanceBurst('#a855f7',70,.15,.055,.65,'add'),100);
    },()=>{const prevWarp=Number(d._warpPrev??w);delete d._warpPrev;save();showToast(`🚀 ${w}단계 워프 완료!`);runMilestoneOnly(prevWarp,w,()=>setActionLocked(false));});
  });
}
document.getElementById("closeModal").onclick=closeModal;
document.getElementById("modal").addEventListener("click",e=>{if(e.target.id==="modal")closeModal();});
window.addEventListener("keydown",e=>{if(e.key==="Escape")closeModal();});
document.querySelectorAll("[data-modal]").forEach(b=>b.onclick=()=>{if(!actionLocked)openModal(b.dataset.modal);});
document.querySelectorAll("[data-game-view]").forEach(b=>b.onclick=()=>setGameView(b.dataset.gameView));
setGameView(currentGameView);
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
  cleanupTransientEffects();
  const motion=motionPreset();
  if(motion==='low'){
    if(typeof onShift==='function')onShift();
    if(typeof onComplete==='function')requestAnimationFrame(onComplete);
    return;
  }
  const old=document.getElementById('warpFxOverlay');if(old)old.remove();
  const overlay=document.createElement('div');overlay.id='warpFxOverlay';overlay.className='warp-fx-overlay';
  const warpStreakCount=motion==='medium'?Math.min(5,perfCount(24,7,4)):perfCount(24,7,4);
  overlay.innerHTML=`
    <div class="warp-fx-space"></div>
    <div class="warp-fx-streaks">${Array.from({length:warpStreakCount},(_,i)=>`<i style="--i:${i};--a:${i*(360/warpStreakCount)}deg"></i>`).join('')}</div>
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
  const motion=motionPreset();
  if(!target||JION_PERF.reduced||motion==='low')return;
  if(JION_PERF.mobile){power*=JION_PERF.lowPower?.45:.62;duration=Math.min(duration,.26);}
  if(motion==='medium'){power*=.58;duration=Math.min(duration,.16);}
  const px=Math.max(2,Math.min(10,power*24));
  gsap.killTweensOf(target);
  gsap.fromTo(target,{x:-px,y:px*.45},{x:px,y:-px*.45,duration:.038,repeat:Math.max(2,Math.round(duration/.076)),yoyo:true,ease:'none',onComplete:()=>gsap.set(target,{x:0,y:0})});
}
function impactFlash(opacity=.75){
  const flash=document.getElementById('flashOverlay');
  const motion=motionPreset();
  if(!flash||motion==='low')return;
  flash.style.opacity='0';
  if(motion==='medium')opacity*=.6;
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
  const motionMode=motionPreset();
  if(motionMode==='low'){render();if(typeof afterFinish==='function')requestAnimationFrame(afterFinish);return;}
  if(motionMode==='medium'){animateResult(status,afterFinish);return;}
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

  const finalRayCount=perfCount(28,8,5),finalTickCount=perfCount(36,9,6);
  const rays=Array.from({length:finalRayCount},(_,i)=>`<i class="final-common-ray" style="--i:${i};--final-count:${finalRayCount}"></i>`).join('');
  const ticks=Array.from({length:finalTickCount},(_,i)=>`<i class="final-common-tick" style="--i:${i};--final-count:${finalTickCount}"></i>`).join('');
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
    FAILED:['강화 하락',`${MAX_LEVEL-2}단계로 하락`,'#ffffff'],
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
  FAILED:'DOWN',
  DESTROYED:'DESTROYED',
  HOLD:'HOLD',
  CRITICAL:'CRITICAL',
  SHIELD_SAVED:'SHIELD',
  TEARS:'TEARS'
};

function resultFxHoldStyle(label,color,kind='hold'){
  const mp=motionPreset(),gp=graphicsPreset();
  if(mp==='low'||gp==='low')return null;
  const normalizedKind=String(kind).toLowerCase();
  const holdRingCount=mp==='medium'?Math.min(2,perfCount(5,3,2)):perfCount(5,3,2),holdTickCount=mp==='medium'?Math.min(6,perfCount(24,7,4)):perfCount(24,7,4);
  const rings=Array.from({length:holdRingCount},(_,i)=>`<div class="hold-ring h${i+1}"></div>`).join('');
  const ticks=Array.from({length:holdTickCount},(_,i)=>`<i class="hold-tick" style="--i:${i};--hold-count:${holdTickCount}"></i>`).join('');
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
  const motionMode=motionPreset();
  pendingParticleOverride=null;
  pendingAnimationOverride=null;
  clearResultFx();

  const visualStatus=animationType==='TEARS'?'TEARS':status;
  if(visualStatus!=='DESTROYED'&&pendingDestroySnapshot)clearDestroySnapshot();
  const label=HOLD_STYLE_LABELS[visualStatus]||String(visualStatus||'RESULT');
  const kind=visualStatus;
  const sceneClass={
    SUCCESS:'status-success',CRITICAL:'status-critical',
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
    const scaledBurst=motionMode==='medium'?Math.max(8,Math.round(burstCount*.58)):burstCount;
    if(scaledBurst)cardBurst(particleColor,scaledBurst,burstPower);
    if(flashAmount)impactFlash(flashAmount);
  };

  gsap.set(motion,{x:0,y:0,z:0,rotation:0,rotationX:0,rotationY:0,scale:1,opacity:1,filter:'none',transformOrigin:'50% 52%'});
  if(glow)gsap.set(glow,{scale:.82,opacity:.06,background:particleColor,x:0,y:0});
  if(shine)gsap.set(shine,{x:'-70%'});

  if(motionMode==='low'){
    commitVisual();
    if(glow){glow.style.opacity='0';glow.style.transform='none';}
    if(flash)flash.style.opacity='0';
    if(typeof afterFinish==='function')requestAnimationFrame(afterFinish);
    return;
  }

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



function resetGame(){
  if(actionLocked)return;
  const ok=window.confirm?.('현재 진행 상황과 연구소 파츠 데이터까지 모두 초기화할까요?') ?? true;
  if(!ok)return;
  document.querySelectorAll('.card-draw-overlay,.berserk-roulette-overlay,.frenzy-event-overlay,.warp-fx-overlay,.system-choice-overlay,.result-fx-layer').forEach(e=>e.remove());
  cleanupTransientEffects();
  state=clone(INITIAL);
  save();
  render();
  closeModal();
  showToast('↻ 게임 데이터를 초기화했습니다.');
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
  if(JION_PERF.mobile||JION_PERF.reduced)return;
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
  if(JION_PERF.mobile||JION_PERF.reduced)return;
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

  const numericIds=['money','points','shield','combo','frenzyValue','cardLevel','cardPrice','cardPoints','cardCost'];
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
