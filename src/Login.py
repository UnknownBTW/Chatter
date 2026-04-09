import customtkinter as ctk
from supabase import create_client
from Home import Home
from App import App

url = "https://imwtmjjkqfztzdytqtlq.supabase.co"
key = "sb_publishable_8cW4rGyg71-W1zhcfkajUw_tBoJYmr_"

supabase = create_client(url, key)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class Login(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.status = ""
        self.build_ui()

    def build_ui(self):
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Email")
        self.email_entry.place(relx=0.5, rely=0.5, anchor="center", y=-50)
        self.email_entry.configure(width=200, height=30)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center", y=0)
        self.password_entry.configure(width=200, height=30)

        self.status_label = ctk.CTkLabel(self, text=self.status)
        self.status_label.place(relx=0.5, rely=0.5, anchor="center", y=30)
        self.status_label.configure(text_color="red")

        login_button = ctk.CTkButton(self, text="Log in", command=self.log_in)
        login_button.place(relx=0.5, rely=0.5, anchor="center", y=60)

        signup_button = ctk.CTkButton(self, text="Sign up", command=self.sign_in, fg_color="transparent", hover_color="#171717")
        signup_button.place(relx=0.5, rely=0.5, anchor="center", y=100)

    def log_in(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.status_label.configure(text="Incorrect login credentials")
        response = supabase.auth.sign_in_with_password({ "email": email, "password": password })
        if response.user:
            print("Login successful")
            self.destroy()
            home_frame = Home(self.master)
            home_frame.pack(fill="both", expand=True)
            
        else:
            self.status_label.configure(text="Incorrect login credentials")


    def sign_in(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        try: 
            response = supabase.auth.sign_up({ 
                "email": email, "password": password 
            }) 
            if response.user: 
                print("Check emial")
                self.status_label.configure(text="Check your email for the login link!")

        except Exception as e: 
            self.status = "Signup failed: " + str(e)