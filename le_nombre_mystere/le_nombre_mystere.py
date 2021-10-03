from random import randint

nombre_a_trouver = randint(0, 100)
essais_restants = 10

print("*** Le jeu du nombre mystère ***")

# Je déclare la boucle principale
while essais_restants > 0:
    print(f"Il te reste {essais_restants} essai{'s' if essais_restants > 1 else ''}")

    # Saisie de l'utilisateur
    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    user_choice = int(user_choice)

    if nombre_a_trouver > user_choice:  # Plus grand
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif nombre_a_trouver < user_choice:  # Plus petit
        print(f"Le nombre mystère est plus petit que {user_choice}")
    else:  # Égal (succès)
        break

    essais_restants -= 1

# Gagné ou perdu
if essais_restants == 0:
    print(f"Dommage ! Le nombre mystère était {nombre_a_trouver}")
else:
    print(f"Bravo ! Le nombre mystère était bien {nombre_a_trouver} !")
    print(f"Tu as trouvé le nombre en {10 - essais_restants} essai")

print("Fin du jeu.")
