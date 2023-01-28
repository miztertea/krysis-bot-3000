# KRYSIS-BOT-3000
A simple discord bot to retrieve a character from raider.io. It can determine whether or not the character has the necessary mythic+ score met for the Keystone Master achievement and provide recommendations for which dungeons have not been completed at a minimum level for the given week.  It can also retrieve a characters rank for their given realm and spec.

Example output:
```
Character Information
---------------------
Føxius <Krysis>
407 Beast Mastery Hunter
Altar of Storms
2463.3 ( ✔ )

+---------+------------+-----------+
| Dungeon | Tyrannical | Fortified |
+---------+------------+-----------+
|    AA   |     ✔      |     ✔     |
|    AV   |     ✔      |     ✔     |
|   COS   |     ✔      |     ✔     |
|   HOV   |     ✔      |     ✔     |
|    NO   |     ✔      |     ✔     |
|   RLP   |     ✔      |     ✔     |
|   SBG   |     ✔      |     ✔     |
|   TJS   |     ✔      |     ✔     |
+---------+------------+-----------+
(Anything 13 or higher shows as a ✔)

Last Updated: 2023-01-23T20:26:31.000Z
```

### Using my hosted discord bot:
- Invite the discord bot to your server: https://discord.com/api/oauth2/authorize?client_id=1067545463982653470&permissions=2048&scope=bot
- Invoke the ksm function using the following syntax: $ksm <realm> <character>
-- Example: $ksm ysondre kaiser
- Invoke the realm rank function using the following syntax: $rank <realm> <character> <role>
-- Example: $ksm ysondre kaiser healer

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


