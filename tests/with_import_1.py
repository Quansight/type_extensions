from example_dataclass import Example
import example_extension


def test_type_extension_visible():
    e = Example()
    assert e.foo() is True
    assert e.one_plus(1) == 2