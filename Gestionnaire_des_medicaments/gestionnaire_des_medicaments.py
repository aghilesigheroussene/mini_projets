from datetime import datetime
import json
import os

class Medicament:
    def __init__(self, nom, heure, duree):
        self.nom = nom
        self.heure = heure
        self.duree = duree
        self.date_debut = datetime.today().strftime("%Y-%m-%d")
        self.jours_pris = []

    def est_a_prendre_aujourdhui(self):
        aujourd_hui = datetime.today().strftime("%Y-%m-%d")
        return aujourd_hui not in self.jours_pris

    def marquer_comme_pris(self):
        aujourd_hui = datetime.today().strftime("%Y-%m-%d")
        if aujourd_hui not in self.jours_pris:
            self.jours_pris.append(aujourd_hui)

    def to_dict(self):
        return {
            "nom": self.nom,
            "heure": self.heure,
            "duree": self.duree,
            "date_debut": self.date_debut,
            "jours_pris": self.jours_pris
        }

    @staticmethod
    def from_dict(data):
        m = Medicament(data["nom"], data["heure"], data["duree"])
        m.date_debut = data["date_debut"]
        m.jours_pris = data["jours_pris"]
        return m

class GestionnaireMedicaments:
    def __init__(self):
        self.medicaments = []

    def ajouter_un_medicament(self, nom, heure, duree):
        m = Medicament(nom, heure, duree)
        self.medicaments.append(m)

    def afficher_du_jour(self):
        for m in self.medicaments:
            statut = "pris" if not m.est_a_prendre_aujourdhui() else "pas encore pris"
            print(f"{m.nom} à {m.heure} [{statut}]")

    def marquer_pris(self, nom):
        for m in self.medicaments:
            if m.nom.lower() == nom.lower():
                m.marquer_comme_pris()
                print(f"{nom} est marqué comme pris")
                return
        print(f"Médicament '{nom}' non trouvé.")

    def sauvegarder(self, fichier="medicaments.json"):
        data = [m.to_dict() for m in self.medicaments]
        with open(fichier, "w") as f:
            json.dump(data, f, indent=4)

    def charger(self, fichier="medicaments.json"):
        if os.path.exists(fichier):
            with open(fichier, "r") as f:
                data = json.load(f)
                self.medicaments = [Medicament.from_dict(d) for d in data]

def menu():
    gestion = GestionnaireMedicaments()
    gestion.charger()

    while True:
        print("\n--- 💊 Gestion des médicaments 💊 ---")
        print("1️⃣ - Ajouter un médicament")
        print("2️⃣ - Voir médicaments du jour")
        print("3️⃣ - Marquer comme pris")
        print("4️⃣ - Quitter")

        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom du médicament : ")
            heure = input("Heure de prise (ex: 08:00) : ")
            try:
                duree = int(input("Durée du traitement (en jours) : "))
                gestion.ajouter_un_medicament(nom, heure, duree)
                gestion.sauvegarder()
            except ValueError:
                print("Erreur : La durée doit être un nombre entier.")
        elif choix == "2":
            gestion.afficher_du_jour()
        elif choix == "3":
            nom = input("Nom du médicament à marquer comme pris : ")
            gestion.marquer_pris(nom)
            gestion.sauvegarder()
        elif choix == "4":
            print("Prenez soin de vous 😊")
            gestion.sauvegarder()
            break
        else:
            print("Choix invalide ! Veuillez réessayer.")

if __name__ == "__main__":
    menu()
