# /usr/bin/python

# Os level operations
import os

# Get the OS I'm in
import platform

INSTALL_PATH = ".local/bin"


def print_program_welcome():
    
    row = "=" * 35
    
    print(row)

    print("")

    print("SETUP SCRIPT OF DANIEL'S QTILE CONFIG".center(len(row), "*"))
    
    print("")
    
    print(row)

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
        print (f"Successfully created the directory {local_bin}")

def check_response(response):
    
    response = response.lower()
    
    if response == "yes":
        return True    
    elif response == "no":
        return False
    else:
        return "repeat"
    
def main():

    print_program_welcome()
    
    if not get_correct_os():
        raise OSError("Sorry Qtile is only supported in Linux") 
    
    if not check_local_folder_exists():
        print(".local/bin folder don't detected")
        print("")
        response = input("Do you want to create that directory [yes, no]>> ") 


if __name__ == "__main__":
    main()
    