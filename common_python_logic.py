
import os
import json
# Import the custom Libraries
from datetime import datetime, timedelta


def open_read_file(file_location, local_env, filename, backend_dir=None):
    try:

        if not backend_dir:
            # Get the directory of the current script
            current_dir = os.path.dirname(__file__)

            # Move up to the backend directory
            backend_dir = os.path.abspath(os.path.join(current_dir, '..'))

        # Construct the full path to the config file
        config_path = os.path.join(backend_dir, file_location, filename + '_config.json')
        # print("config_path ::: ",config_path)

        # print("config_path: {} : {} : {} ".format(backend_dir, file_location, filename + '_config.json'))

        # Load configuration from the file_location and file
        with open(config_path) as config_file:
            config = json.load(config_file)

        # Get the configuration for the current environment
        if local_env:
            config_list_json = config.get(local_env)
        else:
            config_list_json = config

        # Failing if the file is having any issues
        if not config_list_json:
            raise ValueError("No configuration found for environment:%s", local_env)

        # print(config_list_json)
        return config_list_json

    except Exception as e:
        print("Error readfile function in commonUtility  1: {}".format(str(e)))


def open_read_file_box(filename, server=None):

    try:
        # Define the path to the config file
        resource_list = open_read_file('python_script/resources', '', 'general')

        if server:
            # Define the file path for Ubuntu
            ubuntu_resource_path = str(resource_list['ubuntu_resources_server_path']).format(SERVER = server)
        else:
            # Define the file path for Ubuntu
            ubuntu_resource_path = resource_list['ubuntu_resources_path']

        # Define the file path for Windows
        windows_resource_path = resource_list['windows_resources_path']

        # Choose the correct file path based on the operating system
        file_path = ubuntu_resource_path if os.name == 'posix' else windows_resource_path

        filename = file_path + filename + '_config.json'

        # Open the file in read mode and parse the JSON content
        with open(filename, 'r') as file:
            config_list_json = json.load(file)

        # Print the parsed JSON data
        # debug_print(config_list_json)

        # Failing if the file is having any issues
        if not config_list_json:
            raise ValueError("No configuration found for environment")

        # print(config_list_json)
        return config_list_json

    except Exception as e:
        print("Error readfile function in commonUtility  : {}".format(str(e)))