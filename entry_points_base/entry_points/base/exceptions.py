class PluginNotFoundError(Exception):
    def __init__(self, name):
        self.plugin = name
