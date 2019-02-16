from ep_base.discovery import plugin_by_name
from ep_base import registry as base_registry
from ready_plugin import registry as ready_registry
from health_plugin import registry as health_registry


BaseThing = plugin_by_name(base_registry.BaseThing)
ReadyPlugin = plugin_by_name(ready_registry.ReadyPlugin)
HealthPlugin = plugin_by_name(health_registry.HealthPlugin)


class ImplementedThing(BaseThing, ReadyPlugin, HealthPlugin):
    pass
