"""
File: main.py
Author: Sam Nolan
Email: sam.nolan@rmit.edu.au
Github: https://github.com/Hazelfire
Description: quickconfig starting point.
"""

import os
import yaml

class Config:
    """ Represents a yaml configuration file for a program """
    def __init__(self, program_name, defaults=None):
        """
        Initialises a new config file,
        takes a program name and default configuration as arguments
        """
        if not defaults:
            defaults = {}
        self.directory = os.path.expanduser("~/.config/" + program_name)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.conf_file = self.directory + "/conf.yaml"
        if not os.path.exists(self.conf_file):
            self.config = defaults
            with open(self.conf_file, "w") as f:
                f.write(yaml.dump(defaults))
        else:
            self.config = yaml.load(f.read())

    def __getitem__(self, key):
        return self.config[key]

    def __setitem__(self, key, value):
        self.config[key] = value
        with open(self.conf_file, "r") as f:
            f.write(yaml.dump(self.config))

    def __contains__(self, item):
        return item in self.config
