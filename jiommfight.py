import streamlit as st

st.set_page_config(page_title="공 싸움 스킬 게임", page_icon="⚔️", layout="centered")

st.title("⚔️ 공 배틀 + 스킬 시스템 게임")
st.write("공 속도가 느려지고 크기가 커졌으며, 체력바 아래의 **[스킬 사용] 버튼**으로 특수 공격을 쓸 수 있습니다!")

game_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Ball Battle with Skills</title>
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

        .skill-container {
            margin-top: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .skill-btn {
            padding: 4px 10px;
            font-size: 12px;
            font-weight: bold;
            background-color: #6c757d;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .skill-btn.ready {
            background-color: #007bff;
            cursor: pointer;
        }
        .skill-btn.ready:hover {
            background-color: #0056b3;
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
            <div class="skill-container">
                <span style="font-size: 12px;">스킬 대기중...</span>
                <button id="skillBtn1" class="skill-btn" onclick="useSkill(1)">스킬 (5초)</button>
            </div>
        </div>

        <div style="font-weight: bold; font-size: 20px; display:flex; align-items:center;">VS</div>

        <div class="player-panel right">
            <span style="font-weight: bold; color: #1c83e1;">릴고아</span> (HP: <span id="hp2Text">250</span>)
            <div class="hp-bar-container">
                <div id="hpBar2" class="hp-bar" style="width: 100%;"></div>
            </div>
            <div class="skill-container style='flex-direction: row-reverse;'">
                <button id="skillBtn2" class="skill-btn" onclick="useSkill(2)">스킬 (5초)</button>
                <span style="font-size: 12px;">스킬 대기중...</span>
            </div>
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

    // 공 설정 (속도 느리게: vx, vy 낮춤 / 크기 크게: radius 키움)
    let ball1 = {
        x: 150, y: 300,
        vx: 1.8, vy: 1.5,   // 속도 감소
        radius: 45,         // 크기 증가 (기존 30 -> 45)
        hp: 250, maxHp: 250,
        name: "혜혜", color: "#ff4b4b",
        cooldown: 0,
        skillCooldown: 300  // 300프레임 (약 5초 뒤 스킬 활성화)
    };

    let ball2 = {
        x: 450, y: 300,
        vx: -1.8, vy: -1.5, // 속도 감소
        radius: 45,         // 크기 증가
        hp: 250, maxHp: 250,
        name: "릴고아", color: "#1c83e1",
        cooldown: 0,
        skillCooldown: 300
    };

    function useSkill(player) {
        if (isGameOver) return;
        let b = (player === 1) ? ball1 : ball2;
        let enemy = (player === 1) ? ball2 : ball1;

        if (b.skillCooldown <= 0) {
            // 스킬 효과: 상대에게 즉시 40의 고정 데미지 + 잠시 속도 폭발
            enemy.hp -= 40;
            if (enemy.hp < 0) enemy.hp = 0;

            // 스킬 사용 후 쿨타임 재충전 (다시 8초 뒤 사용 가능)
            b.skillCooldown = 480; 
            
            // 시각적 효과 부여 (스킬 쓴 공은 일시적으로 커짐)
            b.radius += 10;
            setTimeout(() => { b.radius -= 10; }, 1000);
        }
    }

    function update() {
        if (isGameOver) return;

        // 위치 이동
        ball1.x += ball1.vx;
        ball1.y += ball1.vy;
        ball2.x += ball2.vx;
        ball2.y += ball2.vy;

        // 벽 충돌 처리 (공 1)
        if (ball1.x - ball1.radius < 0) { ball1.x = ball1.radius; ball1.vx *= -1; }
        if (ball1.x + ball1.radius > canvas.width) { ball1.x = canvas.width - ball1.radius; ball1.vx *= -1; }
        if (ball1.y - ball1.radius < 0) { ball1.y = ball1.radius; ball1.vy *= -1; }
        if (ball1.y + ball1.radius > canvas.height) { ball1.y = canvas.height - ball1.radius; ball1.vy *= -1; }

        // 벽 충돌 처리 (공 2)
        if (ball2.x - ball2.radius < 0) { ball2.x = ball2.radius; ball2.vx *= -1; }
        if (ball2.x + ball2.radius > canvas.width) { ball2.x = canvas.width - ball2.radius; ball2.vx *= -1; }
        if (ball2.y - ball2.radius < 0) { ball2.y = ball2.radius; ball2.vy *= -1; }
        if (ball2.y + ball2.radius > canvas.height) { ball2.y = canvas.height - ball2.radius; ball2.vy *= -1; }

        // 데미지 쿨다운 및 스킬 쿨타임 감소
        if (ball1.cooldown > 0) ball1.cooldown--;
        if (ball2.cooldown > 0) ball2.cooldown--;

        if (ball1.skillCooldown > 0) ball1.skillCooldown--;
        if (ball2.skillCooldown > 0) ball2.skillCooldown--;

        // 스킬 버튼 상태 업데이트 UI 반영
        let btn1 = document.getElementById("skillBtn1");
        if (ball1.skillCooldown <= 0) {
            btn1.innerText = "⚡ 스킬 사용!";
            btn1.className = "skill-btn ready";
        } else {
            let sec = Math.ceil(ball1.skillCooldown / 60);
            btn1.innerText = `대기중 (${sec}초)`;
            btn1.className = "skill-btn";
        }

        let btn2 = document.getElementById("skillBtn2");
        if (ball2.skillCooldown <= 0) {
            btn2.innerText = "⚡ 스킬 사용!";
            btn2.className = "skill-btn ready";
        } else {
            let sec = Math.ceil(ball2.skillCooldown / 60);
            btn2.innerText = `대기중 (${sec}초)`;
            btn2.className = "skill-btn";
        }

        // 공끼리 충돌 계산
        let dx = ball2.x - ball1.x;
        let dy = ball2.y - ball1.y;
        let distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < ball1.radius + ball2.radius) {
            // 물리 탄성 반사
            let tempVx = ball1.vx;
            let tempVy = ball1.vy;
            ball1.vx = ball2.vx;
            ball1.vy = ball2.vy;
            ball2.vx = tempVx;
            ball2.vy = tempVy;

            // 겹침 방지 밀어내기
            let overlap = (ball1.radius + ball2.radius) - distance;
            let angle = Math.atan2(dy, dx);
            ball1.x -= Math.cos(angle) * overlap / 2;
            ball1.y -= Math.sin(angle) * overlap / 2;
            ball2.x += Math.cos(angle) * overlap / 2;
            ball2.y += Math.sin(angle) * overlap / 2;

            // 일반 충돌 데미지
            if (ball1.cooldown === 0 && ball2.cooldown === 0) {
                ball1.hp -= 15;
                ball2.hp -= 15;
                ball1.cooldown = 25;
                ball2.cooldown = 25;

                if (ball1.hp < 0) ball1.hp = 0;
                if (ball2.hp < 0) ball2.hp = 0;
            }
        }

        // UI 텍스트 & 체력바 갱신
        document.getElementById("hp1Text").innerText = ball1.hp;
        document.getElementById("hp2Text").innerText = ball2.hp;
        document.getElementById("hpBar1").style.width = (ball1.hp / ball1.maxHp * 100) + "%";
        document.getElementById("hpBar2").style.width = (ball2.hp / ball2.maxHp * 100) + "%";

        // 게임 종료 체크
        if (ball1.hp <= 0 || ball2.hp <= 0) {
            isGameOver = true;
        }
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 공 1 그리기 (혜혜)
        ctx.beginPath();
        ctx.arc(ball1.x, ball1.y, ball1.radius, 0, Math.PI * 2);
        ctx.fillStyle = ball1.color;
        ctx.fill();
        ctx.lineWidth = 3;
        ctx.strokeStyle = "#333";
        ctx.stroke();
        ctx.closePath();

        ctx.fillStyle = "#333";
        ctx.font = "bold 15px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(ball1.name, ball1.x, ball1.y - ball1.radius - 8);

        // 공 2 그리기 (릴고아)
        ctx.beginPath();
        ctx.arc(ball2.x, ball2.y, ball2.radius, 0, Math.PI * 2);
        ctx.fillStyle = ball2.color;
        ctx.fill();
        ctx.lineWidth = 3;
        ctx.strokeStyle = "#333";
        ctx.stroke();
        ctx.closePath();

        ctx.fillText(ball2.name, ball2.x, ball2.y - ball2.radius - 8);

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
        ball1.skillCooldown = 300;
        ball2.skillCooldown = 300;
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
