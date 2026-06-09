# ⚽ Familien-WM-Tippspiel 2026

Ein familienfreundliches, lustiges Tippspiel zur Fußball-WM 2026 – als **eine einzelne HTML-Datei**, komplett **offline** lauffähig, ohne Server und ohne Installation.

👉 **Spielen:** einfach [`wm-tippspiel.html`](wm-tippspiel.html) im Browser öffnen (Doppelklick genügt) – oder, sobald über GitHub Pages gehostet, direkt im Browser/aufs Handy installieren.

## Features

- **Kompletter WM-2026-Spielplan** – alle 72 Gruppenspiele mit echten Terminen (MESZ) und Stadien, dazu der automatisch erzeugte **K.-o.-Baum nach offiziellem FIFA-Bracket** (Sechzehntel- bis Finale).
- **Tippen & Punkte** – 4 Punkte exakt, 3 für richtige Tordifferenz, 2 für richtige Tendenz; ein **Joker** pro Spieler verdoppelt die Punkte eines Spiels.
- **Bonus-Fragen & Turnier-Vorhersagen** – Weltmeister, Torschützenkönig, Überraschungsteam u. v. m.
- **Live-Gruppentabellen** – berechnet nach den offiziellen FIFA-Sortierregeln (inkl. direktem Vergleich).
- **Spaß-Faktoren:** Spieler-Statistiken, Sammel-Abzeichen, 12 lustige Awards, Strafen-Generator, Pausen-Quiz, Konfetti.
- **Rund ums Spiel:** Countdown zum nächsten Anpfiff, Direktduell zweier Spieler, Punkte-Verlauf-Chart, Außenseiter-Radar.
- **Dark-Mode** (umschaltbar, pro Gerät gespeichert) und **PWA** (installierbar & offline-fähig).
- **Teilen** per Link/QR-Code – der komplette Spielstand steckt im Link (kein Backend nötig).

## Dateien

| Datei | Zweck |
|-------|-------|
| `wm-tippspiel.html` | Die komplette App (HTML, CSS, JS inline, inkl. eingebundener Offline-Bibliotheken) |
| `index.html` | Weiterleitung auf `wm-tippspiel.html` (für die blanke GitHub-Pages-URL) |
| `manifest.json` | PWA-Manifest (Name, Icon, Farben) |
| `sw.js` | Service Worker fürs Offline-Caching |
| `icon.svg` | App-Icon |

## Als App installieren (GitHub Pages)

1. **Settings → Pages → Source:** „Deploy from a branch", Branch `main`, Ordner `/ (root)`.
2. Aufrufen unter `https://<dein-name>.github.io/projekte/` (leitet automatisch aufs Spiel).
3. Auf dem Handy: **Android/Chrome** → Menü → „App installieren"; **iPhone/Safari** → Teilen → „Zum Home-Bildschirm".

Die PWA-Funktionen (Installieren, Offline-Cache) sind nur über `https://` aktiv. Per Doppelklick (`file://`) läuft die App ganz normal weiter – nur eben ohne Installation.

## Daten & Privatsphäre

Alles wird **lokal im Browser** gespeichert (`localStorage`). Es gibt keinen Server, keine Konten, kein Tracking. Zum Sichern/Übertragen dienen der Teilen-Link, der QR-Code oder der Export als Datei.
