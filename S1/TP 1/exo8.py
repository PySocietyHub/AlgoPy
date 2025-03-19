""" Ecrire un script Python qui demande à l’utilisateur de saisir le nom d’un fichier et de lui renvoyer son
extension. Exemple si l’utilisateur saisie coursPython.pdf le programme lui renvoie le message « L’extension
du fichier est .pdf ». """

fichier = input('entrez le nom du fichier: ')

for i in range(len(fichier)):
    if fichier[i] == '.':
        print(f"l'extension de votre fichier est : {fichier[i:]}")
        