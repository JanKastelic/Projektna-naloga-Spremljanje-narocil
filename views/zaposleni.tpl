% rebase('osnova.tpl')
<!-- Main container -->
<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_kategorije, kategorija in enumerate(kategorije):
            % if kategorija == aktualna_kategorija:
            <a class="button is-primary is-selected" name="id_kategorije" value="{{id_kategorije}}">
                {{kategorija.ime_kategorije}}
                <span class="tag is-rounded">{{kategorija.stevilo_odprtih()}}</span>
            </a>
            % else:
            <a href="/zaposleni/{{id_kategorije}}/" class="button" name="id_kategorije" value="{{id_kategorije}}">
                {{kategorija.ime_kategorije}}
                <span class="tag is-rounded">{{kategorija.stevilo_odprtih()}}</span>
            </a>
            % end
            % end
        </div>
    </div>

    <div class="level-right">
        <!-- <div class="level-item">
            <p class="subtitle is-5">
                <strong>123</strong> posts
            </p>
        </div> -->
            <div class="level-item">
                <a class="button is-info" href="/dodaj-zaposlenega/">Dodaj zaposlenega</a>
            </div>
        </form>
    </div>
</nav>

% if aktualna_kategorija:

<table class="table is-hoverable is-fullwidth">
    <thead>
        <tr>
            <form method="POST" action="/dodaj-storitev/{{id_aktualne_kategorije}}/">
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="opis" placeholder="Opis">
                        <span class="icon is-small is-left">
                            <i class="far fa-clipboard-check"></i>
                        </span>
                    </div>
                </td>                
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="datum_sprejema" placeholder="Datum sprejema">
                        <span class="icon is-small is-left">
                            <i class="far fa-calendar-alt"></i>
                        </span>
                    </div>
                </td>
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="oseba" placeholder="Oseba">
                        <span class="icon is-small is-left">
                            <i class="far fa-user"></i>
                        </span>
                    </div>
                </td>  
                <td>
                    <div class="control has-icons-left">
                        <input class="input is-small" type="text" name="rok" placeholder="rok">
                        <span class="icon is-small is-left">
                            <i class="far fa-calendar-alt"></i>
                        </span>
                    </div>
                </td>
                <td>
                    <div class="control">
                        <button class="button is-info is-small">Dodaj</button>
                    </div>
                </td>
                <td></td>
            </form>
        </tr>
    </thead>
    <tbody>
        % for id_storitve, storitev in enumerate(aktualna_kategorija.storitve):
        <tr>
            <td>{{ storitev.opis_storitve }}</td>
            <td>{{ storitev.datum_sprejema }}</td>
            <td>{{ storitev.oseba }}</td>
            <td>{{ storitev.rok }}</td>
            <td>
                % if storitev.stanje:
                    <strong>KONČANO</strong>
                % else:
                    <strong>ODPRTO</strong>
                % end
            </td>
            <td>
                <form method="POST" action="/dokoncano/{{id_aktualne_kategorije}}/{{id_storitve}}/">
                    <span class="icon is-small">
                        <button class="button is-info is-small">Zaključi</button>
                    </span>
                </form>
            </td>
        </tr>
        % end
    </tbody>
</table>

% else:

<p>Nimate vnešenega nobenega od zaposlenih. <a href="/dodaj-zaposlenega/">Dodajte ga!</a></p>