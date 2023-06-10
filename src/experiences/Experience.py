from typing import List

class Experience:
    def __init__(self, role:str, company:str, date_range:str, details:str, skills:List[str]) -> None:
        self.role:str = role
        self.company:str = company
        self.date_range:str = date_range
        self.skills:List[str] = skills
        self.details:str = details
    
    def __str__(self) -> str:
        return f"Role: {self.role}\nCompany: {self.company}\nDate Range: {self.date_range}\nDetails: {self.details}\nSkills: {self.skills}\n"