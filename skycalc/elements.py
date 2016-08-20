"""Templates for most GUI components (including view navigation)."""

import tkinter as tk

import calculator as calc

BG = "#FAEFD4"
BROWN = "#A57C65"
DARK = "#1A1E21"
DARK_BG = "#DECFC7"
DARK_BLUE = "#3F464D"
DARK_GREEN = "#6a7054"
LIGHT = "#EBE7E4"
LIGHT_BLUE = "#688B8A"
LIGHT_GREEN = "#A0B084"
MEDIUM = "#695856"
WHITE = "#FFFFFF"


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


#
class ViewManager(tk.Frame):
    """Contain and manage all views of a branch.

    Attributes:
        parent (Tk): window that contains this frame
        content: tuple with a dictionary for each view
    """

    def __init__(self, parent, content):
        tk.Frame.__init__(self, parent, bg=BG)
        self.parent = parent
        self.content = content
        self.data = calc.DataObject()
        self.i = 0  # number of current view/page

        self.header = self.build_header()
        self.view_container = self.build_view_container()
        self.views = self.build_views()
        self.raise_view()
        self.footer = self.build_footer()
        self.update_footer()

    def build_header(self):
        header = Header(self, self.content[self.i]["Title"],
                        self.content[self.i]["Instruction"])
        header.pack(fill="x")
        return header

    def build_view_container(self):
        container = tk.Frame(self, bg=BG)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.pack(fill="both", expand=True)
        return container

    def build_views(self):
        views = []
        for i in range(len(self.content)):
            view = self.content[i]["View"](self.view_container, self.data)
            views.append(view)
            view.grid(row=0, column=0, sticky="nsew")
        return views

    def build_footer(self):
        footer = Footer(self)
        footer.pack(fill="x", side="bottom")
        return footer

    def update(self):
        self.update_header()
        self.raise_view()
        self.update_footer()

    def update_header(self):
        self.header.change_text(self.content[self.i]["Title"],
                                self.content[self.i]["Instruction"])

    def raise_view(self):
        view = self.views[self.i]
        view.tkraise()

    def update_footer(self):
        if self.i == len(self.content) - 1:
            self.footer.change_text("< Back", "Get Results >")
        else:
            self.footer.change_text("< Back", "Next >")

    def show_next(self):
        view = self.views[self.i]
        if view.can_use_input():
            if self.i + 1 < len(self.content):
                self.i += 1
                self.views[self.i].update()  # update next view
                self.update()  # update view manager
            else:
                import results as r
                r.Results(self.parent, calc.Calculator(self.data)).pack(
                    fill="both", expand=True)
                self.destroy()

    def show_prev(self):
        if self.i - 1 >= 0:
            self.i -= 1
            self.update()
        else:
            import start as s
            s.Start(self.parent).pack(fill="both", expand=True)
            self.destroy()


class Header(tk.Frame):
    """Header with breadcrumbs, title and instruction.

    Attributes:
        manager (ViewManager): contains and manages the header
        title (str): title text
        instruction (str): smaller instruction text
    """

    def __init__(self, manager: ViewManager, title, instruction):
        tk.Frame.__init__(self, manager, bg=BG)
        self.__parent = manager

        # breadcrumb
        tk.Frame(self, bg=BG, height=30).pack(fill="x")

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

        self.__left = NavButton(self, False)
        self.__left.config(command=lambda: self.show_prev())
        self.__left.pack(side="left", padx=10, pady=11)

        self.__right = NavButton(self, True)
        self.__right.config(command=lambda: self.show_next())
        self.__right.pack(side="right", padx=10, pady=11)

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


#
class Headline(tk.Label):
    """Headline - smaller than title.

    Attributes:
        parent (Frame): frame that contains the headline
        text_ (str): displayed headline text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, bg=parent.cget("bg"),
                          font=("Fira Sans Bold", 20))
        self.__parent = parent


class ViewName(tk.Label):
    """View name text.

    Attributes:
        parent (Frame): frame that contains the title, usually a header
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, pady=0, anchor="sw",
                          font=("Fira Sans Light", 26),
                          bg=parent.cget("bg"), fg=DARK_BLUE)
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
                          font=("Fira Sans", 10),
                          bg=parent.cget("bg"), fg=MEDIUM)
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
                           bg=DARK_BG, activebackground=MEDIUM,
                           fg=DARK_BLUE, activeforeground=DARK)
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
                bg=LIGHT_BLUE, activebackground=DARK_BLUE,
                fg=WHITE, activeforeground=MEDIUM)
        else:
            self.config(
                bg=BG, activebackground=BG,
                fg=DARK_BLUE, activeforeground=MEDIUM)


class SortButton(tk.Button):
    """'Toggle button', used for sorting method selection.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'alphabetically' or 'by category'
        command_: button command
    """

    def __init__(self, parent, text_, command_):
        tk.Button.__init__(self, parent, text=text_, command=command_,
                           borderwidth=0, padx=14, pady=7,
                           cursor="hand2", relief="flat",
                           font=("Fira Sans Medium", 10),
                           bg=BG, activebackground=BG,
                           fg=BROWN, activeforeground=DARK_BG)
        self.__parent = parent

    def change_text(self, text_):
        self.config(text=text_)


#
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
                           borderwidth=0, padx=14, pady=7,
                           cursor="hand2", relief="flat",
                           font=("Fira Sans Medium", 12),
                           bg=BG, activebackground=BG,
                           fg=DARK_BLUE, activeforeground=DARK_GREEN)
        self.__parent = parent
        self.__text = text_
        self.__selected = False
        self.config(command=lambda: self.change_selection())

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
                           bg=BG, activebackground=BG,
                           fg=DARK_BLUE, activeforeground=DARK_GREEN)
        self.__parent = parent
        self.__text = text_
        self.__object = object_
        self.config(command=lambda: self.change_selection())

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
        tk.Frame.__init__(self, parent, bg=WHITE, width=300, height=200)
        self.__parent = parent
        self.__text = text_

        tk.Label(self, text=text_, anchor="sw",
                 bg=self.cget("bg"), fg=MEDIUM).pack(fill="x", padx=10, pady=8)
        self.__entry = tk.Entry(self, width=7, borderwidth=0,
                                insertwidth=2, insertbackground=DARK_BLUE,
                                relief="flat", justify="center",
                                font=("Fira Sans", 32),
                                bg=self.cget("bg"))
        self.__entry.pack()

        # spacer
        tk.Frame(self, bg=self.cget("bg"), height=15).pack()

    def get_input(self):
        return self.__entry.get()


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
                 bg=self.cget("bg"), fg=MEDIUM).pack(fill="x", padx=10, pady=8)
        self.__entry = tk.Entry(self, width=7, borderwidth=0,
                                insertwidth=2, insertbackground=DARK_BLUE,
                                relief="flat", justify="center",
                                font=("Fira Sans", 24),
                                bg=self.cget("bg"))
        self.__entry.pack(side="left")

    def get_input(self):
        return self.__entry.get()

    def get_label(self):
        return self.__text
