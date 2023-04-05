import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry box to display result
        self.result = tk.Entry(master, width=25, font=('Arial', 14))
        self.result.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons for digits and operators
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)

        # create button to clear result
        self.clear_button = tk.Button(master, text='Clear', width=10, command=self.clear)
        self.clear_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 14),
                           command=lambda: self.click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def click(self, text):
        if text == '=':
            try:
                result = str(eval(self.result.get()))
            except:
                result = 'Error'
            self.result.delete(0, tk.END)
            self.result.insert(0, result)
        else:
            self.result.insert(tk.END, text)

    def clear(self):
        self.result.delete(0, tk.END)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
