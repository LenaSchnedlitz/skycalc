"""Contains templates for most GUI components."""

import tkinter as tk


# different kinds of text and labels

class Instruction(tk.Label):
    """Instruction text.

    Attributes:
        parent (Frame): frame that contains this title
        text_ (str): displayed text
    """

    def __init__(self, parent, text_):
        tk.Label.__init__(self, parent, text=text_,
                          bg=parent.cget("bg"),
                          fg=Colors.DARK,
                          font=("Helvetica", 10))


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


class TableEntry(tk.Label):
    """Text, usually a table entry.

    Attributes:
        parent (Frame): frame that contains this text
        text_ (str): displayed text
        highlighted (boolean): text will be bigger and brighter if True
    """

    def __init__(self, parent, text_, highlighted=False):
        tk.Label.__init__(self, parent,
                          bg=parent.cget("bg"),
                          text=text_)
        if highlighted:
            self.config(fg=Colors.TEXT, font=("Helvetica", 11))
        else:
            self.config(fg=Colors.LIGHT, font=("Helvetica", 10))


# classic buttons

class ImageButton(tk.Button):
    """Button with an image.

    Attributes:
        parent (Frame): frame that contains this button
        label (str): default text / name
        command_: what happens when button is active
    """

    def __init__(self, parent, label, command_):
        tk.Button.__init__(self, parent,
                           activebackground=parent.cget("bg"),
                           bg=parent.cget("bg"),
                           borderwidth=0,
                           command=command_,
                           cursor="hand2",
                           relief="flat")

        self.__image = ImageImporter.load("button/" + label)
        self.config(image=self.__image)


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


class TabButton(tk.Button):
    """Tab index button.

    For results view
    Attributes:
        parent (Frame): container frame
        text_ (str): displayed text
        tab (Frame): frame that will be shown when the button is clicked
        marker: corresponding tab marker
    """

    def __init__(self, parent, text_, tab, buttons, marker=None):
        tk.Button.__init__(self, parent,
                           activebackground=parent.cget("bg"),
                           bg=parent.cget("bg"),
                           borderwidth=0,
                           cursor="hand2",
                           relief="flat")
        self.__parent = parent
        self.__tab = tab
        self.__buttons = buttons
        self.__marker = marker

        self.__deselected = ImageImporter.load("tab/names/" + text_)
        self.__selected = ImageImporter.load(
            "tab/names/" + text_ + "_SELECTED")

        self.config(command=lambda: self.__on_call())

        self.deselect()

    def deselect(self):
        self.config(image=self.__deselected)

    def select(self):
        for button in self.__buttons:
            button.deselect()
        self.config(image=self.__selected)
        if self.__marker is not None:
            self.__marker.select()

    def __on_call(self):
        self.__tab.tkraise()
        self.select()


class ToggleButton(tk.Button):
    """'Toggle button' used for sorting method selection.

    Attributes:
        parent (Frame): container frame
        text_ (str): button text, usually 'alphabetically', 'by category', ...
    """

    def __init__(self, parent, text_, command_):
        tk.Button.__init__(self, parent, text=text_, command=command_,
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
        self.bind("<Return>", command_)

    def change_text(self, new_text):
        self.config(text=new_text)


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


class Option(Selectable):
    """Selectable; only one element can be selected at a time.

    Attributes:
        parent (Frame): container frame
        text_ (str): displayed text
        provider: object that offers this option
    """

    def __init__(self, parent, text_, provider):
        Selectable.__init__(self, parent, text_)
        self.__object = provider

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


# visualisation

class BreadcrumbMarker(tk.Label):
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


# TODO: make more reusable
class ResultTable(tk.Frame):
    """Displays result data (returned by calculator-functions) in a table.

    Attributes:
        parent (tk.Frame): container
        data (dict): displayed result data
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))

        headlines = ["SKILL", "CURRENT", "GOAL", "TRAIN", "LEGENDARY"]
        for i in range(len(headlines)):
            Image(self, "headlines/" + headlines[i]).grid(row=0, column=i,
                                                          pady=15)

        sorted_relevant_skills = sorted(skill for skill in data.keys() if
                                        data[skill]["Times Leveled"] != 0)

        for i in range(len(sorted_relevant_skills)):
            skill = sorted_relevant_skills[i]
            entry = data[skill]
            TableEntry(self, skill, True).grid(row=i + 1, column=0, pady=7)
            TableEntry(self, entry["Start Level"]).grid(row=i + 1, column=1)
            TableEntry(self, entry["Final Level"]).grid(row=i + 1, column=2)
            TableEntry(self, str(entry["Times Leveled"]) + "x", True).grid(
                row=i + 1, column=3)
            TableEntry(self, str(entry["Times Legendary"]) + "x").grid(
                row=i + 1, column=4)


class TabMarker(tk.Label):
    """Display if a tab is selected. Can be controlled by a TabButton.

    Attributes:
        parent (Frame): container frame
        markers (list): list of all markers
    """

    def __init__(self, parent, markers):
        tk.Label.__init__(self, parent, bg=parent.cget("bg"), borderwidth=0)

        self.__markers = markers

        self.__deselected = ImageImporter.load("tab/markers/deselected")
        self.__selected = ImageImporter.load("tab/markers/selected")

        self.deselect()

    def deselect(self):
        self.config(image=self.__deselected)

    def select(self):
        for marker in self.__markers:
            marker.deselect()
        self.config(image=self.__selected)


# other

class Colors:
    """Some predefined colors."""
    BG = "#1A1816"
    SHADOW = "#12110F"
    TEXT = "#C0BFBF"
    ERROR = "#F22613"

    WHITE = "#EFEFEF"
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
