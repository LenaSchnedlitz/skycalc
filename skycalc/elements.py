"""Templates for most GUI components (including view navigation)."""

import tkinter as tk

import calculator as calc

LIGHT_BG = "#F0FCFF"
DARK_BG = "#222629"

WHITE = "#FFFFFF"
LIGHT = "#A1B0B0"
MEDIUM = "#536572"
DARK = "#435258"
BLACK = "#010101"

LIGHT_COLOR = "#53AC59"
MEDIUM_COLOR = "#3B8952"
DARK_COLOR = "#0F684B"


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


class ViewManager(tk.Frame):
    """Contain and manage all views of a branch.

    Attributes:
        parent (Tk): window that contains this frame
        content: tuple with a dictionary for each view
    """

    def __init__(self, parent, content):
        tk.Frame.__init__(self, parent, bg=LIGHT_BG)
        self.__parent = parent
        self.__content = content
        self.__data = calc.DataObject()
        self.__i = 0  # number of current view/page

        self.__header = self.build_header()
        self.__view_container = self.build_view_container()
        self.__views = self.build_views()
        self.raise_view()
        self.__footer = self.build_footer()
        self.update_footer()

    def build_header(self):
        header = Header(self, self.__content[self.__i]["Title"],
                        self.__content[self.__i]["Instruction"])
        header.pack(fill="x")
        return header

    def build_footer(self):
        footer = Footer(self)
        footer.pack(fill="x", side="bottom")
        return footer

    def build_view_container(self):
        container = tk.Frame(self, bg=self.cget("bg"))
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.pack(fill="both", expand=True)
        return container

    def build_views(self):
        views = []
        for i in range(len(self.__content)):
            view = self.__content[i]["View"](self.__view_container,
                                             self.__data)
            views.append(view)
            view.grid(row=0, column=0, sticky="nsew")
        return views

    def raise_view(self):
        view = self.__views[self.__i]
        view.tkraise()
        view.set_focus()

    def update(self):
        self.update_header()
        self.raise_view()
        self.update_footer()

    def update_header(self):
        self.__header.change_text(self.__content[self.__i]["Title"],
                                  self.__content[self.__i]["Instruction"])

    def update_footer(self):
        if self.__i == len(self.__content) - 1:
            self.__footer.change_text("< Back", "Get Results >")
        else:
            self.__footer.change_text("< Back", "Next >")

    def show_next(self):
        view = self.__views[self.__i]
        if view.can_use_input():
            if self.__i + 1 < len(self.__content):
                self.__i += 1
                self.__views[self.__i].update()  # update next view
                self.update()  # update view manager
            else:
                import results as r
                r.Results(self.__parent, calc.Calculator(self.__data)).pack(
                    fill="both", expand=True)
                self.destroy()

    def show_prev(self):
        if self.__i - 1 >= 0:
            self.__i -= 1
            self.update()
        else:
            import start as s
            s.Start(self.__parent).pack(fill="both", expand=True)
            self.destroy()


class Header(tk.Frame):
    """Header with breadcrumbs, title and instruction.

    Attributes:
        manager (ViewManager): contains and manages the header
        title (str): title text
        instruction (str): smaller instruction text
    """

    def __init__(self, manager: ViewManager, title, instruction):
        tk.Frame.__init__(self, manager, bg=manager.cget("bg"))
        self.__parent = manager

        # breadcrumb
        tk.Frame(self, bg=self.__parent.cget("bg"), height=30).pack(fill="x")

        self.__title = ViewName(self, title)
        self.__title.pack(fill="x", expand=True, padx="15")

        self.__text = Instruction(self, instruction)
        self.__text.pack(fill="x", expand=True, padx="16")

    def change_text(self, title, instruction):
        self.__title.config(text=title)
        self.__text.config(text=instruction)


class Footer(tk.Frame):
    """Footer containing a 'previous'- and a 'next'-button.

    Attributes:
        manager (ViewManager): contains and manages the footer
    """

    def __init__(self, manager: ViewManager):
        tk.Frame.__init__(self, manager, bg=manager.cget("bg"))
        self.__parent = manager

        self.__right = NavButton(self, True)
        self.__right.config(command=lambda: self.show_next())
        self.__right.bind("<Return>", lambda e: self.show_next())
        self.__right.pack(side="right", padx=10, pady=11)

        self.__left = NavButton(self, False)
        self.__left.config(command=lambda: self.show_prev())
        self.__left.bind("<Return>", lambda e: self.show_prev())
        self.__left.pack(side="left", padx=10, pady=11)


    def show_next(self):
        self.__parent.show_next()

    def show_prev(self):
        self.__parent.show_prev()

    def change_text(self, left, right):
        self.__left.config(text=left)
        self.__right.config(text=right)


# different kinds of text

class Title(tk.Label):
    """Title - biggest text.

    Attributes:
        parent (Frame): frame that contains this title
        text_ (str): displayed title text
        color_ (str): text color
    """

    def __init__(self, parent, text_, color_):
        tk.Label.__init__(self, parent, text=text_, fg=color_,
                          bg=parent.cget("bg"),
                          font=("Fira Sans Bold", 34))
        self.__parent = parent


class Headline(tk.Label):
    """Headline - smaller than title.

    Attributes:
        parent (Frame): frame that contains the headline
        text_ (str): displayed headline text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_,
                          bg=parent.cget("bg"), fg=DARK,
                          font=("Fira Sans Bold", 18))
        self.__parent = parent


class ViewName(tk.Label):
    """View name text.

    Attributes:
        parent (Frame): frame that contains the title, usually a header
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, pady=0, anchor="sw",
                          font=("Fira Sans Bold", 22),
                          bg=parent.cget("bg"), fg=BLACK)
        self.__parent = parent


class Instruction(tk.Label):
    """Instruction text.

    Attributes:
        parent (Frame): frame that contains the instruction, usually a header
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, pady=0,
                          anchor="nw", justify="left", wraplength=700,
                          font=("Fira Sans", 11),
                          bg=parent.cget("bg"), fg=DARK)
        self.__parent = parent


class Text(tk.Label):
    """Text.

    Attributes:
        parent (Frame): frame that contains this text
        text_ (str): displayed text
        color_ (str): text color
    """

    def __init__(self, parent, text_, color_):
        tk.Label.__init__(self, parent, text=text_, fg=color_,
                          wraplength=700, bg=parent.cget("bg"),
                          font=("Fira Sans", 10))
        self.__parent = parent


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
                           font=("Fira Sans", 14),
                           bg=LIGHT_COLOR, activebackground=MEDIUM_COLOR,
                           fg=WHITE, activeforeground=LIGHT)
        self.__parent = parent


class NavButton(tk.Button):
    """Standard layout for 'previous'- & 'next'-button.

    Attributes:
        parent (Frame): frame that contains this button
        highlighted (bool): different, highlighted style when true
    """

    def __init__(self, parent, highlighted):
        tk.Button.__init__(self, parent,
                           borderwidth=0, padx=10, pady=2,
                           cursor="hand2", relief="flat",
                           font=("Fira Sans", 10))
        self.__parent = parent
        if highlighted:
            self.config(
                bg=MEDIUM_COLOR, activebackground=DARK_COLOR,
                fg=WHITE, activeforeground=LIGHT)
        else:
            self.config(
                bg=self.__parent.cget("bg"), activebackground=LIGHT,
                fg=DARK, activeforeground=BLACK)


class SortButton(tk.Button):
    """'Toggle button', used for sorting method selection.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'alphabetically' or 'by category'
        command_: button command
    """

    def __init__(self, parent, text_, command_):
        tk.Button.__init__(self, parent, text=text_, command=command_,
                           borderwidth=0, padx=14,
                           cursor="hand2", relief="flat",
                           font=("Fira Sans Medium", 10),
                           bg=parent.cget("bg"),
                           activebackground=parent.cget("bg"),
                           fg=LIGHT, activeforeground=MEDIUM)
        self.__parent = parent

    def change_text(self, text_):
        self.config(text=text_)


class TabButton(tk.Button):
    """Tab index button

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

class MultiSelectable(tk.Button):
    """Multi select button / selectable text.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_,
                           borderwidth=0, width=15, pady=6,
                           cursor="hand2", relief="flat",
                           font=("Fira Sans Medium", 11),
                           bg=parent.cget("bg"), activebackground=MEDIUM_COLOR,
                           fg=BLACK, activeforeground=LIGHT_BG)
        self.__parent = parent
        self.__text = text_
        self.__selected = False
        self.config(command=lambda: self.change_selection())
        self.bind("<Return>", lambda e: self.change_selection())

    def change_selection(self):
        self.__selected = not self.__selected

    def is_selected(self):
        return self.__selected

    def get_label(self):
        return self.__text


class Option(tk.Button):
    """Button / selectable text. Only one option can be selected at a time.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): displayed text
        object_ (any with 'selected' attribute): object that offers this option
    """

    def __init__(self, parent, text_, object_):
        tk.Button.__init__(self, parent, text=text_,
                           borderwidth=0, padx=14, pady=7,
                           cursor="hand2", relief="flat",
                           font=("Fira Sans Medium", 12),
                           bg=parent.cget("bg"), activebackground=DARK_BG,
                           fg=BLACK, activeforeground=DARK)
        self.__parent = parent
        self.__text = text_
        self.__object = object_
        self.config(command=lambda: self.change_selection())
        self.bind("<Return>", lambda e: self.change_selection())

    def change_selection(self):
        self.__object.selected = self.__text

    def get_label(self):
        return self.__text


class BigField(tk.Frame):
    """Big input field with text.

    Perfect for character level input.
    Attributes:
        parent (Frame): frame that contains this field
        text_ (str): label
    """

    def __init__(self, parent, text_):
        tk.Frame.__init__(self, parent, bg=WHITE)
        self.__parent = parent
        self.__text = text_

        tk.Label(self, text=text_, anchor="sw",
                 bg=self.cget("bg"), fg=MEDIUM).pack(fill="x", padx=10, pady=5)
        self.__entry = tk.Entry(self, width=7, borderwidth=0,
                                insertwidth=2, insertbackground=DARK_COLOR,
                                relief="flat", justify="center",
                                font=("Fira Sans", 32),
                                bg=self.cget("bg"))
        self.__entry.pack()

        # spacer
        tk.Frame(self, bg=self.cget("bg"), height=18).pack()

    def get_input(self):
        return self.__entry.get()

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
        tk.Frame.__init__(self, parent, bg=WHITE)
        self.__parent = parent
        self.__text = text_

        tk.Label(self, text=text_, anchor="sw",
                 bg=self.cget("bg"), fg=MEDIUM).pack(fill="x", padx=10, pady=5)
        self.__entry = tk.Entry(self, width=6, borderwidth=0,
                                insertwidth=2, insertbackground=DARK_COLOR,
                                relief="flat", justify="center",
                                font=("Fira Sans", 20),
                                bg=self.cget("bg"))
        self.__entry.pack()

        # spacer
        tk.Frame(self, bg=self.cget("bg"), height=18).pack()

    def get_input(self):
        return self.__entry.get()

    def get_label(self):
        return self.__text

    def set_focus(self):
        self.__entry.focus_set()
