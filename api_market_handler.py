import json                         #PYTHON STANDARD LIBRARY - https://docs.python.org/3/library/json.html
import urllib.error                 #URLLIB v3.9 - THIRD PARTY LIBRARY - https://github.com/urllib3/urllib3
from urllib.request import *

release_state = True

api_key = "x-api-key=9w3MIVAGdu84n6Db"
api_url = "https://tarkov-market.com/api/v1/"


#JSON OBJECT, FILE SCOPE, STORES MARKET DATA FROM API/OFFLINE JSON FILE BACKUP
marketData = None


#RETRIEVES MARKET DATA FROM API AS TYPE JSON OBJECT
#RETURNS MARKET DATA AS TYPE JSON OBJECT
def FetchOnlineMarketData():
    try:
        #STORES DATA RETURNED FROM API (JSON FILE) USING "urlopen" IN "apiJsonFile"
        #LOADS & STORES JSON FILE (apiJsonFile) AS JSON OBJECT (online_marketData)
        print("NOTICE: ATTEMPTING TO CONNECT TO API. . .")
        apiJsonFile = urlopen(api_url + "items/all?&" + api_key)
        online_marketData = json.load(apiJsonFile)
        print("NOTICE: API CONNECTION SUCCESSFUL")

        #SAVES JSON OBJECT (CONTAINING LIVE DATA) AS JSON FILE (FOR OFFLINE USE)
        SaveOnlineMarketData(online_marketData)

        print("\nRelease State = " + str(release_state) + "! API Connected, Market Data Up-To-Date\n")

        #RETURNS JSON OBJECT, TO BE STORED IN JSON OBJECT IN FILE SCOPE
        return online_marketData

    #HANDLES HTTP RELATED ERRORS, "aka. HTTP ERROR 249: TOO MANY REQUEST"
    #SPECIFIC HTTP ERRORS NOT HANDLED INDIVIDUALLY, ALL HTTP ERRORS RESULT IN SAME SOLUTION
    except urllib.error.HTTPError:
        print("WARNING! API CONNECTION FAILIURE, REVERTING TO OFFLINE DATA\n")
        return FetchOfflineMarketData()

#RETRIEVES MARKET DATA FROM SAVED JSON FILE
#REUTRNS MARKET DATA AS JSON OBJECT
def FetchOfflineMarketData():
    print("Release State = " + str(release_state) + "!, API Not Connected, Market Data Outdated\n")

    #LOADS JSON FILE, RETURNS IT AS A JSON OBJECT TO BE STORED IN JSON OBJECT IN FILE SCOPE
    offlineMarketData_Json_File = open("offlineMarketData.json", encoding="utf-8")
    return json.load(offlineMarketData_Json_File)

#TAKES MARKET DATA FROM API AS TYPE JSON OBJECT
#SAVES JSON OBJECT AS JSON FILE (FOR USE WHEN API CONNECTION FAILS)
def SaveOnlineMarketData(updatedMarketData):
    try:
        offlineMarketData_Json_File = open("offlineMarketData.json", "w", encoding="utf-8")
        json.dump(updatedMarketData, offlineMarketData_Json_File, ensure_ascii = False)
        print("NOTICE: OFFLINE MARKET DATA UPDATED & SAVED")
        offlineMarketData_Json_File.close()
    except:
        print("WARNING! FAILED TO UPDATE OFFLINE MARKET DATA")
        offlineMarketData_Json_File.close()

#ONLY REQUESTS MARKET DATA FROM API DATA IF "release_state" OF TYPE bool = True,
#PREVENTS "HTTP ERROR 249: TOO MANY REQUEST" DURING TESTING
if (release_state):
    marketData = FetchOnlineMarketData()
else:
    marketData = FetchOfflineMarketData()


#TAKES ITEM NAME AS TYPE str AND A USERS MESSAGE AS TYPE str
#RETURNS WETHER THE ITEM NAME IS IN THE USER MESSAGE AS TYPE bool
def marketItem_In_userMessage(p_marketItemShortName, p_userMessage):
    if (p_marketItemShortName.replace("-", "").replace(" ", "").lower() in p_userMessage.replace("-", "").replace(" ", "").lower()):
        return True
    return False

#TAKES A USERS MESSAGES AS TYPE str
#RETURNS WETHER AN ITEM NAME (STORED IN THE API DATA) IS PRESENT IN THE USERS MESSAGE AS TYPE bool 
def isItemNamePresent(p_userMessage):
    for marketItem in marketData:
        if (marketItem_In_userMessage(marketItem["shortName"], p_userMessage)):
            return True

    #ITEM NAME NOT PRESENT
    return False

#TAKES A USERS MESSAGE AS TYPE str
#RETURNS ITEM NAME (AS IT APPEARS IN API DATA) AS TYPE str OR bool = False
def getItemName(p_userMessage):
    for marketItem in marketData:
        if (marketItem_In_userMessage(marketItem["shortName"], p_userMessage)):
            return marketItem["shortName"]
    
    #ITEM NAME NOT PRESENT
    return False

#TAKES ITEM NAME AS TYPE str AND MARKET TYPE("tMarket" OR "fMarket") AS TYPE str, 
#RETURNS CORRESPONDING ITEM PRICE (WITH CURRENCY SYMBOL PREFIXED) AS TYPE str OR bool = False
def getItemPrice(p_itemName, p_marketType):
    for marketItem in marketData:
        if (p_itemName == marketItem["shortName"]):
            if (p_marketType == "tMarket"):
                return marketItem["traderPriceCur"] + str(marketItem["traderPrice"])
            elif (p_marketType == "fMarket"):
                return marketItem["traderPriceCur"] + str(marketItem["avg24hPrice"])
            else:
                #MISSING/INCORRECT MARKET TYPE
                return False
    
    #ITEM PRICE NOT FOUND
    return False

#TAKES ITEM NAME AS TYPE str, 
#RETURNS CORRESPONDING ITEM TRADER NAME AS TYPE str OR bool = False
def getItemTraderName(p_itemName):
    for marketItem in marketData:
        if (marketItem["shortName"] == p_itemName):
            return marketItem["traderName"]
    
    #ITEM NAME NOT FOUND
    return False