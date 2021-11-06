import json
from urllib.request import urlopen

api_key = "x-api-key=9w3MIVAGdu84n6Db"
api_url = "https://tarkov-market.com/api/v1/"

release_state = False

if (release_state):
    apiJsonObj = urlopen(api_url + "items/all?&" + api_key)
    fleaMarketData = json.load(apiJsonObj)
else:
    print("Release State = " + str(release_state) + "!, API Not Connected, Market Data Outdated\n")
    tempFleaMarketData_Json_File = open("tempFleaMarketData.json", encoding="utf-8")
    fleaMarketData = json.load(tempFleaMarketData_Json_File)

def RefreshFleaMarketData():
    if(release_state):
        json_obj = urlopen(api_url + "items/all?&" + api_key)
        fleaMarketData = json.load(json_obj)

def WeaponNamePresent(userMessage):
    for weaponItem in fleaMarketData:
        if (weaponItem["tags"][0] == "Weapon"):
            if (weaponItem["shortName"].replace("-", "").replace(" ", "").lower() in userMessage.replace("-", "").replace(" ", "").lower()):
                return True
    return False
def GetWeaponName(userMessage):
    for weaponItem in fleaMarketData:
        if (weaponItem["tags"][0] == "Weapon"):
            if (weaponItem["shortName"].replace("-", "").replace(" ", "").lower() in userMessage.replace("-", "").replace(" ", "").lower()):
                return weaponItem["shortName"]
    return "ERROR! ---Weapon name not present---"
def GetWeaponPrice(weaponName):
    RefreshFleaMarketData()
    for weaponItem in fleaMarketData:
        if (weaponItem["tags"][0] == "Weapon"):
            if (weaponName == weaponItem["shortName"]):
                return weaponItem["avg24hPrice"]
    return "ERROR! ---Price not found---"

def AmmoNamePresent(userMessage):
    for ammoItem in fleaMarketData:
        if (ammoItem["tags"][0] == "Ammo"):
            if (ammoItem["shortName"].replace("-", "").replace(" ", "").lower() in userMessage.replace("-", "").replace(" ", "").lower()):
                return True
        return False
def GetAmmoName(userMessage):
    for ammoItem in fleaMarketData:
        if (ammoItem["tags"][0] == "Ammo"):
            if (ammoItem["shortName"].replace("-", "").replace(" ", "").lower() in userMessage.replace("-", "").replace(" ", "").lower()):
                return ammoItem["shortName"]
    return "ERROR! ---Ammo name not present---"
def GetAmmoPrice(ammoName):
    RefreshFleaMarketData()
    for ammoItem in fleaMarketData:
        if (ammoItem["tags"][0] == "Ammo"):
            if (ammoName == ammoItem["shortName"]):
                return ammoItem["avg24hPrice"]
    return "ERROR! ---Price not found---"


def TestFunction():
    userMessage = "cost of the mp133"
    if (WeaponNamePresent(userMessage)):
        print("The " + GetWeaponName(userMessage) + " costs " + str(GetWeaponPrice(GetWeaponName(userMessage))) + " Rubbles")
    else:
        print("Shit")