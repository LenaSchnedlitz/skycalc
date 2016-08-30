import tkinter as tk

import elements as elem


class CharLevelSelection(elem.View):
    """Frame where player levels (current and goal) are entered.

    Attributes:
        parent (Frame): frame that contains this frame
        collector:
    """

    def __init__(self, parent, collector):
        elem.View.__init__(self, parent, collector)
        self.__collector = collector

        container = tk.Frame(self, bg=self.cget("bg"))
        container.pack(expand=True)

        self.__current_level = elem.BigField(container, "now")
        self.__current_level.pack(side="left", padx=45)

        self.__goal_level = elem.BigField(container, "goal")
        self.__goal_level.pack(side="left", padx=45)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def mark_valid(self):
        self.__current_level.mark_valid()
        self.__goal_level.mark_valid()

    def can_use_input(self):
        self.mark_valid()
        valid = True
        try:
            goal = int(self.__goal_level.get_input())
        except ValueError:
            self.__goal_level.mark_invalid()
            valid = False
        try:
            current = int(self.__current_level.get_input())
        except ValueError:
            self.__current_level.mark_invalid()
            valid = False
        if not valid:
            return False
        if 0 < current < goal and 0 < goal < 300:  # arbitrary cap, >= 252
            self.__collector.set_char_levels((current, goal))
            return True
        self.__goal_level.mark_invalid()
        self.__current_level.mark_invalid()
        return False

    def set_focus(self):
        self.__current_level.set_focus()


class Skills(elem.View):
    """Default skill selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, collector):
        elem.View.__init__(self, parent, collector)
        self.__collector = collector

        self.__sorted_by_type = True
        self.__sort_button = elem.SortButton(self, "Sort alphabetically")
        self.__sort_button.pack(anchor="ne")

        self.__container = self.build_skill_container()
        self.__container.pack(fill="both", expand=True)

        self.__headlines = self.build_headlines()
        self.__skills = self.build_skills()
        self.sort_by_type()

    def build_skill_container(self):
        container = tk.Frame(self, bg=self.cget("bg"), padx=50, pady=0)
        for i in range(3):
            container.grid_columnconfigure(i, weight=1)

        for i in range(7):
            container.grid_rowconfigure(6, weight=1)
        return container

    def build_headlines(self):
        headlines = [elem.Headline(self.__container, "Magic"),
                     elem.Headline(self.__container, "Combat"),
                     elem.Headline(self.__container, "Stealth")]
        return headlines

    def build_skills(self):
        skill_names = ("Illusion", "Conjuration", "Destruction",
                       "Restoration", "Alteration", "Enchanting",

                       "Smithing", "Heavy Armor", "Block",
                       "Two-handed", "One-handed", "Archery",

                       "Light Armor", "Sneak", "Lockpicking",
                       "Pickpocket", "Speech", "Alchemy"
                       )
        skills = []
        for i in range(len(skill_names)):
            skills.append(
                elem.MultiSelectable(self.__container, skill_names[i]))
        return skills

    def sort_by_type(self):
        for i in range(len(self.__headlines)):
            self.__headlines[i].grid(row=0, column=i)

        row_ = 1
        column_ = 0
        for skill in self.__skills:
            skill.grid(row=row_, column=column_, pady=3)
            skill.tkraise()  # for tabbing
            if row_ == 6:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def sort_by_name(self):
        for headline in self.__headlines:
            headline.grid_forget()

        sorted_skills = sorted(self.__skills, key=lambda x: x.get_label())
        row_ = 0
        column_ = 0
        for skill in sorted_skills:
            skill.grid(row=row_, column=column_)
            skill.tkraise()
            if row_ == 5:
                row_ = 0
                column_ += 1
            else:
                row_ += 1

    def sort(self):
        if self.__sorted_by_type:
            self.sort_by_name()
            self.__sort_button.change_text("Sort by type")
            self.__sorted_by_type = False
        else:
            self.sort_by_type()
            self.__sort_button.change_text("Sort alphabetically")
            self.__sorted_by_type = True

    def can_use_input(self):
        selected = []
        for skill in self.__skills:
            if skill.is_selected():
                selected.append(skill.get_label())
        if not self.__sorted_by_type:
            selected = sorted(selected)
        if len(selected) > 0:
            self.__collector.set_selected_skills(selected)
            return True
        return False


class SkillLevelSelection(elem.View):
    """Frame where skill levels are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, collector):
        elem.View.__init__(self, parent, collector)
        self.__collector = collector

        self.__container = tk.Frame(self, bg=parent.cget("bg"))
        self.__container.grid_rowconfigure(0, weight=1)
        self.__container.grid_rowconfigure(1, weight=1)
        self.__container.grid_rowconfigure(2, weight=1)
        self.__container.pack(fill="both", expand=True, padx=50, pady=50)

        self.__selected_skills = []

    @staticmethod
    def get_max_column(n):
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

    def can_use_input(self):
        skill_levels = {}
        for skill in self.__selected_skills:
            skill.mark_valid()  # reset error border
            try:
                level = int(skill.get_input())
            except ValueError:
                skill.mark_invalid()
                return False
            if 15 <= level <= 100:
                skill_levels[skill.get_label()] = level
            else:
                skill.mark_invalid()
                return False
        self.__collector.set_skill_levels(skill_levels)
        return True

    def set_focus(self):
        self.__selected_skills[0].set_focus()

    def update(self):
        for child in self.__container.winfo_children():
            child.destroy()
        self.__selected_skills = []
        for skill in self.__collector.selected_skills:
            self.__selected_skills.append(
                elem.SmallField(self.__container, skill))
        row_ = 0
        column_ = 0
        max_ = self.get_max_column(len(self.__selected_skills))
        self.make_columns_grow(max_)
        for skill in self.__selected_skills:
            skill.grid(row=row_, column=column_, padx=5, pady=10)
            if column_ == max_:
                column_ = 0
                row_ += 1
            else:
                column_ += 1


def build_content():
    content = (
        {"View": CharLevelSelection,
         "Title": "Levels",
         "Instruction": "Enter the level of your character and the level you "
                        "would like to reach:",
         "Error": "Invalid input."},
        {"View": Skills,
         "Title": "Skills",
         "Instruction": "Which skills would you like to train? Please select:",
         "Error": "You need to select at least one skill."},
        {"View": SkillLevelSelection,
         "Title": "Skill Levels",
         "Instruction": "Enter your current skill levels below:",
         "Error": "Skill levels are numbers between 15 and 100."}
    )
    return content


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    view_manager = elem.ViewManager(root, build_content())
    view_manager.pack(fill="both", expand=True)
    root.mainloop()
