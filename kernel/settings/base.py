from pathlib import Path

from utils import get_settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
config = get_settings()
