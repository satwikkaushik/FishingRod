# this is the entry point
import streamlit as st
st.set_page_config(layout="centered")

# css for centering
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 50vh;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

# div container for centering
st.markdown('<div class="centered">', unsafe_allow_html=True)
user_input = st.text_input("Enter URL", key="user_input")

if st.button("Check"):
    if(user_input == ""):
        st.write("Please enter a valid URL")
    else:
        # call required functions
        pass

st.markdown('</div>', unsafe_allow_html=True)
