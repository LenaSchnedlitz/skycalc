import tkinter as tk

import elements as elem


class CharLevelSelection(tk.Frame):
    """Frame where player levels (current and goal) are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))
        self.__parent = parent
        self.__data = data

        container = tk.Frame(self, bg=self.cget("bg"))
        container.pack(expand=True)

        self.__current_level = elem.BigField(container, "Your Level:")
        self.__current_level.pack(side="left", padx=45)

        self.__goal_level = elem.BigField(container, "Your Goal:")
        self.__goal_level.pack(side="left", padx=45)

        # spacer
        tk.Frame(self, height=50, bg=self.cget("bg")).pack(side="bottom")

    def can_use_input(self):
        try:
            current = int(self.__current_level.get_input())
            goal = int(self.__goal_level.get_input())
        except ValueError:
            return False
        if 0 < current < goal and 0 < goal < 300:  # arbitrary cap, >= 252
            self.__data.set_char_levels((current, goal))
            return True
        return False


class Skills(tk.Frame):
    """Default skill selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))
        self.__parent = parent
        self.__data = data
        self.__sorted_by_type = True

        self.__sort_button = elem.SortButton(self, "Sort alphabetically",
                                             lambda: self.sort())
        self.__sort_button.pack(anchor="ne")

        container = tk.Frame(self, bg=parent.cget("bg"), padx=50, pady=20)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)
        container.grid_rowconfigure(2, weight=1)
        container.grid_rowconfigure(3, weight=1)
        container.grid_rowconfigure(4, weight=1)
        container.grid_rowconfigure(5, weight=1)
        container.grid_rowconfigure(6, weight=1)
        container.pack(fill="both", expand=True)

        self.__type_headlines = self.build_headlines(container)
        self.__skills = self.build_skills(container)
        self.pack_by_type()

    @staticmethod
    def build_headlines(container):
        headlines = [elem.Headline(container, "Magic"),
                     elem.Headline(container, "Combat"),
                     elem.Headline(container, "Stealth")]
        return headlines

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
            skills.append(elem.MultiSelectable(container, skill_names[i]))
        return skills

    def pack_by_type(self):
        for i in range(len(self.__type_headlines)):
            self.__type_headlines[i].grid(row=0, column=i)

        row_ = 1
        column_ = 0
        for i in range(len(self.__skills)):
            self.__skills[i].grid(row=row_, column=column_, pady=3)
            if row_ == 6:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def pack_by_name(self):
        for headline in self.__type_headlines:
            headline.grid_forget()
        sorted_skills = sorted(self.__skills, key=lambda x: x.get_label())
        row_ = 0
        column_ = 0
        for i in range(len(sorted_skills)):
            sorted_skills[i].grid(row=row_, column=column_)
            if row_ == 5:
                row_ = 0
                column_ += 1
            else:
                row_ += 1

    def sort(self):
        if self.__sorted_by_type:
            self.pack_by_name()
            self.__sort_button.change_text("Sort by type")
            self.__sorted_by_type = False
        else:
            self.pack_by_type()
            self.__sort_button.change_text("Sort alphabetically")
            self.__sorted_by_type = True

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

    def can_use_input(self):
        selected = []
        for skill in self.__skills:
            if skill.is_selected():
                selected.append(skill.get_label())
        if len(selected) > 0:
            self.__data.set_selected_skills(selected)
            return True
        return False

    def update(self):
        pass  # needed for view manager


class SkillLevelSelection(tk.Frame):
    """Frame where skill levels are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))
        self.__parent = parent
        self.__data = data

        self.__container = tk.Frame(self, bg=parent.cget("bg"))
        self.__container.grid_rowconfigure(0, weight=1)
        self.__container.grid_rowconfigure(1, weight=1)
        self.__container.grid_rowconfigure(2, weight=1)
        self.__container.pack(fill="both", expand=True, padx=50, pady=50)

        self.selected_skills = []

    def can_use_input(self):
        skill_levels = {}
        for skill in self.selected_skills:
            try:
                level = int(skill.get_input())
            except ValueError:
                return False
            if 15 <= level <= 100:
                skill_levels[skill.get_label()] = level
            else:
                return False
        self.__data.set_skill_levels(skill_levels)
        return True

    def update(self):
        for child in self.__container.winfo_children():
            child.destroy()
        self.selected_skills = []
        for skill in self.__data.selected_skills:
            self.selected_skills.append(
                elem.SmallField(self.__container, skill))
        row_ = 0
        column_ = 0
        max_ = self.set_max(len(self.selected_skills))
        self.make_columns_grow(max_)
        for skill in self.selected_skills:
            skill.grid(row=row_, column=column_, padx=5, pady=10)
            if column_ == max_:
                column_ = 0
                row_ += 1
            else:
                column_ += 1

    @staticmethod
    def set_max(n):
        if n > 15:
            return 5
        elif n % 5 == 0:
            return 4
        elif n % 4 == 0:
            return 3
        elif n % 3 == 0:
            return 2
        elif n < 6:
            return n - 1
        else:
            return 5

    def make_columns_grow(self, n):
        for i in range(6):
            self.__container.grid_columnconfigure(i, weight=0)  # reset
        for i in range(n + 1):
            self.__container.grid_columnconfigure(i, weight=1)  # set


def build_content():
    content = (
        {"View": CharLevelSelection,
         "Title": "Levels",
         "Instruction": "Enter your levels!"},
        {"View": Skills,
         "Title": "Skills",
         "Instruction": "Select some skills!"},
        {"View": SkillLevelSelection,
         "Title": "Skill Levels",
         "Instruction": "Enter your skill levels!"}
    )
    return content


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    view_manager = elem.ViewManager(root, build_content())
    view_manager.pack(fill="both", expand=True)
    root.mainloop()
