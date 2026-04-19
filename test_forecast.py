import random

def predict_visitors(temp: float, is_raining: bool = False) -> int:
    """
    Sagt die Besucherzahl für ein Schwimmbad basierend auf Temperatur und Regen voraus.

    Args:
        temp (float): Die aktuelle oder vorhergesagte Temperatur in °C.
        is_raining (bool): Gibt an, ob es regnet. Standard ist False.

    Returns:
        int: Die vorhergesagte Anzahl an Besuchern (mindestens 0).
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
    prediction += random.uniform(-10, 10)

    return max(0, int(prediction))

def print_forecast(temp: float, is_raining: bool, prognose: int) -> None:
    """
    Gibt die Vorhersage in einer formatierten Tabelle aus.
    """
    regen_status = "Ja" if is_raining else "Nein"
    print(f"+-----------------------+-----------+")
    print(f"| Schwimmbad-Check      | Details   |")
    print(f"+-----------------------+-----------+")
    print(f"| Temperatur            | {temp:>7}°C |")
    print(f"| Regen                 | {regen_status:>9} |")
    print(f"| Besucher-Prognose     | {prognose:>9} |")
    print(f"+-----------------------+-----------+")

if __name__ == "__main__":
    # Test-Vorhersage
    heutige_temp = 28
    regnet_es = True  # Neue Variable für Regen
    prognose = predict_visitors(heutige_temp, regnet_es)

    # Schicke Tabellenausgabe
    print_forecast(heutige_temp, regnet_es, prognose)
