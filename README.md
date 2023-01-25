# World of Warcraft KSM Tracker
A simple discord bot to retrieve a character from raider.io that determines whether or not the character has the necessary mythic+ score met for the Keystone Master achievement and provide recommendations for which dungeons have not been completed at a minimum level for the given week.

Example output:
```
Character Information
---------------------
Kaiser < Krysis >
397 Windwalker Monk
Ysondre
2017.6 ( ✔ )

Mythic Plus KSM Status 
( Approximately all level 13 )
------------------------------------------
AA : Fortified ( ✔ ) Tyrannical ( X )
AV : Fortified ( X ) Tyrannical ( X )
COS : Fortified ( ✔ ) Tyrannical ( X )
HOV : Fortified ( ✔ ) Tyrannical ( X )
NO : Fortified ( ✔ ) Tyrannical ( X )
RLP : Fortified ( X ) Tyrannical ( X )
SBG : Tyrannical ( ✔ ) Fortified ( X )
TJS : Fortified ( ✔ ) Tyrannical ( X )
```

### Using my hosted discord bot:
- Invite the discord bot to your server: https://discord.com/api/oauth2/authorize?client_id=1067545463982653470&permissions=2048&scope=bot
- Invoke the bot using the following syntax: $ksm <realm> <character>
-- Example: $ksm ysondre kaiser

### Building the bot from source
- Create an app at: https://discord.com/developers/applications/
- Create a bot in the new app from the left navigation and copy down Token, you will need it later
- Enable: Message Content Intent
- Under OAUTH2 -> URL Generator TAB
-- Select "Bot" under scopes and "Send Messages" under text permissions
-- Copy the link at the bottom and paste into your browser to invite the bot to your server.
-- If you didn't copy down the token, go back to the bot tab and click "reset token" and copy it down.
- Build the docker container.

        docker build --tag ksm-tracker .
    
- Run the docker container

        docker run --env DOCKER_TOKEN=<insert your token> ksm-tracker


