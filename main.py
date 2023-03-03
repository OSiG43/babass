from tkinter import *

"""Le fichier CSV doit etre au format nom;prenom;bucque;fam's   
LES SEPARATEURS SONT DES POINTS6virgules"""


"""
Nom_des_variables:
Proms=[[PG1],[PG2],[PG3]...]
[PG1]=[nom,prenom,bucque,fams]

PG_se_présentant=[PG11,PG25,PG36]
Votes=[Votes_pou_PG11,Votes_pou_PG25,Votes_pou_PG36]

PG_pas_votés=[PG8,PG9,PG10] #liste de tous ceux qui ont pas voté


"""





###
#Vue PG_avec _le noms des gens qui se présentent
###

###
#Vue PG ayant voté (ecran d'attente avant selection par la SDT
###

###
#Vue FT et selection des pg
###

###
#Vue ou on rentre les constantes ( nom du vote / nb de postes dispo / nom des gens qui se presntent )
###



# Fonction de recherche dans la listedes PG
# entree une chaine de caractere
#sortie tous les PG qui ont la chaine de caractère contenue


def recherche()  : #permet de faire une recherche d'un nom, prenom, bucque ou fam's
    pass


# Fonction qui ajoute le vote du pg et enleve son nom des gens qui n'ont pas votés
# entree la selection du pg
#sortie liste=[votes_personne_1_qui_se présente,votes_personne_2_qui_se présente,votes_personne_3_qui_se présente]
#ex: si il y a un PG a élire et 3 pg qui se présentent pg_se_presentant=[PG1,PG2,PG3] Votes=[12,56,3] et liste mise a jour a chaque fois


def vote_du_pg():
    pass

# Fonction qui permet de sauver sur un fichier l'etat du vote (nombre de voix + pg ayant pas votes) qui peut etre exporté a tout moment
# entree liste Pg_pas_voté et liste votes
#sortie tous les PG qui ont la chaine de caractère contenue

def sauvegarde():
    pass

# Fonction qui permet d'annuler le dernier vote en cas d'erreur (ON NE LE FAIT PAS REVOTER DANS CETTE FONCTION)
# entree dernier vote, nom du pg
# sortie : nom pg dans pg_pas_vote, votes remis dans le cas d'avant

def annulation():
    pass
""