from pathlib import Path
import html

root = Path(__file__).parent
common = '''*{box-sizing:border-box}body{font-family:system-ui,sans-serif;max-width:760px;margin:0 auto;padding:20px;color:#17233a;line-height:1.6;font-size:20px}button,input,textarea,select{font:inherit}button{cursor:pointer;padding:10px 16px;border:2px solid #244779;border-radius:8px;background:#fff;color:#17233a;margin:4px}button:hover{background:#e7efff}button:focus-visible,input:focus-visible,textarea:focus-visible,select:focus-visible{outline:3px solid #d17000}input,textarea,select{max-width:100%;padding:8px;border:2px solid #66758c;border-radius:6px}h1{font-size:1.7em}'''
quiz = '''<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>퀴즈 판</title>
<script>
// 여기만 바꾸면 됩니다: 제목, 칭찬과 문제를 고쳐 보세요.
const 제목 = '신나는 구구단 퀴즈';
const 정답칭찬 = '정답이에요! 잘했어요!';
const 오답칭찬 = '아쉬워요! 다음 문제도 도전해요!';
const 문제들 = [
  {문제:'3 × 4는 얼마일까요?', 보기:['7','12','14','16'], 정답:1},
  {문제:'5 × 6은 얼마일까요?', 보기:['25','28','30','35'], 정답:2},
  {문제:'7 × 2는 얼마일까요?', 보기:['9','12','14','16'], 정답:2},
  {문제:'8 × 4는 얼마일까요?', 보기:['24','28','32','36'], 정답:2},
  {문제:'9 × 3은 얼마일까요?', 보기:['18','21','24','27'], 정답:3}
]; // 정답은 보기의 순서에서 1을 뺀 숫자입니다. 첫 번째는 0입니다.
</script><style>''' + common + ''' #보기 button{display:block;width:100%;text-align:left}#알림{min-height:2em;font-weight:bold}</style></head>
<body><h1 id="제목"></h1><p id="순서"></p><h2 id="문제"></h2><div id="보기"></div><p id="알림" role="status"></p><button id="다음" hidden>다음 문제</button><button id="다시" hidden>다시 하기</button>
<script>
let 순서 = 0, 점수 = 0;
document.getElementById('제목').textContent = 제목;
const 순서표 = document.getElementById('순서'), 문제표 = document.getElementById('문제'), 보기판 = document.getElementById('보기'), 알림 = document.getElementById('알림'), 다음 = document.getElementById('다음'), 다시 = document.getElementById('다시');
function 보여주기() {
  순서표.textContent = (순서 + 1) + ' / ' + 문제들.length;
  문제표.textContent = 문제들[순서].문제; 보기판.replaceChildren(); 알림.textContent = ''; 다음.hidden = true;
  문제들[순서].보기.forEach((내용, 번호) => {
    const 버튼 = document.createElement('button'); 버튼.textContent = 내용;
    버튼.onclick = () => {
      const 맞음 = 번호 === 문제들[순서].정답;
      if (맞음) 점수++;
      알림.textContent = (맞음 ? 정답칭찬 : 오답칭찬) + ' 정답: ' + 문제들[순서].보기[문제들[순서].정답];
      보기판.querySelectorAll('button').forEach(b => b.disabled = true); 다음.hidden = false;
    };
    보기판.append(버튼);
  });
}
다음.onclick = () => { 순서++; if (순서 < 문제들.length) 보여주기(); else { 순서표.textContent = '퀴즈 끝!'; 문제표.textContent = 문제들.length + '문제 중 ' + 점수 + '개를 맞혔어요!'; 보기판.replaceChildren(); 알림.textContent = ''; 다음.hidden = true; 다시.hidden = false; } };
다시.onclick = () => { 순서 = 0; 점수 = 0; 다시.hidden = true; 보여주기(); };
보여주기();
</script></body></html>'''
tools = '''<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>교실 도구</title><script>
// 여기만 바꾸면 됩니다: 제목, 문구, 기본 시간과 모둠 이름을 고쳐 보세요.
const 제목 = '우리 교실 도구', 뽑기문구 = '뽑힌 번호', 기본시간 = 3, 모둠이름 = '모둠';
</script><style>''' + common + ''' .큰글씨{font-size:2em;font-weight:bold}section[hidden]{display:none}.끝{background:#fff0b3}nav button[aria-pressed="true"]{background:#244779;color:white}</style></head><body>
<h1 id="제목"></h1><nav aria-label="기능 고르기"><button data-tab="뽑기" aria-pressed="true">번호 뽑기</button><button data-tab="모둠" aria-pressed="false">모둠 나누기</button><button data-tab="타이머" aria-pressed="false">타이머</button></nav>
<section id="뽑기"><h2>번호 뽑기</h2><label>전체 인원수 <input id="인원" type="number" min="1" max="500" value="20"></label><button id="뽑기버튼">번호 뽑기</button><button id="뽑기초기화">다시 뽑기</button><p id="뽑기결과" class="큰글씨" role="status"></p><p id="뽑은목록"></p></section>
<section id="모둠" hidden><h2>모둠 나누기</h2><label>전체 인원수 <input id="모둠인원" type="number" min="1" max="500" value="20"></label> <label>모둠 수 <input id="모둠수" type="number" min="1" max="500" value="4"></label><button id="나누기">나누기</button><div id="모둠결과" role="status"></div></section>
<section id="타이머" hidden><h2>타이머</h2><label>시간 (분) <input id="분" type="number" min="1" max="999"></label><p id="시계" class="큰글씨" role="timer"></p><button id="시작">시작</button><button id="멈춤">멈춤</button><button id="초기화">초기화</button><p id="시간알림" class="큰글씨" role="status"></p></section>
<script>
const $ = id => document.getElementById(id); $('제목').textContent = 제목; $('분').value = 기본시간;
document.querySelectorAll('[data-tab]').forEach(b => b.onclick = () => { document.querySelectorAll('[data-tab]').forEach(x => { const 선택 = x === b; x.setAttribute('aria-pressed', 선택); $(x.dataset.tab).hidden = !선택; }); });
const 숫자 = (id, 최대=500) => { const n = Number($(id).value); return Number.isInteger(n) && n >= 1 && n <= 최대 ? n : 0; };
const 섞기 = a => { for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]];} return a; };
let 남은번호 = [], 뽑은번호 = [], 이전인원 = 0;
$('뽑기초기화').onclick = () => { 남은번호=[]; 뽑은번호=[]; 이전인원=0; $('뽑기결과').textContent=''; $('뽑은목록').textContent=''; };
$('뽑기버튼').onclick = () => { const n=숫자('인원'); if(!n){$('뽑기결과').textContent='인원수를 1부터 500까지 입력해 주세요.'; return;} if(n!==이전인원){남은번호=섞기(Array.from({length:n},(_,i)=>i+1)); 뽑은번호=[]; 이전인원=n;} if(!남은번호.length){$('뽑기결과').textContent='모든 번호를 뽑았어요. 다시 뽑기를 눌러 주세요.'; return;} const 번호=남은번호.pop(); 뽑은번호.push(번호); $('뽑기결과').textContent=뽑기문구+': '+번호; $('뽑은목록').textContent='지금까지: '+뽑은번호.join(', '); };
$('나누기').onclick = () => { const n=숫자('모둠인원'), g=숫자('모둠수'); const 결과=$('모둠결과'); 결과.replaceChildren(); if(!n||!g||g>n){결과.textContent='인원수는 1~500, 모둠 수는 인원수 이하로 입력해 주세요.'; return;} const 그룹=Array.from({length:g},()=>[]); 섞기(Array.from({length:n},(_,i)=>i+1)).forEach((v,i)=>그룹[i%g].push(v)); 그룹.forEach((a,i)=>{const p=document.createElement('p'); p.textContent=모둠이름+' '+(i+1)+': '+a.join(', '); 결과.append(p);}); };
let 남은초=기본시간*60, 간격=null, 종료시각=0;
function 표시(){ $('시계').textContent=String(Math.floor(남은초/60)).padStart(2,'0')+':'+String(남은초%60).padStart(2,'0'); }
function 중지(){clearInterval(간격); 간격=null;}
$('시작').onclick=()=>{ if(간격) return; if(!남은초){$('시간알림').textContent='초기화한 뒤 시작해 주세요.'; return;} 종료시각=Date.now()+남은초*1000; 간격=setInterval(()=>{남은초=Math.max(0,Math.ceil((종료시각-Date.now())/1000)); 표시(); if(!남은초){중지(); $('타이머').classList.add('끝'); $('시간알림').textContent='시간이 끝났어요!';}},200); };
$('멈춤').onclick=()=>{if(간격){남은초=Math.max(0,Math.ceil((종료시각-Date.now())/1000)); 중지(); 표시();}};
$('초기화').onclick=()=>{중지(); const n=숫자('분',999); if(!n){$('시간알림').textContent='시간을 1~999분으로 입력해 주세요.'; return;} 남은초=n*60; $('시간알림').textContent=''; $('타이머').classList.remove('끝'); 표시();};
$('분').onchange=()=>{if(!간격) $('초기화').click();}; 표시();
</script></body></html>'''
words = '''<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>낱말 카드와 빙고</title><script>
// 여기만 바꾸면 됩니다: 제목, 칸 크기와 글자 크기를 고쳐 보세요.
const 제목='낱말 카드와 빙고', 칸높이=110, 글자크기=24;
</script><style>''' + common + ''' textarea{width:100%;min-height:150px}.카드{border:3px solid #244779;border-radius:12px;min-height:180px;display:grid;place-items:center;text-align:center;font-weight:bold}.빙고{display:grid;gap:2px}.빙고 div{border:2px solid #244779;display:grid;place-items:center;text-align:center;overflow-wrap:anywhere;padding:5px}@media print{.조작,button{display:none!important}body{max-width:none;padding:0}.카드,.빙고 div{break-inside:avoid}}</style></head><body><h1 id="제목"></h1>
<div class="조작"><label for="낱말">낱말을 한 줄에 하나씩 적어 주세요.</label><textarea id="낱말">사과
바나나
딸기
포도
수박
참외
복숭아
귤
배</textarea><p><button id="카드만들기">낱말 카드 보기</button> <label>빙고 크기 <select id="크기"><option value="3">3×3</option><option value="4">4×4</option></select></label> <button id="빙고만들기">빙고판 만들기</button></p></div>
<p id="안내" role="status"></p><div id="결과"></div><div id="카드버튼" hidden><button id="이전">이전 카드</button><button id="다음">다음 카드</button></div><button id="인쇄">인쇄하기</button>
<script>
const $=id=>document.getElementById(id); $('제목').textContent=제목; let 낱말들=[], 위치=0;
function 읽기(){return $('낱말').value.split(/\\r?\\n/).map(x=>x.trim()).filter(Boolean);}
function 카드표시(){ $('결과').replaceChildren(); const 카드=document.createElement('div'); 카드.className='카드'; 카드.style.fontSize=글자크기+'px'; 카드.textContent=낱말들[위치]; $('결과').append(카드); $('안내').textContent='카드 '+(위치+1)+' / '+낱말들.length; }
$('카드만들기').onclick=()=>{낱말들=읽기(); $('결과').replaceChildren(); $('카드버튼').hidden=true; if(!낱말들.length){$('안내').textContent='낱말을 한 개 이상 적어 주세요.'; return;} 위치=0; $('카드버튼').hidden=false; 카드표시();};
$('이전').onclick=()=>{위치=(위치-1+낱말들.length)%낱말들.length; 카드표시();}; $('다음').onclick=()=>{위치=(위치+1)%낱말들.length; 카드표시();};
$('빙고만들기').onclick=()=>{const 목록=읽기(), 크기=Number($('크기').value), 필요=크기*크기; $('결과').replaceChildren(); $('카드버튼').hidden=true; if(목록.length<필요){$('안내').textContent='낱말이 '+필요+'개 이상 필요해요. 지금은 '+목록.length+'개예요.'; return;} for(let i=목록.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1)); [목록[i],목록[j]]=[목록[j],목록[i]];} const 판=document.createElement('div'); 판.className='빙고'; 판.style.gridTemplateColumns='repeat('+크기+', 1fr)'; 목록.slice(0,필요).forEach(낱말=>{const 칸=document.createElement('div'); 칸.style.minHeight=칸높이+'px'; 칸.style.fontSize=글자크기+'px'; 칸.textContent=낱말; 판.append(칸);}); $('결과').append(판); $('안내').textContent=크기+'×'+크기+' 빙고판';}; $('인쇄').onclick=()=>window.print(); $('카드만들기').click();
</script></body></html>'''
items=[('example-quiz.html','4지선다 퀴즈 판','한 문제씩 풀어 보는 구구단 퀴즈입니다. 1회차 기본 예시로 사용하세요.',quiz,['문제 3개를 내 교과에 맞게 바꾸기','제목과 칭찬 문구 바꾸기','보기 개수 바꾸기'],['틀린 문제만 다시 풀 수 있게 해 줘.','정답을 맞히면 효과음을 넣어 줘.','문제 순서를 섞어 줘.']),('example-tools.html','번호 뽑기·모둠 나누기·타이머','번호로 뽑고 모둠을 나누고 시간을 재는 교실 도구입니다.',tools,['뽑기 문구 바꾸기','타이머 기본 시간 바꾸기','모둠 이름 바꾸기'],['이미 뽑은 번호 중에서 원하는 번호를 빼 줘.','모둠 이름을 동물 이름으로 바꿔 줘.','타이머에 알림음을 넣어 줘.']),('example-words.html','낱말 카드·빙고판 만들기','낱말을 적어 카드와 빙고판으로 만들어 봅니다.',words,['빙고 칸 크기 바꾸기','글자 크기 바꾸기','제목 바꾸기'],['빙고판 여러 장을 한 번에 만들어 줘.','카드 뒷면에 낱말의 뜻을 넣어 줘.','빙고판 가운데 칸을 비워 줘.'])]
for filename,title,intro,code,changes,prompts in items:
    esc=html.escape(code)
    page=f'''<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} | 연수 예시</title><link rel="stylesheet" href="style.css"><style>.preview{{width:100%;height:650px;border:2px solid #cfd8e6;border-radius:10px;background:white}}.copy-example{{font:inherit;font-weight:bold;padding:12px 18px;background:#1d3a6e;color:white;border:0;border-radius:8px;cursor:pointer}}pre{{max-height:340px;overflow:auto;background:#1e2433;color:white;padding:16px;white-space:pre;font-size:14px}} code{{background:none;color:inherit;padding:0}}</style></head><body><main><p><a href="index.html">← 연수 안내로 돌아가기</a></p><h1>{title}</h1><p class="lead">{intro}</p><h2>바로 실행해 보기</h2><iframe class="preview" title="{title} 실행 화면" sandbox="allow-scripts allow-modals" srcdoc="{html.escape(code, quote=True)}"></iframe><h2>코드 복사하기</h2><p>아래 버튼을 누른 뒤 GitHub의 빈 <code>index.html</code>에 붙여넣으세요.</p><button class="copy-example" type="button">코드 전체 복사</button><p id="복사상태" role="status"></p><details><summary>전체 코드 보기</summary><pre><code id="전체코드">{esc}</code></pre></details><h2>바꿔 볼 곳 3가지</h2><ol>{''.join('<li>'+html.escape(x)+'</li>' for x in changes)}</ol><h2>다음에 AI에게 부탁해 보기</h2><ul>{''.join('<li>“'+html.escape(x)+'”</li>' for x in prompts)}</ul><p>입력한 내용은 저장하지 않고 이 화면에서만 사용합니다.</p></main><script>document.querySelector('.copy-example').addEventListener('click',async()=>{{const text=document.getElementById('전체코드').textContent;const status=document.getElementById('복사상태');try{{if(!navigator.clipboard)throw Error();await navigator.clipboard.writeText(text);status.textContent='코드를 복사했어요. index.html에 붙여넣으세요.';}}catch(e){{const t=document.createElement('textarea');t.value=text;document.body.append(t);t.select();let ok=false;try{{ok=document.execCommand('copy')}}catch(e){{}}t.remove();status.textContent=ok?'코드를 복사했어요. index.html에 붙여넣으세요.':'복사하지 못했어요. 전체 코드 보기를 열어 직접 선택해 복사해 주세요.';}}}});</script></body></html>'''
    (root/filename).write_text(page,encoding='utf-8')

index=root/'index.html'
content=index.read_text(encoding='utf-8')
marker='    <h2>바로 가기</h2>'
links='''    <h2>연수 예시 앱</h2>
    <ul class="cards">
      <li><a class="card" href="example-quiz.html"><b>4지선다 퀴즈 판</b><span>1회차 기본 예시 코드</span></a></li>
      <li><a class="card" href="example-tools.html"><b>번호 뽑기·모둠 나누기·타이머</b><span>번호로 쓰는 교실 도구</span></a></li>
      <li><a class="card" href="example-words.html"><b>낱말 카드·빙고판</b><span>낱말을 넣고 인쇄하기</span></a></li>
    </ul>

'''
if 'example-quiz.html' not in content:
    assert marker in content
    index.write_text(content.replace(marker,links+marker),encoding='utf-8')
