import requests
import json

dungeons = ["AA", "AV", "COS", "HOV", "NO", "RLP", "SBG", "TJS"]
api_url = "https://raider.io/api/v1/characters/profile?region=us&realm=magtheridon&name=blackblade&fields=covenant%2Cgear%2Cguild%2Cmythic_plus_scores_by_season%3Acurrent%2Cmythic_plus_best_runs%2Cmythic_plus_alternate_runs"
response = requests.get(api_url).json()

print("Character Information\n---------------------") 
print(response["name"],"<",response["guild"]["name"],">")
print(response["gear"]["item_level_equipped"],response["active_spec_name"],response["class"])
print(response["realm"])
print(response["mythic_plus_scores_by_season"][0]["scores"]["all"])

print("\n\nMythic Plus KSM Status ~ all 13's\n------------------------------------------")

for i in dungeons
    print(response)