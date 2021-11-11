"""
Example de la syntaxe accessible de Python
"""

# Objectif : Créer une liste de nombres pairs

longueur_liste = 5  # Nombre de chiffres dans la liste
premier_nombre = 2   # Premier nombre
dernier_nombre = premier_nombre + longueur_liste * 2
liste_de_nombres_pairs = []

for nombre in range(premier_nombre, dernier_nombre, 2):
    liste_de_nombres_pairs.append(nombre)

print(liste_de_nombres_pairs)
# [2, 4, 6, 8, 10]
