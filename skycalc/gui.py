import tkinter as tk
import widgets as w


class CharLevelSelection(tk.Frame):
    """Frame where current level and goal level are entered (IIb).

    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        center = tk.Frame(self, bg="aqua")
        center.pack(expand=1)
        w.BigField(center, line="Your Level:").pack(side="left")
        w.BigField(center, line="Your Goal:").pack(side="left")


class GoalLevelSelection(tk.Frame):
    """Frame where goal level is entered (IVa).

    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        w.BigField(self, line="Your Goal:").pack()


class Races(tk.Frame):
    """Main race selection frame (IIa).

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        w.SortButton(self, line="Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.Headline(center, line="Human").grid(row=0, column=0)
        w.ToggleButton(center, line="Breton").grid(row=1, column=0)
        w.ToggleButton(center, line="Nord").grid(row=2, column=0)
        w.ToggleButton(center, line="Imperial").grid(row=3, column=0)
        w.ToggleButton(center, line="Redguard").grid(row=4, column=0)

        w.Headline(center, line="Mer").grid(row=0, column=1)
        w.ToggleButton(center, line="Altmer").grid(row=1, column=1)
        w.ToggleButton(center, line="Bosmer").grid(row=2, column=1)
        w.ToggleButton(center, line="Dunmer").grid(row=3, column=1)
        w.ToggleButton(center, line="Orc").grid(row=4, column=1)

        w.Headline(center, line="Beast").grid(row=0, column=2)
        w.ToggleButton(center, line="Argonian").grid(row=1, column=2)
        w.ToggleButton(center, line="Khajiit").grid(row=2, column=2)


class RacesSorted(tk.Frame):
    """Alternative race selection frame (IIa).

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        w.SortButton(self, line="Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.ToggleButton(center, line="Altmer").grid(row=0, column=0)
        w.ToggleButton(center, line="Argonian").grid(row=1, column=0)
        w.ToggleButton(center, line="Breton").grid(row=2, column=0)
        w.ToggleButton(center, line="Bosmer").grid(row=3, column=0)
        w.ToggleButton(center, line="Dunmer").grid(row=4, column=0)

        w.ToggleButton(center, line="Imperial").grid(row=0, column=1)
        w.ToggleButton(center, line="Khajiit").grid(row=1, column=1)
        w.ToggleButton(center, line="Nord").grid(row=2, column=1)
        w.ToggleButton(center, line="Orc").grid(row=3, column=1)
        w.ToggleButton(center, line="Redguard").grid(row=4, column=1)


class Skills(tk.Frame):
    """Main skill selection frame (III).

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        w.SortButton(self, line="Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.Headline(center, line="Magic").grid(row=0, column=0)
        w.ToggleButton(center, line="Illusion").grid(row=1, column=0)
        w.ToggleButton(center, line="Conjuration").grid(row=2, column=0)
        w.ToggleButton(center, line="Destruction").grid(row=3, column=0)
        w.ToggleButton(center, line="Restoration").grid(row=4, column=0)
        w.ToggleButton(center, line="Alteration").grid(row=5, column=0)
        w.ToggleButton(center, line="Enchanting").grid(row=6, column=0)

        w.Headline(center, line="Combat").grid(row=0, column=1)
        w.ToggleButton(center, line="Smithing").grid(row=1, column=1)
        w.ToggleButton(center, line="Heavy Armor").grid(row=2, column=1)
        w.ToggleButton(center, line="Block").grid(row=3, column=1)
        w.ToggleButton(center, line="Two-handed").grid(row=4, column=1)
        w.ToggleButton(center, line="One-handed").grid(row=5, column=1)
        w.ToggleButton(center, line="Archery").grid(row=6, column=1)

        w.Headline(center, line="Stealth").grid(row=0, column=2)
        w.ToggleButton(center, line="Light Armor").grid(row=1, column=2)
        w.ToggleButton(center, line="Sneak").grid(row=2, column=2)
        w.ToggleButton(center, line="Lockpicking").grid(row=3, column=2)
        w.ToggleButton(center, line="Pickpocket").grid(row=4, column=2)
        w.ToggleButton(center, line="Speech").grid(row=5, column=2)
        w.ToggleButton(center, line="Alchemy").grid(row=6, column=2)


class SkillsSorted(tk.Frame):
    """Alternative skill selection frame (III).

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame.
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        w.SortButton(self, line="Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.ToggleButton(center, line="Alchemy").grid(row=0, column=0)
        w.ToggleButton(center, line="Alteration").grid(row=1, column=0)
        w.ToggleButton(center, line="Archery").grid(row=2, column=0)
        w.ToggleButton(center, line="Block").grid(row=3, column=0)
        w.ToggleButton(center, line="Conjuration").grid(row=4, column=0)
        w.ToggleButton(center, line="Destruction").grid(row=5, column=0)
        w.ToggleButton(center, line="Enchanting").grid(row=0, column=1)
        w.ToggleButton(center, line="Heavy Armor").grid(row=1, column=1)
        w.ToggleButton(center, line="Illusion").grid(row=2, column=1)
        w.ToggleButton(center, line="Light Armor").grid(row=3, column=1)
        w.ToggleButton(center, line="Lockpicking").grid(row=4, column=1)
        w.ToggleButton(center, line="One-handed").grid(row=5, column=1)
        w.ToggleButton(center, line="Pickpocket").grid(row=0, column=2)
        w.ToggleButton(center, line="Restoration").grid(row=1, column=2)
        w.ToggleButton(center, line="Smithing").grid(row=2, column=2)
        w.ToggleButton(center, line="Sneak").grid(row=3, column=2)
        w.ToggleButton(center, line="Speech").grid(row=4, column=2)
        w.ToggleButton(center, line="Two-handed").grid(row=5, column=2)


class SkillLevelSelection(tk.Frame):
    """Frame where skill levels is entered (IVb).

    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        # dummy data
        w.SmallField(self, line="Alchemy").pack()
        w.SmallField(self, line="Destruction").pack()


class ContentWrapper(tk.Frame):
    """Contain all necessary parts of a view.

    Attributes:
        parent (Tk): window that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="blue")
        self.parent = parent

        w.Header(self, title="Title", instruction="At vero eos et accusam et justo duo dolores et ea rebum.").pack(fill="x")
        SkillsSorted(self).pack(fill="x")
        w.Footer(self).pack(fill="x", side="bottom")


class Results(tk.Frame):
    """Display calculated results.

    Three tabs + option to export.
    Attributes:
        parent (Tk): window that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        w.Title(self, "Results").pack()
        sel_container = tk.Frame(self)
        sel_container.pack(expand=1)
        w.TabButton(sel_container, line="a tab").pack(side="left")
        w.TabButton(sel_container, line="b tab").pack(side="left")
        w.TabButton(sel_container, line="c tab").pack(side="left")
        res_container = tk.Frame(self)
        res_container.pack(expand=1)
        w.Headline(res_container, line="Variant").pack()
        w.Text(res_container, line="Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.").pack()


class Start(tk.Frame):
    """Welcome Screen

    Choose between two buttons, 'NEW' and 'EXISTING'
    Attributes:
        parent (Tk): window that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # image placeholder
        tk.Frame(self, bg="gray", width=150, height=150).pack(expand=1)

        w.Title(self, line="Welcome!").pack(expand=1)
        w.Text(self, wrap=700,
            line="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                 "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                 "magna aliquyam erat, sed diam voluptua.").pack(expand=1)

        wrapper = tk.Frame(self, bg="red", width=300, height=100)
        wrapper.pack(expand=1)
        w.ModeButton(wrapper, line="NEW").pack(side="left")
        w.ModeButton(wrapper, line="EXISTING").pack(side="right")


def configure_window(self):
    """Set window title, size, minsize and position"""
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
    start = Start(root).pack(fill="both", expand=1)
    root.mainloop()
