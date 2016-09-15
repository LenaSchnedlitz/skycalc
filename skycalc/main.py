import tkinter as tk

import views as v


class ViewNavigator:
    """Manage all views of a branch.

    Attributes:
        root (Tk): window that contains this frame
        content: tuple with a dictionary for each view
    """

    def __init__(self, root, content, manager):
        self.__root = root
        self.__manager = manager

        self.__n = len(content)
        self.__i = 0  # number of current view/page
        self.__elements = self.__build_window_elements(content)

        self.__update_content()

    def __build_window_elements(self, content):
        header = v.Header(self.__root,
                          [entry["Title"] for entry in content])
        breadcrumbs = v.Breadcrumbs(self.__root, len(content))
        view_container = v.ViewContainer(self.__root,
                                         [entry["View"] for entry in content])
        footer = v.Footer(self.__root, self, len(content),
                          [entry["Instruction"] for entry in content])
        return breadcrumbs, header, view_container, footer

    def __update_content(self):
        for element in self.__elements:
            element.refresh(self.__i)

    def show_next(self):
        try:
            self.__elements[2].use_input(self.__i)
            if self.__i + 1 < self.__n:
                self.__i += 1
                self.__update_content()
            else:
                self.__manager.show_results()
        except Exception as e:
            for element in self.__elements:
                element.show_error(e)

    def show_prev(self):
        if self.__i - 1 >= 0:
            self.__i -= 1
            self.__update_content()
        else:
            self.__manager.show_start()


class GuiManager:
    def __init__(self, root):
        self.__root = root

        self.show_start()
        self.__configure_window()

    def show_existing_path(self):
        self.__destroy_all_elements()
        ViewNavigator(self.__root, v.Recipe.EXISTING_CHAR, self)

    def show_new_path(self):
        self.__destroy_all_elements()
        ViewNavigator(self.__root, v.Recipe.NEW_CHAR, self)

    def show_results(self):
        self.__destroy_all_elements()

    def show_start(self):
        self.__destroy_all_elements()
        v.Start(self.__root, self)

    def __configure_window(self):
        self.__root.iconbitmap("res/Skyrim.ico")
        self.__root.title("Skyrim Calculator")

        width = 800
        height = 600
        self.__root.minsize(width, height)

        # place in screen center
        x_pos = (self.__root.winfo_screenwidth() - width) / 2
        y_pos = (self.__root.winfo_screenheight() - height) / 2
        self.__root.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))

    def __destroy_all_elements(self):
        for child in self.__root.winfo_children():
            child.destroy()


if __name__ == "__main__":
    __root = tk.Tk()
    GuiManager(__root)
    __root.mainloop()
