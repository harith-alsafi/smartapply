from bs4 import BeautifulSoup
from src.logic.FetcherAccount import FetcherAccount

class JobInfo:
    def __init__(self, account:FetcherAccount) -> None:
        self.account:FetcherAccount = account
        self.text:str = None
        self.link:str = None
        self.job_role:str = None
        self.company:str = None
        self.location:str = None
        self.remote:str = None
        self.job_type:str = None
        self.industry:str = None
        self.details:str = None
        # self.about_company:str = None

    def parse(self, link:str):
        self.link = link
        self.text = self.account.get_html(link)
        self.soup = BeautifulSoup(self.text, "html.parser")
        job_div = self.soup.find('div', class_='jobs-search__job-details--container')
        if job_div == None:
            return
        job_title_element = job_div.find('h2', class_='t-24 t-bold jobs-unified-top-card__job-title')
        if job_title_element != None:
            self.job_role = job_title_element.getText(strip=True)
        company_element = job_div.find('a', class_='ember-view t-black t-normal')
        if company_element != None:
            self.company = company_element.getText(strip=True)
        location_element = job_div.find('span', class_='jobs-unified-top-card__bullet')
        if location_element != None:
            self.location = location_element.getText(strip=True)
        remote_element = job_div.find('span', class_='jobs-unified-top-card__workplace-type')
        if remote_element != None:
            self.remote = remote_element.getText(strip=True)
        job_type_elements = job_div.find_all('li', class_='jobs-unified-top-card__job-insight')
        
        if job_type_elements != None and job_type_elements.__len__() >= 2:
            span_element = job_type_elements[0].find('span')
            if span_element != None:
                self.job_type = span_element.getText(strip=True)
            span_element = job_type_elements[1].find('span')
            if span_element != None:
                self.industry = span_element.getText(strip=True)
        
        details_element =  job_div.find('div', class_='jobs-box__html-content jobs-description-content__text t-14 t-normal jobs-description-content__text--stretch', attrs={'id': 'job-details'})
        if details_element != None:
            self.details = details_element.getText(strip=True)
    
    def __str__(self) -> str:
        return f"Role={self.job_role}\nCompany={self.company}\nLocation={self.location}\nRemote={self.remote}\nJob Type={self.job_type}\nIndustry={self.industry}\nDetails={self.details}\n"
        
    def print(self):
        print(self.__str__())
                
        
        
