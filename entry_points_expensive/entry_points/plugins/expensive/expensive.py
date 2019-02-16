from entry_points.base.discovery import plugin_by_name
from entry_points.plugins.base import registry

from time import sleep

# To pretend that we're importing a really large library, like the openstack SDK.
sleep(2)


BasePlugin = plugin_by_name(registry.BasePlugin)


class ExpensivePlugin(BasePlugin):

    def do_expensive(self):
        sleep(2)
