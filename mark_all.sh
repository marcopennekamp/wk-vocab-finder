#!/bin/bash

mrk() {
    python3 mark_levels.py "$@"
}

rm -rf leveled
mkdir leveled

for c in `seq 1 6`; do
    for s in `seq 1 10`; do
        mrk $c-$s
    done
done
