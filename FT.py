from tkinter import *
 
arretrecherche=False #Variable de retour de recherche (soit une bucque soit True si on veut afficher les résultats)
alignx=100 # alignement des wedgets
bucque='' # variable de retour de l'entrée texte (fenetreinitiale)

def recherche(a):
    ###
    #### Fonction de recherche dans la liste déroulante
    ###

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
    ###
    #### Création du titre
    ###

    label1=Label(root,text = "Choisir le PG votant",bg='#222222',fg='#FFFFFF',font=20) # Juste un titre
    label1.place(x=alignx,y=10)

    ###
    #### Création de la liste déroulande des PG
    ###
    
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

    ###
    #### Création de la zone de saisie par le FT
    ###
    

    
    saisie = Entry(root) # Zone d'entrée de la bucque
    saisie.place(x=alignx,y=50)
    saisie.bind_all('<Key>', rechercheoccurence) # Quand il y a une touche pressée on lance la fonction recherche


    ###
    #### Boutton d'annulation
    ###
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
