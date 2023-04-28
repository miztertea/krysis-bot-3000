import requests, json, urllib
from prettytable import PrettyTable

def ksm_status(realm, character):
    #Config
    min_key_level = 13
    io_req = 2000
    season = "season-df-2"
    #dungeons = ["AA", "AV", "COS", "HOV", "NO", "RLP", "SBG", "TJS"]
    dungeons = ["BH", "FH", "HOI", "NL", "NELT", "UNDR", "VP", "ULD"]
    
    #URI encode Player name to account for special characters
    encoded_name = urllib.parse.quote(character)

    # Retrieve character information from Raider.io API
    api_url = "https://raider.io/api/v1/characters/profile?region=us&realm={}&name={}&fields=gear%2Cguild%2Cmythic_plus_scores_by_season%3A{}}%2Cmythic_plus_best_runs%2Cmythic_plus_alternate_runs".format(realm,encoded_name,season)
    response = requests.get(api_url).json()

    # Retrieve the character information
    print("Character Information\n---------------------") 
    #print(response["name"],"<",response["guild"]["name"],">")
    print("{} <{}>".format(response["name"],response["guild"]["name"]))
    print(response["gear"]["item_level_equipped"],response["active_spec_name"],response["class"])
    print(response["realm"])
    print(response["mythic_plus_scores_by_season"][0]["scores"]["all"], end = " ")
    if response["mythic_plus_scores_by_season"][0]["scores"]["all"] < io_req:
        print("- You need", io_req - round(response["mythic_plus_scores_by_season"][0]["scores"]["all"]), "more points.")
    else:
        print("( ✔ )")

    # Function to search for Tyrannical Affix
    def tyrannical(dungeon):
        for best_runs in response["mythic_plus_best_runs"]:
            if best_runs["short_name"] == dungeon and best_runs["affixes"][0]["name"] == "Tyrannical":
                return best_runs["mythic_level"]
            else:
                for alt_runs in response["mythic_plus_alternate_runs"]:
                    if alt_runs["short_name"] == dungeon and alt_runs["affixes"][0]["name"] == "Tyrannical":
                        return alt_runs["mythic_level"]

    # Function to search for Fortified Affix
    def fortified(dungeon):
        for best_runs in response["mythic_plus_best_runs"]:
            if best_runs["short_name"] == dungeon and best_runs["affixes"][0]["name"] == "Fortified":
                return best_runs["mythic_level"]
            else:
                for alt_runs in response["mythic_plus_alternate_runs"]:
                    if alt_runs["short_name"] == dungeon and alt_runs["affixes"][0]["name"] == "Fortified":
                        return alt_runs["mythic_level"]

    # Setup the results table    
    resultsTable = PrettyTable(["Dungeon","Tyrannical","Fortified"])

    # Loop through the dungeon short names in array
    for dungeon in dungeons:
        result = tyrannical(dungeon)
        if result is None:
            bestTyrannical = "-"
        elif result >= min_key_level:
            bestTyrannical = "✔"
        else:
            bestTyrannical = result
        
        result = fortified(dungeon)
        if result is None:
            bestFortified = "-"
        elif result >= min_key_level:
            bestFortified = "✔"
        else:
            bestFortified = result
        resultsTable.add_row([dungeon,bestTyrannical,bestFortified])
    
    # Output results in a "Pretty" table
    print("")
    print(resultsTable)
    print("(Anything",min_key_level,"or higher shows as a ✔)\n")
    print("Last Updated:",response["last_crawled_at"])

def rio_rank(realm, character, role):
    #URI encode Player name to account for special characters
    encoded_name = urllib.parse.quote(character)

    # Retrieve character information from Raider.io API
    api_url = "https://raider.io/api/v1/characters/profile?region=us&realm={}&name={}&fields=mythic_plus_ranks".format(realm,encoded_name)
    response = requests.get(api_url).json()
    classRank = response["mythic_plus_ranks"]["class_" + str.lower(role)]["realm"]
    return str.capitalize(character)+" is the #"+str(classRank)+" "+response["active_spec_name"]+" "+response["class"]+" "+role+" on "+str.capitalize(realm)