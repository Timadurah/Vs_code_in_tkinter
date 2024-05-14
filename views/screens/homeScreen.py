import customtkinter
from static.styles.style import *


class HomeScreen():
    def __init__(self):
        # Lunch the method here.
        
        self.frame = customtkinter.CTkFrame(self.app)
        self.frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.header()
        self.main()
        self.footer()

    def header(self):
        self.headerFrame = customtkinter.CTkFrame(
            self.frame, fg_color=defaultBg, bg_color=defaultBg, height=col("h", 10), corner_radius=0, width=col("w", 100))
        self.headerFrame.grid(row=0, column=0,
                              sticky="ew", columnspan=2)


    def main(self):
        self.headerFrame = customtkinter.CTkFrame(
            self.frame, fg_color=lighterBg, bg_color=lighterBg, corner_radius=0, width=col("w", 100), height=col("h", 76))
        self.headerFrame.grid(row=1, column=0,
                              sticky="ew", columnspan=2)
         # side icon frame
        self.editorSideIcons = customtkinter.CTkFrame(
            self.headerFrame, fg_color=defaultBg, bg_color=defaultBg, corner_radius=0, width=col("w", 5), height=col("h", 76))
        self.editorSideIcons.grid(
            row=0, column=0, sticky="ew", columnspan=1, pady=1, padx=1)

        # outline frame
        self.editorSideOutline = customtkinter.CTkFrame(
            self.headerFrame, fg_color=defaultBg, bg_color=defaultBg, corner_radius=0, width=col("w", 25), height=col("h", 76))
        self.editorSideOutline.grid(
            row=0, column=1, sticky="ew", columnspan=1, padx=1, pady=1)

        # Text editor frame
        self.editorTextbox = customtkinter.CTkFrame(
            self.headerFrame, fg_color=lighterBg, bg_color=lighterBg, corner_radius=0, width=col("w", 70), height=col("h", 76))
        self.editorTextbox.grid(row=0, column=2, sticky="ew", columnspan=2)

        # TextEditor strcuture
        # header
        self.editorheader = customtkinter.CTkFrame(
            self.editorTextbox, fg_color=defaultBg, bg_color=defaultBg, corner_radius=0, width=col("w", 70), height=col("h", 3.5))
        self.editorheader.grid(row=0, column=0, sticky="ew",
                               columnspan=1, pady=0, padx=0)
        self.editorheaderIcon = customtkinter.CTkFrame(
            self.editorheader, fg_color=lighterBg, bg_color=lighterBg, corner_radius=0, width=col("w", 15), height=col("h", 3.5))
        self.editorheaderIcon.grid(
            row=0, column=0, sticky="ew", columnspan=1, pady=0, padx=0)
        self.editorheaderIconTwo = customtkinter.CTkFrame(
            self.editorheader, fg_color=defaultBg, bg_color=defaultBg, corner_radius=0, width=col("w", 50), height=col("h", 3.5))
        self.editorheaderIconTwo.grid(
            row=0, column=1, sticky="ew", columnspan=1, padx=1, pady=0)
        self.editorheaderSideIcon = customtkinter.CTkFrame(
            self.editorheader, fg_color=defaultBg, bg_color=defaultBg, corner_radius=0, width=col("w", 5), height=col("h", 3.5))
        self.editorheaderSideIcon.grid(
            row=0, column=2, sticky="ew", columnspan=2, pady=0, padx=0)

        # main
        self.editorMain = customtkinter.CTkTextbox(
            self.editorTextbox, fg_color=lighterBg, bg_color=lighterBg, corner_radius=0, width=col("w", 70), height=col("h", 53.2), font=("monospace", 20), text_color="brown")
        self.editorMain.grid(row=1, column=0, sticky="ew",
                             columnspan=2, padx=10)
        # Metrics
        self.editorMetrics = customtkinter.CTkFrame(
            self.editorTextbox, fg_color=defaultBg, bg_color=defaultBg, corner_radius=0, width=col("w", 70), height=col("h", 19))
        self.editorMetrics.grid(row=2, column=0, sticky="ew", columnspan=1)



# footer

    def footer(self):
        self.headerFrame = customtkinter.CTkFrame(
            self.frame, fg_color=defaultBg, bg_color=defaultBg, corner_radius=0,  width=col("w", 100), height=col("h", 12))
        self.headerFrame.grid(row=2, column=0,
                              sticky="ew", columnspan=2)
