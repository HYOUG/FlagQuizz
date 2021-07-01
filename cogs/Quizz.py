import asyncio
import colorama
import discord
from discord.embeds import Embed
from discord_components import Button, ActionRow
from discord.ext import commands
from emoji import demojize
from random import choice
from os import listdir
from time import time
from modules.utils import *


class Quizz(commands.Cog):
      
    def __init__(self, bot) -> None:
        self.bot = bot
        self.countries = listdir("./data/flags/")
                
        
    @commands.command()
    async def quizz(self, ctx:commands.Context, round_num:int=1, duration:int=5) -> None:
        game_leaderboard = {}
        
        for round in range(round_num):
            choices = {}
            
            answers = [choice(self.countries) for _ in range(4)]
            solution = choice(answers)
            flag = discord.File(f"./data/flags/{solution}", solution)
            buttons = []
            for answer in answers:
                buttons.append(Button(label=answer[:-4].replace("_", " "), style=1, id=answers.index(answer)+1)) #+1 cuz 0 was buggy for somme reason
            buttons_row = ActionRow(buttons)
            
            embed = discord.Embed(color=embed_color)
            embed.title = "🌍  Find the country for this flag :"
            embed.set_image(url=f"attachment://{solution}")
            embed.add_field(name=f"Round n° {round+1}/{round_num}",
                            value=f":hourglass_flowing_sand: `{duration}` seconds")
            msg = await ctx.send(embed=embed, file=flag, components=buttons_row)
            
            
            start = time()
            
            while time() - start <= duration:
                try:
                    interaction = await self.bot.wait_for("button_click", timeout=time()-start)
                    choices[str(interaction.author.id)] = int(interaction.custom_id)
                    await interaction.respond(content=f"You chose : **{buttons[int(interaction.custom_id)-1].label}**")
                except asyncio.TimeoutError:
                    pass
                
            responses = []
            
            for answer in answers:
                if answer == solution:
                    responses.append(Button(label=answer[:-4].replace("_", " "), style=3, disabled=True))
                else:
                    responses.append(Button(label=answer[:-4].replace("_", " "), style=4, disabled=True))
                    
            buttons_row = ActionRow(responses)
            await msg.edit(components=buttons_row)
            
            for (player, player_choice) in choices.items():
                if player not in game_leaderboard.keys():
                    game_leaderboard[player] = 0
                if player_choice-1 == answers.index(solution):
                    game_leaderboard[player] += 1
            await asyncio.sleep(3)
            
        game_leaderboard = sorted(game_leaderboard.items(), key=lambda el: el[1], reverse=True)
        leaderboard_display = ""
            
        for (player_id, score) in game_leaderboard:
            rank = game_leaderboard.index((player_id, score))
            if  rank == 0:
                medal = "🥇"
            elif rank == 1:
                medal = "🥈"
            elif rank == 2:
                medal = "🥉"
            else:
                medal = "🎖️"
            leaderboard_display += f"{medal} <@{player_id}> : **{score}** pts\n"
                
        embed = Embed(color=embed_color)
        embed.title = "🏆  Leaderboard"
        embed.add_field(name="Ranking", value=leaderboard_display)
        await ctx.send(embed=embed)
            
            
def setup(client):
    client.add_cog(Quizz(client))