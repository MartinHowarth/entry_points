from .dummy_things import HealthyThing, UnhealthyThing


def test_is_healthy():
    healthy = HealthyThing()
    assert healthy.is_healthy()

    unhealthy = UnhealthyThing()
    assert unhealthy.is_healthy() is False

