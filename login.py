import streamlit as st
import base64

# Function to convert image to base64
def img_to_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set the background and styles
def set_background_and_style():
    st.markdown(
        f"""
        <style>
        /* Background Image with Opacity */
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                        url("data:image/png;base64,{img_to_base64('background.jpg')}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* Container to Center Login Form */
        .block-container {{
            max-width: 600px;
            padding-top: 50px;
        }}

        /* Text Box Styling - Fixed Length */
        input[type="text"], input[type="password"] {{
            width: 100% !important;
            max-width: 600px !important;
            padding: 12px !important;
            font-size: 16px !important;
            border: 2px solid #2E3B55 !important;
            border-radius: 8px !important;
        }}

        /* Input labels (text like 'Username', 'Password') in black */
        .stTextInput label, .stPasswordInput label {{
            color: #000000 !important; /* Black text for input labels */
            font-weight: bold;
            font-size: 16px;
        }}

        /* Buttons Styling - Smaller and Centered */
        .stButton {{
            text-align: center;  /* Center the button */
        }}
        .stButton button {{
            background-color: #2E3B55;
            color: #FFFFFF !important;
            border-radius: 8px;
            padding: 8px 12px;  /* Smaller padding */
            font-size: 14px;     /* Slightly smaller text */
            font-weight: bold;
            width: 100px;        /* Fixed width */
            margin: auto;        /* Center horizontally */
            display: block;      /* Ensure block-level for centering */
        }}

        /* Tabs Styling */
        .stTabs [role="tab"] {{
            color: #000000 !important;  /* Black text for tabs */
            font-weight: bold;
        }}

        /* Titles and Text General Styling */
        h1, h2, h3, h4 {{
            color: #2E3B55;
            text-align: center;
        }}

        /* Center the iframe properly */
        .iframe-container {{
            display: flex;
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            margin-top: 50px; /* Optional: Add space from the top */
        }}
        .iframe-container iframe {{
            width: 900px;
            height: 500px;
            border: none; /* Remove iframe border */
        }}

        /* Error and Success Message Styling */
        .stAlert {{
            background-color: rgba(46, 59, 85, 0.8) !important; /* Darker background */
            color: white !important; /* White text */
            font-weight: bold !important;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Initial Session State
if "USER_CREDENTIALS" not in st.session_state:
    st.session_state["USER_CREDENTIALS"] = {"admin": "password123", "user1": "pass1", "user2": "pass2"}
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Login Function
def login(username, password):
    if username in st.session_state["USER_CREDENTIALS"] and st.session_state["USER_CREDENTIALS"][username] == password:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.success("Login successful!")
    else:
        st.error("Invalid username or password. Please try again.")

# Signup Function
def signup(new_username, new_password, confirm_password):
    if new_username in st.session_state["USER_CREDENTIALS"]:
        st.error("Username already exists. Please choose a different one.")
    elif new_password != confirm_password:
        st.error("Passwords do not match. Try again.")
    else:
        st.session_state["USER_CREDENTIALS"][new_username] = new_password
        st.success("Signup successful! Please log in.")

# Logout Function
def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.info("You have been logged out.")

# Apply the background and styles
set_background_and_style()

# App Logic
if not st.session_state["logged_in"]:
    # Login / Signup Tabs
    st.title("Air Quality Insights 🚀")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        st.subheader("Login")
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            if st.button("Login", key="login_button"):
                login(username, password)

    with tab2:
        st.subheader("Signup")
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            new_username = st.text_input("New Username", key="signup_username")
            new_password = st.text_input("New Password", type="password", key="signup_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
            if st.button("Signup", key="signup_button"):
                signup(new_username, new_password, confirm_password)

else:
    # Sidebar for Logout
    st.sidebar.button("Logout", on_click=logout)

    # Dashboard Content
st.markdown("""
    <h2 class='welcome-title' style='color: black; font-family: Arial, sans-serif; font-size: 36px; font-weight: bold; text-align: center;'>
        Air Quality Insights Dashboard
    </h2>
""", unsafe_allow_html=True)


    # Centered iframe
    st.markdown(
        """
       <div style="display: flex; justify-content: center; align-items: center; width: 800px; height: 500px; overflow: hidden;">
            <iframe 
                src="https://app.powerbi.com/view?r=eyJrIjoiMGQ5NjI0YjItNjc2ZC00ZDRlLThjMmYtNjc2ZDdhODdiNzYyIiwidCI6IjkzZTljMTgyLTdhOWMtNGI4YS04YzY1LTM3OTMyNDZlYzgzMyJ9&rs:embed=true&filterPaneEnabled=false" 
                style="width: 1200px; height: 100%; border: none;" 
                allowfullscreen>
            </iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )
