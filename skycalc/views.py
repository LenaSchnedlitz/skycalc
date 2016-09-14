"""Views and Window Elements."""

import tkinter as tk

import widgets as w
from calculation import ValidationException


# Elements

class Element(tk.Frame):
    """Standard element packed in a window. Packs automatically!

    Attributes:
        root: a window element's parent
    """

    def __init__(self, root):
        tk.Frame.__init__(self, root, bg=w.Colors.BG)

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

        self.__start_img = w.ImageImporter.load("bread/START")
        self.__end_img = w.ImageImporter.load("bread/END")

        self.__points = []

        container = tk.Frame(self, bg=self.cget("bg"))
        container.pack(expand=True, pady=10)

        tk.Label(container, bg=self.cget("bg"), borderwidth=0,
                 image=self.__start_img).pack(side="left")

        for i in range(n):
            point = w.BreadcrumbButton(container, i)
            self.__points.append(point)
            point.pack(side="left")

        tk.Label(container, bg=self.cget("bg"), borderwidth=0,
                 image=self.__end_img).pack(side="left")

    def refresh(self, i=0):
        for point in self.__points:
            point.refresh(i)


class Footer(Element):
    """Displays two NavButtons and messages.

    Attributes:
        root: parent window
        manager (ViewManager): a view manager
        n (int): number of stages
    """

    def __init__(self, root, manager, n, instructions):
        Element.__init__(self, root)
        self.__root = root
        self.__manager = manager
        self.__n = n
        self.__instructions = instructions

        self.__right = w.NavButton(self)
        self.__right.config(command=lambda: self.__show_next())
        self.__right.bind("<Return>", lambda x: self.__show_next())
        self.__right.show_next_text()
        self.__right.pack(side="right", padx=10, pady=11)

        self.__left = w.NavButton(self)
        self.__left.config(command=lambda: self.__show_prev())
        self.__left.bind("<Return>", lambda x: self.__show_prev())
        self.__left.show_back_text()
        self.__left.pack(side="left", padx=10, pady=11)

        self.__message = w.Message(self, "")
        self.__message.pack(side="left", expand=True, fill="both")

        self.pack_configure(side="bottom")

    def refresh(self, i=0):
        self.__clear_error_message(i)
        if i == self.__n - 1:
            self.show_results_text()
        else:
            self.show_next_text()

    def show_next_text(self):
        self.__right.show_next_text()

    def show_results_text(self):
        self.__right.show_results_text()

    def show_error(self, text):
        self.__message.show_error(text)

    def __clear_error_message(self, i):
        self.__message.show_normal(self.__instructions[i])

    def __show_next(self):
        self.__manager.show_next()

    def __show_prev(self):
        self.__manager.show_prev()


class Header(Element):
    """Displays a title and an instruction.

    Attributes:
        root: parent window
        titles (str array): array with all titles
    """

    def __init__(self, root, titles):
        Element.__init__(self, root)

        self.__titles = titles
        self.__elements = []

        container = tk.Frame(self, bg=self.cget("bg"))
        container.pack(expand=True)

        for title in self.__titles:
            item = w.BreadcrumbLabel(container, title)
            item.pack(side="left")
            self.__elements.append(item)

        self.refresh()

    def refresh(self, i=0):
        for item in self.__elements:
            item.refresh(self.__titles[i])


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

        w.Title(self, "Results", "white").pack()
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

        self.a = w.TabButton(sel_container, "a tab",
                             self.__fastest_tab).pack(side="left")
        self.a = w.TabButton(sel_container, "b tab",
                             self.__easiest_tab).pack(side="left")
        self.a = w.TabButton(sel_container, "c tab",
                             self.__balanced_tab).pack(side="left")

    def build_tab(self, title, results):
        tab = tk.Frame(self.__tab_container)
        tab.grid(row=0, column=0, sticky="nsew")
        w.Headline(tab, title).pack()
        for skill in results:
            w.ViewInstruction(tab, skill + ":\nCurrent Level: " + str(
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

        button_container = tk.Frame(self, bg=self.cget("bg"))
        button_container.pack(pady=30)
        new_ = w.PathSelectionButton(button_container, "NEW",
                                     lambda: self.__start_new())
        new_.bind("<Return>", lambda x: self.__start_new())
        new_.pack(side="left", padx=5)
        ex_ = w.PathSelectionButton(button_container, "EXISTING",
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

        from calculation import InputCollector, InputValidator
        self.__collector = InputCollector(InputValidator)

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
        view.collect_input()


# Views

class View(tk.Frame):
    """Standard View.

    Attributes:
        parent (Frame): frame that contains this view
    """

    def __init__(self, parent: tk.Frame):
        tk.Frame.__init__(self, parent, bg=parent.cget("bg"))

        self.grid(row=0, column=0, sticky="nsew")

    def collect_input(self):
        pass  # expected

    def set_focus(self):
        self.focus_set()

    def update(self):
        pass  # expected


class CharLevels(View):
    """Frame where player levels (current and goal) are entered.

    Attributes:
        parent (Frame): frame that contains this frame
        collector: object that collects input data
    """

    def __init__(self, parent, collector):
        View.__init__(self, parent)
        self.__collector = collector

        container = tk.Frame(self, bg=self.cget("bg"))
        container.pack(expand=True)

        self.__current_level = w.BigField(container, "now")
        self.__current_level.pack(side="left", padx=45)

        self.__goal_level = w.BigField(container, "goal")
        self.__goal_level.pack(side="left", padx=45)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def collect_input(self):
        self.update()
        try:
            self.__collector.set_char_levels(
                now=self.__current_level.get_input(),
                goal=self.__goal_level.get_input())
        except ValidationException as e:
            self.__show_errors(e.get_errors())
            raise e

    def set_focus(self):
        self.__current_level.set_focus()

    def update(self):
        self.__current_level.mark_valid()
        self.__goal_level.mark_valid()

    def __show_errors(self, errors):
        for error in errors:
            if error == "goal":
                self.__goal_level.mark_invalid()
            elif error == "now":
                self.__current_level.mark_invalid()


class GoalLevel(View):
    """Frame where a goal level is entered.

    Attributes:
        parent (Frame): frame that contains this frame
        collector: object that collects input data
    """

    def __init__(self, parent, collector):
        View.__init__(self, parent)
        self.__collector = collector

        self.__goal_level = w.BigField(self, "goal")
        self.__goal_level.pack(expand=True)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def collect_input(self):
        self.update()
        try:
            self.__collector.set_char_levels(
                goal=self.__goal_level.get_input())
        except ValidationException as e:
            self.__show_errors(e.get_errors())
            raise e

    def set_focus(self):
        self.__goal_level.set_focus()

    def update(self):
        self.__goal_level.mark_valid()

    def __show_errors(self, errors):
        for error in errors:
            if error == "goal":
                self.__goal_level.mark_invalid()


class Races(View):
    """Default race selection frame.

    Can be sorted by type or by name.
    Attributes:
        parent (Frame): frame that contains this frame
        collector: object that collects input data
    """

    def __init__(self, parent, collector):
        View.__init__(self, parent)
        self.__collector = collector

        self.__selected = ""  # selected race

        self.__sorted_by_type = True
        self.__sort_button = w.SortButton(self, "Sort alphabetically")
        self.__sort_button.pack(anchor="ne")

        self.__container = self.__build_race_container()
        self.__container.pack(fill="both", expand=True)

        self.__headline_images = self.__build_headline_images()
        self.__headlines = self.__build_headlines()
        self.__races = self.__build_races()
        self.__sort_by_type()

    def collect_input(self):
        self.update()
        self.__collector.set_race(self.__selected)

    def sort(self):
        if self.__sorted_by_type:
            self.__sort_by_name()
            self.__sort_button.change_text("Sort by type")
            self.__sorted_by_type = False
        else:
            self.__sort_by_type()
            self.__sort_button.change_text("Sort alphabetically")
            self.__sorted_by_type = True

    def select(self, selection):
        self.__selected = selection
        for race in self.__races:
            if race.get_label() == selection:
                race.mark_selected()  # select clicked option
            else:
                race.mark_unselected()  # deselect all other options

    def __build_headline_images(self):
        from calculation import GameData
        headline_images = []
        for word in GameData.RACE_TYPES:
            headline_images.append(w.ImageImporter.load("category_names/" + word))
        return headline_images

    def __build_headlines(self):
        headlines = []
        for image in self.__headline_images:
            headlines.append(tk.Label(self.__container,
                                      bg=self.cget("bg"),
                                      borderwidth=0,
                                      image=image))
        return headlines

    def __build_race_container(self):
        container = tk.Frame(self, bg=self.cget("bg"), padx=50, pady=20)
        for i in range(3):
            container.grid_columnconfigure(i, weight=1)

        for i in range(6):  # looks better than range(5)
            container.grid_rowconfigure(i, weight=1)
        return container

    def __build_races(self):
        from calculation import GameData
        races = []
        for name in GameData.RACE_NAMES:
            races.append(w.Option(self.__container, name, self))
        return races

    def __sort_by_name(self):
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

    def __sort_by_type(self):
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


class SkillLevels(View):
    """Frame where skill levels are entered.

    Attributes:
        parent (Frame): frame that contains this frame
        collector: object that collects input data
    """

    def __init__(self, parent, collector):
        View.__init__(self, parent)
        self.__collector = collector

        self.__container = tk.Frame(self, bg=self.cget("bg"))
        self.__container.grid_rowconfigure(0, weight=1)
        self.__container.grid_rowconfigure(1, weight=1)
        self.__container.grid_rowconfigure(2, weight=1)
        self.__container.pack(fill="both", expand=True, padx=50, pady=50)

        self.__skills = []

    def collect_input(self):
        skill_levels = {}
        for skill in self.__skills:
            skill_levels[skill.get_label()] = skill.get_input()
            print(skill_levels)

        try:
            self.__collector.set_skill_levels(skill_levels)
        except ValidationException as e:
            self.__show_errors(e.get_errors())
            raise e

    @staticmethod
    def get_max_column(n):
        if n > 15:
            return 5
        elif n % 5 == 0:
            return 4
        elif n % 4 == 0 or n == 7:
            return 3
        elif n % 3 == 0:
            return 2
        elif n < 6:
            return n - 1
        else:
            return 5

    def set_focus(self):
        self.__skills[0].set_focus()

    def update(self):
        for child in self.__container.winfo_children():
            child.destroy()
        self.__skills = []
        for skill in self.__collector.get_selected_skills():
            self.__skills.append(
                w.SmallField(self.__container, skill))
        row_ = 0
        column_ = 0
        max_ = self.get_max_column(len(self.__skills))
        self.__make_columns_grow(max_)
        for skill in self.__skills:
            skill.grid(row=row_, column=column_, padx=5, pady=10)
            if column_ == max_:
                column_ = 0
                row_ += 1
            else:
                column_ += 1

    def __make_columns_grow(self, n):
        for i in range(6):
            self.__container.grid_columnconfigure(i, weight=0)  # reset
        for i in range(n + 1):
            self.__container.grid_columnconfigure(i, weight=1)  # set

    def __show_errors(self, errors):
        first_invalid = None
        for skill in self.__skills:
            skill.mark_valid()
            if skill.get_label() in errors:
                skill.mark_invalid()
                if first_invalid is None:
                    first_invalid = skill
        first_invalid.set_focus()


class Skills(View):
    """Default skill selection frame.

    Can be sorted by category or alphabetically
    Attributes:
        parent (Frame): frame that contains this frame
        collector: object that collects input data
    """

    def __init__(self, parent, collector):
        View.__init__(self, parent)
        self.__collector = collector

        self.__sorted_by_type = True
        self.__sort_button = w.SortButton(self, "Sort alphabetically")
        self.__sort_button.pack(anchor="ne")

        self.__container = self.__build_skill_container()
        self.__container.pack(fill="both", expand=True)

        self.__headline_images = self.__build_headline_images()
        self.__headlines = self.__build_headlines()
        self.__skills = self.__build_skills()

        self.__sort_by_type()

    def collect_input(self):
        selected = []
        for skill in self.__skills:
            if skill.is_selected():
                selected.append(skill.get_label())
        if not self.__sorted_by_type:
            selected = sorted(selected)
        self.__collector.set_selected_skills(selected)

    def sort(self):
        if self.__sorted_by_type:
            self.__sort_by_name()
            self.__sort_button.change_text("Sort by type")
            self.__sorted_by_type = False
        else:
            self.__sort_by_type()
            self.__sort_button.change_text("Sort alphabetically")
            self.__sorted_by_type = True

    def __build_headline_images(self):
        from calculation import GameData
        headline_images = []
        for word in GameData.SKILL_TYPES:
            headline_images.append(w.ImageImporter.load("category_names/" + word))
        return headline_images

    def __build_headlines(self):
        headlines = []
        for image in self.__headline_images:
            headlines.append(tk.Label(self.__container,
                                      bg=self.cget("bg"),
                                      borderwidth=0,
                                      image=image))
        return headlines

    def __build_skill_container(self):
        container = tk.Frame(self, bg=self.cget("bg"), padx=50, pady=20)
        for i in range(3):
            container.grid_columnconfigure(i, weight=1)

        for i in range(7):
            container.grid_rowconfigure(i, weight=1)
        return container

    def __build_skills(self):
        from calculation import GameData
        skills = []
        for name in GameData.SKILL_NAMES:
            skills.append(w.MultiSelectable(self.__container, name))
        return skills

    def __sort_by_name(self):
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

    def __sort_by_type(self):
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


class Recipe:
    EXISTING_CHAR = (
        {"View": CharLevels,
         "Title": "LEVELS",
         "Instruction": "Enter the level of your character and the level "
                        "you would like to reach."},
        {"View": Skills,
         "Title": "SKILLS",
         "Instruction": "Pick some skills you would like to train."},
        {"View": SkillLevels,
         "Title": "SKILL_LEVELS",
         "Instruction": "Enter your current skill levels below."}
    )

    NEW_CHAR = (
        {"View": Races,
         "Title": "RACES",
         "Instruction": "Select your character race."},
        {"View": Skills,
         "Title": "SKILLS",
         "Instruction": "Pick some skills you would like to train."},
        {"View": GoalLevel,
         "Title": "GOAL",
         "Instruction": "What's your goal level?"}
    )
