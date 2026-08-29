import random
import streamlit as st

st.set_page_config(page_title="공 싸움 게임", layout="centered")

st.title("🔴 실시간 공 싸움 게임")
st.write("공들이 서로 부딪히고 벽에 튕기며 싸우는 물리 시뮬레이션입니다!")

# 한국어 적용 및 완벽한 벽 튕김 물리 구문이 포함된 HTML/JS 코드
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

    // 공의 움직임 업데이트
    p1.x += p1.vx;
    p1.y += p1.vy;
    p2.x += p2.vx;
    p2.y += p2.vy;

    // --- 벽에 부딪힐 때 완벽하게 튕기는 구문 ---
    // 플레이어 1 벽 충돌
    if (p1.x - p1.radius < 0) {
        p1.x = p1.radius; // 벽 내부로 파고드는 것 방지
        p1.vx *= -1;     // 속도 반전 (튕김)
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

    // 플레이어 2 벽 충돌
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
    }
