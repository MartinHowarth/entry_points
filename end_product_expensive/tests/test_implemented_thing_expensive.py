from end_product_expensive.implemented_thing_expensive import ImplementedThingExpensive
import time


def test_exensive_definition():
    thing = ImplementedThingExpensive()
    assert hasattr(thing, 'is_ready')
    assert hasattr(thing, 'is_healthy')


def test_expensive_setup_is_slow():
    # This test takes >2 seconds to run, because importing ExpensivePlugin sleeps for 2, but it's done dynamically
    thing = ImplementedThingExpensive()
    start_time = time.time()
    thing.do_expensive_setup()
    end_time = time.time()

    # Allow some fuzz to cope with inaccuracy of sleep
    assert end_time - start_time >= 1.9
    assert end_time - start_time < 2.1


def test_do_expensive_thing_is_slow():
    # This test takes >4 seconds to run, because importing ExpensivePlugin sleeps for 2, and do expensive sleeps for 2
    thing = ImplementedThingExpensive()
    thing.do_expensive_setup()
    start_time = time.time()
    thing.do_expensive_thing()
    end_time = time.time()

    # Allow some fuzz to cope with inaccuracy of sleep
    assert end_time - start_time >= 1.9
    assert end_time - start_time < 2.1
