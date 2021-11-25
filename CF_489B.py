def main():
    number_of_boy = input()
    array_boy_skill = input()
    number_of_girl = input()
    array_girl_skill = input()

    array_boy_skill = array_boy_skill.split()
    array_boy_skill = list(map(int, array_boy_skill))

    array_girl_skill = array_girl_skill.split()
    array_girl_skill = list(map(int, array_girl_skill))

    array_boy_skill.sort()
    array_girl_skill.sort()
    pair_ascending = 0
    for boy_skill in array_boy_skill:
        for girl_skill in array_girl_skill:

            if girl_skill == boy_skill-1:
                partner = girl_skill
                index_pop = array_girl_skill.index(partner)
                array_girl_skill.pop(index_pop)
                pair_ascending += 1
                break

            elif girl_skill == boy_skill:
                partner = girl_skill
                index_pop = array_girl_skill.index(partner)
                array_girl_skill.pop(index_pop)
                pair_ascending += 1
                break

            elif girl_skill == boy_skill+1:
                partner = girl_skill
                index_pop = array_girl_skill.index(partner)
                array_girl_skill.pop(index_pop)
                pair_ascending += 1
                break

    print(pair_ascending)

if __name__ == '__main__':
    main()
