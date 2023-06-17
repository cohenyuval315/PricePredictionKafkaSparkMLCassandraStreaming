from configparser import ConfigParser
from configparser import RawConfigParser

class PropertiesReader(object):

    def __init__(self, properties_file_name):
        self.name = properties_file_name
        # self.main_section = 'main'

        # # Add dummy section on top
        # self.lines = [ '[%s]\n' % self.main_section ]

        with open(properties_file_name) as f:
            self.lines.extend(f.readlines())

        # This makes sure that iterator in readfp stops
        self.lines.append('')

    def readline(self):
        return self.lines.pop(0)

    def read_properties(self):
        config = RawConfigParser()

        # Without next line the property names will be lowercased
        config.optionxform = str

        config.readfp(self)
        return dict(config.items(self.main_section))

