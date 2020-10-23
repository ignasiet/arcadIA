import yaml


class ConfigFile():
    def __init__(self, dictionary):
        self.data = dictionary
        # member variable to keep track of current index
        self._n = 0

    def __getattr__(self, name):
        if name in self.data:
            if isinstance(self.data[name], dict):
                return ConfigFile(self.data[name])
            elif isinstance(self.data[name], list):
                return [ConfigFile(item) for item in self.data[name]]
            else:
                return self.data[name]
        else:
            raise Exception(f'{name} not found')

    def __contains__(self, item):
        return item in self.data

    def __getitem__(self, name):
        return self.data[name]

    # def __next__(self):
    #     ''''Returns the next value from team object's lists '''
    #     if self._n < len(self.data):
    #         result = ConfigFile(self.data.get(self._n))
    #         self._n += 1
    #         return result
    #     # End of Iteration
    #     raise StopIteration

    def __iter__(self):
        return iter(self.data.items())

    def __call__(self):
        return str(self.data)

    def __str__(self):
        if isinstance(self.data, dict):
            return "\n".join("{}\t{}".format(k, v) for k, v in self.data.items())
        else:
            return f"{self.data}"

    def __repr__(self):
        return str(self.data)