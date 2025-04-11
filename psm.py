import re
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Password Strength Meter by Arsala Rana",
    page_icon="🔐",
    layout="centered"
)

# --- Custom CSS Styling ---
st.markdown("""
<style>
/* Center align everything */
body, .main {
    text-align: center;
}

/* Input field styling */
div[data-baseweb="input"] {
    width: 60% !important;
    margin: auto;
}

/* Button styling */
.stButton > button {
    width: 50%;
    background-color: #45adf9;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    padding: 0.5em 1em;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #2e8ece;
}

/* Expander styling */
.stExpander {
    background-color: #f9f9f9 !important;
    border-radius: 10px;
}

/* Footer styling */
.footer {
    text-align: center;
    margin-top: 50px;
    font-size: 13px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# --- Page Header ---
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its security level 🔍")

# --- Function to Check Password Strength ---
def check_password_strength(password):
    score = 0 
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Upper and lower case check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase letters**.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one number (0–9)**.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?:{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*...)**.")

    # Result Display
    if score == 4:
        st.success("✅ Your password is **very strong**.")
    elif score == 3:
        st.info("✅ Your password is **moderate**.")
    else:
        st.error("❌ Your password is **weak**.")

    # Show feedback
    if feedback:
        with st.expander("🔍 How to improve your password"):
            for item in feedback:
                st.write(item)

# --- Input Field ---
password = st.text_input("Enter your password", type="password")

# --- Button ---
if st.button("Check Password"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")

# --- Footer ---
st.markdown("""
<div class='footer'>
Developed by <a href='https://github.com/arsala-rana' target='_blank'>Arsala Rana</a>
</div>
""", unsafe_allow_html=True)
