from base.discovery import plugin_by_name
from base import registry

from time import sleep

# To pretend that we're importing a really large library, like the openstack SDK.
sleep(5)


BasePlugin = plugin_by_name(registry.BasePlugin)


class ExpensivePlugin(BasePlugin):

    def do_expensive(self):
        pass
