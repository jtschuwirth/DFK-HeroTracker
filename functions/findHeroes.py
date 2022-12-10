import requests

graph_url = "https://defi-kingdoms-community-api-gateway-co06z8vi.uc.gateway.dev/graphql"
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}



def findHeroes(max_price, classes):
    query = """
        query($max_price: String) {
            saleAuctions(where: {open: true, startingPrice_lt:$max_price}) {
                startingPrice
                tokenId {
                    mainClass
                    subClass
                    profession
                    strengthGrowthP
                    vitalityGrowthP
                    enduranceGrowthP
                    strengthGrowthS
                    vitalityGrowthS
                    enduranceGrowthS
                    network
                }   
            }
        }
    """
    variables = {
        "max_price": str(max_price*10**18)
    }

    response = requests.post(graph_url, json={"query":query, "variables": variables}, headers=headers)
    for hero in response.json()["data"]["saleAuctions"]:
        if hero["tokenId"]["profession"] != "mining": continue
        if hero["tokenId"]["mainClass"] not in classes or hero["tokenId"]["subClass"] not in classes: continue
        if hero["tokenId"]["network"] != "dfk": continue
        print(int(hero["startingPrice"])/10**18, hero["tokenId"]["mainClass"], hero["tokenId"]["subClass"], hero["tokenId"]["profession"], hero["tokenId"]["network"])