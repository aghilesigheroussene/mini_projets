from contact import Contact
from contactbook import contactbook


carnet = contactbook()

def menu():
    print("\n 📘Carnet des Contacts ")
    print("1-Ajouter un Contact")
    print("2-Supprimer un Contact")
    print("3-Rchercher un contact")
    print("4-Afficher tous les contacts")
    print("5-Quitter")

while True:
    menu()
    choix=input("Choix: ")

    if choix == "1":
        nom=input("Nom: ")
        tel=input("Tel: ")
        email=input("Email: ")
        contac=Contact(nom,tel,email)
        carnet.ajouter_contact(contac)

    elif choix == "2":
        nom=input("Nom à supprimer: ")
        carnet.supprimer_contact(nom)

    elif choix == "3":
        nom=input("Nom à rechercher: ")
        resultat=carnet.rechercher_contact(nom)
        for c in resultat:
            print(c)

    elif choix == "4":
        carnet.afficher_contact() 

    elif choix == "5":
        print("Merci!😊")
        break 
    else:
        print("Choix invalide!🙂")

