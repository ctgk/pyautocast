#!/bin/sh

cd `git rev-parse --show-toplevel`
python setup.py clean --all
python setup.py test
exit $?
