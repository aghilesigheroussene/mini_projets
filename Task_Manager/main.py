from model.tache import Tache
from service.gestionnaire import GestionnairedeTaches
from view.console import *


gestionnaire = GestionnairedeTaches("data/taches.json")

while True:
    afficher_menu()
    try:
        choix=int(input("Entrer votre choix: "))
    except ValueError:
        print("❌Valeur invalide.Veulliez rééssayer")
        continue
    
    if choix == 1:
        afficher_taches(gestionnaire.taches)

    elif choix == 2:
        titre = input("Titre: ")
        desc = input("Description: ")
        gestionnaire.ajouter(Tache(titre, desc))
        print("✅Tâche ajoutée")

    elif choix == 3:
        afficher_taches(gestionnaire.taches)
        try:
            i = int(input("Index de la tache à modifier: "))
            titre = input("Nouveau Titre: ")
            description = input("Nouvelle description: ")
            faite = input("Faite (y/n): ") == "y"
            gestionnaire.modifier_tache(i,Tache(titre, description, faite))
            print("✅Tâche modifiée")
        except (ValueError, IndexError):
            print("❌Index invalide ou erreur d'entrée")
    
    elif choix == 4:
        afficher_taches(gestionnaire.taches)
        try:
            i=int(input("Entrer l'index de la tache faite: "))
            gestionnaire.marquer_faite(i)
            print("✅Tâche marqué comme faite")
        except (ValueError, IndexError):
            print("❌Index invalide ou erreur d'entrée")

    elif choix == 5:
        afficher_taches(gestionnaire.taches)
        try:
            i = int(input("Index de la tache à supprimer: "))
            gestionnaire.supprimer_tache(i)
            print("✅Tâche supprimée")
        except (ValueError, IndexError):
            print("❌Index invalide ou erreur d'entrée")

    elif choix == 6:
        print("Au revoir ! 👋")
        break
    else:
        print("❌Choix invalide. Veuillez rééssayer!")

