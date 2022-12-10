from lambda_function import handler

classes = ["Warrior", "Knight", "Berserker", "Pirate", "Paladin", "DarkKnight"]

response = handler({"max_price":100, "classes": classes}, "")

