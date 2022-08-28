<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    % if defined('izbrani_zavihek'):
    <title>Spremljanje naročil – {{oznaka_zavihka[izbrani_zavihek]}}</title>
    % else:
    <title>Spremljanje naročil</title>
    % end
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css">
    <link rel="stylesheet" href="/static/stil.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
    <nav class="navbar is-light">
      <div class="container">
        <div class="navbar-brand">
          <span class="navbar-item">
            <span class="icon">
              <i class="fas fa-ballot-check"></i>
            </span>
            <strong>Spremljanje naročil</strong>
          </span>
          <div class="buttons">
              <a class="button is-primary" href="/">
                <strong>Domov</strong>
              </a>
          </div>
        </div>
        <div class="navbar-start">
          % if defined('izbrani_zavihek'):
            % for zavihek in zavihki:
            % if zavihek == izbrani_zavihek:
              <a class="navbar-item is-active" href="/{{zavihek}}/">
            % else:
              <a class="navbar-item" href="/{{zavihek}}/">
            % end
              <span class="icon">
                <i class="{{ikona_zavihka[zavihek]}}"></i>
              </span>
            <span>{{oznaka_zavihka[zavihek]}}</span>
            </a>
            % end
          % end
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-light" href="/navodila/">
                <strong>Navodila</strong>
              </a>
              <a class="button is-light" href="/registracija/">
                <strong>Registriraj se</strong>
              </a>
              % if defined('uporabnik'):
              <form method="POST" action="/odjava/">
                <button class="button is-light">
                  Odjavi se
                </button>
              </form>
              % else:
              <a class="button is-light" href="/prijava/">
                <strong>Prijavi se</strong>
              </a>
              % end
            </div>
          </div>
          <a class="navbar-item" href="https://github.com/JanKastelic/Projektna-naloga">
            <span class="icon">
              <i class="fab fa-github"></i>
            </span>
          <span>GitHub</span>
          </a>
        </div>
      </div>
    </nav>
    <section class="section">
      {{!base}}
    </section>
  </body>
</html>