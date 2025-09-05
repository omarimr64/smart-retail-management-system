from gui import GUI


class App:
    def __init__(self):
        self.__gui = GUI()
        self.__gui.display_login()
        self.__gui.run()


app = App()
