# Définir le mot de passe correct
mot_de_passe_correct = "1234"

# Initialiser une variable pour stocker l'entrée de l'utilisateur
mot_de_passe = ""

# Boucle tant que le mot de passe est incorrect
while mot_de_passe != mot_de_passe_correct:
    mot_de_passe = input("Entrez le mot de passe : ")
    if mot_de_passe != mot_de_passe_correct:
        print("Mot de passe incorrect. Essayez encore.")
        
print("Accès autorisé !")
nom = ["karim", "farida", "salma"]
print(nom[0])

nom.append("chaimae")
print(nom)

v = input("entrer un nom a ajouter")
nom.append(v)
print(nom)

vs = input("entrer la valeur a supprimer")

if vs in nom:
    nom.remove(vs)
else:
    print(f"{vs} n'est pas dans la liste.")

print(nom)

