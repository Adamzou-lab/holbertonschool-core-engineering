#!/usr/bin/env python3
alphabet = ""
for lettre in range(97, 123):
    if chr(lettre) == "q" or chr(lettre) == "e":
        continue
    alphabet += chr(lettre)
print(alphabet)
