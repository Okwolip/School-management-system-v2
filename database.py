import os
from supabase import create_client, Client
import streamlit as st

# First try Streamlit secrets (for deployment)
SUPABASE_URL = None
SUPABASE_KEY = None

try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
except:
    pass

# If not found, try environment variables (local computer)
if not SUPABASE_URL:
    SUPABASE_URL = os.getenv("SUPABASE_URL")

if not SUPABASE_KEY:
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Final safety check
if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Supabase credentials not found. Check environment variables or Streamlit secrets.")

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
