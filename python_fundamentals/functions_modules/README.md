# Python — Functions & Modules

---

## Exercice 0 — islower

**Leçon** : utiliser `ord()` pour comparer des caractères via leur code ASCII plutôt que des méthodes built-in. Une condition booléenne se retourne directement sans `if/else`.

```python
def islower(c):
    return 97 <= ord(c) <= 122
```

---

## Exercice 1 — uppercase

**Leçon** : parcourir une string avec `for c in str`, construire un résultat progressivement avec `+=`, et comprendre la différence entre `print` et `return`. Conversion ASCII avec `ord()` et `chr()` — différence de 32 entre minuscule et majuscule.

```python
def uppercase(str):
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
```

---

## Exercice 2 — print_last_digit

**Leçon** : `%` pour extraire le dernier chiffre, `abs()` pour toujours avoir un résultat positif. Une fonction peut à la fois `print` ET `return` — ce ne sont pas les mêmes choses.

```python
def print_last_digit(number):
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return digit
```

---

## Exercice 3 — pow

**Leçon** : implémenter une puissance manuellement avec une boucle et un accumulateur qui commence à `1` (neutre de la multiplication). Gérer les exposants négatifs avec `abs()` et `1 / result`. Le cas `b = 0` est géré automatiquement car la boucle tourne zéro fois.

```python
def pow(a, b):
    result = 1
    if b < 0:
        for i in range(abs(b)):
            result = result * a
        result = 1 / result
    else:
        for i in range(b):
            result = result * a
    return result
```

---

## Exercice 4 — Script Execution & Import Behavior

**Leçon** : Python exécute un fichier entièrement à l'import. `__name__` vaut `"__main__"` si le fichier est lancé directement, ou le nom du fichier (sans `.py`) s'il est importé. La garde `if __name__ == "__main__":` protège le code d'exécution des effets de bord.

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(3, 5))
```

| Situation | Valeur de `__name__` |
|---|---|
| `python3 fichier.py` | `"__main__"` |
| `import fichier` | `"fichier"` |

---

## Exercices 5, 6, 7 — Imports

**Leçon** : `from ... import` fonctionne pour les fonctions, plusieurs fonctions à la fois, et les variables. Toujours mettre les imports au top level et le code d'exécution dans la garde.

```python
# Une fonction
from add_0 import add

# Plusieurs fonctions
from calculator_1 import add, sub, mul, div

# Une variable
from variable_load_5 import a
```

---

## Règles à retenir

- **Définitions** (`def`, `import`) → top level
- **Exécution** (`print`, variables, appels) → dans `if __name__ == "__main__":`
- **`ord()`** : caractère → code ASCII
- **`chr()`** : code ASCII → caractère
- **`abs()`** : valeur absolue (toujours positif)
- **`%`** : modulo (reste de la division)