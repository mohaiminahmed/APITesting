import streamlit as st
import GET, POST, PUT, PATCH, DELETE

st.set_page_config(
    page_title="API TESTING",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

selected_method = st.sidebar.selectbox(
    "Select an option:",
    ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
)

if selected_method == 'GET':
    GET.main()

elif selected_method == 'POST':
    POST.main()

elif selected_method == 'PUT':
    PUT.main()

elif selected_method == "PATCH":
    PATCH.main()

elif selected_method == "DELETE":
    DELETE.main()