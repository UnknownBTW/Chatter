import tkinter as tk

def on_button_click():
    print("Button clicked!")

def main():
    window = tk.Tk()
    window.title("Chatter")
    window.geometry("400x300")

    button = tk.Button(window, text="Click Me", command=on_button_click, font=("Arial", 16), bg="#FF0000", fg="black", padx=20, pady=10)
    button.pack(pady=20)

    window.mainloop()