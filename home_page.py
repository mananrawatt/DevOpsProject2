import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Function to load lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load local CSS file
local_css("style.css")

# Load lottie animation
lottie_coding = load_lottieurl("https://lottie.host/0c515a48-108e-46c0-870e-02bb7d022638/qPtkf5RtXn.json")

# Load images
img_contact_form = Image.open("images/images.png")
img_lottie_animation = Image.open("images/download.jpg")


def home_content():
    # Header section
    with st.container():
        st.subheader("Hi, Welcome :wave:")
        st.title("DevOps Automation")
        st.write(
            "A DevOps engineer bridges the gap between development and operations, focusing on automating and streamlining processes to improve software delivery."
        )
        st.write("[Learn More >](https://pythonandvba.com)")

    # What I do section
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
               - CI/CD Pipeline Management:
                Design, implement, and maintain automated build, test, and deployment pipelines.

               - Infrastructure as Code (IaC):
                Use tools like Terraform and Ansible to manage infrastructure through code, ensuring consistency and scalability.

               - Monitoring and Logging:
                Implement and maintain monitoring and logging systems to track application performance and troubleshoot issues.

               - Containerization and Orchestration:
                Use Docker for containerizing applications and Kubernetes for managing container orchestration.

               - Automation and Scripting:
                Automate repetitive tasks and workflows using scripting languages like Bash, Python, or PowerShell.
                """
            )
            st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")

        with right_column:
            st_lottie(lottie_coding, height=500, key="coding")

    # Projects section
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
                In this tutorial, I'll show you exactly how to do it
                """
            )
            st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.subheader("How To Add A Contact Form To Your Streamlit App")
            st.write(
                """
                Want to add a contact form to your Streamlit website?
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                """
            )
            st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

    # Contact section
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form = """
            <form action="https://formsubmit.co/mannanaxis@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

    # Define a function to redirect to a new page
    def redirect(url):
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)

    # Create a button to navigate to a new page
    if st.button("Go to New Page"):
        redirect("https://example.com/new_page")

