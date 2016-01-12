print "\n\n\n\nHello. I'd like to calulate a few things for you.\n"

current = int(raw_input("What's your current character level? "))
goal = int(raw_input("What level do you want to reach? "))

needed_xp = 12.5 * (goal ** 2 - current ** 2) + 62.5 * (goal - current)

print "\nPlease enter the current levels of the skills you would like to train.\n" \
    "You can enter as many values as you like, but you need to seperate them with commas (\",\").\n"

skills = raw_input().split(",")
skills = [int(x) for x in skills]
skills = list(reversed(sorted(skills)))


gained_xp = {
    "apples" : 0,
    "pears" : 0,
    "bananas" : 0
    }

print "\n\n\n\nHere are your results:\n\n"



#fewest skill level-ups:

def apple_wrapper():
    new_levels = list(skills)
    skill_count = len(new_levels)
    times_leveled = [0] * skill_count

    def make_skills_legendary(i):
        if new_levels[i] == 100:
            new_levels[i] = 15

    def train_skills(i):
        times_leveled[i] += 1
        new_levels[i] += 1
        gained_xp["apples"] += new_levels[i]

    def print_results():
        print "\n  LOWEST NUMBER OF SKILL LEVEL-UPS - ideal for trainers:\n"
        for i in range(0, skill_count):
            print "  current Level: %d, train %dx; final level: %d" % (skills[i], times_leveled[i], new_levels[i])
        print "\n\n\n----------------------------------------------------------------\n\n"


    def apples(i):
        while True:
            make_skills_legendary(i)
            train_skills(i)
            if gained_xp["apples"] >= needed_xp:
                break
            elif new_levels[i] == 100 and i+1 < len(new_levels):
                apples(i+1)
                break

    apples(0)
    print_results()

apple_wrapper()




#least skill xp needed - easiest level-ups:
def pear_wrapper():
    new_levels = list(skills)
    skill_count = len(new_levels)
    times_leveled = [0] * skill_count

    def make_skills_legendary(i):
        if new_levels[i] == 100:
            new_levels[i] = 15

    def train_skills(i):
        times_leveled[i] += 1
        new_levels[i] += 1
        gained_xp["pears"] += new_levels[i]

    def print_results():
        print "\n  LEAST SKILL XP NEEDED - easiest level-ups:\n"
        for i in range(0, skill_count):
            print "  current Level: %d, train %dx; final level: %d" % (skills[i], times_leveled[i], new_levels[i])
        print "\n\n\n----------------------------------------------------------------\n\n"


    def pears(index):
        if index > 0:
            while new_levels[index] < new_levels[index-1] and gained_xp["pears"] < needed_xp:
                for j in range(index, skill_count):
                    make_skills_legendary(j)
                    train_skills(j)
                    if gained_xp["pears"] >= needed_xp:
                        break
            index -= 1
            pears(index)
        else:
            while gained_xp["pears"] < needed_xp:
                for j in range(skill_count):
                    make_skills_legendary(j)
                    train_skills(j)
                    if gained_xp["pears"] >= needed_xp:
                        break

    pears(skill_count-1)
    print_results()

pear_wrapper()




#balanced - realistic progress:

def banana_wrapper():

    new_levels = list(skills)
    skill_count = len(new_levels)
    times_leveled = [0] * skill_count

    def make_skills_legendary(i):
        if new_levels[i] == 100:
            new_levels[i] = 15

    def train_skills(i):
        times_leveled[i] += 1
        new_levels[i] += 1
        gained_xp["bananas"] += new_levels[i]

    def print_results():
        print "\n  BALANCED PROGRESSION - train all skills equally:\n"
        for i in range(0, skill_count):
            print "  current Level: %d, train %dx; final level: %d" % (skills[i], times_leveled[i], new_levels[i])
        print "\n\n\n----------------------------------------------------------------\n\n"


    def bananas():
        while gained_xp["bananas"] < needed_xp:
            for j in range(skill_count):
                make_skills_legendary(j)
                train_skills(j)
                if gained_xp["bananas"] >= needed_xp:
                    break

    bananas()
    print_results()

banana_wrapper()