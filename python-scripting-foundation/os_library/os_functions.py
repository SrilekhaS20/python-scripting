import os
#Print out Current Working Directory
cwd = os.getcwd()

print("Current Working Directory Before: ", cwd)

#Changing Directory
chdir = os.chdir("../")

cwd2 = os.getcwd()

print("Current Working Directory After", cwd2)

#Create Directory without using mode
directory = "os_dir"
path = "D:\Git_Repo\python-scripting\python-scripting-foundation\os_library"
new_dir = os.path.join(path, directory)
#Make Directory
os.mkdir(new_dir)
print("New path: ", new_dir)
#Remove Directory
os.rmdir(new_dir)
#Check if removed directory exists or not
if not os.path.exists(new_dir):
    print(f"Directory {new_dir} is removed")
else:
    print(f"Directory {new_dir} exists")

#Create Directory using mode
directory1 = "mode_dir"
path1 = "D:\Git_Repo\python-scripting\python-scripting-foundation\os_library"
mode = 0o666
new_dir1 = os.path.join(path1, directory1)
os.mkdir(new_dir1, mode)
print("New path with mode: ", new_dir1)
#Remove Directory
os.rmdir(new_dir1)
#Check if removed directory exists or not
if not os.path.exists(new_dir1):
    print(f"Directory {new_dir1} is removed")
else:
    print(f"Directory {new_dir1} exists")

#Create Directory with makedirs
directory2 = "new_dir"
path2 = "D:\Git_Repo\python-scripting\python-scripting-foundation\os_library\module"
new_dir2 = os.path.join(path2, directory2)
os.makedirs(new_dir2)
print("New path with makedirs: ", new_dir2)
#Remove Directory
os.rmdir(new_dir2)
#Check if removed directory exists or not
if not os.path.exists(new_dir2):
    print("Directory '%s' is removed" % directory2)
else:
    print("Directory '%s' exists" % directory2)

#Listing Directory & Files
path3 = "/"
dir_list = os.listdir(path3)
print("Files and Directory in '",path3,"': ", dir_list)

#Creating a file
directory3 = "D:\Git_Repo\python-scripting\python-scripting-foundation\os_library"
file_name = "file.txt"
file_path = os.path.join(directory3, file_name)
with open(file_path, "w") as f:
    f.write("This file is written using os.path.join() method")
print(f"{file_name} is created successfully in {directory3}")
#Remove the file
os.remove(file_path)
# Check if file path is present
if not os.path.exists(file_path):
    print(f"{file_name} is removed")
else:
    print(f"{file_name} exists")

#Print OS name
print(os.name)

#File rename
directory4 = "D:\Git_Repo\python-scripting\python-scripting-foundation\os_library"
file_text = "sample.txt"
file_path = os.path.join(directory4, file_text)
#sample.txt to be renamed to dummy.txt
new_file_name = "dummy.txt"
new_file_path = os.path.join(directory4, new_file_name)
#Check if sample.txt and dummy.txt file is present or not
if not os.path.exists(file_path) and not os.path.exists(new_file_path):
    with open(file_path, "w") as f:
        f.write("This file is written to rename")
    print(f"Created: {file_text}")
#Check if sample.txt is present or not
if os.path.exists(file_path):
    os.rename(file_path, new_file_path)
    print(f"{file_text} is renamed as {new_file_name}")
else:
    print(f"{file_text} cannot be renamed. It does not exist.")

#Size of the file
size = os.path.getsize(new_file_name)
print(f"Size of the file is {size} bytes")

#Getting environment
print(os.getenv("HOME"))