from pyautocast._autocast import _autocast, autocast


class CustomCast(object):
    """Class to perform custom type casting.

    Example
    -------
    >>> from pyautocast import autocast
    >>> mycast = CustomCast()
    >>> mycast.add_cast_rule(int, tuple, lambda x: (x, x))
    >>> def tuple2tuple(obj: tuple) -> tuple:
    ...     if len(obj) == 0:
    ...         raise ValueError
    ...     elif len(obj) == 1:
    ...         return (int(obj[0]), int(obj[0]))
    ...     else:
    ...         return (int(obj[0]), int(obj[1]))
    >>> mycast.add_cast_rule(tuple, tuple, tuple2tuple)
    >>> @mycast.autocast(x=tuple, y=tuple, z=tuple)
    ... def func(x, y, z):
    ...     assert(isinstance(x, tuple))
    ...     assert(len(x) == 2)
    ...     assert(isinstance(y, tuple))
    ...     assert(len(y) == 2)
    ...     assert(isinstance(z, tuple))
    ...     assert(len(z) == 2)
    >>> func(3, (3.89,), ("2", "7", "-1"))
    """

    def __init__(self):
        super().__init__()
        self._cast_rules = {}

    def add_cast_rule(
            self,
            input_type: type,
            output_type: type,
            cast_func: callable):
        """Register a type casting rule.

        Parameters
        ----------
        input_type : type
            Type of input argument.
        output_type : type
            Target type to cast to when an instance of `input_type` is given.
        cast_func : callable
            Function to convert an instance of `input_type` to `output_type`.

        Raises
        ------
        TypeError
            Raises if arg `input_type` or `output_type`
            is not an instance of type.
        """
        if not isinstance(input_type, type):
            raise TypeError(
                f"arg `input_type` in {self.add_cast_rule.__name__}() "
                "must be an instance of type.")
        if not isinstance(output_type, type):
            raise TypeError(
                f"arg `output_type` in {self.add_cast_rule.__name__}() "
                "must be an instance of type.")
        if not callable(cast_func):
            raise TypeError(
                f"arg `cast_func` in {self.add_cast_rule.__name__}() "
                "must be callable.")
        self._cast_rules[(input_type, output_type)] = cast_func

    def autocast(self, **cast_to: type):
        return _autocast(self._cast_rules, **cast_to)


__all__ = [
    'autocast',
    'CustomCast',
]
