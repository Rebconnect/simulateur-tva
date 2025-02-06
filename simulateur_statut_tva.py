def simulateur_tva():
    print("Bienvenue dans le simulateur de TVA pour micro-entrepreneur.")
    
    # Collecte des informations de l'utilisateur
    chiffre_affaires = float(input("Quel est votre chiffre d'affaires annuel (hors TVA) ? "))
    
    # Seuils définis par la réforme
    seuil_tva = 25000  # seuil de TVA
    seuil_majoré = 27500  # seuil majoré de TVA
    
    # Vérification des seuils
    if chiffre_affaires < seuil_tva:
        print("\nVotre chiffre d'affaires est inférieur à 25 000 €, vous n'êtes pas soumis à la TVA.")
    elif chiffre_affaires <= seuil_majoré:
        print("\nVotre chiffre d'affaires est compris entre 25 000 € et 27 500 €, vous serez soumis à la TVA à partir du 1ᵉʳ janvier de l'année suivante.")
    else:
        print("\nVotre chiffre d'affaires dépasse 27 500 €, vous êtes déjà soumis à la TVA.")
        
simulateur_tva()
