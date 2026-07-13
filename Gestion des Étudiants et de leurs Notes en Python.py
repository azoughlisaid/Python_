import numpy as np



# Liste des étudiants
etudiants = []
# Liste des matières (NE SERA PLUS UTILISÉE POUR LES ÉTUDIANTS)
matieres = []

#1+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def ajouter_etudiant():

    nom = input("Nom de l'étudiant : ")
    id = int(input("l'ID de l'étudiant : ")) # Mon idée  c'est de basé sur l'ID(unique) pas le nom
    age = int(input("Age de l'étudiant : "))

    nombre_matieres = int(input("Nombre de matières : "))

    #Ajouter les matière selon le choix

    matieres_etudiant = []

    for i in range(nombre_matieres):

        matiere = input("Nom de la matière : ")
        note = float(input("Note obtenue : "))

        matieres_etudiant.append((matiere, note))  #

    etudiant = {
        "nom": nom,
        "id": id,
        "age": age,
        "matieres": matieres_etudiant
    }

    etudiants.append(etudiant)

    print("Étudiant ajouté avec succès")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Trouver un étudaint avec son nom

def trouver_etudiant(id):
    id = int(id)
    for e in etudiants:
        if e["id"] == id:
            return e
    return None

#Question2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 2. Calculer la moyenne d'un étudiant (avec NumPy)

def calculer_moyenne(etudiant):
    notes = [note for (matiere, note) in etudiant["matieres"]]
    if len(notes) == 0:
        return 0
    moyenne = np.mean(notes)
    return moyenne

def afficher_moy():

    id = input("l'ID de l'étudiant que vous voulez voir sa moyenne : ")

    etudiant = trouver_etudiant(id)

    if etudiant is None:
        print("Erreur : étudiant introuvable.\n")
        return


    m = calculer_moyenne(etudiant)

    print("La moyenne de l'étudiant ' ", etudiant["nom"]," ' avec l'ID : ' ", id , " ' est = ", m ,"/20  avec la mention : ")

    if m >= 16:
        print("Excellent !")
    elif m >= 14:
        print("Bien !")
    elif m >= 12:
        print("Assez Bien !")
    elif m >= 10:
        print("Passable !")
    else:
        print("Insuffisant, vous n'avez pas validé !")


# PARTIE 3 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 3. Ajouter une matière à un étudiant existant

def ajouter_matiere():
    id = input("l'ID de l'étudiant que vous voulez ajouter sa nouvelle matière  : ")

    etudiant = trouver_etudiant(id)

    if etudiant is None:
        print("Erreur : étudiant introuvable.\n")
        return

    matiere = input("Nom de la nouvelle matière : ")
    note = float(input("Note obtenue : "))

    etudiant["matieres"].append((matiere, note))
    print("Matière ajoutée avec succès.\n")


# Question 4 a l'aide ici de CHATGPT++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def afficher_liste_etudiants():
    if len(etudiants) == 0:
        print("Aucun étudiant enregistré.\n")
        return

    print("---- Liste des étudiants ----")
    for etudiant in etudiants:
        moyenne = calculer_moyenne(etudiant)
        print(etudiant["nom"] + " - Moyenne : " + str(round(moyenne, 2)))
    print()

def afficher_etudiants_moyenne_superieure(seuil=12):
    print("---- Étudiants avec une moyenne > " + str(seuil) + " ----")
    for etudiant in etudiants:
        moyenne = calculer_moyenne(etudiant)
        if moyenne > seuil:
            print(etudiant["nom"] + " - Moyenne : " + str(round(moyenne, 2)))
    print()


def get_liste_etudiants_infos():
    if len(etudiants) == 0:
        print("Aucun étudiant enregistré.\n")


    texte = "---- Liste complète des étudiants ----\n"

    for e in etudiants:
        # Construire la liste des matières sur une seule ligne
        matieres_str = ""
        for mat, note in e["matieres"]:
            matieres_str = matieres_str + "(" + mat + " : " + str(note) + ") "

        # Ligne complète pour l'étudiant
        ligne = "Nom : " + e["nom"] + ", ID : " + str(e["id"]) + ", Age : " + str(e["age"]) + ", Matières : " + matieres_str + "\n"
        texte = texte + ligne


    return texte



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def retirer_matiere():
    id = input("L'ID de l'étudiant que vous voulez supprime sa maitère: ")

    etudiant = trouver_etudiant(id)
    if etudiant is None:
        print("Erreur : étudiant introuvable.\n")
        return

    matiere_a_retirer = input("Nom de la matière à retirer : ")

    trouve = False
    for mat, note in etudiant["matieres"]:
        if mat == matiere_a_retirer:
            etudiant["matieres"].remove((mat, note))
            trouve = True
            break

    if trouve:
        print("Matière retirée avec succès.\n")
    else:
        print("Cette matière n'existe pas pour cet étudiant.\n")


# 6 =============== RECHERCHER AVEC LE NOM ================================================================================

def rechercher_etudiant(nom):
    for etudiant in etudiants:
        if etudiant["nom"].lower() == nom.lower():
            return etudiant
    return None
def afficher_infos_etudiant_avec_nom(etudiant):
    print("Nom : " + etudiant["nom"])
    print("Age : " + str(etudiant["age"]))
    print("Matières : ", end="")

    # afficher les matières sur une seule ligne
    matieres_str = ""
    for matiere, note in etudiant["matieres"]:
        matieres_str = matieres_str + "(" + matiere + " : " + str(note) + ") "

    print(matieres_str + "\n")


#==============================================================================================


import numpy as np

def moyenne_par_matiere():
    notes_par_matiere = {}  # {"Math": [15, 12], "Physique": [10, 14]}

    # Collecter les notes par matière

    for etudiant in etudiants:
        for matiere, note in etudiant["matieres"]:
            if matiere not in notes_par_matiere:
                notes_par_matiere[matiere] = []
            notes_par_matiere[matiere].append(note)

    print("---- Moyenne par matière ----")

    # Calculer et afficher les moyennes
    for matiere, notes in notes_par_matiere.items():
        tableau_notes = np.array(notes)
        moyenne = np.mean(tableau_notes)
        print(matiere + " : " + str(round(moyenne, 2)))

    print()


#===============================================================================================


# =========================== MENU ====================================

def menu():
    while True:
        print("\n============================ MENU =====================================")

        print("1. Ajouter un étudiant")
        print("2. Afficher la moyenne d'un étudiant en tapant l'ID ")
        print("3. Ajouter une matière à un étudiant en tapant l'ID")
        print("4. Afficher la moyenne globale des étudiants")
        print("5. Afficher les étudiants avec moyenne > 12")
        print("6. Liste des étudiants avec leurs informations")
        print("7. Retirer une matière d'un étudiant")
        print("8. Afficher les étudiants avec le Nom ")
        print("9. Moyenne par matière ")
        print("0. Quitter")

        print("=====================================================================")

        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_etudiant()

        elif choix == "2":
            afficher_moy()

        elif choix == "3":
            ajouter_matiere()

        elif choix == "4":
            afficher_liste_etudiants()

        elif choix == "5":
            afficher_etudiants_moyenne_superieure()

        elif choix == "6":

            print(get_liste_etudiants_infos())

        elif choix == "7":
           retirer_matiere()

        elif choix == "8":
            nom = input("Nom de l'étudiant à rechercher : ")
            etudiant = rechercher_etudiant(nom)
            if etudiant:
                afficher_infos_etudiant_avec_nom(etudiant)
            else:
                print("Étudiant introuvable\n")


        elif choix =="9":
            moyenne_par_matiere()

        elif choix == "0":
            print("Au revoir ! à la prochaine fois ")
            break

        else:
            print("Choix invalide, veuillez réessayer.")


# Lancement du programme
if __name__ == "__main__":
    menu()
