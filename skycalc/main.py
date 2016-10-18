import tkinter as tk

import views as v


class PathNavigator:
    """Manage all views of an input path.

    Attributes:
        controller: gui controller
        content: dict of big gui components like header, footer, view,...
    """

    def __init__(self, controller, content):
        self.__controller = controller

        self.__i = 0  # number of current view/page
        self.__n = len(content)
        self.__content = content

        self.__content["Footer"].set_commands(lambda x=None: self.show_prev(),
                                              lambda x=None: self.show_next())
        self.__update_content()

    def __update_content(self):
        for element in self.__content:
            element.refresh(self.__i)

    def show_next(self):
        try:
            self.__content["Views"].collect_input(self.__i)
            if self.__i + 1 < self.__n:
                self.__i += 1
                self.__update_content()
            else:
                self.__controller.show_results()
        except Exception as e:
            for element in self.__content:
                element.show_error(e)

    def show_prev(self):
        if self.__i - 1 >= 0:
            self.__i -= 1
            self.__update_content()
        else:
            self.__controller.show_start()


class GuiController:
    """Configure the main window and swap its content.

    Attributes:
        root (Tk): window that contains this frame
    """

    def __init__(self, root):
        self.__root = root

        self.show_start()
        self.__configure_window()

    def show_path(self, recipe):
        self.__destroy_all_elements()
        v.InputViewPath(self.__root, self, recipe)

    def show_results(self):
        self.__destroy_all_elements()
        v.Results(self.__root, self, self.__data_collector)

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
    GuiController(__root)
    __root.mainloop()
