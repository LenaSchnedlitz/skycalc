import tkinter as tk


class Header(tk.Frame):
    """ Default header with breadcrumb bar, title, and instruction text """
    def __init__(self, parent, title, instruction):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # breadcrumb
        tk.Frame(self, bg="orange", height=30).pack(fill="x")

        # title and text
        tk.Label(self, text=title).pack(expand=1)
        tk.Label(self, wraplength=700, text=instruction).pack(expand=1)


class NavButton(tk.Button):
    """ Standard layout for 'previous'- & 'next'-button """
    def __init__(self, parent, color, label):
        tk.Button.__init__(self, parent, bg=color, text=label)
        self.parent = parent


class Footer(tk.Frame):
    """ Default footer containing a 'previous'- and a 'next'-button """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="gray", height=200)
        self.parent = parent

        NavButton(self, "white", "PREVIOUS").pack(side="left")
        NavButton(self, color="pink", label="NEXT").pack(side="right")


class Headline(tk.Label):
    """ Default headline style (NOT title style!) """
    def __init__(self, parent, line):
        tk.Label.__init__(self, parent, text=line, bg="aqua")
        self.parent = parent


class ToggleButton(tk.Button):
    """ Default style for buttons without borders / selectable text """
    def __init__(self, parent, label):
        tk.Button.__init__(self, parent, text=label)
        self.parent = parent


class BigField(tk.Frame):
    """ Default style for character level input fields with description """
    def __init__(self, parent, label):
        tk.Frame.__init__(self, parent, bg="white", width=200, height=150)
        self.parent = parent

        tk.Label(self, text=label).pack()
        tk.Entry(self).pack()


class SmallField(tk.Frame):
    """ Default style for skill level input fields with description """
    def __init__(self, parent, label):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        tk.Label(self, text=label).pack(side="left")
        tk.Entry(self).pack(side="left")


class Races(tk.Frame):
    """ Main race selection frame (IIa) """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        # initialize content
        Headline(self, line="Human").grid(row=0, column=0)
        ToggleButton(self, label="Breton").grid(row=1, column=0)
        ToggleButton(self, label="Nord").grid(row=2, column=0)
        ToggleButton(self, label="Imperial").grid(row=3, column=0)
        ToggleButton(self, label="Redguard").grid(row=4, column=0)

        Headline(self, line="Mer").grid(row=0, column=1)
        ToggleButton(self, label="Altmer").grid(row=1, column=1)
        ToggleButton(self, label="Bosmer").grid(row=2, column=1)
        ToggleButton(self, label="Dunmer").grid(row=3, column=1)
        ToggleButton(self, label="Orc").grid(row=4, column=1)

        Headline(self, line="Beast").grid(row=0, column=2)
        ToggleButton(self, label="Argonian").grid(row=1, column=2)
        ToggleButton(self, label="Khajiit").grid(row=2, column=2)


class CharLevelSelection(tk.Frame):
    """ Frame where current and goal level are entered (IIb) """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        center = tk.Frame(self, bg="aqua")
        center.pack(expand=1)
        BigField(center, label="Your Level:").pack(side="left")
        BigField(center, label="Your Goal:").pack(side="left")


class Skills(tk.Frame):
    """ Main skill selection frame (III) """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        # initialize content
        Headline(self, line="Magic").grid(row=0, column=0)
        ToggleButton(self, label="Illusion").grid(row=1, column=0)
        ToggleButton(self, label="Conjuration").grid(row=2, column=0)
        ToggleButton(self, label="Destruction").grid(row=3, column=0)
        ToggleButton(self, label="Restoration").grid(row=4, column=0)
        ToggleButton(self, label="Alteration").grid(row=5, column=0)
        ToggleButton(self, label="Enchanting").grid(row=6, column=0)

        Headline(self, line="Combat").grid(row=0, column=1)
        ToggleButton(self, label="Smithing").grid(row=1, column=1)
        ToggleButton(self, label="Heavy Armor").grid(row=2, column=1)
        ToggleButton(self, label="Block").grid(row=3, column=1)
        ToggleButton(self, label="Two-handed").grid(row=4, column=1)
        ToggleButton(self, label="One-handed").grid(row=5, column=1)
        ToggleButton(self, label="Archery").grid(row=6, column=1)

        Headline(self, line="Stealth").grid(row=0, column=2)
        ToggleButton(self, label="Light Armor").grid(row=1, column=2)
        ToggleButton(self, label="Sneak").grid(row=2, column=2)
        ToggleButton(self, label="Lockpicking").grid(row=3, column=2)
        ToggleButton(self, label="Pickpocket").grid(row=4, column=2)
        ToggleButton(self, label="Speech").grid(row=5, column=2)
        ToggleButton(self, label="Alchemy").grid(row=6, column=2)


class GoalLevelSelection(tk.Frame):
    """ Frame where goal level is entered (IVa) """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        BigField(self, label="Your Goal:").pack()


class SkillLevelSelection(tk.Frame):
    """ Frame where skill levels can be entered (IVb) """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        # dummy data
        SmallField(self, label="Alchemy").pack()
        SmallField(self, label="Destruction").pack()


class ContentWrapper(tk.Frame):
    """ Contains all necessary parts of a view """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="blue")
        self.parent = parent

        Header(self, "Title", "At vero eos et accusam et justo duo dolores et ea rebum.").pack(fill="x")
        SkillLevelSelection(self).pack(fill="x")
        Footer(self).pack(fill="x", side="bottom")


class Start(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # initialize content
        __image = tk.Frame(self, bg="gray", width=150, height=150)
        __title = tk.Label(self, bg="white", text="Welcome!")
        __introduction = tk.Label(self, bg="white", wraplength=700,
            text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                 "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                 "magna aliquyam erat, sed diam voluptua.")
        __wrapper = tk.Frame(self, bg="red", width=300, height=100)
        __new = tk.Button(__wrapper, text="NEW")
        __existing = tk.Button(__wrapper, text="EXISTING")

        __image.pack(expand=1)
        __title.pack(expand=1)
        __introduction.pack(expand=1)
        __wrapper.pack(expand=1)
        __new.pack(side="left")
        __existing.pack(side="right")


def configure_window(self):
    # title
    self.title("Skyrim Calculator")

    # size
    width = 800
    height = 600
    self.minsize(width, height)

    # position
    x_pos = (self.winfo_screenwidth() - width) / 2
    y_pos = (self.winfo_screenheight() - height) / 2
    self.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))


if __name__ == "__main__":
    root = tk.Tk()
    configure_window(root)
    start = ContentWrapper(root).pack(fill="both", expand=1)
    root.mainloop()
