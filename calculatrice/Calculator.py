# On commence par déclarer deux variables a et b
a = b = ""
# Ensuite, on enclenche une boucle tant que a et b ne sont pas des nombres
while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre: ")
    b = input("Entrez un deuxième nombre: ")
    # Si les nombres ne sont pas valides, on affiche une phrase pour reclamer
    # des nombres valides
    if not (a.isdigit() and b.isdigit()):
        print(" Veuillez entrez des nombres valides")
# Pour finir, On affiche le résultat de l'addition
print(f"le résulat de l'addiion de {a} et {b} est égal à {int(a) + int(b)}")
