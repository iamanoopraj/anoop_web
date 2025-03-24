import streamlit as st
import pickle
import hashlib
from PIL import Image
from streamlit_option_menu import option_menu

# Background Image (Ensure Streamlit supports it properly)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/previews/002/099/443/large_2x/programming-code-coding-or-hacker-background-programming-code-icon-made-with-binary-code-digital-binary-data-and-streaming-digital-code-vector.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "About", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

if selected == "Home":
    st.title("You have selected Home")
elif selected == "About":
    st.title("You have selected About")
elif selected == "Contact":
    st.title("You have selected Contact")

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load stored hashed passwords
def load_hashed_passwords():
    try:
        with open("hashed_pw.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Save hashed passwords
def save_hashed_passwords(passwords):
    with open("hashed_pw.pkl", "wb") as file:
        pickle.dump(passwords, file)

# Load existing users
users = load_hashed_passwords()

# Streamlit UI
st.title("Login System using Hashed Passwords")

menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])

if menu == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == hash_password(password):
            st.success("Login successful!")
            # Display image after login
            image = Image.open("anoop.jpg")  # Replace with your image path
            st.image(image, caption="Welcome!", use_column_width=True)
        else:
            st.error("Invalid username or password")

elif menu == "Sign Up":
    st.subheader("Create a New Account")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Sign Up"):
        if new_username in users:
            st.warning("Username already exists! Choose another one.")
        else:
            users[new_username] = hash_password(new_password)
            save_hashed_passwords(users)
            st.success("Account created successfully! You can now log in.")
            
