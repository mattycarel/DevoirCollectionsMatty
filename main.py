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
        "oc,,,tobre"    
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
    
    
     