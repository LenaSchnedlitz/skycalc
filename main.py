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

#fewest skill level-ups:

apple_xp = 0
apple_times_leveled = [0,0,0]
apple_levels = list(skills)


def make_apples_legendary(i):
    if apple_levels[i] == 100:
        apple_levels[i] = 15

def print_apples():
    if apple_times_leveled[2] != 0:
        print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], apple_times_leveled[0], apple_levels[0])
        print ">current Level: %d, train %dx; final level: %d" % (skills[1], apple_times_leveled[1], apple_levels[1])
        print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[2], apple_times_leveled[2], apple_levels[2])
    elif apple_times_leveled[1] != 0:
        print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], apple_times_leveled[0], apple_levels[0])
        print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[1], apple_times_leveled[1], apple_levels[1])
    else:
        print "\n\n>current Level: %d, train %dx; final level: %d\n\n" % (skills[0], apple_times_leveled[0], apple_levels[0])

while True:
    make_apples_legendary(0)
    apple_times_leveled[0] += 1
    apple_levels[0] += 1
    apple_xp += apple_levels[0]
    if apple_xp >= needed_xp:
        print_apples()
        break
    elif apple_levels[0] == 100 and skills[1] != 0:

        while True:
            make_apples_legendary(1)
            apple_times_leveled[1] += 1
            apple_levels[1] += 1
            apple_xp += apple_levels[1]
            if apple_xp >= needed_xp:
                print_apples()
                break
            elif apple_levels[1] == 100 and skills[2] != 0:

                while True:
                    make_apples_legendary(2)
                    apple_times_leveled[2] += 1
                    apple_levels[2] += 1
                    apple_xp += apple_levels[2]
                    if apple_xp >= needed_xp:
                        print_apples()
                        break
                break
        break



#least skill xp needed - easiest level-ups:

pear_xp = 0
pear_times_leveled = [0,0,0]
reversed_skills = list(reversed(skills))
pear_levels = list(reversed_skills)


def make_pears_legendary(i):
    if pear_levels[i] == 100:
        pear_levels[i] = 15

def print_pears():
    if reversed_skills[0] != 0:
        print "\n\n>current Level: %d, train %dx; final level: %d" % (reversed_skills[2], pear_times_leveled[2], pear_levels[2])
        print ">current Level: %d, train %dx; final level: %d" % (reversed_skills[1], pear_times_leveled[1], pear_levels[1])
        print ">current Level: %d, train %dx; final level: %d\n\n" % (reversed_skills[0], pear_times_leveled[0], pear_levels[0])
    elif reversed_skills[1] != 0:
        print "\n\n>current Level: %d, train %dx; final level: %d" % (reversed_skills[2], pear_times_leveled[2], pear_levels[2])
        print ">current Level: %d, train %dx; final level: %d\n\n" % (reversed_skills[1], pear_times_leveled[1], pear_levels[1])
    else:
        print "\n\n>current Level: %d, train %dx; final level: %d\n\n" % (reversed_skills[2], pear_times_leveled[2], pear_levels[2])

if reversed_skills[0] != 0:

    while True:
        make_pears_legendary(0)
        pear_times_leveled[0] += 1
        pear_levels[0] += 1
        pear_xp += pear_levels[0]
        if pear_xp >= needed_xp:
            print_pears()
            break
        elif pear_levels[0] >= pear_levels[1]:

            while True:
                make_pears_legendary(1)
                pear_times_leveled[1] += 1
                pear_levels[1] += 1
                pear_xp += pear_levels[1]
                if pear_xp >= needed_xp:
                    print_pears()
                    break

                elif pear_levels[0] == 100:
                    pear_levels[0] = 15
                pear_times_leveled[0] += 1
                pear_levels[0] += 1
                pear_xp += pear_levels[0]
                if pear_xp >= needed_xp:
                    print_pears()
                    break
                
                elif pear_levels [0] >= pear_levels[2]:

                    while True:
                        make_pears_legendary(2)
                        pear_times_leveled[2] += 1
                        pear_levels[2] += 1
                        pear_xp += pear_levels[2]
                        if pear_xp >= needed_xp:
                            print_pears()
                            break

                        elif pear_levels[1] == 100:
                            pear_levels[1] = 15
                        pear_times_leveled[1] += 1
                        pear_levels[1] += 1
                        pear_xp += pear_levels[1]
                        if pear_xp >= needed_xp:
                            print_pears()
                            break

                        elif pear_levels[0] == 100:
                            pear_levels[0] = 15
                        pear_times_leveled[0] += 1
                        pear_levels[0] += 1
                        pear_xp += pear_levels[0]
                        if pear_xp >= needed_xp:
                            print_pears()
                            break
                    break
            break

elif reversed_skills[0] == 0 and reversed_skills[1] != 0:

    while True:
        make_pears_legendary(1)
        pear_times_leveled[1] += 1
        pear_levels[1] += 1
        pear_xp += pear_levels[1]
        if pear_xp >= needed_xp:
            print_pears()
            break
        elif pear_levels[1] >= pear_levels[2]:

            while True:
                make_pears_legendary(2)
                pear_times_leveled[2] += 1
                pear_levels[2] += 1
                pear_xp += pear_levels[2]
                if pear_xp >= needed_xp:
                    print_pears()
                    break

                elif pear_levels[1] == 100:
                    pear_levels[1] = 15
                pear_times_leveled[1] += 1
                pear_levels[1] += 1
                pear_xp += pear_levels[1]
                if pear_xp >= needed_xp:
                    print_pears()
                    break
            break

else:

    while True:
        make_pears_legendary(2)
        pear_times_leveled[2] += 1
        pear_levels[2] += 1
        pear_xp += pear_levels[2]
        if pear_xp >= needed_xp and pear_levels[2] <= 100:
            print_pears()
            break


#balanced:

banana_xp = 0
banana_times_leveled = [0,0,0]
banana_levels = list(skills)

def make_bananas_legendary(i):
    if banana_levels[i] == 100:
        banana_levels[i] = 15

def print_bananas():
    if banana_times_leveled[2] != 0:
        print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], banana_times_leveled[0], banana_levels[0])
        print ">current Level: %d, train %dx; final level: %d" % (skills[1], banana_times_leveled[1], banana_levels[1])
        print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[2], banana_times_leveled[2], banana_levels[2])
    elif banana_times_leveled[1] != 0:
        print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], banana_times_leveled[0], banana_levels[0])
        print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[1], banana_times_leveled[1], banana_levels[1])
    else:
        print "\n\n>current Level: %d, train %dx; final level: %d\n\n" % (skills[0], banana_times_leveled[0], banana_levels[0])

if skills[1] != 0 and skills[2] != 0:

    while True:
        make_bananas_legendary(0)
        banana_times_leveled[0] += 1
        banana_levels[0] += 1
        banana_xp += banana_levels[0]
        if banana_xp >= needed_xp:
            print_bananas()
            break

        elif banana_levels[1] == 100:
            banana_levels[1] = 15
        banana_times_leveled[1] += 1
        banana_levels[1] += 1
        banana_xp += banana_levels[1]
        if banana_xp >= needed_xp:
            print_bananas()
            break

        elif banana_levels[2] == 100:
            banana_levels[2] = 15
        banana_times_leveled[2] += 1
        banana_levels[2] += 1
        banana_xp += banana_levels[2]
        if banana_xp >= needed_xp:
            print_bananas()
            break

elif skills[1] != 0:

    while True:
        make_bananas_legendary(0)
        banana_times_leveled[0] += 1
        banana_levels[0] += 1
        banana_xp += banana_levels[0]
        if banana_xp >= needed_xp:
            print_bananas()
            break

        elif banana_levels[1] == 100:
            banana_levels[1] = 15
        banana_times_leveled[1] += 1
        banana_levels[1] += 1
        banana_xp += banana_levels[1]
        if banana_xp >= needed_xp:
            print_bananas()
            break

else:

    while True:
        make_bananas_legendary(0)
        banana_times_leveled[0] += 1
        banana_levels[0] += 1
        banana_xp += banana_levels[0]
        if banana_xp >= needed_xp:
            print_bananas()
            break