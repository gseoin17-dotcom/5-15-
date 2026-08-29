import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="공 싸움 게임", layout="centered")

st.title("🔴 실시간 공 싸움 게임")
st.write("공들이 서로 부딪히고 벽에 튕기며 싸우는 물리 시뮬레이션입니다!")

game_html = <!DOCTYPE html>
<html>
<head>
<style>
  body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #0e1117;
    color: white;
    font-family: sans-serif;
  }
  canvas {
    border: 4px solid #ffffff;
    background-color: #1a1c23;
    box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.2);
  }
  .scoreboard {
    display: flex;
    justify-content: space-between;
    width: 600px;
    margin-bottom: 10px;
    font-size: 20px;
    font-weight: bold;
  }
</style>
</head>
<body>

<div class="scoreboard">
  <div style="color: #ff4b4b;">플레이어 1 (빨강): <span id="hp1">100</span></div>
  <div style="color: #4b9eff;">플레이어 2 (파랑): <span id="hp2">100</span></div>
</div>

<canvas id="gameCanvas" width="600" height="400"></canvas>
<br>
<button onclick="resetGame()" style="padding: 10px 20px; font-size: 16px; cursor: pointer; background-color: #ff4b4b; color: white; border: none; border-radius: 5px; font-weight: bold;">게임 다시 시작</button>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let p1 = { x: 150, y: 200, vx: 5, vy: 3, radius: 25, color: "#ff4b4b", hp: 100 };
let p2 = { x: 450, y: 200, vx: -5, vy: -3, radius: 25, color: "#4b9eff", hp: 100 };

function resetGame() {
    p1 = { x: 150, y: 200, vx: (Math.random()-0.5)*10, vy: (Math.random()-0.5)*10, radius: 25, color: "#ff4b4b", hp: 100 };
    p2 = { x: 450, y: 200, vx: (Math.random()-0.5)*10, vy: (Math.random()-0.5)*10, radius: 25, color: "#4b9eff", hp: 100 };
}

function update() {
    if (p1.hp <= 0 || p2.hp <= 0) return;

    p1.x += p1.vx;
    p1.y += p1.vy;
    p2.x += p2.vx;
    p2.y += p2.vy;

    if (p1.x - p1.radius < 0) {
        p1.x = p1.radius;
        p1.vx *= -1;
    } else if (p1.x + p1.radius > canvas.width) {
        p1.x = canvas.width - p1.radius;
        p1.vx *= -1;
    }
    if (p1.y - p1.radius < 0) {
        p1.y = p1.radius;
        p1.vy *= -1;
    } else if (p1.y + p1.radius > canvas.height) {
        p1.y = canvas.height - p1.radius;
        p1.vy *= -1;
    }

    if (p2.x - p2.radius < 0) {
        p2.x = p2.radius;
        p2.vx *= -1;
    } else if (p2.x + p2.radius > canvas.width) {
        p2.x = canvas.width - p2.radius;
        p2.vx *= -1;
    }
    if (p2.y - p2.radius < 0) {
        p2.y = p2.radius;
        p2.vy *= -1;
    } else if (p2.y + p2.radius > canvas.height) {
        p2.y = canvas.height - p2.radius;
        p2.vy *= -1;
    }

    let dx = p2.x - p1.x;
    let dy = p2.y - p1.y;
    let dist = Math.sqrt(dx * dx + dy * dy);

    if (dist < p1.radius + p2.radius) {
        let angle = Math.atan2(dy, dx);
        let sin = Math.sin(angle);
        let cos = Math.cos(angle);

        let vx1 = p1.vx * cos + p1.vy * sin;
        let vy1 = p1.vy * cos - p1.vx * sin;
        let vx2 = p2.vx * cos + p2.vy * sin;
        let vy2 = p2.vy * cos - p2.vx * sin;

        let temp = vx1;
        vx1 = vx2;
        vx2 = temp;

        p1.vx = vx1 * cos - vy1 * sin;
        p1.vy = vy1 * cos + vx1 * sin;
        p2.vx = vx2 * cos - vy2 * sin;
        p2.vy = vy2 * cos + vx2 * sin;

        let overlap = (p1.radius + p2.radius) - dist;
        p1.x -= overlap * cos * 0.5;
        p1.y -= overlap * sin * 0.5;
        p2.x += overlap * cos * 0.5;
        p2.y += overlap * sin * 0.5;

        let impactSpeed = Math.abs(vx1 - vx2);
        let damage = Math.floor(impactSpeed * 1.2);
        if (damage > 2) {
            if (Math.random() > 0.5) p1.hp -= damage;
            else p2.hp -= damage;
            
            if (p1.hp < 0) p1.hp = 0;
            if (p2.hp < 0) p2.hp = 0;
        }
    }

    document.getElementById("hp1").innerText = p1.hp;
    document.getElementById("hp2").innerText = p2.hp;
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    ctx.arc(p1.x, p1.y, p1.radius, 0, Math.PI * 2);
    ctx.fillStyle = p1.color;
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = "#ffffff";
    ctx.stroke();
    ctx.closePath();

    ctx.beginPath();
    ctx.arc(p2.x, p2.y, p2.radius, 0, Math.PI * 2);
    ctx.fillStyle = p2.color;
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = "#ffffff";
    ctx.stroke();
    ctx.closePath();
}

function loop() {
    update();
    draw();
    requestAnimationFrame(loop);
}

loop();
</script>

</body>
</html>"""

components.html(game_html, height=520)
