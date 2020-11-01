# Modules
from discord.ext import commands

# Main class
class Prism(object):

    """Represents the internal system of Prism v2"""

    def __init__(self):

        self._set_bot()

    def _set_bot(self):

        """Creates a fresh `commands.Bot` instance and maps it to `self.bot`"""

        bot = commands.Bot(command_prefix = "p!")

        bot.remove_command("help")  # the default help command is ugly

        self.bot = bot  # just map the bot
        