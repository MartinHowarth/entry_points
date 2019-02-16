from ep_base.discovery import plugin_by_name
from ep_base import registry as base_registry
from health_plugin import registry as health_registry


BaseThing = plugin_by_name(base_registry.BaseThing)
HealthPlugin = plugin_by_name(health_registry.HealthPlugin)


class HealthyThing(BaseThing, HealthPlugin):

    def always_true(self):
        return True

    health_methods = [always_true]


class UnhealthyThing(BaseThing, HealthPlugin):

    def always_false(self):
        return False

    health_methods = [always_false]
