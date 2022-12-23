#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
if __name__ == "__main__":

    if len(sys.argv) < 10:
        print("Недостаточно строк", file=sys.stderr)

    else:
        print("Последние 10 строк", str(sys.argv[-10::]))
