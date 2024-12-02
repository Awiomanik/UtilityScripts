import os
import re
import sys
import subprocess
from collections import defaultdict # Provides default value for a nonexistent key

# Utility functions
def get_case_insensitive_item(dictionary, target_key):
    '''Retrns dictionary item that maches target_key no matter the casing'''
    for key, value in dictionary.items():
        if key.lower() == target_key.lower():
            return key, value
    return None, None  # If not found, return None for both
def get_terminal_size_windows():
    '''Returns tuple of rows and columns of a console, default None'''
    try:
        output = subprocess.check_output(['mode', 'con'], shell=True).decode('utf-8')
        lines = output.split('\n')
        for line in lines:
            if 'Lines' in line:
                rows = int(line.split(':')[1].strip())
            elif 'Columns' in line:
                columns = int(line.split(':')[1].strip())
        return rows, columns
    except:
        return None
def paginate(lines, lines_per_page):
    '''Dislays given text lines_per_page lines at the time'''
    lines -= 2
    if not lines_per_page: lines_per_page = 25
    for i in range(0, len(lines), lines_per_page):
        print('\n'.join(lines[i:i+lines_per_page]))
        print("Press arrow UP/DOWN")

        os.system('clear')

# Parameters of the script
def process_flags(argv):
    # Check if help is requested
    help_output = """
    USAGE:
    -h         Output help message
    -u 'str'   Set unit (default: MebiBytes)
    -d 'path'  Set directory (default: current)
    -t 'int'   Set bottom threshold file/directory size in kilo-bytes [kb] (default: 0)
    -e 'regex' Set regular expresion to exclude files and directories that mach it

    Accepted units:
    'bit' bits
    'b'   Bytes     = 8      bits
    'kb'  KiloBytes = 1000   Bytes  
    'mb'  MegaBytes = 1000^2 Bytes
    'gb'  GigaBytes = 1000^3 Bytes
    'tb'  TeraBytes = 1000^4 Bytes
    'kib' KibiBytes = 1024   Bytes
    'mib' MebiBytes = 2^20   Bytes 
    'gib' GibiBytes = 2^30   Bytes
    'tib' Tebibytes = 2^40   Bytes
    """
    if '-h' in argv:
        sys.exit(help_output)

    # Initialize default flag values
    flags = {'-u': 'mib', '-d': os.getcwd(), '-e': None, '-t': 0}
    
    # Check arguments for flags
    i = 1  # Skip the script name
    while i < len(argv):    
        # check for unit
        if argv[i] == '-u' and i+1 < len(argv):
            flags['-u'] = argv[i+1].lower()
            i += 1

        # check for diractory
        elif argv[i] == '-d' and i+1 < len(argv):
            flags['-d'] = argv[i+1]
            i += 1

        # check for excluding regex
        elif argv[i] == '-e' and i+1 < len(argv):
            flags['-e'] = argv[i+1]
            i += 1

         # check for size threshold
        elif argv[i] == '-t' and i + 1 < len(argv):
            try:
                flags['-t'] = int(argv[i + 1])
                i += 1
            except ValueError:
                print(f"\nInvalid size threshold: {argv[i + 1]}")
                sys.exit(help_output)

        # default case
        else: 
            print(f"\nUnknown argument or missing value: {argv[i]}")
            sys.exit(help_output)
        i += 1

    # Set variables based on flags
    # Directory
    if flags['-d']: root_folder = flags['-d']
    # Unit
    # Validate the unit
    valid_units = {'bit': 1,
                   'B': 8, 'KB': 8*1000, 'MB': 8*(1000**2), 'GB': 8*(1000**3), 'TB': 8*(1000**4),
                   'KiB': 8*1024, 'MiB': 8*(2**20), 'GiB': 8*(2**30), 'TiB': 8*(2**40)}
    unit_argument = flags['-u']
    exclude_regex = flags['-e']
    size_threshold = flags['-t'] * 1000 # bytes to kb
    correct_key, unit_value = get_case_insensitive_item(valid_units, unit_argument)

    if correct_key is not None:
        return root_folder, correct_key, unit_value, exclude_regex, size_threshold
    else:
        print(f"Invalid unit: {unit_argument}\n{help_output}")
        sys.exit()

# Returns list of folders sorted by size (descending)
def list_folder_sizes(flags):
    print("\nParsing folder...", end='\r')

    root_folder, unit_abbreviation, unit_divider, exclude_regex, size_threshold = flags
    folder_sizes = defaultdict(int)
    compiled_regex = re.compile(exclude_regex) if exclude_regex else None
    
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Exclude files and directories matching the regex
        if compiled_regex:
            dirnames[:] = [d for d in dirnames if not compiled_regex.search(d)]
            filenames = [f for f in filenames if not compiled_regex.search(f)]

        # Calulate size
        folder_size = sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)
        
        # Add this folder's size to all its parents
        while dirpath != root_folder:
            folder_sizes[dirpath] += folder_size
            dirpath = os.path.dirname(dirpath)
            
        folder_sizes[root_folder] += folder_size  # Add to root folder

    # Applying the threshold size
    filtered_folders = { folder: size for folder, size in folder_sizes.items() if size >= size_threshold }
        
    print("All needed information gattered.\n")

    # Sort by size and return
    print("Sorting elements...", end= '\r')
    folders_table = []
    for folder, size in sorted(filtered_folders.items(), key=lambda x: x[1], reverse=True):
        folders_table += [f"{(size*8)//unit_divider} {unit_abbreviation}:\t{folder}"]

    print("All elements sorted.  \n")
    return folders_table

# Execute
flags = process_flags(sys.argv)
list = list_folder_sizes(flags)
rows, col = get_terminal_size_windows()
if col: list = [l[:col-10] for l in list]

print("\n<------------ ", flags[0], " content sorted by size ------------>\n\n")
for l in list: print(l)

sys.exit()
