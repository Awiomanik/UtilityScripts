"""
A script to visualize a directory structure as a tree.

This script generates a tree representation of a directory, allowing for customization
via command-line arguments. It can show directory contents, exclude files or directories
based on a regular expression, and save the output to a file or display it in the console.
The output can be adjusted with options for indentation and the number of levels to go up
from the specified directory.

Key Features:
- Visualizes a directory structure as a tree with customizable indentation.
- Supports exclusions based on regular expressions.
- Option to exclude files and limit output to directories only.
- Ability to output the tree to a file or display it in the console.

Command-Line Arguments:
- `-h, --help`: Show usage information.
- `-p <path>, --path <path>`: Specify the root directory to visualize.
- `-u <int>, --up <int>`: Move up the directory hierarchy by the specified number of levels.
- `-f, --file`: Output the tree to a file.
- `-vt <int>`: Set the vertical tabulation (indentation) in spaces.
- `-ht <int>`: Set the horizontal tabulation (indentation) in spaces.
- `-e <regex>`: Exclude files and directories matching the given regular expression.
- `-d`: Exclude files, showing only directories.

Functions:
- `process_arguments(arg: list[str]) -> dict`: Processes the command-line arguments and returns a dictionary with the selected options.
- `get_directory_structure(path: str, includeFiles: bool, exclude_pattern: re.Pattern) -> tuple[dict, int]`: Recursively retrieves the directory structure.
- `tree_string(tree: dict, tab: int = 4, horizontal_tab: int = 0) -> str`: Converts the directory structure to a visual tree string.

"""
import os
import re
import sys

# Symbols used to visualize the tree
horizontal: str = "\u002D"  # -
vertical: str   = "\u007C"  # |
corner: str     = "\u2514"  # └
verBranch: str  = "\u251C"  # ├

def process_arguments(arg: list[str]) -> dict:
    """
    Processes command-line arguments to determine various options for directory processing.

    Parameters:
    - arg (list[str]): Command-line arguments passed to the script, can include:
        - `-h` or `--help`: Displays usage information and exits.
        - `-p` or `--path`: Sepifies path to the directory that will be visualized.
        - `-u <int>` or `--up <int>`: Moves up the specified number of levels in the directory hierarchy starting from the current or sepcified directory.
        - `-f` or `--file`: Outputs the result to a file.
        - `-vt <int>`: Sets the number of spaces to use as vertical tabs for indentation.
        - `-ht <int>`: Sets the number of spaces to use as horizontal tabs for indentation.
        - `-e <str>`: Specifies files and directories that match regular expression to be exclude from the directory listing.
        - `-d`: Excludes files from a tree limiting it to directories.

    Returns:
    - dict: A dictionary containing parsed options and values. ({"directory": str, "output2file": bool, "vertical_tab": int, "horizontal_tab": int, "excluded": str, "no_files": bool})

    Exits:
    - Displays help and exits if `-h` is specified.
    - Exits with an error message if the arguments are invalid.
    """
    options = {
        "directory": os.getcwd(),
        "output2file": False,
        "vertical_tab": 4,
        "horizontal_tab": 0,
        "excluded": None,
        "no_files": False
    }
    levels_up: int = 0

    # Display help and exit if `-h` or `--help` is provided
    if "-h" in arg or "--help" in arg:
        print("Usage: directory_structure.py [options]\n"
              "Options:\n"
              "  -h, --help               Show this help message and exit\n"
              "  -p <str> or --path <str> Specify ddirectory to be visualized\n"
              "  -u <int>, --up <int>     Create a tree for the directory up <int> levels in the directory hierarchy\n"
              "  -f, --file               Output tree to a file\n"
              "  -vt <int>                Set vertical tab size (number of spaces for indentation)\n"
              "  -ht <int>                Set horizontal tab size (number of spaces for indentation)\n"
              "  -e <str>                 Exclude files and directories that mach <str> regular expresion from the directory listing\n"
              "  -d                       Excludes files from a tree limiting it to directories")
        sys.exit()

    # Parse arguments
    i = 1
    while i < len(arg):
        if arg[i] in ("-p", "--path"):
            # Handle `-p` or `--path` flag with string
            if i + 1 < len(arg) and os.path.exists(arg[i + 1]):
                options["directory"] = arg[i + 1]
                i += 2
            else:
                sys.exit("Error: The '-p' or '--path' flag must be followed by a valid path.")

        elif arg[i] in ("-u", "--up"):
            # Handle `-u` or `--up` flag with an integer
            if i + 1 < len(arg) and arg[i + 1].isdigit():
                levels_up = int(arg[i + 1])
                i += 2
            else:
                sys.exit("Error: The '-u' or '--up' flag must be followed by an integer.")

        elif arg[i] == "-f":
            # Handle `-f` flag for output to file
            options["output2file"] = True
            i += 1

        elif arg[i] == "-vt":
            # Handle `-vt` flag for vertical tabs
            if i + 1 < len(arg) and arg[i + 1].isdigit():
                options["vertical_tab"] = int(arg[i + 1])
                i += 2
            else:
                sys.exit("Error: The '-vt' flag must be followed by an integer.")

        elif arg[i] == "-ht":
            # Handle `-ht` flag for horizontal tabs
            if i + 1 < len(arg) and arg[i + 1].isdigit():
                options["horizontal_tab"] = int(arg[i + 1])
                i += 2
            else:
                sys.exit("Error: The '-ht' flag must be followed by an integer.")

        elif arg[i] == "-e":
            # Handle `-e` flag for exclusion regex
            if i + 1 < len(arg):
                try:
                    options["excluded"] = re.compile(arg[i + 1])
                    i += 2
                except re.error as e:
                    sys.exit(f"Error: Invalid regular expression provided for exclusion: {e}")
            else:
                sys.exit("Error: The '-e' flag must be followed by a regular expression with no spaces.")

        elif arg[i] == "-d":
            options["no_files"] = True
            i += 1

        else:
            # Invalid or unsupported argument
            sys.exit(f"Error: Invalid argument '{arg[i]}'")

    # Adjust directory
    for _ in range(levels_up): 
        options["directory"] = os.path.dirname(options["directory"])

    return options

def get_directory_structure(path: str, includeFiles: bool, exclude_pattern: re.Pattern) -> tuple[dict, int]:
    """
    Recursively generates a dictionary representing the directory structure.
    
    Parameters:
    - path (str): The root directory path to scan.
    - includeFiles (bool): Whether to include files or just directories.
    - exclude_pattern (re.Pattern): Regular expression that excludes matched files and directories if mached.

    Returns:
    - tuple containing:
        - dict: A nested dictionary representing the directory structure. (None value represents a file)
        - int: An element counter.
    """
    # Recursive function to traverse the directory tree
    def build_tree(current_path: str) -> tuple[dict, int]:
        # Initial tree
        dir_tree: dict = {}
        element_counter: int = 1

        # Iterate over elements in directory
        for element in os.listdir(current_path):
            if not (exclude_pattern and re.match(exclude_pattern, element)):
                element_path = os.path.join(current_path, element)

                # Encountered directory, recurse deeper
                if os.path.isdir(element_path):
                    dir_tree[element], temp_counter = build_tree(os.path.join(current_path, element))
                    element_counter += temp_counter

                # Encountered file, mark with None
                elif includeFiles and os.path.isfile(element_path):
                    dir_tree[element] = None
                    element_counter += 1
        
        return dir_tree, element_counter
    
    tree, counter = build_tree(path)
    return {os.path.basename(path) : tree}, counter - 1 

def tree_string(tree: dict, tab: int = 4, horizontal_tab: int = 0) -> str:
    """
    Generates a visual representation of a directory structure.

    This function takes a nested dictionary representing a directory structure
    and returns a formatted string that visually represents the structure
    as a tree, using symbols to indicate branching. Files are represented
    as leaf nodes, and directories are shown with branches connecting their
    contents. Each level of the tree is indented based on the specified tab size.

    Arguments:
    - tree (dict): A nested dictionary where each key represents a directory or file.
                   Directories are represented as keys with dictionary values,
                   while files are represented as keys with `None` values.
    - tab (int): The number of characters used for indentation at each level. Default is 4.
    - horizontal_tab (int): The number of lines that separate each branch. Default is 0.

    Returns:
    - str: A string containing the visual representation of the directory tree.
    """
    # Recursive function to build tree string
    def build_string(tree: dict, prefix: str = '', depth: bool = False) -> str:
        # initial string
        tree_str: str = ''

        # iterate over elements in current directory 
        for index, element in enumerate(tree, 1):

            # Check if it's the last element
            isLast: bool = index == len(tree)
            edge: str = corner if isLast else verBranch
            
            # Insert horizontal tabulation
            for _ in range(horizontal_tab):
                tree_str += prefix + '|' + '\n'

            tree_str += f"{prefix}{edge}{horizontal * (tab-1)} {element}"

            # If it's a directory
            if tree[element] is not None:               
                # Finnish row
                tree_str += "/\n"

                # Update prefix for deeper branch
                deeper_prefix = prefix     
                if tree[element]:
                    deeper_prefix += (' ' if isLast else vertical) + ' ' * tab

                # Add sub branch
                tree_str += build_string(tree[element], deeper_prefix, True)

            # If it's a file
            else: tree_str += '\n'

        return tree_str
    
    head: str = list(tree.keys())[0]
    return head + '\n' + build_string(tree[head])

if __name__ == "__main__":
    options = process_arguments(sys.argv)

    print("Preparing directory tree for specified options:\n")
    print("Directory:\t\t", options["directory"])
    print("Output to:\t\t", "file" if options["output2file"] else "console")
    print("Vertical tabulation:\t", options["vertical_tab"], "characters")
    print("Horizontal tabulation:\t", options["horizontal_tab"], "characters")
    print("Exclude names matching:\t", options["excluded"])
    print("Exclude files:\t\t", options["no_files"])
    
    print("\nScanning directory tree...", end="\r")
    tree, counter = get_directory_structure(options["directory"], 
                                            not options["no_files"], 
                                            options["excluded"])
    print(f"Directory scanned, {counter} elements found.\n")

    tree = tree_string(tree, options["vertical_tab"], options["horizontal_tab"])

    if options["output2file"]:
        fileName:str = os.path.basename(options["directory"]) + "_directory_tree.txt"
        counter = 1
        while os.path.exists(fileName):
            fileName = f"""{os.path.basename(options["directory"])}_directory_tree({counter}).txt"""
            counter += 1

        with open(fileName, 'w', encoding="utf-8") as file:
            file.write(tree)
        
        print("Directory tree saved to", fileName)
    else:
        print(tree)
