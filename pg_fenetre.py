from tkinter import* 

long,larg=800,480 #taille en pxl de l'écran, à modifier selon écran

'''
fonction principale du programme, je fais tout les calcule et je créer mon interface, je lance un
Ouvre_Page_vote(Liste_vote,Nom,nb_vote) pour demarrer le programme, Liste_vote c'est la liste avec
le nom de tout les candidats pour qui on peut voter, nom c'est le nom de celui qui vote et 
nb_vote c'est le nombre de candidat pour qui je peux voter'
'''
def Ouvre_Page_vote(Liste_vote,Nom,nb_vote):
    global Page_vote,entrées,nb_select #permet de rendre des variable présente en dehors de la fonction, y a Page_vote qui est l'objet de la page sous tk, entrées c'est une listes avec tout les objets des bouttons de candidats et vote blanc en dernier et nb_select le nombre de cadidat selectionner
    entrées=[]#je crée une liste entrées vide que je vais remplir après avec les objets boutton
    nb_select=0#on commence avec un nombre de candidat selectionner de 0
    Page_vote=Tk()#je créer ma page vote
    Page_vote.configure(bg ="#F1EA9C")#je change le background en jaune beige avec comme code hexa #F1EA9C, on peut changer si ça plait pas mais j'aime bien
    Page_vote.title("Page de vote")#je change le nom de la page, useless parce que la page sera en plein écran mais au cas où
    Page_vote.geometry(str(long)+"x"+str(larg))# je choisi la taille que doit prendre la page en s'ouvrant et je l'accorde pour qu'elle prenne la taille de l'écran en entier
    
    '''
    mon but là c'est d'avoir un carrée de boutton pour que ce soit joli, c'est à dire que je vais
    remplir un carré ligne par ligne de bouton. mais avant je dois alors connaitre le coté
    de ce carré pour qu'il soit le plus opti, pour ça je vais connaitre le carré le plus petit avant le
    nombre de boutton, pour ça je fais int(len(Liste_vote)**0.5)+1 mais ça marche pas si le nombre est 
    déjà un carré, donc je fais une vérif si il est pas carré et je trouve coté
    '''
    
    if int(len(Liste_vote)**0.5)!=len(Liste_vote)**0.5:
        coté=int(len(Liste_vote)**0.5)+1
    else:
        coté=int(len(Liste_vote)**0.5)
    
    
    "création du text au dessus"
    Text1=Label(Page_vote, text="Salss "+str(Nom)+", clique pour voter",font=("",20),bg ="#F1EA9C")#je precise que le label (zone de texte) est sur la page page_vote, le texte c'est sal'ss avec le nom de celui qui vote, veuiller voter, je regle la police de 20 modifiable et type de police par défaut
    Text1.place(x=0, y=0)#je place la zone de texte en haut à gauche de la page, place marche avec des pxl contrairement à grid! ce qui nous facilitera pour que la page s'adapte à la taille de l'écran
    
    '''
    là je vais calculer la largeur et la longueurs de tout les boutton des candidats (validation et blanc compte
    pas), pour long c'est ez, c'est juste longueur page/(nb bouton par coté) le tout en pxl on le rappel.
    pour la largeur je dois vérifier qu'il y a assez de candidat pour remplir la dernière ligne du carré
    pour faire la même chose que longeur (je supprime cependant 40 pour la zone de texte du dessus qui est
    aussi modifiable et 100 pour la largeur des bouton de valdiation et blanc). Si la dernière ligne n'est
    pas remplis alors j'enlève la ligne en soustrayant 1 au coté. Je pense que mathématiquemnt ce système
    n'est pas correcte pour des nombre de candidats élever dans l'ordre des 50 parce qu'il y aura plus d'une
    ligne non rempli mais là on dépasse pas les 20 donc à voir
    '''
    
    long_but=int(long/coté)#longeur d'un bouton
    if coté**2-coté<len(Liste_vote):
        larg_but=int((larg-40-100)/coté)#largeur d'un bouton
    else:
        larg_but=int((larg-40-100)/(coté-1))
    
    '''
    je vais ensuite ranger la liste des candidats dans un tableau qui sera exactement le même que
    celui des bouton (ou peut-être pas, j'inverse souvent ligne et colone comme un teubé') juste
    là je rajoute un système de ligne, c'est à dire qu'à chaque fois que je complète une ligne, 
    i reviens à 0 et ligne augmente de 1. je commence d'un tableau rempli de None pour aussi connaitre
    mes cases vides
    '''
    
    Tableau=[[None for i in range(coté)]for i in range(coté)]
    ligne=0
    for i in range(len(Liste_vote)):
        if i-ligne*coté>=coté:
            ligne+=1
        Tableau[ligne][i-ligne*coté]=Liste_vote[i]

    '''
    l'heure exitante de créer nos boutons est venu ! pour ça j'explore Tableau et je chope les cases
    non remplis et je créer un tableau avec comme text le nom du candidat
    '''
    for i in range(coté):
        for j in range(coté):
            if Tableau[j][i]!=None:#si la case n'est pas vide
                entrée=Button(Page_vote,text=Tableau[j][i],font=("",20),bg ="#F1EA9C")#je créer un boutton qui est en fait un objet, donc si je parcour plusieur fois cette ligne je créer plusieur boutton avec des instances différentes mais avec toujour la même variable entrée, j'attribue à chaque boutton son nom de candidat comme text, inscrit sur la page page_vote, sa couleur jaune et sa police
                entrée['command']=change_color(entrée,nb_vote)# j'ajoute une commande, c'est à dire une fonction à executer si je clique sur le bouton, voir change_color, celuici reprend l'instance du boutton et le nombre de vote, j'aurais pu mettre la commande dans le paramétrage du bouton (ligne au dessus) mais j'ai besoin de slectionner entrée qui est l'instance du boutton individuelle pour pouvoir le modifier lui et aucun autre, sauf qu'il n'étais pas encore déclarer au dessus LUL
                a=long_but*i#je calcule la position y du bouton avec i qui est le numérau de ma colone et le nb de pxl d'un bouton
                if Tableau[j][-1]==None:#pour centrer la dernière ligne qui n'est pas forcement complète, je vais vérifier que la dernière case de la ligne n'existe pas, sinon je passe
                    a+=(coté-(len(Liste_vote)%coté))*long_but/2 # je trouve alors le nombre de pxl de bouton manquant pour avoir une ligne complète avec (coté-(len(Liste_vote)%coté))*long_but que je divise par 2 et que j'additionne à toute la ligne pour avoir un espace à gauche et décaler tout les boutons
                entrée.place(x=a, y=40+j*larg_but,height=str(larg_but),width=str(long_but)) # je place mon bouton selon x que j'ai caluler avant et y qui est largeur_bouton*numéro de ligne, je rajoute aussi avec height et width la largeur et longeur du bouton
                entrées.append(entrée)#j'enregistre mon instance dans la listes des entrées
    
    '''
    je créer mon bouton valider et blanc
    '''
        
    valider=Button(Page_vote,text="valider", command=validation(Liste_vote,nb_vote), bg="green",font=("",20))# comme d'hab, sinon que j'utilise une fonction valider à la fin
    valider.place(x=long/2,y=larg-100,height=str(100),width=str(long/2))# je place le bouton pour qu'il soit en bas à droite de l'écran et prennent la moitier de l'écran en longeuru, largeur de 10 pxl
    
    blanc=Button(Page_vote, command=reset(), text="blanc",font=("",20))
    blanc.place(x=0, y=larg-100,height=str(100),width=str(long/2))# je place le bouton pour qu'il soit en bas à gauche de l'écran et prennent la moitier de l'écran en longeuru, largeur de 10 pxl
    
    entrées.append(blanc) # je rajoute aussi blanc dans les entrées
    
    Page_vote.mainloop()# boucle de tk obligatoir pour une page

'''
je souhaite que quand je selectionne un bouton, celui-ci m'affiche que je le selectionne et que je le garde,'
fonction qui permet en connaissant le boutton que j'ai tapé, de le changer en gris si il etait jaune et inversement
deplus si je clique sur un bouton alors le boutton blanc était gris, alors je dois le remettre blanc. deplus je
ne peux pas mettre plus de boutton gris que le nombre de vote.
'''

def change_color(entrée,nb_vote):
    def do_it():#quand je créer une modif à partir d'une commande, tk vas l'exécuter directement et donc mon boutton sera directement gris au lancement. mais je peux contourner le problème en créant une fonction  dans la fonction et je mets mes modifs dessus
        global nb_select, entrées#toujours en commun les fonction du nombre selectionner et des instances de mes boutons
        if entrée["bg"]=="#F1EA9C" and nb_select<nb_vote: # si mon bouton étais jaune et que j'ai une selection plus petite que le nombre de vote,
            entrée["bg"] ="grey" #alors je peux le colorier en gris
            entrées[-1]["bg"]="white"#je remet le boutton blanc en blanc qqs la couleur d'avant, pour rappelle la dernière instance de entrée est toujours blanc
            nb_select+=1# je rajoute un au nombre selectionner
        elif entrée['bg']=="grey":# si il étais gris
            entrée["bg"] ="#F1EA9C"# je le retransforme een jaune
            nb_select-=1# j'enlève 1 à ma selection
    return do_it

'''
je souhaite que lorsque je clique sur blanc, blanc deviens gris et inversement, deplus je veux que mes
autres bouton soit redevienne jaune pour ne plus être selectionner
'''

def reset():
    def do_it():
        global nb_select, entrées
        if entrées[-1]["bg"]=="white":
            entrées[-1]["bg"] ="grey"
            nb_select=0
            for i in range(len(entrées)-1):# je parcour toutes mes instances de bouton sauf la dernière qui est le bouton blanc
                entrées[i]["bg"]="#F1EA9C"# je le remet en jaune
        else:
            entrées[-1]["bg"] ="white"
    return do_it

'''
je souhaite que lorsque j'appuie sur valider, je récupère une liste de tout les bouton sélectionner
 soit tout les bouton en gris. Le bouton fonctionne uniquement si j'ai suffisament de vote pour voter
 ou si blanc est select'
 j'ai pas encore de lien avec les autres programme alors je sais pas comment il vont le récupérer, pour
 l'instant je stock tout dans une variable global qui est vote'
'''

def validation(Liste_vote,nb_vote):
    def do_it():
        global entrées,nb_select,vote
        vote=[]
        if nb_select==nb_vote or entrées[-1]["bg"]=="grey":#si j'ai suffisament de vote pour voter ou si blanc est select
            for i in entrées:# je parcour tout mes boutons
                if i["bg"]=="grey" :# si y en a un qui est gris, j'ajoute le text du bouton à la liste vote, si j'ai voter blanc alors je n'aurais que blanc en gris et je retrouverais dans ma liste que blanc'
                    vote.append(i["text"])
            Page_vote.destroy()# je supprime la page 
        print(vote)
    return do_it

'''
petit mot pour la fin: sqrt(29μ93) les plus grands crapal's de KIN
aussi compilez sur la bell'eff'situde de la 57μ(16-128) la fam's qui pine le plus et dort le moin!
Bercerf'k 57μ(16-128)
'''