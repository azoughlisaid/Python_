# ========================================================
# DONNEES
# ========================================================

ventes_liste = [
["ordinateur", 2, 800, "Alice", "2025-01-15"],
["souris", 15, 25, "Bob", "2025-01-15"],
["clavier", 8, 45, "Alice", "2025-01-15"],
["écran", 3, 300, "Charlie", "2025-01-15"],
["webcam", 12, 80, "Bob", "2025-01-15"],
["ordinateur", 1, 800, "Alice", "2025-01-16"],
["souris", 20, 25, "Charlie", "2025-01-16"]
]


vendeurs_info = [
("Alice", "Senior", 0.05),
("Bob", "Junior", 0.03),
("Charlie", "Senior", 0.05)
]


catalogue_produits = {
"ordinateur": {"categorie": "Informatique", "stock": 50, "seuil_alerte": 10},
"souris": {"categorie": "Périphérique", "stock": 200, "seuil_alerte": 50},
"clavier": {"categorie": "Périphérique", "stock": 100, "seuil_alerte": 30},
"écran": {"categorie": "Informatique", "stock": 25, "seuil_alerte": 5},
"webcam": {"categorie": "Périphérique", "stock": 80, "seuil_alerte": 20}
}



# ========================================================
# TRANSFORMATION DES DONNEES
# ========================================================

ventes_dict = []

for vente in ventes_liste:

    element = {
        "produit": vente[0],
        "quantité": vente[1],
        "prix_unitaire": vente[2],
        "vendeur": vente[3],
        "date_vente": vente[4]
    }

    ventes_dict.append(element)



# ========================================================
# 1 - CA PAR PRODUIT
# ========================================================

def chiffre_affaires_produit():

    produit_ca = {}

    for vente in ventes_dict:

        produit = vente["produit"]

        ca = vente["quantité"] * vente["prix_unitaire"]

        if produit not in produit_ca:
            produit_ca[produit] = ca
        else:
            produit_ca[produit] += ca


    print("\nCA par produit")

    for produit, ca in produit_ca.items():
        print(produit, "===>", ca, "€")



# ========================================================
# 2 - VENTES PAR VENDEUR
# ========================================================

def ventes_vendeurs():

    ventes = {}

    for vente in ventes_dict:

        vendeur = vente["vendeur"]

        qte = vente["quantité"]

        valeur = vente["quantité"] * vente["prix_unitaire"]


        if vendeur not in ventes:

            ventes[vendeur] = {
                "quantité": qte,
                "valeur": valeur
            }

        else:

            ventes[vendeur]["quantité"] += qte
            ventes[vendeur]["valeur"] += valeur


    for vendeur, info in ventes.items():

        print("\n", vendeur)

        print("Quantité :", info["quantité"])

        print("Valeur :", info["valeur"], "€")



# ========================================================
# 3 - PRODUITS PAR JOUR
# ========================================================

def produits_jour():

    produits = {}

    for vente in ventes_dict:

        date = vente["date_vente"]

        if date not in produits:
            produits[date] = set()


        produits[date].add(vente["produit"])


    for date, liste in produits.items():

        print(date, ":", liste)



# ========================================================
# 4 - PRODUITS ALICE ET BOB
# ========================================================

def intersection_vendeurs():

    alice = set()
    bob = set()


    for vente in ventes_dict:

        if vente["vendeur"] == "Alice":
            alice.add(vente["produit"])


        if vente["vendeur"] == "Bob":
            bob.add(vente["produit"])



    print("Alice :", alice)

    print("Bob :", bob)


    print("Commun :", alice & bob)



# ========================================================
# 5 - STOCK
# ========================================================

def alerte_stock():

    stocks_restants = {}


    for produit, info in catalogue_produits.items():

        vendu = 0


        for vente in ventes_dict:

            if vente["produit"] == produit:

                vendu += vente["quantité"]



        stocks_restants[produit] = info["stock"] - vendu



    print("\nStocks restants :")


    for produit, stock in stocks_restants.items():

        print(produit, "==>", stock)



    alertes = [

        produit

        for produit, stock in stocks_restants.items()

        if stock < catalogue_produits[produit]["seuil_alerte"]

    ]


    print("\nProduits en alerte :")

    for produit in alertes:

        print("##", produit)



# ========================================================
# MENU PRINCIPAL
# ========================================================


while True:

    print("\n================ MENU ================")

    print("1 - Chiffre d'affaires par produit")

    print("2 - Ventes par vendeur")

    print("3 - Produits vendus chaque jour")

    print("4 - Produits vendus par Alice et Bob")

    print("5 - Alertes stock")

    print("0 - Quitter")


    choix = input("\nVotre choix : ")



    if choix == "1":

        chiffre_affaires_produit()


    elif choix == "2":

        ventes_vendeurs()


    elif choix == "3":

        produits_jour()


    elif choix == "4":

        intersection_vendeurs()


    elif choix == "5":

        alerte_stock()


    elif choix == "0":

        print("Fin du programme")

        break


    else:

        print("Choix incorrect !")