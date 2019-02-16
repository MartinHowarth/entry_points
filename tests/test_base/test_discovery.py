from base.discovery import plugin_by_name
from base import registry as base_registry


def test_plugin_by_name():
    BaseThing = plugin_by_name(base_registry.BaseThing)
    BasePlugin = plugin_by_name(base_registry.BasePlugin)

    from base.thing import BaseThing as BaseThingImported
    from base.plugin import BasePlugin as BasePluginImported

    assert BaseThing == BaseThingImported
    assert BasePlugin == BasePluginImported
