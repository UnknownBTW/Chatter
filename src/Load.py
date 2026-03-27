import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Chatter")
    window.geometry("400x300")

    text = tk.Label(window, text="Updating", font=("Arial", 18), fg="#0026FF")
    text.pack(pady=20)

    return window