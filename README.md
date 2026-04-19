# Schwimmbad Besucher-Prognose

Dieses Projekt enthält ein einfaches Skript zur Vorhersage der Besucherzahlen eines Schwimmbads basierend auf der Temperatur und den Wetterbedingungen (Regen).

## Inhaltsverzeichnis
- [Beschreibung](#beschreibung)
- [Voraussetzungen](#voraussetzungen)
- [Nutzung](#nutzung)
- [Logik](#logik)
- [Ausgabe](#ausgabe)

## Beschreibung

Die Datei `test_forecast.py` simuliert eine Vorhersage für die Anzahl der Gäste, die ein Schwimmbad besuchen könnten. Es nutzt eine Basis-Besucherzahl und passt diese anhand von Temperatur und Regenwahrscheinlichkeit an. Zusätzlich wird ein Zufallselement ("Rauschen") hinzugefügt, um natürliche Schwankungen abzubilden.

## Voraussetzungen

Das Skript verwendet nur die Standardbibliothek von Python. Es werden keine zusätzlichen Abhängigkeiten oder Pakete benötigt.
Python 3.x sollte installiert sein.

## Nutzung

Um die Vorhersage zu testen, kann das Skript einfach in der Kommandozeile ausgeführt werden:

```bash
python test_forecast.py
```

Das Skript ist derzeit mit fest codierten Testwerten ausgestattet:
- `heutige_temp = 28`
- `regnet_es = True`

Um andere Szenarien zu testen, können diese Werte am Ende der Datei `test_forecast.py` geändert werden.

## Logik

Die Funktion `predict_visitors(temp, is_raining=False)` führt folgende Schritte aus:

1. **Basis-Besucherzahl:** Das Schwimmbad hat unabhängig vom Wetter eine Basis-Auslastung von **100 Gästen**.
2. **Temperatur-Einfluss:** Für jedes Grad Celsius über 20°C kommen **20 weitere Gäste** hinzu. Liegt die Temperatur bei 20°C oder darunter, bleibt es bei den Basis-Gästen.
3. **Regen-Einfluss:** Wenn es regnet (`is_raining = True`), halbiert sich die bis dahin berechnete erwartete Besucherzahl (**-50%**).
4. **Zufall / Rauschen:** Um realistische Unschärfen in der Prognose abzubilden, wird am Ende ein zufälliger Wert zwischen **-10 und +10 Gästen** zur Schätzung addiert.

## Ausgabe

Wenn das Skript ausgeführt wird, gibt es die berechneten Werte in einer übersichtlichen, formatierten ASCII-Tabelle aus.

Beispielausgabe für 28°C mit Regen:

```text
+-----------------------+-----------+
| Schwimmbad-Check      | Details   |
+-----------------------+-----------+
| Temperatur            |      28°C |
| Regen                 |        Ja |
| Besucher-Prognose     |       125 |
+-----------------------+-----------+
```
*(Die `Besucher-Prognose` variiert bei jeder Ausführung leicht durch den Zufallsfaktor).*
