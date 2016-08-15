import tkinter as tk

import elements as elem


class Races(tk.Frame):
    """Default race selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.data = data
        self.selected = ""

        elem.SortButton(self, "Sort alphabetically").pack(anchor="ne")

        container = tk.Frame(self)
        container.pack(fill="x", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.races = self.build_races(container)

    def build_races(self, container):
        race_names = ("Breton", "Nord", "Imperial", "Redguard",
                      "Altmer", "Bosmer", "Dunmer", "Orc",
                      "Argonian", "Khajiit"
                      )
        races = []
        for i in range(len(race_names)):
            races.append(elem.OnlySelectable(container, race_names[i], self))
        self.pack(races, container)
        return races

    @staticmethod
    def pack(races, container):
        elem.Headline(container, "Human").grid(row=0, column=0)
        elem.Headline(container, "Mer").grid(row=0, column=1)
        elem.Headline(container, "Beast").grid(row=0, column=2)

        row_ = 1
        column_ = 0
        for i in range(len(races)):
            races[i].grid(row=row_, column=column_)
            if row_ == 4:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def can_use_input(self):
        if self.selected == "":
            return False
        self.data.set_race(self.selected)
        return True


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

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent
        self.data = data

        elem.SortButton(self, "Sort alphabetically").pack(anchor="ne")

        container = tk.Frame(self)
        container.pack(fill="x", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.skills = self.build_skills(container)

    def build_skills(self, container):
        skill_names = ("Illusion", "Conjuration", "Destruction",
                       "Restoration", "Alteration", "Enchanting",

                       "Smithing", "Heavy Armor", "Block",
                       "Two-handed", "One-handed", "Archery",

                       "Light Armor", "Sneak", "Lockpicking",
                       "Pickpocket", "Speech", "Alchemy"
                       )
        skills = []
        for i in range(len(skill_names)):
            skills.append(elem.Selectable(container, skill_names[i]))
        self.pack_by_type(skills, container)
        return skills

    @staticmethod
    def pack_by_type(skills, container):
        elem.Headline(container, "Magic").grid(row=0, column=0)
        elem.Headline(container, "Combat").grid(row=0, column=1)
        elem.Headline(container, "Stealth").grid(row=0, column=2)

        row_ = 1
        column_ = 0
        for i in range(len(skills)):
            skills[i].grid(row=row_, column=column_)
            if row_ == 6:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def can_use_input(self):
        selected = []
        for skill in self.skills:
            if skill.get_value():
                selected.append(skill.get_text())
        if len(selected) > 0:
            self.data.set_selected_skills(selected)
            self.data.generate_selected_skill_levels()
            return True
        return False

    def update(self):
        pass  # needed for view manager


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

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.data = data

        self.goal_level = elem.BigField(self, "Your Goal:")
        self.goal_level.pack(expand=True)

    def can_use_input(self):
        try:
            goal = int(self.goal_level.get())
        except ValueError:
            return False
        if 1 < goal < 500:  # arbitrary cap
            self.data.set_char_levels((1, goal))  # current level is always 1
            return True
        return False


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
