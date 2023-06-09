from typing import List

class Education:
    def __init__(self, major:str, school:str, date_range:str, details:str, skills:str):
        self.major:str = major
        self.school:str = school
        self.date_range:str = date_range
        self.skills:List[str] = []
        self.details:str = details

    def __str__(self) -> str:
        pass


        
    