from end_product.implemented_thing_expensive import ImplementedThingExpensive


def test_ImplementedThingExpensive():
    thing = ImplementedThingExpensive()
    assert hasattr(thing, 'is_ready')
    assert hasattr(thing, 'is_healthy')
    assert hasattr(thing, 'do_expensive')
