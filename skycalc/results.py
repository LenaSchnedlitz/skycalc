import tkinter as tk

import elements as elem


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

        elem.Title(self, "Results", "white").pack()
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

        self.a = elem.TabButton(sel_container, "a tab",
                                self.__fastest_tab).pack(side="left")
        self.a = elem.TabButton(sel_container, "b tab",
                                self.__easiest_tab).pack(side="left")
        self.a = elem.TabButton(sel_container, "c tab",
                                self.__balanced_tab).pack(side="left")

    def build_tab(self, title, results):
        tab = tk.Frame(self.__tab_container)
        tab.grid(row=0, column=0, sticky="nsew")
        elem.Headline(tab, title).pack()
        for skill in results:
            elem.Instruction(tab, skill + ":\nCurrent Level: " + str(
                results[skill]["start"]) + "\nGoal Level: " + str(
                results[skill]["end"]) + "\nMade legendary " + str(
                results[skill]["legendary"]) + " times\n\n").pack()
        return tab
