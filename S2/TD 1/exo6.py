# Ecrire une fonction (ou procédure) qui permet de permuter deux entiers
def permutation(a, b):
    return b, a

# Ecrire une fonction (ou procédure) qui permet de remplir un tableau de taille 100. 
def remplir_tableau(tableau):
    for i in range(100):
        tableau.append(i)

# Ecrire une fonction (ou procédure) qui permet dʼafficher un tableau.
def affiche_tableau(tableau):
    print(tableau)
    
#En utilisant les fonctions (ou procédures) précédentes, écrire un algorithme qui lit les valeurs 
#dʼun tableau de taille 100 etaffiche le tableau trié.

def main():
    nums = []
    remplir_tableau(nums)
    affiche_tableau(nums)
    
main()