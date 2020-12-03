import rpg.personnages.spark
import rpg.personnages.ennemy

combat_cours = True

# Module de test pour arrêter le combat
# def test_mort():
#     for i in [0]:
#         if (rpg.personnages.spark.pv) < 1:
#             print("Terminé ! \n", rpg.personnages.ennemy.nom, "gagne le match")
#             break
#         if (rpg.personnages.ennemy.pv) < 1:
#             print("Terminé ! \n", rpg.personnages.spark.nom, "gagne le match")
#             break

while combat_cours:
    
    # Tour du J1
    # On teste si un personnage est mort
    if (rpg.personnages.spark.pv) < 1:
        print("Terminé ! \n", rpg.personnages.ennemy.nom, "gagne le match")
        break
    if (rpg.personnages.ennemy.pv) < 1:
        print("Terminé ! \n", rpg.personnages.spark.nom, "gagne le match")
        break
    print("Tour du J1\n")
    print("Joueur 1 : ", rpg.personnages.spark.nom, "(", rpg.personnages.spark.pv, "pv)")
    print("Joueur 2 : ", rpg.personnages.ennemy.nom, "(", rpg.personnages.ennemy.pv, "pv)")
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
        degats = rpg.personnages.spark.attaque - rpg.personnages.ennemy.defense
        rpg.personnages.ennemy.pv = rpg.personnages.ennemy.pv - degats
        print(rpg.personnages.spark.nom, "inflige", degats, "dégats à", rpg.personnages.ennemy.nom)
        choix_utilisateur = "R"

    # if choix_utilisateur.lower() == "d":
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
    if (rpg.personnages.spark.pv) < 1:
        print("Terminé ! \n", rpg.personnages.ennemy.nom, "gagne le match")
        break
    if (rpg.personnages.ennemy.pv) < 1:
        print("Terminé ! \n", rpg.personnages.spark.nom, "gagne le match")
        break
    print("Tour du J2\n")    
    print("Joueur 2 : ", rpg.personnages.ennemy.nom, "(",rpg.personnages.ennemy.pv, "pv)") 
    print("Joueur 1 : ", rpg.personnages.spark.nom, "(",rpg.personnages.spark.pv, "pv)")
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
        degats = rpg.personnages.ennemy.attaque - rpg.personnages.spark.defense
        rpg.personnages.spark.pv = rpg.personnages.spark.pv - degats
        print(rpg.personnages.ennemy.nom, "inflige", degats, "dégats à", rpg.personnages.spark.nom)
        choix_utilisateur = "R"