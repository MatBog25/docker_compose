#stworzenie obrazu na bazie ubuntu w wersji 20.04
FROM ubuntu:20.04
#uruchomienie update apt i instalacja pythona w kontenerze
RUN apt update && apt install -y python3 python3-pip
#skopiowanie pliku wyswietl_zawartosc.py do /app/ --- dodajemy drugi / zeby folder sie stworzyl 
COPY wyswietl_zawartosc.py /app/
#skopiowanie calego folderu data do danego miejsca w kontenerze
COPY data /app/data/
#tu mozna dac np. ["python3", "wyswietl_zawartosc.py"] i wtedy uruchomi sie kod automatycznie a jak damy bash to mozna to samemu zrobic --- CMD jako ostatnia komenda do wykonania.
CMD [ "bash" ]