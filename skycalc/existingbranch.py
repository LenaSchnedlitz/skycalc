import tkinter as tk

import elements as elem


class CharLevelSelection(tk.Frame):
    """Frame where player levels (current and goal) are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.data = data

        container = tk.Frame(self, bg="aqua")
        container.pack(expand=True)

        self.current_level = elem.BigField(container, "Your Level:")
        self.current_level.pack(side="left")
        self.goal_level = elem.BigField(container, "Your Goal:")
        self.goal_level.pack(side="left")

    def can_use_input(self):
        try:
            current = int(self.current_level.get())
            goal = int(self.goal_level.get())
        except ValueError:
            return False
        if 0 < current < goal and 0 < goal < 500:  # arbitrary cap
            self.data.set_char_levels((current, goal))
            return True
        return False


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
        self.pack_by_type(self.skills, container)

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
                selected.append(skill)
        if len(selected) > 0:
            self.data.set_selected_skills(selected)
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


class SkillLevelSelection(tk.Frame):
    """Frame where skill levels are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.data = data

        self.container = tk.Frame(self)
        self.container.pack(expand=True)

        self.selected_skills = []

    def can_use_input(self):
        skill_levels = {}
        for skill in self.selected_skills:
            try:
                level = int(skill.get())
            except ValueError:
                return False
            if 15 <= level <= 100:
                skill_levels[skill.get_text()] = level
            else:
                return False
        self.data.set_skill_levels(skill_levels)
        return True

    def update(self):
        for child in self.container.winfo_children():
            child.destroy()
        self.selected_skills = []
        for skill in self.data.selected_skills:
            self.selected_skills.append(
                elem.SmallField(self.container, skill.get_text()))
        for skill in self.selected_skills:
            skill.pack()


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
