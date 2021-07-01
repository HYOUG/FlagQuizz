#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

from discord import Game, Status
from discord.ext import commands
from discord_components import DiscordComponents
from os import listdir
from modules.utils import *


token = open("./data/token.txt", "r").read()
bot = commands.Bot(command_prefix="&")
status = Game("with &quizz | &help")
bot.remove_command("help")
    
    
for filename in listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        bot.get_cog(filename[:-3])
    
    
@bot.event
async def on_ready():
    await bot.change_presence(status=Status.online, activity=status)
    DiscordComponents(bot)
    print(f"{yellow(bot.user.name)} is now running")
    

bot.run(token)
