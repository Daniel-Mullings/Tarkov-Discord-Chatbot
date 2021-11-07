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



def isWeaponNamePresent(p_userMessage):
    return ItemNamePresent(p_userMessage, "Weapon")
def isAmmoNamePresent(p_userMessage):
    return ItemNamePresent(p_userMessage, "Ammo")

def getWeaponName(p_userMessage):
    return ItemName(p_userMessage, "Weapon")
def getAmmoName(p_userMessage):
    return ItemName(p_userMessage, "Ammo")

def getWeaponPrice(p_weaponName):
    return ItemPrice(p_weaponName, "Weapon")
def getAmmoPrice(p_ammoName):
    return ItemPrice(p_ammoName, "Ammo")



def ItemNamePresent(p_userMessage, p_itemType):
    for marketItem in fleaMarketData:
        if (marketItem["tags"][0] == p_itemType):
            if (marketItem["shortName"].replace("-", "").replace(" ", "").lower() in p_userMessage.replace("-", "").replace(" ", "").lower()):
                return True
    return False
def ItemName(p_userMessage, p_itemType):
    for marketItem in fleaMarketData:
        if (marketItem["tags"][0] == p_itemType):
            if (p_userMessage == "debug_PrintAll"):
                print(marketItem["tags"])
            if (marketItem["shortName"].replace("-", "").replace(" ", "").lower() in p_userMessage.replace("-", "").replace(" ", "").lower()):
                return marketItem["shortName"]
    return "ERROR! ---Item name not present---"
def ItemPrice(p_itemName, p_itemType):
    RefreshFleaMarketData()
    for marketItem in fleaMarketData:
        if (marketItem["tags"][0] == p_itemType):
            if (p_itemName == marketItem["shortName"]):
                return marketItem["avg24hPrice"]
    return "ERROR! ---Item price not found---"



def printAllItemName(p_itemType):
    if (not release_state):
        ItemName("debug_PrintAll", p_itemType)