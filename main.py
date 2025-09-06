from gui import GUI
from user import User


class App:
    def __init__(self):
        self.__user = User("1", "1")
        self.__gui = GUI()
        self.__gui.run(self.__user.check_login)


app = App()
