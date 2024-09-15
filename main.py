import os
import sys

# Print current working directory
print("Current working directory:", os.getcwd())

# Print all paths in sys.path
for path in sys.path:
    print("sys.path entry:", path)
