from entry_points.base.discovery import plugin_by_name
from entry_points.plugins.base import registry as base_registry
from entry_points.plugins.ready import registry as ready_registry
from entry_points.plugins.health import registry as health_registry
from entry_points.plugins.expensive import registry as expensive_registry


BaseThing = plugin_by_name(base_registry.BaseThing)
ReadyPlugin = plugin_by_name(ready_registry.ReadyPlugin)
HealthPlugin = plugin_by_name(health_registry.HealthPlugin)


class ImplementedThingExpensive(BaseThing, ReadyPlugin, HealthPlugin):
    """Example of how to dynamically import an expensive-to-import module using entry point plugins."""

    def __init__(self):
        self._expensive = None

    def do_expensive_setup(self):
        self._expensive = plugin_by_name(expensive_registry.ExpensivePlugin)()

    def do_expensive_thing(self):
        self._expensive.do_expensive()
