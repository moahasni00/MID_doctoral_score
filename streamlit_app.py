import streamlit as st

st.set_page_config(page_title="Doctoral Score Estimator", layout="centered")

st.title("🎓 Doctoral Candidacy Score Estimator")
st.write("Estimate your score out of 100 based on academic criteria.")

# --- Bac Mention ---
st.subheader("1. Mention au Baccalauréat (sur 10)")
mention_bac = st.selectbox("Sélectionnez votre mention :", [
    "Passable", "Assez Bien", "Bien", "Très Bien"
])

mention_scores = {
    "Passable": 2,
    "Assez Bien": 6,
    "Bien": 8,
    "Très Bien": 10
}
score_bac = mention_scores[mention_bac]

# --- Système Universitaire ---
st.subheader("2. Formation Universitaire (sur 70)")
system_type = st.radio("Quel est votre système universitaire ?", ["LMD", "NLMD"])

if system_type == "LMD":
    licence_avg = st.number_input("Moyenne générale de la Licence (/20)", min_value=0.0, max_value=20.0, value=12.0)
    master_avg = st.number_input("Moyenne générale du Master (/20)", min_value=0.0, max_value=20.0, value=14.0)
    score_univ = (licence_avg * 1.75) + (master_avg * 1.75)
else:
    global_avg = st.number_input("Moyenne générale de toutes les années (/20)", min_value=0.0, max_value=20.0, value=13.0)
    score_univ = global_avg * 3.5

# --- Redoublement ---
repeated_years = st.number_input("Nombre d’années redoublées", min_value=0, max_value=5, step=1)
penalty = repeated_years * 5
score_univ -= penalty
score_univ = max(0, round(score_univ, 2))  # Prevent negatives

# --- Spécialité ---
st.subheader("3. Spécialité du sujet de thèse (sur 20)")
speciality = st.selectbox("Votre formation est-elle liée au sujet ?", [
    "Loin de la spécialité", "Proche de la spécialité", "Dans la spécialité (ex: Économie, Statistique, Économétrie)"
])
speciality_scores = {
    "Loin de la spécialité": 0,
    "Proche de la spécialité": 10,
    "Dans la spécialité (ex: Économie, Statistique, Économétrie)": 20
}
score_speciality = speciality_scores[speciality]

# --- Total ---
score_total = round(score_bac + score_univ + score_speciality, 2)

# --- Display Results ---
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

# Footer
st.markdown("---")
st.caption("© Mohammed Amine Hasni – Estimation basée sur les critères officiels de présélection doctorale.")
