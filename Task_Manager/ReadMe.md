# Gestionnaire de Tâches en Console

Un mini projet Python permettant de gérer une liste de tâches depuis le terminal. Il suit une architecture **MVC** claire et utilise un fichier `.json` pour sauvegarder les données.

---

## Structure du projet

task_manager/
├── main.py # Fichier principal pour lancer l'application
├── models/
│ └── tache.py # Définition de la classe Tache
├── services/
│ └── gestionnaire.py # Gestionnaire de logique (ajout, suppression, etc.)
├── views/
│ └── console.py # Interface console (affichage des menus)
├── data/
│ └── taches.json # Fichier de sauvegarde des tâches



##  Fonctionnalités

- ➕ Ajouter une tâche
- 📝 Modifier une tâche
- ✅ Marquer une tâche comme faite
- ❌ Supprimer une tâche
- 📄 Sauvegarde dans `data/taches.json`
- 🔁 Menu interactif en boucle

---
## Exemple de Menu

---Gestionnaire des tâches---
1-Afficher toutes les tâches
2-Ajouter une tâche
3-Modifier une tâche
4-Marquer une tâche comme faite
5-Supprimer une tâche
6-Quitter

## Technologies utilisées

-Python 3.x
-Programmation Orientée Objet (POO)
-JSON (stockage)
-Architecture MVC (Modèle - Vue - Contrôleur)
-Gestion des erreurs avec try/except

## Auteur
Développé par moi-même pour l'apprentissage de la POO en Python.

## Lancer l'application

```bash
python main.py
```
