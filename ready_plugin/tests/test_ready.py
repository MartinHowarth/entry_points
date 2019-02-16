from .dummy_things import ReadyThing, UnreadyThing


def test_is_ready():
    ready = ReadyThing()
    assert ready.is_ready()

    unready = UnreadyThing()
    assert unready.is_ready() is False

