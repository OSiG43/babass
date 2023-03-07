from tkinter import *

Resultat = {"Iron man": 8, "Hulk": 7, "BlackWidow": 5, "Captain América": 10, "Thor": 7, "Spider man": 6, "Ant Man": 4, "Blanc": 2}
titrevote = 'Vote pour la meilleur Avenger'
long, larg = 450, 650
"""
Définition de la fonction affichant le résultat final d'un vote sur l'écran FT de la Babas 
Elle prend comme parametre le dictionnaire contenant les résultats du vote 
"""

def affichage_resultat(Resultat):
    """
    Création de la fenètre d'affichage
    """
    fenetre = Tk()
    fenetre.geometry(str(long) + "x" + str(larg))
    fenetre.title('Résultats')

    """
    Création de trois widgets contenant le texte du titre du vote , de la liste des candidats et du nombre de vote obtenus
    Pour que le placement de ces widgets et la taille de l'écriture s'adaptent à la taille de l'écran j'ai utilisé des coefficients
    qui divisent les parametres de longueur et de largeur de l'écran que j'ai déterminé au filing pour que ça rende à peu près bien
    """
    Titre_vote = Label(fenetre, text=titrevote, relief=GROOVE, width=30, height=2, font=("", int(long / 40)))
    Titre_vote.pack()

    Candidats = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Candidats.place(x=10, y=larg / 8, width=long / 2.5)
    Label(Candidats, text="Liste des candidats", height=0, width=int(long / 22.5), font=("", int(long / 45))).pack(
        padx=2, pady=2)

    Votes = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Votes.place(x=long - int(long / 2.5) - 10, y=larg / 8, width=long / 2.5)
    Label(Votes, text="Nombre de votes", height=0, width=int(long / 22.5), font=("", int(long / 45))).pack(padx=2,
                                                                                                           pady=2)

    """
    Pour l'affichage des résultats j'ai utilisé deux frames, une pour les bucques et une autre pour les nombre de votes obtenus 
    par les candidats. J'ai ensuite crée une fenètre à l'intérieur de chacune des frames dans laquelle j'ajoute au fur et à mesure 
    des panneaux disposés verticalement contenant les bucques et le nombre de vote. Pour chaque panneau, j'ajoute un label avec la 
    la bucque/le nombre de vote que j'obtient en parcourant le dicoctionnaire. J'ai finalement placé ces frames pour que ça rende
    bien à l'affichage. 
    """
    Bucques = Frame(fenetre, borderwidth=0)
    Bucques.place(x=10, y=larg / 4, width=long / 2.5)
    p = PanedWindow(Bucques, width=150, height=300, orient=VERTICAL)
    p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
    for cle in Resultat.items():
        p.add(Label(p, text=cle[0], font=("", int(long / 55)), anchor=CENTER))
    p.pack()

    Nb_votes = Frame(fenetre, borderwidth=0)
    Nb_votes.place(x=long - int(long / 2.5) - 10, y=larg / 4, width=long / 2.5)
    p = PanedWindow(Nb_votes, width=150, height=300, orient=VERTICAL)
    p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
    for valeur in Resultat.items():
        p.add(Label(p, text=valeur[1], font=("", int(long / 55)), anchor=CENTER))
    p.pack()

    """
    Pour finir, j'ai ajouté un boutton pour pouvoir fermer la fentre d'affichage du vote.
    Pour ça j'ai du définir une fonction pour que cela fonctionne (merci Ylan)
    """
    def quitter():
        def faire():
            fenetre.destroy()

        return faire

    bouton = Button(fenetre, text="Fermer", command=quitter())
    bouton.pack(side=BOTTOM)

    fenetre.mainloop()


"""
Note de fin : Bon voila j'ai pas fait grand chose et il y aura surement des trucs à améliorer. Notamment pour l'esthétisme de 
l'affichage par exemple. Déso je commence seulement à vraiment m'intéresser à la programmation c'est pour ça que je suis lent xd 
"""


affichage_resultat(Resultat)