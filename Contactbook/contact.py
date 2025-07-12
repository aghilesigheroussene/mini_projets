class Contact:
    def __init__(self,nom,tel,email):
        self.nom = nom
        self.tel = tel
        self.email = email

    def to_dict(self):
        return {"nom":self.nom, "tel":self.tel, "email":self.email}
    
    def __str__(self):
        return f"{self.nom} - 📞 {self.tel} - 📧 {self.email}"