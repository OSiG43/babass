from tkinter import * 

###
#### Fonction de recherche dans la liste déroulante
###

def recherche(a)  :
    if type(saisie.get())==str : 
        if len(saisie.get())>0 : # Si il y a qque chose de rentré
            listeaffiche.delete(0,len(ListePG)) # On commence par tout effacer
            for i in range (0,len(ListePG)) : # On se ballade dans notre liste de PG
                sommeoccurences=0
                for j in saisie.get().split(" ") : # On sépare la recherche du FT en plusieurs strings
                    if ListePG[i].find(j)!=-1 : # Si il y a une occurence, on incrémente notre compteur
                        sommeoccurences=sommeoccurences+1
                if sommeoccurences >= len(saisie.get().split(" ")) : # On vérifie qu'il y ai autant d'occurences que de mots du FT
                    listeaffiche.insert('end',replace(ListePG[i][:-1]," ")) # On insère les occurences en retirant les ;
        else : # Au cas où le FT revient à une entrée nulle, on refresh la liste
            listeaffiche.delete(0,len(ListePG)) # On supprime les non-occurences
            for item in ListePG :
                listeaffiche.insert('end',item[:-1])

alignx=100 # alignement des wedgets


###
#### Création de la fenêtre
###

root=Tk() 
root.configure(background='#222222') # Fond


###
#### Création du titre
###

label1=Label(root,text = "Choisir le PG votant",bg='#222222',fg='#FFFFFF',font=20) # Juste un titre
label1.place(x=alignx,y=10)

###
#### Création de la liste déroulande des PG
###

listeaffiche = Listbox(root, listvariable=StringVar()) # Liste des PG correspondants
PROMS=open("PROMS.csv", "r")
ListePG=PROMS.readlines() # On importe tout nos PG dans une liste
PROMS.close()

for item in ListePG: # On se déplace dans notre liste pour les ajouter à notre liste déroulante
    listeaffiche.insert('end',item[:-1])
listeaffiche.place(x=alignx,y=100)

###
#### Création de la zone de saisie par le FT
###

saisie = Entry() # Zone d'entrée de la bucque
saisie.place(x=alignx,y=50)
saisie.bind_all('<Key>', recherche) # Quand il y a une touche pressée on lance la fonction recherche

###
#### Boutton d'annulation'
###

bouton = Button(text = "Annuler le dernier vote")
bouton.place(x=alignx,y=300)

root.mainloop()
