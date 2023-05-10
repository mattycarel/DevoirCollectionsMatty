if __name__ == '__main__':
    
    
    #### QUESTION I
    Months=[
        "janvier" ,
        "fevrier",
        "mars",
        "avril",
        "mai",
        "juin",
        "juillet",
        "aout",
        "septembre",
        "octobre"    
    ]
    #### I.1 Afficher les elements de la liste
    print("-----Afficher les elements de la liste-----")
    print(Months)
    
    #### I.2 Change Le contenu de l'element num 5
    print("-----Change Le contenu de l'element num 5-----")
    Months[6]="Matty"
    print(Months)
    
    #### I.3 nouvelle liste
    print("-----nouvelle liste-----")
    
    Newlist=[]
    
    #### les elements nouvelle liste
    print("-----les elements nouvelle liste-----")
    for m in Months :
            if 'a' in m:
              Newlist.append(m)  
    print(Newlist)
    
    #### I.4 ajouter un element a la fin de la liste
    print("-----ajouter un element a la fin de la liste-----")
    Newlist.append("end")
    print(Newlist)
    
    #### I.5 ajouter un element a l'index num 2
    print("-----ajouter un element a l'index num 2-----")
    print(Newlist[2])
    
    #### I.6 supprimer l'element num 3
    print("-----supprimer l'element num 3-----")
    Newlist.pop(4)
    print(Newlist)
    
    #### I.7 supprimer l'element a l'index  num 2
    print("-----supprimer l'element a l'index  num 2-----")
    Newlist.pop(2)
    print(Newlist)
    
    #### I.8 Ordonner la liste
    print("-----Ordonner la liste-----")
    Newlist.sort()
    print(Newlist)
    
    #### I.9 afficher la liste inverse 
    print("-----afficher la liste inverse-----")
    Newlist.sort(reverse=True)
    print(Newlist)
    
    #### I.10 vider la liste
    print("-----vider la liste-----")
    Newlist.clear()
    print(Newlist)
    
    #### I.11 supprimer la liste
    print("-----supprimer la liste-----")
    del Newlist
    
    #### QUESTION II
    print("------QUESTION II-----")
    
    Numbers = (1,12,3,15,5,3,7,8,9,10)
    
    #### II.1 Afficher le nombre de fois la valeur 3 apparait dans la tuple
    print("-----Afficher le nombre de fois la valeur 3 apparait dans la tuple----")
    count = Numbers.count(3)
    print(count) 
    
    #### II.2 Afficher le contenu de l'element numero 5
    print("----Afficher le contenu de l'element numero 5-----")
    print(Numbers[5-1])
    
    #### II.3 Ordonner la tuple
    print("----Ordonner la tuple-----")
    s=sorted(Numbers)
    print(s)
    
    #### II.4 Ajouter un element a la fin de la tuple
    print("----Ajouter un element a la fin de la tuple-----")
    l=list(Numbers)
    l.append(100)
    Numbers=tuple(l)
    print(Numbers)
    
    #### II.5 Ajouter un element a l’index numero 3
    print("----Ajouter un element a l’index numero 3-----")
    n=list(Numbers)
    n.insert(3, 500)
    Numbers=tuple(n)
    print(Numbers)
    
    #### II.6 Afficher la nouvelle tuple
    print("----Afficher la nouvelle tuple-----")
    print(Numbers)
    
    #### QUESTION III
    print("-----QUESTION III-----")
    
    Players={
        "Curry",
        "Lebron",
        "Giannis" ,
        "Harden",
        "Kid",
        "Parker",
        "Irivng",
        "Poole",
        "Savoka",
        "Yao"   
    }
    
    #### III.1 Ajouter un element
    print("------Ajouter un element------")
    Players.add("Matty")
    print(Players)
    
    #### III.2 Supprimer un element
    print("------Supprimer un element------")
    Players.remove("Matty")
    print(Players)
    
    #### III.3 supprimer le set
    print("------Supprimer le set------")
    del Players
    
    #### QUESTION IV
    print("----QUESTION IV-----")
    
    Person={
        "Nom" : "Bizindavyi",
        "Prenom" : "Joe Matty Carel",
        "Nationalite" : "Burundaise",
        "Age" : "24",
        "Tel" : "61989328",
        "Profession" : "Etudiant",
        "Taille" : "1,88cm",
        "Email" : "Joemattycarelb@gmail.com",
        "Universite" : "ULT",
        "Faculte" : "Informatique"    
    }
    
    #### IV.1 Afficher le dictionnaire
    print("-------Afficher le dictionnaire----")
    print(Person)
    
    #### IV.2 Afficher seulement les cles
    print("-------Afficher seulement les cles----")
    for i in Person.keys():
        print(i)
    
    #### IV.3 Afficher seulement les valeurs
    print("-------Afficher seulement les valeurs----")
    for j in Person.values():
        print(j)
    
    #### IV.4 Afficher les cles et les valeurs sous le format: Cle: Valeur  
    print("-------Afficher les cles et les valeurs sous le format: Cle: Valeur---")
    for c,v in Person.items():
        print(c ,":",v)
    
    #### IV.5 Supprimer l'element a la cle numero 2
    print("-------Supprimer l'element a la cle numero 2---")
    Person.pop("Prenom")
    print(Person)
    
    #### IV.6 Afficher l'element de cla cle numero 5
    print("-------Afficher l'element de la cle numero 5---")
    num_5 = Person["Tel"]
    print(num_5)
    
    #### IV.7 Ajouter un nouvel element 
    print("-------Ajouter un nouvel element---")
    Person["BasketBall_Team"]="New Star"
    print(Person)
    
    #### IV.7 Creer une copie du dictionnaire
    print("-------Creer une copie du dictionnaire---")
    copy=Person.copy()
    print(copy)
    
    #### Afficher les nouveaux elements
    print("-------Afficher les nouveaux elements---")
    print(Person)
    
    
    
    
    
        
        
          
    
    