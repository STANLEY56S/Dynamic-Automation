import os
import shutil
 
# project main folder path
path1 = "C:\\Users\\Stanley Parmar\\OneDrive\\Desktop\\WORK\\project_name\\"
 
# list out the project of project_name
files = [ f for f in os.listdir(path1) if str(f).startswith('project_name_') ]
 
# loop over the files
for file_name in files:
    # join path foe project and git
    file_remove_path = os.path.join(path1, file_name, '.git')
 
    # print("file_remove_path :: ",file_remove_path)
 
    if os.path.isdir(file_remove_path):
 
        # remove os path for .git file
        shutil.rmtree(file_remove_path)