from src.education.EducationList import EducationList
from src.logic.FetcherAccount import FetcherAccount

if __name__ == "__main__":
    fetcher = FetcherAccount()
    fetcher.login()
    educationList = EducationList("https://www.linkedin.com/in/harith-al-safi/", fetcher)
    educationList.parse()
    educationList.print()
    fetcher.logout()