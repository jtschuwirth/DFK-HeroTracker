import requests
import json

graph_url = "https://defi-kingdoms-community-api-gateway-co06z8vi.uc.gateway.dev/graphql"
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

GrowthJson = open("data/base_growth.json")
growth_data = json.load(GrowthJson)

def findHeroes(max_price, classes, subClasses):
    query = """
        query($max_price: String, $mainClass: [String], $subClass: [String]) {
            heroes(orderBy: salePrice, where: {
                network: "dfk", 
                salePrice_not: null, 
                salePrice_lt:$max_price,
                profession: "mining",
                mainClass_in: $mainClass,
                subClass_in: $subClass
            }) {
                salePrice
                mainClass
                subClass
                strengthGrowthP
                vitalityGrowthP
                enduranceGrowthP
                strengthGrowthS
                vitalityGrowthS
                enduranceGrowthS
            }
        }
    """
    variables = {
        "max_price": str(max_price*10**18),
        "mainClass": classes,
        "subClass": subClasses
    }

    offers = []
    response = requests.post(graph_url, json={"query":query, "variables": variables}, headers=headers)
    for hero in response.json()["data"]["heroes"]:
        boosted = []
        if int(hero["strengthGrowthP"]) != growth_data[hero["mainClass"]]["str"]:
            boosted.append({"str":(int(hero["strengthGrowthP"])-growth_data[hero["mainClass"]]["str"])/100})
        if int(hero["vitalityGrowthP"]) != growth_data[hero["mainClass"]]["vit"]: 
            boosted.append({"vit":(int(hero["vitalityGrowthP"])-growth_data[hero["mainClass"]]["vit"])/100}) 
        if int(hero["enduranceGrowthP"]) != growth_data[hero["mainClass"]]["end"]:
            boosted.append({"end":(int(hero["enduranceGrowthP"])-growth_data[hero["mainClass"]]["end"])/100})

        offers.append({
            "price": int(hero["salePrice"])/10**18, 
            "class": hero["mainClass"], 
            "subclass": hero["subClass"], 
            "GrowthP":int(hero["strengthGrowthP"]+hero["vitalityGrowthP"]+hero["enduranceGrowthP"])/100,
            "GrowthS":int(hero["strengthGrowthS"]+hero["vitalityGrowthS"]+hero["enduranceGrowthS"])/100,
            "boosted": boosted,
            "t_growth": int(hero["strengthGrowthP"]+hero["vitalityGrowthP"]+hero["enduranceGrowthP"])/100+int(hero["strengthGrowthS"]+hero["vitalityGrowthS"]+hero["enduranceGrowthS"])/100
            })

    return offers