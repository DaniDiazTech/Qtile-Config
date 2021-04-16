# /usr/bin/python

# Os level operations
import os
from getpass import getuser

# Determinates if the program is installed
from shutil import which

# Get the OS I'm in
import platform

INSTALL_PATH = ".local/bin"


def print_program_welcome():
    
    row = "=" * 55

    sep = "||"

    welcome = "SETUP SCRIPT OF DANIEL'S QTILE CONFIG".center(len(row) - len(sep) * 2)

    welcome = sep + welcome + sep
     
     
    print(row)

    print("")


    print(welcome)
    
    print("")
    
    print(row + "\n")

    print(f"Hi there {getuser()}, you are about to setup Qtile".center(len(row)))
    
    print("\n" + row)


def print_current_dir():
    print(f"Currently you are in {os.getcwd()} directory")

def get_correct_os():
    """
    Returns the Os name:
    
    get_os -> bool
    
    Linux: linux
    Mac: darwin
    Windows: windows 
    """
    os = platform.system().lower()

    return os == "linux"


def get_home_path():
    """
    Get Linux home path

    get_home_path -> str
    """
    return os.path.expanduser("~")

def get_local_bin(home):
    """
    Returns the local bin path of the User
    """
    return f"{home}/.local/bin"

def check_local_folder_exists():
    """
    Check if .local/bin exists
    """
    home = get_home_path()

    local = get_local_bin(home)

    return os.path.exists(local)


def create_local_install_folder(local_bin):
    """
    Creates local bin folder
    """
    print("")
    print(f"Creating folder ar {local_bin}")
    print("")

    try:
        os.mkdir(local_bin)
    except OSError:
        raise OSError(f"Creation of the directory {local_bin} failed")
    else:
        print(f"Successfully created the directory {local_bin}")

def get_response(message="yes/no"):
    """
    returns -> bool
    """
    while True:
        response = input(message).lower()
     
        if response == "yes":
            return True    
        elif response == "no":
            return False
        else:
            print("\nSorry your response must be yes or no\n")
            continue
        

LOCAL_BIN = get_local_bin(get_home_path())

def link_scripts(path):
    
    path = os.path.abspath(path) 
    if not os.path.exists(path):
        raise OSError("Sorry that path doesn't exist")


    os.chdir(path)

    i = 0


    for file_ in os.listdir(path):
        file_path = os.path.abspath(file_)
        
        file_name = file_.split(".")[0] 
        
        link_path = LOCAL_BIN + f"/{file_name}"

        if os.path.exists(link_path):
            print("You have already in path", file_name)        
            continue
        
        os.link(file_path, link_path)

        i += 1

    return f"Linked {i} files to .local/bin"


def get_dependencies(software_path="software.txt"):
    """software_path -> path of software.txt
    
    returns list of dependencies
    """
    
    if not os.path.exists(software_path): 
        print(f"The file {software_path} wasn't found. Please clone again or provide one")
        
        if get_response("Continue without dependencies warnings? [yes/no]"):
            print("Dependencies won't be shown")
            return None
        else:
            print("Clone again or provide a file.")
            exit()

    software = []    
    
    with open(software_path, "r") as file_:
        for line in file_:
            software.append(line.strip())
   
    return software 

def check_dependencies(dependencies=None):
    """dependencies ->  list
    
    returns -> str programs that aren't installed
    """
    if dependencies is None:
        return ""
    
    not_installed = []

    for program in dependencies:
        if which(program) is not None:
            continue

        not_installed.append(program)
    
    first_row = "The following software is not installed, some scripts may not work\n" 

    if not_installed: 
        return first_row + "\n".join(not_installed)
    else:
        return ""

def main():
    
    print_program_welcome()
    
    if not get_correct_os():
        raise OSError("Sorry Qtile is only supported in Linux") 
    
    if not check_local_folder_exists():
        print("\n.local/bin folder doesn't exists\n")

        response = get_response(message="Do you want to create that directory [yes, no] >> ") 

        if not response:
            print("Setup can't continue if .local/bin doesn't exists")
            print("Rerun the script or set up the scripts manually")
            exit()

        print("Creating .local/bin/folder")
        create_local_install_folder(LOCAL_BIN)
    
    
    dependencies = get_dependencies() 
    scripts_path = "./scripts"
    print(check_dependencies(dependencies=dependencies)) 
    print(link_scripts(path=scripts_path))

    
if __name__ == "__main__":
    main()
    