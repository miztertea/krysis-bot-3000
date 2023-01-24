# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from ksmdiscord import *
from io import StringIO
import sys
import os
from dotenv import load_dotenv

load_dotenv()
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

bot.run(TOKEN)