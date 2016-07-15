import tkinter as tk
import widgets as w


class Races(tk.Frame):
    """Main race selection frame (IIa).

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        w.SortButton(self, label="Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.Headline(center, line="Human").grid(row=0, column=0)
        w.ToggleButton(center, label="Breton").grid(row=1, column=0)
        w.ToggleButton(center, label="Nord").grid(row=2, column=0)
        w.ToggleButton(center, label="Imperial").grid(row=3, column=0)
        w.ToggleButton(center, label="Redguard").grid(row=4, column=0)

        w.Headline(center, line="Mer").grid(row=0, column=1)
        w.ToggleButton(center, label="Altmer").grid(row=1, column=1)
        w.ToggleButton(center, label="Bosmer").grid(row=2, column=1)
        w.ToggleButton(center, label="Dunmer").grid(row=3, column=1)
        w.ToggleButton(center, label="Orc").grid(row=4, column=1)

        w.Headline(center, line="Beast").grid(row=0, column=2)
        w.ToggleButton(center, label="Argonian").grid(row=1, column=2)
        w.ToggleButton(center, label="Khajiit").grid(row=2, column=2)


class RacesSorted(tk.Frame):
    """Alternative race selection frame (IIa).

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        w.SortButton(self, label="Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.ToggleButton(center, label="Altmer").grid(row=0, column=0)
        w.ToggleButton(center, label="Argonian").grid(row=1, column=0)
        w.ToggleButton(center, label="Breton").grid(row=2, column=0)
        w.ToggleButton(center, label="Bosmer").grid(row=3, column=0)
        w.ToggleButton(center, label="Dunmer").grid(row=4, column=0)

        w.ToggleButton(center, label="Imperial").grid(row=0, column=1)
        w.ToggleButton(center, label="Khajiit").grid(row=1, column=1)
        w.ToggleButton(center, label="Nord").grid(row=2, column=1)
        w.ToggleButton(center, label="Orc").grid(row=3, column=1)
        w.ToggleButton(center, label="Redguard").grid(row=4, column=1)


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
        w.BigField(center, label="Your Level:").pack(side="left")
        w.BigField(center, label="Your Goal:").pack(side="left")


class Skills(tk.Frame):
    """Main skill selection frame (III).

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        w.SortButton(self, label="Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.Headline(center, line="Magic").grid(row=0, column=0)
        w.ToggleButton(center, label="Illusion").grid(row=1, column=0)
        w.ToggleButton(center, label="Conjuration").grid(row=2, column=0)
        w.ToggleButton(center, label="Destruction").grid(row=3, column=0)
        w.ToggleButton(center, label="Restoration").grid(row=4, column=0)
        w.ToggleButton(center, label="Alteration").grid(row=5, column=0)
        w.ToggleButton(center, label="Enchanting").grid(row=6, column=0)

        w.Headline(center, line="Combat").grid(row=0, column=1)
        w.ToggleButton(center, label="Smithing").grid(row=1, column=1)
        w.ToggleButton(center, label="Heavy Armor").grid(row=2, column=1)
        w.ToggleButton(center, label="Block").grid(row=3, column=1)
        w.ToggleButton(center, label="Two-handed").grid(row=4, column=1)
        w.ToggleButton(center, label="One-handed").grid(row=5, column=1)
        w.ToggleButton(center, label="Archery").grid(row=6, column=1)

        w.Headline(center, line="Stealth").grid(row=0, column=2)
        w.ToggleButton(center, label="Light Armor").grid(row=1, column=2)
        w.ToggleButton(center, label="Sneak").grid(row=2, column=2)
        w.ToggleButton(center, label="Lockpicking").grid(row=3, column=2)
        w.ToggleButton(center, label="Pickpocket").grid(row=4, column=2)
        w.ToggleButton(center, label="Speech").grid(row=5, column=2)
        w.ToggleButton(center, label="Alchemy").grid(row=6, column=2)


class SkillsSorted(tk.Frame):
    """Alternative skill selection frame (III).

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame.
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        w.SortButton(self, label="Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=1)
        w.ToggleButton(center, label="Alchemy").grid(row=0, column=0)
        w.ToggleButton(center, label="Alteration").grid(row=1, column=0)
        w.ToggleButton(center, label="Archery").grid(row=2, column=0)
        w.ToggleButton(center, label="Block").grid(row=3, column=0)
        w.ToggleButton(center, label="Conjuration").grid(row=4, column=0)
        w.ToggleButton(center, label="Destruction").grid(row=5, column=0)
        w.ToggleButton(center, label="Enchanting").grid(row=0, column=1)
        w.ToggleButton(center, label="Heavy Armor").grid(row=1, column=1)
        w.ToggleButton(center, label="Illusion").grid(row=2, column=1)
        w.ToggleButton(center, label="Light Armor").grid(row=3, column=1)
        w.ToggleButton(center, label="Lockpicking").grid(row=4, column=1)
        w.ToggleButton(center, label="One-handed").grid(row=5, column=1)
        w.ToggleButton(center, label="Pickpocket").grid(row=0, column=2)
        w.ToggleButton(center, label="Restoration").grid(row=1, column=2)
        w.ToggleButton(center, label="Smithing").grid(row=2, column=2)
        w.ToggleButton(center, label="Sneak").grid(row=3, column=2)
        w.ToggleButton(center, label="Speech").grid(row=4, column=2)
        w.ToggleButton(center, label="Two-handed").grid(row=5, column=2)


class GoalLevelSelection(tk.Frame):
    """Frame where goal level is entered (IVa).

    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        w.BigField(self, label="Your Goal:").pack()


class SkillLevelSelection(tk.Frame):
    """Frame where skill levels is entered (IVb).

    Attributes:
        parent (Frame): frame that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        # dummy data
        w.SmallField(self, label="Alchemy").pack()
        w.SmallField(self, label="Destruction").pack()


class ContentWrapper(tk.Frame):
    """Contain all necessary parts of a view.

    Attributes:
        parent (Frame): window that contains this frame
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="blue")
        self.parent = parent

        w.Header(self, "Title", "At vero eos et accusam et justo duo dolores et ea rebum.").pack(fill="x")
        SkillsSorted(self).pack(fill="x")
        w.Footer(self).pack(fill="x", side="bottom")


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
    start = ContentWrapper(root).pack(fill="both", expand=1)
    root.mainloop()
