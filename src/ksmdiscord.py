#Import Required Libraries
import requests, json, urllib

def my_function(realm, character):
    #Config
    #realm = "altar-of-storms"
    #character = "ineedmythong"
    min_key_level = 13
    io_req = 2000

    #URI encode Player name to account for special characters
    encoded_name = urllib.parse.quote(character)

    # Array of Short Names of Dungeons
    # SL SEASON 3 dungeons=["MISTS", "DOS", "HOA", "SD", "NW", "SOA", "PF", "TOP", "GMBT", "STRT"]
    # SL SEASON 4 dungeons=["STRT", "GMBT", "UPPR", "LOWR", "WORK", "YARD", "GD", "ID"]
    dungeons = ["AA", "AV", "COS", "HOV", "NO", "RLP", "SBG", "TJS"]

    # Retrieve character information from Raider.io API
    api_url = "https://raider.io/api/v1/characters/profile?region=us&realm={}&name={}&fields=covenant%2Cgear%2Cguild%2Cmythic_plus_scores_by_season%3Acurrent%2Cmythic_plus_best_runs%2Cmythic_plus_alternate_runs".format(realm,encoded_name)
    response = requests.get(api_url).json()

    # Retrieve the character information
    print("Character Information\n---------------------") 
    print(response["name"],"<",response["guild"]["name"],">")
    print(response["gear"]["item_level_equipped"],response["active_spec_name"],response["class"])
    print(response["realm"])
    print(response["mythic_plus_scores_by_season"][0]["scores"]["all"], end = " ")
    if response["mythic_plus_scores_by_season"][0]["scores"]["all"] < io_req:
        print("- You need", io_req - round(response["mythic_plus_scores_by_season"][0]["scores"]["all"]), "more points.")
    else:
        print("( ✔ )")

    # Output the header
    print("\n\nMythic Plus KSM Status \n( Approximately all level", min_key_level, ")\n------------------------------------------")

    # Loop through the dungeon short names in array
    for dungeon in dungeons:
        # Reset Variables
        result1 = ""
        result2 = ""

        # Parse JSON for Affix Weeks completed
        for best_runs in response["mythic_plus_best_runs"]:
            if best_runs["short_name"] == dungeon and best_runs["mythic_level"] > min_key_level:
                result1 = best_runs["affixes"][0]["name"]
        
        for alt_runs in response["mythic_plus_alternate_runs"]:
            if alt_runs["short_name"] == dungeon and alt_runs["mythic_level"] > min_key_level:
                result2 = alt_runs["affixes"][0]["name"]
        
        # Logic for difference combinations of results
        print(dungeon,":", end = " ")
        if result1:
            print(result1,"( ✔ )", end = " ")
        if result2:
            print(result2,"( ✔ ) ")
        # Check if no result for dungeons
        if result1 == "" and result2 == "":
            print("Fortified ( X ) Tyrannical ( X )")
        # Check if mixed result for dungeons
        if result1 == "Tyrannical" and result2 != "Fortified":
            print("Fortified ( X )")
        if result1 == "Fortified" and result2 != "Tyrannical":
            print("Tyrannical ( X )")