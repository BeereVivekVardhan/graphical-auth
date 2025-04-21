import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Save image selection
email = st.text_input("Email")
img = st.file_uploader("Select image")

if st.button("Register") and img:
    db.collection("users").add({
        "email": email,
        "pattern": [img.name]  # You can enhance this with hashes or image IDs
    })
    st.success("User saved to Firebase!")
