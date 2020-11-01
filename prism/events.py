# Event class
class Events(object):

    """Represents Prism's event system, containing function calls"""

    def __init__(self, prism):
        self.prism = prism
        self.bot = self.prism.bot

    def on_ready(self):

        """Simple function to declare that we are logged in"""

        print(f"Logged in as {self.bot.user}.")
        print(f"-------------{'-' * len(str(self.bot.user))}-")

        print()  # a new line just for effect
