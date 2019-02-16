from ep_base.discovery import plugin_by_name
from ep_base import registry


BasePlugin = plugin_by_name(registry.BasePlugin)


class HealthPlugin(BasePlugin):

    health_methods = []

    def is_healthy(self):
        return all(method(self) for method in self.health_methods)
