import customtkinter
app = customtkinter.CTk()
# app.winfo_screenwidth()
# header
defaultBg = "#080808"
lighterBg = "#111113"
fullWidth = app.winfo_screenwidth()
fullHeight = app.winfo_screenheight()

# col for screen percentage


def col(type, percentOfScreenNeeded):
    if type == "w":
        percent = (fullWidth * percentOfScreenNeeded) / 100
        return percent

    elif type == "h":
        percent = (fullHeight * percentOfScreenNeeded) / 100
        return percent
app.destroy()