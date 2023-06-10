
from src.logic.FetcherAccount import FetcherAccount
from src.logic.JobInfo import JobInfo
from src.logic.User import User


if __name__ == "__main__":
    fetcher = FetcherAccount()
    fetcher.login()
    jobInfo = JobInfo(fetcher)
    user:User = User(fetcher)
    user.parse("https://www.linkedin.com/in/harith-al-safi/")
    user.print()
    jobInfo.parse("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3625988657")
    jobInfo.print()