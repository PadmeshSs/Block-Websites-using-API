
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os
import sys

def get_project_root():
    """
    Returns the folder where the executable/script should consider the project root.
    When frozen by PyInstaller, resources are located in sys._MEIPASS.
    Otherwise we use this file's parent (project root).
    """
    if getattr(sys, "frozen", False):
        # When PyInstaller bundles your app, _MEIPASS points to temp dir containing bundled files.
        return Path(sys._MEIPASS)
    return Path(__file__).parent

# Compute .env path (project_root/.env)
project_root = get_project_root()
dotenv_path = project_root / ".env"

# Fallback: find_dotenv() if .env is elsewhere
if not dotenv_path.exists():
    found = find_dotenv()
    if found:
        dotenv_path = Path(found)

# Load it (silently if missing)
load_dotenv(dotenv_path=dotenv_path)

# Expose variables
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

# Optional: quick sanity check (only if you want debug)
print("Loaded env from:", dotenv_path)
print("VIRUSTOTAL_API_KEY:", bool(VIRUSTOTAL_API_KEY))
