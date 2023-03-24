import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display widget
        self.display = tk.Entry(master, width=25, font=('Arial', 16), justify='right', bd=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        buttons = ['7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', '.', '=', '+']
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.button_click(x)
            if button == '=':
                tk.Button(master, text=button, width=6, height=2, command=command).grid(row=row, column=col, rowspan=2, padx=2, pady=2)
            else:
                tk.Button(master, text=button, width=6, height=2, command=command).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, button):
        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
