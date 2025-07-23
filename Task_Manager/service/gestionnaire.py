import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from model.tache import Tache
import json

class GestionnairedeTaches:
    def __init__(self,fichier):
        self.fichier=fichier
        self.taches=self.charger()

    def ajouter(self, tache):
        self.taches.append(tache)
        self.sauvegarder()

    def modifier_tache(self, index, nvtache):
        if 0 <= index < len(self.taches):
            self.taches[index] = nvtache
            self.sauvegarder()

    def supprimer_tache(self,index):
        if 0 <= index < len(self.taches):
            del self.taches[index]
            self.sauvegarder()
    def marquer_faite(self, index):
        if 0 <= index < len(self.taches):
            self.taches[index].faite = True
            self.sauvegarder()

    def charger(self):
        try:
            with open(self.fichier, "r") as f:
                data = json.load(f)
                return [Tache.from_dict(d) for d in data]
        except FileNotFoundError:
            return []
        
    def sauvegarder(self):
        with open(self.fichier, "w") as f:
            json.dump([t.to_dict() for t in self.taches], f, indent=2)