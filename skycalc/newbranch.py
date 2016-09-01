import tkinter as tk

import elements as elem


class Races(elem.View):
    """Default race selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame

    """

    def __init__(self, parent, validator):
        elem.View.__init__(self, parent)
        self.__validator = validator

        self.__selected = ""

        self.__sorted_by_type = True
        self.__sort_button = elem.SortButton(self, "Sort alphabetically")
        self.__sort_button.pack(anchor="ne")

        self.__container = self.build_race_container()
        self.__container.pack(fill="both", expand=True)

        self.__headlines = self.build_headlines()
        self.__races = self.build_races()
        self.sort_by_type()

    def build_race_container(self):
        container = tk.Frame(self, bg=self.cget("bg"), padx=50, pady=20)
        for i in range(3):
            container.grid_columnconfigure(i, weight=1)

        for i in range(6):  # looks better than range(5)
            container.grid_rowconfigure(i, weight=1)
        return container

    def build_headlines(self):
        headlines = [elem.Headline(self.__container, "Human"),
                     elem.Headline(self.__container, "Mer"),
                     elem.Headline(self.__container, "Beast")]
        return headlines

    def build_races(self):
        race_names = ("Breton", "Nord", "Imperial", "Redguard",
                      "Altmer", "Bosmer", "Dunmer", "Orc",
                      "Argonian", "Khajiit"
                      )
        races = []
        for name in race_names:
            races.append(elem.Option(self.__container, name, self))
        return races

    def sort_by_type(self):
        self.__container.grid_columnconfigure(2, weight=1)  # set column scale

        for i in range(len(self.__headlines)):
            self.__headlines[i].grid(row=0, column=i)

        row_ = 1
        column_ = 0
        for race in self.__races:
            race.grid(row=row_, column=column_)
            race.tkraise()  # for expected tabbing order
            if row_ == 4:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def sort_by_name(self):
        self.__container.grid_columnconfigure(2, weight=0)  # set column scale

        for headline in self.__headlines:
            headline.grid_forget()

        sorted_races = sorted(self.__races, key=lambda x: x.get_label())
        row_ = 0
        column_ = 0
        for race in sorted_races:
            race.grid(row=row_, column=column_)
            race.tkraise()  # for expected tabbing order
            if row_ == 4:
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

    def select(self, selection):
        self.__selected = selection
        for race in self.__races:
            if race.get_label() == selection:
                race.mark_selected()  # select clicked option
            else:
                race.mark_unselected()  # deselect all other options

    def can_use_input(self):
        self.__validator.set_race(self.__selected)


class Skills(elem.View):
    """Default skill selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, validator):
        elem.View.__init__(self, parent)
        self.__validator = validator

        self.__sorted_by_type = True
        self.__sort_button = elem.SortButton(self, "Sort alphabetically")
        self.__sort_button.pack(anchor="ne")

        self.__container = self.build_skill_container()
        self.__container.pack(fill="both", expand=True)

        self.__headlines = self.build_headlines()
        self.__skills = self.build_skills()
        self.sort_by_type()

    def build_skill_container(self):
        container = tk.Frame(self, bg=self.cget("bg"), padx=50, pady=20)
        for i in range(3):
            container.grid_columnconfigure(i, weight=1)

        for i in range(7):
            container.grid_rowconfigure(i, weight=1)
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
            skill.grid(row=row_, column=column_)
            skill.tkraise()  # for tabbing order
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
            skill.tkraise()  # for tabbing order
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
        self.__validator.set_selected_skills(selected)


class GoalLevelSelection(elem.View):
    """Frame where goal level is entered.

    Attributes:
        parent (Frame): frame that contains this frame

    """

    def __init__(self, parent, validator):
        elem.View.__init__(self, parent)
        self.__validator = validator

        self.__goal_level = elem.BigField(self, "goal")
        self.__goal_level.pack(expand=True)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def can_use_input(self):
        self.__validator.set_goal(self.__goal_level.get_input())

    def set_focus(self):
        self.__goal_level.set_focus()

    def update(self):
        self.__goal_level.mark_valid()  # remove error highlight


def build_content():
    content = (
        {"View": Races,
         "Title": "Races",
         "Instruction": "Select your character race:"},
        {"View": Skills,
         "Title": "Skills",
         "Instruction": "Which skills would you like to train? Please select:"},
        {"View": GoalLevelSelection,
         "Title": "Level",
         "Instruction": "What's your goal level?"}
    )
    return content


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    view_manager = elem.ViewManager(root, build_content())
    root.mainloop()
