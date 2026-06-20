import random
from player import get_max_hp


shop_items = {
    "small potion": {"type": "potion", "price": 20, "effect": 30, "level": 1},
    "iron sword": {"type": "weapon", "price": 50, "effect": 5, "level": 1},
    "iron armor": {"type": "armor", "price": 50, "effect": 3, "level": 1},

    "big potion": {"type": "potion", "price": 40, "effect": 60, "level": 3},
    "steel sword": {"type": "weapon", "price": 100, "effect": 12, "level": 3},
    "steel armor": {"type": "armor", "price": 100, "effect": 8, "level": 3},

    "super potion": {"type": "potion", "price": 80, "effect": 120, "level": 5},
    "magic sword": {"type": "weapon", "price": 200, "effect": 25, "level": 5},
    "magic armor": {"type": "armor", "price": 200, "effect": 18, "level": 5},
}


def get_available_items(level):
    available_items = []

    for item_name in shop_items:
        item = shop_items[item_name]

        if level >= item["level"]:
            available_items.append(item_name)

    return available_items


def create_shop_list(level):
    available_items = get_available_items(level)

    if len(available_items) <= 3:
        return available_items

    return random.sample(available_items, 3)


def show_shop(shop_list):
    print("\n===== Shop =====")

    for i in range(len(shop_list)):
        item_name = shop_list[i]
        item = shop_items[item_name]

        print(i + 1, ".",item_name)
        print("  Price:",item["price"])
        print("   Type:",item["type"])
        print("   Effect:",item["effect"])
    # Print the shop title
    # Use a loop to show each item
    # Print price, type and effect
    print("0. Leave shop")

    pass


def buy_item(item_name, hp, gold, weapon_bonus, armor_bonus, level):
    # TODO:
    # Check if player has enough gold
    # Spend gold
    # If item is a potion:
    #     Heal HP
    # If item is a weapon:
    #     Increase attack
    # If item is armor:
    #     Increase armor
    # Return updated values

    pass


def shop(hp, gold, weapon_bonus, armor_bonus, level):
    # TODO:
    # Create a shop list
    # Repeat until player leaves
    # Show the shop
    # Get player's choice
    # If choice is 0:
    #     Leave the shop
    # If choice is 1, 2 or 3:
    #     Buy the item
    #     Remove the item from the shop list
    # Stop when the shop is empty
    # Return updated values

    pass