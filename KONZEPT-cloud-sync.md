# 🌐 Konzept: Gemeinsame Datenbank mit Supabase (Live-Sync für die ganze Familie)

> Ziel: Jeder tippt auf **seinem eigenen Handy**, alle sehen **dieselben Daten live**.
> Nur **du als Admin** kannst Ergebnisse eintragen, Spiele sperren und zurücksetzen.
> Backend: **Supabase** · Admin-Schutz: **einfacher PIN**

Dieses Dokument ist der **Plan** – es wird noch kein Code umgebaut. Wenn du es
gelesen hast und einverstanden bist, setze ich es Schritt für Schritt um.

---

## 1. Was sich grundsätzlich ändert

**Heute:** Alle Daten liegen nur im Browser deines Geräts (`localStorage`).
Teilen = eine eingefrorene Momentaufnahme per Link/QR.

**Künftig:** Eine kleine Cloud-Datenbank (Supabase) ist die „Wahrheit". Jedes
Handy liest und schreibt dort hinein und bekommt Änderungen der anderen **live**
mitgeteilt (Supabase „Realtime").

```
        ┌─────────────┐        ┌─────────────┐        ┌─────────────┐
        │  Dein Handy │        │ Omas Handy  │        │ Lukas' Handy│
        └──────┬──────┘        └──────┬──────┘        └──────┬──────┘
               │                      │                      │
               └──────────────┬───────┴──────────┬───────────┘
                              ▼                   ▼
                       ┌─────────────────────────────┐
                       │   Supabase (Postgres + Sync) │
                       │   Spiele · Tipps · Spieler   │
                       └─────────────────────────────┘
```

**Wichtige Konsequenzen, ehrlich gesagt:**
- 🌐 **Internet nötig** zum Tippen (Offline-Anzeige bleibt als Cache möglich).
- 🔐 Der PIN-Schutz ist **bequem, aber nicht 100 % manipulationssicher** – für die
  Familie völlig okay, aber ein technisch versierter Mitspieler *könnte* ihn umgehen.
  (Echten Schutz gäbe es nur mit richtiger Anmeldung – das war bewusst nicht gewählt.)
- 🆔 Jeder wählt auf seinem Gerät **einmalig „Wer bist du?"** – damit Tipps
  zugeordnet werden und man nur seine eigenen ändern kann.

---

## 2. Datenmodell (die Tabellen in Supabase)

Statt eines einzigen großen Datenklumpens speichern wir **normalisiert** – jeder
Tipp ist eine eigene Zeile. Das ist entscheidend, damit sich gleichzeitige Tipps
**nicht gegenseitig überschreiben** (zwei Leute tippen kurz vor Anpfiff → beide
Tipps bleiben erhalten).

| Tabelle | Inhalt | Wer schreibt? |
|---|---|---|
| `players` | Mitspieler (Name, Avatar) | alle |
| `matches` | Spielplan (Teams, Phase, Spieltag, Ergebnis, Sperre) | **nur Admin** |
| `tips` | je Spieler+Spiel ein Tipp (e1, e2, Joker) | jeder nur **seine** Zeile |
| `bonus_questions` | Bonus-/Turnierfragen | **nur Admin** |
| `bonus_tips` | Antworten der Spieler auf Bonusfragen | jeder seine |
| `settings` | u. a. der Admin-PIN | **nur Admin** |

### SQL zum Anlegen (liefere ich fertig – hier zur Vorschau)

```sql
create table players (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  avatar text,
  created_at timestamptz default now()
);

create table matches (
  id uuid primary key default gen_random_uuid(),
  t1 text, t2 text,
  phase text, datum text, ort text,
  spieltag int, ko_runde int, ko_index int,
  sieger text,
  gespielt boolean default false,
  e1 int, e2 int,
  gesperrt boolean default false,
  sort_order int
);

create table tips (
  player_id uuid references players(id) on delete cascade,
  match_id  uuid references matches(id) on delete cascade,
  e1 int, e2 int,
  is_joker boolean default false,
  updated_at timestamptz default now(),
  primary key (player_id, match_id)
);

create table bonus_questions (
  id uuid primary key default gen_random_uuid(),
  frage text, optionen jsonb, punkte int default 5,
  loesung text, sort_order int
);

create table bonus_tips (
  player_id   uuid references players(id) on delete cascade,
  question_id uuid references bonus_questions(id) on delete cascade,
  antwort text,
  primary key (player_id, question_id)
);

create table settings (
  id int primary key default 1 check (id = 1),
  admin_pin text
);
```

---

## 3. So funktioniert der Admin-Schutz (PIN)

1. Beim ersten Einrichten legst **du** einen PIN fest (z. B. 4–6 Ziffern). Er
   landet in der `settings`-Tabelle.
2. Auf jedem Gerät gibt es einen Knopf **„🔑 Als Admin anmelden"**. Wer den
   richtigen PIN eingibt, schaltet auf diesem Gerät die Admin-Funktionen frei:
   - Ergebnisse eintragen
   - Spiele sperren / freigeben
   - Spielplan laden, K.-o.-Runden erzeugen
   - Bonusfragen anlegen/auflösen
   - **Alles zurücksetzen**
3. Ohne Admin-Freischaltung sehen die anderen diese Knöpfe **gar nicht** – sie
   können nur tippen.

> 🔎 *Technische Ehrlichkeit:* Der PIN gated die **Oberfläche**. Die Datenbank
> selbst akzeptiert mit dem öffentlichen „anon"-Schlüssel weiterhin Schreibzugriffe.
> Für die Familie ist das in Ordnung; wenn du später echten Schutz willst, rüsten
> wir eine richtige Anmeldung nach (überschaubarer Zusatzaufwand).

---

## 4. Was du einrichten musst (einmalig, ca. 15 Min)

1. **Konto:** Auf [supabase.com](https://supabase.com) kostenlos registrieren.
2. **Projekt anlegen** (Name z. B. „wm-tippspiel", Region Frankfurt/EU).
3. **Tabellen erstellen:** Mein fertiges SQL in den „SQL Editor" einfügen → ausführen.
4. **Realtime aktivieren:** Für die Tabellen `matches`, `tips`, `bonus_tips`,
   `players` den Live-Sync anschalten (1 Klick je Tabelle bzw. per SQL).
5. **Zugangsdaten kopieren:** Unter *Project Settings → API* findest du
   - die **Project URL** (z. B. `https://xxxx.supabase.co`)
   - den **anon public key** (ein langer Schlüssel)
6. Diese **zwei Werte** gibst du mir – ich trage sie in die HTML-Datei ein.

> ⚠️ **Niemals** den `service_role`-Schlüssel weitergeben oder in die HTML-Datei
> packen! Nur der **anon public**-Schlüssel gehört dorthin (der ist für genau
> diesen Zweck öffentlich gedacht und sicher).

---

## 5. Was ich im Code umbaue

1. **Supabase-SDK einbinden** (eine kleine Bibliothek, offline-fähig gecacht).
2. **`config.js`** für URL + anon-Key (leicht austauschbar, nicht im Hauptcode vergraben).
3. **Speicherschicht umstellen:** `localStorage` → Supabase-Lese-/Schreibfunktionen.
   `localStorage` bleibt als **Offline-Cache** für die reine Anzeige erhalten.
4. **Realtime-Abos:** App lauscht auf DB-Änderungen → Tabelle/Tipps aktualisieren
   sich automatisch, ohne Neuladen.
5. **„Wer bist du?"-Auswahl** pro Gerät (lokal gemerkt). Man kann nur eigene Tipps
   bearbeiten.
6. **Admin-PIN-Flow** + Verstecken der Admin-Knöpfe für normale Spieler.
7. **Einmaliger „⬆️ In die Cloud hochladen"-Knopf**, der deinen jetzigen lokalen
   Spielstand (Spieler, Spiele, Tipps) in Supabase überträgt – damit nichts verloren geht.

---

## 6. Aufwand & Reihenfolge (Vorschlag)

| Schritt | Wer | Aufwand |
|---|---|---|
| Supabase-Projekt + SQL + Realtime | **du** (ich liefere SQL/Anleitung) | ~15 Min |
| URL + anon-Key an mich | du | 1 Min |
| Cloud-Anbindung einbauen | ich | – |
| „Wer bist du?" + Admin-PIN | ich | – |
| Bestehende Daten hochladen | du (1 Knopf) | 1 Min |
| Testen mit 2 Geräten | gemeinsam | ~10 Min |

---

## 7. Offene Punkte, die wir noch klären sollten

- **Ein Spiel oder mehrere?** Reicht **eine** Familien-Runde pro Datenbank (am
  einfachsten), oder willst du mehrere getrennte Tipprunden über einen „Spiel-Code"?
- **Joker & Sperren** verhalten sich wie bisher – nur eben für alle sichtbar. OK so?
- **Was passiert mit alten Geräten/Links?** Der bisherige Teilen-Link wird durch
  die Cloud überflüssig; wir können ihn als „Notfall-Export" trotzdem behalten.

> Sag mir einfach Bescheid, wenn das so passt – dann liefere ich dir als Erstes
> das fertige SQL-Skript + die Klick-für-Klick-Anleitung für Supabase.
