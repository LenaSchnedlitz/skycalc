"""Templates for most GUI components."""

import tkinter as tk


# different kinds of text

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


class Headline(tk.Label):
    """Headline - smaller than title.

    Attributes:
        parent (Frame): frame that contains the headline
        text_ (str): displayed headline text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_,
                          bg=parent.cget("bg"),
                          fg=Colors.DARK,
                          font="-size 18 -weight bold",
                          pady=20)


class ViewName(tk.Label):
    """View name text.

    Attributes:
        parent (Frame): frame that contains the title, usually a header
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, pady=0, anchor="sw",
                          font="-size 22 -weight bold",
                          bg=parent.cget("bg"), fg=Colors.DARK)
        self.__parent = parent


class Instruction(tk.Label):
    """Instruction text.

    Attributes:
        parent (Frame): frame that contains the instruction, usually a header
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_,
                          anchor="nw",
                          bg=parent.cget("bg"),
                          fg=Colors.MEDIUM,
                          font="-size 11",
                          justify="left",
                          pady=0,
                          wraplength=700)


class Text(tk.Label):
    """Text.

    Attributes:
        parent (Frame): frame that contains this text
        text_ (str): displayed text
        color_ (str): text color
    """

    def __init__(self, parent, text_, color_):
        tk.Label.__init__(self, parent, text=text_, fg=color_,
                          bg=parent.cget("bg"),
                          font=("Helvetica", 10),
                          wraplength=700)


class ErrorMessage(tk.Label):
    """Error Message.

    Attributes:
        parent (Frame): frame that contains this text
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_,
                          bg=parent.cget("bg"),
                          fg=Colors.ERROR,
                          font=("Helvetica", 10),
                          wraplength=500)


# classic buttons

class BranchSelectionButton(tk.Button):
    """Layout for 'NEW'- and 'EXISTING'-button.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'NEW' or 'EXISTING'
        command_: button command
    """

    def __init__(self, parent, text_, command_):
        tk.Button.__init__(self, parent, text=text_, command=command_,
                           width=12, borderwidth=0, pady=7,
                           cursor="hand2", relief="flat",
                           font="-size 13",
                           bg=Colors.LIGHT,
                           activebackground=Colors.MEDIUM,
                           fg=Colors.WHITE, activeforeground=Colors.LIGHT)
        self.__parent = parent


class BreadcrumbButton(tk.Label):
    def __init__(self, parent, i):
        tk.Label.__init__(self, parent, bg=parent.cget("bg"))
        self.__i = i

        self.__empty = ImageImporter.load("bread_empty")
        self.__filled = ImageImporter.load("bread_" + str(i))

        self.refresh()

    def refresh(self, n=0):
        if self.__i <= n + 1:  # 'n + 1' because count starts with 1
            self.config(image=self.__filled)
        else:
            self.config(image=self.__empty)


class NavButton(tk.Button):
    """Standard layout for 'previous'- & 'next'-button.

    Attributes:
        parent (Frame): frame that contains this button
    """

    def __init__(self, parent):
        tk.Button.__init__(self, parent,
                           activebackground=parent.cget("bg"),
                           bg=parent.cget("bg"),
                           borderwidth=0,
                           cursor="hand2",
                           relief="flat")
        self.__back_img = ImageImporter.load("nav_BACK")
        self.__next_img = ImageImporter.load("nav_NEXT")
        self.__results_img = ImageImporter.load("nav_RESULTS")

        self.show_next_text()

    def show_back_text(self):
        self.config(image=self.__back_img)

    def show_next_text(self):
        self.config(image=self.__next_img)

    def show_results_text(self):
        self.config(image=self.__results_img)


class SortButton(tk.Button):
    """'Toggle button', used for sorting method selection.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'alphabetically' or 'by category'
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_,
                           activebackground=parent.cget("bg"),
                           activeforeground=Colors.DARK,
                           bg=parent.cget("bg"),
                           borderwidth=0,
                           cursor="hand2",
                           fg=Colors.MEDIUM,
                           font="-size 10",
                           padx=14,
                           relief="flat")
        self.bind("<Return>", lambda x: parent.sort())
        self.config(command=lambda: parent.sort())

    def change_text(self, new_text):
        self.config(text=new_text)


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


# user interaction widgets

class Selectable(tk.Button):
    """Selectable text.

    Attributes:
        parent (Frame): frame that contains this button
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
                           relief="flat")
        self.__text = text_
        self.__normal_img = ImageImporter.load("selectable")
        self.__selected_img = ImageImporter.load("selectable_SELECTED")

        self.config(command=lambda: self.select())
        self.bind("<Return>", lambda x: self.select())

        self.__mark_unselected()

    def get_label(self):
        return self.__text

    def select(self):
        self.__mark_selected()

    def __mark_selected(self):
        self.config(image=self.__selected_img, fg=Colors.LIGHT)

    def __mark_unselected(self):
        self.config(image=self.__normal_img, fg=Colors.WHITE)


class MultiSelectable(Selectable):
    """Selectable; more than one element can be selected.

    Attributes:
        parent (Frame): frame that contains this selectable
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        Selectable.__init__(self, parent, text_)
        self.__selected = False

    def is_selected(self):
        return self.__selected

    def select(self):
        if self.__selected:
            self.__mark_unselected()
        else:
            self.__mark_selected()
        self.__selected = not self.__selected


class Option(Selectable):
    """Selectable; only one element can be selected at a time.

    Attributes:
        parent (Frame): frame that contains this selectable
        text_ (str): displayed text
        object_ (any with 'selected' attribute): object that offers this option
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
        parent (Frame): frame that contains this field
        name (str): suffix of bg image file name
    """

    def __init__(self, parent, name):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))

        self.__selected_bg = ImageImporter.load("bigfield_SELECTED_" + name)
        self.__error_bg = ImageImporter.load("bigfield_ERROR_" + name)

        self.__background_label = tk.Label(self, bg=self.cget("bg"))
        self.__background_label.grid(row=0, column=0)

        self.__entry = tk.Entry(self, width=3, borderwidth=0, insertwidth=2,
                                relief="flat", justify="center",
                                font="-size 38",
                                bg=Colors.SHADOW, fg=Colors.TEXT)
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
        parent (Frame): frame that contains this field
        text_ (str): Label
    """

    def __init__(self, parent, text_):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"),
                          width=95, height=91)
        self.__text = text_

        self.__bg_image = ImageImporter.load("smallfield")
        self.__error_bg_image = ImageImporter.load("smallfield_ERROR")

        self.__background_label = tk.Label(self, bg=self.cget("bg"),
                                           image=self.__bg_image)
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.pack_propagate(0)

        tk.Label(self, text=text_, anchor="sw", bg=Colors.WHITE,
                 fg=Colors.MEDIUM).pack(fill="x", padx=10, pady=5)
        self.__entry = tk.Entry(self, width=4, borderwidth=0,
                                insertwidth=2,
                                insertbackground=Colors.DARK,
                                relief="flat", justify="center",
                                font="-size 24",
                                bg=Colors.WHITE)
        self.__entry.pack()

        # spacer
        tk.Frame(self, bg=self.cget("bg"), height=12).pack(pady=2)

    def get_input(self):
        return self.__entry.get()

    def get_label(self):
        return self.__text

    def set_focus(self):
        self.__entry.focus_set()

    def mark_invalid(self):
        self.__background_label.config(image=self.__error_bg_image)

    def mark_valid(self):
        self.__background_label.config(image=self.__bg_image)


class Colors:
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


class ImageImporter:
    @staticmethod
    def load(image):
        from PIL import Image, ImageTk
        return ImageTk.PhotoImage(Image.open("res/" + image + ".png"))
