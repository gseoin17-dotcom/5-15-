import streamlit as st

st.set_page_config(page_title="공 싸움 게임", page_icon="⚽", layout="centered")

st.title("⚔️ 공끼리 충돌 데미지 시뮬레이션")
st.write("두 공이 화면 안에서 움직이며 서로 부딪힐 때 체력이 닳는 게임입니다.")

# HTML5 Canvas와 JavaScript를 활용한 실시간 물리/충돌 게임 코드
game_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Ball Fight</title>
    <style>
        body {
            background-color: #0e1117;
            color: white;
            text-align: center;
            font-family: sans-serif;
            margin: 0;
            padding: 0;
        }
        canvas {
            background: #1e1e2f;
            display: block;
            margin: 20px auto;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        }
        .ui {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

    <div class="ui">
        🔴 공 1 HP: <span id="hp1">100</span> &nbsp;&nbsp;&nbsp;&nbsp; 🔵 공 2 HP: <span id="hp2">100</span>
    </div>

    <canvas id="gameCanvas" width="600" height="400"></canvas>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        // 공 객체 정의
        let ball1 = {
            x: 150,
            y: 200,
            vx: 3,
            vy: 2,
            radius: 25,
            color: "#ff4b4b",
            hp: 100,
            maxHp: 100,
            cooldown: 0
        };

        let ball2 = {
            x: 450,
            y: 200,
            vx: -3,
            vy: -2,
            radius: 25,
            color: "#1c83e1",
            hp: 100,
            maxHp: 100,
            cooldown: 0
        };

        function update() {
            // 위치 업데이트
            ball1.x += ball1.vx;
            ball1.y += ball1.vy;
            ball2.x += ball2.vx;
            ball2.y += ball2.vy;

            // 벽 충돌 (공 1)
            if (ball1.x - ball1.radius < 0 || ball1.x + ball1.radius > canvas.width) ball1.vx *= -1;
            if (ball1.y - ball1.radius < 0 || ball1.y + ball1.radius > canvas.height) ball1.vy *= -1;

            // 벽 충돌 (공 2)
            if (ball2.x - ball2.radius < 0 || ball2.x + ball2.radius > canvas.width) ball2.vx *= -1;
            if (ball2.y - ball2.radius < 0 || ball2.y + ball2.radius > canvas.height) ball2.vy *= -1;

            // 쿨다운 감소
            if (ball1.cooldown > 0) ball1.cooldown--;
            if (ball2.cooldown > 0) ball2.cooldown--;

            // 공끼리 충돌 감지 (원 거리 공식)
            let dx = ball2.x - ball1.x;
            let dy = ball2.y - ball1.y;
            let distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < ball1.radius + ball2.radius) {
                // 충돌 시 탄성 반사 처리 (간이 반사)
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

                // 데미지 처리 (쿨다운 적용으로 따닥 방지)
                if (ball1.cooldown === 0 && ball2.cooldown === 0) {
                    ball1.hp -= 10;
                    ball2.hp -= 10;
                    ball1.cooldown = 30; // 30프레임 동안 중복 데미지 방지
                    ball2.cooldown = 30;

                    if (ball1.hp < 0) ball1.hp = 0;
                    if (ball2.hp < 0) ball2.hp = 0;
                }
            }

            // UI 텍스트 업데이트
            document.getElementById("hp1").innerText = ball1.hp;
            document.getElementById("hp2").innerText = ball2.hp;

            // 게임 종료 체크
            if (ball1.hp <= 0 || ball2.hp <= 0) {
                // 게임 리셋 로직 필요시 추가 가능
            }
        }

        function draw() {
            // 화면 지우기
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // 공 1 그리기
            ctx.beginPath();
            ctx.arc(ball1.x, ball1.y, ball1.radius, 0, Math.PI * 2);
            ctx.fillStyle = ball1.color;
            ctx.fill();
            ctx.closePath();

            // 공 2 그리기
            ctx.beginPath();
            ctx.arc(ball2.x, ball2.y, ball2.radius, 0, Math.PI * 2);
            ctx.fillStyle = ball2.color;
            ctx.fill();
            ctx.closePath();
        }

        function loop() {
            if (ball1.hp > 0 && ball2.hp > 0) {
                update();
            }
            draw();
            requestAnimationFrame(loop);
        }

        loop();
    </script>
</body>
</html>
"""

# Streamlit에 HTML 컴포넌트 임베드
st.components.v1.html(game_html, height=500)
