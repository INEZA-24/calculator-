'''import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
window.title("My first GUI")
add = tk.Label(window, text="Addition", font=('Tahoma', 10))
add.pack(padx=20, pady=20)
textbox = tk.Text(window, font=('Arial', 16), height=3)
textbox.pack(padx=20, pady=20)
button = tk.Button(window, height=1, text="click here ", font="Helvetica")
button.pack(padx=1)
buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 10))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 10))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 10))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 10))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 10))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 10))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')


window.mainloop()'''
import tkinter as tk 
class mygui:
    def __init__(self):
        self.root=tk.Tk()

        self.root.mainloop()

        
