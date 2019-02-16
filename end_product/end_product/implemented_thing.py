from entry_points.base.thing import BaseThing
from entry_points.plugins.ready.ready import ReadyPlugin
from entry_points.plugins.health.health import HealthPlugin


class ImplementedThing(BaseThing, ReadyPlugin, HealthPlugin):
    pass
