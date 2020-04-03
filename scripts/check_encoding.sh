#!/bin/bash
if [[ ! -e $1 ]]; then
    exit 1
fi
text=$(printf "%s" $(cat $1))

if [[ $1 = *[![:ascii:]]* ]]; then
    cat <<\EOF
Error: It contains non-ASCII characters.

This can cause problems if you want to work with people on other platforms.
EOF
    exit 1
fi

exit 0
