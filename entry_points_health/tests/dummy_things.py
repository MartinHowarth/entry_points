from entry_points.base.discovery import plugin_by_name
from entry_points.plugins.base import registry as base_registry
from entry_points.plugins.health import registry as health_registry


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
