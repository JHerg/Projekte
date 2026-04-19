"""
Modul für die Vorhersage der Besucherzahlen eines Schwimmbads.

Dieses Skript enthält eine einfache Logik, um basierend auf Temperatur
und Wetterbedingungen (Regen) die ungefähre Besucherzahl vorherzusagen.
"""

import random

def predict_visitors(temp, is_raining=False):
    """
    Sagt die Besucherzahl für ein Schwimmbad basierend auf Temperatur und Regen vorher.

    Die Basis-Besucherzahl beträgt 100 Gäste.
    Für jedes Grad Celsius über 20°C kommen weitere 20 Gäste hinzu.
    Bei Regen reduziert sich die erwartete Besucherzahl um 50%.
    Zusätzlich wird ein leichtes Rauschen (-10 bis +10 Gäste) hinzugefügt, um
    realistische Schwankungen zu simulieren.

    Args:
        temp (float oder int): Die vorhergesagte Temperatur in Grad Celsius.
        is_raining (bool, optional): Gibt an, ob es regnet. Standardmäßig False.

    Returns:
        int: Die prognostizierte Besucherzahl.
    """
    # Einfache Logik: Basis 100 Gäste + 20 pro Grad über 20°C
    base_visitors = 100
    if temp > 20:
        prediction = base_visitors + (temp - 20) * 20
    else:
        prediction = base_visitors

    # Wenn es regnet, sinkt die Besucherzahl um 50%
    if is_raining:
        prediction *= 0.5

    # Ein bisschen Zufall (Rauschen) für die Realität
    return int(prediction + random.uniform(-10, 10))

# Test-Vorhersage
heutige_temp = 28
regnet_es = True  # Neue Variable für Regen
prognose = predict_visitors(heutige_temp, regnet_es)

# Schicke Tabellenausgabe
regen_status = "Ja" if regnet_es else "Nein"
print(f"+-----------------------+-----------+")
print(f"| Schwimmbad-Check      | Details   |")
print(f"+-----------------------+-----------+")
print(f"| Temperatur            | {heutige_temp:>7}°C |")
print(f"| Regen                 | {regen_status:>9} |")
print(f"| Besucher-Prognose     | {prognose:>9} |")
print(f"+-----------------------+-----------+")