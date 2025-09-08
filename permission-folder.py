import os
import json
import re
import subprocess

def get_Permission_folder(root_path, root_permission_directory):
    

    # List all subdirectories that start with 'project_name'
    project_name_folders = [f for f in os.listdir(root_path) if f.startswith('project_name') and os.path.isdir(os.path.join(root_path, f))]

    for folder in project_name_folders:

        if str(folder).startswith('project_name'):

            config_path = os.path.join(root_path, folder, "backend", "resources", "general_config.json")

            if not os.path.isfile(config_path):
                print(f"[SKIP] Config file not found: {config_path}")
                continue

            try:

                # Read and update the config file
                with open(config_path, 'r') as file:
                    config = json.load(file)

                folder_path = config['log_path']

                print("folder_path ::: ",folder_path)
                if not os.path.exists(folder_path):
                    try:
                        subprocess.run(["sudo", "mkdir", "-p", folder_path], check=True)
                        # os.makedirs(folder_path)
                        print(f"✅ Folder created: {folder_path}")
                    except Exception as e:
                        print(f"❌ Error creating folder {folder_path}: {e}")

                # Convert 777 to octal (0o777) and apply it
                # os.chmod(folder_path, 0o777)
                subprocess.run(["sudo", "chmod", "777", folder_path], check=True)
                print(f"✅ Permissions changed to 777 for: {folder_path}")

            except Exception as e:
                print(f"❌ Error changing permissions for {folder_path}: {e}")



# Set your base directory here
root_directory = "/home/stanley/{project_name}"
root_permission_directory = '/var/log'
get_Permission_folder(root_directory, root_permission_directory)