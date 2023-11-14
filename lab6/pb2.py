
import os
directory_path = "testing_lab6"

# check if the directory exists
if not os.path.exists(directory_path):
    print("Directory does not exist.")
else:
    # get a list of all files in the directory
    files = os.listdir(directory_path)
    
    # loop through each file and rename it with a sequential number prefix
    for i, file in enumerate(files):
        # get the file extension
        file_extension = os.path.splitext(file)[1]
        
        # create the new file name with the sequential number prefix
        new_file_name = "file" + str(i+1) + file_extension
        
        try:
            # rename the file
            os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_file_name))
        except Exception as e:
            print(f"Error renaming file {file}: {e}")
