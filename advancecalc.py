import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        # create the result display
        self.result_label = tk.Label(master, textvariable=self.result_var, font=('Arial', 14))
        self.result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create the buttons
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'exp',
            '(', ')', 'sqrt', 'log', 'pi'
        ]
        row = 1
        col = 0
        for button_text in buttons:
            tk.Button(master, text=button_text, width=5, height=2, command=lambda x=button_text: self.button_click(x)).grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def button_click(self, button_text):
        if button_text == '=':
            try:
                result = str(eval(self.result_var.get()))
            except:
                result = "Error"
            self.result_var.set(result)
        elif button_text == 'sqrt':
            self.result_var.set(str(math.sqrt(float(self.result_var.get()))))
        elif button_text == 'log':
            self.result_var.set(str(math.log(float(self.result_var.get()))))
        elif button_text == 'sin':
            self.result_var.set(str(math.sin(float(self.result_var.get()))))
        elif button_text == 'cos':
            self.result_var.set(str(math.cos(float(self.result_var.get()))))
        elif button_text == 'tan':
            self.result_var.set(str(math.tan(float(self.result_var.get()))))
        elif button_text == 'exp':
            self.result_var.set(str(math.exp(float(self.result_var.get()))))
        elif button_text == 'pi':
            self.result_var.set(str(math.pi))
        else:
            self.result_var.set(self.result_var.get() + button_text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
