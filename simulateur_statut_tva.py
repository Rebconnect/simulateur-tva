import streamlit as st

def calculer_tva(ca, tva_deductible=0):
    seuil_franchise = 25000
    seuil_majoration = 27500
    taux_tva = 0.20
    
    if ca <= seuil_franchise:
        return 0, "Franchise de TVA", 0
    elif seuil_franchise < ca <= seuil_majoration:
        return ca * taux_tva, "TVA applicable dès l'année suivante", tva_deductible
    else:
        return ca * taux_tva, "TVA applicable immédiatement", tva_deductible

def calculer_charges(ca, taux_charges):
    return ca * taux_charges

def calculer_impots(revenu_imposable, taux_ir):
    return revenu_imposable * taux_ir

def comparer_statuts(ca, charges_deductibles, charges_non_deductibles, tva_deductible):
    resultats = {}
    
    statuts = {
        "Micro-entreprise": (0.22, 0.34, 0.11),
        "Entreprise Individuelle": (0.45, 0, 0.20),
        "EURL": (0.50, 0, 0.15),
        "SASU": (0.55, 0, 0.25)
    }
    
    for statut, (taux_charges, taux_abattement, taux_ir) in statuts.items():
        tva_collectee, statut_tva, tva_ded = calculer_tva(ca, tva_deductible)
        charges_totales = calculer_charges(ca, taux_charges) + charges_non_deductibles
        revenu_imposable = ca - charges_totales - tva_collectee + charges_deductibles
        impots = calculer_impots(revenu_imposable, taux_ir)
        benefice_net = ca - tva_collectee - charges_totales - impots + tva_ded
        
        resultats[statut] = (benefice_net, statut_tva, charges_totales, impots, tva_collectee, tva_ded)
    
    return resultats

st.title("Simulateur de Statut & TVA")
ca = st.number_input("Entrez votre chiffre d'affaires annuel (€)", min_value=0)
tva_deductible = st.number_input("Entrez votre TVA déductible (€)", min_value=0)
charges_deductibles = st.number_input("Entrez vos charges déductibles (€)", min_value=0)
charges_non_deductibles = st.number_input("Entrez vos charges non déductibles (€)", min_value=0)

if st.button("Simuler"):
    resultats = comparer_statuts(ca, charges_deductibles, charges_non_deductibles, tva_deductible)
    
    st.subheader("Résultats :")
    for statut, (benef, tva_statut, charges, impots, tva, tva_ded) in resultats.items():
        st.write(f"**{statut}** → Bénéfice net estimé : {benef:.2f} € | {tva_statut}")
        st.write(f"  - Charges totales : {charges:.2f} €")
        st.write(f"  - Impôts estimés : {impots:.2f} €")
        st.write(f"  - TVA collectée : {tva:.2f} €")
        st.write(f"  - TVA déductible : {tva_ded:.2f} €")
