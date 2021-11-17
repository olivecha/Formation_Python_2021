"""
Programme additionnant une liste de nombres
"""

def addition(nombres):
    somme = 0
    for nombre in nombres:
        somme += nombre

    return somme

# Exemple
print(addition([1, 2, 3]))
# >>> 6
