def afficher_menu():
    print("\n---Gestionnaire des tâches---")
    print("1-Afficher toutes les tâches")
    print("2-Ajouter une tâche")
    print("3-Modifier une tâche")
    print("4-Marquer une tache faite")
    print("5-Supprimer une tâche")
    print("6-Quitter")

def afficher_taches(taches):
    if not taches:
        print("aucune tache")
    for i, t in enumerate(taches):
        Statut = "✅" if t.faite else "❌"
        print(f"{i}. {Statut} {t.titre} - {t.description}")

