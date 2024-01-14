from typing import Any
import customtkinter as ctk
import re

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.createWidgets()
        self.placeWidgets()

    def createWidgets(self):
        self.numpadFrame = NumpadFrame(self)
        self.inputScreen = ctk.CTkEntry(self, font=("", 22))

    def placeWidgets(self):
        self.inputScreen.grid(row=0, column=0, sticky="new", padx=10, pady=50)
        self.numpadFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

class NumpadFrame(ctk.CTkFrame):
    def __init__(self, master: Any):
        super().__init__(master=master)
        self.createWidgets()
        self.placeWidgets()

        self.index = 0

    def btn_0_command(self):
        self.master.inputScreen.insert(self.index, "0")
        self.index += 1

    def btn_1_command(self):
        self.master.inputScreen.insert(self.index, "1")
        self.index += 1

    def btn_2_command(self):
        self.master.inputScreen.insert(self.index, "2")
        self.index += 1

    def btn_3_command(self):
        self.master.inputScreen.insert(self.index, "3")
        self.index += 1

    def btn_4_command(self):
        self.master.inputScreen.insert(self.index, "4")
        self.index += 1

    def btn_5_command(self):
        self.master.inputScreen.insert(self.index, "5")
        self.index += 1

    def btn_6_command(self):
        self.master.inputScreen.insert(self.index, "6")
        self.index += 1

    def btn_7_command(self):
        self.master.inputScreen.insert(self.index, "7")
        self.index += 1

    def btn_8_command(self):
        self.master.inputScreen.insert(self.index, "8")
        self.index += 1

    def btn_9_command(self):
        self.master.inputScreen.insert(self.index, "9")
        self.index += 1

    def btn_eq_command(self):
        currentText = self.master.inputScreen.get()
        if not currentText:
            return
        if not self.isValidInput(currentText):
            return
        result = self.calculate(currentText)
        self.master.inputScreen.delete(0, ctk.END)
        self.master.inputScreen.insert(0, result)
        self.index = len(str(result))

    def btn_dot_command(self):
        self.master.inputScreen.insert(self.index, ".")
        self.index += 1

    def btn_del_command(self):
        self.master.inputScreen.delete(self.index - 1, ctk.END)
        self.index -= 1

    def btn_plus_command(self):
        currentText = self.master.inputScreen.get()
        if currentText == "":
            return
        elif len(currentText) > 1 and currentText[-1] in ["+", "-", "*", "/"]:
            newText = currentText[:-1] + "+"
        elif len(currentText) == 1 and currentText[0] in ["+", "-", "*", "/"]:
            return
        else:
            newText = currentText + "+"
        self.master.inputScreen.delete(0, ctk.END)
        self.master.inputScreen.insert(0, newText)
        self.index = len(newText)

    def btn_minus_command(self):
        currentText = self.master.inputScreen.get()
        if currentText and currentText[-1] in ["+", "-", "*", "/"]:
            newText = currentText[:-1] + "-"
        else:
            newText = currentText + "-"
        self.master.inputScreen.delete(0, ctk.END)
        self.master.inputScreen.insert(0, newText)
        self.index = len(newText)

    def btn_multiply_command(self):
        currentText = self.master.inputScreen.get()
        if currentText == "":
            return
        elif len(currentText) > 1 and currentText[-1] in ["+", "-", "*", "/"]:
            newText = currentText[:-1] + "*"
        elif len(currentText) == 1 and currentText[0] in ["+", "-", "*", "/"]:
            return
        else:
            newText = currentText + "*"
        self.master.inputScreen.delete(0, ctk.END)
        self.master.inputScreen.insert(0, newText)
        self.index = len(newText)

    def btn_divide_command(self):
        currentText = self.master.inputScreen.get()
        if currentText == "":
            return
        elif len(currentText) > 1 and currentText[-1] in ["+", "-", "*", "/"]:
            newText = currentText[:-1] + "/"
        elif len(currentText) == 1 and currentText[0] in ["+", "-", "*", "/"]:
            return
        else:
            newText = currentText + "/"
        self.master.inputScreen.delete(0, ctk.END)
        self.master.inputScreen.insert(0, newText)
        self.index = len(newText)

    def btn_clear_command(self):
        self.master.inputScreen.delete(0, ctk.END)
        self.index = 0

    def btn_open_parenthesis_command(self):
        self.master.inputScreen.insert(self.index, "(")
        self.index += 1

    def btn_close_parenthesis_command(self):
        self.master.inputScreen.insert(self.index, ")")
        self.index += 1

    def calculate(self, currentText):
        if currentText == "":
            return
        cleanedText = currentText.replace(" ", "")
        try:
            result = eval(cleanedText)
            formattedResult = f"{result:e}"
            return formattedResult
        except Exception as e:
            result = e
            return result

    def isValidInput(self, currentText):
        return bool(re.match(r'^[0-9+\-*/().e\s]*$', currentText))

    def createWidgets(self):
        self.btn_0 = ctk.CTkButton(                self, text="0",   width=60, height=60, command=self.btn_0_command)
        self.btn_1 = ctk.CTkButton(                self, text="1",   width=60, height=60, command=self.btn_1_command)
        self.btn_2 = ctk.CTkButton(                self, text="2",   width=60, height=60, command=self.btn_2_command)
        self.btn_3 = ctk.CTkButton(                self, text="3",   width=60, height=60, command=self.btn_3_command)
        self.btn_4 = ctk.CTkButton(                self, text="4",   width=60, height=60, command=self.btn_4_command)
        self.btn_5 = ctk.CTkButton(                self, text="5",   width=60, height=60, command=self.btn_5_command)
        self.btn_6 = ctk.CTkButton(                self, text="6",   width=60, height=60, command=self.btn_6_command)
        self.btn_7 = ctk.CTkButton(                self, text="7",   width=60, height=60, command=self.btn_7_command)
        self.btn_8 = ctk.CTkButton(                self, text="8",   width=60, height=60, command=self.btn_8_command)
        self.btn_9 = ctk.CTkButton(                self, text="9",   width=60, height=60, command=self.btn_9_command)
        self.btn_eq = ctk.CTkButton(               self, text="=",   width=60, height=60, command=self.btn_eq_command)
        self.btn_dot = ctk.CTkButton(              self, text=".",   width=60, height=60, command=self.btn_dot_command)
        self.btn_del = ctk.CTkButton(              self, text="DEL", width=60, height=60, command=self.btn_del_command)
        self.btn_plus = ctk.CTkButton(             self, text="+",   width=60, height=60, command=self.btn_plus_command)
        self.btn_minus = ctk.CTkButton(            self, text="-",   width=60, height=60, command=self.btn_minus_command)
        self.btn_multiply = ctk.CTkButton(         self, text="*",   width=60, height=60, command=self.btn_multiply_command)
        self.btn_divide = ctk.CTkButton(           self, text="/",   width=60, height=60, command=self.btn_divide_command)
        self.btn_clear = ctk.CTkButton(            self, text="CLS", width=60, height=60, command=self.btn_clear_command)
        self.btn_open_parenthesis = ctk.CTkButton( self, text="(",   width=60, height=60, command=self.btn_open_parenthesis_command)
        self.btn_close_parenthesis = ctk.CTkButton(self, text=")",   width=60, height=60, command=self.btn_close_parenthesis_command)

    def placeWidgets(self):
        self.btn_0.grid(                row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_1.grid(                row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_2.grid(                row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_3.grid(                row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_4.grid(                row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_5.grid(                row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_6.grid(                row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_7.grid(                row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_8.grid(                row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_9.grid(                row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_eq.grid(               row=3, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_dot.grid(              row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_del.grid(              row=0, column=4, padx=10, pady=10, sticky="nsew")
        self.btn_plus.grid(             row=0, column=3, padx=10, pady=10, sticky="nsew")
        self.btn_minus.grid(            row=1, column=3, padx=10, pady=10, sticky="nsew")
        self.btn_multiply.grid(         row=2, column=3, padx=10, pady=10, sticky="nsew")
        self.btn_divide.grid(           row=3, column=3, padx=10, pady=10, sticky="nsew")
        self.btn_clear.grid(            row=1, column=4, padx=10, pady=10, sticky="nsew")
        self.btn_open_parenthesis.grid( row=2, column=4, padx=10, pady=10, sticky="nsew")
        self.btn_close_parenthesis.grid(row=3, column=4, padx=10, pady=10, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()