import streamlit as st
from PIL import Image

st.set_page_config(page_title="Doctoral Score Estimator", layout="wide")

# --- Header avec les logos ---
col_left, col_center, col_right = st.columns([1, 6, 1])
with col_left:
    # Charge le logo FEG01.png à la racine du repo
    logo_feg1 = Image.open("FEG01.png")
    st.image(logo_feg1, width=100)

with col_center:
    st.markdown(
        "<h1 style='text-align: center;'>🎓 Pôle d'Études Doctorales</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center;'>"
        "Université Hassan I – "
        "<a href='https://ced.uh1.ac.ma/' target='_blank'>https://ced.uh1.ac.ma</a>"
        "</p>",
        unsafe_allow_html=True
    )

with col_right:
    # Charge le logo FEG.png à la racine du repo
    logo_feg = Image.open("FEG.png")
    st.image(logo_feg, width=100)

st.markdown("---")

# --- Expander: Critères de présélection ---
with st.expander("📘 Critères de présélection – Cliquez pour voir les détails ou consultez la source officielle"):
    st.markdown("""
    ### 📋 Critères d’évaluation des candidatures au cycle doctoral
    
    Chaque dossier est noté sur **100 points**, répartis comme suit :
    
    #### 🎓 1. Baccalauréat (10 points)
    - Passable → 2 points  
    - Assez Bien → 6 points  
    - Bien → 8 points  
    - Très Bien → 10 points  

    #### 🎓 2. Formation Universitaire (70 points)
    - **Système LMD** :  
      - Licence (/20) × 1.75  
      - Master (/20) × 1.75  
    - **Système NLMD** :  
      - Moyenne générale × 3.5  
    - ⚠️ Chaque **année redoublée** retire **5 points** du total universitaire.

    #### 🧠 3. Spécialité (20 points)
    - Loin de la spécialité → 0 point  
    - Proche de la spécialité → 10 points  
    - Exactement dans la spécialité → 20 points  
    
    🔗 [Critères de préselection officiels](https://ced.uh1.ac.ma/criteres-de-preselection/)
    """)

# --- Expander: Sujets de recherche ---
with st.expander("📚 Sujets de recherche proposés"):
    st.markdown("""
    Les sujets de recherche proposés par les enseignants‑chercheurs 
    de l’Université Hassan 1er sont disponibles en ligne ici :
    [https://api-ced.uh1.ac.ma/sujets](https://api-ced.uh1.ac.ma/sujets)
    """)

# --- Inputs utilisateur ---
st.subheader("1. Mention au Baccalauréat (sur 10)")
mention_bac = st.selectbox(
    "Sélectionnez votre mention :",
    ["Passable", "Assez Bien", "Bien", "Très Bien"]
)
mention_scores = {"Passable": 2, "Assez Bien": 6, "Bien": 8, "Très Bien": 10}
score_bac = mention_scores[mention_bac]

st.subheader("2. Formation Universitaire (sur 70)")
system_type = st.radio(
    "Quel est votre système universitaire ?",
    ["LMD", "NLMD"]
)

if system_type == "LMD":
    licence_avg = st.number_input(
        "Moyenne Licence (/20)",
        min_value=0.0, max_value=20.0, value=12.0
    )
    master_avg = st.number_input(
        "Moyenne Master (/20)",
        min_value=0.0, max_value=20.0, value=14.0
    )
    score_univ = (licence_avg * 1.75) + (master_avg * 1.75)
else:
    global_avg = st.number_input(
        "Moyenne générale globale (/20)",
        min_value=0.0, max_value=20.0, value=13.0
    )
    score_univ = global_avg * 3.5

repeated_years = st.number_input(
    "Nombre d’années redoublées",
    min_value=0, max_value=5, step=1
)
penalty = repeated_years * 5
score_univ -= penalty
score_univ = max(0, round(score_univ, 2))

st.subheader("3. Spécialité du sujet de thèse (sur 20)")
speciality = st.selectbox(
    "Lien entre votre formation et le sujet de thèse :",
    [
        "Loin de la spécialité",
        "Proche de la spécialité",
        "Dans la spécialité (ex: Économie, Statistique, Économétrie)"
    ]
)
speciality_scores = {
    "Loin de la spécialité": 0,
    "Proche de la spécialité": 10,
    "Dans la spécialité (ex: Économie, Statistique, Économétrie)": 20
}
score_speciality = speciality_scores[speciality]

# --- Score total ---
score_total = round(score_bac + score_univ + score_speciality, 2)

st.markdown("---")
st.subheader("🧮 Résultat Final")
st.write(f"**Score Bac :** {score_bac} / 10")
st.write(f"**Score Formation Universitaire :** {score_univ} / 70")
st.write(f"**Score Spécialité :** {score_speciality} / 20")
st.success(f"🎯 **Score Total : {score_total} / 100**")

if score_total >= 65:
    st.markdown("✅ Vous êtes **compétitif** pour postuler au doctorat.")
elif score_total >= 50:
    st.markdown("⚠️ Vous êtes **éligible**, mais un bon projet renforcera votre dossier.")
else:
    st.markdown("❌ Vous êtes **en dessous du seuil recommandé** pour la sélection.")

# --- Footer ---
st.markdown("---")
st.caption(
    "© Mohammed Amine Hasni – Basé sur les critères officiels du "
    "Pôle d'Études Doctorales de l’Université Hassan I."
)
