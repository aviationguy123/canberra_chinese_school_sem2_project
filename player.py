def get_max_hp(level):
    return 80 + level * 20


def get_attack(level, weapon_bonus):
    return 10 + level * 5 + weapon_bonus


def show_player(level, exp, hp, gold, weapon_bonus, armor_bonus, floor):
    print("\n===== Player Status =====")
    print("Floor:", floor)
    print("Level:", level)
    print("EXP:", exp, "/ 100")
    print("HP:", hp, "/", get_max_hp(level))
    print("Gold:", gold)
    print("Attack:", get_attack(level, weapon_bonus))
    print("Armor:", armor_bonus)
    print("=========================")


def add_exp(level, exp, gained_exp):
    # TODO:
    # Print gained EXP
    # Add EXP
    # Level up when EXP >= 100
    # Return level and exp
    pass