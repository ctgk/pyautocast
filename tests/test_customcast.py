import doctest
import unittest

from pyautocast import CustomCast


class TestCustomCast(unittest.TestCase):

    def test_autocast(self):
        doctest.run_docstring_examples(CustomCast, None)

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
