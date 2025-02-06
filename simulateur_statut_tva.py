import streamlit as st

def simulateur_tva():
    st.title("Simulateur de TVA pour Micro-Entrepreneur")

    # Collecte des informations de l'utilisateur
    chiffre_affaires = st.number_input("Quel est votre chiffre d'affaires annuel (hors TVA) ?", min_value=0.0, step=100.0)
    charges_professionnelles = st.number_input("Quel est le total de vos charges professionnelles annuelles (hors TVA) ?", min_value=0.0, step=100.0)
    charges_deductibles = st.number_input("Quel montant de vos charges est déductible (TVA récupérable) ?", min_value=0.0, step=100.0)
    type_activite = st.selectbox("Quel est votre type d'activité ?", ["Vente de biens", "Prestation de services", "Mixte"])

    # Seuils définis par la réforme
    seuil_tva = 25000  # seuil de TVA
    seuil_majoré = 27500  # seuil majoré de TVA
    taux_tva = 0.2  # taux de TVA standard à 20%

    # Vérification des seuils
    if chiffre_affaires < seuil_tva:
        st.subheader("Votre chiffre d'affaires est inférieur à 25 000 €, vous n'êtes pas soumis à la TVA.")
        st.write("Vous pouvez continuer à bénéficier de la franchise en base de TVA.")
        return

    # Vérification du seuil de tolérance
    if chiffre_affaires <= seuil_majoré:
        st.subheader("Votre chiffre d'affaires est compris entre 25 000 € et 27 500 €, vous serez soumis à la TVA à partir du 1ᵉʳ janvier de l'année suivante.")
        st.write("Il est conseillé de commencer à vous préparer à la collecte de la TVA.")
        return

    # Si le chiffre d'affaires dépasse le seuil et la tolérance
    st.subheader("Votre chiffre d'affaires dépasse 27 500 €, vous êtes déjà soumis à la TVA.")
    
    # Calcul TVA collectée et TVA déductible
    tva_collectee = chiffre_affaires * taux_tva
    tva_deductible = charges_deductibles * taux_tva
    
    # Affichage des résultats
    st.write(f"TVA collectée sur votre chiffre d'affaires : {tva_collectee:.2f}€")
    st.write(f"TVA récupérable sur vos charges déductibles : {tva_deductible:.2f}€")
    
    # Conseils de passage à un régime réel
    st.subheader("Passer à un régime réel d'imposition ?")
    st.write("Si vous avez beaucoup de charges déductibles et que vous souhaitez récupérer plus de TVA, un passage à un régime réel pourrait être bénéfique.")
    
    # Estimation selon le type d'activité
    if type_activite == "Vente de biens":
        st.write("Si vous vendez des biens, vous pouvez récupérer la TVA sur vos achats professionnels.")
    elif type_activite == "Prestation de services":
        st.write("Si vous proposez des services, vous pouvez récupérer la TVA sur vos charges professionnelles liées à cette activité.")
    else:
        st.write("Si vous avez une activité mixte, vous devrez gérer la TVA sur vos produits et services.")
    
    # Simulation des avantages d'un changement de statut
    statut_souhaite = st.selectbox("Souhaitez-vous passer en société (SARL, SAS, etc.) ?", ["Oui", "Non"])
    
    if statut_souhaite == "Oui":
        st.write("Passer en société implique de tenir une comptabilité complète, mais vous pourrez récupérer davantage de TVA sur vos charges et bénéficier d'autres avantages fiscaux.")
        st.write("Il peut être nécessaire de consulter un expert-comptable pour déterminer la structure juridique la plus adaptée.")
    else:
        st.write("Vous pouvez continuer en tant que micro-entrepreneur, mais assurez-vous de bien comprendre les implications de la TVA et la gestion de vos charges déductibles.")

if __name__ == "__main__":
    simulateur_tva()
