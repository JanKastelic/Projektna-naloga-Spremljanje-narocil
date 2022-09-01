from datetime import date
from model import Stanje, Kategorija, Storitev

IME_DATOTEKE = "stanja_uporabnikov/primer-stanja.json"

try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(kategorije=[])

def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")

def izberi_moznost(moznosti):
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")

def prikaz_kategorije(kategorija):
    vse = kategorija.stevilo_vseh()
    return f"{kategorija.ime_kategorije.upper()} ({vse})"

def prikaz_storitve(storitev):
    if storitev.stanje:
        return f"°ZAKLJUČENO: {storitev.opis_storitve}, naročilo sprejel/-a {storitev.oseba}"
    elif storitev.rok:
        return f"°ODPRTO: {storitev.opis_storitve}, rok: {storitev.rok}, naročilo sprejel/-a {storitev.oseba}"
    else:
        return f"°ODPRTO: {storitev.opis_storitve}, naročilo sprejel/-a {storitev.oseba}"

def zacetni_pozdrav():
    print("Podravljeni v aplikaciji za evidenco naročil.")

def izberi_kategorijo(stanje):
    print("Izberite želenega zaposlenega:")
    return izberi_moznost(
        [
            (kategorija, prikaz_kategorije(kategorija)) for kategorija in stanje.kategorije
        ]
    )

def izberi_storitev(kategorija):
    print("Izberite storitev:")
    return izberi_moznost(
        [(storitev, prikaz_storitve(storitev)) for storitev in kategorija.storitve]
    )

def dodaj_kategorijo():
    print("Vnesite podatke o zaposlenem.")
    ime_kategorije = input("Ime: >")
    nova_kategorija = Kategorija(ime_kategorije, [])
    stanje.dodaj_kategorijo(nova_kategorija)

def dodaj_storitev():
    kategorija = izberi_kategorijo(stanje)
    print("Vnesite podatke o storitvi.")
    opis = input("Opis: >")
    datum_sprejema = input("Datum sprejema (YYYY-MM-DD): >")
    if datum_sprejema.strip():
        datum_sprejema = date.fromisoformat(datum_sprejema)
    else:
        datum_sprejema = date.today()
    oseba = input("Oseba, ki je sprejela naročilo: >")
    rok = input("Rok (YYYY-MM-DD): >")
    if rok.strip():
        rok = date.fromisoformat(rok)
    else:
        rok = None
    nova_storitev = Storitev(opis, datum_sprejema, oseba, rok)
    kategorija.dodaj_storitev(nova_storitev)

def zakljuci_storitev():
    kategorija = izberi_kategorijo(stanje)
    storitev = izberi_storitev(kategorija)
    storitev.dokoncano()

def izpisi_trenutno_stanje():
    for kategorija in stanje.kategorije:
        print(f"{prikaz_kategorije(kategorija)}:")
        for storitev in kategorija.storitve:
            print(f"{prikaz_storitve(storitev)}:")
    if not stanje.kategorije:
        print("Vnešen ni še nihče od zaposlenih. Dodajte njegovo ime.")

def zakljuci_izvajanje():
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    print("Nasvidenje!")
    exit()

def ponudi_moznosti():
    print("Izberite želeno dejanje:")
    izbrano_dejanje = izberi_moznost(
        [
            (dodaj_kategorijo, "dodajanje novega zaposlenega"),
            (dodaj_storitev, "dodajanje nove storitve"),
            (zakljuci_storitev, "zaključi storitev"),
            (zakljuci_izvajanje, "shrani in zapri program")
        ]
    )
    izbrano_dejanje()

def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        izpisi_trenutno_stanje()
        ponudi_moznosti()


tekstovni_vmesnik()