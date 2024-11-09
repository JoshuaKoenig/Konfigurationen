  GNU nano 8.1                                                                                                                                                                                         xor_decrypt.py                                                                                                                                                                                                  
import argparse

def xor_decrypt(input_string, printable_only=True):
    """
    Führt eine XOR-Entschlüsselung auf eine gegebene Zeichenfolge durch und gibt 
    die Ergebnisse für alle Schlüssel (0-255) aus.
    
    :param input_string: Die Eingabezeichenfolge, die entschlüsselt werden soll.
    :param printable_only: Gibt nur Ergebnisse zurück, die druckbare Zeichen enthalten (32-126).
    :return: Ein Dictionary mit den getesteten Schlüsseln und den entsprechenden entschlüsselten Zeichenfolgen.
    """
    # Konvertiere die Eingabezeichenfolge in eine Liste von Ganzzahlen (ASCII-Werte)
    input_as_int = [ord(char) for char in input_string]
    
    # Ergebnis speichern
    results = {}

    # Führe XOR für jeden möglichen Schlüssel (0-255) durch
    for key in range(256):
        # Wende XOR auf jedes Zeichen an und füge es zu einer neuen Zeichenfolge zusammen
        decrypted_string = ''.join([chr(num ^ key) for num in input_as_int])
        
        # Speichere je nach Einstellung nur die druckbaren oder alle Ergebnisse
        if not printable_only or all(32 <= ord(c) <= 126 for c in decrypted_string):
            results[key] = decrypted_string

    return results

def main():
    # Argumentparser für den Input-String von der Konsole
    parser = argparse.ArgumentParser(description="Führt eine XOR-Umwandlung auf eine Zeichenfolge durch.")
    parser.add_argument("input_string", type=str, help="Die Zeichenfolge, die verarbeitet werden soll.")
    parser.add_argument(
        "--all", 
        action="store_true", 
        help="Zeigt alle Ergebnisse an, einschließlich nicht-druckbarer Zeichen."
    )
    
    # Argumente parsen
    args = parser.parse_args()

    # Führe die XOR-Umwandlung durch
    decrypted_results = xor_decrypt(args.input_string, printable_only=not args.all)

    # Zeige die Ergebnisse an und erläutere den Schlüssel
    for key, result in decrypted_results.items():
        print(f"Schlüssel {key}: {result}")

if __name__ == "__main__":
    main()

