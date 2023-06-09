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

def get_resume():
    with open('assets/resume-template-2.html', 'r') as file:
        html_string = file.read()
    return html_string

def get_coverletter():
    with open('assets/coverletter-template.html', 'r') as file:
        html_string = file.read()
    return html_string

def get_questions():
    with open('assets/interviewquestions-template.html', 'r') as file:
        html_string = file.read()
    return html_string

#this is suppose to be the main function, but the variables are not being passed
st.header("Smart Apply 📋")
page_icon="📋"
st.subheader("Generated Resume!")

toggle_button1 = st.checkbox("Hide Resume")
st.empty()
if not toggle_button1:
    #Displays the resume
    st.markdown(get_resume(), unsafe_allow_html=True)

toggle_button2 = st.checkbox("Hide Cover Letter")
st.empty()
if not toggle_button2:
    #Displays the resume
    st.markdown(get_coverletter(), unsafe_allow_html=True)

toggle_button3 = st.checkbox("Hide Interview Questions")
st.empty()
if not toggle_button3:
    #Displays the resume
    st.markdown(get_questions(), unsafe_allow_html=True)



with st.sidebar:
    st.title("Place your information:")
    input_linkedin = st.text_input("Place Your Linkedin URL")
    input_position = st.text_input("Place the job posting page")
    github_linkedin = st.text_input("Place Your Github URL")
    existing_resume = st.file_uploader("Upload your existing resume")




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