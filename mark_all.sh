#!/bin/bash

mrk() {
    python3 mark_levels.py "$@"
}

rm -rf leveled
mkdir leveled
mrk 1-1
