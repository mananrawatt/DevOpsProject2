# import streamlit as st
# import requests
#
# # Function to fetch Jenkins data
# def fetch_jenkins_data(jenkins_url, job_name, username, api_token):
#     try:
#         job_url = f"{jenkins_url}/job/{job_name}/api/json"
#         response = requests.get(job_url, auth=(username, api_token))
#         response.raise_for_status()  # Will raise an HTTPError for bad responses
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error fetching data from Jenkins: {e}")
#         return None
#
# # Function to display pipeline status
# def display_pipeline_status():
#     st.header("Jenkins Pipeline Status")
#     st.write("##")
#
#     jenkins_url = st.text_input("Jenkins URL", "http://localhost:8080")
#     job_name = st.text_input("Job Name")
#     username = st.text_input("Username")
#     api_token = st.text_input("API Token", type="password")
#
#     if st.button("Fetch Pipeline Status"):
#         data = fetch_jenkins_data(jenkins_url, job_name, username, api_token)
#         if data:
#             st.subheader("Jenkins Pipeline Status")
#             st.write(f"Job Name: {data['name']}")
#             st.write(f"Status: {data['color']}")
#             st.write(f"Builds: {len(data['builds'])}")
#             for build in data['builds']:
#                 st.write(f"Build Number: {build['number']}, URL: {build['url']}")
#                 st.write("---")
#         else:
#             st.write("No data to display")


import streamlit as st
import requests


# Function to fetch Jenkins data for a specific job
def fetch_jenkins_data(jenkins_url, job_name, username, api_token):
    try:
        job_url = f"{jenkins_url}/job/{job_name}/api/json"
        response = requests.get(job_url, auth=(username, api_token))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from Jenkins: {e}")
        return None


# Function to fetch Jenkins jobs
def fetch_jenkins_jobs(jenkins_url, username, api_token):
    try:
        response = requests.get(f"{jenkins_url}/api/json", auth=(username, api_token))
        response.raise_for_status()
        jobs = response.json().get('jobs', [])
        return [job['name'] for job in jobs]
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching jobs from Jenkins: {e}")
        return []


# Function to display pipeline status
def display_pipeline_status():
    st.header("Jenkins Pipeline Status")
    st.write("##")

    # Environment selection
    env = st.selectbox("Select Environment", ["dev", "uat", "pre-prod", "prod"])

    # Jenkins details inputs
    jenkins_url = st.text_input("Jenkins URL", "http://localhost:8080")
    username = st.text_input("Username")
    api_token = st.text_input("API Token", type="password")

    if jenkins_url and username and api_token:
        # Fetch Jenkins jobs
        jobs = fetch_jenkins_jobs(jenkins_url, username, api_token)
        if jobs:
            job_name = st.selectbox("Select Job", jobs)
            if st.button("Fetch Pipeline Status"):
                data = fetch_jenkins_data(jenkins_url, job_name, username, api_token)
                if data:
                    st.subheader("Jenkins Pipeline Status")
                    st.write(f"Job Name: {data['name']}")
                    st.write(f"Status: {data['color']}")
                    st.write(f"Builds: {len(data['builds'])}")
                    for build in data['builds']:
                        st.write(f"Build Number: {build['number']}, URL: {build['url']}")
                        st.write("---")
                else:
                    st.write("No data to display")
        else:
            st.write("No jobs found for the provided Jenkins URL.")
