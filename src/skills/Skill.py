class Skill:
    def __init__(self, title:str, details:str):
        self.title:str = title
        self.details:int = details

    def __str__(self) -> str:
        return f"Title: {self.title}\nDetails: {self.details}\n"