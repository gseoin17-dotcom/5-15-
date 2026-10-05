create table if not exists public.gz_votes (
  member text not null,
  voter_user_id text not null,
  role text not null check (role in ('임시 멤버','애매한 멤버','정착 멤버','정식 멤버')),
  created_at timestamptz not null default now(),
  primary key (member, voter_user_id)
);

create table if not exists public.gz_settings (
  key text primary key,
  value text not null,
  updated_at timestamptz not null default now()
);

alter table public.gz_votes enable row level security;
alter table public.gz_settings enable row level security;
