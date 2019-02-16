from setuptools import setup

setup(
    name='expensive_plugin',
    entry_points={
        'ep': [
            'expensive = expensive_plugin.expensive:ExpensivePlugin',
        ],
    }
)
