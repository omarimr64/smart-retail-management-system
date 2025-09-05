import tkinter as tk
from tkinter import font


class GUI:
    def __init__(self):
        print("GUI started")
        self.__root = tk.Tk()
        self.__global_font = font.Font(family="Arial", size=16, weight="normal")
        self.__title_font = font.Font(family="Arial", size=22, weight="bold")
        self.__configure_GUI()

    def __configure_GUI(self):
        root = self.__root

        # Widget
        root.title("Smart Retail Management System")
        root.geometry("1000x700")
        root.resizable(False, False)
        root.configure(bg="#1e1e1e")
        root.iconbitmap("")

        # Font
        root.option_add("*Font", self.__global_font)
        root.option_add("*Foreground", "white")
        root.option_add("*Background", "#1e1e1e")

        # App title
        label = tk.Label(
            root,
            text="smart retail management system".title(),
            pady=30,
            font=self.__title_font,
        )
        label.pack()

    def display_login(self):
        root = self.__root

        # Login form
        frame = tk.Frame(root)
        frame.pack(pady=150)

        label = tk.Label(frame, text="Login", font=self.__title_font)
        label.grid(row=0, column=0, pady=15, sticky="w")

        username_label = tk.Label(frame, text="Username:")
        username_label.grid(row=1, column=0, pady=5, sticky="w")
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1, pady=5, sticky="e")

        password_label = tk.Label(frame, text="Password:")
        password_label.grid(row=2, column=0, pady=5, sticky="w")
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, pady=5, sticky="e")

        submit_entry = tk.Button(
            frame,
            text="login",
        )
        submit_entry.grid(row=3, column=1, pady=5, sticky="e")

    def run(self):
        self.__root.mainloop()
