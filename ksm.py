import requests
import json

dungeons = ["AA", "AV", "COS", "HOV", "NO", "RLP", "SBG", "TJS"]
api_url = "https://raider.io/api/v1/characters/profile?region=us&realm=ysondre&name=meowmage&fields=covenant%2Cgear%2Cguild%2Cmythic_plus_scores_by_season%3Acurrent%2Cmythic_plus_best_runs%2Cmythic_plus_alternate_runs"
response = requests.get(api_url).json()

print("Character Information\n---------------------") 
print(response["name"],"<",response["guild"]["name"],">")
print(response["gear"]["item_level_equipped"],response["active_spec_name"],response["class"])
print(response["realm"])
print(response["mythic_plus_scores_by_season"][0]["scores"]["all"], end = " ")
if response["mythic_plus_scores_by_season"][0]["scores"]["all"] < 2000:
    print("( X )")
else:
    print("( ✔ )")

print("\n\nMythic Plus KSM Status ~ all 13's\n------------------------------------------")

for dungeon in dungeons:
    result1 = ""
    result2 = ""

    for best_runs in response["mythic_plus_best_runs"]:
        if best_runs["short_name"] == dungeon and best_runs["mythic_level"] > 13:
            result1 = best_runs["affixes"][0]["name"]
    
    for alt_runs in response["mythic_plus_alternate_runs"]:
        if alt_runs["short_name"] == dungeon and alt_runs["mythic_level"] > 13:
            result2 = alt_runs["affixes"][0]["name"]
    
    print(dungeon,":", end = " ")
    if result1:
        print(result1,"( ✔ ) ")
    if result2:
        print(result2,"( ✔ ) ")
    if result1 == "" and result2 == "":
        print("Fortified ( X ) Tyrannical ( X )")
    if result1 == "Tyrannical" and result2 != "Fortified":
        print("Fortified ( X )")
    if result1 == "Fortified" and result2 != "Tyrannical":
        print("Tyrannical ( X )")