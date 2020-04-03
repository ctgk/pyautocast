import unittest

from pyautocast import autocast


class TestAutocast(unittest.TestCase):

    def test_autocast(self):

        @autocast(x=float)
        def func(x, y):
            self.assertIsInstance(x, float)
            self.assertIsInstance(y, str)

        func("3.4", "abc")

    def test_autocast_name_error(self):

        with self.assertRaises(ValueError):

            @autocast(y=tuple)
            def func(x):
                pass

    def test_autocast_type_error(self):

        with self.assertRaises(TypeError):

            @autocast(x=1)
            def func(x):
                pass

    def test_autocast_cast_error(self):

        @autocast(x=int)
        def func(x):
            pass

        with self.assertRaises(ValueError):
            func("abc")


if __name__ == "__main__":
    unittest.main()
