let me=null, endsAt=null, timerId=null;

async function api(url, options={}) {
  const res = await fetch(url, {
    headers:{'Content-Type':'application/json', ...(options.headers||{})},
    ...options
  });
  const data = await res.json().catch(()=>({}));
  if(!res.ok) throw new Error(data.error || '오류가 발생했습니다.');
  return data;
}
function esc(s=''){return String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]))}

function updateTimer(){
  if(!endsAt)return;
  const timer=document.getElementById('timer');
  const status=document.getElementById('timerStatus');
  const remain=new Date(endsAt).getTime()-Date.now();

  if(remain<=0){
    timer.textContent='00시간 00분 00초';
    status.textContent='투표 종료';
    status.classList.add('ended');
    if(me) me.votingOpen=false;
    document.querySelectorAll('.vote').forEach(b=>b.disabled=true);
    return;
  }
  const s=Math.floor(remain/1000), h=Math.floor(s/3600), m=Math.floor((s%3600)/60), sec=s%60;
  timer.textContent=`${String(h).padStart(2,'0')}시간 ${String(m).padStart(2,'0')}분 ${String(sec).padStart(2,'0')}초`;
  status.textContent='투표 진행 중';
  status.classList.remove('ended');
}

async function loadMe(){
  me=await api('/api/me');
  endsAt=me.endsAt;
  updateTimer();
  if(timerId)clearInterval(timerId);
  timerId=setInterval(updateTimer,1000);

  const area=document.getElementById('userArea');
  const notice=document.getElementById('loginNotice');
  const reset=document.getElementById('resetBtn');
  if(!me.user){
    area.innerHTML=`<a class="btn" href="/auth/discord">Discord 로그인</a>`;
    notice.classList.remove('hidden');
  } else {
    area.innerHTML=`<div class="userbox">${me.user.avatar?`<img class="avatar" src="${me.user.avatar}">`:`<div class="avatar"></div>`}<div class="username">${esc(me.user.username)}</div><button class="ghost" onclick="logout()">로그아웃</button></div>`;
    if(me.admin) reset.classList.remove('hidden');
  }
}

async function loadVotes(){
  const data=await api('/api/votes');
  document.getElementById('cards').innerHTML=data.members.map(item=>{
    const stats=data.roles.map(role=>{
      const count=item.counts[role]||0, pct=item.total?Math.round(count/item.total*100):0;
      return `<div class="stat"><span>${role.replace(' 멤버','')}</span><div class="track"><div class="fill" style="width:${pct}%"></div></div><span class="count">${count}표</span></div>`;
    }).join('');
    const buttons=data.roles.map(role=>`<button class="vote ${item.myVote===role?'active':''}" ${(!me?.user||!me?.votingOpen)?'disabled':''} onclick="vote('${item.member}','${role}')">${role.replace(' 멤버','')}</button>`).join('');
    return `<article class="card"><div class="card-top"><div class="member-name">${esc(item.member)}</div><div class="result">현재 결과<strong>${item.leader?esc(item.leader):'투표 없음'}</strong></div></div><div class="options">${buttons}</div><div class="stats">${stats}</div></article>`;
  }).join('');
}
async function vote(member,role){
  if(!me?.votingOpen)return alert('투표가 종료되었습니다.');
  try{await api('/api/vote',{method:'POST',body:JSON.stringify({member,role})});await loadVotes()}catch(e){alert(e.message)}
}
async function logout(){await api('/api/logout',{method:'POST'});location.reload()}
document.getElementById('resetBtn').addEventListener('click',async()=>{
  if(!confirm('모든 투표를 지우고 25시간을 다시 시작할까요?'))return;
  try{
    const r=await api('/api/admin/reset',{method:'POST'});
    endsAt=r.endsAt; me.votingOpen=true; updateTimer(); await loadVotes();
  }catch(e){alert(e.message)}
});
(async()=>{await loadMe();await loadVotes()})();
