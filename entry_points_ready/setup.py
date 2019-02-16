from setuptools import setup

setup(
    name='entry_points_ready',
    packages=[
        'entry_points.plugins.ready'
    ],
    entry_points={
        'ep': [
            'ready = entry_points.plugins.ready.ready:ReadyPlugin',
        ],
    }
)
