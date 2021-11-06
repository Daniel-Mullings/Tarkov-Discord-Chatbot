import json
from urllib.request import urlopen

api_key = "x-api-key=9w3MIVAGdu84n6Db"
api_url = "https://tarkov-market.com/api/v1/"

apiJsonObj = urlopen(api_url + "items/all?&" + api_key)
fleaMarketData = json.load(apiJsonObj)

def RefreshFleaMarketData():
    json_obj = urlopen("https://tarkov-market.com/api/v1/items/all?&x-api-key=9w3MIVAGdu84n6Db")
    fleaMarketData = json.load(json_obj)

def WeaponNamePresent(userMessage):
    for weaponItem in fleaMarketData:
        if (weaponItem["tags"][0] == "Weapon"):
            #print(weaponItem["shortName"])
            if (weaponItem["shortName"].lower() in userMessage.lower()):
                return True
    return False

def GetWeaponName(userMessage):
    for weaponItem in fleaMarketData:
        if (weaponItem["tags"][0] == "Weapon"):
            if (weaponItem["shortName"].lower() in userMessage):
                return weaponItem["shortName"]
    return "Weapon name not present"

def GetWeaponPrice(weaponName):
    RefreshFleaMarketData()
    for weaponItem in fleaMarketData:
        if (weaponItem["tags"][0] == "Weapon"):
            if (weaponName == weaponItem["shortName"]):
                return weaponItem["avg24hPrice"]
    return "Price not found"

userMessage = "How much is ak-101"
if (WeaponNamePresent(userMessage)):
    print("The " + GetWeaponName(userMessage) + " costs " + str(GetWeaponPrice(GetWeaponName(userMessage))) + " Rubbles")
else:
    print("Shit")