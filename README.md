# Mine Adventure

Welcome to **Mine Adventure**, a simple text-based RPG game made with Python!

In this project, you will build your own adventure game step by step.

Fight monsters, earn gold, buy equipment, and survive all 10 floors!

---

# Project Files

| File         | Description                   |
| ------------ | ----------------------------- |
| `main.py`    | Main game loop                |
| `player.py`  | Player stats and level system |
| `monster.py` | Monster generation            |
| `battle.py`  | Battle system                 |
| `shop.py`    | Shop system                   |

---

# Lesson 1 - Battle System

In this lesson, you will complete:

### player.py

* Gain EXP after winning a battle
* Level up when EXP reaches 100

### monster.py

Create normal monsters:

* Slime
* Bat
* Goblin

Different floors should create stronger monsters and better rewards.

### battle.py

Create the battle system:

* Player attacks the monster
* Monster attacks the player
* Repeat until someone loses
* Gain gold and EXP after winning

After Lesson 1, you should be able to fight one monster.

---

# Lesson 2 - Shop System

In this lesson, you will complete:

### Show the shop

Display:

* Item name
* Price
* Type
* Effect

### Buy items

Different items have different effects:

* Potions heal HP
* Weapons increase attack
* Armor increases defense

### Shop loop

Players can:

* Buy items
* Leave the shop
* Continue shopping until the shop is empty

---

# Lesson 3 - Main Game

In this lesson, you will connect everything together.

The game should:

1. Show player status.
2. Start a battle.
3. Check if the player survives.
4. Open the shop.
5. Move to the next floor.
6. Repeat until floor 10.

If HP becomes 0, the game ends.

If you clear floor 10, you win!

---

# Python Concepts Used

This project uses:

* Variables
* Functions
* Parameters and return values
* Lists
* Dictionaries
* If statements
* Loops (`for` and `while`)
* Random numbers
* Multiple Python files
* Importing functions

---

# Goal

By the end of this project, you will have created your own RPG game with:

* Monsters
* Battles
* Levels
* Gold
* Shops
* Equipment
* Boss fights

Good luck, adventurer!
