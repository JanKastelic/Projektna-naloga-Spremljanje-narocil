from datetime import date
import json

class Stanje:

    def __init__(self, kategorije):
        self.kategorije = kategorije

    def dodaj_kategorijo(self, kategorija):
        self.kategorije.append(kategorija)
        return len(self.kategorije) - 1

    def preverjanje_kategorije(self, kategorija):
        for obsotjeca_kategorija in self.kategorije:
            if obsotjeca_kategorija.ime_kategorije == kategorija.ime_kategorije:
                return {"ime": "Ta zaposleni ima že svoj seznam."}

    def v_slovar(self):
        return {
            "kategorije": [kategorija.v_slovar() for kategorija in self.kategorije],
            }

    @staticmethod
    def iz_slovarja(slovar):
        return Stanje([Kategorija.iz_slovarja(kategorije_slovarja) for kategorije_slovarja in slovar["kategorije"]])

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, mode="w") as datoteka:
            slovar = self.v_slovar()
            json.dump(slovar, datoteka, indent=4, ensure_ascii=False)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar = json.load(datoteka)
            return Stanje.iz_slovarja(slovar)


class Kategorija:

    def __init__(self, ime_kategorije, storitve):
        self.ime_kategorije = ime_kategorije
        self.storitve = storitve

    def dodaj_storitev(self, storitev):
        self.storitve.append(storitev)

    def stevilo_odprtih(self):
        odprtih = 0
        for storitev in self.storitve:
            if not storitev.stanje:
                odprtih += 1
            return odprtih

    def stevilo_zakljucenih(self):
        zakljucenih = 0
        for storitev in self.storitve:
            if storitev.stanje:
                zakljucenih += 1
            return zakljucenih

    def stevilo_cez_rok(self):
        cez_rok = 0
        for storitev in self.storitve:
            if storitev.cez_rok():
                cez_rok += 1
            return cez_rok

    def v_slovar(self):
        return {
            "ime_kategorije": self.ime_kategorije,
            "storitve": [storitev.v_slovar() for storitev in self.storitve],
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Kategorija(
            slovar["ime_kategorije"], 
            [Storitev.iz_slovarja(storitve_slovarja) for storitve_slovarja in slovar["storitve"]]
        )


class Storitev:
    def __init__(self, opis_storitve, datum_sprejema, oseba, rok, stanje=False):
        self.opis_storitve = opis_storitve
        self.datum_sprejema = datum_sprejema
        self.oseba = oseba
        self.rok = rok
        self.stanje = stanje

    def dokoncano(self):
        self.stanje = True

    def cez_rok(self):
        rok_storitve = self.rok and self.rok < date.today()
        return not self.stanje and rok_storitve

    def v_slovar(self):
        return {
            "opis_storitve": self.opis_storitve,
            "datum_sprejema": self.datum_sprejema.isoformat() if self.rok else date.today().isoformat(),
            "oseba": self.oseba,
            "rok": self.rok.isoformat() if self.rok else None,
            "stanje": self.stanje,
        }   

    @staticmethod
    def iz_slovarja(slovar):
        return Storitev(
            slovar["opis_storitve"],
            date.fromisoformat(slovar["datum_sprejema"]) if slovar["datum_sprejema"] else None,
            slovar["oseba"],
            date.fromisoformat(slovar["rok"]) if slovar["rok"] else None,
            slovar["stanje"],
        )