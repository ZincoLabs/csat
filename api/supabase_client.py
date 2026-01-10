from supabase import create_client
from config import SUPABASE_URL, SUPABASE_SERVICE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

def insert_survey(data: dict):
    return supabase.table("encuesta_satisfaccion").insert(data).execute()
