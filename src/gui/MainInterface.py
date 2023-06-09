import streamlit as st
from streamlit_chat import message as st_message
import validators

class MainInterface:
    def __init__(self):
        pass
    def check_inputs(self):
        if not self.create_resume and not self.create_coverletter and not self.create_interview:
            st.write("Please select at least one option")
            checkbox_selected = False

        else:
            if not validators.url(self.input_linkedin):
                st.write("Please enter a valid Linkedin URL")
            elif not validators.url(self.input_position):
                st.write("Please enter a valid job posting URL")
            elif not validators.url(self.github_linkedin) and not self.github_linkedin =="":
                st.write("Please enter a valid Github URL")
            else:
                st.write("Recieving information.....")   
                self.user_facing()

    def user_facing(self):
        if self.create_resume:
            st.write("Generating Resume...")
        if self.create_coverletter:
            st.write("Generating Cover Letter...")
        if self.create_interview:
            st.write("Generating Interview Questions...")

    def get_resume(self):
        with open('assets/resume-template-2.html', 'r') as file:
            html_string = file.read()
        return html_string

    def get_coverletter(self):
        with open('assets/coverletter-template.html', 'r') as file:
            html_string = file.read()
        return html_string

    def get_questions(self):
        with open('assets/interviewquestions-template.html', 'r') as file:
            html_string = file.read()
        return html_string

    def main_interface(self):
        st.set_page_config(
            page_title="Smart Apply",
            page_icon="📋",
        )
        st.header("Smart Apply 📋")
        page_icon="📋"
        st.subheader("Generated Resume!")

        toggle_button1 = st.checkbox("Hide Resume")
        st.empty()
        if not toggle_button1:
            #Displays the resume
            st.markdown(self.get_resume(), unsafe_allow_html=True)

        toggle_button2 = st.checkbox("Hide Cover Letter")
        st.empty()
        if not toggle_button2:
            #Displays the resume
            st.markdown(self.get_coverletter(), unsafe_allow_html=True)

        toggle_button3 = st.checkbox("Hide Interview Questions")
        st.empty()
        if not toggle_button3:
            #Displays the resume
            st.markdown(self.get_questions(), unsafe_allow_html=True)



        with st.sidebar:
            st.title("Place your information:")
            self.input_linkedin = st.text_input("Place Your Linkedin URL")
            self.input_position = st.text_input("Place the job posting page")
            self.github_linkedin = st.text_input("Place Your Github URL")
            self.existing_resume = st.file_uploader("Upload your existing resume")




            st.write("what do you want to generate?")
            self.create_resume = st.checkbox("Create Resume")
            self.create_coverletter = st.checkbox("Create Cover Letter")
            self.create_interview =st.checkbox("Create Interview Questions")

            if st.button("Generate"):
                self.check_inputs()



# history = [
#    {
#        "message": "Hello, I'm a message",
#        "is_user": False

#    }
# ]