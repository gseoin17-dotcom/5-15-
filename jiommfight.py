import streamlit as st

st.set_page_config(page_title="공 싸움 게임", page_icon="⚔️", layout="centered")

st.title("⚔️ 공 배틀 시뮬레이션 게임")
st.write("영상의 게임 규칙처럼, 두 공이 부딪힐 때마다 데미지가 닳고 체력이 0이 되면 승자가 결정됩니다!")

# HTML5 Canvas + JavaScript 기반의 실시간 배틀 게임
game_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Ball Battle Game</title>
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
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #1e1e2f;
            padding: 15px 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        }
        .player-info {
            width: 45%;
            text-align: left;
        }
        .player-info.right {
            text-align: right;
        }
        .hp-bar-container {
            background: #333;
            border-radius: 5px;
            overflow: hidden;
            height: 20px;
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
        <div class="player-info">
            <span style="font-weight: bold; color: #ff4b4b;">혜혜</span> (HP: <span id="hp1Text">250</span> / 250)
            <div class="hp-bar-container">
                <div id="hpBar1" class="hp-bar" style="width: 100%;"></div>
            </div>
        </div>
        <div style="font-weight: bold; font-size: 20px;">VS</div>
        <div class="player-info right">
            <span style="font-weight: bold; color: #1c83e1;">릴고아</span> (HP: <span id="hp2Text">250</span> / 250)
            <div class="hp-bar-container">
                <div id="hpBar2" class="hp-bar" style="width: 100%;"></div>
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

    // 게임 상태 변수
    let isGameOver = false;

    let ball1 = {
        x: 150,
        y: 300,
        vx: 4,
        vy: 3.5,
        radius: 30,
        hp: 250,
        maxHp: 250,
        name: "혜혜",
        color: "#ff4b4b",
        cooldown: 0
    };

    let ball2 = {
        x: 450,
        y: 300,
        vx: -4,
        vy: -3.5,
        radius: 30,
        hp: 250,
        maxHp: 250,
        name: "릴고아",
        color: "#1c83e1",
        cooldown: 0
    };

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

        // 쿨다운 감소
        if (ball1.cooldown > 0) ball1.cooldown--;
        if (ball2.cooldown > 0) ball2.cooldown--;

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

            // 데미지 처리 (영상처럼 부딪힐 때마다 HP 차감)
            if (ball1.cooldown === 0 && ball2.cooldown === 0) {
                ball1.hp -= 20;
                ball2.hp -= 20;
                ball1.cooldown = 20; // 연속 데미지 방지 딜레이
                ball2.cooldown = 20;

                if (ball1.hp < 0) ball1.hp = 0;
                if (ball2.hp < 0) ball2.hp = 0;
            }
        }

        // UI 갱신
        document.getElementById("hp1Text").innerText = ball1.hp;
        document.getElementById("hp2Text").innerText = ball2.hp;
        document.getElementById("hpBar1").style.width = (ball1.hp / ball1.maxHp * 100) + "%";
        document.getElementById("hpBar2").style.width = (ball2.hp / ball2.maxHp * 100) + "%";

        // 게임 종료 조건 체크
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

        // 공 1 이름 텍스트
        ctx.fillStyle = "#333";
        ctx.font = "bold 14px sans-serif";
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

        // 공 2 이름 텍스트
        ctx.fillText(ball2.name, ball2.x, ball2.y - ball2.radius - 8);

        // 게임 종료 시 승리 문구 출력
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
        ball1.x = 150;
        ball1.y = 300;
        ball2.x = 450;
        ball2.y = 300;
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

# Streamlit에 컴포넌트 렌더링
st.components.v1.html(game_html, height=720)
