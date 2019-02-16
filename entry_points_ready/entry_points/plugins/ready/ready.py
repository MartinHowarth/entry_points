from entry_points.base.discovery import plugin_by_name
from entry_points.plugins.base import registry

BasePlugin = plugin_by_name(registry.BasePlugin)


class ReadyPlugin(BasePlugin):

    ready_methods = []

    def is_ready(self):
        return all(method(self) for method in self.ready_methods)
