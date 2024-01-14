from typing import Any, Optional, Tuple, Union
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self._set_appearance_mode("system")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.createWidgets()
        self.placeWidgets()

    def createWidgets(self):
        self.numpadFrame = NumpadFrame(self)
        self.inputScreen = ctk.CTkEntry(self)

    def placeWidgets(self):
        self.inputScreen.grid(row=0, column=0, sticky="new", padx=10, pady=50)
        self.numpadFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    @classmethod
    def test(cls):
        print("test")

class NumpadFrame(ctk.CTkFrame):
    def __init__(self, master: Any):
        super().__init__(master=master)
        self.createWidgets()
        self.placeWidgets()

    def createWidgets(self):
        self.btn_0 = ctk.CTkButton(       self, text="0",   width=50, height=50)
        self.btn_1 = ctk.CTkButton(       self, text="1",   width=50, height=50)
        self.btn_2 = ctk.CTkButton(       self, text="2",   width=50, height=50)
        self.btn_3 = ctk.CTkButton(       self, text="3",   width=50, height=50)
        self.btn_4 = ctk.CTkButton(       self, text="4",   width=50, height=50)
        self.btn_5 = ctk.CTkButton(       self, text="5",   width=50, height=50)
        self.btn_6 = ctk.CTkButton(       self, text="6",   width=50, height=50)
        self.btn_7 = ctk.CTkButton(       self, text="7",   width=50, height=50)
        self.btn_8 = ctk.CTkButton(       self, text="8",   width=50, height=50)
        self.btn_9 = ctk.CTkButton(       self, text="9",   width=50, height=50)
        self.btn_eq = ctk.CTkButton(      self, text="=",   width=50, height=50)
        self.btn_del = ctk.CTkButton(     self, text="DEL", width=50, height=50)
        self.btn_plus = ctk.CTkButton(    self, text="+",   width=50, height=50)
        self.btn_minus = ctk.CTkButton(   self, text="-",   width=50, height=50)
        self.btn_multiply = ctk.CTkButton(self, text="*",   width=50, height=50)
        self.btn_divide = ctk.CTkButton(  self, text="/",   width=50, height=50)

    def placeWidgets(self):
        self.btn_0.grid(       row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_1.grid(       row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_2.grid(       row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_3.grid(       row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_4.grid(       row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_5.grid(       row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_6.grid(       row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_7.grid(       row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.btn_8.grid(       row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_9.grid(       row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_eq.grid(      row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.btn_del.grid(     row=3, column=2, padx=10, pady=10, sticky="nsew")
        self.btn_plus.grid(    row=0, column=3, padx=10, pady=10, sticky="nsew")
        self.btn_minus.grid(   row=1, column=3, padx=10, pady=10, sticky="nsew")
        self.btn_multiply.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
        self.btn_divide.grid(  row=3, column=3, padx=10, pady=10, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()