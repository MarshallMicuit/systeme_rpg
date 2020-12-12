import personnages.spark
import personnages.ennemy

# Fonctions d'attaque

def attaque(): #Il faut deux paramètres attaquant et défenseur
    degats = personnages.spark.attaque - personnages.ennemy.defense_temporaire
    personnages.ennemy.pv = personnages.ennemy.pv - degats
    print("{} inflige {} dégats à {}".format(personnages.spark.nom, degats, personnages.ennemy.nom))
    choix_utilisateur = "R"

def attaque2(): # voué à disparaître
    degats = personnages.ennemy.attaque - personnages.spark.defense_temporaire
    personnages.spark.pv = personnages.spark.pv - degats
    print("{} inflige {} dégats à {}".format(personnages.ennemy.nom, degats, personnages.spark.nom))
    choix_utilisateur = "R"

# Fonctions de défense

def defense():
    personnages.spark.defense_temporaire = personnages.spark.defense + 20
    print("{} se prépare a encaisser le choc".format(personnages.spark.nom))
    choix_utilisateur = "R"

def defense2():
    personnages.ennemy.defense_temporaire = personnages.ennemy.defense + 20
    print("{} se prépare a encaisser le choc".format(personnages.ennemy.nom))    
    choix_utilisateur = "R"