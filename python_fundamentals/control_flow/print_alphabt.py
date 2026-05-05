#!/usr/bin/env python3
import string
for lettre in string.ascii_lowercase:
    if lettre == "q" or lettre == "e":
        continue
    print(lettre, end="")
print()
