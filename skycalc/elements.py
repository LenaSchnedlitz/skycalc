"""Templates for most GUI components (including view navigation)."""

import tkinter as tk


class ViewManager(tk.Frame):
    """Contain and manage all views of a branch.

    Attributes:
        parent (Tk): window that contains this frame
        content: 2 dimensional; each entry is of length 3 consisting of a frame
                [0], a title [1] and an instruction [2]
    """

    VIEW = 0
    TITLE = 1
    INSTRUCTION = 2

    def __init__(self, parent, content):
        tk.Frame.__init__(self, parent, bg="blue")
        self.parent = parent
        self.content = content
        self.current = 0

        self.header = Header(self, self.content[0][self.TITLE],
                             self.content[0][self.INSTRUCTION])
        self.header.pack(fill="x")

        self.view = tk.Frame(self)
        self.view.pack(fill="x")

        self.footer = Footer(self)
        self.set_footer(0)
        self.footer.pack(fill="x", side="bottom")

    def set_header(self, i):
        self.header.set(self.content[i][self.TITLE],
                        self.content[i][self.INSTRUCTION])

    def set_footer(self, i):
        if i == len(self.content):
            self.footer.set("< Back", "Get Results >")
        else:
            self.footer.set("< Back", "Next >")

    def show_next(self):
        if self.current + 1 < len(self.content):
            self.current += 1

    def show_prev(self):
        if self.current - 1 >= 0:
            self.current -= 1


class Header(tk.Frame):
    """Default header with breadcrumbs, title and instruction.

    Attributes:
        manager (ViewManager): contains and manages the header
        title (str): title text
        instruction (str): smaller instruction text
    """

    def __init__(self, manager: ViewManager, title, instruction):
        tk.Frame.__init__(self, manager, bg="white")
        self.parent = manager

        # breadcrumb
        tk.Frame(self, bg="orange", height=30).pack(fill="x")

        self.title = ViewTitle(self, title)
        self.title.pack(expand=1)

        self.text = Instruction(self, instruction)
        self.text.pack(expand=1)

    def set(self, title, instruction):
        self.title.config(text=title)
        self.text.config(text=instruction)


class Footer(tk.Frame):
    """Default footer containing a 'previous'- and a 'next'-button.

    Attributes:
        manager (ViewManager): contains and manages the footer
    """

    def __init__(self, manager: ViewManager):
        tk.Frame.__init__(self, manager, bg="gray", height=200)
        self.parent = manager

        self.left = NavButton(self, "")
        self.left.config(command=self.show_prev())
        self.left.pack(side="left")

        self.right = NavButton(self, "")
        self.right.config()
        self.right.pack(side="right")

    def show_next(self):
        self.parent.show_next()

    def show_prev(self):
        self.parent.show_prev()

    def set(self, left, right):
        self.left.config(text=left)
        self.right.config(text=right)


# different kinds of text

class Title(tk.Label):
    """Default title style - biggest text

    Attributes:
        parent (Frame): frame that contains this title
        text_ (str): displayed title text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, bg="yellow")
        self.parent = parent


class Headline(tk.Label):
    """Default headline style - smaller than title

    Attributes:
        parent (Frame): frame that contains the headline
        text_ (str): displayed headline text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, bg="aqua")
        self.parent = parent


class ViewTitle(tk.Label):
    """View title

    Attributes:
        parent (Frame): frame that contains the title, usually a header
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, bg="aqua")
        self.parent = parent


class Instruction(tk.Label):
    """Instruction

    Attributes:
        parent (Frame): frame that contains the instruction, usually a header
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, bg="aqua")
        self.parent = parent


class Text(tk.Label):
    """Default text style

    Attributes:
        parent (Frame): frame that contains this text
        text_ (str): displayed title text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_, wraplength=700,
                          bg="yellow")
        self.parent = parent


# classic buttons

class BranchSelectionButton(tk.Button):
    """Layout for 'NEW'- and 'EXISTING'-button.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'NEW' or 'EXISTING'
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_)
        self.parent = parent


class NavButton(tk.Button):
    """Standard layout for 'previous'- & 'next'-button.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'Back' or 'Next'
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_)
        self.parent = parent


class SortButton(tk.Button):
    """'Toggle button' for switching sorting methods.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): button text, usually 'alphabetically' or 'by category'
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_)
        self.parent = parent


class TabButton(tk.Button):
    """Result tab index button.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_)
        self.parent = parent


# user interaction widgets

class Selectable(tk.Button):
    """Default style for buttons without borders / selectable text.

    Attributes:
        parent (Frame): frame that contains this button
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Button.__init__(self, parent, text=text_)
        self.parent = parent


class BigField(tk.Frame):
    """Big input field with text.

    Perfect for character level input.
    Attributes:
        parent (Frame): frame that contains this field
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Frame.__init__(self, parent, bg="white", width=200, height=150)
        self.parent = parent

        tk.Label(self, text=text_).pack()
        tk.Entry(self).pack()


class SmallField(tk.Frame):
    """Small input field with text.

    Made for skill level input.
    Attributes:
        parent (Frame): frame that contains this field
        text_ (str): button text, usually 'Previous' or 'Next'
    """

    def __init__(self, parent, text_):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        tk.Label(self, text=text_).pack(side="left")
        tk.Entry(self).pack(side="left")
