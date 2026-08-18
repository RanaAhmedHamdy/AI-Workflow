#!/usr/bin/env python3
"""Backward-compatible entry point for tools/install.py.

Despite the historical filename, this now performs the full bootstrap by
default. Pass --skills-only to retain the old skills-only behavior.
"""
from install import main


if __name__ == "__main__":
    raise SystemExit(main())
