


def recuperer_mot_masque(mot_complet, lettres_trouvees):
    """Cette fonction renvoie le mot masqué, partiellement découvert ou non

    On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
    n'a pas encore trouvées."""
    
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque

def run():
    # Nombre de coups par partie
    nb_coups = 8

    # Mot à découvrir
    mot_a_trouver = "alphabet"

    # Variable pour stocker les lettres trouvées
    lettres_trouvees = []

    # On récupère un nom d'utilisateur
    utilisateur = input("Tapez votre nom: ")

    print("Bienevenue ",utilisateur," jouons ensemble")
    
    # Intialisation de la partie
    mot_trouve = '*'*len(mot_a_trouver)    #recuperer_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    
    # Traitement de la partie
    while mot_a_trouver!=mot_trouve and nb_chances>0:

        print("Mot à trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
        lettre = input("Tapez une lettre: ").lower()

        # La lettre a déjà été choisie
        if lettre in lettres_trouvees: 
            print("Vous avez déjà choisi cette lettre.")
        # La lettre est dans le mot à trouver
        elif lettre in mot_a_trouver: 
            print("Bien joué.")
        # La lettre n'est pas dans le mot à trouver
        else:
            nb_chances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")
        lettres_trouvees.append(lettre)
        mot_trouve = recuperer_mot_masque(mot_a_trouver, lettres_trouvees)

    # A-t-on trouvé le mot ou nos chances sont-elles épuisées ?
    if mot_a_trouver==mot_trouve:
        print("Félicitations ! Vous avez trouvé le mot {0}.".format(mot_a_trouver))
    else:
        print("PENDU !!! Vous avez perdu.")

run()
