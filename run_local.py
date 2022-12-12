from lambda_function import handler

classes = ["Warrior", "Knight", "Berserker", "Paladin", "DarkKnight", "Shapeshifter", "Dragoon", "DreadKnight"]
#classes = ["Knight", "DarkKnight", "Paladin"]
subClasses =  ["Warrior", "Knight", "Berserker", "Paladin", "DarkKnight", "Shapeshifter", "Dragoon", "DreadKnight", "Monk", "Pirate"]

request1 = handler({"max_price":120, "classes": classes, "subClasses": subClasses}, "")

print("-----Request 1: main mining classes only-----")
for hero in request1:
    print(hero)

subClasses =  ["Warrior", "Knight", "Berserker", "Pirate", "Paladin", "DarkKnight", "Wizard", "Monk", "Archer", "Ninja", "Seer", "Thief", "Priest", "Summoner", "Dragoon", "Sage", "DreadKnight"]
request2 = handler({"max_price":0, "classes": classes, "subClasses": subClasses}, "")

print("-----Request 2: no sub classes-----")
for hero in request2:
   print(hero)

