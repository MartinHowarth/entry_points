from ep_base.discovery import plugin_by_name
from ep_base import registry as base_registry
from ready_plugin import registry as ready_registry


BaseThing = plugin_by_name(base_registry.BaseThing)
ReadyPlugin = plugin_by_name(ready_registry.ReadyPlugin)


class ReadyThing(BaseThing, ReadyPlugin):

    def always_true(self):
        return True

    ready_methods = [always_true]


class UnreadyThing(BaseThing, ReadyPlugin):

    def always_false(self):
        return False

    ready_methods = [always_false]
