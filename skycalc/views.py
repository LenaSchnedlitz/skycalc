"""Views and Window Elements."""

import tkinter as tk

import widgets as w


# Window Content

class WindowContent(tk.Frame):
    """Standard view filling a window. Automatically packed!

    Attributes:
        root (Tk): window that contains this element
    """

    def __init__(self, root):
        tk.Frame.__init__(self, root, bg=w.Colors.BG)
        self.pack(fill="both", expand=True)


class InputGetter(WindowContent):
    """Contain input forms consisting of headers, input views and footers.

    Attributes:
        root (Tk): window that contains this element
        recipe: information which views are needed
        navigator: responsible for navigation between forms
        collector: collects input from forms
    """

    def __init__(self, root, recipe, navigator, collector):
        WindowContent.__init__(self, root)
        self.__collector = collector

        header = Header(self, [entry["Title"] for entry in recipe])
        views = InputFormContainer(self,
                                   [entry["View"] for entry in recipe],
                                   self.__collector)
        footer = Footer(self, [entry["Instruction"] for entry in recipe])

        navigator.set_content(
            {"Header": header, "Views": views, "Footer": footer})

    def get_collector(self):
        return self.__collector


class Results(WindowContent):
    """Display calculated results.

    Three tabs + option to export.
    Attributes:
        root (Tk): container window
        collector: data object
        return_command: allows to navigate back
    """

    def __init__(self, root, collector, return_command):
        WindowContent.__init__(self, root)
        import calculator as calc

        self.config(bg=w.Colors.SHADOW)

        levels = collector.get_skill_levels()
        now, goal = collector.get_char_levels()

        data = [calc.simulate_fast_training(levels, now, goal),
                calc.simulate_balanced_training(levels, now, goal),
                calc.simulate_easy_training(levels, now, goal)]
        names = ["fast", "balanced", "easy"]

        top = tk.Frame(self, bg=w.Colors.BG)
        w.Image(top, "tab/results").pack(pady=20)
        button_container = tk.Frame(top, bg=top.cget("bg"))
        button_container.pack()
        marker_container = tk.Frame(top, bg=top.cget("bg"))
        marker_container.pack()
        top.pack(fill="x")

        tab_container = tk.Frame(self, bg=self.cget("bg"))
        tab_container.pack()

        bottom = tk.Frame(self, bg=self.cget("bg"))
        w.ImageButton(bottom,
                      "start_over",
                      return_command).pack(side="left", padx=10, pady=11)
        bottom.pack(fill="x", side="bottom")

        tabs = self.__make_tabs(tab_container, data)
        markers = self.__make_markers(marker_container, len(tabs))
        buttons = self.__make_buttons(button_container, names, tabs, markers)

        buttons[1].invoke()

    @staticmethod
    def __make_buttons(parent, names, tabs, markers):
        buttons = []
        for i in range(len(tabs)):
            button = w.TabButton(parent, names[i], tabs[i], buttons,
                                 markers[i])
            button.pack(side="left")
            buttons.append(button)
        return buttons

    @staticmethod
    def __make_markers(parent, amount):
        markers = []
        w.Image(parent, "tab/markers/left").pack(side="left")
        for i in range(amount):
            marker = w.TabMarker(parent, markers)
            marker.pack(side="left")
            markers.append(marker)
        w.Image(parent, "tab/markers/right").pack(side="left")
        return markers

    @staticmethod
    def __make_tabs(parent, data):
        tabs = []
        for data_set in data:
            tab = tk.Frame(parent, bg=parent.cget("bg"))
            w.ResultTable(tab, data_set).pack()
            tab.grid(row=0, column=0, sticky="nsew")
            tabs.append(tab)
        return tabs


class Start(WindowContent):
    """Welcome screen.

    Let users choose whether they want to level a new character or an
    existing one.
    Attributes:
        root (Tk): container window
        controller: gui controller
    """

    def __init__(self, root, controller):
        WindowContent.__init__(self, root)
        self.__controller = controller
        self.config(bg=w.Colors.SHADOW)

        w.Image(self, "bg").place(relx=0.5, rely=0.5, anchor="center")

        rel_x = 0.48
        rel_y = 0.65

        new_ = w.ImageButton(self,
                             "new",
                             lambda x=None: self.__controller.show_input_forms(
                                 Recipe.NEW_CHAR))
        new_.config(bg="#141311")  # dirty fix
        new_.place(relx=rel_x, rely=rel_y, anchor="e")

        ex_ = w.ImageButton(self,
                            "pretrained",
                            lambda x=None: self.__controller.show_input_forms(
                                Recipe.EXISTING_CHAR))
        ex_.config(bg="#141311")  # dirty fix
        ex_.place(relx=1 - rel_x, rely=rel_y, anchor="w")


# View Elements

class ViewElement(tk.Frame):
    """Standard element that fills part of a window and can be updated.

    Automatically packed!
    Attributes:
        parent: a view element's container
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=w.Colors.BG)
        self.pack(fill="x")

    def refresh(self, i=0):
        self.update()

    def show_error(self, message):
        pass  # expected method


class Footer(ViewElement):
    """Display two NavButtons and a Message at the bottom of a window.

    Attributes:
        parent: parent frame/view/window
        instructions (str list): all instruction messages
    """

    def __init__(self, parent, instructions):
        ViewElement.__init__(self, parent)

        self.__instructions = instructions

        self.__right = w.NavButton(self, "NEXT", "RESULTS")
        self.__left = w.NavButton(self, "BACK")

        self.__right.pack(side="right", padx=10, pady=11)
        self.__left.pack(side="left", padx=10, pady=11)

        self.__message = w.Message(self, "")
        self.__message.pack(side="left", expand=True, fill="both")

        self.pack_configure(side="bottom")

    def refresh(self, i=0):
        self.__show_instruction(self.__instructions[i])

        if i == len(self.__instructions) - 1:  # last page
            self.__right.show_alternative()
        else:
            self.__right.show_default()

    def set_commands(self, left, right):
        self.__left.set_command(left)
        self.__right.set_command(right)

    def show_error(self, message):
        self.__message.show_error(message)

    def __show_instruction(self, message):
        self.__message.show_normal(message)


class Header(ViewElement):
    """Highlight the current stage and display its name to show progress.

    Option to navigate back to already completed stages.
    Attributes:
        parent: container frame/view/window
        titles (str list): list of all titles
    """

    def __init__(self, parent, titles):
        ViewElement.__init__(self, parent)

        self.__labels = []
        labels_container = tk.Frame(self, bg=self.cget("bg"))
        labels_container.pack(expand=True)

        self.__breadcrumb_buttons = []
        breadcrumbs_container = tk.Frame(self, bg=self.cget("bg"))
        breadcrumbs_container.pack(expand=True, pady=10)

        w.Image(breadcrumbs_container, "bread/START").pack(side="left")
        for i in range(len(titles)):
            label = w.BreadcrumbLabel(labels_container, titles[i], i)
            self.__labels.append(label)
            label.pack(side="left")

            button = w.BreadcrumbMarker(breadcrumbs_container, i)
            self.__breadcrumb_buttons.append(button)
            button.pack(side="left")
        w.Image(breadcrumbs_container, "bread/END").pack(side="left")

    def refresh(self, i=0):
        for label in self.__labels:
            label.refresh(i)
        for button in self.__breadcrumb_buttons:
            button.refresh(i)


class InputFormContainer(ViewElement):
    """Display the current input form.

    Attributes:
        parent: parent frame/view/window
        view_types (list): all available view types
        collector: data collector
    """

    def __init__(self, parent, view_types, collector):
        ViewElement.__init__(self, parent)

        self.__views = []
        for type_ in view_types:
            self.__views.append(type_(self, collector))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.pack_configure(fill="both", expand=True)

        self.refresh()

    def refresh(self, i=0):
        view = self.__views[i]
        view.update()
        view.tkraise()
        view.set_focus()

    def collect_input(self, i):
        view = self.__views[i]
        view.collect_input()


# Input Views

class InputForm(tk.Frame):
    """Default form type, used for getting user input.

    Put into (0,0) of the parent grid. Use of collectors recommended.
    Attributes:
        parent (Frame): frame that contains this view
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=w.Colors.SHADOW)

        self.grid(row=0, column=0, sticky="nsew")

    def collect_input(self):
        pass  # expected method

    def set_focus(self):
        self.focus_set()

    def update(self):
        pass  # expected method


class CharLevels(InputForm):
    """Frame where player levels (current and goal) are entered.

    Attributes:
        parent (Frame): container frame
        collector: collects input data
    """

    def __init__(self, parent, collector):
        InputForm.__init__(self, parent)
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
        from inputparser import ValidationException
        self.update()
        try:
            self.__collector.set_char_levels(
                now=self.__current_level.get_input(),
                goal=self.__goal_level.get_input())
        except ValidationException as e:
            self.__show_problems(e.get_problems())
            raise e

    def set_focus(self):
        self.__current_level.set_focus()

    def update(self):
        self.__current_level.mark_valid()
        self.__goal_level.mark_valid()

    def __show_problems(self, problems):
        for problem in problems:
            if problem == "goal":
                self.__goal_level.mark_invalid()
            elif problem == "now":
                self.__current_level.mark_invalid()


class GoalLevel(InputForm):
    """Frame where a goal level is entered.

    Attributes:
        parent (Frame): container frame
        collector: collects input data
    """

    def __init__(self, parent, collector):
        InputForm.__init__(self, parent)
        self.__collector = collector

        self.__goal_level = w.BigField(self, "goal")
        self.__goal_level.pack(expand=True)

        spacer = tk.Frame(self, height=50, bg=self.cget("bg"))
        spacer.pack(side="bottom")

    def collect_input(self):
        from inputparser import ValidationException
        self.update()
        try:
            self.__collector.set_char_levels(
                goal=self.__goal_level.get_input())
        except ValidationException as e:
            self.__show_problems(e.get_problems())
            raise e

    def set_focus(self):
        self.__goal_level.set_focus()

    def update(self):
        self.__goal_level.mark_valid()

    def __show_problems(self, problems):
        for problem in problems:
            if problem == "goal":
                self.__goal_level.mark_invalid()


class Races(InputForm):
    """Let user select their character's race.

    Can be sorted by type or by name.
    Attributes:
        parent (Frame): container frame
        collector: collects input data
    """

    def __init__(self, parent, collector):
        InputForm.__init__(self, parent)
        self.__collector = collector

        self.__selected = ""  # selected race

        self.__sorted_by_type = True
        self.__sort_button = w.ToggleButton(self, "Sort alphabetically",
                                            lambda x=None: self.__sort())
        self.__sort_button.pack(anchor="ne", pady=10)

        self.__container = self.__build_race_container()
        self.__container.pack(fill="both", expand=True)

        self.__headlines = self.__build_headlines()
        self.__races = self.__build_races()
        self.__sort_by_type()

    def collect_input(self):
        self.update()
        self.__collector.set_race(self.__selected)  # no try block necessary
        self.__collector.set_template(self.__selected)

    def select(self, selection):
        self.__selected = selection
        for race in self.__races:
            if race.get_label() == selection:
                race.mark_selected()  # select clicked option
            else:
                race.mark_unselected()  # deselect all other options

    def __build_headlines(self):
        from inputparser import GameData

        headlines = []
        for word in GameData.RACE_TYPES:
            headlines.append(
                w.Image(self.__container, "category_names/" + word))

        return headlines

    def __build_race_container(self):
        container = tk.Frame(self, bg=self.cget("bg"), padx=50, pady=20)

        for i in range(3):
            container.grid_columnconfigure(i, weight=1)
        for i in range(6):  # looks better than range(5)
            container.grid_rowconfigure(i, weight=1)

        return container

    def __build_races(self):
        from inputparser import GameData
        races = []
        for name in GameData.RACE_NAMES:
            races.append(w.Option(self.__container, name, self))
        return races

    def __sort(self):
        if self.__sorted_by_type:
            self.__sort_by_name()
            self.__sort_button.change_text("Sort by type")
            self.__sorted_by_type = False
        else:
            self.__sort_by_type()
            self.__sort_button.change_text("Sort alphabetically")
            self.__sorted_by_type = True

    def __sort_by_name(self):
        self.__container.grid_columnconfigure(2, weight=0)  # set column scale

        for headline in self.__headlines:
            headline.grid_forget()

        sorted_races = sorted(self.__races, key=lambda x: x.get_label())
        row_ = 0
        column_ = 0
        for race in sorted_races:
            race.grid(row=row_, column=column_)
            race.tkraise()  # for keyboard only navigation
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
            race.tkraise()  # for keyboard only navigation
            if row_ == 4:
                row_ = 1
                column_ += 1
            else:
                row_ += 1


class SkillLevels(InputForm):
    """Frame where skill levels are entered.

    Attributes:
        parent (Frame): container frame
        collector: collects input data
    """

    def __init__(self, parent, collector):
        InputForm.__init__(self, parent)
        self.__collector = collector

        self.__container = tk.Frame(self, bg=self.cget("bg"))
        self.__container.grid_rowconfigure(0, weight=1)
        self.__container.grid_rowconfigure(1, weight=1)
        self.__container.grid_rowconfigure(2, weight=1)
        self.__container.pack(fill="both", expand=True, padx=50, pady=50)

        self.__skills = []

    def collect_input(self):
        from inputparser import ValidationException
        skill_levels = {}
        for skill in self.__skills:
            skill_levels[skill.get_label()] = skill.get_input()

        try:
            self.__collector.set_skill_levels(skill_levels)
        except ValidationException as e:
            self.__show_problems(e.get_problems())
            raise e

    def set_focus(self):
        self.__skills[0].set_focus()

    def update(self):
        for child in self.__container.winfo_children():
            child.destroy()

        self.__skills = []
        for skill in self.__collector.get_selected_skills():
            self.__skills.append(w.SmallField(self.__container, skill))
        row_ = 0
        column_ = 0
        max_ = self.__calculate_max_index(len(self.__skills))
        self.__update_column_scale(max_)
        for skill in self.__skills:
            skill.grid(row=row_, column=column_, padx=5, pady=10)
            if column_ == max_:
                column_ = 0
                row_ += 1
            else:
                column_ += 1

    @staticmethod
    def __calculate_max_index(n):
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

    def __show_problems(self, problems):
        first_invalid = None
        for skill in self.__skills:
            skill.mark_valid()
            if skill.get_label() in problems:
                skill.mark_invalid()
                if first_invalid is None:
                    first_invalid = skill
        first_invalid.set_focus()

    def __update_column_scale(self, n):
        for i in range(6):
            self.__container.grid_columnconfigure(i, weight=0)  # reset
        for i in range(n + 1):
            self.__container.grid_columnconfigure(i, weight=1)  # set


class Skills(InputForm):
    """Let player select some skills.

    Can be sorted by category or alphabetically.
    Attributes:
        parent (Frame): container frame
        collector: collects input data
    """

    def __init__(self, parent, collector):
        InputForm.__init__(self, parent)
        self.__collector = collector

        self.__sorted_by_type = True
        self.__sort_button = w.ToggleButton(self,
                                            "Sort alphabetically",
                                            lambda x=None: self.__sort())
        self.__sort_button.pack(anchor="ne", pady=10)

        self.__container = self.__build_skill_container()
        self.__container.pack(fill="both", expand=True)

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
        self.__collector.set_template(None)
        self.__collector.set_selected_skills(selected)

    def update(self):
        if self.__collector.has_template():
            selection = self.__collector.get_template()
            self.__deselect_all()
            for button in self.__skills:
                if button.get_label() in selection:
                    button.select()

    def __build_headlines(self):
        from inputparser import GameData

        headlines = []
        for word in GameData.SKILL_TYPES:
            headlines.append(
                w.Image(self.__container, "category_names/" + word))

        return headlines

    def __build_skill_container(self):
        container = tk.Frame(self, bg=self.cget("bg"), padx=50, pady=20)

        for i in range(3):
            container.grid_columnconfigure(i, weight=1)
        for i in range(7):
            container.grid_rowconfigure(i, weight=1)

        return container

    def __build_skills(self):
        from inputparser import GameData

        skills = []
        for name in GameData.SKILL_NAMES:
            skills.append(w.MultiSelectable(self.__container, name))
        return skills

    def __deselect_all(self):
        for skill in self.__skills:
            if skill.is_selected():
                skill.select()

    def __sort(self):
        if self.__sorted_by_type:
            self.__sort_by_name()
            self.__sort_button.change_text("Sort by type")
            self.__sorted_by_type = False
        else:
            self.__sort_by_type()
            self.__sort_button.change_text("Sort alphabetically")
            self.__sorted_by_type = True

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


# other


class Recipe:
    """Contain data about possible 'View Paths'."""
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


if __name__ == "__main__":
    def __make_window(type_):
        import main as m
        __root = tk.Tk()
        __root.lift()
        __root.attributes('-topmost', True)
        __root.after_idle(__root.attributes, '-topmost', False)

        if type_ == "e":
            m.GuiController(__root).show_input_forms(Recipe.EXISTING_CHAR)
        else:
            m.GuiController(__root).show_input_forms(Recipe.NEW_CHAR)
        __root.mainloop()


    def __get_valid_type(prompt):
        choice = input(prompt)
        if choice == "e" or choice == "n":
            return choice

        else:
            return __get_valid_type("You need to enter either 'e' or 'n'.\n>")


    __make_window(__get_valid_type(
        "Hello. Would you like to calculate progress for an existing "
        "character [e] or a new one [n]?\n>"))
