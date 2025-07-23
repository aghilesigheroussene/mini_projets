class Tache:
    def __init__(self,titre,description="",faite=False):
        self.titre=titre
        self.description=description
        self.faite=faite

    def to_dict(self):
        return {
            "titre":self.titre,
            "description":self.description,
            "faite":self.faite
         }
        
    @staticmethod
    def from_dict(data):
        return Tache(data["titre"], data.get("description",""), data.get("faite",False))
    