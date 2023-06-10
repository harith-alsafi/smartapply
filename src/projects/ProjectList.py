from src.projects.Project import Project
from src.logic.FetcherAccount import FetcherAccount
from typing import List, Tuple
from bs4 import BeautifulSoup, ResultSet
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProjectList:
    chrome_options:Options
    account:FetcherAccount
    soup:BeautifulSoup
    project_elements:ResultSet
    text:str
    def __init__(self, link:str, account:FetcherAccount):
        self.project_list:List[Project] = []
        self.link:str = link+"details/projects/"
        self.account = account
    
    def parse(self):
        self.text = self.account.get_html(self.link)
        self.soup = BeautifulSoup(self.text, "html.parser")
        self.project_elements = self.soup.find_all('li', class_='pvs-list__paged-list-item')
        if self.project_elements == None:
            return
        for element in self.project_elements:
            role = self.get_role(element)
            company = self.get_company(element)
            date_range = self.get_date_range(element)
            details_skills = self.get_skills_details(element)
            details = details_skills[0]
            skills =  details_skills[1]
            project = Project(role, company, date_range, details, skills)
            self.project_list.append(project)

    def get_role(self, element:ResultSet) -> str:
        role_div = element.find('div', class_='display-flex flex-wrap align-items-center full-height')
        role = "N/A"
        if role_div == None:
            return role
        role_element = role_div.find('span')
        if role_element == None:
            return role
        role = role_element.getText(strip=True)
        return role
    
    def get_company(self, element:ResultSet) -> str:
        company_span = element.find('span', class_='t-14')
        company = "N/A"
        if company_span == None:
            return company
        company_span = company_span.find('span', attrs={'aria-hidden': 'true'})
        if company_span == None:
            return company
        company = company_span.getText(strip=True)
        return company

    def get_date_range(self, element:ResultSet) -> str:
        date_range_element = element.find('span', class_='t-14 t-normal t-black--light')
        date_range = "N/A"
        if date_range_element == None:
            return date_range
        date_range_element = date_range_element.find('span')
        if date_range_element == None:
            return date_range
        date_range = date_range_element.getText(strip=True)
        return date_range

    def get_skills_details(self, element:ResultSet) -> Tuple[str, List[str]]:
        details = ""
        skill = ""
        skills:List[str] = []
        info = element.find('ul', class_='pvs-list')
        if info == None:
            return "N/A", skills
        info = info.find_all('span')
        if info == None:
            return "N/A", skills
        for i in info:
            found_skills = i.find('span', class_='white-space-pre')      
            if found_skills:
                skill = i.get_text(strip=True)
            elif i.has_attr('class') and i['class'][0] == 'visually-hidden':
                text = i.get_text(strip=True)
                if details != text:
                    details = details + text + "\n"
        
        if skill != "":
            index = skill.find("Skills:")
            if index != -1:
                skill = skill[index+7:]
                skills = skill.split("\u00b7")
                skills = [i.strip() for i in skills]
        return details, skills
    
    def print(self):
        print(self.link)
        for project in self.project_list:
            print(project)




