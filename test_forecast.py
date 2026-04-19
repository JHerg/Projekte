import random

def predict_visitors(temp, is_raining=False):
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

if __name__ == "__main__":
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