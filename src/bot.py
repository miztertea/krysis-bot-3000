# This example requires the 'message_content' intent.
import os, sys, discord
from discord.ext import commands
from ksmdiscord import *
from io import StringIO

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ksm(ctx, realm, character):
    temp_out = StringIO()
    sys.stdout = temp_out
    print("```")
    ksm = my_function(realm, character)
    print("```")
    sys.stdout = sys.__stdout__
    await ctx.send(temp_out.getvalue())

@ksm.error
async def ksm_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing argument... Please ensure you use $ksm realm character')

    elif isinstance(error, commands.CommandError):
        await ctx.send('Character not found... Please check the name and try again')
bot.run(TOKEN)