import os

def wyswietl_zawartosc_pliku(sciezka_do_pliku):
    # Sprawdzamy, czy plik istnieje
    if os.path.isfile(sciezka_do_pliku):
        print(f"Plik w folderze {os.path.dirname(sciezka_do_pliku)} istnieje.")
        # Otwieramy i wyświetlamy zawartość pliku
        with open(sciezka_do_pliku, 'r') as plik:
            zawartosc = plik.read()
            print(f"Zawartość pliku: {zawartosc}")
    else:
        print(f"Plik {sciezka_do_pliku} nie istnieje.")

# Ścieżki do sprawdzanych plików
plik1 = "./data/jakis_plik.txt"
plik2 = "./data_ale_w_wolumenie/jakis_plik.txt"


# Sprawdzanie pliku w folderze /data
wyswietl_zawartosc_pliku(plik1)

# Sprawdzanie pliku w folderze /data_ale_w_wolumenie
wyswietl_zawartosc_pliku(plik2)
