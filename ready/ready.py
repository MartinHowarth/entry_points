from base.discovery import plugin_by_name
from base import registry


BasePlugin = plugin_by_name(registry.BasePlugin)


class ReadyPlugin(BasePlugin):

    ready_methods = []

    def is_ready(self):
        return all(method(self) for method in self.ready_methods)
