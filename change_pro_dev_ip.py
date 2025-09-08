import os
import re

def find_files_with_postgres(root_dir='.'):
    matching_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if '_postgres' in file:
                matching_files.append(os.path.join(root, file))
    return matching_files

def update_all_project_name_configs(root_directory, ip_map, ip_for):
    try:
        # List all subdirectories that start with 'project_name'
        project_name_config_file = find_files_with_postgres(root_directory)
        print("project_name_config_file :: ",project_name_config_file)

        if not project_name_config_file:
            print("No folders starting with 'project_name' found.")
            return

        for config_path in project_name_config_file:
            print("config_path :: ",config_path)
            
            if not os.path.isfile(config_path):
                print(f"[SKIP] Config file not found: {config_path}")
                continue

            file_name_list = config_path.split('/')
            last_file_name = file_name_list[-1]

            print("last_file_name ::: ",last_file_name)

            last_file_name = last_file_name.split('_', 1)

            print("last_file_name :: ",last_file_name)

            start_with = last_file_name[0]

            # pass not Use migrate for these projects
            if start_with in ['project 3', 'project 4']:
                continue

            ip = ip_map[ip_for+ '-' + start_with]

            try:
                # Read and update the config file
                with open(config_path, 'r') as file:
                    content = file.read()

                updated_content = re.sub(
                    r'("db_host"\s*:\s*)"(.*?)"',
                    r'"db_host":"{IP}"'.format(IP=ip),  # Replace with your target IP
                    content
                )

                with open(config_path, 'w') as file:
                    file.write(updated_content)

                print(f"[UPDATED] {config_path}")
            except Exception as e:
                print(f"[ERROR] Failed to process {config_path}: {e}")

    except Exception as e:
        print(f"[FATAL ERROR] {e}")

map_ip_server = {'dev-project 1':'192.168.111111.111111', 'prod-project 2':'192.168.111111.222222', 
                 'dev-project 1':'192.168.111111.111111', 'prod-project 2':'192.168.111111.222222',
                 'dev-project 1':'192.168.111111.111111', 'prod-project 2':'192.168.111111.222222',
                 }

# Set your base directory here
root_directory = "/home/stanley/project_name/dev/project_name_resources"
ip_for = "dev"
update_all_project_name_configs(root_directory, map_ip_server, ip_for)

# Set your base directory here
root_directory = "/home/stanley/project_name/prod/project_name_resources"
ip_for = "prod"
update_all_project_name_configs(root_directory, map_ip_server, ip_for)
