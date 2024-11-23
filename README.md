# Utility Scripts Repository

## Description

This repository is a compilation of various scripts I've created as part of my programming learning journey. These scripts are not interconnected but instead serve individual purposes that range from file comparison, disk space analysis, to secure password generation.

Please note that these scripts are shared for educational purposes. They were created to help me with tasks I encounter along the way and even though they worked as I intended they are merely examples of my progress in coding and are provided "as is" without warranties. They may not always function as intended on your machine, and their safety is not guaranteed. Users are advised to review the code and use it at their own discretion.

## Scripts:

- Python Scripts:
    - [file_diff](#file_diffpy) – Compare two files and generate a detailed difference report.
    - [loading_bar](#loading_barpy) – Provides a visual loading bar for progress tracking.
    - [folder_size_analyzer](#folder_size_analyzerpy) – Analyzes and displays folder sizes within a specified directory.
    - [directory_structure](#directory_structurepy) – Visualize a directory structure as a tree with command-line options.
    </br>
- C++ Scripts:
    - [break_reminder](break_remindercpp) - Displays timed notifications for work and break intervals.
    </br>
- CMD Scripts:
    - [delayed_shoutdown](#delayed_shoutdowncmd) - Schedule a system shutdown at a specific time with a live countdown.
    - [system_info](#system_infocmd) - Display detailed system, hardware, and network information.
</br>

#### Repository Tree

```
UtilityScripts/
|
├---- .git/
|     └---- ...
|
├---- CMD_Scripts/
|     ├---- delayed_shoutdown.cmd
|     └---- system_info.cmd
|
├---- cpp_Scripts/
|     └---- break_reminder/
|           └---- break_reminder.exe
|
├---- Python_Scripts/
|     ├---- directory_structure/
|     |     └---- directory_structure.py
|     |
|     ├---- file_diff/
|     |     ├---- file_diff.py
|     |     ├---- pyproject.toml
|     |     └---- __init__.py
|     |
|     ├---- google_takeout_parser/ (Still in development)
|     |     ├---- google_takeout_parser.py
|     |     ├---- pyproject.toml
|     |     └---- __init__.py
|     |
|     ├---- loading_bar/
|     |     ├---- loading_bar.py
|     |     ├---- pyproject.toml
|     |     ├---- setup.py
|     |     └---- __init__.py
|     |
|     └---- size_of_folders/
|           ├---- pyproject.toml
|           ├---- size_of_folders.py
|           └---- __init__.py
|
├---- pyproject.toml
├---- LICENSE
└---- README.md
```
*Files and folders with 'TST' in their name will be treated as testing ones and thus will be ignored by git.*

</br>

### CMD Scripts

#### `delayed_shutdown.cmd`:
></br>
> A script to schedule a system shutdown at a user-specified time, with a live countdown and options to cancel or exit the program.</br></br>
>
> **Functionality:**
> - **Time Setup**: Allows the user to set a shutdown time in `HH:MM:SS` format.
> - **Live Countdown**: Displays the time remaining until shutdown in real-time.
> - **User Interaction**: Provides options to cancel the shutdown or exit the script without canceling the scheduled task.
> - **Immediate Shutdown**: Includes an option to shut down the system immediately.
>
> **Features**:
> - Supports scheduling shutdowns for the same day or the next day.
> - Automatically adjusts for the next-day scenario if the shutdown time is earlier than the current time.
> - Offers an interactive interface during the countdown.
>
> **Example Usage**:
> ```console
> delayed_shutdown.cmd
> ```
> When run, the script prompts the user to enter the desired shutdown time or choose to shut down immediately. The remaining time is displayed in real-time.
></br>

#### `system_info.cmd`:
></br>
> A script that gathers and displays detailed information about the operating system, hardware, and network configuration. </br></br>
>
> **Functionality:**
> - **Operating System Details**: Displays OS name and version.
> - **Hardware Information**: Shows BIOS type, CPU name, and total physical memory.
> - **Network Configuration**: Lists IPv4 and IPv6 addresses of active adapters.
> - **Battery Status**: (For laptops) Displays the remaining battery charge.
> - **Disk Information**: Shows free and total disk space for all drives.
>
> **Features**:
> - Outputs system information in a clean, structured format.
> - Automatically detects missing hardware (e.g., no battery on desktops).
> - Portable and runs on any Windows machine without additional dependencies.
>
> **Example Usage**:
> ```console
> system_info.cmd
> ```
> The script outputs all system details to the console in a structured format.
></br>

</br>

### C++ Scripts

#### `break_reminder.cpp`:
></br>Command-line utility to help maintain a healthy work-break schedule. Displays timed reminders for work and break intervals.
>
> **Functionality:**
> - **Interval Setup**: Allows users to set custom durations for work and break intervals, with defaults of 45 minutes for work and 15 minutes for breaks. </br></br>
> - **Reminders**: Notifies the user with a console message and a system pop-up at the end of each interval.</br></br>
> - **Exit Option**: The program runs continuously in the background but can be terminated in a controled manner by pressing Enter.
>
> **Features**:
> - Default values for work and break intervals.
> - Customizable settings for each session.
> - Clean exit mechanism via Enter key detection.
> - Lightweight and works across Windows systems.
>
> **Example Usage**:
>```console
>break_reminder.exe
>```
> When run, the program prompts the user to set work and break intervals or accept defaults. It notifies the user at the end of each interval with a pop-up message.
></br>

</br>

### Python Scripts

#### `file_diff.py`:
></br>Command-line tool. Compare two files and generate a detailed report of the differences between them.
>
> **Functionality:**
> - **Argument Verification**: The script starts by checking if the correct number of arguments is passed. It requires exactly two file paths. It verifies the existence of the provided file paths. Compares the MIME types of both files to ensure they are the same before proceeding with the comparison.</br></br>
> - **Difference Report Creation**: It uses the `difflib.Differ` class to compute the differences and creates a human-readable report.</br></br>
> - **Overwrite Protection**: The script outputs the differences to a new file named using a combination of the input file names. If a file with the same name exists, it will append a numeral to ensure uniqueness.
>
> **Example Usage:** 
>```console
> python file_diff.py path/to/file1 path/to/file2
>``` 
>
>( The files to be compared must be text-based and have the same MIME type ) </br></br>

#### `loading_bar.py`:
></br>Command-line tool. Provides a visual loading bar that updates in real-time, useful for monitoring progress in time-consuming tasks.<br>
> **Functionality:**
> - **Initialization**: Sets up the loading bar with the total number of iterations and optional additional information for display.
> - **Progress Updates**: The loading bar is updated with each iteration, showing current progress, average time per iteration, and estimated time remaining.
> - **Completion Display**: At the end of the task, the loading bar displays the total time taken and allows for optional additional messages.
>
> **Methods**:
> - `update`: Updates the loading bar with the current iteration, estimated time remaining, and optional additional details about the task.
> - `close`: Finalizes the display by showing the total time and can clear the loading bar from the console.</br>
>
> **Example Usage**:
> ```python
> from loading_bar import LoadingBar
> import time
> 
> bar = LoadingBar(total=100)
> for i in range(100):
>     time.sleep(0.1)  # Simulate a task
>     bar.update(i + 1)
> bar.close()
> ```
>The script provides a customizable loading bar to visualize progress in console applications. To use, import `LoadingBar`, initialize with a total count, and update the bar in each iteration:
>
>The loading bar displays progress, average time, and estimated time to completion.
></br>

#### `folder_size_analyzer.py`:
></br>Command-line tool. Analyzes and lists folder sizes within a specified directory, allowing for unit customization (e.g., bytes, KB, MB). Useful for disk usage analysis.<br>
> **Functionality:**
> - **Directory and Unit Customization**: Allows the user to specify a target directory (`-d`) and unit (`-u`) to display folder sizes, with support for units from bits to tebibytes.
> - **Folder Size Calculation**: Recursively calculates folder sizes and presents them in descending order by size.
>
> **Methods:**
> - `get_case_insensitive_item`: Searches for a unit in a case-insensitive manner.
> - `get_terminal_size_windows`: Determines terminal size on Windows to adjust output display.
> - `paginate`: Handles paginated output for large lists.
> - `list_folder_sizes`: Returns a list of folder sizes in descending order.
>
> **Example Usage:**
>The script calculates the sizes of all folders in a directory and lists them by size. You can specify the directory and the unit for display with the `-d` and `-u` flags:
> ```bash
> python folder_size_analyzer.py -d /path/to/directory -u MB
> ```
>Supported units: `bit`, `B`, `KB`, `MB`, `GB`, `TB`, `KiB`, `MiB`, `GiB`, `TiB`. By default, it uses the current directory and MiB.
></br>

#### `directory_structure.py`:
></br>
>A script to visualize a directory structure as a tree.
></br></br>
>This script generates a tree representation of a directory, allowing for customization via command-line arguments. It can show directory contents, exclude files or directories based on a regular expression, and save the output to a file or display it in the console. The output can be adjusted with options for indentation and the number of levels to go up from the specified directory.</br></br>
>
>**Key Features:**
>- **Visualizes a directory structure as a tree with customizable indentation.**
>- **Supports exclusions based on regular expressions.**
>- **Option to exclude files and limit output to directories only.**
>- **Ability to output the tree to a file or display it in the console.**
>
>**Command-Line Arguments:**
>- `-h, --help`: Show usage information.
>- `-p <path>, --path <path>`: Specify the root directory to visualize.
>- `-u <int>, --up <int>`: Move up the directory hierarchy by the specified number of levels.
>- `-f, --file`: Output the tree to a file.
>- `-vt <int>`: Set the vertical tabulation (indentation) in spaces.
>- `-ht <int>`: Set the horizontal tabulation (indentation) in spaces.
>- `-e <regex>`: Exclude files and directories matching the given regular expression.
>- `-d`: Exclude files, showing only directories.
>
>**Functions:**
>- `process_arguments(arg: list[str]) -> dict`: Processes the command-line arguments and returns a dictionary with the selected options.
>- `get_directory_structure(path: str, includeFiles: bool, exclude_pattern: re.Pattern) -> tuple[dict, int]`: Recursively retrieves the directory structure.
>- `tree_string(tree: dict, tab: int = 4, horizontal_tab: int = 0) -> str`: Converts the directory structure to a visual tree string.
>
>**Example Usage:**
>```console
>python directory_structure.py -p /path/to/directory -d -vt 4 -ht 2 -e ^~.*|.*\.tmp$ -f
>```
>(Generates a directory-only tree with custom vertical and horizontal tab spacing, excludes temporary files and saves it into a file.)
></br>

## Usage

Each script can be run independently. 
For Python scripts, you'll need to have Python installed on your system. For detailed usage instructions, refer to the list above, individual script files and [guide](#general-usage-guide-python) below.
For C++ scripts, you'll need to compile scripts to binary executable compatible with your system. For more details refer to the [guide](#general-usage-guide-c) below.
CMD scripts require no instalation.

#### **General Usage Guide** (CMD)

CMD scripts are self-contained and require no compilation or installation. Simply run the script directly by clicking it in GUI or from the terminal:

**Example:**
```console
system_info.cmd
```
For interactive scripts like delayed_shutdown.cmd, follow the on-screen prompts to schedule or cancel the shutdown.
#### **General Usage Guide** (C++)

**Compilation**
To run the `C++` utilities, compile the `*.cpp` files (if not already compiled) to executable files. For example:
```bash
g++ -o break_reminder break_reminder.cpp
```

**Execution**
Then execute the resulting binary. For example:
```console
break_reminder.exe
```

#### **General Usage Guide** (Python)

#### 1. Instalation 
Most scripts are structured as a self-contained packages with their own `pyproject.toml` and `__init__.py` files. To install them individually or together, you can use Poetry, or simply link them directly if they are added as submodules in another project.

**a) Installing Individual Scripts**
To install a single script, navigate to its directory and use Poetry to set it up:
```bash
cd UtilityScripts/Python_Scripts/<script_folder>
poetry install
```
This command installs the script and any dependencies specified in the `pyproject.toml` file.
</br>

**b) Adding dependencies**
You can add any of these scripts as dependencies in other projects using `Poetry`:

1. In the target project, open the `pyproject.toml`.
2. Add a path dependency to each script:
```toml
[tool.poetry.dependencies]
loading_bar = { path = "../UtilityScripts/Python_Scripts/loading_bar" }
```
3. Pull the dependencies using `Poetry`:
```bash
poetry install
```
</br>

**c) Importing Utility Scripts in other projects**
After installation, import functions from your script like this:
```python
from loading_bar import LoadingBar
bar = LoadingBar(total=100)
```
</br>

#### 2. Running Scripts Directly
Each script can also be run directly from the command line. Ensure you’re in the relevant directory and use Python to execute:
```bash
python folder_size_analyzer.py
```

#### 3. Adding to `PATH` for Global Command Access
To make these scripts accessible from any directory in the terminal:

Add the scripts' folder path to your system's PATH environment variable.
Create an alias for each command in your shell configuration:
Example:
```bash
alias filediff="python /path/to/UtilityScripts/Python_Scripts/file_diff/file_diff.py"
```

## Contributing

Contributions to this project are welcome! If you have improvements or bug fixes, please feel free to fork the repository and submit a pull request.
I encourage contributors to extend the compatibility of the Windows-specific scripts to other platforms (e.g., Linux, macOS) by using cross-platform libraries for notifications.

## License

This project is open source and available under the Apache v.2.0 [LICENSE](LICENSE).

## Disclaimer

These scripts are personal learning projects and may not be optimized for production use. The author is not responsible for any damage or data loss incurred through the use of these scripts.
Some of these scripts, such as `loading_bar.py`, are designed to assist with performance monitoring during iterative tasks. Ensure compatibility with your environment before relying on them in production systems.

## Contact

If you have any questions or feedback, please open an issue in the repository or contact me directly through: wojciech.kosnik.kowalczuk@gmail.com

Thank you for checking out my utility scripts repo!
