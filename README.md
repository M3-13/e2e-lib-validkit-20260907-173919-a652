# validkit

validkit ist eine kleine, eigenständige Python-Bibliothek mit neun voneinander
unabhängigen, reinen Prüf- und Normalisierungsfunktionen: E-Mail-Prüfung,
Luhn-Prüfziffer, IBAN- und ISBN-13-Validierung, Telefon-Normalisierung,
Entfernen von Akzenten, Maskieren von Geheimnissen, Slug-Erzeugung und
Wertebegrenzung (Clamping). Die Bibliothek kommt ohne Laufzeitabhängigkeiten
aus (nur Standardbibliothek), ist vollständig typannotiert und meldet ungültige
Eingaben mit aussagekräftigen Fehlern.

## Tech-Stack

- **Sprache**: Python
- **Runtime**: Python 3.10+
- **Test-Framework**: pytest (nur als Entwicklungsabhängigkeit)
- **Laufzeitabhängigkeiten**: keine (nur Standardbibliothek)

## Installation

```bash
pip install -e .
```

Ein Import funktioniert ohne Drittpakete:

```python
import validkit
```

## Testlauf

```bash
pytest
```

## Verwendung

Jede der neun Funktionen ist direkt aus dem Paket importierbar:

```python
from validkit import (
    is_valid_email,
    luhn_check,
    is_valid_iban,
    is_valid_isbn13,
    normalize_phone,
    strip_accents,
    mask_secret,
    slugify,
    clamp,
)
```

### Beispiele

| Funktion | Aufruf | Ergebnis |
| --- | --- | --- |
| `is_valid_email` | `is_valid_email("user@example.com")` | `True` |
| `luhn_check` | `luhn_check("79927398713")` | `True` |
| `is_valid_iban` | `is_valid_iban("DE89370400440532013000")` | `True` |
| `is_valid_isbn13` | `is_valid_isbn13("9780306406157")` | `True` |
| `normalize_phone` | `normalize_phone("030 1234567", "DE")` | `"+49301234567"` |
| `strip_accents` | `strip_accents("café naïve")` | `"cafe naive"` |
| `mask_secret` | `mask_secret("abcdefgh")` | `"****efgh"` |
| `slugify` | `slugify("Héllo Wörld!")` | `"hello-world"` |
| `clamp` | `clamp(5, 0, 10)` | `5` |

## Funktionsumfang

- `is_valid_email` – prüft, ob eine E-Mail-Adresse gültig ist
- `luhn_check` – prüft eine Ziffernfolge mit der Luhn-Prüfziffer
- `is_valid_iban` – prüft eine IBAN inklusive Prüfziffer
- `is_valid_isbn13` – prüft eine ISBN-13 inklusive Prüfziffer
- `normalize_phone` – normalisiert eine Telefonnummer nach E.164
- `strip_accents` – entfernt diakritische Zeichen aus einem Text
- `mask_secret` – maskiert einen geheimen Text bis auf die letzten Zeichen
- `slugify` – wandelt Text in einen URL-freundlichen Slug um
- `clamp` – begrenzt einen Wert auf ein Intervall
