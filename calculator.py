
import tkinter as tk

Digit_Font = ("Arial", 24, "bold")
Default_Font = ("Arial", 20)
L_Font = ("Arial", 40, "bold")
S_Font = ("Arial", 16)


White1 = "#fcf4de"
Gray = "#F5F5F5"
LABEL_COLOR = "#f71111"
WHITE = "#FFFFFF"
Blue = "#b5f794"



class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator by Sahadat")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.display_frame()

        self.total_label, self.label = self.display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.button_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.digit_buttons()
        self.operator_buttons()
        self.special_button()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append(operator))

    def special_button(self):
        self.clear_button()
        self.equal_button()
        self.sqr_button()
        self.sqrt_button()



    def display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=Gray)
        frame.pack(expand=True, fill="both")
        return frame

    def display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=Gray,
                               fg=LABEL_COLOR, padx=24, font=S_Font)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=Gray,
                         fg=LABEL_COLOR, padx=24, font=L_Font)
        label.pack(expand=True, fill='both')

        return total_label, label


    def digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=Digit_Font,
                               borderwidth=0, command=lambda x=digit: self.expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()


    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=White1, fg=LABEL_COLOR, font=Default_Font,
                               borderwidth=0, command=lambda x=operator: self.append(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=White1, fg=LABEL_COLOR, font=Default_Font,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def sqr_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=White1, fg=LABEL_COLOR, font=Default_Font,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=White1, fg=LABEL_COLOR, font=Default_Font,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def equal_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=Blue, fg=LABEL_COLOR, font=Default_Font,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()


    def button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()