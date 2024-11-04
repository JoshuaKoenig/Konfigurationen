import argparse

def xor_decrypt(input_string):
    # Konvertiere die Eingabezeichenfolge in eine Liste von Ganzzahlen (ASCII-Werte)
    input_as_int = [ord(char) for char in input_string]

    # Ergebnis speichern
    results = {}

    # Führe XOR für jeden möglichen Schlüssel (0-255) durch
    for key in range(256):
        # Wende XOR auf jedes Zeichen an und füge es zu einer neuen Zeichenfolge zusammen
        decrypted_string = ''.join([chr(num ^ key) for num in input_as_int])

        # Speichere nur die Zeichenfolgen, die druckbare Zeichen enthalten
        if all(32 <= ord(c) <= 126 for c in decrypted_string):
            results[key] = decrypted_string

    return results

def main():
    # Argumentparser für den Input-String von der Konsole
    parser = argparse.ArgumentParser(description="Führt eine XOR-Umwandlung auf eine Zeichenfolge durch.")
    parser.add_argument("input_string", type=str, help="Die Zeichenfolge, die verarbeitet werden soll.")
    
    # Argumente parsen
    args = parser.parse_args()

    # Führe die XOR-Umwandlung durch
    decrypted_results = xor_decrypt(args.input_string)

    # Zeige die Ergebnisse an und erläutere den Schlüssel
    for key, result in decrypted_results.items():
        if key == 0:
            print(f"Schlüssel {key} (kein XOR angewendet): {result}")
        else:
            print(f"Schlüssel {key} (XOR mit {key}): {result}")

if __name__ == "__main__":
    main()
