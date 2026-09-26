import customtkinter

class App(customtkinter.CTk):

    Todo = []
    Completed = []

    def addtask(self, test):
            test = self.entrybox.get()
            print(test)

    def __init__(self):
        super().__init__()
        self.geometry("400x150") #hehehe i took this from the documentation >:]
        self.title("SimplyTodo")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.todocheckbox = customtkinter.CTkCheckBox(self, text="test")
        self.todocheckbox.grid(row=0)

        #Entrybox code
        self.entrybox = customtkinter.CTkEntry(self, placeholder_text="enter thing todo :P")
        self.entrybox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.entrybox.bind("<Return>", self.addtask)

app = App()
app.mainloop()