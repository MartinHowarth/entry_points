from ep_base.discovery import plugin_by_name
from ep_base import registry as base_registry


def test_plugin_by_name():
    BaseThing = plugin_by_name(base_registry.BaseThing)
    BasePlugin = plugin_by_name(base_registry.BasePlugin)

    from ep_base.thing import BaseThing as BaseThingImported
    from ep_base.plugin import BasePlugin as BasePluginImported

    assert BaseThing == BaseThingImported
    assert BasePlugin == BasePluginImported
