# je récupère l'email de l'utilisateur
email = input("Give me your email: ")
# je cherche la position de l'arobase (@)
position_arobase = email.find("@")
# je cherche la position du point, à partir de l'arobase
position_point = email.find(".", position_arobase)
# je range dans une variable intermédiaire un morceau de mon email, qui
# va de l'arobase (+1) jusqu'à mon point
resultat = email[position_arobase + 1:position_point]
# je print
print(resultat)
