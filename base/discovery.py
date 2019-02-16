import pkg_resources

from .exceptions import PluginNotFoundError
from .registry import PLUGIN_ENTRYPOINT_NAME


def all_plugins():
    plugins = {}
    for entry_point in pkg_resources.iter_entry_points(PLUGIN_ENTRYPOINT_NAME):
        # try:
        # Don't `.load()` here to prevent hitting import loops.
        plugins[entry_point.name] = entry_point
        # except ImportError:
        #     # If a plugin definition relies on another plugin definition, then we need to discover the
        #     # original plugin before the second can be `.load()`ed above - causing an ImportError.
        #     # Therefore we catch this ImportError and put the onus on the user to make sure they don't cause
        #     # import loops themselves.
        #     print("%s: not available yet" % entry_point.name)
    print(plugins)
    return plugins


def plugin_by_name(name):
    plugin = all_plugins().get(name)
    if plugin is None:
        raise PluginNotFoundError(name)
    return plugin.load()
