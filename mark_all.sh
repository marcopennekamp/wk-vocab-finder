#!/bin/bash

mrk() {
    python3 mark_levels.py "$@"
}

rm -rf leveled
mkdir leveled
mrk 1-1
mrk 1-2
mrk 1-3
mrk 1-4
mrk 1-5
mrk 1-6
mrk 1-7
mrk 1-8
mrk 1-9
mrk 1-10
