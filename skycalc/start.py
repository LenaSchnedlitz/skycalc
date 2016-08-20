import tkinter as tk

import elements as elem


class Start(tk.Frame):
    """Welcome screen

    Choose between two buttons, 'NEW' and 'EXISTING'
    Attributes:
        parent (Tk): window that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=elem.DARK_BLUE)
        self.__parent = parent

        # image placeholder
        img = tk.PhotoImage(file="res/skyrim.gif")
        label = tk.Label(self, image=img, bg=self.cget("bg"))
        label.image = img
        label.pack()

        elem.Title(self, "Welcome!", elem.BG).pack()
        elem.Text(self,
                  "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                  "sed diam nonumy eirmod tempor invidunt ut labore et "
                  "dolore magna aliquyam erat, sed diam voluptua.",
                  elem.WHITE).pack()

        button_container = tk.Frame(self, bg=self.cget("bg"))
        button_container.pack(pady=30)
        elem.BranchSelectionButton(button_container, "NEW",
                                   lambda: self.start_new()).pack(side="left",
                                                                  padx=5)
        elem.BranchSelectionButton(button_container, "EXISTING",
                                   lambda: self.start_ex()).pack(side="right",
                                                                 padx=5)

    def start_new(self):
        import newbranch as n
        elem.ViewManager(self.__parent, n.build_content()).pack(fill="both",
                                                                expand=True)
        self.destroy()

    def start_ex(self):
        import existingbranch as e
        elem.ViewManager(self.__parent, e.build_content()).pack(fill="both",
                                                                expand=True)
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    content = Start(root).pack(fill="both", expand=True)
    root.mainloop()
