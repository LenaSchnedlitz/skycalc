import tkinter as tk
import widgets as w


class Results(tk.Frame):
    """Display calculated results.

    Three tabs + option to export.
    Attributes:
        parent (Tk): window that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        w.Title(self, "Results").pack()
        sel_container = tk.Frame(self)
        sel_container.pack(expand=1)
        w.TabButton(sel_container, line="a tab").pack(side="left")
        w.TabButton(sel_container, line="b tab").pack(side="left")
        w.TabButton(sel_container, line="c tab").pack(side="left")
        res_container = tk.Frame(self)
        res_container.pack(expand=1)
        w.Headline(res_container, line="Variant").pack()
        w.Text(res_container, wrap=700,
               line="Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.").pack()


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
    content = Results(root).pack(fill="both", expand=1)
    root.mainloop()
