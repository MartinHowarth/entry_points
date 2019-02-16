from setuptools import setup

setup(
    name='entry_points_health',
    packages=[
        'entry_points.plugins.health'
    ],
    entry_points={
        'ep': [
            'health = entry_points.plugins.health.health:HealthPlugin',
        ],
    }
)
