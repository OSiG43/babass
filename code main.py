    ##Main()
from tkinter import *
"""
import FT
import fenetrePG.py
"""


###code_creation_fenetre
import csv

import os
global sortie_creation_vote
sortie_creation_vote=["nom du vote","chemin du fichier des votants","chemin du fichier des candidats"]
""" commande global
 sortie_creation_vote
filename_creation_vote
filename_creation_vote2
 """

# explorateur de fichier
# Python program to create
# a file explorer in Tkinter


# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer root_vote
def browseFiles():#Attention il faut changer le chemin du fichier
    global filename_creation_vote
    filename_creation_vote = filedialog.askopenfilename(initialdir = "C:/Users/guill/Desktop/Rezal",
                                          title = "Selectionner un fichier",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("Text files",
                                                        "*.txt*")))

    # Change label contents
    label_file_explorer.configure(text="Fichier liste des votants: "+filename_creation_vote)

def browseFiles2():#Attention il faut changer le chemin du fichier
    global filename_creation_vote2
    filename_creation_vote2 = filedialog.askopenfilename(initialdir = "C:/Users/guill/Desktop/Rezal",
                                          title = "Selectionner un fichier",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("Text files",
                                                        "*.txt*")))

    # Change label contents
    label_file_explorer2.configure(text="Fichier liste des candidats: "+filename_creation_vote2)

def validation_du_choix ():
    sortie_creation_vote=[saisie_creation_vote.get(),filename_creation_vote,filename_creation_vote2]
    print(sortie_creation_vote)

def creer_fenetre():

    # Create the root root_vote
    root_vote = Tk()
    root_vote.configure(background='#222222')
    alignx=100

    # Set root_vote title
    root_vote.title('File Explorer')

    # Set root_vote size
    root_vote.geometry("500x500")

    #Set root_vote background color
    root_vote.config(background = "white")

    # Create a File Explorer label
    global label_file_explorer
    label_file_explorer = Label(root_vote,
                                text = "Fichier liste des votants: ",
                                width = 100, height = 4,
                                fg = "blue")
            #"""Je crée ici en double les fenetres pour prendre des infos et explorer les fichiers"""
    global label_file_explorer2
    label_file_explorer2 = Label(root_vote,
                                text = "Fichier liste des candidats: ",
                                width = 100, height = 4,
                                fg = "blue")

    #de même avec les boutons
    button_explore = Button(root_vote,
                            text = "Sélection de la liste des votants",
                            command = browseFiles)
    button_explore2 = Button(root_vote,
                            text = "Sélection de la liste des candidats",
                            command = browseFiles2)

    button_valider= Button(root_vote,
                            text = "Valider",
                            command = validation_du_choix)
    button_exit = Button(root_vote,
                        text = "Exit",
                        command = exit)

    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column = 1, row = 4)
    button_explore.grid(column = 1, row = 5)

    label_file_explorer2.grid(column = 1, row = 6)
    button_explore2.grid(column = 1, row = 7)

    button_exit.grid(column = 1,row = 100)

    button_valider.grid(column = 1,row = 99)
    root_vote.configure(background='#222222')


    label1=Label(root_vote,text = "Nom du vote",bg='#222222',fg='#FFFFFF',font=20) # Juste un titre
    label1.grid(column = 1,row = 1)

    saisie_creation_vote = Entry() # Zone d'entrée du nom du vote
    saisie_creation_vote.grid(column = 1,row = 2)
    root_vote.mainloop()
"""
# Let the root_vote wait for any events
print(sortie_creation_vote)
root_vote.mainloop()

"""
##fenetre PG
'''
-Fonctions global:
Page_vote
entrees
nb_select
'''

from tkinter import*
from random import*

long,larg=800,480 #taille en pxl de l'ecran, a modifier selon ecran

'''
fonction principale du programme, je fais tout les calcule et je creer mon interface, je lance un
Ouvre_Page_vote(Liste_vote,Nom,nb_vote) pour demarrer le programme, Liste_vote c'est la liste avec
le nom de tout les candidats pour qui on peut voter, nom c'est le nom de celui qui vote et
nb_vote c'est le nombre de candidat pour qui je peux voter'
'''
def Ouvre_Page_vote(Liste_vote,Nom,nb_vote):
    global Page_vote,entrees,nb_select #permet de rendre des variable presente en dehors de la fonction, y a Page_vote qui est l'objet de la page sous tk, entrees c'est une listes avec tout les objets des bouttons de candidats et vote blanc en dernier et nb_select le nombre de cadidat selectionner
    entrees=[]#je cree une liste entrees vide que je vais remplir après avec les objets boutton
    nb_select=0#on commence avec un nombre de candidat selectionner de 0
    Page_vote=Tk()#je creer ma page vote
    Page_vote.configure(bg ="#F1EA9C")#je change le background en jaune beige avec comme code hexa #F1EA9C, on peut changer si ça plait pas mais j'aime bien
    Page_vote.title("Page de vote")#je change le nom de la page, useless parce que la page sera en plein ecran mais au cas ou
    Page_vote.geometry(str(long)+"x"+str(larg))# je choisi la taille que doit prendre la page en s'ouvrant et je l'accorde pour qu'elle prenne la taille de l'ecran en entier
    Page_vote.attributes('-fullscreen', True)#mets en plein écran
    shuffle(Liste_vote)

    '''
    mon but la c'est d'avoir un carree de boutton pour que ce soit joli, c'est a dire que je vais
    remplir un carre ligne par ligne de bouton. mais avant je dois alors connaitre le cote
    de ce carre pour qu'il soit le plus opti, pour ça je vais connaitre le carre le plus petit avant le
    nombre de boutton, pour ça je fais int(len(Liste_vote)**0.5)+1 mais ça marche pas si le nombre est
    deja un carre, donc je fais une verif si il est pas carre et je trouve cote
    '''

    if int(len(Liste_vote)**0.5)!=len(Liste_vote)**0.5:
        cote=int(len(Liste_vote)**0.5)+1
    else:
        cote=int(len(Liste_vote)**0.5)


    "creation du text au dessus"
    Text1=Label(Page_vote, text="Salss "+str(Nom)+", clique pour voter",font=("",20),bg ="#F1EA9C")#je precise que le label (zone de texte) est sur la page page_vote, le texte c'est sal'ss avec le nom de celui qui vote, veuiller voter, je regle la police de 20 modifiable et type de police par defaut
    Text1.place(x=0, y=0)#je place la zone de texte en haut a gauche de la page, place marche avec des pxl contrairement a grid! ce qui nous facilitera pour que la page s'adapte a la taille de l'ecran

    '''
    la je vais calculer la largeur et la longueurs de tout les boutton des candidats (validation et blanc compte
    pas), pour long c'est ez, c'est juste longueur page/(nb bouton par cote) le tout en pxl on le rappel.
    pour la largeur je dois verifier qu'il y a assez de candidat pour remplir la dernière ligne du carre
    pour faire la même chose que longeur (je supprime cependant 40 pour la zone de texte du dessus qui est
    aussi modifiable et 100 pour la largeur des bouton de valdiation et blanc). Si la dernière ligne n'est
    pas remplis alors j'enlève la ligne en soustrayant 1 au cote. Je pense que mathematiquemnt ce système
    n'est pas correcte pour des nombre de candidats elever dans l'ordre des 50 parce qu'il y aura plus d'une
    ligne non rempli mais la on depasse pas les 20 donc a voir
    '''

    long_but=int(long/cote)#longeur d'un bouton
    if cote**2-cote<len(Liste_vote):
        larg_but=int((larg-40-100)/cote)#largeur d'un bouton
    else:
        larg_but=int((larg-40-100)/(cote-1))

    '''
    je vais ensuite ranger la liste des candidats dans un tableau qui sera exactement le même que
    celui des bouton (ou peut-être pas, j'inverse souvent ligne et colone comme un teube') juste
    la je rajoute un système de ligne, c'est a dire qu'a chaque fois que je complète une ligne,
    i reviens a 0 et ligne augmente de 1. je commence d'un tableau rempli de None pour aussi connaitre
    mes cases vides
    '''

    Tableau=[[None for i in range(cote)]for i in range(cote)]
    ligne=0
    for i in range(len(Liste_vote)):
        if i-ligne*cote>=cote:
            ligne+=1
        Tableau[ligne][i-ligne*cote]=Liste_vote[i]

    '''
    l'heure exitante de creer nos boutons est venu ! pour ça j'explore Tableau et je chope les cases
    non remplis et je creer un tableau avec comme text le nom du candidat
    '''
    for i in range(cote):
        for j in range(cote):
            if Tableau[j][i]!=None:#si la case n'est pas vide
                entree=Button(Page_vote, text=Tableau[j][i],font=(None,20),bg ="#F1EA9C")#je creer un boutton qui est en fait un objet, donc si je parcour plusieur fois cette ligne je creer plusieur boutton avec des instances differentes mais avec toujour la même variable entree, j'attribue a chaque boutton son nom de candidat comme text, inscrit sur la page page_vote, sa couleur jaune et sa police
                entree['command']=change_color(entree,nb_vote)# j'ajoute une commande, c'est a dire une fonction a executer si je clique sur le bouton, voir change_color, celuici reprend l'instance du boutton et le nombre de vote, j'aurais pu mettre la commande dans le parametrage du bouton (ligne au dessus) mais j'ai besoin de slectionner entree qui est l'instance du boutton individuelle pour pouvoir le modifier lui et aucun autre, sauf qu'il n'etais pas encore declarer au dessus LUL
                a=long_but*i#je calcule la position y du bouton avec i qui est le numerau de ma colone et le nb de pxl d'un bouton
                if Tableau[j][-1]==None:#pour centrer la dernière ligne qui n'est pas forcement complète, je vais verifier que la dernière case de la ligne n'existe pas, sinon je passe
                    a+=(cote-(len(Liste_vote)%cote))*long_but/2 # je trouve alors le nombre de pxl de bouton manquant pour avoir une ligne complète avec (cote-(len(Liste_vote)%cote))*long_but que je divise par 2 et que j'additionne a toute la ligne pour avoir un espace a gauche et decaler tout les boutons
                entree.place(x=a, y=40+j*larg_but,height=str(larg_but),width=str(long_but)) # je place mon bouton selon x que j'ai caluler avant et y qui est largeur_bouton*numero de ligne, je rajoute aussi avec height et width la largeur et longeur du bouton
                entrees.append(entree)#j'enregistre mon instance dans la listes des entrees

    '''
    je creer mon bouton valider et blanc
    '''

    valider=Button(Page_vote,text="valider", command=validation(Liste_vote,nb_vote), bg="green",font=("",20))# comme d'hab, sinon que j'utilise une fonction valider a la fin
    valider.place(x=long/2,y=larg-100,height=str(100),width=str(long/2))# je place le bouton pour qu'il soit en bas a droite de l'ecran et prennent la moitier de l'ecran en longeuru, largeur de 10 pxl

    blanc=Button(Page_vote, command=reset(), text="blanc",font=("",20))
    blanc.place(x=0, y=larg-100,height=str(100),width=str(long/2))# je place le bouton pour qu'il soit en bas a gauche de l'ecran et prennent la moitier de l'ecran en longeuru, largeur de 10 pxl

    entrees.append(blanc) # je rajoute aussi blanc dans les entrees

    Page_vote.mainloop()# boucle de tk obligatoir pour une page

'''
je souhaite que quand je selectionne un bouton, celui-ci m'affiche que je le selectionne et que je le garde,'
fonction qui permet en connaissant le boutton que j'ai tape, de le changer en gris si il etait jaune et inversement
deplus si je clique sur un bouton alors le boutton blanc etait gris, alors je dois le remettre blanc. deplus je
ne peux pas mettre plus de boutton gris que le nombre de vote.
'''

def change_color(entree,nb_vote):
    def do_it():#quand je creer une modif a partir d'une commande, tk vas l'executer directement et donc mon boutton sera directement gris au lancement. mais je peux contourner le problème en creant une fonction  dans la fonction et je mets mes modifs dessus
        global nb_select, entrees#toujours en commun les fonction du nombre selectionner et des instances de mes boutons
        if entree["bg"]=="#F1EA9C" and nb_select<nb_vote: # si mon bouton etais jaune et que j'ai une selection plus petite que le nombre de vote,
            entree["bg"] ="grey" #alors je peux le colorier en gris
            entrees[-1]["bg"]="white"#je remet le boutton blanc en blanc qqs la couleur d'avant, pour rappelle la dernière instance de entree est toujours blanc
            nb_select+=1# je rajoute un au nombre selectionner
        elif entree['bg']=="grey":# si il etais gris
            entree["bg"] ="#F1EA9C"# je le retransforme een jaune
            nb_select-=1# j'enlève 1 a ma selection
    return do_it

'''
je souhaite que lorsque je clique sur blanc, blanc deviens gris et inversement, deplus je veux que mes
autres bouton soit redevienne jaune pour ne plus être selectionner
'''

def reset():
    def do_it():
        global nb_select, entrees
        if entrees[-1]["bg"]=="white":
            entrees[-1]["bg"] ="grey"
            nb_select=0
            for i in range(len(entrees)-1):# je parcour toutes mes instances de bouton sauf la dernière qui est le bouton blanc
                entrees[i]["bg"]="#F1EA9C"# je le remet en jaune
        else:
            entrees[-1]["bg"] ="white"
    return do_it

'''
je souhaite que lorsque j'appuie sur valider, je recupère une liste de tout les bouton selectionner
 soit tout les bouton en gris. Le bouton fonctionne uniquement si j'ai suffisament de vote pour voter
 ou si blanc est select'
 j'ai pas encore de lien avec les autres programme alors je sais pas comment il vont le recuperer, pour
 l'instant je stock tout dans une variable global qui est vote'
'''

def validation(Liste_vote,nb_vote):
    def do_it():
        global entrees,nb_select,vote
        vote=[]
        if nb_select==nb_vote or entrees[-1]["bg"]=="grey":#si j'ai suffisament de vote pour voter ou si blanc est select
            for i in entrees:# je parcour tout mes boutons
                if i["bg"]=="grey" :# si y en a un qui est gris, j'ajoute le text du bouton a la liste vote, si j'ai voter blanc alors je n'aurais que blanc en gris et je retrouverais dans ma liste que blanc'
                    vote.append(i["text"])
            Page_vote.destroy()# je supprime la page
        print(vote)
    return do_it

'''
petit mot pour la fin: sqrt(29μ93) les plus grands crapal's de KIN
aussi compilez sur la bell'eff'situde de la 57μ(16-128) la fam's qui pine le plus et dort le moin!
Bercerf'k 57μ(16-128)
'''




###FT
from tkinter import *

arretrecherche=False #Variable de retour de recherche (soit une bucque soit True si on veut afficher les résultats)
alignx=100 # alignement des wedgets
bucque='' # variable de retour de l'entrée texte (fenetreinitiale)

def recherche(a):

# Fonction de recherche dans la liste déroulante


    def rechercheoccurence(a)  :
        if type(saisie.get())==str :
            if len(saisie.get())>0 : # Si il y a qque chose de rentré
                listeaffiche.delete(0,len(ListePG)) # On commence par tout effacer
                for i in range (0,len(ListePG)) : # On se ballade dans notre liste de PG
                    sommeoccurences=0
                    for j in saisie.get().split(" ") : # On sépare la recherche du FT en plusieurs strings
                        if ListePG[i].find(j)!=-1 : # Si il y a une occurence, on incrémente notre compteur
                            sommeoccurences=sommeoccurences+1
                    if sommeoccurences >= len(saisie.get().split(" ")) : # On vérifie qu'il y ai autant d'occurences que de mots du FT
                        listeaffiche.insert('end',ListePG[i].replace(";"," ")) # On insère les occurences en retirant les ;
            else : # Au cas où le FT revient à une entrée nulle, on refresh la liste
                listeaffiche.delete(0,len(ListePG)) # On supprime les non-occurences
                for item in ListePG :
                    listeaffiche.insert('end',item[:-1].replace(";"," "))

# Création du titre


    label1=Label(root,text = "Choisir le PG votant",bg='#222222',fg='#FFFFFF',font=20) # Juste un titre
    label1.place(x=alignx,y=10)


# Création de la liste déroulande des PG


    def selecpg(a) :
        global arretrecherche
        arretrecherche=listeaffiche.get(listeaffiche.curselection())
        print(arretrecherche)
        root.quit()

    listeaffiche = Listbox(root, listvariable=StringVar()) # Liste des PG correspondants
    PROMS=open("PROMS.csv", "r")
    ListePG=PROMS.readlines() # On importe tout nos PG dans une liste
    PROMS.close()
    listeaffiche.bind_all('<Return>', selecpg)
    listeaffiche.bind_all('<Double-1>', selecpg)

    for item in ListePG: # On se déplace dans notre liste pour les ajouter à notre liste déroulante
        listeaffiche.insert('end',item[:-1].replace(";"," "))
    listeaffiche.place(x=alignx,y=100)


# Création de la zone de saisie par le FT




    saisie = Entry(root) # Zone d'entrée de la bucque
    saisie.place(x=alignx,y=50)
    saisie.bind_all('<Key>', rechercheoccurence) # Quand il y a une touche pressée on lance la fonction recherche



# Boutton d'annulation

    def boutonpress() : #fonction permettant de quitter la fênetre quand le bouton d'affichage des résultats est préssé
        global arretrecherche
        arretrecherche=True
        print(arretrecherche)
        root.quit()

    bouton = Button(text = "Fin du vote",command = boutonpress)
    bouton.place(x=alignx,y=300)

    root.mainloop()


def fenetreinitiale (texte) : #fenêtre avec une zone d'entrée de bucque'
    def entree(a) :
        global bucque
        bucque=saisie.get()
        root.quit()

    label1=Label(root,text = texte,bg='#222222',fg='#FFFFFF',font=20) # Juste un titre
    label1.place(x=alignx,y=10)

    saisie = Entry(root) # Zone d'entrée de la bucque
    saisie.place(x=alignx,y=50)
    saisie.bind_all('<Return>', entree)
    root.mainloop()

###affichage résultat

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
###
def initialisation():

    global verification
    verification=True#permet d'arreter le vote si on passe cette variable sur False
    Dicti_résultat={}#résultat du vote par candidat
    CMD=0
    l_var_global=[CMD,verification,Dicti_résultat]





def afficher_liste():

    pass

def incrementation_resultat(liste_des_choix,Dicti_résultat):
    #liste de nom ou de valeurs avec les choix du votant
    for i in vote:
        Dicti_résultat.update({i:Dicti_résultat[i]+1})


def lancer_vote():
    menu_accueil.destroy()
    initialisation()
    creer_fenetre()
    nom_du_vote=sortie_creation_vote[0]
    path_liste_votants=sortie_creation_vote[1]
    path_liste_candidats=sortie_creation_vote[2]
    """
    sortie de vote est une liste de chaine de caractère contenant les choix du votant ex:['Pierre', 'Baptiste', 'GrosGay']
    """
    while verification :
        fenetrePG(PROMS, nom, nb_de_vote)
        fenetreinitiale (texte)
        incrementation_resultat (vote,Dicti_résultat)


# création de la fenêtre de menu
alignx=10
menu_accueil=Tk()
menu_accueil.configure(background='#222222') # Fond
label_titre_1=Label(menu_accueil,text = "Menu d'accueil'",bg='#222222',fg='#FFFFFF',font=20) # Juste un titre
label_titre_1.place(x=alignx,y=10)

bouton_afficher_liste = Button(text = "Afficher une liste",command=afficher_liste())
bouton_afficher_liste.place(x=alignx,y=50)

bouton_lancer_vote = Button(text = "Lancer un vote",command=lancer_vote)
bouton_lancer_vote.place(x=alignx,y=100)

menu_accueil.mainloop()
"""
if CMD==1 :
    afficher_liste()# code pour chercher dans les fichier et afficher une liste

else:
    dossier_vote=creation_vote()# donne le nom du vote apparaissant dans les fichiers, la matrice des résultats initialisée avec les noms des candidats,le chemin vers le csv contenant la liste de proms (SOUS FORME DE DICTIONNAIRE)
    nom_vote,liste_résultat,liste_votants=dossier_vote
    for i in liste votant:
        dicti_résultat{i} =0

"""
    #à ce stade la c'est censé etre pret à lancer le vote

"""
    code de vote
    boucle while:
    alternance de fonction FT vérification et PG

    FT
    Entrée:Rien
    Sortie: nom  du votant


    PG
    Entrée:Liste des candidats, nom du PG votant, nombre de vote
    Sortie: renvoie une liste stockée en global avec le vote du PG qui passe.

while verification :
    PG(PROMS, nom, nb_de_vote)
    FT()
    incrémentation_résultat (SortiePG)
"""

"""
    incrémente la matrice des résultats ici un dictionnaire nommé Dicti_résultat
    """

"""

"""
"""
Fichier_sortie=open(nom_vote,"r+")
for i in Dicti_résultat:
    Fichier_sortie.writelines(i[0])#nom des candidats
    Fichier_sortie.writelines(i[1])#nombre de vote
Fichier_sortie.close()
menu_accueil.mainloop()
"""