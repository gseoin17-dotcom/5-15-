import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="메이플 러너 3D", page_icon="⚔️", layout="wide")

st.title("⚔️ 메이플 러너 3D")
st.caption("Python + Streamlit + Three.js 로 만든 메이플스토리 감성 3D 사이드 스크롤 액션 게임")

with st.expander("🎮 조작법 보기", expanded=False):
    st.markdown(
        """
        - **← / A**, **→ / D** : 좌우 이동
        - **스페이스바 / ↑ / W** : 점프 (더블 점프 가능!)
        - **X 또는 J** : 검 공격 (근처 몬스터 처치)
        - 몬스터를 처치하면 **EXP**, 코인을 먹으면 **점수**가 올라갑니다.
        - EXP를 다 채우면 **레벨업**! 체력이 0이 되면 게임 오버.
        """
    )

GAME_HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  html, body { margin:0; padding:0; overflow:hidden; background:#87CEEB; }
  #gameWrap { position:relative; width:100%; height:620px; border-radius:14px; overflow:hidden;
    box-shadow: 0 8px 30px rgba(0,0,0,0.35); border:3px solid #6b3fa0; }
  canvas { display:block; }
  #hud { position:absolute; top:10px; left:10px; font-family:'Trebuchet MS', sans-serif; color:#fff;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.8); z-index:10; user-select:none; }
  .barBg { width:220px; height:16px; background:rgba(0,0,0,0.4); border-radius:8px; margin:4px 0;
    border:1px solid rgba(255,255,255,0.5); overflow:hidden; }
  .barFill { height:100%; transition:width 0.2s ease; }
  #hpFill { background:linear-gradient(90deg,#ff5e5e,#ff2626); }
  #expFill { background:linear-gradient(90deg,#7ee0ff,#2196f3); }
  #lvlText { font-size:20px; font-weight:bold; color:#ffe066; }
  #scoreText { font-size:16px; margin-top:4px; }
  #msg { position:absolute; top:45%; left:50%; transform:translate(-50%,-50%); z-index:20;
    font-family:'Trebuchet MS', sans-serif; font-size:34px; font-weight:bold; color:#fff;
    text-shadow:2px 2px 6px rgba(0,0,0,0.8); text-align:center; display:none; }
  #startBtn { margin-top:14px; padding:10px 26px; font-size:18px; border-radius:10px; border:none;
    background:#ffe066; color:#5b3200; font-weight:bold; cursor:pointer; box-shadow:0 4px 0 #c9a53a; }
  #startBtn:active { transform:translateY(3px); box-shadow:none; }
</style>
</head>
<body>
<div id="gameWrap">
  <div id="hud">
    <div id="lvlText">Lv. 1</div>
    <div class="barBg"><div id="hpFill" class="barFill" style="width:100%"></div></div>
    <div class="barBg"><div id="expFill" class="barFill" style="width:0%"></div></div>
    <div id="scoreText">SCORE 0</div>
  </div>
  <div id="msg">
    <div id="msgText">메이플 러너 3D</div>
    <div><button id="startBtn">모험 시작!</button></div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){
  const wrap = document.getElementById('gameWrap');
  const W = wrap.clientWidth, H = 620;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x87CEEB);
  scene.fog = new THREE.Fog(0x87CEEB, 30, 90);

  const camera = new THREE.PerspectiveCamera(50, W/H, 0.1, 200);
  camera.position.set(0, 6, 16);

  const renderer = new THREE.WebGLRenderer({antialias:true});
  renderer.setSize(W, H);
  renderer.shadowMap.enabled = true;
  wrap.insertBefore(renderer.domElement, wrap.firstChild);

  const hemi = new THREE.HemisphereLight(0xffffff, 0x445566, 0.9);
  scene.add(hemi);
  const sun = new THREE.DirectionalLight(0xfff2cc, 1.0);
  sun.position.set(10, 20, 10);
  sun.castShadow = true;
  sun.shadow.mapSize.set(1024,1024);
  scene.add(sun);

  // Decorative clouds
  for (let i=0;i<10;i++){
    const cloud = new THREE.Mesh(
      new THREE.SphereGeometry(1.2+Math.random(), 8, 8),
      new THREE.MeshStandardMaterial({color:0xffffff, transparent:true, opacity:0.85})
    );
    cloud.position.set(-40+Math.random()*160, 10+Math.random()*8, -20-Math.random()*15);
    scene.add(cloud);
  }

  // Platforms (Maple-style floating islands)
  const platforms = [];
  const platMat = new THREE.MeshStandardMaterial({color:0x8bc34a});
  const dirtMat = new THREE.MeshStandardMaterial({color:0x8d6e42});
  function addPlatform(x,y,w){
    const grp = new THREE.Group();
    const top = new THREE.Mesh(new THREE.BoxGeometry(w,0.6,4), platMat);
    top.position.y = 0.3;
    top.castShadow = true; top.receiveShadow = true;
    const body = new THREE.Mesh(new THREE.BoxGeometry(w-0.4,1.4,3.4), dirtMat);
    body.position.y = -0.7;
    body.receiveShadow = true;
    grp.add(top, body);
    grp.position.set(x,y,0);
    scene.add(grp);
    platforms.push({x, y, w, mesh:grp});
  }
  addPlatform(0, 0, 14);
  addPlatform(11, 2.2, 6);
  addPlatform(19, 4.4, 5);
  addPlatform(27, 2.2, 6);
  addPlatform(35, 0, 14);
  addPlatform(46, 2.8, 6);
  addPlatform(54, 5.2, 5);
  addPlatform(62, 2.8, 6);
  addPlatform(70, 0, 20);

  // Trees
  function addTree(x,y){
    const trunk = new THREE.Mesh(new THREE.CylinderGeometry(0.2,0.25,1.6,8), new THREE.MeshStandardMaterial({color:0x7a4a2b}));
    trunk.position.set(x, y+1.1, -1.2);
    const leaves = new THREE.Mesh(new THREE.SphereGeometry(0.9,10,10), new THREE.MeshStandardMaterial({color:0x4caf50}));
    leaves.position.set(x, y+2.1, -1.2);
    scene.add(trunk, leaves);
  }
  platforms.forEach(p => { if(p.w>10) addTree(p.x - p.w/4, p.y); });

  // Player (capsule-ish blocky character, Maple vibe)
  const player = new THREE.Group();
  const body = new THREE.Mesh(new THREE.BoxGeometry(0.7,0.9,0.5), new THREE.MeshStandardMaterial({color:0x3f51b5}));
  body.position.y = 0.45; body.castShadow = true;
  const head = new THREE.Mesh(new THREE.SphereGeometry(0.35,12,12), new THREE.MeshStandardMaterial({color:0xffe0b2}));
  head.position.y = 1.1; head.castShadow = true;
  const hair = new THREE.Mesh(new THREE.SphereGeometry(0.38,12,12,0,Math.PI*2,0,Math.PI/1.6), new THREE.MeshStandardMaterial({color:0xffca28}));
  hair.position.y = 1.18;
  const sword = new THREE.Mesh(new THREE.BoxGeometry(0.1,0.9,0.1), new THREE.MeshStandardMaterial({color:0xcfd8dc}));
  sword.position.set(0.5, 0.5, 0);
  sword.rotation.z = -0.5;
  player.add(body, head, hair, sword);
  player.position.set(0, 0.6, 0);
  scene.add(player);

  // Enemies (slimes)
  const enemies = [];
  function addEnemy(x,y,range){
    const slime = new THREE.Mesh(new THREE.SphereGeometry(0.45,12,12), new THREE.MeshStandardMaterial({color:0xef5350}));
    slime.position.set(x, y+0.45, 0);
    slime.castShadow = true;
    scene.add(slime);
    enemies.push({mesh:slime, baseX:x, y:y, range, dir:1, speed:0.02+Math.random()*0.015, alive:true});
  }
  addEnemy(4, 0, 2.5);
  addEnemy(19, 4.4, 1.5);
  addEnemy(38, 0, 3);
  addEnemy(46, 2.8, 2);
  addEnemy(70, 0, 4);
  addEnemy(76, 0, 3);

  // Coins
  const coins = [];
  function addCoin(x,y){
    const coin = new THREE.Mesh(new THREE.CylinderGeometry(0.25,0.25,0.08,16), new THREE.MeshStandardMaterial({color:0xffd54f, metalness:0.6, roughness:0.3}));
    coin.rotation.x = Math.PI/2;
    coin.position.set(x, y+1.3, 0);
    scene.add(coin);
    coins.push({mesh:coin, taken:false});
  }
  [2,6,11,15,19,23,27,31,38,42,46,50,54,58,62,66,70,74].forEach((x,i)=>addCoin(x, platforms.reduce((a,p)=> (x>=p.x-p.w/2 && x<=p.x+p.w/2)? p.y : a, 0)));

  // Physics state
  let vy = 0, vx = 0;
  const GRAV = -0.028, MOVE = 0.14, JUMP = 0.46;
  let onGround = false, jumpsLeft = 2;
  let facing = 1;

  let hp = 100, maxHp = 100, exp = 0, expMax = 50, level = 1, score = 0;
  let gameOver = false, started = false;
  let attackCooldown = 0, invuln = 0;

  const keys = {};
  window.addEventListener('keydown', e => {
    keys[e.code] = true;
    if ((e.code==='Space'||e.code==='ArrowUp'||e.code==='KeyW') ) e.preventDefault();
  });
  window.addEventListener('keyup', e => keys[e.code] = false);

  function currentPlatformY(x, y){
    let best = null;
    for (const p of platforms){
      if (x > p.x-p.w/2 && x < p.x+p.w/2){
        if (y - p.y >= -0.05){
          if (best===null || p.y>best) best = p.y;
        }
      }
    }
    return best;
  }

  function updateHUD(){
    document.getElementById('hpFill').style.width = Math.max(0,(hp/maxHp*100))+'%';
    document.getElementById('expFill').style.width = Math.max(0,(exp/expMax*100))+'%';
    document.getElementById('lvlText').textContent = 'Lv. ' + level;
    document.getElementById('scoreText').textContent = 'SCORE ' + score;
  }

  function showMsg(text, showBtn){
    const msg = document.getElementById('msg');
    document.getElementById('msgText').textContent = text;
    document.getElementById('startBtn').style.display = showBtn ? 'inline-block' : 'none';
    msg.style.display = 'block';
  }
  function hideMsg(){ document.getElementById('msg').style.display = 'none'; }

  document.getElementById('startBtn').addEventListener('click', () => {
    hideMsg();
    started = true;
    if (gameOver) resetGame();
  });

  function resetGame(){
    hp=100; exp=0; expMax=50; level=1; score=0; gameOver=false;
    player.position.set(0,0.6,0); vx=0; vy=0;
    enemies.forEach(en=>{ en.alive=true; en.mesh.visible=true; en.mesh.position.x = en.baseX; });
    coins.forEach(c=>{ c.taken=false; c.mesh.visible=true; });
    updateHUD();
  }

  function levelUp(){
    level += 1;
    exp = 0;
    expMax = Math.floor(expMax*1.35);
    maxHp += 15; hp = maxHp;
  }

  function gainExp(v){
    exp += v;
    while (exp >= expMax){ exp -= expMax; levelUp(); }
  }

  function takeDamage(v){
    if (invuln > 0) return;
    hp -= v; invuln = 45;
    if (hp <= 0){
      hp = 0; gameOver = true; started = false;
      showMsg('게임 오버! 점수: ' + score, true);
    }
  }

  function attack(){
    if (attackCooldown > 0) return;
    attackCooldown = 20;
    sword.rotation.z = -2.0;
    setTimeout(()=>{ sword.rotation.z = -0.5; }, 120);
    enemies.forEach(en => {
      if (!en.alive) return;
      const dx = en.mesh.position.x - player.position.x;
      const dy = en.mesh.position.y - player.position.y;
      if (Math.abs(dx) < 1.4 && Math.abs(dy) < 1.4 && Math.sign(dx||1)===facing){
        en.alive = false;
        en.mesh.visible = false;
        gainExp(18);
        score += 50;
      }
    });
  }

  function animate(){
    requestAnimationFrame(animate);
    if (started && !gameOver){
      // input
      vx = 0;
      if (keys['ArrowLeft']||keys['KeyA']){ vx = -MOVE; facing=-1; }
      if (keys['ArrowRight']||keys['KeyD']){ vx = MOVE; facing=1; }
      if ((keys['Space']||keys['ArrowUp']||keys['KeyW']) && jumpsLeft>0 && !keys['__jumpLock']){
        vy = JUMP; jumpsLeft -= 1; keys['__jumpLock']=true;
      }
      if (!(keys['Space']||keys['ArrowUp']||keys['KeyW'])) keys['__jumpLock']=false;
      if (keys['KeyX']||keys['KeyJ']) attack();

      vy += GRAV;
      player.position.x += vx;
      player.position.y += vy;
      player.rotation.y = facing>0 ? Math.PI/2 : -Math.PI/2;

      const groundY = currentPlatformY(player.position.x, player.position.y);
      if (groundY !== null && player.position.y + vy <= groundY + 0.601 && vy <= 0){
        player.position.y = groundY + 0.6;
        vy = 0; onGround = true; jumpsLeft = 2;
      } else {
        onGround = false;
      }
      if (player.position.y < -8){
        takeDamage(100);
      }
      player.position.x = Math.max(-2, player.position.x);

      // enemies patrol + collision
      enemies.forEach(en => {
        if (!en.alive) return;
        en.mesh.position.x += en.dir*en.speed;
        if (Math.abs(en.mesh.position.x - en.baseX) > en.range) en.dir *= -1;
        en.mesh.rotation.y += 0.05;
        const dx = en.mesh.position.x - player.position.x;
        const dyv = en.mesh.position.y - player.position.y;
        if (Math.abs(dx) < 0.8 && Math.abs(dyv) < 0.9){
          takeDamage(8);
        }
      });

      // coins
      coins.forEach(c => {
        if (c.taken) return;
        c.mesh.rotation.z += 0.08;
        const dx = c.mesh.position.x - player.position.x;
        const dy = c.mesh.position.y - player.position.y;
        if (Math.abs(dx) < 0.7 && Math.abs(dy) < 0.9){
          c.taken = true; c.mesh.visible = false; score += 10;
        }
      });

      if (attackCooldown>0) attackCooldown--;
      if (invuln>0) invuln--;
      body.material.opacity = 1;

      // win condition
      if (player.position.x > 78){
        started = false;
        showMsg('클리어! 최종 점수: ' + score, true);
      }

      // camera follow
      camera.position.x += (player.position.x - camera.position.x) * 0.08;
      camera.position.y += (player.position.y + 4.5 - camera.position.y) * 0.08;
      camera.lookAt(player.position.x, player.position.y+0.6, 0);

      updateHUD();
    }
    renderer.render(scene, camera);
  }

  showMsg('메이플 러너 3D', true);
  animate();
})();
</script>
</body>
</html>
"""

components.html(GAME_HTML, height=650, scrolling=False)

st.markdown(
    """
    ---
    ### 💡 게임 정보
    - **엔진**: Three.js (WebGL) — Streamlit 컴포넌트로 임베드
    - **테마**: 메이플스토리 감성의 플로팅 아일랜드, 슬라임 몬스터, 코인, 레벨업 시스템
    - 오른쪽 끝(약 x=78)까지 도달하면 클리어! 슬라임을 피하거나 검으로 처치하며 진행하세요.
    - 로컬에서 실행: `pip install streamlit` 후 `streamlit run maple_platformer.py`
    """
)
