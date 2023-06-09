from edu.Education import Education
from typing import List
from bs4 import BeautifulSoup, ResultSet
import requests

class EducationList:
    soup:BeautifulSoup
    education_elements:ResultSet
    text:str
    def __init__(self, link:str):
        self.education_list:List[Education] = []
        self.link:str = link+"/details/education/"
    
    def parse(self):
        self.text = requests.get(self.link).text
        self.soup = BeautifulSoup(self.text, "html.parser")
        self.education_elements = self.soup.find_all('li', class_='pvs-list__paged-list-item')
        if self.education_elements == None:
            return
        for element in self.education_elements:
            university_name = self.get_university_name(element)
            degree = self.get_degree(element)
            date_range = self.get_date_range(element)
            details = self.get_details(element)
            skills = self.get_skills(element)
            education = Education(university_name, degree, date_range, details, skills)
            self.education_list.append(education)

    def get_university_name(self, element:ResultSet) -> str:
        university_div = element.find('div', class_='display-flex flex-wrap align-items-center full-height')
        university_name = "N/A"
        if university_div == None:
            return university_name
        university_element = university_div.find('span')
        if university_element == None:
            return university_name
        university_name = university_element.getText(strip=True)
        return university_name
    
    def get_degree(self, element:ResultSet) -> str:
        degree_span = element.find('span', class_='t-14')
        degree = "N/A"
        if degree_span == None:
            return degree
        degree_span = degree_span.find('span', attrs={'aria-hidden': 'true'})
        if degree_span == None:
            return degree
        degree = degree_span.getText(strip=True)
        return degree

    def get_date_range(self, element:ResultSet) -> str:
        date_range = "N/A"
        
        return date_range


    def get_details(self, element:ResultSet) -> str:
        details = "N/A"
        
        return details
    
    def get_skills(self, element:ResultSet) -> List[str]:
        skills = []
        
        return skills

