import random

roulette = [num for num in range(0, 37)]
budget = 2000

print('####################################################')
print('Bienvenue au jeu de roulette simplifié !')
print(f'Votre budget initial est de {budget} MAD.')
print('Essayez de maximiser vos gains. Bonne chance !')
print('####################################################')

while budget > 0:
    print(f'Votre budget actuel est de {budget} MAD.')

    guess = None
    while guess not in roulette:
        try:
            guess = int(input('Sur quel numéro souhaitez-vous parier (0-36) ? '))
            if guess not in roulette:
                print('Entrée invalide. Veuillez choisir un numéro entre 0 et 36.')
        except ValueError:
            print('Entrée invalide. Veuillez entrer un nombre.')

    mise = 0
    while mise <= 0 or mise > budget:
        try:
            mise = int(input(f'Combien souhaitez-vous miser ? (1-{budget}) '))
            if mise <= 0 or mise > budget:
                print(f'Montant invalide. Veuillez miser un montant compris entre 1 et {budget} MAD.')
        except ValueError:
            print('Entrée invalide. Veuillez entrer un nombre.')

    print('La roue tourne...')
    choice = random.choice(roulette)
    print(f'Et s’arrête sur le numéro {choice} !')

    if choice == guess:
        winnings = mise * 36
        budget += winnings
        print(f'Félicitations ! Vous avez gagné {winnings} MAD.')
    else:
        budget -= mise
        print(f'Dommage ! Vous avez perdu {mise} MAD.')

    if budget > 0:
        continuer = input('Souhaitez-vous continuer à jouer ? (oui/non) ')
        if continuer != 'oui':
            break
    else:
        print('Vous n’avez plus de budget pour continuer.')

print('Merci d’avoir joué !')
print(f'Votre budget final est de {budget} MAD.')
print('À bientôt !')
