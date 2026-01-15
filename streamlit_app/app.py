import streamlit as st
from supabase import create_client

# -------------------------------
# Configuración segura
# -------------------------------

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = st.secrets["SUPABASE_SERVICE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

SCALE_MAPPING = {
    "Muy satisfecho/a": 5,
    "Satisfecho/a": 4,
    "Neutral": 3,
    "Insatisfecho/a": 2,
    "Muy insatisfecho/a": 1
}

# -------------------------------
# UI
# -------------------------------

st.set_page_config(page_title="Encuesta de Satisfacción", page_icon="📋")

st.title("¿Qué piensas de ZincoLabs?")
st.subheader(
    "Tu opinión es muy importante para nosotros. "
    "Agradecemos de antemano tu tiempo, que no será más de 2 minutos."
)

with st.form("encuesta"):

    name = st.text_input("¿Cuál es el nombre de tu empresa?")

    csat = st.radio(
        "1. ¿Cómo valorarías tu experiencia general con el servicio de ZincoLabs?",
        SCALE_MAPPING.keys()
    )

    quality = st.radio(
        "2. ¿Cómo valorarías la calidad del producto que has recibido?",
        SCALE_MAPPING.keys()
    )

    comunication = st.radio(
        "3. ¿Cómo valorarías la atención recibida y la comunicación con el equipo?",
        SCALE_MAPPING.keys()
    )

    expectations = st.radio(
        "4. ¿El servicio cumplió tus expectativas?",
        SCALE_MAPPING.keys()
    )

    nps = st.slider(
        "5. ¿Qué probabilidad hay de que recomiendes ZincoLabs a un amigo o familiar?",
        min_value=0,
        max_value=10,
        value=8
    )

    improvement = st.text_area(
        "¿En qué aspectos crees que podemos mejorar y cómo? (opcional)"
    )

    comment = st.text_area("Comentarios adicionales (opcional)")

    submitted = st.form_submit_button("Enviar")

# -------------------------------
# Inserción en Supabase
# -------------------------------

if submitted:
    data = {
        "name": name,
        "csat": SCALE_MAPPING[csat],
        "quality": SCALE_MAPPING[quality],
        "comunication": SCALE_MAPPING[comunication],
        "expectations": SCALE_MAPPING[expectations],
        "nps": nps,
        "improvement": improvement,
        "comment": comment
    }

    try:
        supabase.table("satisfaction").insert(data).execute()
        st.success("✅ Gracias por tu respuesta")

except Exception as e:
    st.error("❌ Error guardando la encuesta")
    st.code(str(e))



