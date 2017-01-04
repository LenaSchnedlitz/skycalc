class GameData:
    """Information about Skyrim."""

    NEW_CHAR_LEVEL_INFO = {
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

    RACE_NAMES = ("Breton", "Nord", "Imperial", "Redguard",
                  "Altmer", "Bosmer", "Dunmer", "Orc",
                  "Argonian", "Khajiit")

    RACE_TYPES = ("HUMAN", "MER", "BEAST")

    SKILL_NAMES = ("Illusion", "Conjuration", "Destruction",
                   "Restoration", "Alteration", "Enchanting",

                   "Smithing", "Heavy Armor", "Block",
                   "Two-handed", "One-handed", "Archery",

                   "Light Armor", "Sneak", "Lockpicking",
                   "Pickpocket", "Speech", "Alchemy")

    SKILL_TYPES = ("MAGIC", "COMBAT", "STEALTH")

    PLAY_STYLES = {
        "Crafty Merchant": ("Speech", "Alchemy", "Smithing", "Enchanting"),
        "Basic Criminal": ("Sneak", "Lockpicking", "Pickpocket")
    }


class ValidationException(Exception):
    """Exception with 'problem list'.

    Attributes:
        message (str): error message
        problems (list): list of all errors
    """

    def __init__(self, message, problems=None):
        super(ValidationException, self).__init__(message)
        self.__problems = problems

    def get_problems(self):
        return self.__problems


class InputValidator:
    """Check if given input is valid (= could be Skyrim game data)."""

    @staticmethod
    def are_valid_skills(skills):
        for skill in skills:
            if skill not in GameData.SKILL_NAMES:
                return False
        return True

    @staticmethod
    def is_valid_char_level(level):
        try:
            level = int(level)
        except ValueError:
            return False

        return 0 < level < 300  # arbitrary cap, >= 252

    @staticmethod
    def is_valid_level_combination(now, goal):
        try:
            now = int(now)
            goal = int(goal)
        except ValueError:
            return False

        return now < goal

    @staticmethod
    def is_valid_race(race):
        return race in GameData.RACE_NAMES

    @staticmethod
    def is_valid_selection(selection):
        return isinstance(selection, list) and len(selection) > 0

    @staticmethod
    def is_valid_skill_dictionary(dictionary):
        if not isinstance(dictionary, dict) or len(dictionary) == 0:
            return False

        return InputValidator.are_valid_skills(dictionary)

    @staticmethod
    def is_valid_skill_level(level):
        try:
            level = int(level)
        except ValueError:
            return False

        return 15 <= level <= 100


class InputCollector:
    """Collect valid user input.

    Validation is handled by the validator passed to the constructor.
    Attributes:
        validator: any validator class/object.
    """

    def __init__(self, validator=InputValidator):
        self.__validator = validator

        self.__goal = None
        self.__now = None
        self.__race = None
        self.__selected_skills = None
        self.__skill_levels = None
        self.__template = None

    def get_char_levels(self):
        return self.__now, self.__goal

    def get_race(self):
        return self.__race

    def get_selected_skills(self):
        return self.__selected_skills

    def get_skill_levels(self):
        if self.__skill_levels is None:
            self.__set_default_skill_levels()
        return self.__skill_levels

    def get_template(self):
        temp = self.__template
        if temp is None:
            return ()
        if temp in GameData.PLAY_STYLES:
            return GameData.PLAY_STYLES[temp]
        return [k for k, v in GameData.NEW_CHAR_LEVEL_INFO[temp].items() if
                v > 15]

    def has_template(self):
        return self.__template is not None

    def set_char_levels(self, goal, now=1):
        valid_goal = self.__validator.is_valid_char_level(goal)
        valid_now = now == 1 or self.__validator.is_valid_char_level(now)

        if valid_goal and valid_now:
            goal = int(goal)
            now = int(now)
            if self.__validator.is_valid_level_combination(goal=goal, now=now):
                self.__goal = goal
                self.__now = now
            else:
                raise ValidationException(
                    "Your goal level must be higher than your current level.",
                    ["Goal", "Now"])
        elif valid_goal:
            raise ValidationException("Please enter a valid character level.",
                                      ["Now"])
        elif valid_now:
            raise ValidationException("Please enter a valid goal level.",
                                      ["Goal"])
        else:
            raise ValidationException("Please enter valid levels.",
                                      ["Goal", "Now"])

    def set_race(self, race):
        if self.__validator.is_valid_race(race):
            self.__race = race
        else:
            raise ValidationException("Please select a race.")

    def set_selected_skills(self, skills):
        if self.__validator.is_valid_selection(skills):
            if self.__validator.are_valid_skills(skills):
                self.__selected_skills = skills
            else:
                raise ValidationException("Those skills are invalid.")
        else:
            raise ValidationException("You need to select at least one skill.")

    def set_skill_levels(self, skill_levels):
        if not self.__validator.is_valid_skill_dictionary(skill_levels):
            raise ValidationException("Something went wrong.")

        invalid_skills = []
        for s in skill_levels:
            if not self.__validator.is_valid_skill_level(skill_levels[s]):
                invalid_skills.append(s)
        if not invalid_skills:
            self.__skill_levels = {skill: int(skill_levels[skill]) for skill in
                                   skill_levels}
        else:
            raise ValidationException(
                "Skill levels can range from 15 to 100.", invalid_skills)

    def set_template(self, template):
        self.__template = template  # no validation!

    def __set_default_skill_levels(self):
        default_levels = GameData.NEW_CHAR_LEVEL_INFO[self.__race]
        self.__skill_levels = {skill: default_levels[skill] for skill in
                               self.__selected_skills}
