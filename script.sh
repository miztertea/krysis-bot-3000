#!/bin/bash

#Use command line parameters for realm and character name
#Example:  ./script.sh ysondre Starskey

clear
#URI encode Player name to account for special characters
encoded=$(printf %s "$2" | jq -s -R -r @uri)

# Array of Short Names of Dungeons
# SL SEASON 3 dungeons=(MISTS DOS HOA SD NW SOA PF TOP GMBT STRT)
# SL SEASON 4 dungeons=(STRT GMBT UPPR LOWR WORK YARD GD ID)
keylevel=13
ioreq=2000
dungeons=(AA AV COS HOV NO RLP SBG TJS)
temp_file=$(date +%s)

# Retrieve character information from Raider.io API
curl -sX 'GET' \
  'https://raider.io/api/v1/characters/profile?region=us&realm='$1'&name='$encoded'&fields=covenant%2Cgear%2Cguild%2Cmythic_plus_scores_by_season%3Acurrent%2Cmythic_plus_best_runs%2Cmythic_plus_alternate_runs' \
  -H 'accept: application/json' > $temp_file

# Error handling if character doesn't exist
error=$(jq -jrc '.statusCode' $temp_file)
if [ "$error" = 400 ]
then
  printf "Error: $2 not found on realm $1, please check the name and server and try again.\n"
  rm $temp_file
  exit
fi

# Retrieve the character information
printf "Character Information\n---------------------\n"
jq -jrc '.name, " <",.guild.name,">","\n",.gear.item_level_equipped," ",.active_spec_name," ",.class,"\n",.realm,"\n"' $temp_file
score=$(jq -rc '.mythic_plus_scores_by_season[0] | .scores | .all' $temp_file)
scoreInt=${score%.*}
if (( $scoreInt > $ioreq ))
then
  printf "$score ( ✔ )"
else
  printf "$score ( X )"
fi
# Output the header
printf "\n\nMythic Plus KSM Status ~ all $keylevel's\n------------------------------------------\n"

# Loop through the dungeon short names in array
for i in "${dungeons[@]}"
do
  # Reset Variables
  dungeon1=""
  dungeon2=""
  
  # Parse JSON for Affix Weeks completed with a 15 or greater
  dungeon1=$(jq -jrc '.mythic_plus_best_runs[] | select((.short_name=="'$i'") and .mythic_level >= '$keylevel') | .affixes[0].name' $temp_file)
  dungeon2=$(jq -jrc '.mythic_plus_alternate_runs[] | select((.short_name=="'$i'") and .mythic_level >= '$keylevel') | .affixes[0].name' $temp_file)
  
  # Check if a result for dungeon1
  printf "$i : "
  if [ "$dungeon1" ]
  then
    printf "$dungeon1 ( ✔ ) "
  fi

  # Check if a result for dungeon2
  if [ "$dungeon2" ]
  then
    printf "$dungeon2 ( ✔ )\n"
  fi

  # Check if no result for dungeons
  if [ -z "$dungeon1" -a -z "$dungeon2" ]
  then
    printf "Fortified ( X ) Tyrannical ( X )\n"
  fi

  # Check if mixed result for dungeons
  if [ "$dungeon1" == "Tyrannical" -a "$dungeon2" != "Fortified" ]
  then
    printf "Fortified ( X )\n"
  elif [ "$dungeon1" == "Fortified" -a "$dungeon2" != "Tyrannical" ]
  then
    printf "Tyrannical ( X )\n"
  fi
done

# Output last time Raider IO was updated
jq -jrc '"\nLast updated: ",.last_crawled_at,"\n"' $temp_file

# Output some blank lines for formatting
printf '%.0s\n' {1..3}

# Cleanup the temporary file
rm $temp_file