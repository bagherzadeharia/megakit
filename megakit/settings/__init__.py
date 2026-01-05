import importlib.util
from pathlib import Path

# Get the parent directory (megakit/)
parent_dir = Path(__file__).resolve().parent.parent

# Import settings.py as a module
settings_file = parent_dir / 'settings.py'
spec = importlib.util.spec_from_file_location("megakit.settings.base", settings_file)
settings_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(settings_module)

# Copy all public attributes to this module's namespace
for attr_name in dir(settings_module):
    if not attr_name.startswith('_'):
        globals()[attr_name] = getattr(settings_module, attr_name)
