import tkinter as tk

import elements as elem


class Races(tk.Frame):
    """Default race selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))
        self.parent = parent
        self.data = data
        self.selected = ""
        self.sorted_by_type = True

        self.sort_button = elem.SortButton(self, "Sort alphabetically",
                                           lambda: self.sort())
        self.sort_button.pack(anchor="ne")

        container = tk.Frame(self, bg=parent.cget("bg"))
        container.pack(fill="x", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.races = self.build_races(container)
        self.headlines = self.build_headlines(container)
        self.pack_by_type()

    def build_races(self, container):
        race_names = ("Breton", "Nord", "Imperial", "Redguard",
                      "Altmer", "Bosmer", "Dunmer", "Orc",
                      "Argonian", "Khajiit"
                      )
        races = []
        for i in range(len(race_names)):
            races.append(elem.Option(container, race_names[i], self))
        return races

    @staticmethod
    def build_headlines(container):
        headlines = [elem.Headline(container, "Human"),
                     elem.Headline(container, "Mer"),
                     elem.Headline(container, "Beast")]
        return headlines

    def pack_by_type(self):
        for i in range(len(self.headlines)):
            self.headlines[i].grid(row=0, column=i)

        row_ = 1
        column_ = 0
        for i in range(len(self.races)):
            self.races[i].grid(row=row_, column=column_)
            if row_ == 4:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def pack_by_name(self):
        for headline in self.headlines:
            headline.grid_forget()
        sorted_races = sorted(self.races, key=lambda x: x.get_label())
        row_ = 0
        column_ = 0
        for i in range(len(sorted_races)):
            sorted_races[i].grid(row=row_, column=column_)
            if row_ == 4:
                row_ = 0
                column_ += 1
            else:
                row_ += 1

    def sort(self):
        if self.sorted_by_type:
            self.pack_by_name()
            self.sort_button.change_text("Sort by type")
            self.sorted_by_type = False
        else:
            self.pack_by_type()
            self.sort_button.change_text("Sort alphabetically")
            self.sorted_by_type = True

    def can_use_input(self):
        if self.selected == "":
            return False
        self.data.set_race(self.selected)
        return True


class Skills(tk.Frame):
    """Default skill selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))
        self.parent = parent
        self.data = data
        self.sorted_by_type = True

        container = tk.Frame(self, bg=parent.cget("bg"))
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.type_headlines = self.build_headlines(container)
        self.skills = self.build_skills(container)
        self.pack_by_type()

        self.sort_button = elem.SortButton(self, "Sort alphabetically",
                                           lambda: self.sort())
        self.sort_button.pack(anchor="ne")

        container.pack(fill="x", expand=True)

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

    @staticmethod
    def build_headlines(container):
        headlines = [elem.Headline(container, "Magic"),
                     elem.Headline(container, "Combat"),
                     elem.Headline(container, "Stealth")]
        return headlines

    def pack_by_type(self):
        for i in range(len(self.type_headlines)):
            self.type_headlines[i].grid(row=0, column=i)

        row_ = 1
        column_ = 0
        for i in range(len(self.skills)):
            self.skills[i].grid(row=row_, column=column_)
            if row_ == 6:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def pack_by_name(self):
        for headline in self.type_headlines:
            headline.grid_forget()
        sorted_skills = sorted(self.skills, key=lambda x: x.get_label())
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
        if self.sorted_by_type:
            self.pack_by_name()
            self.sort_button.change_text("Sort by type")
            self.sorted_by_type = False
        else:
            self.pack_by_type()
            self.sort_button.change_text("Sort alphabetically")
            self.sorted_by_type = True

    def can_use_input(self):
        selected = []
        for skill in self.skills:
            if skill.is_selected():
                selected.append(skill.get_label())
        if len(selected) > 0:
            self.data.set_selected_skills(selected)
            self.data.generate_selected_skill_levels()
            return True
        return False

    def update(self):
        pass  # needed for view manager


class GoalLevelSelection(tk.Frame):
    """Frame where goal level is entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))
        self.parent = parent
        self.data = data

        self.goal_level = elem.BigField(self, "Your Goal:")
        self.goal_level.pack(expand=True)

    def can_use_input(self):
        try:
            goal = int(self.goal_level.get_input())
        except ValueError:
            return False
        if 1 < goal < 500:  # arbitrary cap
            self.data.set_char_levels((1, goal))  # current level is always 1
            return True
        return False


def build_content():
    content = (
        {"View": Races,
         "Title": "Races",
         "Instruction": "Select a race!"},
        {"View": Skills,
         "Title": "Skills",
         "Instruction": "Select some skills!"},
        {"View": GoalLevelSelection,
         "Title": "Level",
         "Instruction": "Enter your goal level!"}
    )
    return content


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    view_manager = elem.ViewManager(root, build_content())
    view_manager.pack(fill="both", expand=True)
    root.mainloop()
