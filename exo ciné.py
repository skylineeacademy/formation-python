prix_adulte = 700
prix_enfant = 500
prix_pop = 250
rang = 1
enfant = 0
adulte = 0
nombre_pop = 0

print("Combien de personnes êtes-vous ?")
groupe = int(input("-> "))

for i in range(groupe):
    print("Donnez l'âge de la personne numéro " + str(rang) + " :")
    age = int(input("-> "))
    rang += 1
    if age < 18:
        enfant += 1
    else:
        adulte += 1

    print("Voulez-vous du popcorn, oui/non ?")
    pop = input("-> ")
    if pop.lower() == "oui":
        nombre_pop += 1

prix_total = (adulte * prix_adulte) + (enfant * prix_enfant) + (nombre_pop * prix_pop)
print("Vous avez pris :")
print(str(adulte) + " place(s) adulte(s)")
print(str(enfant) + " place(s) enfant(s)")
print(str(nombre_pop) + " paquet(s) de popcorn")
print("Le prix total est de " + str(prix_total) + " dz.")