import tkinter as tk

def on_button_click():
    print("Button clicked!")

def main():
    window = tk.Tk()
    window.title("Chatter")
    window.geometry("400x300")

    button = tk.Button(window, text="Click Me", command=on_button_click)
    button.pack(pady=20)

    window.mainloop()