from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_survey_response(data: dict):
    supabase.table("encuesta_satisfaccion").insert(data).execute()
