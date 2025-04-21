import streamlit as st
import firebase_admin
from firebase_admin import credentials
import json
import io

# Reformat the private key (replacing \n with actual newlines)
private_key = st.secrets["firebase"]["private_key"].replace("\\n", "\n")

# Create a complete credentials dictionary
firebase_credentials = {
    "type": st.secrets["firebase"]["type"],
    "project_id": st.secrets["firebase"]["project_id"],
    "private_key_id": st.secrets["firebase"]["private_key_id"],
    "private_key": private_key,
    "client_email": st.secrets["firebase"]["client_email"],
    "client_id": st.secrets["firebase"]["client_id"],
    "auth_uri": st.secrets["firebase"]["auth_uri"],
    "token_uri": st.secrets["firebase"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
}

# Convert the dictionary to a JSON string and wrap it as a file-like object
cred_file = io.StringIO(json.dumps(firebase_credentials))

# Load credentials from the file-like object
cred = credentials.Certificate(cred_file)
firebase_admin.initialize_app(cred)
