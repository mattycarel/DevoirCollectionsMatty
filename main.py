if __name__ == '__main__':
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
    print("-----les elements de la liste-----")
    print(Months)
    
    print("-----Change Le contenu de l'element num 5-----")
    Months[6]="Matty"
    print(Months)
    
    print("-----nouvelle liste-----")
    
    Newlist=[]
    
    print("-----les elements nouvelle liste-----")
    for m in Months :
            if 'a' in m:
              Newlist.append(m)  
    print(Newlist)
    
    print("-----ajouter un element a la fin de la liste -----")
    Newlist.append("end")
    print(Newlist)
    
    print("-----ajouter un element a l'index num 2-----")
    print(Newlist[2])
    
    print("-----supprimer l'element num 3-----")
    Newlist.pop(4)
    print(Newlist)
    
    print("-----supprimer l'element a l'index  num 3-----")
    Newlist.pop(3)
    print(Newlist)
    
    print("-----Ordonner la liste-----")
    Newlist.sort()
    print(Newlist)
    
    print("-----afficher la liste inverse-----")
    Newlist.sort(reverse=True)
    print(Newlist)
    
    print("-----vider la liste-----")
    Newlist.clear()
    print(Newlist)
    
    print("-----supprimer la liste-----")
    del Newlist
    
    
    print("------QUESTION II-----")
    
    Numbers = (1,12,3,15,5,3,7,8,9,10)
    
    print("-----Afficher le nombre de fois la valeur 3 apparait dans la tuple----")
    count = Numbers.count(3)
    print(count) 
    
    print("----Afficher le contenu de l'element numero 5-----")
    print(Numbers[5-1])
    
    print("----Ordonner la tuple-----")
    s=sorted(Numbers)
    print(s)
    
    print("----Ajouter un element a la fin de la tuple-----")
    l=list(Numbers)
    l.append(100)
    Numbers=tuple(l)
    print(Numbers)
    
    print("----Ajouter un element a l’index numero 3-----")
    n=list(Numbers)
    n.insert(3, 500)
    Numbers=tuple(n)
    print(Numbers)
    
    print("----Afficher la nouvelle tuple-----")
   
    print(Numbers)
    
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
    
    print("------Ajouter un element------")
    Players.add("Matty")
    print(Players)
    
    print("------Supprimer un element------")
    Players.remove("Matty")
    print(Players)
    
    print("------Supprimer le set------")
    del Players
    
    
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
    
    print("-------Afficher le dictionnaire----")
    print(Person)
    
    print("-------Afficher seulement les cles----")
    for i in Person.keys():
        print(i)
    
    print("-------Afficher seulement les valeurs----")
    for j in Person.values():
        print(j)
        
    print("-------Afficher les cles et les valeurs sous le format: Cle: Valeur---")
    for c,v in Person.items():
        print(c ,":",v)
    
    print("-------Supprimer l'element a la cle numero 2---")
    Person.pop("Prenom")
    print(Person)
    
    print("-------Afficher l'element de la cle numero 5---")
    num_5 = Person["Tel"]
    print(num_5)
    
    print("-------Ajouter un nouvel element---")
    Person["BasketBall_Team"]="New Star"
    print(Person)
    
    
    
    
        
        
          
    
    