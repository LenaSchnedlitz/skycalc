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

        elem.SortButton(self, "Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(fill="x", expand=True)
        center.grid_columnconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        center.grid_columnconfigure(2, weight=1)

        elem.Headline(center, "Human").grid(row=0, column=0)
        elem.Selectable(center, "Breton").grid(row=1, column=0)
        elem.Selectable(center, "Nord").grid(row=2, column=0)
        elem.Selectable(center, "Imperial").grid(row=3, column=0)
        elem.Selectable(center, "Redguard").grid(row=4, column=0)

        elem.Headline(center, "Mer").grid(row=0, column=1)
        elem.Selectable(center, "Altmer").grid(row=1, column=1)
        elem.Selectable(center, "Bosmer").grid(row=2, column=1)
        elem.Selectable(center, "Dunmer").grid(row=3, column=1)
        elem.Selectable(center, "Orc").grid(row=4, column=1)

        elem.Headline(center, "Beast").grid(row=0, column=2)
        elem.Selectable(center, "Argonian").grid(row=1, column=2)
        elem.Selectable(center, "Khajiit").grid(row=2, column=2)


class RacesSorted(tk.Frame):
    """Alternative race selection frame.

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        elem.SortButton(self, "Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=True)
        elem.Selectable(center, "Altmer").grid(row=0, column=0)
        elem.Selectable(center, "Argonian").grid(row=1, column=0)
        elem.Selectable(center, "Breton").grid(row=2, column=0)
        elem.Selectable(center, "Bosmer").grid(row=3, column=0)
        elem.Selectable(center, "Dunmer").grid(row=4, column=0)

        elem.Selectable(center, "Imperial").grid(row=0, column=1)
        elem.Selectable(center, "Khajiit").grid(row=1, column=1)
        elem.Selectable(center, "Nord").grid(row=2, column=1)
        elem.Selectable(center, "Orc").grid(row=3, column=1)
        elem.Selectable(center, "Redguard").grid(row=4, column=1)


class Skills(tk.Frame):
    """Default skill selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        elem.SortButton(self, "Sort alphabetically").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(fill="x", expand=True)
        center.grid_columnconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        center.grid_columnconfigure(2, weight=1)

        elem.Headline(center, "Magic").grid(row=0, column=0)
        elem.Selectable(center, "Illusion").grid(row=1, column=0)
        elem.Selectable(center, "Conjuration").grid(row=2, column=0)
        elem.Selectable(center, "Destruction").grid(row=3, column=0)
        elem.Selectable(center, "Restoration").grid(row=4, column=0)
        elem.Selectable(center, "Alteration").grid(row=5, column=0)
        elem.Selectable(center, "Enchanting").grid(row=6, column=0)

        elem.Headline(center, "Combat").grid(row=0, column=1)
        elem.Selectable(center, "Smithing").grid(row=1, column=1)
        elem.Selectable(center, "Heavy Armor").grid(row=2, column=1)
        elem.Selectable(center, "Block").grid(row=3, column=1)
        elem.Selectable(center, "Two-handed").grid(row=4, column=1)
        elem.Selectable(center, "One-handed").grid(row=5, column=1)
        elem.Selectable(center, "Archery").grid(row=6, column=1)

        elem.Headline(center, "Stealth").grid(row=0, column=2)
        elem.Selectable(center, "Light Armor").grid(row=1, column=2)
        elem.Selectable(center, "Sneak").grid(row=2, column=2)
        elem.Selectable(center, "Lockpicking").grid(row=3, column=2)
        elem.Selectable(center, "Pickpocket").grid(row=4, column=2)
        elem.Selectable(center, "Speech").grid(row=5, column=2)
        elem.Selectable(center, "Alchemy").grid(row=6, column=2)


class SkillsSorted(tk.Frame):
    """Alternative skill selection frame.

    Sorted alphabetically.
    Attributes:
        parent (Frame): frame that contains this frame.
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent

        elem.SortButton(self, "Sort by category").pack(anchor="ne")

        center = tk.Frame(self)
        center.pack(expand=True)
        elem.Selectable(center, "Alchemy").grid(row=0, column=0)
        elem.Selectable(center, "Alteration").grid(row=1, column=0)
        elem.Selectable(center, "Archery").grid(row=2, column=0)
        elem.Selectable(center, "Block").grid(row=3, column=0)
        elem.Selectable(center, "Conjuration").grid(row=4, column=0)
        elem.Selectable(center, "Destruction").grid(row=5, column=0)
        elem.Selectable(center, "Enchanting").grid(row=0, column=1)
        elem.Selectable(center, "Heavy Armor").grid(row=1, column=1)
        elem.Selectable(center, "Illusion").grid(row=2, column=1)
        elem.Selectable(center, "Light Armor").grid(row=3, column=1)
        elem.Selectable(center, "Lockpicking").grid(row=4, column=1)
        elem.Selectable(center, "One-handed").grid(row=5, column=1)
        elem.Selectable(center, "Pickpocket").grid(row=0, column=2)
        elem.Selectable(center, "Restoration").grid(row=1, column=2)
        elem.Selectable(center, "Smithing").grid(row=2, column=2)
        elem.Selectable(center, "Sneak").grid(row=3, column=2)
        elem.Selectable(center, "Speech").grid(row=4, column=2)
        elem.Selectable(center, "Two-handed").grid(row=5, column=2)


class GoalLevelSelection(tk.Frame):
    """Frame where goal level is entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        elem.BigField(self, "Your Goal:").pack(expand=True)


def create_content():
    content = (
        (Races, "Races", "Select a race!"),
        (Skills, "Skills", "Select some skills!"),
        (GoalLevelSelection, "Level", "Enter your goal level!")
    )
    return content


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    view_manager = elem.ViewManager(root, create_content())
    view_manager.pack(fill="both", expand=True)
    root.mainloop()
