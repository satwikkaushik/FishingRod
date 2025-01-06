# this is the entry point
import streamlit as st
from utils import check_URL, extractor

def check_forwarding_URL(parent_URL):
    forwarding_URLs = extractor.extract_URL(parent_URL)
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
        # no need for further checking if Parent URL was falgged
        if(parent_URL_result == 0):
            st.success("Parent URL is safe*")
            st.write("Analyzing forwarding URLs")

            # analyzing forwarding URL
            fowarding_URL_result = check_forwarding_URL(user_input)
            if(fowarding_URL_result == 0):
                st.success("Forwarding URLs are safe*")
            else:
                st.error("One or multiple forwarding URLs were flagged*")

        elif(parent_URL_result == 1):
            st.error("Parent URL was flagged*")
        else:
            st.warning("Some error occurred")
    
def main():
    # elements in left side of UI
    with left_UI:
        user_input = st.text_input("Enter URL", key="user_input")
        if st.button("Check"):
            buttonClicked(user_input)

        st.divider()
        st.caption("\* the model may produce wrong results. Please proceed with own caution")

    # elements in right side of UI
    with right_UI:
        pass


# heading
st.header("Fishing Rod 🎣")
st.divider()

# dividing UI into two columns
left_UI, right_UI = st.columns([2, 1])

if __name__ == "__main__":
    main()