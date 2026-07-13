# ========================================================
# STRUCTURE COMPLEXE IMBRIQUEE
# VERSION AVEC MENU
# BLOC 1/3
# ========================================================


donnees_business = {
"2025-01-15": {
"Paris": {
"ventes": [("laptop", 3, 900), ("mouse", 25, 30), ("keyboard", 15, 50)],
"meteo": {"temp": 18, "humidite": 65, "pluie": True},
"vendeurs_actifs": {"Alice", "Bob", "Charlie"}
},
"Lyon": {
"ventes": [("laptop", 2, 900), ("screen", 8, 250), ("webcam", 20, 80)],
"meteo": {"temp": 20, "humidite": 60, "pluie": False},
"vendeurs_actifs": {"Diana", "Eve"}
},
"Marseille": {
"ventes": [("mouse", 40, 30), ("keyboard", 12, 50)],
"meteo": {"temp": 25, "humidite": 45, "pluie": False},
"vendeurs_actifs": {"Frank", "Alice"}
}
},

"2025-01-16": {

"Paris": {
"ventes": [("laptop", 1, 900), ("screen", 12, 250)],
"meteo": {"temp": 22, "humidite": 70, "pluie": False},
"vendeurs_actifs": {"Alice", "Bob"}
},

"Lyon": {
"ventes": [("webcam", 15, 80), ("mouse", 30, 30)],
"meteo": {"temp": 24, "humidite": 65, "pluie": True},
"vendeurs_actifs": {"Diana", "Eve", "Charlie"}
},

"Marseille": {
"ventes": [("laptop", 4, 900), ("keyboard", 8, 50)],
"meteo": {"temp": 28, "humidite": 40, "pluie": False},
"vendeurs_actifs": {"Frank"}
}
}
}



produits_ref = {

"laptop": {
"prix_achat":650,
"categorie":"High-Tech",
"marge_cible":0.3
},

"mouse": {
"prix_achat":18,
"categorie":"Accessoire",
"marge_cible":0.4
},

"keyboard": {
"prix_achat":30,
"categorie":"Accessoire",
"marge_cible":0.4
},

"screen": {
"prix_achat":180,
"categorie":"High-Tech",
"marge_cible":0.25
},

"webcam": {
"prix_achat":55,
"categorie":"Accessoire",
"marge_cible":0.35
}

}



# ========================================================
# 1 - EXTRAIRE TOUTES LES VENTES
# ========================================================

def extraire_toutes_les_ventes():

    toutes_les_ventes = []


    for date, villes in donnees_business.items():

        for ville, informations in villes.items():

            for produit, quantite, prix in informations["ventes"]:


                vente = {

                    "date": date,
                    "ville": ville,
                    "produit": produit,
                    "quantite": quantite,
                    "prix": prix

                }


                toutes_les_ventes.append(vente)



    print("\nToutes les ventes :")


    for vente in toutes_les_ventes:

        print(vente)



# ========================================================
# 2 - PRODUITS PAR VILLE
# ========================================================


def produits_par_ville():


    produits_villes = {}



    for date, villes in donnees_business.items():


        for ville, informations in villes.items():


            if ville not in produits_villes:

                produits_villes[ville] = []



            for vente in informations["ventes"]:


                produits_villes[ville].append(vente[0])




    print("\nProduits vendus par ville :")


    for ville, produits in produits_villes.items():

        print("##", ville)

        print(produits)




# ========================================================
# 3 - MATRICE CHIFFRE AFFAIRES
# ========================================================


def matrice_chiffre_affaires():


    matrice_ca = {}



    for date, villes in donnees_business.items():


        matrice_ca[date] = {}



        for ville, informations in villes.items():


            ca = 0



            for produit, quantite, prix in informations["ventes"]:


                ca += quantite * prix



            matrice_ca[date][ville] = ca





    print("\nMatrice chiffre d'affaires :")



    for date, villes in matrice_ca.items():


        print(date)



        for ville, ca in villes.items():

            print("\t", ville, ":", ca, "€")





# ========================================================
# 4 - PERFORMANCE QUOTIDIENNE PAR VILLE
# ========================================================


def performance_quotidienne():


    performances = {}



    for date, villes in donnees_business.items():


        performances[date] = []



        for ville, informations in villes.items():


            ca = 0



            for produit, quantite, prix in informations["ventes"]:

                ca += quantite * prix



            performances[date].append((ville, ca))



        performances[date].sort(
            key=lambda x:x[1],
            reverse=True
        )



    print("\nPerformance quotidienne :")



    for date, liste in performances.items():

        print("\nDate :", date)


        for ville, ca in liste:

            print(ville,"===>",ca,"€")





# ========================================================
# 5 - RANKING PRODUITS
# ========================================================


def ranking_produits():


    ranking = {}



    for date, villes in donnees_business.items():


        for ville, informations in villes.items():


            for produit, quantite, prix in informations["ventes"]:



                if produit not in ranking:

                    ranking[produit] = quantite


                else:

                    ranking[produit] += quantite




    classement = sorted(

        ranking.items(),

        key=lambda x:x[1],

        reverse=True

    )




    print("\nRanking produits :")



    for rang, (produit, quantite) in enumerate(classement,start=1):

        print(
            rang,
            "==>",
            produit,
            ":",
            quantite,
            "unités"

        )





# ========================================================
# BLOC 2/3
# ANALYSES + SETS
# ========================================================



# ========================================================
# 6 - IMPACT DE LA PLUIE SUR LES VENTES
# ========================================================


def impact_pluie():


    impact = {}



    for date, villes in donnees_business.items():


        impact[date] = []



        for ville, informations in villes.items():



            if informations["meteo"]["pluie"] == True:



                ca = 0



                for produit, quantite, prix in informations["ventes"]:


                    ca += quantite * prix




                impact[date].append((ville, ca))




    print("\nVilles où il pleut et impact sur les ventes :")



    for date, villes in impact.items():


        print("\nDate :", date)



        if len(villes) == 0:


            print("Aucune ville sous la pluie.")



        else:


            for ville, ca in villes:


                print(
                    ville,
                    "===> Chiffre d'affaires :",
                    ca,
                    "€"
                )





# ========================================================
# 7 - TEMPERATURE MOYENNE VS CA
# ========================================================


def temperature_vs_ca():


    statistiques = {}



    for date, villes in donnees_business.items():


        for ville, informations in villes.items():



            temperature = informations["meteo"]["temp"]



            ca = 0



            for produit, quantite, prix in informations["ventes"]:


                ca += quantite * prix





            if ville not in statistiques:



                statistiques[ville] = {


                    "total_temperature": temperature,

                    "total_ca": ca,

                    "nombre_jours": 1

                }



            else:



                statistiques[ville]["total_temperature"] += temperature

                statistiques[ville]["total_ca"] += ca

                statistiques[ville]["nombre_jours"] += 1





    print("\nTempérature moyenne et CA moyen :")



    for ville, info in statistiques.items():


        moyenne_temp = (
            info["total_temperature"]
            /
            info["nombre_jours"]
        )


        moyenne_ca = (
            info["total_ca"]
            /
            info["nombre_jours"]
        )



        print("\n", ville)

        print(
            "Température moyenne :",
            round(moyenne_temp,2),
            "°C"
        )


        print(
            "CA moyen :",
            round(moyenne_ca,2),
            "€"
        )





# ========================================================
# 8 - MEILLEUR RATIO CA / VENDEURS
# ========================================================


def ratio_ca_vendeurs():


    ratios = []



    for date, villes in donnees_business.items():


        for ville, informations in villes.items():



            ca = 0



            for produit, quantite, prix in informations["ventes"]:


                ca += quantite * prix




            nombre_vendeurs = len(
                informations["vendeurs_actifs"]
            )



            ratio = ca / nombre_vendeurs



            ratios.append(
                (date, ville, ratio)
            )




    ratios.sort(
        key=lambda x:x[2],
        reverse=True
    )




    print("\nClassement ratio CA / vendeurs :")



    for date, ville, ratio in ratios:


        print(
            date,
            "-",
            ville,
            "===>",
            round(ratio,2),
            "€ par vendeur"
        )





# ========================================================
# 9 - VENDEURS PRESENTS DANS PLUSIEURS VILLES
# ========================================================


def intersection_vendeurs():



    print("\nVendeurs communs entre villes :")



    for date, villes in donnees_business.items():


        print("\nDate :", date)



        liste_villes = list(villes.keys())



        for i in range(len(liste_villes)):



            for j in range(i+1,len(liste_villes)):



                ville1 = liste_villes[i]

                ville2 = liste_villes[j]



                communs = (
                    villes[ville1]["vendeurs_actifs"]
                    &
                    villes[ville2]["vendeurs_actifs"]
                )



                if len(communs)>0:


                    print(
                        ville1,
                        "-",
                        ville2,
                        ":",
                        communs
                    )





# ========================================================
# 10 - PRODUITS VENDUS DANS TOUTES LES VILLES
# ========================================================


def produits_toutes_villes():


    print("\nProduits communs dans toutes les villes :")



    for date, villes in donnees_business.items():



        produits_par_ville = []



        for ville, informations in villes.items():



            produits = set()



            for produit, quantite, prix in informations["ventes"]:


                produits.add(produit)



            produits_par_ville.append(produits)





        resultat = produits_par_ville[0]



        for produits in produits_par_ville[1:]:


            resultat = resultat & produits




        print(
            "\nDate :",
            date
        )


        print(
            resultat
        )





# ========================================================
# 11 - MIGRATION DES VENDEURS
# ========================================================


def migration_vendeurs():



    print("\nMigration des vendeurs :")



    for date, villes in donnees_business.items():


        print("\nDate :", date)



        liste_villes = list(villes.keys())



        for i in range(len(liste_villes)):



            for j in range(i+1,len(liste_villes)):



                ville1 = liste_villes[i]

                ville2 = liste_villes[j]



                vendeurs1 = villes[ville1]["vendeurs_actifs"]

                vendeurs2 = villes[ville2]["vendeurs_actifs"]




                print(
                    ville1,
                    "->",
                    ville2,
                    ":",
                    vendeurs1 - vendeurs2
                )


                print(
                    ville2,
                    "->",
                    ville1,
                    ":",
                    vendeurs2 - vendeurs1
                )







# ========================================================
# BLOC 3/3
# MENU PRINCIPAL
# ========================================================


def menu():

    while True:

        print("\n==========================================")
        print("        ANALYSE BUSINESS PYTHON")
        print("==========================================")

        print("1  - Extraire toutes les ventes")
        print("2  - Produits vendus par ville")
        print("3  - Matrice chiffre d'affaires")
        print("4  - Performance quotidienne par ville")
        print("5  - Ranking des produits vendus")
        print("6  - Impact de la pluie sur les ventes")
        print("7  - Température moyenne vs CA")
        print("8  - Ratio CA / vendeurs")
        print("9  - Vendeurs présents dans plusieurs villes")
        print("10 - Produits vendus dans toutes les villes")
        print("11 - Migration des vendeurs entre villes")
        print("0  - Quitter")


        choix = input("\nVotre choix : ")



        if choix == "1":

            extraire_toutes_les_ventes()



        elif choix == "2":

            produits_par_ville()



        elif choix == "3":

            matrice_chiffre_affaires()



        elif choix == "4":

            performance_quotidienne()



        elif choix == "5":

            ranking_produits()



        elif choix == "6":

            impact_pluie()



        elif choix == "7":

            temperature_vs_ca()



        elif choix == "8":

            ratio_ca_vendeurs()



        elif choix == "9":

            intersection_vendeurs()



        elif choix == "10":

            produits_toutes_villes()



        elif choix == "11":

            migration_vendeurs()



        elif choix == "0":

            print("\nFin du programme.")

            break



        else:

            print("\nChoix invalide !")





# ========================================================
# LANCEMENT PROGRAMME
# ========================================================


menu()