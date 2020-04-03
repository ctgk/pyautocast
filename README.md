# pyautocast
Python library to automatically cast function arguments using decorator.

## Install

```bash
git clone git+https://github.com/ctgk/pyautocast.git
```

## Usage

```py
>>> from pyautocast import autocast
>>> @autocast(x=str)
... def func(x):
...     assert(isinstance(x, str))
...     return "arg 'x' in func() is " + x
...
>>> func(2)
"arg 'x' in func() is 2"
>>> func([1, 2, 3])
"arg 'x' in func() is [1, 2, 3]"
```

## Develop

```bash
$ git clone https://github.com/ctgk/pyautocast.git
$ cd pyautocast
$ ./scripts/setup_hooks.sh
$ pip install -e .[develop]
```
