from discord.ext import commands
from discord import Embed
from modules.utils import embed_color

class Help(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx: commands.Context) -> None:
        embed = Embed(color=embed_color)
        embed.title = "❔ Help"
        embed.add_field(name="Commands synthax", value="`&command_name (mandatory argument) [optional argument]`", inline=False)
        embed.add_field(name="&quizz [round number] [round duration]",
                        value="`Start a quizz of [round number] rounds (default: 1), every round will last [round duration] seconds (default: 5)`")
        
        await ctx.author.send(embed=embed)
    
    
def setup(client):
    client.add_cog(Help(client))