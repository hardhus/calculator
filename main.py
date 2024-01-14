from typing import Any, Optional, Tuple, Union
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self._set_appearance_mode("system")
        self.grid_columnconfigure(0, weight=1)

        self.numpadFrame = NumpadFrame(self)
        self.numpadFrame.grid(row=0, column=0, sticky="nsew")

class NumpadFrame(ctk.CTkFrame):
    def __init__(self, master: Any):
        super().__init__(master=master)

    def createWidgets(self):
        self.btn_0 = ctk.CTkButton(self, text="0")
    
    def placeWidgets(self):
        self.btn_0.grid(row=0, column=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()