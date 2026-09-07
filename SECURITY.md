VERDICT: APPROVED

## Sicherheitsbericht

Geprüft gegen die Sicherheitskriterien **AC-14**, **AC-15** und **AC-16** sowie allgemein auf Secrets, Injection, AuthN/AuthZ, Abhängigkeiten und Konfiguration/Transport.

### Erfüllte Sicherheitskriterien

- **AC-14:** Alle Zeichenketten-Eingaben der neun Funktionen werden über `validkit/_validation.py::_check_length` vor der eigentlichen Verarbeitung auf maximal 1024 Zeichen geprüft. Bei Überschreitung wird ein `ValueError` ausgelöst, bevor reguläre Ausdrücke oder Normalisierungsschleifen laufen. `clamp` verarbeitet keine Zeichenketten und fällt daher nicht unter das Kriterium.
- **AC-15:** Im Produktcode unter `validkit/*.py` sind keine Aufrufe von `eval`, `exec`, `compile`, `pickle.loads` oder `subprocess` sichtbar. Der Test `tests/test_skeleton.py` prüft dies zusätzlich per Quelltextscan.
- **AC-16:** `mask_secret` verwendet ausschließlich Fehlermeldungen ohne den übergebenen Geheimtext (`"keep must be an integer"`, `"keep must be >= 0"`). Auch `_check_length` gibt Eingaben nicht in der Fehlermeldung aus. Die vorhandenen Tests decken diesen Punkt ab.

### Scanner-Auswertung

- **bandit:** wurde nicht ausgeführt (`[skipped] bandit not installed`).
- **semgrep:** wurde nicht ausgeführt (`[skipped] semgrep not installed`).

Die fehlenden Scanner-Ergebnisse sind kein Beleg für eine Schwachstelle. Die sichtbare Codebasis wurde manuell geprüft.

### Befunde

Keine.

### Anmerkungen (nicht blockierend)

- In `validkit/luhn.py` wird `_check_length` vor der `isinstance`-Prüfung aufgerufen. Bei einer Nicht-String-Eingabe wie `12345` entsteht dadurch ein relativ unschöner `TypeError` aus `len()`, statt der expliziten Meldung `"digits must be a string"`. Dies ist kein Sicherheitsproblem und verletzt kein Kriterium, wäre aber eine kleine Robustheitsverbesserung.
- Da weder bandit noch semgrep installiert waren, empfiehlt es sich, vor einem produktiven Release einmalig eine automatisierte SAST-Prüfung laufen zu lassen.