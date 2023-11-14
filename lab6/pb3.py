
import os
import sys

try:
    # get directory path from command line argument
    directory_path = sys.argv[1]
    
    # initialize total size to 0
    total_size = 0
    
    # iterate through all files in directory and subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # get full file path
            file_path = os.path.join(root, file)
            # add file size to total size
            total_size += os.path.getsize(file_path)
    
    # display total size in bytes
    print(f"Total size of all files in directory: {total_size} bytes")
    
except IndexError:
    print("Please provide a directory path as a command line argument.")
    
except FileNotFoundError:
    print("Directory not found.")
    
except PermissionError:
    print("Permission denied to access directory or files.")    
