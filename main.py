print "\n\n>Hello. I'd like to calulate a few things for you.\n"

current = int(raw_input(">What's your current character level? "))
goal = int(raw_input(">What level do you want to reach? "))

needed_xp = 12.5 * (goal ** 2 - current ** 2) + 62.5 * (goal - current)

print "\n>Please enter the current levels of the skills you would like to train.\n" \
    " You can enter up to 3 values, but you need to seperate them with commas (\",\").\n"

skills = reversed(sorted(raw_input().split(",")))
skills = [int(x) for x in skills]
while len(skills) < 3:
    skills.append(0)


#fewest skill level-ups:

min_xp = 0
min_times_leveled1 = 0
min_skill1 = skills[0]

while True:
    min_times_leveled1 += 1
    min_skill1 += 1
    min_xp += min_skill1
    if min_xp >= needed_xp and min_skill1 <= 100:
        print "\n>current Level: %d, train %dx; final level: %d\n\n" % (skills[0], min_times_leveled1, min_skill1)
        break
    elif min_skill1 == 100 and skills[1] == 0:
        min_skill1 = 15
    elif min_skill1 == 100 and skills[1] != 0:
        min_skill2 = skills[1]
        min_times_leveled2 = 0

        while True:
            min_times_leveled2 += 1
            min_skill2 += 1
            min_xp += min_skill2
            if min_xp >= needed_xp and min_skill2 <= 100:
                print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], min_times_leveled1, min_skill1)
                print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[1], min_times_leveled2, min_skill2)
                break
            elif min_skill2 == 100 and skills[2] == 0:
                min_skill2 = 15
            elif min_skill2 == 100 and skills [2] != 0:
                min_skill3 = skills[2]
                min_times_leveled3 = 0

                while True:
                    min_times_leveled3 += 1
                    min_skill3 += 1
                    min_xp += min_skill3
                    if min_xp >= needed_xp and min_skill3 <= 100:
                        print "\n\n>current Level: %d, train %dx; final level: %d" % (skills[0], min_times_leveled1, min_skill1)
                        print ">current Level: %d, train %dx; final level: %d" % (skills[1], min_times_leveled2, min_skill2)
                        print ">current Level: %d, train %dx; final level: %d\n\n" % (skills[2], min_times_leveled3, min_skill3)
                        break
                    elif min_skill3 == 100:
                        min_skill3 = 15
                break
        break

