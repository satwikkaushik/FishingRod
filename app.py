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

def buttonClicked(user_input):
    if(user_input == ""):
        st.write("Please enter a valid URL")
        return
    
    # call required functions
    parent_URL_result = check_URL.check(user_input)
    
    # rendering results in right side of UI
    with right_UI:
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
    
def main():
    # elements in left side of UI
    with left_UI:
        user_input = st.text_input("Enter URL", key="user_input")
        if st.button("Check"):
            buttonClicked(user_input)

    # elements in right side of UI
    with right_UI:
        pass

    st.write('<span style="color: grey; font-size: 12px;">* : the model may produce wrong results. Please proceed with own caution</span>', unsafe_allow_html=True)

# dividing UI into two columns
left_UI, right_UI = st.columns([2, 1])

if __name__ == "__main__":
    main()