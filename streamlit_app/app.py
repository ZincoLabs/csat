import streamlit as st
import requests

SCALE_MAPPING = {
    "Muy insatisfecho/a": 1,
    "Insatisfecho/a": 2,
    "Neutral": 3,
    "Satisfecho/a": 4,
    "Muy satisfecho/a": 5
}


st.set_page_config(page_title="Encuesta de Satisfacción", page_icon="📋")
st.title("Encuesta de Satisfacción ZincoLabs")
st.subheader("Tu opinión es muy importante para nosotros. Agradecemos de antemano tu tiempo, que no será más de 2 minutos.")

with st.form("encuesta"):
    
    client = st.text_area("¿Cuál es el nombre de tu empresa?")
    q1 = st.radio("1. ¿Cómo valorarías tu experiencia general con el servicio de ZincoLabs?", SCALE_MAPPING.keys())
    q2 = st.radio("2. ¿Cómo valorarías la calidad del producto que has recibido?", SCALE_MAPPING.keys())
    q3 = st.radio("3. ¿Cómo valorarías la atención recibida y la comunicación con el equipo?", SCALE_MAPPING.keys())
    q4 = st.radio("4. ¿El servicio cumplió tus expectativas?", SCALE_MAPPING.keys())

    improvement = st.text_area("¿En qué aspectos crees que podemos mejorar y cómo? (opcional)")
    comentarios = st.text_area("Comentarios adicionales (opcional)")

    if st.form_submit_button("Enviar"):
        payload = {
            "q1": SCALE_MAPPING[q1],
            "q2": SCALE_MAPPING[q2],
            "q3": SCALE_MAPPING[q3],
            "q4": SCALE_MAPPING[q4],
            "comentarios": comentarios
        }

        r = requests.post(f"{API_URL}/submit-survey", json=payload)

        if r.status_code == 200:
            st.success("✅ Gracias por tu respuesta")
        else:
            st.error("❌ Error enviando la encuesta")

