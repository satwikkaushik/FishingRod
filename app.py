# this is the entry point
import streamlit as st
from utils import check_URL, extract_URL

def check_forwarding_URL(parent_URL):
    forwarding_URLs = extract_URL.extract(parent_URL)
    result = 0

    for link in forwarding_URLs:
        link_result = check_URL.check(link)
        if(link_result == -1):
            break
        else :
            result += link_result

    if(round(result/len(forwarding_URLs), 2) <= 0.30):
        return 0
    else:
        return 1
    
def main():
    # css for centering
    st.set_page_config(layout="centered")

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
            parent_URL_result = check_URL.check(user_input)
            
            if(parent_URL_result == 0):
                st.write('<span style="color: green; font-size: 18px;">Parent URL is Safe*</span>', unsafe_allow_html=True)
                st.write('<span style="color: green; font-size: 18px;">Analyzing Forwarding URLs</span>', unsafe_allow_html=True)

                fowarding_URL_result = check_forwarding_URL(user_input)
                if(fowarding_URL_result == 0):
                    st.write('<span style="color: green; font-size: 18px;">Forwarding URLs are Safe*</span>', unsafe_allow_html=True)
                else:
                    st.write('<span style="color: red; font-size: 18px;">Forwarding URLs were flagged Phishing*</span>', unsafe_allow_html=True)

            elif(parent_URL_result == 1):
                st.write('<span style="color: red; font-size: 18px;">Parent URL is flagged phishing*</span>', unsafe_allow_html=True)
            else:
                st.write('<span style="color: orange; font-size: 18px;">Some Error Occurred</span>', unsafe_allow_html=True)
            

    st.write('<span style="color: grey; font-size: 12px;">* : the model may produce wrong results. Please proceed with own caution</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()