import os
import sys

try:
    # se extrag argumentele din linia de comanda
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    if not os.path.exists(directory_path):
        raise Exception("Invalid directory path")

    for file_name in os.listdir(directory_path):
        if file_name.endswith(file_extension):
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    print(file.read())
            except Exception as e:
                print(f"Error accessing file {file_path}: {e}")
except Exception as e:
    print(f"Error: {e}")


