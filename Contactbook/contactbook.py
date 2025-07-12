from contact import Contact
import json

class contactbook:
    def __init__(self, filename="contact.json"):
        self.filename = filename
        self.contacts = []
        self.charger_contacts()

    def ajouter_contact(self,contact):
        self.contacts.append(contact)
        self.enregistrer_contact()

    def rechercher_contact(self,nom):
        return [c for c in self.contacts if nom.lower() in c.nom.lower()]
    
    def supprimer_contact(self,nom):
        self.contacts = [c for c in self.contacts if c.nom.lower() != nom.lower()]
        self.enregistrer_contact()

    def afficher_contact(self):
        for contact in self.contacts:
            print(contact)

    def charger_contacts(self):
        try:
            with open ("contact.json", "r") as f:
                contacts_data = json.load(f)
                self.contacts = [Contact(**data) for data in contacts_data]
        except FileNotFoundError:
            self.contacts = []

    def enregistrer_contact(self):
        with open ("contact.json", "w") as f:
            json.dump([contact.to_dict() for contact in self.contacts],f, indent=4)
            


    
    