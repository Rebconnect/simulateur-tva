import streamlit as st

def simulateur_tva_charges():
    st.title("Simulateur de TVA : Charges, Produits et Prévisionnel")

    # Collecte des informations de l'utilisateur
    chiffre_affaires = st.number_input("Quel est votre chiffre d'affaires annuel (hors TVA) ?", min_value=0.0, step=100.0)
    charges_professionnelles = st.number_input("Quel est le total de vos charges professionnelles annuelles (hors TVA) ?", min_value=0.0, step=100.0)
    charges_deductibles = st.number_input("Quel montant de vos charges est déductible (TVA récupérable) ?", min_value=0.0, step=100.0)
    type_activite = st.selectbox("Quel est votre type d'activité ?", ["Vente de biens", "Prestation de services", "Mixte"])

    # Seuils de TVA
    seuil_tva = 25000  # seuil de TVA
    taux_tva = 0.2  # taux de TVA standard à 20%

    # Calcul de la TVA collectée
    tva_collectee = chiffre_affaires * taux_tva

    # Calcul de la TVA déductible
    tva_deductible = charges_deductibles * taux_tva

    # Calcul de la TVA nette (collectée - déductible)
    tva_nette = tva_collectee - tva_deductible

    # Affichage des résultats
    st.subheader("Prévisionnel de TVA")
    st.write(f"TVA collectée sur votre chiffre d'affaires : {tva_collectee:.2f}€")
    st.write(f"TVA déductible sur vos charges : {tva_deductible:.2f}€")
    st.write(f"TVA nette à reverser : {tva_nette:.2f}€")

    # Conseils par rapport à l'activité
    if type_activite == "Vente de biens":
        st.write("Dans le cadre d'une vente de biens, vous pouvez récupérer la TVA sur vos achats de marchandises.")
    elif type_activite == "Prestation de services":
        st.write("Pour les prestations de services, vous pouvez récupérer la TVA sur vos frais de sous-traitance, mais pas sur vos frais de personnel.")
    else:
        st.write("Si vous avez une activité mixte, vous devrez proportionner la TVA déductible en fonction de la part de votre activité de vente et de services.")

    # Simulation de passage en société
    statut_souhaite = st.selectbox("Souhaitez-vous passer en société (SARL, SAS, etc.) ?", ["Oui", "Non"])

    if statut_souhaite == "Oui":
        st.write("Passer en société vous permet de récupérer la TVA sur une plus grande variété de charges et d'optimiser votre fiscalité.")
        st.write("Il est conseillé de consulter un expert-comptable pour choisir le statut juridique qui vous conviendrait le mieux.")
    else:
        st.write("En restant en micro-entreprise, vous ne pourrez pas récupérer la TVA sur certaines charges, mais vous bénéficiez d'un régime simplifié.")

if __name__ == "__main__":
    simulateur_tva_charges()
