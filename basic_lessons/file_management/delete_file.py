import os
import shutil

# path = "test.txt"
#
# try:
#     os.remove(path) # delete a file
# except FileNotFoundError as e:
#     print(e)
#     print("That file was not found")

path = "folder"

try:
    #os.rmdir(path)     # delete a empty directory
    shutil.rmtree(path) # delete a directory that contains files
except FileNotFoundError as e:
    print(e)
    print("That file was not found")
except PermissionError as e:
    print(e)
    print("You do not have permission to delete that")
except OSError as e:
    print(e)
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
