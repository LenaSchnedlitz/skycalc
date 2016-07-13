import tkinter as tk


class ContentWrapper(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="blue")
        self.parent = parent

        # initialize content
        breadcrumb = tk.Frame(self, bg="orange", height=30)

        header = tk.Frame(self, bg="white", height=200)
        title = tk.Label(header, text="Title")
        instruction = tk.Label(header, wraplength=700, text="At vero eos et accusam et justo duo dolores et ea rebum.")
        title.pack(expand=1)
        instruction.pack(expand=1)

        footer = tk.Frame(self, bg="white", height=200)
        previous = tk.Button(footer, text="PREVIOUS")
        next = tk.Button(footer, text="NEXT")
        previous.pack(side="left")
        next.pack(side="right")

        breadcrumb.pack(fill="x")
        header.pack(fill="x")
        footer.pack(fill="x", side="bottom")


class Start(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # initialize content
        __image = tk.Frame(self, bg="gray", width=150, height=150)
        __title = tk.Label(self, bg="white", text="Welcome!")
        __introduction = tk.Label(self, bg="white", wraplength=700,
            text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                 "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                 "magna aliquyam erat, sed diam voluptua.")
        __wrapper = tk.Frame(self, bg="red", width=300, height=100)
        __new = tk.Button(__wrapper, text="NEW")
        __existing = tk.Button(__wrapper, text="EXISTING")

        __image.pack(expand=1)
        __title.pack(expand=1)
        __introduction.pack(expand=1)
        __wrapper.pack(expand=1)
        __new.pack(side="left")
        __existing.pack(side="right")


def configure_window(self):
    """ Sets default size and minimum size; centers window """
    width = 800
    height = 600

    screenwidth = self.winfo_screenwidth()
    screenheight = self.winfo_screenheight()
    x_pos = (screenwidth - width) / 2
    y_pos = (screenheight - height) / 2

    self.minsize(width, height)
    self.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Skyrim Calculator")
    configure_window(root)
    start = ContentWrapper(root).pack(fill="both", expand=1)
    root.mainloop()
