import streamlit as st
import requests

def main():
    st.title("DELETE METHOD - API TESTING")

    pet_id = st.text_input("Enter Pet ID", value=500)

    if st.button("DELETE METHOD TEST"):
        url = f"https://petstore.swagger.io/v2/pet/{pet_id}"

        response = requests.delete(url)

        if response.status_code == 200:
            st.write(f"Successfully deleted the pet. Status code: {response.status_code}")

        else:
            st.write(f"Failed! Status code: {response.status_code}")
            st.write("Response:", response.text)

