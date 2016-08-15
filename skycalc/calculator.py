class DataObject:
    def __init__(self):
        self.race = ""
        self.char_levels = []
        self.selected_skills = []
        self.skill_levels = {}

    def set_race(self, race):
        self.race = race

    def set_char_levels(self, char_levels):
        self.char_levels = char_levels

    def set_selected_skills(self, skills):
        self.selected_skills = skills

    def set_skill_levels(self, skill_levels):
        self.skill_levels = skill_levels

    def generate_selected_skill_levels(self):
        skill_info = self.get_race_skills_info()[self.race]
        self.skill_levels = {}
        for skill in self.selected_skills:
            self.skill_levels[skill] = skill_info[skill]

    @staticmethod
    def get_race_skills_info():
        return {
            "Breton": {
                "Illusion": 20,
                "Conjuration": 25,
                "Destruction": 15,
                "Restoration": 20,
                "Alteration": 20,
                "Enchanting": 15,
                "Smithing": 15,
                "Heavy Armor": 15,
                "Block": 15,
                "Two-handed": 15,
                "One-handed": 15,
                "Archery": 15,
                "Light Armor": 15,
                "Sneak": 15,
                "Lockpicking": 15,
                "Pickpocket": 15,
                "Speech": 20,
                "Alchemy": 20,
            },
            "Nord": {
                "Illusion": 15,
                "Conjuration": 15,
                "Destruction": 15,
                "Restoration": 15,
                "Alteration": 15,
                "Enchanting": 15,
                "Smithing": 20,
                "Heavy Armor": 15,
                "Block": 20,
                "Two-handed": 25,
                "One-handed": 20,
                "Archery": 15,
                "Light Armor": 20,
                "Sneak": 15,
                "Lockpicking": 15,
                "Pickpocket": 15,
                "Speech": 20,
                "Alchemy": 15,
            },
            "Imperial": {
                "Illusion": 15,
                "Conjuration": 15,
                "Destruction": 20,
                "Restoration": 25,
                "Alteration": 15,
                "Enchanting": 20,
                "Smithing": 15,
                "Heavy Armor": 20,
                "Block": 20,
                "Two-handed": 15,
                "One-handed": 20,
                "Archery": 15,
                "Light Armor": 15,
                "Sneak": 15,
                "Lockpicking": 15,
                "Pickpocket": 15,
                "Speech": 15,
                "Alchemy": 15,
            },
            "Redguard": {
                "Illusion": 15,
                "Conjuration": 15,
                "Destruction": 20,
                "Restoration": 15,
                "Alteration": 20,
                "Enchanting": 15,
                "Smithing": 20,
                "Heavy Armor": 15,
                "Block": 20,
                "Two-handed": 15,
                "One-handed": 25,
                "Archery": 20,
                "Light Armor": 15,
                "Sneak": 15,
                "Lockpicking": 15,
                "Pickpocket": 15,
                "Speech": 15,
                "Alchemy": 15,
            },
            "Altmer": {
                "Illusion": 25,
                "Conjuration": 20,
                "Destruction": 20,
                "Restoration": 20,
                "Alteration": 20,
                "Enchanting": 20,
                "Smithing": 15,
                "Heavy Armor": 15,
                "Block": 15,
                "Two-handed": 15,
                "One-handed": 15,
                "Archery": 15,
                "Light Armor": 15,
                "Sneak": 15,
                "Lockpicking": 15,
                "Pickpocket": 15,
                "Speech": 15,
                "Alchemy": 15,
            },
            "Bosmer": {
                "Illusion": 15,
                "Conjuration": 15,
                "Destruction": 15,
                "Restoration": 15,
                "Alteration": 15,
                "Enchanting": 15,
                "Smithing": 15,
                "Heavy Armor": 15,
                "Block": 15,
                "Two-handed": 15,
                "One-handed": 15,
                "Archery": 25,
                "Light Armor": 20,
                "Sneak": 20,
                "Lockpicking": 20,
                "Pickpocket": 20,
                "Speech": 15,
                "Alchemy": 20,
            },
            "Dunmer": {
                "Illusion": 20,
                "Conjuration": 15,
                "Destruction": 25,
                "Restoration": 15,
                "Alteration": 20,
                "Enchanting": 15,
                "Smithing": 15,
                "Heavy Armor": 15,
                "Block": 15,
                "Two-handed": 15,
                "One-handed": 15,
                "Archery": 15,
                "Light Armor": 20,
                "Sneak": 20,
                "Lockpicking": 15,
                "Pickpocket": 15,
                "Speech": 15,
                "Alchemy": 20,
            },
            "Orc": {
                "Illusion": 15,
                "Conjuration": 15,
                "Destruction": 15,
                "Restoration": 15,
                "Alteration": 15,
                "Enchanting": 20,
                "Smithing": 20,
                "Heavy Armor": 25,
                "Block": 20,
                "Two-handed": 20,
                "One-handed": 20,
                "Archery": 15,
                "Light Armor": 15,
                "Sneak": 15,
                "Lockpicking": 15,
                "Pickpocket": 15,
                "Speech": 15,
                "Alchemy": 15,
            },
            "Argonian": {
                "Illusion": 15,
                "Conjuration": 15,
                "Destruction": 15,
                "Restoration": 20,
                "Alteration": 20,
                "Enchanting": 15,
                "Smithing": 15,
                "Heavy Armor": 15,
                "Block": 15,
                "Two-handed": 15,
                "One-handed": 15,
                "Archery": 15,
                "Light Armor": 20,
                "Sneak": 20,
                "Lockpicking": 25,
                "Pickpocket": 20,
                "Speech": 15,
                "Alchemy": 15,
            },
            "Khajiit": {
                "Illusion": 15,
                "Conjuration": 15,
                "Destruction": 15,
                "Restoration": 15,
                "Alteration": 15,
                "Enchanting": 15,
                "Smithing": 15,
                "Heavy Armor": 15,
                "Block": 15,
                "Two-handed": 15,
                "One-handed": 20,
                "Archery": 20,
                "Light Armor": 15,
                "Sneak": 25,
                "Lockpicking": 20,
                "Pickpocket": 20,
                "Speech": 15,
                "Alchemy": 20,
            }
        }


class Calculator:
    def __init__(self, data: DataObject):
        self.current_xp = data.char_levels[0]
        self.goal_xp = data.char_levels[1]
        self.needed_xp = self.calculate_needed_xp()
        self.current_skill_levels = data.skill_levels

    def calculate_needed_xp(self):
        a = 12.5 * (self.goal_xp ** 2 - self.current_xp ** 2)
        b = 62.5 * (self.goal_xp - self.current_xp)
        return a + b

    def get_fastest_results(self):
        still_needed = self.needed_xp
        end_levels = self.current_skill_levels.copy()
        times_legendary = {}
        for skill in end_levels:
            times_legendary[skill] = 0

        while still_needed > 0:
            selected = max(end_levels, key=lambda key: end_levels[key])
            print(selected)
            training_result = self.train_skill(end_levels[selected])
            end_levels[selected] = training_result
            if training_result == 15:
                times_legendary[selected] += 1
                still_needed -= 100
            else:
                still_needed -= training_result
        return end_levels

    def get_easiest_results(self):
        still_needed = self.needed_xp
        end_levels = self.current_skill_levels.copy()
        times_legendary = {}
        for skill in end_levels:
            times_legendary[skill] = 0

        while still_needed > 0:
            selected = min(end_levels, key=lambda key: end_levels[key])
            print(selected)
            training_result = self.train_skill(end_levels[selected])
            end_levels[selected] = training_result
            if training_result == 15:
                times_legendary[selected] += 1
                still_needed -= 100
            else:
                still_needed -= training_result
        return end_levels

    def get_balanced_results(self):
        still_needed = self.needed_xp
        end_levels = self.current_skill_levels.copy()
        times_legendary = {}
        for skill in end_levels:
            times_legendary[skill] = 0

        while True:
            for skill in end_levels:
                print(skill)
                training_result = self.train_skill(end_levels[skill])
                end_levels[skill] = training_result
                if training_result == 15:
                    times_legendary[skill] += 1
                    still_needed -= 100
                else:
                    still_needed -= training_result
                if still_needed <= 0:
                    break
        return end_levels

    def train_skill(self, level):
        level += 1
        if level == 100:
            level = 15
        return level
