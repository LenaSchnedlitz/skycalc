import tkinter as tk

import views as v


# TODO: make more reusable
class Navigator:
    """Manage all views of an input getter.

    Attributes:
        controller: gui controller
    """

    def __init__(self, controller):
        self.__controller = controller

        self.__i = 0  # number of current view/page
        self.__n = 0  # must be set by set_content
        self.__content = None  # must be set by set_content

    def set_content(self, content):
        self.__n = len(content)
        self.__content = content
        self.__content["Footer"].set_commands(lambda x=None: self.show_prev(),
                                              lambda x=None: self.show_next())
        self.__update_content()

    def show_next(self):
        try:
            self.__content["Views"].collect_input(self.__i)
            if self.__i + 1 < self.__n:
                self.__i += 1
                self.__update_content()
            else:
                self.__controller.show_results()
        except Exception as e:
            for element in self.__content.values():
                element.show_error(e)

    def show_prev(self):
        if self.__i - 1 >= 0:
            self.__i -= 1
            self.__update_content()
        else:
            self.__controller.show_start()

    def __update_content(self):
        for element in self.__content.values():
            element.refresh(self.__i)


class GuiController:
    """Configure the main window and swap its content.

    Attributes:
        root (Tk): main window
    """

    def __init__(self, root):
        self.__root = root
        self.__collector = None

        self.show_start()
        self.__configure_window()

    def show_input_forms(self, recipe):
        self.__destroy_all_elements()
        self.__reset_collector()
        v.InputGetter(self.__root, recipe, Navigator(self), self.__collector)

    def show_results(self):
        self.__destroy_all_elements()
        v.Results(self.__root, self.__collector,
                  lambda x=None: self.show_start())

    def show_start(self):
        self.__destroy_all_elements()
        v.Start(self.__root, self)

    def __configure_window(self):
        self.__root.iconbitmap("res/arrow.ico")
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

    def __reset_collector(self):
        import inputparser as p
        self.__collector = p.InputCollector()


if __name__ == "__main__":
    __root = tk.Tk()
    GuiController(__root)
    __root.mainloop()
