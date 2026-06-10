# ☁️ Cloud-Modus einrichten (gemeinsame Datenbank) – Schritt für Schritt

Mit dem Cloud-Modus tippt **jedes Familienmitglied auf seinem eigenen Handy**,
und alle sehen denselben Stand **live**. Nur **du als Admin** trägst Ergebnisse
ein, sperrst Spiele und kannst zurücksetzen.

> Ohne diese Einrichtung läuft die App ganz normal **lokal/offline** weiter –
> du aktivierst die Cloud also nur, wenn du möchtest.

---

## Schritt 1 – Supabase-Projekt anlegen (ca. 5 Min)

1. Geh auf **[supabase.com](https://supabase.com)** → **Start your project** → mit
   GitHub oder E-Mail kostenlos registrieren.
2. **New project** anlegen:
   - **Name:** z. B. `wm-tippspiel`
   - **Database Password:** ein beliebiges starkes Passwort (brauchst du später
     nicht für die App – einfach notieren).
   - **Region:** `Central EU (Frankfurt)` (näher = schneller).
3. Kurz warten, bis das Projekt „bereit" ist.

## Schritt 2 – Tabellen & Live-Sync erstellen (2 Min)

1. Links im Menü: **SQL Editor** → **New query**.
2. Öffne die Datei **[`supabase-setup.sql`](supabase-setup.sql)** aus diesem
   Projekt, kopiere den **kompletten Inhalt** in den Editor.
3. **Run** (oder `Strg/Cmd + Enter`) klicken.
4. Es sollte „Success. No rows returned" erscheinen – fertig. ✅

> Falls beim erneuten Ausführen Fehler wie „policy already exists" kommen:
> alles gut, dann ist es bereits eingerichtet.

## Schritt 3 – Zugangsdaten kopieren (1 Min)

1. Links im Menü: **Project Settings** (Zahnrad) → **API**.
2. Notiere dir zwei Werte:
   - **Project URL** – z. B. `https://abcd1234.supabase.co`
   - **anon public** (unter *Project API keys*) – ein langer Schlüssel.

> ⚠️ Den **`service_role`**-Schlüssel **niemals** verwenden/teilen! Nur den
> **anon public**. Der ist genau für den Einsatz in einer Webseite gedacht.

## Schritt 4 – Werte in die App eintragen (1 Min)

Öffne **[`cloud-config.js`](cloud-config.js)** und trage deine zwei Werte ein:

```js
window.CLOUD_CONFIG = {
  url: "https://abcd1234.supabase.co",
  anonKey: "dein-langer-anon-public-key"
};
```

Speichern, committen und pushen (oder sag mir Bescheid, dann mache ich das).
Sobald die Seite über GitHub Pages aktualisiert ist, läuft die App im
**Cloud-Modus** – oben rechts erscheint ein **🔑-Symbol**.

## Schritt 5 – Als Admin anmelden & Daten hochladen

1. Öffne die Seite. Tippe oben rechts auf **🔑**.
2. Da noch kein PIN existiert, wirst du gebeten, **einen Admin-PIN festzulegen**
   (z. B. 4–6 Ziffern). Merke ihn dir – damit meldest du dich auf anderen Geräten
   als Admin an. Du bist jetzt Admin (Symbol wird zu **🔓**).
3. Hast du **schon einen lokalen Spielstand** (Spieler/Spiele/Tipps)? Dann geh
   in **⚙️ Verwalten → ☁️ Gemeinsame Cloud → „⬆️ Lokalen Stand hochladen"**.
   Damit landet dein bisheriger Stand einmalig in der Cloud.
   *Alternativ* fängst du frisch an: lade als Admin den WM-Plan über
   **„🌍 Kompletten Gruppenplan laden"**.

## Schritt 6 – An die Familie verteilen

1. Schick allen einfach den **gleichen Link** zur Seite
   (`https://<dein-name>.github.io/Projekte/`).
2. Jeder öffnet ihn, geht auf **👨‍👩‍👧 Familie** und legt **sich selbst** als
   Mitspieler an (Name + Avatar). Das Gerät merkt sich automatisch, **wer** es ist.
3. Ab dann tippt jeder seine Spiele – alle Tipps und die Tabelle aktualisieren
   sich bei allen **automatisch**.

---

## Wer darf was?

| Aktion | Mitglied | Admin (🔓) |
|---|:---:|:---:|
| Eigene Spiele tippen, Joker setzen | ✅ | ✅ |
| Bonus-Fragen beantworten | ✅ | ✅ |
| Sich selbst als Spieler anlegen | ✅ | ✅ |
| Ergebnisse eintragen, Spiele sperren | – | ✅ |
| Spielplan/K.-o.-Runden laden, Bonus-Fragen anlegen/auflösen | – | ✅ |
| Spieler entfernen, alles zurücksetzen | – | ✅ |

Admin wirst du pro Gerät über das **🔑-Symbol + PIN**. Mit **🔓** (nochmal tippen)
meldest du dich wieder ab.

## Gut zu wissen

- **Internet** ist zum Tippen nötig (die App lädt zuletzt bekannte Daten auch
  offline aus dem Cache, neue Tipps brauchen aber Verbindung).
- Der **PIN-Schutz** ist bequem, aber technisch umgehbar – für die Familie okay.
  Echten Schutz gäbe es nur mit richtiger Anmeldung (können wir später nachrüsten).
- **Kosten:** Das kostenlose Supabase-Kontingent reicht für eine Familie locker.
- **Zurück zu rein lokal?** Einfach die Werte in `cloud-config.js` wieder leeren.
