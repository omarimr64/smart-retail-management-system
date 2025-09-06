import tkinter as tk
from tkinter import font, messagebox
from plyer import notification
import random


class GUI:
    def __init__(self):
        print("GUI started")
        self.__start_GUI()

    def __start_GUI(self):
        self.__root = tk.Tk()
        self.__global_font = font.Font(family="Arial", size=16, weight="normal")
        self.__title_font = font.Font(family="Arial", size=22, weight="bold")
        self.__pages = {}
        self.__current_page = ""

        root = self.__root

        # Widget
        root.title("Smart Retail Management System")
        root.geometry("1000x700")
        root.resizable(False, False)
        root.configure(bg="#1e1e1e")

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

        # Pages frame
        self.__container = tk.Frame(self.__root)
        self.__container.pack(fill="both", expand=True)

    # LOGIN PAGE
    def __configure_login(self, check_login):
        # Login Functionality
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

            self.__root.focus()
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

        # Login frame
        login_frame = tk.Frame(self.__container)
        self.__add_page("login", login_frame)
        self.__show_page("login")

        inner_frame = tk.Frame(login_frame)
        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

        label = tk.Label(login_frame, text="Login", font=self.__title_font)
        label.pack(pady=(0, 50))

        username_label = tk.Label(inner_frame, text="Username:")
        username_label.grid(row=1, column=0, pady=5, sticky="w")
        username_entry = tk.Entry(inner_frame)
        username_entry.grid(row=1, column=1, pady=5, sticky="e")

        password_label = tk.Label(inner_frame, text="Password:")
        password_label.grid(row=2, column=0, pady=5, sticky="w")
        password_entry = tk.Entry(inner_frame, show="*")
        password_entry.grid(row=2, column=1, pady=5, sticky="e")

        submit_button = tk.Button(inner_frame, text="login", command=login)
        submit_button.grid(row=3, column=1, pady=5, sticky="e")

    # VERIFICATION MODAL
    def __open_verification_modal(self, verification_code):
        # Verification functionality
        def verification():
            if verification_entry.get() == str(verification_code):
                print("Verified")
                modal.destroy()
                self.__show_page("dashboard")
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

    # DASHBOARD PAGE
    def __configure_dashboard(self):
        dashboard_frame = tk.Frame(self.__container)
        self.__add_page("dashboard", dashboard_frame)

        # Title
        label = tk.Label(dashboard_frame, text="Dashboard", font=self.__title_font)
        label.pack(pady=(0, 50))

        # Dashboard navigation
        dashboard_navbar = tk.Frame(dashboard_frame)
        dashboard_navbar.pack(pady=10, fill="x")

        grocery_btn = tk.Button(
            dashboard_navbar, text="grocery", command=self.__show_grocery_content
        )
        grocery_btn.pack(side="left", padx=20)

        stationary_btn = tk.Button(
            dashboard_navbar, text="stationary", command=self.__show_stationary_content
        )
        stationary_btn.pack(side="left")

        cart_btn = tk.Button(
            dashboard_navbar, text="cart", command=self.__show_cart_content
        )
        cart_btn.pack(side="right", padx=(0, 20))

        # Dashboard content
        self.__dashboard_content = tk.Frame(dashboard_frame)
        self.__dashboard_content.pack(pady=(10, 0), fill="both")
        self.__dashboard_current_frame = tk.Frame()
        self.__show_grocery_content()

    # MULTIPLE PAGES
    def __add_page(self, page_name, page_frame):
        self.__pages[page_name] = page_frame

    def __show_page(self, page_name, pad=0):
        if page_name not in self.__pages:
            return "ERROR"

        if self.__current_page:
            self.__pages[self.__current_page].pack_forget()

        self.__current_page = page_name
        self.__pages[page_name].pack(pady=pad, fill="both", expand=True)

    # DASHBOARD CONTENTS
    def __show_grocery_content(self):
        grocery_frame = tk.Frame(self.__dashboard_content)
        grocery_frame.pack()

        self.__dashboard_current_frame.pack_forget()
        self.__dashboard_current_frame = grocery_frame

        content_title = tk.Label(grocery_frame, text="Grocery", font=self.__title_font)
        content_title.pack()

    def __show_stationary_content(self):
        stationary_frame = tk.Frame(self.__dashboard_content)
        stationary_frame.pack()

        self.__dashboard_current_frame.pack_forget()
        self.__dashboard_current_frame = stationary_frame

        content_title = tk.Label(
            stationary_frame, text="Stationary", font=self.__title_font
        )
        content_title.pack()

    def __show_cart_content(self):
        cart_frame = tk.Frame(self.__dashboard_content)
        cart_frame.pack()

        self.__dashboard_current_frame.pack_forget()
        self.__dashboard_current_frame = cart_frame

        content_title = tk.Label(cart_frame, text="Cart", font=self.__title_font)
        content_title.pack()

    # RUNING THE APP
    def run(self, check_login):
        self.__configure_login(check_login)
        self.__configure_dashboard()
        self.__root.mainloop()
