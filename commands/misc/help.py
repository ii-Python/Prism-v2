# Modules
import discord
import inspect

import importlib
from os import listdir

from discord.ext import commands

# Command class
class Help(commands.Cog):

    """The help command, it lists available commands. | [category/command]"""

    def __init__(self, bot, prism):
        self.bot = bot
        self.prism = prism

    def fetch_commands(self, folder):

        response = ""

        for file in listdir(f"commands/{folder}"):

            if file.endswith(".py"):  # yea its a command

                response += f"`{file[:-3]}`, "  # subtract the .py from the end obv

        return response[:-2]  # subtract the extra , at the end

    @commands.command(pass_context = True)
    async def help(self, ctx, module = None):

        categories = self.prism.config.fetch("categories")

        if not module:

            # Show them the default Prism embed
            embed = discord.Embed(title = "Prism", description = "The only discord bot you need.\nYou can hover over blue text for more information.", url = self.prism.config.fetch("dbl_url"), color = self.prism.color)

            for cat in categories:

                embed.add_field(name = f":{categories[cat]['emoji']}: {cat}", value = f"[List commands with `{ctx.prefix}help {categories[cat]['aliases'][0]}`](https://about:blank \"{categories[cat]['description']}\")")

        else:

            # They actually specified something
            module = module.lower()
            category = None

            for cat in categories:

                if cat.lower() == module:
                    
                    category = cat

                else:

                    if module in categories[cat]["aliases"]:

                        category = cat

            if category:

                # They specified the name of a category
                embed = discord.Embed(title = f":{categories[category]['emoji']}: {category} Commands", description = self.fetch_commands(categories[cat]["folder"]), color = self.prism.color)

            else:

                # Maybe they typed a command?
                path = self.prism.locate_command(module)

                if not path:

                    # alrighty then maybe not
                    return await ctx.send(embed = self.prism.error("Failed to locate that module."))

                m = importlib.import_module(path)

                # scan through the classes and locate the command
                for class_ in inspect.getmembers(m, inspect.isclass):

                    if issubclass(class_[1], commands.Cog):

                        description = class_[1].__doc__

                        if "|" in description:

                            description = description.split(" | ")

                            description[1] = " " + description[1]

                        else:

                            description = (description, "")

                embed = discord.Embed(title = module[0].upper() + module[1:], description = description[0], color = self.prism.color)

                embed.add_field(name = "Command Usage", value = f"`{module}{description[1]}`")

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        embed.set_author(name = "| Help", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f"| Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Setup function
def setup(bot):

    bot.add_cog(Help(bot, bot.prism))
