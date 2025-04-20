def summarize(*args, **kwargs):
    if len(args) < 1: 
        return 'absence d\'arguments'
    
    somme = sum(args)
    average = somme / len(args)
    
    # get the options from the kwargs
    precision = kwargs.get('precision')
    verbose = kwargs.get('verbose')
    
    somme = round(somme, precision)
    average = round(average, precision)
    
    if verbose: # return detailed report
        print(f'Valeurs: {args}')
        print(f'Somme: {somme}')
        print(f'Moyenne: {average}')
    else:
        return somme, average
    
print(summarize(1,2,3, precision=3, verbose = False))

print(summarize(5,10,15, verbose=True))

print(summarize())


# Question : comment gérer l’absence d’arguments pour éviter une division par zéro lors du calcul de la moyenne ?
# if len(args) < 1: