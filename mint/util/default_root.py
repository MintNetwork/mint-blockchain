import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("MINT_ROOT", "~/.mint/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("MINT_KEYS_ROOT", "~/.mint_keys"))).resolve()
