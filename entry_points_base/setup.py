from setuptools import setup

setup(
    name='entry_points_base',
    packages=[
        'entry_points.base',
        'entry_points.plugins',
        'entry_points.plugins.base',
    ],
    entry_points={
        'ep': [
            'base_thing = entry_points.base.thing:BaseThing',
            'base_plugin = entry_points.plugins.base.plugin:BasePlugin',
        ],
    }
)
