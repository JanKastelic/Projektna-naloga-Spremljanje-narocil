% rebase('osnova.tpl')
<form method="POST">
    <div class="field">
        <label class="label">Ime</label>
        <div class="control">
            <input class="input" name="Ime" type="text" placeholder="Ime">
        </div>
    </div>    
    <div class="field">
        <label class="label">Priimek</label>
        <div class="control">
            <input class="input" name="Priimek" type="text" placeholder="Priimek">
        </div>
    </div>
        <div class="field">
        <label class="label">Uporabniško ime</label>
        <div class="control has-icons-left">
            <input class="input" name="Uporabnisko_ime" type="text" placeholder="Uporabniško ime">
            <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
            </span>
        </div>
    </div>
    <div class="field">
        <label class="label">Geslo</label>
        <div class="control has-icons-left">
            <input class="input" name="Geslo" type="password" placeholder="Geslo">
            <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
            </span>
        </div>
        <div class="control has-icons-left">
            <input class="input" name="Potrdi geslo" type="password" placeholder="Potrdi geslo">
            <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
            </span>
        </div>
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button is-link">Registriraj se</button>
        </div>
         <div class="control">
            <a class="button is-link is-light" href="/">Prekliči</a>
        </div>
    </div>
</form>