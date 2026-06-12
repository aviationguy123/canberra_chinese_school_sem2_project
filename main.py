from player import get_max_hp, show_status
from battle import battle


# =========================
# Test Battle
# =========================

player_level = 1
player_exp = 0
player_hp = get_max_hp(player_level)

gold = 0
weapon_bonus = 0
armor_bonus = 0

floor = 1


print("Welcome to Mine Adventure!")
print("This is a one-battle test.")


show_status(
    player_level,
    player_exp,
    player_hp,
    gold,
    weapon_bonus,
    armor_bonus,
    floor
)


player_level, player_exp, player_hp, gold = battle(
    player_level,
    player_exp,
    player_hp,
    gold,
    weapon_bonus,
    armor_bonus,
    floor
)


print("\nAfter battle:")

show_status(
    player_level,
    player_exp,
    player_hp,
    gold,
    weapon_bonus,
    armor_bonus,
    floor
)