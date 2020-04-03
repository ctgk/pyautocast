from collections.abc import Iterable
import doctest
import unittest

from pyautocast import CustomCast


class TestCustomCast(unittest.TestCase):

    def test_autocast(self):
        doctest.run_docstring_examples(CustomCast, None)

    def test_autocast_priority(self):
        cast1 = CustomCast()
        cast2 = CustomCast()

        def tuple2tuple(obj: tuple) -> tuple:
            if len(obj) == 0:
                raise ValueError
            elif len(obj) == 1:
                return (int(obj[0]), int(obj[0]))
            else:
                return (int(obj[0]), int(obj[1]))

        def iterable2tuple(obj: Iterable) -> tuple:
            if len(obj) == 0:
                raise ValueError
            elif len(obj) == 1:
                return (int(obj[0]), int(obj[0]))
            else:
                return (int(obj[0]), int(obj[0]))

        cast1.add_cast_rule(tuple, tuple, tuple2tuple)
        cast1.add_cast_rule(Iterable, tuple, iterable2tuple)
        cast2.add_cast_rule(Iterable, tuple, iterable2tuple)
        cast2.add_cast_rule(tuple, tuple, tuple2tuple)

        @cast1.autocast(x=tuple, y=tuple)
        def func1(x, y):
            self.assertTupleEqual((3, 7), x)
            self.assertTupleEqual((9, 9), y)

        func1((3.89, "7"), ["9", -2.5])

        @cast2.autocast(x=tuple, y=tuple)
        def func2(x, y):
            self.assertTupleEqual((3, 3), x)
            self.assertTupleEqual((9, 9), y)

        func2((3.89, "7"), ["9", -2.5])

    def test_add_cast_rule_input_type_error(self):
        mycast = CustomCast()
        with self.assertRaises(TypeError):
            mycast.add_cast_rule(1, int, int)

    def test_add_cast_rule_output_type_error(self):
        mycast = CustomCast()
        with self.assertRaises(TypeError):
            mycast.add_cast_rule(int, 1, int)

    def test_add_cast_rule_cast_func_error(self):
        mycast = CustomCast()
        with self.assertRaises(TypeError):
            mycast.add_cast_rule(int, int, "a")


if __name__ == "__main__":
    unittest.main()
