# Modules
import discord
from discord.ext import commands

# Command class
class Load(commands.Cog):

    """Loads a module | <module>"""

    def __init__(self, bot, prism):
        self.bot = bot
        self.prism = prism

    @commands.command(pass_context = True)
    @commands.is_owner()
    async def load(self, ctx, module = None):

        if not module:

            return await ctx.send(embed = self.prism.error("No module specified to load."))

        elif module.endswith(".py"):

            module = module[:-3]  # subtract the .py

        path = self.prism.locate_command(module)

        if not path:

            return await ctx.send(embed = self.prism.error("Failed to locate module."))

        try:

            self.bot.load_extension(path)
            
            embed = discord.Embed(title = "Load successful!", description = f"Loaded module: `{path}`", color = self.prism.color)
            embed.set_footer(text = f"| Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

            return await ctx.send(embed = embed)

        except Exception as err:

            embed = discord.Embed(title = f"Failed to load `{path}`.", description = f"Additional details:\n```\n{err}\n```", color = self.prism.color)

            return await ctx.send(embed = embed)

# Setup function
def setup(bot):

    bot.add_cog(Load(bot, bot.prism))
