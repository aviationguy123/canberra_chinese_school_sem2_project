import random
from player import get_attack, add_exp
from monster import create_monster


def battle(level, hp, weapon_bonus, armor_bonus, floor, exp, gold):
    monster_name, monster_hp, monster_attack, monster_exp, monster_gold = create_monster(floor)

    print("A", monster_name, "appears!")
    print(monster_name, "HP:", monster_hp)

    while hp > 0 and monster_hp > 0:
        # TODO:
        # Get player's attack
        # Calculate damage
        # Reduce monster HP
        # Print battle messages
        # Check if monster is defeated

        # TODO:
        # Calculate enemy damage
        # Reduce player HP
        # Print battle messages
        pass

    # TODO:
    # If player wins:
    #     Get gold
    #     Gain EXP

    # Return updated values
    pass