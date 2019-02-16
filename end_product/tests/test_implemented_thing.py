from end_product.implemented_thing import ImplementedThing


def test_ImplementedThing():
    thing = ImplementedThing()
    assert hasattr(thing, 'is_ready')
    assert hasattr(thing, 'is_healthy')
