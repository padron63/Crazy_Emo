from tkinter import *

def click():
    print('Good Job Theodore')
window = Tk()

photo = PhotoImage(file='Flanderson.png')

button = Button(window, text='Click me !',
             font=("Comic Sans",30),
             command=click,
             fg="#F0F0F8",
             bg="black",
             activeforeground="#F0F0F8",
             activebackground="black",
             state=ACTIVE,
             image=photo)

button.pack()

window.mainloop()