#!/bin/bash

if [[ ${1: -3} == ".py" ]]; then
    flake8 $1
    exit $?
fi

exit 0
