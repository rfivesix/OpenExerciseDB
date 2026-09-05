"""Shared library for import, build, and validation.

Placed deliberately as a separate package alongside `build/` and `import/`: `import`
is a Python keyword and cannot be an importable package name, so scripts there
cannot export modules.
"""

