import streamlit as st
from supabase import create_client

# -------------------------------
# Configuración segura
# -------------------------------

if "SUPABASE_URL" not in st.secrets or "SUPABASE_SERVICE_KEY" not in st.secrets:
    st.error("❌ Faltan las credenciales de Supabase en los secretos de Streamlit")
    st.stop()

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = st.secrets["SUPABASE_SERVICE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

SCALE_MAPPING = {
    "Muy insatisfecho/a": 1,
    "Insatisfecho/a": 2,
    "Neutral": 3,
    "Satisfecho/a": 4,
    "Muy satisfecho/a": 5
}

# -------------------------------
# UI
# -------------------------------

st.set_page_config(page_title="Encuesta de Satisfacción", page_icon="📋")

st.title("Encuesta de Satisfacción ZincoLabs")
st.subheader(
    "Tu opinión es muy importante para nosotros. "
    "Agradecemos de antemano tu tiempo, no te llevará más de 2 minutos."
)

with st.form("encuesta"):

    client = st.text_area("¿Cuál es el nombre de tu empresa?")

    q1 = st.radio(
        "1. ¿Cómo valorarías tu experiencia general con el servicio de ZincoLabs?",
        SCALE_MAPPING.keys()
    )

    q2 = st.radio(
        "2. ¿Cómo valorarías la calidad del producto que has recibido?",
        SCALE_MAPPING.keys()
    )

    q3 = st.radio(
        "3. ¿Cómo valorarías la atención recibida y la comunicación con el equipo?",
        SCALE_MAPPING.keys()
    )

    q4 = st.radio(
        "4. ¿El servicio cumplió tus expectativas?",
        SCALE_MAPPING.keys()
    )

    nps = st.slider(
        "5. ¿Qué probabilidad hay de que recomiendes nuestro servicio a un amigo o familiar?",
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
        "client": client,
        "q1": SCALE_MAPPING[q1],
        "q2": SCALE_MAPPING[q2],
        "q3": SCALE_MAPPING[q3],
        "q4": SCALE_MAPPING[q4],
        "nps": nps,
        "improvement": improvement,
        "comment": comment
    }

    try:
        supabase.table("encuesta_satisfaccion").insert(data).execute()
        st.success("✅ Gracias por tu respuesta")

    except Exception:
        st.error("❌ Error guardando la encuesta. Inténtalo más tarde.")


