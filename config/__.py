import customtkinter
from views.screens.homeScreen import HomeScreen


class startApp(HomeScreen):

    def __init__(self) -> None:
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.app = customtkinter.CTk()
        self.app.title("VS  Tkinter")
        self.app._windows_set_titlebar_color("#080808")
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(0, weight=1)
        self.app.after(0, lambda: self.app.state('zoomed'))
        super().__init__()
        self.app.mainloop()
