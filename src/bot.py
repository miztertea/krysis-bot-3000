import os, sys, discord
from discord.ext import commands
from engine import *
from io import StringIO

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ksm(ctx, realm, character):
    # Setup a variable to capture stdout from print statements in function
    temp_out = StringIO()
    sys.stdout = temp_out
    
    # Calls function and creates output
    print("```")
    ksm = ksm_status(realm, character)
    print("```")
    
    # Returns stdout to the system
    sys.stdout = sys.__stdout__
    
    # Post the output back to discord channel
    await ctx.send(temp_out.getvalue())

@bot.command()
async def rank(ctx, realm, character, role):
    rank = rio_rank(realm, character, role)
    if rank is None:
        await ctx.send("Character is not that role.")
    else:
        await ctx.send(rank)

# Error Handling
@ksm.error
async def ksm_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing argument... Please ensure you use $ksm realm character')

    elif isinstance(error, commands.CommandError):
        await ctx.send('Character not found... Please check the name and try again')

# Error Handling
@rank.error
async def ksm_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing argument... Please ensure you use $rank realm character role(tank,dps,healer)')

    elif isinstance(error, commands.CommandError):
        await ctx.send('Character/realm/role combination not found... Please try again')

bot.run(TOKEN)