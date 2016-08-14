import tkinter as tk
import elements as elem


class Start(tk.Frame):
    """Welcome Screen

    Choose between two buttons, 'NEW' and 'EXISTING'
    Attributes:
        parent (Tk): window that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # image placeholder
        tk.Frame(self, bg="gray", width=150, height=150).pack(expand=1)

        elem.Title(self, "Welcome!").pack(expand=1)
        elem.Text(self,
                  "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.").pack(
            expand=1)

        wrapper = tk.Frame(self, bg="red", width=300, height=100)
        wrapper.pack(expand=1)
        elem.BranchSelectionButton(wrapper, "NEW").pack(side="left")
        elem.BranchSelectionButton(wrapper, "EXISTING").pack(side="right")


def configure_window(self):
    """Set window title, size, minsize and position"""
    # title
    self.title("Skyrim Calculator")

    # size
    width = 800
    height = 600
    self.minsize(width, height)

    # position
    x_pos = (self.winfo_screenwidth() - width) / 2
    y_pos = (self.winfo_screenheight() - height) / 2
    self.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))


if __name__ == "__main__":
    root = tk.Tk()
    configure_window(root)
    content = Start(root).pack(fill="both", expand=1)
    root.mainloop()
