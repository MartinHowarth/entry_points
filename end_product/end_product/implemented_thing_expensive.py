from base.discovery import plugin_by_name
from base import registry as base_registry
from ready import registry as ready_registry
from health import registry as health_registry
from expensive import registry as expensive_registry


BaseThing = plugin_by_name(base_registry.BaseThing)
ReadyPlugin = plugin_by_name(ready_registry.ReadyPlugin)
HealthPlugin = plugin_by_name(health_registry.HealthPlugin)
ExpensivePlugin = plugin_by_name(expensive_registry.ExpensivePlugin)


class ImplementedThingExpensive(BaseThing, ReadyPlugin, HealthPlugin, ExpensivePlugin):
    pass
