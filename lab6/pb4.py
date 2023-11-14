
import os
import sys

if len(sys.argv) != 2:
    print("Usage: python pb4.py <directory_path>")
    sys.exit(1)

directory_path = sys.argv[1]

if not os.path.isdir(directory_path):
    print(f"{directory_path} is not a directory.")
    sys.exit(1)

try:
    files = os.listdir(directory_path)
except PermissionError:
    print(f"No read permission for {directory_path}.")
    sys.exit(1)

if not files:
    print(f"{directory_path} is empty.")
    sys.exit(0)

extension_counts = {}

for file in files:
    if os.path.isfile(os.path.join(directory_path, file)):
        extension = os.path.splitext(file)[1]
        if extension in extension_counts:
            extension_counts[extension] += 1
        else:
            extension_counts[extension] = 1

for extension, count in extension_counts.items():
    print(f"{extension}: {count}")
