% rebase('osnova.tpl')
<form method="POST">
    <div class="field">
        <label class="label">Ime</label>
        <div class="control has-icons-left has-icons-right">
            <input class="input" name="ime_kategorije" type="text" placeholder="Ime zaposlenega" value="{{polja.get('ime_kategorije', '')}}">
            <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
            </span>
        </div>
        % if "ime" in napake:
        <p class="help is-danger">{{ napake["ime"] }}</p>
        % end
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button is-link">Dodaj</button>
        </div>
        <div class="control">
            <a class="button is-link is-light" href="/">Prekliči</a>
        </div>
    </div>
</form>