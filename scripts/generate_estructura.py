"""Genera el diagrama de estructura del proyecto (HTML + Playwright)."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "export_estructura.py"

if __name__ == "__main__":
    subprocess.run([sys.executable, str(SCRIPT)], check=True)
