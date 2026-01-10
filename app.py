import streamlit as st
from supabase_client import save_survey_response
from config import SCALE_MAPPING

st.set_page_config(page_title="Encuesta de Satisfacción", page_icon="📋")

st.title("📋 Encuesta de Satisfacción")
st.write("Tu opinión es muy importante. La encuesta es anónima y solo te llevará 2 minutos.")

with st.form("encuesta_satisfaccion"):

    q1 = st.radio(
        "1. ¿Cómo valorarías tu experiencia general?",
        options=list(SCALE_MAPPING.keys())
    )

    q2 = st.radio(
        "2. ¿Cómo valorarías la calidad del servicio?",
        options=list(SCALE_MAPPING.keys())
    )

    q3 = st.radio(
        "3. ¿Qué nivel de satisfacción tienes con la atención y comunicación recibida?",
        options=list(SCALE_MAPPING.keys())
    )

    q4 = st.radio(
        "4. ¿El servicio cumplió tus expectativas?",
        options=list(SCALE_MAPPING.keys())
    )

    comentarios = st.text_area("Comentarios adicionales (opcional)")

    submitted = st.form_submit_button("Enviar")

    if submitted:
        data = {
            "q1": SCALE_MAPPING[q1],
            "q2": SCALE_MAPPING[q2],
            "q3": SCALE_MAPPING[q3],
            "q4": SCALE_MAPPING[q4],
            "comentarios": comentarios
        }

        save_survey_response(data)
        st.success("✅ ¡Gracias! Tu respuesta ha sido registrada correctamente.")
