if __name__ == '__main__':
    Months=[
        "Janvier" ,
        "Fevrier",
        "Mars",
        "avril",
        "Mai",
        "Juin",
        "Juillet",
        "Aout",
        "Septembre",
        "Octobre"    
    ]
    print("-----les elements de la liste-----")
    print(Months)
    
    print("-----Change Le contenu de l'element num 5-----")
    Months[5]="Matty"
    print(Months)
    
    print("-----nouvelle liste-----")
    
    Newlist=[]
    for m in Months :
            if 'a' in m:
              Newlist.append(m)  
    print(Newlist)