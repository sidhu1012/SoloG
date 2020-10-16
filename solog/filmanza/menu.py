from solog.filmanza.gameplay import hollywood_medium, bollywood_medium, bollywood_hard, hollywood_hard, hollywood_easy, bollywood_easy

def game_level():
    print("\t\t\tSelect Difficulty")
    print("Press '1' for Easy")
    print("Press '2' for Medium")
    print("Press '3' for Hard")
    lvl = int(input())
    val_level= [1,2,3]
    if lvl not in val_level:
        print('Wrong input')
        game_level()
    return lvl

def game_type():
    print("Press '1' for Bollywood ")
    print("Press '2' for Hollywood")
    choice_type = int(input())
    val_lvl = [1,2]
    if choice_type not in val_lvl:
        print('Wrong input')
        game_level()
    return choice_type

def menu():
    c1, c2 = game_type(), game_level()
    if c1 == 1:
        if c2 == 1:
            bollywood_easy()
        if c2 == 2:
            bollywood_medium()
        if c2 == 3:
            bollywood_hard()
    if c1 == 2:
        if c2 == 1:
            hollywood_easy()
        if c2 == 2:
            hollywood_medium()
        if c2 == 3:
            hollywood_hard()
