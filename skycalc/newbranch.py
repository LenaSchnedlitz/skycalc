import tkinter as tk
import elements as elem


class Races(tk.Frame):
    """Default race selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        elem.SortButton(self, line="Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        elem.Headline(center, line="Human").grid(row=0, column=0)
        elem.ToggleButton(center, line="Breton").grid(row=1, column=0)
        elem.ToggleButton(center, line="Nord").grid(row=2, column=0)
        elem.ToggleButton(center, line="Imperial").grid(row=3, column=0)
        elem.ToggleButton(center, line="Redguard").grid(row=4, column=0)

        elem.Headline(center, line="Mer").grid(row=0, column=1)
        elem.ToggleButton(center, line="Altmer").grid(row=1, column=1)
        elem.ToggleButton(center, line="Bosmer").grid(row=2, column=1)
        elem.ToggleButton(center, line="Dunmer").grid(row=3, column=1)
        elem.ToggleButton(center, line="Orc").grid(row=4, column=1)

        elem.Headline(center, line="Beast").grid(row=0, column=2)
        elem.ToggleButton(center, line="Argonian").grid(row=1, column=2)
        elem.ToggleButton(center, line="Khajiit").grid(row=2, column=2)


class RacesSorted(tk.Frame):
    """Alternative race selection frame.

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        elem.SortButton(self, line="Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        elem.ToggleButton(center, line="Altmer").grid(row=0, column=0)
        elem.ToggleButton(center, line="Argonian").grid(row=1, column=0)
        elem.ToggleButton(center, line="Breton").grid(row=2, column=0)
        elem.ToggleButton(center, line="Bosmer").grid(row=3, column=0)
        elem.ToggleButton(center, line="Dunmer").grid(row=4, column=0)

        elem.ToggleButton(center, line="Imperial").grid(row=0, column=1)
        elem.ToggleButton(center, line="Khajiit").grid(row=1, column=1)
        elem.ToggleButton(center, line="Nord").grid(row=2, column=1)
        elem.ToggleButton(center, line="Orc").grid(row=3, column=1)
        elem.ToggleButton(center, line="Redguard").grid(row=4, column=1)


class Skills(tk.Frame):
    """Default skill selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        elem.SortButton(self, line="Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        elem.Headline(center, line="Magic").grid(row=0, column=0)
        elem.ToggleButton(center, line="Illusion").grid(row=1, column=0)
        elem.ToggleButton(center, line="Conjuration").grid(row=2, column=0)
        elem.ToggleButton(center, line="Destruction").grid(row=3, column=0)
        elem.ToggleButton(center, line="Restoration").grid(row=4, column=0)
        elem.ToggleButton(center, line="Alteration").grid(row=5, column=0)
        elem.ToggleButton(center, line="Enchanting").grid(row=6, column=0)

        elem.Headline(center, line="Combat").grid(row=0, column=1)
        elem.ToggleButton(center, line="Smithing").grid(row=1, column=1)
        elem.ToggleButton(center, line="Heavy Armor").grid(row=2, column=1)
        elem.ToggleButton(center, line="Block").grid(row=3, column=1)
        elem.ToggleButton(center, line="Two-handed").grid(row=4, column=1)
        elem.ToggleButton(center, line="One-handed").grid(row=5, column=1)
        elem.ToggleButton(center, line="Archery").grid(row=6, column=1)

        elem.Headline(center, line="Stealth").grid(row=0, column=2)
        elem.ToggleButton(center, line="Light Armor").grid(row=1, column=2)
        elem.ToggleButton(center, line="Sneak").grid(row=2, column=2)
        elem.ToggleButton(center, line="Lockpicking").grid(row=3, column=2)
        elem.ToggleButton(center, line="Pickpocket").grid(row=4, column=2)
        elem.ToggleButton(center, line="Speech").grid(row=5, column=2)
        elem.ToggleButton(center, line="Alchemy").grid(row=6, column=2)


class SkillsSorted(tk.Frame):
    """Alternative skill selection frame.

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame.
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        elem.SortButton(self, line="Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        elem.ToggleButton(center, line="Alchemy").grid(row=0, column=0)
        elem.ToggleButton(center, line="Alteration").grid(row=1, column=0)
        elem.ToggleButton(center, line="Archery").grid(row=2, column=0)
        elem.ToggleButton(center, line="Block").grid(row=3, column=0)
        elem.ToggleButton(center, line="Conjuration").grid(row=4, column=0)
        elem.ToggleButton(center, line="Destruction").grid(row=5, column=0)
        elem.ToggleButton(center, line="Enchanting").grid(row=0, column=1)
        elem.ToggleButton(center, line="Heavy Armor").grid(row=1, column=1)
        elem.ToggleButton(center, line="Illusion").grid(row=2, column=1)
        elem.ToggleButton(center, line="Light Armor").grid(row=3, column=1)
        elem.ToggleButton(center, line="Lockpicking").grid(row=4, column=1)
        elem.ToggleButton(center, line="One-handed").grid(row=5, column=1)
        elem.ToggleButton(center, line="Pickpocket").grid(row=0, column=2)
        elem.ToggleButton(center, line="Restoration").grid(row=1, column=2)
        elem.ToggleButton(center, line="Smithing").grid(row=2, column=2)
        elem.ToggleButton(center, line="Sneak").grid(row=3, column=2)
        elem.ToggleButton(center, line="Speech").grid(row=4, column=2)
        elem.ToggleButton(center, line="Two-handed").grid(row=5, column=2)


class GoalLevelSelection(tk.Frame):
    """Frame where goal level is entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        elem.BigField(self, line="Your Goal:").pack()


class ContentWrapper(tk.Frame):
    """Contain all necessary parts of a view.

    Attributes:
        parent (Tk): window that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="blue")
        self.parent = parent

        elem.Header(self, title="Title",
                    instruction="At vero eos et accusam et justo duo dolores et ea rebum.").pack(
            fill="x")
        Races(self).pack(fill="x")
        elem.Footer(self).pack(fill="x", side="bottom")


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
    content = ContentWrapper(root).pack(fill="both", expand=1)
    root.mainloop()
