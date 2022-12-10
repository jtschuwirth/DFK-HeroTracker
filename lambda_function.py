from functions.findHeroes import findHeroes

def handler(event, context):
    return findHeroes(event["max_price"], event["classes"])

