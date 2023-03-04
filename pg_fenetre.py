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