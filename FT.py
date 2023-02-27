from tkinter import * 

###
#### Fonction de recherche dans la liste déroulante
###

def recherche(j)  :
    if type(saisie.get())==str : 
        if len(saisie.get())>0 : # Si il y a qque chose de rentré
            lb.delete(0,len(ListePG)) # On commence par tout effacer
            for i in range (0,len(ListePG)) :
                if occurencePG(ListePG[i],saisie.get())>0 : # Et on ajoute toutes les occurences
                    lb.insert('end',ListePG[i][:-1])
        else : # Au cas où le FT revient à une entrée nulle, on refresh la liste
            lb.delete(0,len(ListePG))
            for item in ListePG :
                lb.insert('end',item[:-1])
    pass

def occurencePG(chaine,mot) : # Fonction d'occurence utile pour la recherche
    apparitions=0
    for i in range (0,len(chaine)-len(mot)+1) :
        j=0
        while (j<len(mot)) and (chaine[i+j]==mot[j]) :
            j=j+1
            if (j==len(mot)) :
                apparitions=apparitions+1
    return apparitions

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

lb = Listbox(root, listvariable=StringVar()) # Liste des PG correspondants
PROMS=open("PROMS.csv", "r")
ListePG=PROMS.readlines() # On importe tout nos PG dans une liste
PROMS.close()

for item in ListePG: # On se déplace dans notre liste pour les ajouter à notre liste déroulante
    lb.insert('end',item[:-1])
lb.place(x=alignx,y=100)

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
