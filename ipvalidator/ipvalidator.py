# Je déclare ma fonction ip_validator
def ip_validator(ip):
    # je split l'ip sur les point pour récupérer les nombres qui la compose
    # dans une liste contenue dans une variable
    ma_var = ip.split(".")
    # je vérifie la taille de la liste
    if not len(ma_var) == 4:
        return False
        # je parcours les elements de la liste
    for elem in ma_var:
        # je verifie si ce sont bien des nombres
        if not elem.isdigit():
            return False
        # si verifie si ils sont entre 0 et 255
        if int(elem) > 255 or int(elem) < 0:
            return False
    return True


print(ip_validator("195.6.78.79"))
