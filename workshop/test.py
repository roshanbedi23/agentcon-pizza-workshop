
import os
from pathlib import Path

documents_dir = Path(__file__).parent / "documents"

print("Documents dir:", documents_dir)
print("Exists:", documents_dir.exists())

