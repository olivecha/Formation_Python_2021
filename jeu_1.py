import random

print('Bienvenue à devine le nombre entre 0 et 10!')
nombre = random.randint(0, 10)
nombre_utilisateur = -1  # Un nombre impossible d'être égal au nombre de l'ordinateur

while nombre_utilisateur != nombre:
    # Les 'input' sont toujours des strings alors on les transforme en 'int'
    nombre_utilisateur = int(input("Entrer votre tentative : "))

    if nombre_utilisateur > nombre:
        print('Votre nombre est trop haut')
    elif nombre_utilisateur < nombre:
        print('Votre nombre est trop bas')

# Le else statement s'exécute à la fin de la boucle while
else:
    print('Félicitation vous avez réussi')
