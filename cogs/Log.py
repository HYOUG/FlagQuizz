from discord.ext import commands
from modules.utils import *

class Log(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        self.new = f"[{green('+')}]"
    
    @commands.Cog.listener(name="on_message")
    async def on_message(self, message):
        if not message.author.bot and message.content.startswith("&quizz"):
            print(f"{self.new}[{get_time()}] {blue(str(message.author))}: {green(message.content)} {pink(f'({message.channel.name})')}")
           
            
def setup(client):
    client.add_cog(Log(client))