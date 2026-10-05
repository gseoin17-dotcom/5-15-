# GZ ROLE VOTE - Vercel + Supabase

PC를 꺼도 계속 작동하는 배포용 버전입니다.

## 기능
- Discord 로그인
- GZ 서버 멤버만 투표 가능
- 14명 고정:
  경모, 지온, 원태, 지호, 탁원, 지욱, 주영, 원석, 성준, 민호, 준서, 민기, 동훈, 태민
- 각 멤버마다 임시 / 애매한 / 정착 / 정식 중 하나 투표
- 투표 변경 가능
- Supabase 영구 저장
- 25시간 자동 종료
- 실시간 남은 시간 표시
- 관리자 전체 초기화 + 25시간 재시작

## 1. Supabase 설정
1. Supabase에서 새 프로젝트 생성
2. SQL Editor 열기
3. `supabase.sql` 전체 실행
4. Project Settings > API에서:
   - Project URL -> `SUPABASE_URL`
   - service_role key -> `SUPABASE_SERVICE_ROLE_KEY`

주의: service_role 키는 절대로 GitHub에 올리면 안 됩니다.

## 2. GitHub 업로드
이 폴더 안의 파일을 새 GitHub 저장소에 업로드하세요.
`.env` 또는 `.env.local`은 올리지 마세요.

## 3. Vercel 배포
1. Vercel 로그인
2. Add New > Project
3. GitHub 저장소 선택
4. Framework Preset: Other
5. Environment Variables에 아래 값 입력:

DISCORD_CLIENT_ID
DISCORD_CLIENT_SECRET
DISCORD_BOT_TOKEN
DISCORD_GUILD_ID
ADMIN_USER_IDS
SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY
SESSION_SECRET
SITE_NAME

처음 배포할 때 SITE_URL만 비워두고 배포한 뒤,
Vercel에서 생성된 주소 예:
https://gz-role-vote.vercel.app

을 확인해서 `SITE_URL=https://gz-role-vote.vercel.app` 로 추가 후 재배포하세요.

## 4. Discord Redirect URI
Discord Developer Portal > OAuth2 > Redirects에 아래 주소 추가:

https://네-Vercel-주소.vercel.app/auth/discord/callback

예:
https://gz-role-vote.vercel.app/auth/discord/callback

## 5. 25시간 시작 시점
배포 후 사이트 API가 처음 사용될 때 Supabase에 종료 시간이 저장되고,
그 시점 기준 25시간 후 투표가 자동 종료됩니다.

관리자 화면의 `전체 초기화 + 25시간 재시작` 버튼을 누르면
모든 표를 지우고 다시 25시간이 시작됩니다.
