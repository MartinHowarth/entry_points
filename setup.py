from setuptools import setup

setup(
    name='entry_points',
    packages=[
        'base',
        'expensive',
        'health',
        'ready',
    ],
    entry_points={
        'ep': [
            'base_thing = base.thing:BaseThing',
            'base_plugin = base.plugin:BasePlugin',
            'expensive = expensive.expensive:ExpensivePlugin',
            'health = health.health:HealthPlugin',
            'ready = ready.ready:ReadyPlugin',
        ],
    }
)
