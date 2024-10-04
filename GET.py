import streamlit as st
import requests

def main():
    st.title("GET METHOD - API TESTING")

    pet_id = st.text_input("Enter Pet ID", value=500)

    if st.button("GET METHOD TEST"):
        url = f"https://petstore.swagger.io/v2/pet/{pet_id}"

        response = requests.get(url)

        if response.status_code == 200:
            pet_data = response.json()
            st.write("Success!")
            st.write("Response", pet_data)
        else:
            st.write(f"Failed! Status code: {response.status_code}")
            st.write("Response:", response.text)