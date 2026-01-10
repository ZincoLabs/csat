import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

SCALE_MAPPING = {
    "Muy insatisfecho/a": 1,
    "Insatisfecho/a": 2,
    "Neutral": 3,
    "Satisfecho/a": 4,
    "Muy satisfecho/a": 5
}
