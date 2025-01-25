"""
Module: fintel_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Derek Fintel
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standard library
import pathlib
import time
import os
import fintel_project_setup 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    for year in range (start_year, end_year +1): 
        create_folder = data_path.joinpath(str(year))
        create_folder.mkdir(exist_ok=True)
    print(f"Created folder: {create_folder}")
  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list) -> None:
    # TODO: Add docstring
    # TODO: Log the function call and its arguments
    # TODO: Implement this function and remove the temporary pass
    #pass
    '''
    Create folders from a list
    Arguments: 
    folder_list = A list of folder names to create
    '''
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")

    for create_folder in folder_list:
        create_folder = project_path.joinpath(create_folder)
        create_folder.mkdir(exist_ok=True)
    print(f"Created folder: {create_folder}")

#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create prefixed folders from a list
    Arguments:
    folder_list = A list of folder names to create
    prefix = a str added to each folder name
    '''
    print(f"FUNCTION CALLED: create_prefixed_folders with folder list={folder_list} and prefix={prefix}")

    for create_folder in folder_list:
        create_folder = project_path.joinpath(f"{prefix}{create_folder}")
        create_folder.mkdir(exist_ok=True)
        print(f"Created folder: {create_folder}")

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders every 5 seconds
    Arguments: 
    duration_seconds: int count of seconds between folder creation
    '''
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")
    folder_count = 1
    while folder_count <= 5: 
        create_folder = project_path.joinpath(f"periodic_folder_{folder_count}")
        create_folder.mkdir(exist_ok=True)
        print(f"Created folder: {create_folder}")
        folder_count += 1
        time.sleep(duration_seconds)

#####################################
# Define Function 5. Call function to force lowercase and remove spaces of folder names
# if/and statements and bool arguments to enact the changes
#####################################

def modify_elements_in_folder_str(folder_list: list, force_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Add functions for making changes to str elements in the folder names
    Arguments:
    folder_list = A list of folder names to create
    force_lowercase = Modify characters to lowercase
    remove_spaces = Delete spaces in folder names
    '''
    print(f"FUNCTION CALLED: modify_elements_in_folder_str with folder_list={folder_list}, force_lowercase={force_lowercase},remove_spaces={remove_spaces}")
    for folder_name in folder_list:
        if force_lowercase and remove_spaces:
            folder_name = folder_name.lower()
            folder_name = folder_name.replace(" ", "_")
        create_folder = project_path.joinpath(folder_name)
        create_folder.mkdir(exist_ok=True)
        print(f"Created folder: {create_folder}")

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")
    print(f"Byline: {fintel_project_setup}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs: int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 5 to force lowercase and remove spaces of folder names
    folder_count = int
    # Call your function and test these options
    regions = ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"]
    modify_elements_in_folder_str(regions, force_lowercase=True, remove_spaces=True)
    
    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.
