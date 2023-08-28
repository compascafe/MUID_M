#!/usr/bin/env python3

from microprediction import new_key, MicroWriter
write_key = new_key(difficulty=11)
mw = MicroWriter(write_key=write_key)
print(write_key)
