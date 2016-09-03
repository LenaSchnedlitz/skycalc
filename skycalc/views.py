"""Views and Window Elements."""

import tkinter as tk

import components as comp


# Elements

class Element(tk.Frame):
    """Standard element packed in a window. Packs automatically!

    Attributes:
        root: a window element's parent
    """

    def __init__(self, root):
        tk.Frame.__init__(self, root, bg=comp.Colors.BG)

        self.pack(fill="x")

    def refresh(self, i=0):
        self.update()

    def show_error(self, message):
        pass  # expected method


class Breadcrumbs(Element):
    """Displays progress by highlighting completed stages.

    Attributes:
        root: parent window
        n (int): number of stages
    """

    def __init__(self, root, n):
        Element.__init__(self, root)

        self.__line_img = comp.ImageImporter.load("bread_line")
        self.__points = []

        container = tk.Frame(self, bg=self.cget("bg"))
        for i in range(n):
            point = comp.BreadcrumbButton(container, i + 1)  # starts with 1
            self.__points.append(point)
            point.pack(side="left")
            if i + 1 < n:
                tk.Label(container, bg=self.cget("bg"),
                         image=self.__line_img).pack(side="left")
        container.pack(expand=True, pady=10)

    def refresh(self, i=0):
        for point in self.__points:
            point.refresh(i)


class Footer(Element):
    """Displays two NavButtons ('Back' and 'Next') and error messages.

    Attributes:
        root: parent window
        manager (ViewManager): a view manager
        n (int): number of stages
    """

    def __init__(self, root, manager, n):
        Element.__init__(self, root)
        self.__root = root
        self.__manager = manager
        self.__n = n

        self.__right = comp.NavButton(self)
        self.__right.config(command=lambda: self.show_next())
        self.__right.bind("<Return>", lambda x: self.show_next())
        self.__right.show_next_text()
        self.__right.pack(side="right", padx=10, pady=11)

        self.__left = comp.NavButton(self)
        self.__left.config(command=lambda: self.show_prev())
        self.__left.bind("<Return>", lambda x: self.show_prev())
        self.__left.show_back_text()
        self.__left.pack(side="left", padx=10, pady=11)

        self.__error_message = comp.ErrorMessage(self, "")
        self.__error_message.pack(side="left", expand=True, fill="both")

        self.pack_configure(side="bottom")

    def refresh(self, i=0):
        self.clear_error_message()
        if i == self.__n - 1:
            self.show_results_text()
        else:
            self.show_next_text()

    def show_next(self):
        self.__manager.show_next()

    def show_prev(self):
        self.__manager.show_prev()

    def show_results_text(self):
        self.__right.show_results_text()

    def show_next_text(self):
        self.__right.show_next_text()

    def show_error(self, message):
        self.__error_message.config(text=message)

    def clear_error_message(self):
        self.show_error("")


class Header(Element):
    """Displays a title and an instruction.

    Attributes:
        root: parent window
        titles (str array): array with all titles
        instructions (str array): array with all instructions
    """

    def __init__(self, root, titles, instructions):
        Element.__init__(self, root)

        self.__titles = titles
        self.__instructions = instructions

        self.__title = comp.ViewName(self, titles[0])
        self.__title.pack(fill="x", expand=True, padx="15")

        self.__text = comp.Instruction(self, instructions[0])
        self.__text.pack(fill="x", expand=True, padx="16")

    def refresh(self, i=0):
        self.__title.config(text=self.__titles[i])
        self.__text.config(text=self.__instructions[i])


class Results(tk.Frame):
    """Display calculated results.

    Three tabs + option to export.
    Attributes:
        parent (Tk): window that contains this frame
    """

    def __init__(self, parent, calculator):
        tk.Frame.__init__(self, parent)
        self.__parent = parent
        self.__calculator = calculator

        comp.Title(self, "Results", "white").pack()
        sel_container = tk.Frame(self)
        sel_container.pack(expand=True)

        self.__tab_container = tk.Frame(self)
        self.__tab_container.grid_rowconfigure(0, weight=1)
        self.__tab_container.grid_columnconfigure(0, weight=1)
        self.__tab_container.pack(fill="both", expand=True)

        self.__fastest_tab = self.build_tab("Fastest method",
                                            calculator.get_fastest_results())
        self.__easiest_tab = self.build_tab("Easiest method",
                                            calculator.get_easiest_results())
        self.__balanced_tab = self.build_tab("Balanced method",
                                             calculator.get_balanced_results())

        self.a = comp.TabButton(sel_container, "a tab",
                                self.__fastest_tab).pack(side="left")
        self.a = comp.TabButton(sel_container, "b tab",
                                self.__easiest_tab).pack(side="left")
        self.a = comp.TabButton(sel_container, "c tab",
                                self.__balanced_tab).pack(side="left")

    def build_tab(self, title, results):
        tab = tk.Frame(self.__tab_container)
        tab.grid(row=0, column=0, sticky="nsew")
        comp.Headline(tab, title).pack()
        for skill in results:
            comp.Instruction(tab, skill + ":\nCurrent Level: " + str(
                results[skill]["start"]) + "\nGoal Level: " + str(
                results[skill]["end"]) + "\nMade legendary " + str(
                results[skill]["legendary"]) + " times\n\n").pack()
        return tab


class Start(Element):
    """Welcome screen

    Choose between two buttons, 'NEW' and 'EXISTING'
    Attributes:
        parent (Tk): window that contains this element
    """

    def __init__(self, parent, manager):
        Element.__init__(self, parent)
        self.__manager = manager

        img = tk.PhotoImage(file="res/skyrim.gif")
        label = tk.Label(self, image=img, bg=self.cget("bg"))
        label.image = img
        label.pack()

        comp.Title(self, "Welcome!", comp.Colors.WHITE).pack()
        comp.Text(self,
                  "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                  "sed diam nonumy eirmod tempor invidunt ut labore et "
                  "dolore magna aliquyam erat, sed diam voluptua.",
                  comp.Colors.LIGHT).pack()

        button_container = tk.Frame(self, bg=self.cget("bg"))
        button_container.pack(pady=30)
        new_ = comp.BranchSelectionButton(button_container, "NEW",
                                          lambda: self.__start_new())
        new_.bind("<Return>", lambda x: self.__start_new())
        new_.pack(side="left", padx=5)
        ex_ = comp.BranchSelectionButton(button_container, "EXISTING",
                                         lambda: self.__start_ex())
        ex_.bind("<Return>", lambda x: self.__start_ex())
        ex_.pack(side="right", padx=5)

        self.pack(fill="both", expand=True)

    def __start_new(self):
        self.__manager.show_new_branch()

    def __start_ex(self):
        self.__manager.show_existing_branch()


class ViewContainer(Element):
    """Displays the current view.

    Attributes:
        root: parent window
        view_types (View array): array with all available view types
    """

    def __init__(self, root, view_types):
        Element.__init__(self, root)
        
        from calculator import Collector
        self.__collector = Collector()

        self.__views = []
        for type_ in view_types:
            self.__views.append(type_(self, self.__collector))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.pack_configure(fill="both", expand=True)

        self.refresh()

    def refresh(self, i=0):
        view = self.__views[i]
        view.update()
        view.tkraise()
        view.set_focus()

    def use_input(self, i):
        view = self.__views[i]
        try:
            view.can_use_input()
        except Exception as e:
            raise e


# Views

class View(tk.Frame):
    """Standard View.

    Attributes:
        parent (Frame): frame that contains this view
    """
    def __init__(self, parent: tk.Frame):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))

        self.grid(row=0, column=0, sticky="nsew")

    def set_focus(self):
        self.focus_set()

    def show_error(self):
        pass

    def update(self):
        pass


class CharLevelSelection(View):
    """Frame where player levels (current and goal) are entered.

    Attributes:
        parent (Frame): frame that contains this frame
        collector:
    """

    def __init__(self, parent, collector):
        View.__init__(self, parent)
        self.__collector = collector

        container = tk.Frame(self, bg=self.cget("bg"))
        container.pack(expand=True)

        self.__current_level = comp.BigField(container, "now")
        self.__current_level.pack(side="left", padx=45)

        self.__goal_level = comp.BigField(container, "goal")
        self.__goal_level.pack(side="left", padx=45)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def can_use_input(self):
        self.update()
        self.__collector.set_char_levels(self.__current_level.get_input(),
                                         self.__goal_level.get_input())

    def set_focus(self):
        self.__current_level.set_focus()

    def update(self):
        self.__current_level.mark_valid()
        self.__goal_level.mark_valid()


class GoalLevelSelection(View):
    """Frame where goal level is entered.

    Attributes:
        parent (Frame): frame that contains this frame

    """

    def __init__(self, parent, validator):
        View.__init__(self, parent)
        self.__validator = validator

        self.__goal_level = comp.BigField(self, "goal")
        self.__goal_level.pack(expand=True)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def can_use_input(self):
        self.__validator.set_goal(self.__goal_level.get_input())

    def set_focus(self):
        self.__goal_level.set_focus()

    def update(self):
        self.__goal_level.mark_valid()  # remove error highlight


class Races(View):
    """Default race selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame

    """

    def __init__(self, parent, validator):
        View.__init__(self, parent)
        self.__validator = validator

        self.__selected = ""

        self.__sorted_by_type = True
        self.__sort_button = comp.SortButton(self, "Sort alphabetically")
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
        headlines = [comp.Headline(self.__container, "Human"),
                     comp.Headline(self.__container, "Mer"),
                     comp.Headline(self.__container, "Beast")]
        return headlines

    def build_races(self):
        race_names = ("Breton", "Nord", "Imperial", "Redguard",
                      "Altmer", "Bosmer", "Dunmer", "Orc",
                      "Argonian", "Khajiit"
                      )
        races = []
        for name in race_names:
            races.append(comp.Option(self.__container, name, self))
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


class SkillLevelSelection(View):
    """Frame where skill levels are entered.

    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, collector):
        View.__init__(self, parent)
        self.__collector = collector

        self.__container = tk.Frame(self, bg=self.cget("bg"))
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
                comp.SmallField(self.__container, skill))
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


class Skills(View):
    """Default skill selection frame.

    Sorted by category.
    Attributes:
        parent (Frame): frame that contains this frame
    """

    def __init__(self, parent, validator):
        View.__init__(self, parent)
        self.__validator = validator

        self.__sorted_by_type = True
        self.__sort_button = comp.SortButton(self, "Sort alphabetically")
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
        headlines = [comp.Headline(self.__container, "Magic"),
                     comp.Headline(self.__container, "Combat"),
                     comp.Headline(self.__container, "Stealth")]
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
                comp.MultiSelectable(self.__container, skill_names[i]))
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


# Data

class ViewInfo:
    @staticmethod
    def get_existing_char_content():
        return (
            {"View": CharLevelSelection,
             "Title": "Levels",
             "Instruction": "Enter the level of your character and the level "
                            "you "
                            "would like to reach:"},
            {"View": Skills,
             "Title": "Skills",
             "Instruction": "Which skills would you like to train? Please "
                            "select:"},
            {"View": SkillLevelSelection,
             "Title": "Skill Levels",
             "Instruction": "Enter your current skill levels below:"}
        )

    @staticmethod
    def get_new_char_content():
        return (
            {"View": Races,
             "Title": "Races",
             "Instruction": "Select your character race:"},
            {"View": Skills,
             "Title": "Skills",
             "Instruction": "Which skills would you like to train? Please "
                            "select:"},
            {"View": GoalLevelSelection,
             "Title": "Level",
             "Instruction": "What's your goal level?"}
        )