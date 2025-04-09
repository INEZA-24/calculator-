import tkinter as tk
calculation = " "


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:

        result = str(eval(calculation))
        calculation = " "
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "error")


def clear_field():
    global calculation
    calculation = " "
    text_result.delete(1.0, "end")
    pass


main = tk.Tk()
main.geometry("315x320")
text_result = tk.Text(height=2, width=19, font=("Arial", 24))
text_result.grid(columnspan=5, )
# btn1
btn_1 = tk.Button(main, text=("1"), command=lambda: add_to_calculation(
    1), width=5, font=('Arial', 14))
btn_1.grid(column=0, row=1)
# btn 2
btn_2 = tk.Button(main, text=("2"), command=lambda: add_to_calculation(
    2), width=5, font=('Arial', 14))
btn_2.grid(column=1, row=1)
# btn3
btn_1 = tk.Button(main, text=("3"), command=lambda: add_to_calculation(
    3), width=5, font=('Arial', 14))
btn_1.grid(column=2, row=1)
# btn4
btn_1 = tk.Button(main, text=("4"), command=lambda: add_to_calculation(
    4), width=5, font=('Arial', 14))
btn_1.grid(column=0, row=2)
# btn5
btn_1 = tk.Button(main, text=("5"), command=lambda: add_to_calculation(
    5), width=5, font=('Arial', 14))
btn_1.grid(column=1, row=2)
# btn6
btn_1 = tk.Button(main, text=("6"), command=lambda: add_to_calculation(
    6), width=5, font=('Arial', 14))
btn_1.grid(column=2, row=2)
# btn6
btn_1 = tk.Button(main, text=("7"), command=lambda: add_to_calculation(
    7), width=5, font=('Arial', 14))
btn_1.grid(column=0, row=3)
# btn7
btn_1 = tk.Button(main, text=("8"), command=lambda: add_to_calculation(
    8), width=5, font=('Arial', 14))
btn_1.grid(column=1, row=3)
# btn8
btn_1 = tk.Button(main, text=("9"), command=lambda: add_to_calculation(
    9), width=5, font=('Arial', 14))
btn_1.grid(column=2, row=3)
# btn9
btn_1 = tk.Button(main, text=("0"), command=lambda: add_to_calculation(
    0), width=5, font=('Arial', 14))
btn_1.grid(column=0, row=4)
# bracket open
btn_1 = tk.Button(main, text=("("), command=lambda: add_to_calculation(
    "("), width=5, font=('Arial', 14))
btn_1.grid(column=1, row=4)
# bracket closed
btn_1 = tk.Button(main, text=(")"), command=lambda: add_to_calculation(
    ")"), width=5, font=('Arial', 14))
btn_1.grid(column=2, row=4)
# equal /answer
btn_1 = tk.Button(main, text=("="), command=evaluate_calculation,
                  width=5, font=('Arial', 14))
btn_1.grid(column=2, row=5)
# addition
btn_1 = tk.Button(main, text=(
    "+"), command=lambda: add_to_calculation("+"), width=5, font=('Arial', 14))
btn_1.grid(column=3, row=1)
# multiplication
btn_1 = tk.Button(main, text=("X"), command=lambda: add_to_calculation(
    "*"), width=5, font=('Arial', 14))
btn_1.grid(column=3, row=2)
# subtraction
btn_1 = tk.Button(main, text=("-"), command=lambda: add_to_calculation("-"),
                  width=5, font=('Arial', 14))
btn_1.grid(column=3, row=3)
# division
btn_1 = tk.Button(main, text=("/"), command=lambda: add_to_calculation(
    "/"), width=5, font=('Arial', 14))
btn_1.grid(column=3, row=4)
# clear
btn_1 = tk.Button(main, text=("Clear"), command=clear_field,
                  width=5, font=('Arial', 14))
btn_1.grid(column=1, row=5)

main.mainloop()
