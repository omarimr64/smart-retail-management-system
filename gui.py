import tkinter as tk
from tkinter import font, messagebox
from plyer import notification
import random


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

    def __open_verification_modal(self, verification_code):

        def verification():
            if verification_entry.get() == str(verification_code):
                print("Verified")
                modal.destroy()
            else:
                messagebox.showerror("ERROR", "Incorrect code")

        # Create a new Toplevel window
        modal = tk.Toplevel(self.__root)
        modal.title("Modal Window")
        modal.geometry("350x200")

        modal.grab_set()
        modal.focus_set()
        modal.resizable(False, False)

        verification_label = tk.Label(modal, text="Varfication Code:")
        verification_label.pack(pady=20)

        verification_entry = tk.Entry(modal)
        verification_entry.pack(pady=20)

        verification_button = tk.Button(modal, text="enter", command=verification)
        verification_button.pack()

    def display_login(self, check_login):
        root = self.__root

        def login():
            if check_login(username_entry.get(), password_entry.get()):
                print("Logged In Successfully")

                verification_code = random.randint(100000, 999999)
                notification.notify(
                    title="System verification",
                    message=f"Your verification code is {verification_code}",
                    timeout=15,
                )

                self.__open_verification_modal(verification_code)
            else:
                messagebox.showerror("ERROR", "username or password is incorrect")

            root.focus()
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

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

        submit_button = tk.Button(frame, text="login", command=login)
        submit_button.grid(row=3, column=1, pady=5, sticky="e")

    def run(self):
        self.__root.mainloop()
