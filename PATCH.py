import streamlit as st
import requests
import json

def main():
    st.write("This is intentionally left blank!")

    # pet_id = 500
    # url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    #
    # patch_data = {
    #     "name": "Penguin"
    # }
    #
    # headers = {
    #     'Content-Type': 'application/json'
    # }
    #
    # response = requests.patch(url, data=json.dumps(patch_data), headers=headers)
    #
    # if response.status_code == 200:
    #     st.write(f"Success! Status code: {response.status_code}")
    #     st.write("Response:", response.json())
    #
    # else:
    #     st.write(f"Failed! Status code: {response.status_code}")
    #     st.write("Response:", response.text)