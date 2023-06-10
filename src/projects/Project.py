from typing import List

class Project:
    def __init__(self, title:str, date_range:str, details:str, skills:List[str]):
        self.title:str = title
        self.date_range:str = date_range
        self.skills:List[str] = skills