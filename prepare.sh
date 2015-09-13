#!/bin/bash
python3 parse_wk.py > data/wk.vocab
python3 filter6k.py > data/6k.vocab
mkdir result
