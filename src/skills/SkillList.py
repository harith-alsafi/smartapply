from src.skills.Skill import Skill
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

class SkillList:
    chrome_options:Options
    account:FetcherAccount
    soup:BeautifulSoup
    skill_elements:ResultSet
    text:str
    def __init__(self, link:str, account:FetcherAccount):
        self.skill_list:List[Skill] = []
        self.link:str = link+"details/skills/"
        self.account = account
    
    def parse(self):
        self.text = self.account.get_html(self.link)
        self.soup = BeautifulSoup(self.text, "html.parser")
        self.skill_elements = self.soup.find_all('li', class_='pvs-list__paged-list-item')
        if self.skill_elements == None:
            return
        for element in self.skill_elements:
            title = self.get_title(element)
            details_skills = self.get_skills_details(element)
            details = details_skills[0]
            skill = Skill(title, details)
            self.skill_list.append(skill)

    def get_title(self, element:ResultSet) -> str:
        title_div = element.find('div', class_='display-flex flex-wrap align-items-center full-height')
        title = "N/A"
        if title_div == None:
            return title
        title_element = title_div.find('span')
        if title_element == None:
            return title
        title = title_element.getText(strip=True)
        return title

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
        for skill in self.skill_list:
            print(skill)




