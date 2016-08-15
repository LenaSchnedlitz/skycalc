class DataObject:
    def __init__(self):
        self.char_levels = []
        self.selected_skills = []
        self.skill_levels = {}

    def set_char_levels(self, char_levels):
        self.char_levels = char_levels

    def set_selected_skills(self, skills):
        self.selected_skills = skills

    def set_skill_levels(self, skill_levels):
        self.skill_levels = skill_levels
