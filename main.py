import streamlit as st
from streamlit_chat import message as st_message
import validators


def check_inputs():
    if not create_resume and not create_coverletter and not create_interview:
        st.write("Please select at least one option")
        checkbox_selected = False

    else:
        if not validators.url(input_linkedin):
            st.write("Please enter a valid Linkedin URL")
        elif not validators.url(input_position):
            st.write("Please enter a valid job posting URL")
        elif not validators.url(github_linkedin) and not github_linkedin =="":
            st.write("Please enter a valid Github URL")
        else:
            st.write("Recieving information.....")   
            user_facing()

def user_facing():
    if create_resume:
        st.write("Generating Resume...")
    if create_coverletter:
        st.write("Generating Cover Letter...")
    if create_interview:
        st.write("Generating Interview Questions...")


    st.set_page_config(
        page_title="Smart Apply",
        page_icon="📋",
    )


#this is suppose to be the main function, but the variables are not being passed
st.header("Smart Apply 📋")
with st.sidebar:
    st.title("Place your information:")
    input_linkedin = st.text_input("Place Your Linkedin URL")
    input_position = st.text_input("Place the job posting page")
    github_linkedin = st.text_input("Place Your Github URL")


    st.write("what do you want to generate?")
    create_resume = st.checkbox("Create Resume")
    create_coverletter = st.checkbox("Create Cover Letter")
    create_interview =st.checkbox("Create Interview Questions")

    if st.button("Generate"):
        check_inputs()




# history = [
#    {
#        "message": "Hello, I'm a message",
#        "is_user": False

#    }
# ]