class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def check_login(self, username, password):
        if username == self.__username and password == self.__password:
            return True
