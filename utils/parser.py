import yaml
from utils.config import ConfigFile


class Parser():
    def __init__(self, filename):
        self.loadFile(filename)
    
    def loadFile(self, filename)
        # instantiate
        with open(filename, 'r') as stream:
            config = yaml.safe_load(stream)    
        self.configurations = ConfigFile(config)
    
    