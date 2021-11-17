"""
Example script for the if, elif, else structure
"""

number = 2

# Je suis évalué en premier
if number == 0:
    # Si la condition est vraie le segment suivant est exécuté et le code termine
    print('Le nombre est zéro')

# Si la première condition n'est pas vraie je suis évalué
elif number % 2 == 0:
    # Si la condition est vraie le segment suivant est exécuté et le code termine
    print('Le nombre est pair')

# Un nombre arbitraire de "elif" peut être utilisé
elif number == 1001:
    print('Le nombre est 1001')

# Si TOUTES Les conditions précédents ne sont pas vraies le code qui suit est exécuté
else:
    print('Le nombre est impair')
