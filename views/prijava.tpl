% rebase('osnova.tpl')
<form method="POST">
    <div class="field">
        <label class="label">Uporabniško ime</label>
        <div class="control has-icons-left">
            <input class="input" name="uporabnisko_ime" type="text" placeholder="uporabniško ime">
            <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
            </span>
        </div>
    </div>
    <div class="field">
        <label class="label">Geslo</label>
        <div class="control has-icons-left">
            <input class="input" name="geslo" type="password" placeholder="geslo">
            <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
            </span>
        </div>
    </div>
    <div class="field is-grouped">
        <div class="control">
            <button class="button is-link">Prijavi se</button>
        </div>
    </div>
</form>