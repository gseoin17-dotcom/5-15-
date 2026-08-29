import streamlit as st

st.set_page_config(page_title="Ball Fight Simulator", page_icon="💥", layout="centered")

game_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Ball Fight</title>
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
            width: 750px;
            margin: 0 auto;
            border: 4px solid black;
            background: #ffffff;
            position: relative;
            overflow: hidden;
        }
        canvas {
            display: block;
            background: #ffffff;
        }
        .scoreboard {
            width: 750px;
            margin: 12px auto 0 auto;
            display: flex;
            justify-content: space-between;
            border: 2px solid black;
            padding: 10px;
            background: #f9f9f9;
            box-sizing: border-box;
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
            height: 24px;
            margin-top: 5px;
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
            line-height: 20px;
        }
        .reset-btn {
            margin-top: 15px;
            padding: 10px 20px;
            font-weight: bold;
            font-size: 14px;
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
    <canvas id="gameCanvas" width="750" height="600"></canvas>
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
    let cracks = [];     
    let particles = [];
    let shockwaves = [];
    let screenShake = 0;

    // 공 속도를 훨씬 더 느리게 설정
    let ball1 = {
        x: 200, y: 300, vx: 0.55, vy: 0.45, radius: 40,
        hp: 250, maxHp: 250, name: "혜혜", color: "#3498db", cooldown: 0, skillTimer: 350, isSkill: false
    };

    let ball2 = {
        x: 550, y: 300, vx: -0.55, vy: -0.45, radius: 40,
        hp: 250, maxHp: 250, name: "릴고아", color: "#e74c3c", cooldown: 0, skillTimer: 450, isSkill: false
    };

    // 벽 충돌 시 진짜 벽이 깨진 듯한 정교한 크랙 생성
    function addCrack(x, y) {
        cracks.push({
            x: x, 
            y: y, 
            points: [
                {dx: -15, dy: -10}, {dx: 10, dy: -20}, {dx: 25, dy: 5},
                {dx: 15, dy: 20}, {dx: -10, dy: 25}, {dx: -20, dy: 5}
            ],
            size: Math.random() * 15 + 25
        });
        if (cracks.length > 12) cracks.shift();

        // 파편 파티클 튀는 효과
        for(let i=0; i<6; i++) {
            particles.push({
                x: x, y: y,
                vx: (Math.random() - 0.5) * 3,
                vy: (Math.random() - 0.5) * 3,
                size: Math.random() * 4 + 2,
                alpha: 1.0
            });
        }
    }

    // 개쩌는 궁극기 스킬 연출
    function triggerEpicSkill(b, enemy) {
        enemy.hp -= 45;
        if (enemy.hp < 0) enemy.hp = 0;
        b.isSkill = true;
        screenShake = 20; // 화면 흔들림

        setTimeout(() => { b.isSkill = false; }, 800);

        // 강력한 충격파 링 생성
        shockwaves.push({ x: b.x, y: b.y, r: 10, maxR: 150, alpha: 1.0, color: b.color });

        // 화려한 폭발 파티클 생성
        for(let i=0; i<30; i++) {
            let angle = Math.random() * Math.PI * 2;
            let speed = Math.random() * 4 + 2;
            particles.push({
                x: b.x, y: b.y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                size: Math.random() * 6 + 3,
                color: b.color,
                alpha: 1.0
            });
        }
    }

    function update() {
        if (isGameOver) return;

        if (screenShake > 0) screenShake--;

        ball1.x += ball1.vx; ball1.y += ball1.vy;
        ball2.x += ball2.vx; ball2.y += ball2.vy;

        // 벽 충돌 (좌, 우, 상, 하)
        if (ball1.x - ball1.radius < 0) { ball1.x = ball1.radius; ball1.vx *= -1; addCrack(ball1.x, ball1.y); }
        if (ball1.x + ball1.radius > canvas.width) { ball1.x = canvas.width - ball1.radius; ball1.vx *= -1; addCrack(ball1.x, ball1.y); }
        if (ball1.y - ball1.radius < 0) { ball1.y = ball1.radius; ball1.vy *= -1; addCrack(ball1.x, ball1.y); }
        if (ball1.y + ball1.radius > canvas.height) { ball1.y = canvas.height - ball1.radius; ball1.vy *= -1; addCrack(ball1.x, ball1.y); }

        if (ball2.x - ball2.radius < 0) { ball2.x = ball2.radius; ball2.vx *= -1; addCrack(ball2.x, ball2.y); }
        if (ball2.x + ball2.radius > canvas.width) { ball2.x = canvas.width - ball2.radius; ball2.vx *= -1; addCrack(ball2.x, ball2.y); }
        if (ball2.y - ball2.radius < 0) { ball2.y = ball2.radius; ball2.vy *= -1; addCrack(ball2.x, ball2.y); }
        if (ball2.y + ball2.radius > canvas.height) { ball2.y = canvas.height - ball2.radius; ball2.vy *= -1; addCrack(ball2.x, ball2.y); }

        ball1.skillTimer--;
        if (ball1.skillTimer <= 0) { triggerEpicSkill(ball1, ball2); ball1.skillTimer = 350; }
        ball2.skillTimer--;
        if (ball2.skillTimer <= 0) { triggerEpicSkill(ball2, ball1); ball2.skillTimer = 450; }

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
                ball1.hp -= 15; ball2.hp -= 15;
                ball1.cooldown = 40; ball2.cooldown = 40;
                if (ball1.hp < 0) ball1.hp = 0;
                if (ball2.hp < 0) ball2.hp = 0;
            }
        }

        document.getElementById("hpBar1").style.width = (ball1.hp / ball1.maxHp * 100) + "%";
        document.getElementById("hpText1").innerText = ball1.hp + " / 250";
        document.getElementById("hpBar2").style.width = (ball2.hp / ball2.maxHp * 100) + "%";
        document.getElementById("hpText2").innerText = ball2.hp + " / 250";

        if (ball1.hp <= 0 || ball2.hp <= 0) isGameOver = true;
    }

    function drawCrack(c) {
        ctx.save();
        ctx.strokeStyle = "#555555";
        ctx.lineWidth = 2.5;
        ctx.fillStyle = "rgba(200, 200, 200, 0.5)";
        
        ctx.beginPath();
        ctx.moveTo(c.x, c.y);
        c.points.forEach(p => ctx.lineTo(c.x + p.dx, c.y + p.dy));
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
        ctx.restore();
    }

    function drawBall(b) {
        ctx.save();
        let r = b.isSkill ? b.radius + 15 : b.radius;
        
        // 스킬 시전 시 오라 효과
        if (b.isSkill) {
            ctx.beginPath();
            ctx.arc(b.x, b.y, r + 10, 0, Math.PI * 2);
            ctx.fillStyle = b.color === "#3498db" ? "rgba(52, 152, 219, 0.3)" : "rgba(231, 76, 60, 0.3)";
            ctx.fill();
        }

        ctx.beginPath();
        ctx.arc(b.x, b.y, r, 0, Math.PI * 2);
        ctx.fillStyle = b.color;
        ctx.fill();
        ctx.lineWidth = b.isSkill ? 5 : 3;
        ctx.strokeStyle = b.isSkill ? "#f1c40f" : "#111111";
        ctx.stroke();
        ctx.closePath();

        ctx.fillStyle = "black";
        ctx.font = "bold 15px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(b.name, b.x, b.y - r - 8);
        ctx.restore();
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        ctx.save();
        // 화면 흔들림 적용
        if (screenShake > 0) {
            let shakeX = (Math.random() - 0.5) * 8;
            let shakeY = (Math.random() - 0.5) * 8;
            ctx.translate(shakeX, shakeY);
        }

        // 벽 크랙 렌더링
        cracks.forEach(c => drawCrack(c));

        // 충격파 렌더링
        for (let i = shockwaves.length - 1; i >= 0; i--) {
            let sw = shockwaves[i];
            ctx.save();
            ctx.beginPath();
            ctx.arc(sw.x, sw.y, sw.r, 0, Math.PI * 2);
            ctx.strokeStyle = sw.color;
            ctx.lineWidth = 5;
            ctx.globalAlpha = sw.alpha;
            ctx.stroke();
            ctx.restore();

            sw.r += 4;
            sw.alpha -= 0.02;
            if (sw.alpha <= 0) shockwaves.splice(i, 1);
        }

        // 파티클 렌더링
        for (let i = particles.length - 1; i >= 0; i--) {
            let p = particles[i];
            ctx.save();
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fillStyle = p.color || "#777";
            ctx.globalAlpha = p.alpha;
            ctx.fill();
            ctx.restore();

            p.x += p.vx;
            p.y += p.vy;
            p.alpha -= 0.02;
            if (p.alpha <= 0) particles.splice(i, 1);
        }

        drawBall(ball1);
        drawBall(ball2);

        ctx.restore();

        // 게임 종료 시 왕관과 승리 메시지
        if (isGameOver) {
            ctx.fillStyle = "rgba(255, 255, 255, 0.9)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "black";
            ctx.font = "bold 38px sans-serif";
            ctx.textAlign = "center";
            let winner = ball1.hp > 0 ? ball1.name : (ball2.hp > 0 ? ball2.name : "무승부");
            ctx.fillText("👑 " + winner + " 승리! 👑", canvas.width / 2, canvas.height / 2);
        }
    }

    function resetGame() {
        ball1.hp = 250; ball2.hp = 250;
        ball1.x = 200; ball1.y = 300;
        ball2.x = 550; ball2.y = 300;
        ball1.skillTimer = 350; ball2.skillTimer = 450;
        cracks = []; particles = []; shockwaves = []; isGameOver = false;
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

st.components.v1.html(game_html, height=720)
