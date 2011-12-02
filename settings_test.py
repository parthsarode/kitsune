# The test system uses this to override settings in settings.py and
# settings_local.py with settings appropriate for testing.

# Make sure the doctypes (the keys) match the doctypes in ES_INDEXES
# in settings.py and settings_local.py.
ES_INDEXES = {'default': 'sumo_test'}

# This makes sure we only turn on ES stuff when we're testing ES
# stuff.
USE_ELASTIC = False
