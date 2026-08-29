import streamlit as st

st.set_page_config(page_title="Ball Fight Game", page_icon="💥", layout="centered")

# 영상과 완전히 똑같은 UI와 캔버스 게임 엔진을 품은 HTML/JS 코드
game_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Ball Fight Simulator</title>
    <style>
        body {
            background-color: #ffffff;
            color: black;
            text-align: center;
            font-family: 'Malgun Gothic', sans-serif;
            margin: 0;
            padding: 10px;
        }
        .game-container {
            width: 600px;
            margin: 0 auto;
            border: 3px solid black;
            background: #ffffff;
            position: relative;
        }
        canvas {
            display: block;
            background: #ffffff;
        }
        .scoreboard {
            width: 600px;
            margin: 10px auto 0 auto;
            display: flex;
            justify-content: space-between;
            border: 2px solid black;
            padding: 5px;
            background: #f9f9f9;
        }
        .player-box {
            width: 48%;
            text-align: left;
        }
        .player-box.right {
            text-align: right;
        }
        .name {
            font-weight: bold;
            font-size: 18px;
        }
        .hp-bar-outer {
            background-color: #333;
            border: 2px solid black;
            height: 22px;
            margin-top: 4px;
            position: relative;
        }
        .hp-bar-inner {
            height: 100%;
            width: 100%;
            background-color: #2ecc71;
            transition: width 0.1s linear;
        }
        .hp-text {
            position: absolute;
            width: 100%;
            top: 0;
            left: 0;
            text-align: center;
            font-size: 12px;
            font-weight: bold;
            color: white;
            line-height: 18px;
        }
        .reset-btn {
            margin-top: 15px;
            padding: 8px 16px;
            font-weight: bold;
            background: #ff4b4b;
            color: white;
            border: 2px solid black;
            cursor: pointer;
            border-radius: 4px;
        }
        .reset-btn:hover {
            background: #ff2121;
        }
    </style>
</head>
<body>

<div class="game-container">
    <canvas id="gameCanvas" width="600" height="500"></canvas>
</div>

<div class="scoreboard">
    <div class="player-box">
        <div class="name" style="color: #27ae60;">혜혜</div>
        <div class="hp-bar-outer">
            <div id="hpBar1" class="hp-bar-inner"></div>
            <div id="hpText1" class="hp-text">250 / 250</div>
        </div>
    </div>
    <div class="player-box right">
        <div class="name" style="color: #27ae60;">릴고아</div>
        <div class="hp-bar-outer">
            <div id="hpBar2" class="hp-bar-inner" style="background-color: #2ecc71;"></div>
            <div id="hpText2" class="hp-text">250 / 250</div>
        </div>
    </div>
</div>

<button class="reset-btn" onclick="resetGame()">경기 다시 시작</button>

<script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    let isGameOver = false;
    let cracks = [];     // 벽에 부딪힐 때 생기는 크랙 자국들
    let effects = [];    // 스킬 파동 이펙트
    let chats = [];      // 상단 채팅 및 후원 메시지 로그

    // 가상의 프로필 이미지 생성용 아바타 (실제 이미지 로드 실패 시 대체 그리기용)
    let img1Loaded = false, img2Loaded = false;
    let avatar1 = new Image(); avatar1.src = "https://i.imgur.com/74u9rAx.png"; avatar1.onload = () => { img1Loaded = true; };
    let avatar2 = new Image(); avatar2.src = "https://i.imgur.com/82v9KtX.png"; avatar2.onload = () => { img2Loaded = true; };

    let ball1 = {
        x: 150, y: 250,
        vx: 1.5, vy: 1.2,   // 느린 속도
        radius: 35,
        hp: 250, maxHp: 250,
        name: "혜혜",
        cooldown: 0,
        skillTimer: 300,    // 약 5초마다 자동 스킬
        isSkill: false
    };

    let ball2 = {
        x: 450, y: 250,
        vx: -1.5, vy: -1.2, // 느린 속도
        radius: 35,
        hp: 250, maxHp: 250,
        name: "릴고아",
        cooldown: 0,
        skillTimer: 420,    // 약 7초마다 자동 스킬 (주기 다름)
        isSkill: false
    };

    // 초기 채팅 메시지 설정
    chats.push({ text: "🟢 ball_fight_korea님이 1,000원 후원함", sub: "기습적 무추위야! 릴고아님에겐 딜도 박히지도 않네" });
    
    // 무작위 대사 이벤트 추가 타이머
    let chatTimer = 0;
    const sampleChats = [
        "5초간 콥볼소우 흉내 내주세요",
        "즐거 같은데 빨리 본체 투혼!",
        "퍼가요~",
        "빨리 버튼 눌러주세요 현기증 난단 말이에요"
    ];

    function addCrack(x, y) {
        cracks.push({ x: x, y: y, size: Math.random() * 15 + 20 });
        if (cracks.length > 15) cracks.shift(); // 너무 많아지면 오래된 것 삭제
    }

    function triggerSkill(b, enemy) {
        enemy.hp -= 30;
        if (enemy.hp < 0) enemy.hp = 0;
        b.isSkill = true;
        setTimeout(() => { b.isSkill = false; }, 500);

        // 파동 이펙트 생성
        effects.push({ x: b.x, y: b.y, r: 10, maxR: 80, alpha: 1.0 });
        
        // 랜덤 채팅 추가
        chats.push({ text: "💬 " + b.name + " 스킬 발동!", sub: sampleChats[Math.floor(Math.random() * sampleChats.length)] });
        if (chats.length > 3) chats.shift();
    }

    function update() {
        if (isGameOver) return;

        // 채팅 타이머
        chatTimer++;
        if (chatTimer > 250) {
            chats.push({ text: "💬 시청자", sub: sampleChats[Math.floor(Math.random() * sampleChats.length)] });
            if (chats.length > 3) chats.shift();
            chatTimer = 0;
        }

        // 위치 이동
        ball1.x += ball1.vx;
        ball1.y += ball1.vy;
        ball2.x += ball2.vx;
        ball2.y += ball2.vy;

        // 벽 충돌 및 크랙 생성 (공 1)
        if (ball1.x - ball1.radius < 0) { ball1.x = ball1.radius; ball1.vx *= -1; addCrack(ball1.x, ball1.y); }
        if (ball1.x + ball1.radius > canvas.width) { ball1.x = canvas.width - ball1.radius; ball1.vx *= -1; addCrack(ball1.x, ball1.y); }
        if (ball1.y - ball1.radius < 0) { ball1.y = ball1.radius; ball1.vy *= -1; addCrack(ball1.x, ball1.y); }
        if (ball1.y + ball1.radius > canvas.height) { ball1.y = canvas.height - ball1.radius; ball1.vy *= -1; addCrack(ball1.x, ball1.y); }

        // 벽 충돌 및 크랙 생성 (공 2)
        if (ball2.x - ball2.radius < 0) { ball2.x = ball2.radius; ball2.vx *= -1; addCrack(ball2.x, ball2.y); }
        if (ball2.x + ball2.radius > canvas.width) { ball2.x = canvas.width - ball2.radius; ball2.vx *= -1; addCrack(ball2.x, ball2.y); }
        if (ball2.y - ball2.radius < 0) { ball2.y = ball2.radius; ball2.vy *= -1; addCrack(ball2.x, ball2.y); }
        if (ball2.y + ball2.radius > canvas.height) { ball2.y = canvas.height - ball2.radius; ball2.vy *= -1; addCrack(ball2.x, ball2.y); }

        // 스킬 타이머 감소 (서로 다름)
        ball1.skillTimer--;
        if (ball1.skillTimer <= 0) {
            triggerSkill(ball1, ball2);
            ball1.skillTimer = 320;
        }
        ball2.skillTimer--;
        if (ball2.skillTimer <= 0) {
            triggerSkill(ball2, ball1);
            ball2.skillTimer = 400;
        }

        if (ball1.cooldown > 0) ball1.cooldown--;
        if (ball2.cooldown > 0) ball2.cooldown--;

        // 공끼리 충돌
        let dx = ball2.x - ball1.x;
        let dy = ball2.y - ball1.y;
        let dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < ball1.radius + ball2.radius) {
            let tempVx = ball1.vx; let tempVy = ball1.vy;
            ball1.vx = ball2.vx; ball1.vy = ball2.vy;
            ball2.vx = tempVx; ball2.vy = tempVy;

            let overlap = (ball1.radius + ball2.radius) - dist;
            let angle = Math.atan2(dy, dx);
            ball1.x -= Math.cos(angle) * overlap / 2;
            ball1.y -= Math.sin(angle) * overlap / 2;
            ball2.x += Math.cos(angle) * overlap / 2;
            ball2.y += Math.sin(angle) * overlap / 2;

            if (ball1.cooldown === 0 && ball2.cooldown === 0) {
                ball1.hp -= 15;
                ball2.hp -= 15;
                ball1.cooldown = 30;
                ball2.cooldown = 30;
                if (ball1.hp < 0) ball1.hp = 0;
                if (ball2.hp < 0) ball2.hp = 0;
            }
        }

        // HTML UI 갱신
        document.getElementById("hpBar1").style.width = (ball1.hp / ball1.maxHp * 100) + "%";
        document.getElementById("hpText1.innerText = ball1.hp + " / 250";
        document.getElementById("hpBar2").style.width = (ball2.hp / ball2.maxHp * 100) + "%";
        document.getElementById("hpText2").innerText = ball2.hp + " / 250";

        if (ball1.hp <= 0 || ball2.hp <= 0) {
            isGameOver = true;
        }
    }

    function drawCrack(c) {
        ctx.save();
        ctx.strokeStyle = "#888888";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(c.x, c.y, c.size * 0.4, 0, Math.PI * 2);
        ctx.stroke();
        // 깨진 틈새 선들
        ctx.beginPath();
        ctx.moveTo(c.x, c.y); ctx.lineTo(c.x + c.size * 0.6, c.y - c.size * 0.5);
        ctx.moveTo(c.x, c.y); ctx.lineTo(c.x - c.size * 0.5, c.y + c.size * 0.4);
        ctx.moveTo(c.x, c.y); ctx.lineTo(c.x + c.size * 0.4, c.y + c.size * 0.5);
        ctx.stroke();
        ctx.restore();
    }

    function drawBall(b, imgLoaded, imgObj) {
        ctx.save();
        ctx.beginPath();
        let r = b.isSkill ? b.radius + 10 : b.radius;
        ctx.arc(b.x, b.y, r, 0, Math.PI * 2);
        ctx.clip();

        if (imgLoaded) {
            ctx.drawImage(imgObj, b.x - r, b.y - r, r * 2, r * 2);
        } else {
            ctx.fillStyle = "#ddd";
            ctx.fill();
        }
        ctx.restore();

        // 테두리
        ctx.beginPath();
        ctx.arc(b.x, b.y, r, 0, Math.PI * 2);
        ctx.lineWidth = b.isSkill ? 4 : 2;
        ctx.strokeStyle = b.isSkill ? "#ff0000" : "#27ae60";
        ctx.stroke();

        // 이름 텍스트
        ctx.fillStyle = "black";
        ctx.font = "bold 13px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(b.name, b.x, b.y - r - 6);
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 벽 크랙 그리기
        cracks.forEach(c => drawCrack(c));

        // 상단 채팅/후원 UI 박스 렌더링 (영상 속 디자인 모사)
        if (chats.length > 0) {
            ctx.save();
            ctx.fillStyle = "rgba(240, 240, 240, 0.9)";
            ctx.fillRect(80, 10, 440, 45);
            ctx.strokeStyle = "#ccc";
            ctx.strokeRect(80, 10, 440, 45);

            ctx.fillStyle = "#333";
            ctx.font = "12px sans-serif";
            ctx.textAlign = "left";
            ctx.fillText(chats[chats.length - 1].text, 90, 26);
            ctx.fillStyle = "#666";
            ctx.fillText(chats[chats.length - 1].sub, 90, 44);
            ctx.restore();
        }

        // 스킬 파동 이펙트
        for (let i = effects.length - 1; i >= 0; i--) {
            let ef = effects[i];
            ctx.save();
            ctx.beginPath();
            ctx.arc(ef.x, ef.y, ef.r, 0, Math.PI * 2);
            ctx.strokeStyle = "rgba(255, 0, 0, " + ef.alpha + ")";
            ctx.lineWidth = 3;
            ctx.stroke();
            ctx.restore();

            ef.r += 2;
            ef.alpha -= 0.03;
            if (ef.alpha <= 0) effects.splice(i, 1);
        }

        // 공 그리기
        drawBall(ball1, img1Loaded, avatar1);
        drawBall(ball2, img2Loaded, avatar2);

        // 게임 종료 시 승리 문구 및 왕관
        if (isGameOver) {
            ctx.fillStyle = "rgba(255, 255, 255, 0.85)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "black";
            ctx.font = "bold 30px sans-serif";
            ctx.textAlign = "center";
            let winner = ball1.hp > 0 ? ball1.name : (ball2.hp > 0 ? ball2.name : "무승부");
            ctx.fillText("👑 " + winner + " 승리! 👑", canvas.width / 2, canvas.height / 2);
        }
    }

    function resetGame() {
        ball1.hp = 250; ball2.hp = 250;
        ball1.x = 150; ball1.y = 250;
        ball2.x = 450; ball2.y = 250;
        ball1.skillTimer = 300; ball2.skillTimer = 420;
        cracks = [];
        effects = [];
        isGameOver = false;
    }

    function loop() {
        update();
        draw();
        requestAnimationFrame(loop);
    }

    loop();
</script>

</body>
</html>
"""

st.components.v1.html(game_html, height=620)
