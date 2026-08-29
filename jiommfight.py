import random
import time
import streamlit as st

st.set_page_config(page_title="Ball Fighting Game", layout="centered")

st.title("🔴 Ball Fighting Game (Streamlit Edition)")
st.write("Watch the balls fight in real-time using physics simulation!")

# Embedded HTML/JS for smooth 60fps real-time physics and rendering
game_html = """
<!DOCTYPE html>
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
  <div style="color: #ff4b4b;">Player 1 (Red): <span id="hp1">100</span></div>
  <div style="color: #4b9eff;">Player 2 (Blue): <span id="hp2">100</span></div>
</div>

<canvas id="gameCanvas" width="600" height="400"></canvas>
<br>
<button onclick="resetGame()" style="padding: 10px 20px; font-size: 16px; cursor: pointer;">Restart Fight</button>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let p1 = { x: 150, y: 200, vx: 4, vy: 3, radius: 25, color: "#ff4b4b", hp: 100 };
let p2 = { x: 450, y: 200, vx: -4, vy: -3, radius: 25, color: "#4b9eff", hp: 100 };

function resetGame() {
    p1 = { x: 150, y: 200, vx: (Math.random()-0.5)*8, vy: (Math.random()-0.5)*8, radius: 25, color: "#ff4b4b", hp: 100 };
    p2 = { x: 450, y: 200, vx: (Math.random()-0.5)*8, vy: (Math.random()-0.5)*8, radius: 25, color: "#4b9eff", hp: 100 };
}

function update() {
    if (p1.hp <= 0 || p2.hp <= 0) return;

    // Move balls with slight AI tracking/randomness
    p1.vx += (Math.random() - 0.5) * 0.8;
    p1.vy += (Math.random() - 0.5) * 0.8;
    p2.vx += (Math.random() - 0.5) * 0.8;
    p2.vy += (Math.random() - 0.5) * 0.8;

    // Damping to keep speed stable
    p1.vx *= 0.99; p1.vy *= 0.99;
    p2.vx *= 0.99; p2.vy *= 0.99;

    p1.x += p1.vx; p1.y += p1.vy;
    p2.x += p2.vx; p2.y += p2.vy;

    // Wall collisions
    if (p1.x - p1.radius < 0 || p1.x + p1.radius > canvas.width) p1.vx *= -1;
    if (p1.y - p1.radius < 0 || p1.y + p1.radius > canvas.height) p1.vy *= -1;
    if (p2.x - p2.radius < 0 || p2.x + p2.radius > canvas.width) p2.vx *= -1;
    if (p2.y - p2.radius < 0 || p2.y + p2.radius > canvas.height) p2.vy *= -1;

    // Ball-to-ball collision
    let dx = p2.x - p1.x;
    let dy = p2.y - p1.y;
    let dist = Math.sqrt(dx * dx + dy * dy);

    if (dist < p1.radius + p2.radius) {
        // Elastic collision response
        let angle = Math.atan2(dy, dx);
        let sin = Math.sin(angle);
        let cos = Math.cos(angle);

        // Rotate velocities
        let vx1 = p1.vx * cos + p1.vy * sin;
        let vy1 = p1.vy * cos - p1.vx * sin;
        let vx2 = p2.vx * cos + p2.vy * sin;
        let vy2 = p2.vy * cos - p2.vx * sin;

        // Swap velocities (equal mass)
        let temp = vx1;
        vx1 = vx2;
        vx2 = temp;

        // Rotate back
        p1.vx = vx1 * cos - vy1 * sin;
        p1.vy = vy1 * cos + vx1 * sin;
        p2.vx = vx2 * cos - vy2 * sin;
        p2.vy = vy2 * cos + vx2 * sin;

        // Separate positions to prevent sticking
        let overlap = (p1.radius + p2.radius) - dist;
        p1.x -= overlap * cos * 0.5;
        p1.y -= overlap * sin * 0.5;
        p2.x += overlap * cos * 0.5;
        p2.y += overlap * sin * 0.5;

        // Damage calculation based on collision impact speed
        let impactSpeed = Math.abs(vx1 - vx2);
        let damage = Math.floor(impactSpeed * 1.5);
        if (damage > 1) {
            if (Math.random() > 0.5) p1.hp -= damage;
            else p2.hp -= damage;
            
            if (p1.hp < 0) p1.hp = 0;
            if (p2.hp < 0) p2.hp = 0;
        }
    }

    // Update scoreboard text
    document.getElementById("hp1").innerText = p1.hp;
    document.getElementById("hp2").innerText = p2.hp;
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw P1
    ctx.beginPath();
    ctx.arc(p1.x, p1.y, p1.radius, 0, Math.PI * 2);
    ctx.fillStyle = p1.color;
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = "#ffffff";
    ctx.stroke();
    ctx.closePath();

    // Draw P2
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
</html>
"""

# Render the HTML/JS component inside Streamlit
st.components.v1.html(game_html, height=520)

What specific features or characters from the Instagram clip would you like to add next?
