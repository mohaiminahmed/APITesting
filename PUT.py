import streamlit as st
import requests
import json

def main():
    st.write("PUT METHOD - API TESTING")

    pet_id = st.text_input("Enter Pet ID", value=500)
    pet_name = st.text_input("Enter Pet Name", value="Koala")

    if st.button("PUT METHOD TEST"):
        url = "https://petstore.swagger.io/v2/pet"

        pet_data = {
            "id": int(pet_id),
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": pet_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.put(url, data=json.dumps(pet_data), headers=headers)

        if response.status_code == 200:
            st.write(f"Success! Status code: {response.status_code}")
            st.write("Response:", response.json())

        else:
            st.write(f"Failed! Status code: {response.status_code}")
            st.write("Response:", response.text)