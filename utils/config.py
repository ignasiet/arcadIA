import yaml

class ConfigFile():
    def __init__(self, dictionary):
        self.data = dictionary

    def __getattr__(self, name):
        if name in self.data:
            if isinstance(self.data[name],dict): 
                return ConfigFile(self.data[name])
            else:
                return self.data[name]
        else:
            raise Exception(f'{name} not found')

    def __call__(self):
        return str(self.data)
    
    def __str__(self):
        return "\n".join("{}\t{}".format(k, v) for k, v in self.data.items())

    def __repr__(self):
        return str(self.data)