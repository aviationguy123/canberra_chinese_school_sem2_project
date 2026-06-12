import random

def create_monster(floor):
    if floor == 5 or floor == 10:
        monster_name = "Boss"
        monster_hp = 80 + floor * 10
        monster_attack = 15 + floor * 2
        monster_exp = 80
        monster_gold = 50
    else:
        monster_names = ["Slime", "Bat", "Goblin"]
        # TODO:
        # Choose a monster
        # Calculate HP
        # Calculate attack
        # Calculate EXP reward
        # Calculate gold reward

    return monster_name, monster_hp, monster_attack, monster_exp, monster_gold