EXZ4;/8LIimport random CT, 5X.   CGHK N3M
from player import get_attack, add_exp
from monster import create_monster


def battle(level, hp, weapon_bonus, armor_bonus, floor, exp, gold):
    monster_name, monster_hp, monster_attack, monster_exp, monster_gold = create_monster(floor)

    print("A", monster_name, "appears!")
    print(monster_name, "HP:", monster_hp)

    whil/e hp > 0 and monster_hp > 0:
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
        enemy_attack_damage = random.randint(monster_attack - 2,monster_attack + 2) - armor_bonus
        if enemy_attack < 0:
            print("you are defeated by the monster")
        
        pass

    # TODO:
    # If player wins:
    #     Get gold
    #     Gain EXP

    # Return updated values
    pass