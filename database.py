import os
from supabase import create_client, Client
from dotenv import load_dotenv
import streamlit as st

# Load .env file (for local development)
load_dotenv()

SUPABASE_URL = None
SUPABASE_KEY = None

# 1️⃣ Try Streamlit Cloud secrets first
try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
except:
    pass

# 2️⃣ If not found, try environment variables (.env file)
if not SUPABASE_URL:
    SUPABASE_URL = os.getenv("SUPABASE_URL")

if not SUPABASE_KEY:
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# 3️⃣ Final check
if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Supabase credentials not found. Check .env file or Streamlit secrets.")

# 4️⃣ Connect
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
