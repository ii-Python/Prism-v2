# Modules
import logging
from json import loads

# Setup logging
logging.basicConfig(
    format = "%(levelname)s: %(message)s",
    level = logging.WARNING
)

# Master class
class Config(object):

    """Simple class to help Prism interact with the `config.json` file"""

    def __init__(self):
        
        self.data = {}

        self.reload_config()

    def reload_config(self):

        try:

            with open("config.json") as f:
                raw = f.read()

            self.data = loads(raw)

        except:

            logging.critical("Failed to load config.json file!")

    def fetch(self, key):

        if not key in self.data:

            logging.warning("The key '%s' is not present in the config.json file, returning None " % key)

            return None

        return self.data[key]
