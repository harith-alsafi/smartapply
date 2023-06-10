from src.education.EducationList import EducationList

if __name__ == "__main__":
    education_list = EducationList("https://www.linkedin.com/in/harith-alsafi/")
    education_list.parse()
    education_list.print()