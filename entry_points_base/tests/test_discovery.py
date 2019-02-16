from entry_points.base.discovery import plugin_by_name
from entry_points.plugins.base import registry as base_registry


def test_plugin_by_name():
    BaseThing = plugin_by_name(base_registry.BaseThing)
    BasePlugin = plugin_by_name(base_registry.BasePlugin)

    from entry_points.base.thing import BaseThing as BaseThingImported
    from entry_points.plugins.base.plugin import BasePlugin as BasePluginImported

    assert BaseThing == BaseThingImported
    assert BasePlugin == BasePluginImported
