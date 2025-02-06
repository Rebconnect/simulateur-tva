import streamlit as st

def calculer_tva(ca):
    seuil_franchise = 25000
    seuil_seuil_majoration = 27500
    taux_tva = 0.20
    
    if ca <= seuil_franchise:
        return 0, "Franchise de TVA"
    elif seuil_franchise < ca <= seuil_seuil_majoration:
        return ca * taux_tva, "TVA applicable dès l'année suivante"
    else:
        return ca * taux_tva, "TVA applicable immédiatement"

def calculer_charges(ca, taux_charges):
    return ca * taux_charges

def calculer_impots(ca, taux_abattement, taux_ir):
    revenu_imposable = ca * (1 - taux_abattement)
    return revenu_imposable * taux_ir

def comparer_statuts(ca):
    tva_micro, statut_tva_micro = calculer_tva(ca)
    charges_micro = calculer_charges(ca, 0.22)
    impots_micro = calculer_impots(ca, 0.34, 0.11)
    benef_micro = ca - tva_micro - charges_micro - impots_micro
    
    # Simulation EI (Entreprise Individuelle)
    tva_ei, statut_tva_ei = calculer_tva(ca)
    charges_ei = calculer_charges(ca, 0.45)
    impots_ei = calculer_impots(ca - charges_ei, 0, 0.20)
    benef_ei = ca - tva_ei - charges_ei - impots_ei
    
    # Simulation EURL (unipersonnelle)
    tva_eurl, statut_tva_eurl = calculer_tva(ca)
    charges_eurl = calculer_charges(ca, 0.50)
    impots_eurl = calculer_impots(ca - charges_eurl, 0, 0.15)
    benef_eurl = ca - tva_eurl - charges_eurl - impots_eurl
    
    # Simulation SASU
    tva_sasu, statut_tva_sasu = calculer_tva(ca)
    charges_sasu = calculer_charges(ca, 0.55)
    impots_sasu = calculer_impots(ca - charges_sasu, 0, 0.25)
    benef_sasu = ca - tva_sasu - charges_sasu - impots_sasu
    
    return {
        "Micro-entreprise": (benef_micro, statut_tva_micro, charges_micro, impots_micro, tva_micro),
        "Entreprise Individuelle": (benef_ei, statut_tva_ei, charges_ei, impots_ei, tva_ei),
        "EURL": (benef_eurl, statut_tva_eurl, charges_eurl, impots_eurl, tva_eurl),
        "SASU": (benef_sasu, statut_tva_sasu, charges_sasu, impots_sasu, tva_sasu),
    }

st.title("Simulateur de Statut & TVA")
ca = st.number_input("Entrez votre chiffre d'affaires annuel (€)", min_value=0)

if st.button("Simuler"):
    resultats = comparer_statuts(ca)
    
    st.subheader("Résultats :")
    for statut, (benef, tva_statut, charges, impots, tva) in resultats.items():
        st.write(f"**{statut}** → Bénéfice net estimé : {benef:.2f} € | {tva_statut}")
        st.write(f"  - Charges totales : {charges:.2f} €")
        st.write(f"  - Impôts estimés : {impots:.2f} €")
        st.write(f"  - TVA due : {tva:.2f} €")
