from setuptools import setup

setup(
    name='ep_base',
    entry_points={
        'ep': [
            'base_thing = ep_base.thing:BaseThing',
            'base_plugin = ep_base.plugin:BasePlugin',
        ],
    }
)
