"""
Settings used by plainlegal project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from plainlegal.settings.production import *

# Import optional local settings.
try:
    from plainlegal.settings.local import *
except ImportError:
    pass