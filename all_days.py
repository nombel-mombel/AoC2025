import os
import re

pattern = re.compile(r"\d\d.py")

for file in sorted(os.listdir()):
    if pattern.match(file) is not None:
        os.system(f"python3 {file}")
        print("\n")
