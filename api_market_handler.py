import json
from urllib.request import urlopen

api_key = "x-api-key=9w3MIVAGdu84n6Db"
api_url = "https://tarkov-market.com/api/v1/"

release_state = False

if (release_state):
    print("Release State = " + str(release_state) + "! API Connected, Market Data Up-To-Date")
    apiJsonObj = urlopen(api_url + "items/all?&" + api_key)
    fleaMarketData = json.load(apiJsonObj)
else:
    print("Release State = " + str(release_state) + "!, API Not Connected, Market Data Outdated")
    tempFleaMarketData_Json_File = open("tempFleaMarketData.json", encoding="utf-8")
    fleaMarketData = json.load(tempFleaMarketData_Json_File)

def RefreshFleaMarketData():
    if(release_state):
        json_obj = urlopen(api_url + "items/all?&" + api_key)
        fleaMarketData = json.load(json_obj)


def itemMarket_In_userMessage(p_marketItemShortName, p_userMessage):
    if (p_marketItemShortName.replace("-", "").replace(" ", "").lower() in p_userMessage.replace("-", "").replace(" ", "").lower()):
        return True
    return False

def isItemNamePresent(p_userMessage):
    for marketItem in fleaMarketData:
        if (itemMarket_In_userMessage(marketItem["shortName"], p_userMessage)):
            return True
    return False
def getItemName(p_userMessage):
    for marketItem in fleaMarketData:
        if (itemMarket_In_userMessage(marketItem["shortName"], p_userMessage)):
            return marketItem["shortName"]
    return "ERROR! ---Item name not present---"
def getItemPrice(p_itemName, p_marketType):
    RefreshFleaMarketData()
    for marketItem in fleaMarketData:
        if (p_itemName == marketItem["shortName"]):
            if (p_marketType == "tMarket"):
                return marketItem["traderPriceCur"] + str(marketItem["traderPrice"])
            elif (p_marketType == "fMarket"):
                return marketItem["traderPriceCur"] + str(marketItem["avg24hPrice"])
            else:
                return "ERROR! ---Item price type not specified---"
    return "ERROR! ---Item price not found---"
def getItemTraderName(p_itemName):
    for marketItem in fleaMarketData:
        if (marketItem["shortName"] == p_itemName):
            return marketItem["traderName"]
    return "ERROR! ---Item not sold by any trader" 