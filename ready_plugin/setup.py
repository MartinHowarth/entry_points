from setuptools import setup

setup(
    name='ready_plugin',
    entry_points={
        'ep': [
            'ready = ready_plugin.ready:ReadyPlugin',
        ],
    }
)
