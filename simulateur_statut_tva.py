def simulateur_tva():
    print("Bienvenue dans le simulateur de TVA pour micro-entrepreneur.")
    
    # Collecte des informations de l'utilisateur
    chiffre_affaires = float(input("Quel est votre chiffre d'affaires annuel (hors TVA) ? "))
    charges_professionnelles = float(input("Quel est le total de vos charges professionnelles annuelles (hors TVA) ? "))
    charges_deductibles = float(input("Quel montant de vos charges est déductible (TVA récupérable) ? "))
    type_activite = input("Quel est votre type d'activité (vente de biens / prestation de services / mixte) ? ").lower()
    
    # Seuils définis par la réforme
    seuil_tva = 25000  # seuil de TVA
    seuil_majoré = 27500  # seuil majoré de TVA
    taux_tva = 0.2  # taux de TVA standard à 20%
    
    # Vérification des seuils
    if chiffre_affaires < seuil_tva:
        print("\nVotre chiffre d'affaires est inférieur à 25 000 €, vous n'êtes pas soumis à la TVA.")
        print("Vous pouvez continuer à bénéficier de la franchise en base de TVA.")
        return
    
    # Vérification du seuil de tolérance
    if chiffre_affaires <= seuil_majoré:
        print("\nVotre chiffre d'affaires est compris entre 25 000 € et 27 500 €, vous serez soumis à la TVA à partir du 1ᵉʳ janvier de l'année suivante.")
        print("Il est conseillé de commencer à vous préparer à la collecte de la TVA.")
        return
    
    # Si le chiffre d'affaires dépasse le seuil et la tolérance
    print("\nVotre chiffre d'affaires dépasse 27 500 €, vous êtes déjà soumis à la TVA.")
    
    # Calcul TVA collectée et TVA déductible
    tva_collectee = chiffre_affaires * taux_tva
    tva_deductible = charges_deductibles * taux_tva
    
    # Affichage des résultats
    print(f"\nRésultats du calcul :")
    print(f"TVA collectée sur votre chiffre d'affaires : {tva_collectee}€")
    print(f"TVA récupérable sur vos charges déductibles : {tva_deductible}€")
    
    # Conseils de passage à un régime réel
    print("\nPasser à un régime réel d'imposition ?")
    print("Si vous avez beaucoup de charges déductibles et que vous souhaitez récupérer plus de TVA, un passage à un régime réel pourrait être bénéfique.")
    
    # Estimation selon le type d'activité
    if type_activite == "vente de biens":
        print("Si vous vendez des biens, vous pouvez récupérer la TVA sur vos achats professionnels.")
    elif type_activite == "prestation de services":
        print("Si vous proposez des services, vous pouvez récupérer la TVA sur vos charges professionnelles liées à cette activité.")
    else:
        print("Si vous avez une activité mixte, vous devrez gérer la TVA sur vos produits et services.")
    
    # Simulation des avantages d'un changement de statut
    statut_souhaite = input("\nSouhaitez-vous passer en société (SARL, SAS, etc.) ? (oui/non) : ").lower()
    
    if statut_souhaite == "oui":
        print("\nPasser en société implique de tenir une comptabilité complète, mais vous pourrez récupérer davantage de TVA sur vos charges et bénéficier d'autres avantages fiscaux.")
        print("Il peut être nécessaire de consulter un expert-comptable pour déterminer la structure juridique la plus adaptée.")
    elif statut_souhaite == "non":
        print("\nVous pouvez continuer en tant que micro-entrepreneur, mais assurez-vous de bien comprendre les implications de la TVA et la gestion de vos charges déductibles.")
    else:
        print("Choix non valide.")
        
simulateur_tva()
