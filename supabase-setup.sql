-- ============================================================================
--  Familien-WM-Tippspiel 2026 · Supabase-Datenbank einrichten
-- ----------------------------------------------------------------------------
--  So geht's:
--   1. In Supabase dein Projekt öffnen
--   2. Links im Menü:  SQL Editor  →  "New query"
--   3. Diesen kompletten Inhalt einfügen  →  "Run" klicken
--  Danach sind alle Tabellen, Zugriffsregeln und der Live-Sync eingerichtet.
-- ============================================================================

-- ---------- Tabellen --------------------------------------------------------
create table if not exists players (
  id         text primary key,        -- ID kommt aus der App (kein Auto-Wert)
  name       text not null,
  avatar     text,
  pin        text,                    -- optionales Tipp-Passwort des Mitspielers
  created_at timestamptz default now()
);
-- Falls die Tabelle schon vorher existierte: Spalte nachrüsten.
alter table players add column if not exists pin text;

create table if not exists matches (
  id        text primary key,
  t1 text, t2 text,
  phase text, datum text, ort text,
  spieltag int, ko_runde int, ko_index int,
  sieger text,
  gespielt boolean default false,
  e1 int, e2 int,
  gesperrt boolean default false,
  sort_order int                       -- bewahrt die Anzeige-Reihenfolge
);

create table if not exists tips (
  player_id  text references players(id) on delete cascade,
  match_id   text references matches(id) on delete cascade,
  e1 int, e2 int,
  is_joker   boolean default false,
  updated_at timestamptz default now(),
  primary key (player_id, match_id)    -- ein Tipp je Spieler & Spiel
);

create table if not exists bonus_questions (
  id text primary key,
  frage text, optionen jsonb, punkte int default 5,
  loesung text, sort_order int
);

create table if not exists bonus_tips (
  player_id   text references players(id) on delete cascade,
  question_id text references bonus_questions(id) on delete cascade,
  antwort text,
  primary key (player_id, question_id)
);

create table if not exists settings (
  id        int primary key default 1 check (id = 1),
  admin_pin text
);
insert into settings (id) values (1) on conflict (id) do nothing;

-- ---------- Zugriff (Row Level Security) ------------------------------------
--  Einfaches Familienmodell: Jeder mit dem öffentlichen anon-Key darf lesen
--  und schreiben. Der Admin-Schutz (Ergebnisse, Sperren, Reset) passiert in
--  der App über einen PIN. Das ist bequem, aber technisch umgehbar – für die
--  Familie in Ordnung. Echten Schutz gäbe es nur mit richtiger Anmeldung.
alter table players          enable row level security;
alter table matches          enable row level security;
alter table tips             enable row level security;
alter table bonus_questions  enable row level security;
alter table bonus_tips       enable row level security;
alter table settings         enable row level security;

create policy "familie_alles" on players         for all using (true) with check (true);
create policy "familie_alles" on matches         for all using (true) with check (true);
create policy "familie_alles" on tips            for all using (true) with check (true);
create policy "familie_alles" on bonus_questions for all using (true) with check (true);
create policy "familie_alles" on bonus_tips      for all using (true) with check (true);
create policy "familie_alles" on settings        for all using (true) with check (true);

-- ---------- Live-Sync (Realtime) --------------------------------------------
--  Sorgt dafür, dass Änderungen sofort bei allen Geräten ankommen.
alter publication supabase_realtime add table players;
alter publication supabase_realtime add table matches;
alter publication supabase_realtime add table tips;
alter publication supabase_realtime add table bonus_questions;
alter publication supabase_realtime add table bonus_tips;
alter publication supabase_realtime add table settings;

-- Fertig! 🎉  Jetzt nur noch Project URL + anon-Key in cloud-config.js eintragen.
