import customtkinter

class App(customtkinter.CTk): #hehehe i took this from the documentation >:]

    Todo = []
    Completed = []

    def __init__(self):

        super().__init__()



        # -- initialization -- #

        self.geometry("400x150") 
        self.title("SimplyTodo")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # -- initialization -- #


        # -- Todo frame -- #

        self.todoCheckBoxScrollableFrame = todoCheckBoxScrollableFrame(self, "ToDo")
        self.todoCheckBoxScrollableFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nwes")
        self.todoCheckBoxScrollableFrame.rowconfigure(0, weight=1)
        self.todoCheckBoxScrollableFrame.columnconfigure(0, weight=1)

        # -- Todo frame -- #


        # -- Completed frame -- #

        self.completedCheckBoxScrollableFrame = completedCheckBoxScrollableFrame(self, "Completed")
        self.completedCheckBoxScrollableFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nwes")
        self.completedCheckBoxScrollableFrame.rowconfigure(0, weight=1)
        self.completedCheckBoxScrollableFrame.columnconfigure(0, weight=1)

        # -- Completed frame -- #


        # -- EntryBox -- #

        self.entrybox = customtkinter.CTkEntry(self, placeholder_text="enter thing todo :P")
        self.entrybox.grid(row=2, column=0, padx=20, pady=20, sticky="ews")
        self.entrybox.bind("<Return>", self.addtask)

        # -- EntryBox -- #

    def addtask(self, event):
        enteredText = self.entrybox.get()
        if enteredText == (''):
            return
        self.Todo.append(enteredText)
        self.todoCheckBoxScrollableFrame.update_display(self.Todo[-1], self.Todo)
        self.entrybox.delete(0, 'end')


class todoCheckBoxScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, todoTitle):
        super().__init__(master)
        self.todoTitle = todoTitle

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text=self.todoTitle, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="we")

    def update_display(self, task, Todo):
        self.todocheckbox = customtkinter.CTkCheckBox(self, text=task)
        self.todocheckbox.grid(row=len(Todo), column=0, padx=20, pady=20, sticky="nw")


class completedCheckBoxScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, completedTitle):
        super().__init__(master)

        self.completedTitle = completedTitle
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(self, text=self.completedTitle, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="we")


#wow this was hard to make

app = App()
app.mainloop()