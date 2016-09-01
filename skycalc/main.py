import tkinter as tk

import windowelements as elem
import calculator as calc


class ViewManager:
    """Contain and manage all views of a branch.

    Attributes:
        root (Tk): window that contains this frame
        content: tuple with a dictionary for each view
    """

    def __init__(self, root, content):
        self.__root = root
        self.__collector = calc.InputValidator()
        self.__n = len(content)
        self.__i = 0  # number of current view/page

        self.__elements = self.build_window_elements(content)

        self.update_content()

    def build_window_elements(self, content):
        breadcrumbs = elem.Breadcrumbs(self.__root, len(content))
        header = elem.Header(self.__root,
                             [v["Title"] for v in content],
                             [v["Instruction"] for v in content])
        view_container = elem.ViewContainer(self.__root,
                                            [v["View"] for v in content],
                                            self.__collector)
        footer = elem.Footer(self.__root, self, len(content))
        return breadcrumbs, header, view_container, footer

    def update_content(self):
        for element in self.__elements:
            element.refresh(self.__i)

    def destroy_content(self):
        for element in self.__elements:
            element.destroy()

    def show_next(self):
        try:
            self.__elements[2].use_input(self.__i)
            if self.__i + 1 < self.__n:
                self.__i += 1
                self.update_content()
            else:
                elem.Results(self.__root,
                             calc.Calculator(self.__collector)).pack(
                    fill="both", expand=True)
                self.destroy_content()
        except Exception as e:
            for element in self.__elements:
                element.show_error(e)

    def show_prev(self):
        if self.__i - 1 >= 0:
            self.__i -= 1
            self.update_content()
        else:
            elem.Start(self.__root).pack(fill="both", expand=True)
            self.destroy_content()


def configure_window(self):
    """Set window title, size, minsize and position"""

    self.iconbitmap("res/Skyrim.ico")

    self.title("Skyrim Calculator")

    width = 800
    height = 600
    self.minsize(width, height)

    x_pos = (self.winfo_screenwidth() - width) / 2
    y_pos = (self.winfo_screenheight() - height) / 2
    self.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))


if __name__ == "__main__":
    root = tk.Tk()
    configure_window(root)
    content = elem.Start(root)
    root.mainloop()
