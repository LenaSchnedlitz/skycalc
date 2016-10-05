"""Calculate optimal training strategies to reach a certain character level.

3 Versions: fast, easy and balanced.
"""


def simulate_training(original_skill_levels, current, goal, selected_from):
    """Simulate skill training and return resulting information.

    Attributes:
        original_skill_levels: dict containing current levels of used skills.
        current (int): current character level
        goal (int): goal level
        selected_from: selection method used for optimization
    """

    def done(xp):
        return xp <= 0

    def make_result_dict(original_dict):
        """Return formatted skill data dictionary.

        Attributes:
            original_dict: dict containing current levels of used skills.
        """

        def reformat(entry):
            """Reformat dictionary entry."""
            return {"START_LEVEL": original_dict[entry],
                    "TIMES_LEVELED": 0,
                    "TIMES_LEGENDARY": 0,
                    "FINAL_LEVEL": original_dict[entry]}

        return {entry: reformat(entry) for entry in original_dict}

    def total_xp(current_lvl, goal_lvl):
        """Return xp needed to advance from a current level to a goal level.

        Attributes:
            current_lvl (int): current character level
            goal_lvl (int): goal level
        """

        def level_up_xp(level):
            """Return xp needed for next level-up at a given level."""
            return (level + 3) * 25

        return sum(level_up_xp(lvl) for lvl in range(current_lvl, goal_lvl))

    # TODO: get rid of side effects
    def train(data, skill):
        """Update data as if a skill was trained."""

        def trained(skill_level):
            """Return level reached by training a skill with a given level."""
            if skill_level == 100:  # 'make legendary'
                return 16
            else:
                return skill_level + 1

        data[skill]["FINAL_LEVEL"] = trained(data[skill]["FINAL_LEVEL"])
        data[skill]["TIMES_LEVELED"] += 1

    # TODO: make 'prettier'
    needed_xp = total_xp(current, goal)
    skill_data = make_result_dict(original_skill_levels)

    while not done(needed_xp):
        selected_skill = selected_from(skill_data)
        train(skill_data, selected_skill)
        needed_xp -= skill_data[selected_skill]["FINAL_LEVEL"]
    return skill_data


def simulate_balanced_training(original_skill_levels,
                               current_level, goal_level):
    """Return skill training data for a balanced training method.

    All skills are trained equally.
    Attributes:
        original_skill_levels: dict containing current levels of used skills.
        current_level (int): current character level
        goal_level (int): goal level
    """

    def least_leveled(skill_dict):
        """Return the skill that was trained least."""
        stripped_dict = {s: skill_dict[s]["TIMES_LEVELED"] for s in skill_dict}
        return min(stripped_dict, key=stripped_dict.get)

    return simulate_training(original_skill_levels,
                             current_level, goal_level,
                             least_leveled)


def simulate_easy_training(original_skill_levels, current_level, goal_level):
    """Return skill training data for the easiest possible training.

    Always level the skill easiest to train.
    Attributes:
        original_skill_levels: dict containing current levels of used skills.
        current_level (int): current character level
        goal_level (int): goal level
    """

    def lowest(skill_dict):
        """Return the skill with the lowest final level."""
        stripped_dict = {s: skill_dict[s]["FINAL_LEVEL"] for s in skill_dict}
        return min(stripped_dict, key=stripped_dict.get)

    return simulate_training(original_skill_levels,
                             current_level, goal_level,
                             lowest)


def simulate_fast_training(original_skill_levels, current_level, goal_level):
    """Return skill training data for the fastest possible training.

    Always train the skill giving the most xp.
    Attributes:
        original_skill_levels: dict containing current levels of used skills.
        current_level (int): current character level
        goal_level (int): goal level
    """

    def highest(skill_dict):
        """Return the skill with the highest final level."""
        stripped_dict = {s: skill_dict[s]["FINAL_LEVEL"] for s in skill_dict}
        return max(stripped_dict, key=stripped_dict.get)

    return simulate_training(original_skill_levels,
                             current_level, goal_level,
                             highest)


if __name__ == "__main__":
    print(__doc__, "Not meant to be used as main.")
