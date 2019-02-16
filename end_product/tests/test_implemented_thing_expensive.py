from end_product.implemented_thing_expensive import ImplementedThingExpensive


def test_ImplementedThingExpensive():
    # This test takes >5 seconds to run, because importing ExpensivePlugin sleeps for 5.
    thing = ImplementedThingExpensive()
    assert hasattr(thing, 'is_ready')
    assert hasattr(thing, 'is_healthy')
    assert hasattr(thing, 'do_expensive')
