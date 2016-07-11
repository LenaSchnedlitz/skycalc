from tkinter import *


class StartFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.start()

    def start(self):
        self.parent.title("Skyrim Calculator")
        self.pack(fill="both", expand=1)
        self.center_window()

        placeholder_text = Label(self, text="image missing")
        placeholder_text.grid(row=0, columnspan=2)
        instruction = Label(self, bg="white", text="select your option:")
        instruction.grid(row=1, columnspan=2)
        new = Button(self, text="new")
        new.grid(row=2, column=0)
        existing = Button(self, text="existing")
        existing.grid(row=2, column=1)

    def center_window(self):
        width = 800
        height = 600

        screenwidth = self.parent.winfo_screenwidth()
        screenheight = self.parent.winfo_screenheight()

        x_pos = (screenwidth - width) / 2
        y_pos = (screenheight - height) / 2

        self.parent.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))


def main():
    """ open application window with start frame """
    root = Tk()
    window = StartFrame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
