import customtkinter


class App(customtkinter.CTk):

    Todo = []
    Completed = []

    def __init__(self):

        super().__init__()

        self.geometry("700x400")
        self.title("SimplyTodo")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # -- Todo frame -- #

        self.todoCheckBoxScrollableFrame = todoCheckBoxScrollableFrame(
            self,
            "ToDo"
        )

        self.todoCheckBoxScrollableFrame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nwes"
        )

        # -- Completed frame -- #

        self.completedCheckBoxScrollableFrame = completedCheckBoxScrollableFrame(
            self,
            "Completed"
        )

        self.completedCheckBoxScrollableFrame.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nwes"
        )

        # -- EntryBox -- #

        self.entrybox = customtkinter.CTkEntry(
            self,
            placeholder_text="enter thing todo :P"
        )

        self.entrybox.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
            sticky="ews"
        )

        self.entrybox.bind("<Return>", self.addtask)

    def addtask(self, event):

        enteredText = self.entrybox.get()

        if enteredText == "":
            return

        self.Todo.append(enteredText)

        print(self.Todo)

        self.todoCheckBoxScrollableFrame.update_display(
            self.Todo[-1],
            len(self.Todo)
        )

        self.entrybox.delete(0, "end")


class todoCheckBoxScrollableFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, todoTitle):

        super().__init__(master)

        self.todoTitle = todoTitle

        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(
            self,
            text=self.todoTitle,
            fg_color="gray30",
            corner_radius=6
        )

        self.title.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 0),
            sticky="we"
        )

    def update_display(self, task, row):

        checkbox = customtkinter.CTkCheckBox(
            self,
            text=task,
            command=lambda: self.moveToCompleted(checkbox)
        )

        checkbox.grid(
            row=row,
            column=0,
            padx=20,
            pady=20,
            sticky="nw"
        )

    def moveToCompleted(self, checkbox):

        print("moveToCompleted Ran")

        if checkbox.get() == 1:

            grid_info = checkbox.grid_info()

            print(grid_info)

            print("Row:", grid_info["row"])


class completedCheckBoxScrollableFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, completedTitle):

        super().__init__(master)

        self.completedTitle = completedTitle

        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(
            self,
            text=self.completedTitle,
            fg_color="gray30",
            corner_radius=6
        )

        self.title.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="we"
        )


app = App()
app.mainloop()
