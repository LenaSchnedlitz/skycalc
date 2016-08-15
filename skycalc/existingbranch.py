import tkinter as tk

import elements as elem


class CharLevelSelection(tk.Frame):
    """Frame where player levels (current and goal) are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        container = tk.Frame(self, bg="aqua")
        container.pack(expand=True)

        self.current_level = elem.BigField(container, "Your Level:")
        self.current_level.pack(side="left")
        self.goal_level = elem.BigField(container, "Your Goal:")
        self.goal_level.pack(side="left")

    def get(self):
        return self.current_level.get(), self.goal_level.get()

    @staticmethod
    def is_valid(input_):
        try:
            current = int(input_[0])
            goal = int(input_[1])
        except ValueError:
            return False
        return 0 < current < goal and 0 < goal < 500  # arbitrary cap


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

        container = tk.Frame(self)
        container.pack(fill="x", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.skills = self.build_skills(container)
        self.align_by_type(self.skills, container)

    @staticmethod
    def build_skills(container):
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
        return skills

    @staticmethod
    def align_by_type(skills, container):
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

    def get(self):
        selected = []
        for skill in self.skills:
            if skill.get_value():
                selected.append(skill)
        return selected

    @staticmethod
    def is_valid(input_):
        return len(input_) > 0

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


class SkillLevelSelection(tk.Frame):
    """Frame where skill levels are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        container = tk.Frame(self)
        container.pack(expand=True)

        self.skill_levels = []

        # dummy data
        elem.SmallField(container, "Alchemy").pack()
        elem.SmallField(container, "Destruction").pack()

    def get(self):
        return self.skill_levels

    @staticmethod
    def is_valid(input_):
        for skill_level in input_:
            try:
                level = int(skill_level)
            except ValueError:
                return False
            if 15 > level or level > 100:
                return False
        return True

    def update(self, data):
        pass


def create_content():
    content = (
        (CharLevelSelection, "Levels", "Enter your levels!"),
        (Skills, "Skills", "Select some skills!"),
        (SkillLevelSelection, "Skill Levels", "Enter your skill levels!")
    )
    return content


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    view_manager = elem.ViewManager(root, create_content())
    view_manager.pack(fill="both", expand=True)
    root.mainloop()
