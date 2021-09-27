# je declare la fonction rectangle plein avec deux
# paramètres : hauteur et largeur
def full_rectangle(height, width):
    if height > 0 and width > 0:
        for i in range(height):
            for j in range(width):
                print("*", end="")
            print()


# je declare la fonction rectangle vide avec deux
# paramètres : hauteur et largeur
def empty_rectangle(height, width):
    if height > 0 and width > 0:
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0 or i == height-1 or j == width-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


# je declare la fonction diagonal
def diagonal(height, width):
    # les diagonales sont possibles quesur les formes carrées
    # donc hauteur = largeur
    if height == width:
        for i in range(height):
            for j in range(width):
                if i == j:
                    print("*", end="")
                elif i == height-1-j:
                    print("*", end="")
                elif i == 0 or j == 0 or i == height-1 or j == width-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


# je declare ma fonction concentric
def concentric(height, width):
    # j'applique la condition de l'exercice
    if height == width and (height-3) % 4 == 0:
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0 or i == height-1 or j == width-1:
                    print("*", end="")
                elif i % 2 == 0 and i <= j and i <= height-1-j:
                    print("*", end="")
                elif i % 2 == 0 and i >= j and i >= height-1-j:
                    print("*", end="")
                elif j % 2 == 0 and j <= i and j <= height-1-i:
                    print("*", end="")
                elif j % 2 == 0 and j >= i and j >= height-1-i:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


# je declare la fonction final pattern avec le paramètre words en plus
# qui permet d'appeler les fonctions déclarées en amont.
def final_pattern(words, height, width):
    if height > 0 and width > 0:
        for elem in words:
            if elem == "full":
                full_rectangle(height, width)
            elif elem == "empty":
                empty_rectangle(height, width)
            elif elem == "diagonal":
                diagonal(height, width)
            elif elem == "concentric":
                concentric(height, width)


final_pattern(["full", "concentric"], 23, 23)