from configparser import ConfigParser

@staticmethod
def readProperty(path,section,key):
    config = ConfigParser()
    config.read(path)
    test = config.get(section,key)
    return test

@staticmethod
def readSection(path,section):
    config = ConfigParser()
    config.read(path)
    test = config.get(section)
    return test

@staticmethod
def readPropertiesFile(path):
    config = ConfigParser()
    config.read(path)
    test = config.get()
    return test


