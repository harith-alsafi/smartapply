
from src.logic.User import User


if __name__ == "__main__":
    user:User = User()
    user.parse("https://www.linkedin.com/in/harith-al-safi/")
    user.print()