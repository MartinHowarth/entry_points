from setuptools import setup

setup(
    name='entry_points_expensive',
    packages=[
        'entry_points.plugins.expensive'
    ],
    entry_points={
        'ep': [
            'expensive = entry_points.plugins.expensive.expensive:ExpensivePlugin',
        ],
    }
)
