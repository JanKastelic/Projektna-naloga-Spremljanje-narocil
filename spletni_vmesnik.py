import bottle
from datetime import date
from model import Stanje, Kategorija, Storitev

IME_DATOTEKE = "stanje.json"

SIFRIRNI_KLJUC = "To je poseben šifrirni ključ"

try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(kategorije=[])

def url_kategorije(id_kategorije):
    return f"/kategorija/{id_kategorije}/"

def ime_uporabnikove_datoteke(uporabnisko_ime):
    return f"stanja_uporabnikov/{uporabnisko_ime}.json"

def stanje_trenutnega_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    if uporabnisko_ime == None:
        bottle.redirect("/prijava/")
    else:
        uporabnisko_ime = uporabnisko_ime
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    try:
        stanje = Stanje.preberi_iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje.preberi_iz_datoteke("stanje.json")
        stanje.shrani_v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    stanje.shrani_v_datoteko(ime_datoteke)


@bottle.get("/")
def zacetna_stran():
    stanje = stanje_trenutnega_uporabnika()
    return bottle.template("zacetna_stran.tpl", kategorije=stanje.kategorije,)

@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.tpl")

@bottle.post("/registracija/")
def registracija_post():
    bottle.redirect("/prijava/")

@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.tpl")

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo = bottle.request.forms.getunicode("geslo")
    if uporabnisko_ime == geslo:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
        bottle.redirect("/")
    else:
        return "Napaka ob prijavi"

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    bottle.redirect("/")
    
@bottle.get("/kategorija/<id_kategorije:int>/")
def prikazi_kategorijo(id_kategorije):
    stanje = stanje_trenutnega_uporabnika()
    kategorija = stanje.kategorije[id_kategorije]
    return bottle.template(
        "kategorija.tpl",
        kategorije=stanje.kategorije,
        aktualna_kategorija=kategorija,
        id_aktualne_kategorije=id_kategorije,
    )
    
@bottle.get("/dodaj-kategorijo/")
def dodaj_kategorijo_get():
    return bottle.template("dodaj_kategorijo.tpl", napake={}, polja={})

@bottle.post("/dodaj-kategorijo/")
def dodaj_kategorijo_post():
    stanje = stanje_trenutnega_uporabnika()
    ime_kategorije = bottle.request.forms.getunicode("ime_kategorije")
    kategorija = Kategorija(ime_kategorije, opravila=[])
    napake = stanje.preverjanje_kategorije(kategorija)
    if napake:
        polja = {"ime_kategorije": ime_kategorije}
        return bottle.template("dodaj_kategorijo.tpl", napake=napake, polja=polja)
    else:
        id_kategorije = stanje.dodaj_kategorijo(kategorija)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(url_kategorije(id_kategorije))
   
@bottle.post("/dodaj-storitev/<id_kategorije:int>/")
def dodaj_storitev(id_kategorije):
    stanje = stanje_trenutnega_uporabnika()
    kategorija = stanje.kategorije[id_kategorije]
    opis = bottle.request.forms.getunicode("opis")
    if bottle.request.forms["datum_sprejema"]:
        datum_sprejema = date.fromisoformat(bottle.request.forms["datum_sprejema"])
    else:
        datum_sprejema = date.fromisoformat(date.today())
    oseba = bottle.request.forms.getunicode("oseba")
    if bottle.request.forms["rok"]:
        rok = date.fromisoformat(bottle.request.forms["rok"])
    else:
        rok = None
    storitev = Storitev(opis, datum_sprejema, oseba, rok)
    kategorija.dodaj_storitev(storitev)
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_kategorije(id_kategorije))
   
@bottle.post("/dokoncano/<id_kategorije:int>/<id_storitve:int>/")
def opravi(id_kategorije, id_storitve):
    stanje = stanje_trenutnega_uporabnika()
    kategorija = stanje.kategorije[id_kategorije]
    storitev = kategorija.storitve[id_storitve]
    storitev.dokoncano()
    shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_kategorije(id_kategorije))
   
   
   
    
bottle.run(debug=True, reloader=True)
