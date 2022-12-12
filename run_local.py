from lambda_function import handler
from colorama import Fore, Style

classes = ["Warrior", "Knight", "Berserker", "Paladin",
    "DarkKnight", "Shapeshifter", "Dragoon", "DreadKnight"]
# classes = ["Knight", "DarkKnight", "Paladin"]
subClasses = ["Warrior", "Knight", "Berserker", "Paladin", "DarkKnight",
    "Shapeshifter", "Dragoon", "DreadKnight", "Monk", "Pirate"]

request1 = handler({"max_price": 120, "classes": classes,
                   "subClasses": subClasses, "profession": "mining"}, "")

print("-----Request 1: main mining classes only-----")
for hero in request1:
    if hero["t_growth"] >= 275:
        print(Fore.GREEN + str(hero), Style.RESET_ALL)
    else:
        print(hero)

subClasses= ["Warrior", "Knight", "Berserker", "Pirate", "Paladin", "DarkKnight", "Wizard", "Monk",
    "Archer", "Ninja", "Seer", "Thief", "Priest", "Summoner", "Dragoon", "Sage", "DreadKnight"]
request2= handler({"max_price": 0, "classes": classes, "subClasses": subClasses, "profession": "mining"}, "")

print("-----Request 2: no sub classes-----")
for hero in request2:
    if hero["t_growth"] > 270:
        print(Fore.GREEN + str(hero))
        print(Style.RESET_ALL)
    else:
        print(hero)
