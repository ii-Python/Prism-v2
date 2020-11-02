# Modules
import discord
from requests import get

from datetime import datetime
from discord.ext import commands

# Command class
class Ping(commands.Cog):

    """Displays latency information"""

    def __init__(self, bot, prism):
        self.bot = bot
        self.prism = prism

    @commands.command(pass_context = True)
    async def ping(self, ctx):

        # Calculate bot ping
        bot = round(self.bot.latency * 1000)
        
        # Calculate API latency
        first = datetime.now()

        msg = await ctx.send("This is a message used to calculate ping time.")  # Measures the API latency    

        api = int(str(datetime.now() - first).split(".")[1][:2])

        # Attempt to remove message
        try:

            await msg.delete()

        except:

            pass

        # Send results
        embed = discord.Embed(title = "Pong! Here are the results.", color = self.prism.color)

        embed.add_field(name = "Bot Ping", value = f"`{bot}ms`")
        embed.add_field(name = "API Ping", value = f"`{api}ms`")
        embed.add_field(name = "Roundtrip", value = f"`{bot + api}ms`")

        return await ctx.send(embed = embed)

# Setup function
def setup(bot):

    bot.add_cog(Ping(bot, bot.prism))
