import tkinter as tk

import elements as elem
import newbranch as n
import existingbranch as e


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
        tk.Frame(self, bg="gray", width=150, height=150).pack(expand=True)

        elem.Title(self, "Welcome!").pack(expand=True)
        elem.Text(self,
                  "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.").pack(
            expand=True)

        wrapper = tk.Frame(self, bg="red", width=300, height=100)
        wrapper.pack(expand=True)
        elem.BranchSelectionButton(wrapper, "NEW",
                                   lambda: self.start_new()).pack(side="left")
        elem.BranchSelectionButton(wrapper, "EXISTING",
                                   lambda: self.start_ex()).pack(side="right")

    def start_new(self):
        branch = elem.ViewManager(self.parent, n.create_content())
        branch.pack(fill="both", expand=True)
        self.destroy()

    def start_ex(self):
        branch = elem.ViewManager(self.parent, e.create_content())
        branch.pack(fill="both", expand=True)
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    content = Start(root).pack(fill="both", expand=True)
    root.mainloop()
