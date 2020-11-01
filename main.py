# Prism v2 - The only discord bot you need.
# Copyright 2020, iiPython (github/ii-Python).

# Modules
from os import getenv
from dotenv import load_dotenv
from prism import Prism, Events

# Initialization
load_dotenv()

prism = Prism()
bot = prism.bot

# Event handler
events = Events(prism)

@bot.event
async def on_ready():

    events.on_ready()

# Run
bot.run(getenv("TOKEN"), reconnect = True)
