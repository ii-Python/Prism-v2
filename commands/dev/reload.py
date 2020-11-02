# Modules
import discord
from discord.ext import commands

# Command class
class Reload(commands.Cog):

    """Reloads a module | <module>"""

    def __init__(self, bot, prism):
        self.bot = bot
        self.prism = prism

    @commands.command(pass_context = True, aliases = ["re"])
    @commands.is_owner()
    async def reload(self, ctx, module = None):

        if not module:

            return await ctx.send(embed = self.prism.error("No module specified to reload."))

        elif module.endswith(".py"):

            module = module[:-3]  # subtract the .py

        path = self.prism.locate_command(module)

        if not path:

            return await ctx.send(embed = self.prism.error("Failed to locate module."))

        try:

            self.bot.unload_extension(path)
            self.bot.load_extension(path)
            
            embed = discord.Embed(title = "Reload successful!", description = f"Reloaded module: `{path}`", color = self.prism.color)
            embed.set_footer(text = f"| Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

            return await ctx.send(embed = embed)

        except Exception as err:

            embed = discord.Embed(title = f"Failed to reload `{path}`.", description = f"Additional details:\n```\n{err}\n```", color = self.prism.color)

            return await ctx.send(embed = embed)

# Setup function
def setup(bot):

    bot.add_cog(Reload(bot, bot.prism))
