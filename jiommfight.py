import streamlit as st

st.set_page_config(page_title="자동 스킬 공 싸움 게임", page_icon="⚡", layout="centered")

st.title("⚡ 자동 스킬 & 애니메이션 공 배틀 게임")
st.write("공이 스스로 움직이며, 각자 다른 주기(혜혜: 6초, 릴고아: 8초)로 자동 스킬을 쓰고 화려한 충돌/스킬 이펙트가 발생합니다!")

game_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Auto Skill Ball Battle</title>
    <style>
        body {
            background-color: #0e1117;
            color: white;
            text-align: center;
            font-family: 'Malgun Gothic', sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 650px;
            margin: 0 auto;
        }
        .scoreboard {
            background: #1e1e2f;
            padding: 15px 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            display: flex;
            justify-content: space-between;
        }
        .player-panel {
            width: 45%;
            text-align: left;
        }
        .player-panel.right {
            text-align: right;
        }
        .hp-bar-container {
            background: #333;
            border-radius: 5px;
            overflow: hidden;
            height: 18px;
            margin-top: 5px;
            border: 1px solid #555;
        }
        .hp-bar {
            height: 100%;
            width: 100%;
            transition: width 0.1s ease;
        }
        #hpBar1 { background-color: #28a745; }
        #hpBar2 { background-color: #ffc107; }

        .skill-status {
            margin-top: 6px;
            font-size: 13px;
            font-weight: bold;
            color: #00d2ff;
        }

        canvas {
            background: #ffffff;
            display: block;
            margin: 0 auto;
            border: 3px solid #333;
            border-radius: 8px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        }
        .btn {
            margin-top: 15px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            background-color: #ff4b4b;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #ff2121;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="scoreboard">
        <div class="player-panel">
            <span style="font-weight: bold; color: #ff4b4b;">혜혜</span> (HP: <span id="hp1Text">250</span>)
            <div class="hp-bar-container">
                <div id="hpBar1" class="hp-bar" style="width: 100%;"></div>
            </div>
            <div class="skill-status" id="skillStatus1">스킬 충전중 (6초 주기)</div>
        </div>

        <div style="font-weight: bold; font-size: 20px; display:flex; align-items:center;">VS</div>

        <div class="player-panel right">
            <span style="font-weight: bold; color: #1c83e1;">릴고아</span> (HP: <span id="hp2Text">250</span>)
            <div class="hp-bar-container">
                <div id="hpBar2" class="hp-bar" style="width: 100%;"></div>
            </div>
            <div class="skill-status" id="skillStatus2" style="text-align: right;">스킬 충전중 (8초 주기)</div>
        </div>
    </div>

    <canvas id="gameCanvas" width="600" height="600"></canvas>
    <br>
    <button class="btn" onclick="resetGame()">게임 다시 시작</button>
</div>

<script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    let isGameOver = false;
    let effects = []; // 스킬/충돌 이펙트 애니메이션 배열

    let ball1 = {
        x: 150, y: 300,
        vx: 1.8, vy: 1.5,
        radius: 45,
        hp: 250, maxHp: 250,
        name: "혜혜", color: "#ff4b4b",
        cooldown: 0,
        skillMaxTime: 360,     // 6초 주기 (60프레임 * 6)
        skillTimer: 360,
        isUsingSkill: false
    };

    let ball2 = {
        x: 450, y: 300,
        vx: -1.8, vy: -1.5,
        radius: 45,
        hp: 250, maxHp: 250,
        name: "릴고아", color: "#1c83e1",
        cooldown: 0,
        skillMaxTime: 480,     // 8초 주기 (60프레임 * 8) - 서로 다름!
        skillTimer: 480,
        isUsingSkill: false
    };

    // 화려한 파동 이펙트 추가 함수
    function addEffect(x, y, color) {
        effects.push({
            x: x,
            y: y,
            radius: 10,
            maxRadius: 70,
            color: color,
            alpha: 1.0
        });
    }

    function triggerAutoSkill(b, enemy) {
        // 스킬 발동 시 데미지 및 이펙트
        enemy.hp -= 35;
        if (enemy.hp < 0) enemy.hp = 0;

        // 애니메이션 효과 추가
        addEffect(b.x, b.y, b.color);

        // 스킬 사용 모션 (잠시 커졌다가 돌아오기)
        b.isUsingSkill = true;
        setTimeout(() => { b.isUsingSkill = false; }, 400);
    }

    function update() {
        if (isGameOver) return;

        // 위치 이동
        ball1.x += ball1.vx;
        ball1.y += ball1.vy;
        ball2.x += ball2.vx;
        ball2.y += ball2.vy;

        // 벽 충돌 (공 1)
        if (ball1.x - ball1.radius < 0) { ball1.x = ball1.radius; ball1.vx *= -1; }
        if (ball1.x + ball1.radius > canvas.width) { ball1.x = canvas.width - ball1.radius; ball1.vx *= -1; }
        if (ball1.y - ball1.radius < 0) { ball1.y = ball1.radius; ball1.vy *= -1; }
        if (ball1.y + ball1.radius > canvas.height) { ball1.y = canvas.height - ball1.radius; ball1.vy *= -1; }

        // 벽 충돌 (공 2)
        if (ball2.x - ball2.radius < 0) { ball2.x = ball2.radius; ball2.vx *= -1; }
        if (ball2.x + ball2.radius > canvas.width) { ball2.x = canvas.width - ball2.radius; ball2.vx *= -1; }
        if (ball2.y - ball2.radius < 0) { ball2.y = ball2.radius; ball2.vy *= -1; }
        if (ball2.y + ball2.radius > canvas.height) { ball2.y = canvas.height - ball2.radius; ball2.vy *= -1; }

        // 데미지 쿨다운 감소
        if (ball1.cooldown > 0) ball1.cooldown--;
        if (ball2.cooldown > 0) ball2.cooldown--;

        // 자동 스킬 타이머 감소 및 발동 (서로 다른 주기)
        ball1.skillTimer--;
        if (ball1.skillTimer <= 0) {
            triggerAutoSkill(ball1, ball2);
            ball1.skillTimer = ball1.skillMaxTime; // 타이머 리셋
        }

        ball2.skillTimer--;
        if (ball2.skillTimer <= 0) {
            triggerAutoSkill(ball2, ball1);
            ball2.skillTimer = ball2.skillMaxTime; // 타이머 리셋
        }

        // UI 갱신 (상단 스킬 충전 표시)
        let s1Sec = (ball1.skillTimer / 60).toFixed(1);
        document.getElementById("skillStatus1").innerText = `⚡ 스킬 대기중 (${s1Sec}초)`;
        
        let s2Sec = (ball2.skillTimer / 60).toFixed(1);
        document.getElementById("skillStatus2").innerText = `⚡ 스킬 대기중 (${s2Sec}초)`;

        // 공끼리 충돌 계산
        let dx = ball2.x - ball1.x;
        let dy = ball2.y - ball1.y;
        let distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < ball1.radius + ball2.radius) {
            let tempVx = ball1.vx;
            let tempVy = ball1.vy;
            ball1.vx = ball2.vx;
            ball1.vy = ball2.vy;
            ball2.vx = tempVx;
            ball2.vy = tempVy;

            let overlap = (ball1.radius + ball2.radius) - distance;
            let angle = Math.atan2(dy, dx);
            ball1.x -= Math.cos(angle) * overlap / 2;
            ball1.y -= Math.sin(angle) * overlap / 2;
            ball2.x += Math.cos(angle) * overlap / 2;
            ball2.y += Math.sin(angle) * overlap / 2;

            // 일반 충돌 시에도 작은 파동 이펙트 추가
            if (ball1.cooldown === 0 && ball2.cooldown === 0) {
                ball1.hp -= 15;
                ball2.hp -= 15;
                ball1.cooldown = 25;
                ball2.cooldown = 25;

                addEffect((ball1.x + ball2.x)/2, (ball1.y + ball2.y)/2, "#888888");

                if (ball1.hp < 0) ball1.hp = 0;
                if (ball2.hp < 0) ball2.hp = 0;
            }
        }

        // HP UI 갱신
        document.getElementById("hp1Text").innerText = ball1.hp;
        document.getElementById("hp2Text").innerText = ball2.hp;
        document.getElementById("hpBar1").style.width = (ball1.hp / ball1.maxHp * 100) + "%";
        document.getElementById("hpBar2").style.width = (ball2.hp / ball2.maxHp * 100) + "%";

        if (ball1.hp <= 0 || ball2.hp <= 0) {
            isGameOver = true;
        }
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 이펙트 애니메이션 그리기 (파동 퍼지는 효과)
        for (let i = effects.length - 1; i >= 0; i--) {
            let eff = effects[i];
            ctx.beginPath();
            ctx.arc(eff.x, eff.y, eff.radius, 0, Math.PI * 2);
            ctx.strokeStyle = eff.color;
            ctx.lineWidth = 4;
            ctx.globalAlpha = eff.alpha;
            ctx.stroke();
            ctx.closePath();

            // 퍼지면서 투명해짐
            eff.radius += 2.5;
            eff.alpha -= 0.03;
            if (eff.alpha <= 0 || eff.radius >= eff.maxRadius) {
                effects.splice(i, 1);
            }
        }
        ctx.globalAlpha = 1.0; // 투명도 초기화

        // 공 1 그리기 (혜혜) - 스킬 사용 시 크기 확장 모션
        let r1 = ball1.isUsingSkill ? ball1.radius + 15 : ball1.radius;
        ctx.beginPath();
        ctx.arc(ball1.x, ball1.y, r1, 0, Math.PI * 2);
        ctx.fillStyle = ball1.color;
        ctx.fill();
        ctx.lineWidth = ball1.isUsingSkill ? 6 : 3;
        ctx.strokeStyle = ball1.isUsingSkill ? "#ffeb3b" : "#333";
        ctx.stroke();
        ctx.closePath();

        ctx.fillStyle = "#333";
        ctx.font = "bold 15px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(ball1.name, ball1.x, ball1.y - r1 - 8);

        // 공 2 그리기 (릴고아) - 스킬 사용 시 크기 확장 모션
        let r2 = ball2.isUsingSkill ? ball2.radius + 15 : ball2.radius;
        ctx.beginPath();
        ctx.arc(ball2.x, ball2.y, r2, 0, Math.PI * 2);
        ctx.fillStyle = ball2.color;
        ctx.fill();
        ctx.lineWidth = ball2.isUsingSkill ? 6 : 3;
        ctx.strokeStyle = ball2.isUsingSkill ? "#ffeb3b" : "#333";
        ctx.stroke();
        ctx.closePath();

        ctx.fillText(ball2.name, ball2.x, ball2.y - r2 - 8);

        // 게임 종료 화면
        if (isGameOver) {
            ctx.fillStyle = "rgba(0, 0, 0, 0.7)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 32px sans-serif";
            ctx.textAlign = "center";
            let winner = ball1.hp > 0 ? ball1.name : (ball2.hp > 0 ? ball2.name : "무승부");
            ctx.fillText("👑 " + winner + " 승리! 👑", canvas.width / 2, canvas.height / 2 - 20);
            
            ctx.font = "18px sans-serif";
            ctx.fillText("아래 '게임 다시 시작' 버튼을 눌러주세요.", canvas.width / 2, canvas.height / 2 + 20);
        }
    }

    function resetGame() {
        ball1.hp = 250;
        ball2.hp = 250;
        ball1.x = 150; ball1.y = 300;
        ball2.x = 450; ball2.y = 300;
        ball1.skillTimer = ball1.skillMaxTime;
        ball2.skillTimer = ball2.skillMaxTime;
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

st.components.v1.html(game_html, height=760)
