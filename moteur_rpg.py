import personnages.spark
import personnages.ennemy
import actions_combat

combat_cours = True
nb_tours = 1

# Module de test pour arrêter le combat
# def test_mort():
#     for i in [0]:
#         if (personnages.spark.pv) < 1:
#             print("Terminé ! \n", personnages.ennemy.nom, "gagne le match")
#             break
#         if (personnages.ennemy.pv) < 1:
#             print("Terminé ! \n", personnages.spark.nom, "gagne le match")
#             break

while combat_cours:
    
    # Tour du J1
    # On teste si un personnage est mort
    if (personnages.spark.pv) < 1:
        print("Terminé ! \n{} gagne le match en {} tour(s)".format(personnages.ennemy.nom, nb_tours))
        break
    if (personnages.ennemy.pv) < 1:
        print("Terminé ! \n{} gagne le match en {} tour(s)".format(personnages.spark.nom, nb_tours))
        break

    personnages.spark.defense_temporaire = personnages.spark.defense
    # Réinitialise la défense du personnage en cas d'action défendre

    print("Tour du J1\n")
    print("Joueur 1 : {} ({} pv)".format(personnages.spark.nom, personnages.spark.pv))
    print("Joueur 2 : {} ({} pv)".format(personnages.ennemy.nom, personnages.ennemy.pv))
    print("Actions : (A)ttaquer, (D)éfendre, (C)ompétences, (O)bjets, (S)tatut")
    choix_utilisateur = str(input("Choix ? (Lettre entre parenthèse) "))
    
    # Pour l'instant on a qu'un choix, c'est l'attaque
    if choix_utilisateur.lower() == "a":
        # try:
        #     choix_utilisateur = str(choix_utilisateur)
        # except TypeError:
        #     print("Entrez la lettre entre parenthèses")
        #     choix_utilisateur = "R"
        # continue
    # Là on compare les valeurs d'attaque et de défense des fiches et on fait une soustraction pour 
    # voir de combien sont les dégâts infligés
        actions_combat.attaque()
        
    if choix_utilisateur.lower() == "d":
        actions_combat.defense()
        # On augmente la défense du joueur de 75%
        # def1*1.75
        # choix_utilisateur = "R"

    # if choix_utilisateur.lower() == "c":
        # On récupère la liste des compétences du joueur pour pouvoir déduire leur coût et appliquer leurs effets
        
        # Dépend du choix mais en gros mana1 - cout_competence
        # choix_utilisateur = "R"

    # if choix_utilisateur.lower() == "o":
        # Récupère la liste des objets du joueur pour pouvoir l'utiliser pendant le tour du combat.
        # telobjet -= 1
        # if telobjet < 1
            #supprimer objet de la liste
    # else
        #On fait R

    # Tour du J2
    # On teste si un personnage est mort
    if (personnages.spark.pv) < 1:
        print("Terminé ! \n{} gagne le match en {} tour(s)".format(personnages.ennemy.nom, nb_tours))
        break
    if (personnages.ennemy.pv) < 1:
        print("Terminé ! \n{} gagne le match en {} tour(s)".format(personnages.spark.nom, nb_tours))
        break

    personnages.ennemy.defense_temporaire = personnages.ennemy.defense
    # Réinitialise la défense du personnage en cas d'action défendre

    print("Tour du J2\n")    
    print("Joueur 2 : {} ({} pv)".format(personnages.ennemy.nom, personnages.ennemy.pv))
    print("Joueur 1 : {} ({} pv)".format(personnages.spark.nom, personnages.spark.pv))
    print("Actions : (A)ttaquer, (D)éfendre, (C)ompétences, (O)bjets, (S)tatut")
    choix_utilisateur = str(input("Choix ? (Lettre entre parenthèse) "))
    
    # Pour l'instant on a qu'un choix, c'est l'attaque
    if choix_utilisateur.lower() == "a":
        # try:
        #     choix_utilisateur = str(choix_utilisateur)
        # except TypeError:
        #     print("Entrez la lettre entre parenthèses")
        #     choix_utilisateur = "R"
        # continue
    # Là on compare les valeurs d'attaque et de défense des fiches et on fait une soustraction pour 
    # voir de combien sont les dégâts infligés
        actions_combat.attaque2()

    if choix_utilisateur.lower() == "d":
        actions_combat.defense2()

    nb_tours += 1