# Modules
import discord
import inspect

import logging
import importlib

from os import listdir
from .config import Config

from discord.ext import commands

# Main class
class Prism(object):

    """Represents the internal system of Prism v2"""

    def __init__(self):

        self.bot = None
        self.config = Config()

        self._set_bot()
        self._init_colors()

    def _set_bot(self):

        """Creates a fresh `commands.Bot` instance and maps it to `self.bot`"""

        bot = commands.Bot(command_prefix = "p!")

        bot.remove_command("help")  # the default help command is ugly

        self.bot = bot  # just map the bot

    def _init_colors(self):

        """Loads the colors from `config.json` and sets them to a `discord.Color` value"""

        color = self.config.fetch("color")
        
        try:

            r = color["r"]
            g = color["g"]
            b = color["b"]

            self.color = discord.Color.from_rgb(r, g, b)

        except:

            logging.warning("Failed to load colors, setting them to default")

            self.color = 0x126bf1

    def load_commands(self):

        """Loads all of the commands in the `commands` folder and its subfolders"""

        for category in listdir("commands"):

            for file in listdir(f"commands/{category}"):

                if file.endswith(".py"):  # this prevents pycache from being scanned

                    module = importlib.import_module(f"commands.{category}.{file[:-3]}")

                    for class_ in inspect.getmembers(module, inspect.isclass):

                        if issubclass(class_[1], commands.Cog):  # located the command

                            # begin loading into the bot
                            self.bot.add_cog(class_[1](self.bot, self))

    def error(self, text):

        """Returns a `discord.Embed` object containing error information"""

        return discord.Embed(description = f":x: \t **{text}**", color = 0xFF0000)
                    
