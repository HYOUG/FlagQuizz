from discord.ext import commands
from os import system
from modules.utils import *


class Admin(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.command()
    async def off(self, ctx):
        await ctx.send(f"{self.bot.user.name} will log out soon")
        await self.bot.close()
        print(f"{yellow(self.bot.user.name)} is logging out")


    @commands.command()
    async def reboot(self, ctx):
        await ctx.send(f"{self.bot.user.name} will reboot soon !")
        await self.bot.close()
        print(f"{yellow(self.bot.user.name)} is rebooting...")
        system("python main.py")
        
        
def setup(client):
    client.add_cog(Admin(client))