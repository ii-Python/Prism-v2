# Modules
import discord
import logging

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

        # Create bot
        bot = commands.Bot(command_prefix = "p!")

        bot.remove_command("help")  # the default help command is ugly

        # Mapping
        self.bot = bot

        # Link items to the bot
        bot.prism = self

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

                    self.bot.load_extension(f"commands.{category}.{file[:-3]}")

    def error(self, text):

        """Returns a `discord.Embed` object containing error information"""

        return discord.Embed(description = f":x: \t **{text}**", color = 0xFF0000)

    def locate_command(self, command):

        """Attempts to locate a command file, returns `None` if failed"""

        for folder in listdir("commands"):

            for file in listdir(f"commands/{folder}"):  # each file in the category

                if file == command + ".py":  # is it the same

                    return f"commands.{folder}.{command}"  # yea its a valid command and it exists

        return None  # nope sorry
                    