from tkinter import *
from tkinter import filedialog as fd

long, larg = 450, 650
titrevote = ""    ### variable global contenant le titre du vote à consulter et qui sera utilisé pour l'affichage des résultats 
nom= ""    ### variable globale contenant le nom du vote à afficher et qui sera utilisé pour lire le fichier du vote à consulter 
arret=0    ### variable globale permettant l'arret du programme d'affichage 

'''
fonction permettant de connaitre le chemin d'un ancien vote sélectionné par un pg qui est enregistré dans la raspberry en csv
'''
def select_ancien_vote():
    def callback():                                      ### définition de la commande 
       global nom,titrevote
       chemin="C:/Users/evanl/Documents/ENSAM/Rezal"     ### définition du chemin d'enregistrement des anciens votes (à modifier)
       nom=fd.askopenfilename(initialdir = chemin)
       titrevote=nom[-(len(nom)-len(chemin)-1):-4]       ### Récupération du titre du vote = nom du fichier. ex: 'Vote pour le Zt pokemon 222'
       if nom!="":
          fenetre.destroy()
    fenetre=Tk()
    fenetre.geometry(str(long) + "x" + str(larg))
    Button(text='Cliquer içi pour sélectionner un vote',font=('',12),command=callback).pack(fill=X)          
    def quitter():
        def faire():
            global arret
            fenetre.destroy()
            arret=1               ### J'affecte une valeur à cette variable globale pour fermer le programme et arrêter la boucle d'affichage quand le pg ne veut plus consulter de vote                                    
        return faire
    bouton = Button(fenetre, text="Fermer", command=quitter())
    bouton.pack(side=BOTTOM)
    fenetre.mainloop()

'''
fonction permettant d'extraire les données du fichier selctionné et qui retourne un dictionnaire avec les résultats du vote
Le fichier doit être en csv et doit contenir deux colonnes : une pour les bucques des candidats et une autre pour leur nombre de vote 
ainsi que d'une en-tête d'une ligne (la stucture peut être modifiée)
'''
def resultat_ancien_vote():
    fh=open(nom,"r")
    data=fh.readlines()
    fh.close()
    Bucque,Nbvote=[],[]
    Resultat={}
    for i in range(1,len(data)):
        ligne=data[i].split(";")
        try:
           Bucque+=[ligne[0]]
           Nbvote+=[ligne[1].rstrip('\n')]
        except:
            print("rerreur ligne"+str(i))
    u=0
    for j in Bucque:
        Resultat[j]=Nbvote[u]
        u+=1
    return(Resultat)
    
'''
Réutilisation de la fonction qui permet l'affichage des résultats
'''    
def affichage_resultat(Resultat):
    fenetre = Tk()
    fenetre.geometry(str(long) + "x" + str(larg))
    fenetre.title('Résultats')
    Titre_vote = Label(fenetre, text=titrevote, relief=GROOVE, width=30, height=2, font=("", int(long / 40)))
    Titre_vote.pack()
    Candidats = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Candidats.place(x=10, y=larg / 8, width=long / 2.5)
    Label(Candidats, text="Liste des candidats", height=0, width=int(long / 22.5), font=("", int(long / 45))).pack(
        padx=2, pady=2)
    Votes = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Votes.place(x=long - int(long / 2.5) - 10, y=larg / 8, width=long / 2.5)
    Label(Votes, text="Nombre de votes", height=0, width=int(long / 22.5), font=("", int(long / 45))).pack(padx=2,pady=2)
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
    def quitter():
        def faire():
            fenetre.destroy()
        return faire
    bouton = Button(fenetre, text="Fermer", command=quitter())
    bouton.pack(side=BOTTOM)
    fenetre.mainloop()

'''
fonction ultime regrouppant les fonctions précédentes et qui permet de sélectionner et visualiser les résultats d'un ancien vote 
'''
def affichage_ancien_vote():
    global arret
    while arret ==0:               ### tant que le pg n'a pas cliqué sur le bouton quitter du menu de sélection le programme lui demandera si il veut consulter un vote 
      select_ancien_vote()
      if arret ==0:
         affichage_resultat(resultat_ancien_vote())
    arret=0                        ### permet de réinitialiser la variable globale après avoir quitter le menu de sélection 
    
    
'''
Note de fin : Je n'ai pas réussi a fusionner en une seule fonction ce code c'est pour ça qu'il est découpé en plusieurs parties.
Je n'ai également pas pu me passer de l'utilisation des variables globales. 
Pour finir, il faudra prévoir un bouton dans le menu principale pour pouvoir activer ce programme et également connaitre le chemin 
d'enretrement des fichiers de vote sur la raspberry.
'''
