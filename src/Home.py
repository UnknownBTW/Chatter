import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Home(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.build_ui()
    
    def build_ui(self):
        self.status_label = ctk.CTkLabel(self, text="Welcome to Chatter!")
        self.status_label.pack(pady=20)
        self.status_label.place(relx=0.5, rely=0.5, anchor="center")