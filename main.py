print "\n\n>Hello. I'd like to calulate a few things for you.\n"

current = int(raw_input(">What's your current character level? "))
goal = int(raw_input(">What level do you want to reach? "))

needed_xp = 12.5 * (goal ** 2 - current ** 2) + 62.5 * (goal - current)

print "\n>Please enter the current levels of the skills you would like to train.\n" \
    " You can enter up to 3 values, but you need to seperate them with commas (\",\").\n"

skills = raw_input().split(",")
skills = [int(x) for x in skills]
skills = list(reversed(sorted(skills)))
while len(skills) < 3:
    skills.append(0)


gained_xp = {
    "apples" : 0,
    "pears" : 0,
    "bananas" : 0
    }


#fewest skill level-ups:


def apple_wrapper():
    times_leveled = [0,0,0]
    new_levels = list(skills)

    def make_skills_legendary(i):
        if new_levels[i] == 100:
            new_levels[i] = 15

    def train_skills(i):
        times_leveled[i] += 1
        new_levels[i] += 1
        gained_xp["apples"] += new_levels[i]

    def print_results():
        if times_leveled[2] != 0:
            print "\n\n>current Level: %d, trainl %dx; final level: %d" % (skills[0], times_leveled[0], new_levels[0])
            print ">current Level: %d, train %dx; final level: %d" % (skills[1], times_leveled[1], new_levels[1])
            print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[2], times_leveled[2], new_levels[2])
        elif times_leveled[1] != 0:
            print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], times_leveled[0], new_levels[0])
            print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[1], times_leveled[1], new_levels[1])
        else:
            print "\n\n>current Level: %d, train %dx; final level: %d\n\n" % (skills[0], times_leveled[0], new_levels[0])


    def apples(i):
        while True:
            make_skills_legendary(i)
            train_skills(i)
            if gained_xp["apples"] >= needed_xp:
                break
            elif new_levels[i] == 100 and i+1 < len(skills):
                apples(i+1)
                break

    apples(0)
    print_results()

apple_wrapper()




#least skill xp needed - easiest level-ups:
def pear_wrapper():
    times_leveled = [0,0,0]
    new_levels = list(skills)
    length = len(list(skills))

    def make_skills_legendary(i):
        if new_levels[i] == 100:
            new_levels[i] = 15

    def train_skills(i):
        times_leveled[i] += 1
        new_levels[i] += 1
        gained_xp["pears"] += new_levels[i]

    def print_pears():
        if times_leveled[2] != 0:
            print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], times_leveled[0], new_levels[0])
            print ">current Level: %d, train %dx; final level: %d" % (skills[1], times_leveled[1], new_levels[1])
            print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[2], times_leveled[2], new_levels[2])
        elif times_leveled[1] != 0:
            print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], times_leveled[0], new_levels[0])
            print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[1], times_leveled[1], new_levels[1])
        else:
            print "\n\n>current Level: %d, train %dx; final level: %d\n\n" % (skills[0], times_leveled[0], new_levels[0])

    def pears(index):
        if index > 0:
            while new_levels[index] < new_levels[index-1] and gained_xp["pears"] < needed_xp:
                for j in range(index, length):
                    make_skills_legendary(j)
                    train_skills(j)
                    if gained_xp["pears"] >= needed_xp:
                        break
            index -= 1
            pears(index)
        else:
            while gained_xp["pears"] < needed_xp:
                for j in range(length):
                    make_skills_legendary(j)
                    train_skills(j)
                    if gained_xp["pears"] >= needed_xp:
                        break

    pears(length-1)
    print_pears()

pear_wrapper()


#balanced - realistic progress:


def banana_wrapper():
    times_leveled = [0,0,0]
    new_levels = list(skills)

    def make_skills_legendary(i):
        if new_levels[i] == 100:
            new_levels[i] = 15

    def train_skills(i):
        times_leveled[i] += 1
        new_levels[i] += 1
        gained_xp["bananas"] += new_levels[i]

    def print_bananas():
        if times_leveled[2] != 0:
            print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], times_leveled[0], new_levels[0])
            print ">current Level: %d, train %dx; final level: %d" % (skills[1], times_leveled[1], new_levels[1])
            print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[2], times_leveled[2], new_levels[2])
        elif times_leveled[1] != 0:
            print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], times_leveled[0], new_levels[0])
            print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[1], times_leveled[1], new_levels[1])
        else:
            print "\n\n>current Level: %d, train %dx; final level: %d\n\n" % (skills[0], times_leveled[0], new_levels[0])


    def bananas():
        while gained_xp["bananas"] < needed_xp:
            for j in range(3):
                make_skills_legendary(j)
                train_skills(j)
                if gained_xp["bananas"] >= needed_xp:
                    break

    bananas()
    print_bananas()

banana_wrapper()