from concurrent.futures import ThreadPoolExecutor
from src.education.EducationList import EducationList
from src.logic.FetcherAccount import FetcherAccount
from src.experiences.ExperienceList import ExperienceList
from src.skills.SkillList import SkillList
from src.projects.ProjectList import ProjectList

def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()

class User:
    def __init__(self, account:FetcherAccount):
        self.fetcher:FetcherAccount = account
        self.education_list:EducationList = None
        self.experience_list:ExperienceList = None
        self.skill_list:SkillList = None
        # self.project_list:ProjectList = None

    def parse(self, link:str):
        self.education_list:EducationList = EducationList(link, self.fetcher)
        self.experience_list:ExperienceList = ExperienceList(link, self.fetcher)
        self.skill_list:SkillList = SkillList(link, self.fetcher)
        # self.project_list:ProjectList = ProjectList(link, self.fetcher)
        # run_io_tasks_in_parallel([self.education_list.parse, self.experience_list.parse, self.skill_list.parse])
        self.education_list.parse()
        self.experience_list.parse()
        self.skill_list.parse()
        # self.project_list.parse()

    def print(self):
        if self.education_list != None:
            print("Education: \n------------------\n")
            self.education_list.print()
        if self.experience_list != None:
            print("Experience: \n------------------\n")
            self.experience_list.print()
        if self.skill_list != None:
            print("Skills: \n------------------\n")
            self.skill_list.print()
        # if self.project_list != None:
        #     print("Projects: \n------------------\n")
        #     self.project_list.print()

