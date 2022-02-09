"""
Jeu du bonhomme pendu
"""
from random import randint

MOTS_DISPONIBLES = ['dauphin', 'plage', 'citron', 'fruit', 'vendeur', 'tigre']

def mot_au_hazard():
    """
    Fonction retournant un mot au hazard
    """
    i = randint(0, len(MOTS_DISPONIBLES) - 1)
    return MOTS_DISPONIBLES[i]

def trouver_lettre(lettre, mot):
    """
    Find if a letter is in a word
    returns the indexes of the letter
    """
    i = 0
    lettre_indexes = []
    for character in mot:
        if character == lettre:
            lettre_indexes.append(i)
        i += 1
    return lettre_indexes


def print_liste(liste):
    """
    Fonction imprimant une liste en une ligne avec des espaces
    """
    string = liste[0]
    for item in liste[1:]:
        string += (' ' + item)

    print(string)
    print('\n')


def bonhomme_pendu(chances=None):
    """
    Fonction pour jouer au bonhomme pendu
    """
    # Prendre un mot au hazard
    mot = mot_au_hazard()
    mot_print = ['_'] * len(mot)
    if chances is None:
        chances = len(mot) * 2

    # Print the header
    print('Bienvenue au jeu du bonhomme pendu')
    print('Votre mot contient ', len(mot), ' Lettres')
    print('Vous avez ', chances, ' chances pour le deviner')
    print('\n')
    # Imprimer le mot vide
    print_liste(mot_print)

    while True:
        # Demander une lettre
        lettre = input('Entrez votre lettre : ')
        print('\n')
        # Trouver si la lettre est dans le mot
        indexes = trouver_lettre(lettre, mot)
        # Remplacer les barre par la lettre là ou elle est dans le mot
        for i in indexes:
            mot_print[i] = lettre

        # Imprimer le mot mis à jour
        print_liste(mot_print)

        if len(indexes) == 0:
            # La lettre n'était pas dans le mot
            chances -= 1
            print("La lettre n'est pas dans le mot, il vous reste ", chances, ' chances...')
            print('\n')

        if '_' not in mot_print:
            print('Vous avez réussi !')
            break

        if chances == 0:
            print('Vous avez perdu :(')
            break
