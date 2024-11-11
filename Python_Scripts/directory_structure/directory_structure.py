import os
import sys

# Symbols used to visualize the tree
horizontal: str = "\u002D"  # -
vertical: str   = "\u007C"  # |
corner: str     = "\u2514"  # └
verBranch: str  = "\u251C"  # ├

def process_arguments(arg: list[str]) -> str:
    """
    Processes command-line arguments to determine the target directory path.
    
    - If no arguments are provided, returns the current working directory.
    - If a single path argument is provided, validates the path and returns it.
    - If a flag `-u` or `--up` is provided with an integer, moves up the specified number
      of levels in the directory hierarchy starting from the current working directory.
    
    Parameters:
    - arg (list[str]): Command-line arguments passed to the script. Can accept (beyond scripts name):
        - A single path argument
        - A flag `-u` or `--up` followed by an integer (e.g., `-u 2`).
    
    Returns:
    - str: The resolved directory path based on the provided argument(s).
    
    Exits:
    - Exits with an error message if the arguments are invalid or if there are too many arguments.
    """
    # Check for too many arguments
    if len(arg) > 3:
        sys.exit(
            "Error:\tThis script accepts at most one path argument, or a flag '-u/--up' followed by a level count.\n"
            "\tIf no path or flag is specified, the current directory will be used by default."
        )

    # Default to current working directory if no argument is provided
    if len(arg) == 1:
        return os.getcwd()

    # Handle the `-u` or `--up` flag for moving up directory levels
    if arg[1] in ("-u", "--up"):
        if len(arg) == 3 and arg[2].isdigit():
            path = os.getcwd()
            levels_up = int(arg[2])
            for _ in range(levels_up):
                path = os.path.dirname(path)
            return path
        else:
            sys.exit("Error:\tThe '-u' or '--up' flag must be followed by a single integer specifying levels to go up.")
    
    # Handle a single path argument
    elif len(arg) == 2:
        target = arg[1]
        if os.path.exists(target):
            return target
        else:
            sys.exit("Error:\tThe specified path does not exist.")
    
    # Invalid input scenario
    sys.exit("Error:\tInvalid arguments. Use a path or the '-u/--up' flag with an integer.")

def get_directory_structure(path: str) -> tuple[dict, int]:
    """
    Recursively generates a dictionary representing the directory structure.
    
    Parameters:
    - path (str): The root directory path to scan.

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
            element_path = os.path.join(current_path, element)

            # Encountered directory, recurse deeper
            if os.path.isdir(element_path):
                dir_tree[element], temp_counter = build_tree(os.path.join(current_path, element))
                element_counter += temp_counter

            # Encountered file, mark with None
            elif os.path.isfile(element_path):
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
    path = process_arguments(sys.argv)

    print("Scanning directory tree...", end="\r")
    tree, counter = get_directory_structure(path)
    print(f"Directory scanned, {counter} elements found.")

    tree = tree_string(tree, 5, 0)
    print(tree)

# without files
# tabs
# excluded directories
# output to file
# help
# file docstring