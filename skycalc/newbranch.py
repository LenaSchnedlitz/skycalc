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
        self.__parent = parent
        self.__data = data
        self.__selected = ""
        self.__sorted_by_type = True

        self.__sort_button = elem.SortButton(self, "Sort alphabetically",
                                             lambda: self.sort())
        self.__sort_button.bind("<Return>", lambda x: self.sort())
        self.__sort_button.pack(anchor="ne")

        self.__container = tk.Frame(self, bg=parent.cget("bg"),
                                    padx=50, pady=20)
        self.__container.grid_columnconfigure(0, weight=1)
        self.__container.grid_columnconfigure(1, weight=1)
        self.__container.grid_columnconfigure(2, weight=1)
        self.__container.grid_rowconfigure(0, weight=1)
        self.__container.grid_rowconfigure(1, weight=1)
        self.__container.grid_rowconfigure(2, weight=1)
        self.__container.grid_rowconfigure(3, weight=1)
        self.__container.grid_rowconfigure(4, weight=1)
        self.__container.grid_rowconfigure(5, weight=1)  # looks better
        self.__container.pack(fill="both", expand=True)

        self.__headlines = self.build_headlines(self.__container)
        self.__races = self.build_races(self.__container)
        self.sort_by_type()

    @staticmethod
    def build_headlines(container):
        headlines = [elem.Headline(container, "Human"),
                     elem.Headline(container, "Mer"),
                     elem.Headline(container, "Beast")]
        return headlines

    def build_races(self, container):
        race_names = ("Breton", "Nord", "Imperial", "Redguard",
                      "Altmer", "Bosmer", "Dunmer", "Orc",
                      "Argonian", "Khajiit"
                      )
        races = []
        for name in race_names:
            races.append(elem.Option(container, name, self))
        return races

    def sort_by_type(self):
        for i in range(len(self.__headlines)):
            self.__headlines[i].grid(row=0, column=i)

        row_ = 1
        column_ = 0
        for race in self.__races:
            race.grid(row=row_, column=column_)
            race.tkraise()
            if row_ == 4:
                row_ = 1
                column_ += 1
            else:
                row_ += 1
        self.__container.grid_columnconfigure(2, weight=1)  # set grid scale

    def sort_by_name(self):
        for headline in self.__headlines:
            headline.grid_forget()
        sorted_races = sorted(self.__races, key=lambda x: x.get_label())
        row_ = 0
        column_ = 0
        for race in sorted_races:
            race.grid(row=row_, column=column_)
            race.tkraise()
            if row_ == 4:
                row_ = 0
                column_ += 1
            else:
                row_ += 1
        self.__container.grid_columnconfigure(2, weight=0)  # reset grid scale

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
        if self.__selected == "":
            return False
        self.__data.set_race(self.__selected)
        return True

    def set_focus(self):
        self.focus_set()


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
        self.__sort_button.bind("<Return>", lambda x: self.sort())
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
        self.sort_by_type()

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

    def sort_by_type(self):
        for i in range(len(self.__type_headlines)):
            self.__type_headlines[i].grid(row=0, column=i)

        row_ = 1
        column_ = 0
        for skill in self.__skills:
            skill.grid(row=row_, column=column_)
            skill.tkraise()
            if row_ == 6:
                row_ = 1
                column_ += 1
            else:
                row_ += 1

    def sort_by_name(self):
        for headline in self.__type_headlines:
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
        if len(selected) > 0:
            self.__data.set_selected_skills(selected)
            self.__data.generate_selected_skill_levels()
            return True
        return False

    def update(self):
        pass  # needed for view manager

    def set_focus(self):
        self.focus_set()


class GoalLevelSelection(tk.Frame):
    """Frame where goal level is entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, data):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))
        self.__parent = parent
        self.__data = data

        self.__goal_level = elem.BigField(self, "Your Goal:")
        self.__goal_level.pack(expand=True)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def update(self):
        self.__goal_level.mark_valid()  # remove red error border

    def can_use_input(self):
        try:
            goal = int(self.__goal_level.get_input())
        except ValueError:
            self.__goal_level.mark_invalid()
            return False
        if 1 < goal < 300:  # arbitrary cap, >= 252
            self.__data.set_char_levels((1, goal))  # new char lvl is always 1
            return True
        self.__goal_level.mark_invalid()
        return False

    def set_focus(self):
        self.__goal_level.set_focus()


def build_content():
    content = (
        {"View": Races,
         "Title": "Races",
         "Instruction": "Select a race!",
         "Error": "Please select a race."},
        {"View": Skills,
         "Title": "Skills",
         "Instruction": "Select some skills!",
         "Error": "You need to select at least one skill."},
        {"View": GoalLevelSelection,
         "Title": "Level",
         "Instruction": "Enter your goal level!",
         "Error": "Invalid level."}
    )
    return content


if __name__ == "__main__":
    root = tk.Tk()
    elem.configure_window(root)
    view_manager = elem.ViewManager(root, build_content())
    view_manager.pack(fill="both", expand=True)
    root.mainloop()
