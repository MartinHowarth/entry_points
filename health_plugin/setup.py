from setuptools import setup

setup(
    name='health_plugin',
    entry_points={
        'ep': [
            'health = health_plugin.health:HealthPlugin',
        ],
    }
)
