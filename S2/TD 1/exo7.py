def cout_kilometrique(total_kilometres):
    if total_kilometres <= 100:
        return total_kilometres
    elif total_kilometres <= 1000:
        return 100 + ((total_kilometres -100) * 2) # we first remove the first 100 km billed diffrently
    else:
        return 100 + (900 * 2) + ((total_kilometres - 1000) * 5) # we remove the first 100km and the second 1000km

def cout_forfait_journalier(nbr_jours):
    return nbr_jours * 250


def main():
    nbr_jours = int(input('entrez le nombre de jours de location: '))
    total_kilometres = int(input('entrez le nombre total de kilomètres parcourus: '))
    
    cout_km = cout_kilometrique(total_kilometres)
    cout_forfait = cout_forfait_journalier(nbr_jours)
    
    print(f"Coût selon la tarification au kilomètre: {cout_km} MAD")
    print(f"Coût selon le forfait journalier: {cout_forfait} MAD")
    
    if cout_km < cout_forfait:
        print(f"La meilleure option est la tarification au kilomètre ({cout_km} MAD).")
    else:
        print(f"La meilleure option est le forfait journalier ({cout_forfait} MAD).")

    
main()