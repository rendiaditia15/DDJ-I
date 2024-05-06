from tkinter import *

def display_greeting():
    greeting_label.config(text="Hallo Selamat Datang!")
    
window = Tk()
window.title("Program Sambutan")

greeting_label = Label(window, text="")
greeting_label.pack(pady=20)

greet_button = Button(window, text="Tampilkan Sambutan", command=display_greeting)
greet_button.pack()

window.mainloop()