% rebase('osnova.tpl')
<!-- Main container -->
<nav class="level">
    <div class="level-left">
        <div class="buttons has-addons field is-horizontal">
            % for id_zaposlenega, zaposleni in enumerate(kategorije):
            <a href="/zaposleni/{{id_zaposlenega}}/" class="button" name="id_zaposlenega" value="{{id_zaposlenega}}">
                {{zaposleni.ime_kategorije}}
                <span class="tag is-rounded">{{zaposleni.stevilo_vseh()}}</span>
            </a>
            % end
        </div>
    </div>
    <div class="level-right">
            <div class="level-item">
                <a class="button is-info" href="/dodaj-zaposlenega/">Dodaj zaposlenega</a>
            </div>
        </form>
    </div>
</nav>