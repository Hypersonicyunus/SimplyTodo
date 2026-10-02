import customtkinter

class App(customtkinter.CTk): #hehehe i took this from the documentation >:]

    def __init__(self):

        super().__init__()

        NewTodo = []
        Completed = []

        # -- initialization -- #

        self.geometry("400x150") 
        self.title("SimplyTodo")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # -- initialization -- #


        self.checkBoxFrame = checkBoxFrame(self, self.addtask)
        self.checkBoxFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

class checkBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master, addtask):
        super().__init__(master)

        def addtask(self, enteredText):
            enteredText = self.entrybox.get()
            if enteredText == (''):
                return
            self.NewTodo.append(enteredText)
            print(self.NewTodo)
            self.update_display()
            self.entrybox.delete(0, 'end')
            self.NewTodo.clear()

        def update_display(self):
            for item in self.NewTodo:
                self.todocheckbox = customtkinter.CTkCheckBox(self, text=self.NewTodo)
                self.todocheckbox.grid(row=+1, column=0, rowspan=1, padx=20, pady=20, sticky="nw")

        #Entrybox code
        self.entrybox = customtkinter.CTkEntry(self, placeholder_text="enter thing todo :P")
        self.entrybox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.entrybox.bind("<Return>", addtask)




app = App()
app.mainloop()