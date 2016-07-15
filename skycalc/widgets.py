"""Create and style templates for user interface components.

Construct templates from tkinter widgets.
Set colors, font, size, padding,....
"""

import tkinter as tk


class NavButton(tk.Button):
    """Standard layout for 'previous'- & 'next'-button.

    Attributes:
        parent (Frame): frame that contains this button
        label (str): button text, usually 'Previous' or 'Next'
    """

    def __init__(self, parent, color, label):
        tk.Button.__init__(self, parent, bg=color, text=label)
        self.parent = parent


class SortButton(tk.Button):
    """Button for selecting sorting methods.

    Attributes:
        parent (Frame): frame that contains this button
        label (str): button text, usually 'alphabetically' or 'by category'
    """

    def __init__(self, parent, label):
        tk.Button.__init__(self, parent, text=label)
        self.parent = parent


class ToggleButton(tk.Button):
    """Default style for buttons without borders / selectable text.

    Attributes:
        parent (Frame): frame that contains this button
        label (str): displayed text
    """

    def __init__(self, parent, label):
        tk.Button.__init__(self, parent, text=label)
        self.parent = parent


class Header(tk.Frame):
    """Default header for most views.

    Attributes:
        parent (Frame): frame that contains the header
        title (str): will be shown as title
        instruction (str): instruction text displayed beneath the title
    """

    def __init__(self, parent, title, instruction):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # breadcrumb
        tk.Frame(self, bg="orange", height=30).pack(fill="x")

        # title and text
        tk.Label(self, text=title).pack(expand=1)
        tk.Label(self, wraplength=700, text=instruction).pack(expand=1)


class Footer(tk.Frame):
    """Default footer containing a 'previous'- and a 'next'-button.

    Attributes:
        parent (Frame): frame that contains the footer
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="gray", height=200)
        self.parent = parent

        NavButton(self, "white", "PREVIOUS").pack(side="left")
        NavButton(self, color="pink", label="NEXT").pack(side="right")


class Headline(tk.Label):
    """Default headline style (NOT title!).

    Attributes:
        parent (Frame): frame that contains the headline
        line (str): displayed headline text
    """

    def __init__(self, parent, line):
        tk.Label.__init__(self, parent, text=line, bg="aqua")
        self.parent = parent


class BigField(tk.Frame):
    """Big input field with text.

    Perfect for character level input.
    Attributes:
        parent (Frame): frame that contains this field
        label (str): displayed text
    """

    def __init__(self, parent, label):
        tk.Frame.__init__(self, parent, bg="white", width=200, height=150)
        self.parent = parent

        tk.Label(self, text=label).pack()
        tk.Entry(self).pack()


class SmallField(tk.Frame):
    """Small input field with text.

    Perfect for skill level input.
    Attributes:
        parent (Frame): frame that contains this field
        label (str): button text, usually 'Previous' or 'Next'
    """

    def __init__(self, parent, label):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        tk.Label(self, text=label).pack(side="left")
        tk.Entry(self).pack(side="left")
