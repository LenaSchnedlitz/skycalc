"""Contains templates for most GUI components."""

import tkinter as tk


# different kinds of text and labels

# TODO use or remove
class Title(tk.Label):
    """Title - biggest text.

    Attributes:
        parent (Frame): frame that contains this title
        text_ (str): displayed text
        color_ (str): text color
    """

    def __init__(self, parent, text_, color_):
        tk.Label.__init__(self, parent, text=text_, fg=color_,
                          bg=parent.cget("bg"),
                          font="-size 34 -weight bold")


class BreadcrumbLabel(tk.Label):
    """Display title of current stage.

    Attributes:
        parent (Frame): parent frame
        text (str): label text/image file name
        i (int): position/index
    """

    def __init__(self, parent, text, i):
        tk.Label.__init__(self, parent, bg=parent.cget("bg"), borderwidth=0)
        self.__i = i  # index/id

        self.__empty = ImageImporter.load("bread/labels/empty")
        self.__filled = ImageImporter.load("bread/labels/" + text)

    def refresh(self, n=0):
        if self.__i == n:
            self.config(image=self.__filled)
        else:
            self.config(image=self.__empty)


class Message(tk.Label):
    """Standard message with 2 modes (normal and error).

    Attributes:
        parent (Frame): frame that contains this text
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent,
                          bg=parent.cget("bg"),
                          font=("Helvetica", 10),
                          wraplength=500)
        self.show_normal(text_)

    def show_error(self, new_text):
        self.config(text=new_text, fg=Colors.ERROR)

    def show_normal(self, new_text):
        self.config(text=new_text, fg=Colors.DARK)


# classic buttons

# TODO Button functionality
class BreadcrumbButton(tk.Label):
    """Breadcrumb button displaying status of a step.

    Attributes:
        parent (Frame): frame that contains this image
        i (int): position/index
    """

    def __init__(self, parent, i):
        tk.Label.__init__(self, parent, bg=parent.cget("bg"), borderwidth=0)
        self.__i = i  # index/id

        self.__old = ImageImporter.load("bread/OLD")
        self.__now = ImageImporter.load("bread/NOW")
        self.__new = ImageImporter.load("bread/NEW")

        self.refresh()

    def refresh(self, n=0):
        if self.__i < n:
            self.config(image=self.__old)
        elif self.__i == n:
            self.config(image=self.__now)
        else:
            self.config(image=self.__new)


class NavButton(tk.Button):
    """Standard layout for 'previous'- or 'next'-buttons.

    Attributes:
        parent (Frame): frame that contains this button
        label (str): default text
        alt_label (str): optional, alternative text
    """

    def __init__(self, parent, label, alt_label=None):
        tk.Button.__init__(self, parent,
                           activebackground=parent.cget("bg"),
                           bg=parent.cget("bg"),
                           borderwidth=0,
                           cursor="hand2",
                           relief="flat")

        self.__image = ImageImporter.load("nav/" + label)

        self.__alt_image = None
        if alt_label is not None:
            self.__alt_image = ImageImporter.load("nav/" + alt_label)

        self.show_default()

    def show_default(self):
        self.config(image=self.__image)

    def set_command(self, command_):
        self.config(command=command_)
        self.bind("<Return>", command_)

    def show_alternative(self):
        if self.__alt_image is not None:
            self.config(image=self.__alt_image)


class StartButton(tk.Button):
    """Default button layout, mainly used in 'Start'.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'NEW' or 'EXISTING'
        command_: button command
    """

    def __init__(self, parent, text_, command_):
        tk.Button.__init__(self, parent, text=text_, command=command_,
                           activebackground=Colors.MEDIUM,
                           activeforeground=Colors.LIGHT,
                           bg=Colors.LIGHT,
                           borderwidth=0,
                           cursor="hand2",
                           fg=Colors.WHITE,
                           font="-size 13",
                           pady=7,
                           relief="flat",
                           width=12
                           )
        self.bind("<Return>", command_)


class SortButton(tk.Button):
    """'Toggle button' used for sorting method selection.

    Attributes:
        parent (Frame): container frame
        text_ (str): button text, usually 'alphabetically', 'by category', ...
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_,
                           activebackground=parent.cget("bg"),
                           activeforeground=Colors.DARK,
                           bg=parent.cget("bg"),
                           borderwidth=0,
                           cursor="hand2",
                           fg=Colors.DARK,
                           font="-size 10",
                           padx=14,
                           relief="flat"
                           )
        self.bind("<Return>", lambda x: parent.sort())
        self.config(command=lambda: parent.sort())

    def change_text(self, new_text):
        self.config(text=new_text)


# TODO use or remove
class TabButton(tk.Button):
    """Tab index button.

    For results view
    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): displayed text
        tab (Frame): frame that will be shown when the button is clicked
    """

    def __init__(self, parent, text_, tab):
        tk.Button.__init__(self, parent, text=text_)
        self.__parent = parent
        self.config(command=lambda: tab.tkraise())


# getting user input

class Selectable(tk.Button):
    """Selectable text, can be toggled (selected - deselected).

    Attributes:
        parent (Frame): container frame
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_,
                           activebackground=parent.cget("bg"),
                           activeforeground=Colors.MEDIUM,
                           bg=parent.cget("bg"),
                           borderwidth=0,
                           compound="center",
                           cursor="hand2",
                           font="-size 11",
                           relief="flat"
                           )
        self.__text = text_
        self.__normal_img = ImageImporter.load("selectable/empty")
        self.__selected_img = ImageImporter.load("selectable/SELECTED")

        self.config(command=lambda: self.select())
        self.bind("<Return>", lambda x: self.select())

        self.mark_unselected()

    def get_label(self):
        return self.__text

    def mark_selected(self):
        self.config(image=self.__selected_img, fg=Colors.LIGHT)

    def mark_unselected(self):
        self.config(image=self.__normal_img, fg=Colors.WHITE)

    def select(self):
        self.mark_selected()


class MultiSelectable(Selectable):
    """Selectable; more than one element can be selected.

    Attributes:
        parent (Frame): container frame
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        Selectable.__init__(self, parent, text_)
        self.__selected = False

    def is_selected(self):
        return self.__selected

    def select(self):
        if self.__selected:
            self.mark_unselected()
        else:
            self.mark_selected()
        self.__selected = not self.__selected


# TODO: rename object_
class Option(Selectable):
    """Selectable; only one element can be selected at a time.

    Attributes:
        parent (Frame): container frame
        text_ (str): displayed text
        object_: object that offers this option
    """

    def __init__(self, parent, text_, object_):
        Selectable.__init__(self, parent, text_)
        self.__object = object_

    def select(self):
        self.__object.select(self.get_label())


class BigField(tk.Frame):
    """Big input field with text.

    Perfect for character level input.
    Attributes:
        parent (Frame): container frame
        name_ (str): bg image file name
    """

    def __init__(self, parent, name_):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))

        self.__selected_bg = ImageImporter.load("bigfield/SELECTED_" + name_)
        self.__error_bg = ImageImporter.load("bigfield/ERROR_" + name_)

        self.__background_label = tk.Label(self, bg=self.cget("bg"))
        self.__background_label.grid(row=0, column=0)

        self.__entry = tk.Entry(self,
                                bg=Colors.SHADOW,
                                borderwidth=0,
                                fg=Colors.TEXT,
                                font="-size 38",
                                insertwidth=2,
                                justify="center",
                                relief="flat",
                                width=3
                                )
        self.__entry.grid(row=0, column=0)

        self.mark_valid()

    def get_input(self):
        return self.__entry.get()

    def mark_invalid(self):
        self.__background_label.config(image=self.__error_bg)
        self.__entry.config(insertbackground=Colors.ERROR)
        self.set_focus()

    def mark_valid(self):
        self.__background_label.config(image=self.__selected_bg)
        self.__entry.config(insertbackground=Colors.MEDIUM)

    def set_focus(self):
        self.__entry.focus_set()


class SmallField(tk.Frame):
    """Small input field with text.

    Made for skill level input.
    Attributes:
        parent (Frame): container frame
        name_ (str): field name
    """

    def __init__(self, parent, name_):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))

        self.__name = name_
        file_name = name_.replace(" ", "_")  # no whitespace in file names

        self.__selected_bg = ImageImporter.load("smallfield/" + file_name)
        self.__error_bg = ImageImporter.load("smallfield/ERROR_" + file_name)

        self.__background_label = tk.Label(self, bg=self.cget("bg"))
        self.__background_label.grid(row=0, column=0)

        self.__entry = tk.Entry(self,
                                bg=Colors.SHADOW,
                                borderwidth=0,
                                fg=Colors.TEXT,
                                font="-size 24",
                                insertwidth=2,
                                justify="center",
                                relief="flat",
                                width=3
                                )
        self.__entry.grid(row=0, column=0, pady=24, sticky="s")

        self.mark_valid()

    def get_input(self):
        return self.__entry.get()

    def get_label(self):
        return self.__name

    def mark_invalid(self):
        self.__background_label.config(image=self.__error_bg)
        self.__entry.config(insertbackground=Colors.ERROR)
        self.set_focus()

    def mark_valid(self):
        self.__background_label.config(image=self.__selected_bg)
        self.__entry.config(insertbackground=Colors.MEDIUM)

    def set_focus(self):
        self.__entry.focus_set()


# other

class Colors:
    """Some predefined colors."""
    BG = "#1A1816"
    TEXT = "#C0BFBF"
    ERROR = "#F22613"

    WHITE = "#EFEFEF"
    SHADOW = "#12110F"
    BLACK = "#080706"

    LIGHT = "#D0B180"
    MEDIUM = "#937E62"
    DARK = "#584D45"
    DARKER = "#2F2924"


class Image(tk.Label):
    """Display a .png-image imported by the ImageImporter.

    Attributes:
        parent (Frame): parent frame
        name_ (str): image file name
    """

    def __init__(self, parent, name_):
        tk.Label.__init__(self, parent, bg=parent.cget("bg"), borderwidth=0)
        self.__image = ImageImporter.load(name_)
        self.config(image=self.__image)


class ImageImporter:
    """Import a .png-image from /res."""

    @staticmethod
    def load(image):
        from PIL import Image, ImageTk
        return ImageTk.PhotoImage(Image.open("res/" + image + ".png"))


if __name__ == "__main__":
    import sys
    import inspect

    print(__doc__, "\n")
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj.__name__, "\n",
                  obj.__doc__, "\n\n")
