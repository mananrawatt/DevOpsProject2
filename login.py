import streamlit as st
from streamlit_lottie import st_lottie
import requests
from header import header

def login_page():
    # Header
    st.markdown(header(), unsafe_allow_html=True)

    # Load Lottie animation
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Import CSS file for styling
    st.markdown(
        '<link rel="stylesheet" type="text/css" href="./style/login.css">',
        unsafe_allow_html=True
    )

    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    st.markdown('<h2 class="login-title">Login</h2>', unsafe_allow_html=True)

    lottie_coding = load_lottieurl("https://lottie.host/19375b79-c9bf-4afc-a80f-e0124bf214da/yXR9TVbtZN.json")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            id = st.text_input("ID", key="login-id-input")
            password = st.text_input("Password", type="password", key="login-password-input")
            if st.button("Login", key="login-button"):
                if id == "devops" and password == "devops":
                    st.success("Login successful")
                    st.session_state.authenticated = True
                    st.experimental_rerun()  # This will rerun the app to reflect the change in session state
                else:
                    st.markdown('<p class="login-error">Incorrect ID or Password</p>', unsafe_allow_html=True)

        with right_column:
            st_lottie(lottie_coding, height=400, key="coding")

    st.markdown('</div>', unsafe_allow_html=True)

login_page()

