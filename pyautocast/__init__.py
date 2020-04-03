import inspect
import functools


def autocast(**cast_to: type) -> callable:
    """Decorator to automatically cast function arguments.

    Parameters
    ----------
    cast_to : type
        Specifies casting destination of arguments.

    Returns
    -------
    callable
        Function with type casting.

    Raises
    ------
    ValueError
        Raises if an argument not found in the original function.
    TypeError
        Raises if cast destination is invalid.
    """

    def _autocast(func: callable) -> callable:
        argspec = inspect.getfullargspec(func)
        arg_names = argspec.args
        for key, value in cast_to.items():
            if key not in arg_names:
                raise ValueError(
                    f"arg '{key}' not found in {func.__name__}().")
            if not isinstance(value, type):
                raise TypeError(
                    f"Cast destination of arg '{key}' in {func.__name__}() "
                    "must be an instance of type.")

        @functools.wraps(func)
        def _func_with_typecast(*args, **kwargs):
            args_casted = []
            for name, arg in zip(arg_names, args):
                if name in cast_to:
                    args_casted.append(cast_to[name](arg))
                else:
                    args_casted.append(arg)
            kwargs_casted = {}
            for name, arg in kwargs.items():
                if name in cast_to:
                    kwargs_casted[name] = cast_to[name](arg)
                else:
                    kwargs_casted[name] = arg
            return func(*args_casted, **kwargs_casted)

        _func_with_typecast.__signature__ = inspect.signature(func)
        return _func_with_typecast

    return _autocast


__all__ = [
    'autocast',
]
