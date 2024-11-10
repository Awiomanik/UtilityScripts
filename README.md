# Utility Scripts Repository

## Description

This repository is a compilation of various scripts I've created as part of my programming learning journey. These scripts are not interconnected but instead serve individual purposes that range from file comparison, disk space analysis, to secure password generation.

Please note that these scripts are shared for educational purposes. They were created to help me with tasks I encounter along the way and even though they worked as I intended they are merely examples of my progress in coding and are provided "as is" without warranties. They may not always function as intended on your machine, and their safety is not guaranteed. Users are advised to review the code and use it at their own discretion.

## Scripts

### Python Scripts

- `file_diff.py`:
Command-line tool. Compare two files and generate a detailed report of the differences between them.
> **Functionality:**
> - **Argument Verification**: The script starts by checking if the correct number of arguments is passed. It requires exactly two file paths. It verifies the existence of the provided file paths. Compares the MIME types of both files to ensure they are the same before proceeding with the comparison.
> - **Difference Report Creation**: It uses the `difflib.Differ` class to compute the differences and creates a human-readable report.
> - **Overwrite Protection**: The script outputs the differences to a new file named using a combination of the input file names. If a file with the same name exists, it will append a numeral to ensure uniqueness.

- `loading_bar.py`:
Command-line tool. Provides a visual loading bar that updates in real-time, useful for monitoring progress in time-consuming tasks.<br>
> **Functionality:**
> - **Initialization**: Sets up the loading bar with the total number of iterations and optional additional information for display.
> - **Progress Updates**: The loading bar is updated with each iteration, showing current progress, average time per iteration, and estimated time remaining.
> - **Completion Display**: At the end of the task, the loading bar displays the total time taken and allows for optional additional messages.

> **Methods**:
> - `update`: Updates the loading bar with the current iteration, estimated time remaining, and optional additional details about the task.
> - `close`: Finalizes the display by showing the total time and can clear the loading bar from the console.

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

- `folder_size_analyzer.py`:
Command-line tool. Analyzes and lists folder sizes within a specified directory, allowing for unit customization (e.g., bytes, KB, MB). Useful for disk usage analysis.<br>
> **Functionality:**
> - **Directory and Unit Customization**: Allows the user to specify a target directory (`-d`) and unit (`-u`) to display folder sizes, with support for units from bits to tebibytes.
> - **Folder Size Calculation**: Recursively calculates folder sizes and presents them in descending order by size.

> **Methods**:
> - `get_case_insensitive_item`: Searches for a unit in a case-insensitive manner.
> - `get_terminal_size_windows`: Determines terminal size on Windows to adjust output display.
> - `paginate`: Handles paginated output for large lists.
> - `list_folder_sizes`: Returns a list of folder sizes in descending order.

> **Example Usage**:
> ```bash
> python folder_size_analyzer.py -d /path/to/directory -u MB
> ```

## Usage

Each script can be run independently. For Python scripts, you'll need to have Python installed on your system. For detailed usage instructions, refer to the list below and individual script files.

- `file_diff.py`:<br>
  >Run the script from the command line by passing two file paths:<br> `>python file_diff.py path/to/file1 path/to/file2`.<br>
  >The files to be compared must be text-based and have the same MIME type.

- `loading_bar.py`:<br>
  >The script provides a customizable loading bar to visualize progress in console applications. To use, import `LoadingBar`, initialize with a total count, and update the bar in each iteration:
  ```python
  from loading_bar import LoadingBar
  bar = LoadingBar(total=200)
  for i in range(200):
      bar.update(i + 1)
  bar.close()
  ```
  >The loading bar displays progress, average time, and estimated time to completion.

- `folder_size_analyzer.py`:<br>
  >The script calculates the sizes of all folders in a directory and lists them by size. You can specify the directory and the unit for display with the `-d` and `-u` flags:
  ```bash
  python folder_size_analyzer.py -d /path/to/directory -u MB
  ```
  >Supported units: `bit`, `B`, `KB`, `MB`, `GB`, `TB`, `KiB`, `MiB`, `GiB`, `TiB`. By default, it uses the current directory and MiB.

## Contributing

Contributions to this project are welcome! If you have improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

This project is open source and available under the Apache v.2.0 (LICENSE).

## Disclaimer

These scripts are personal learning projects and may not be optimized for production use. The author is not responsible for any damage or data loss incurred through the use of these scripts.
Some of these scripts, such as `loading_bar.py`, are designed to assist with performance monitoring during iterative tasks. Ensure compatibility with your environment before relying on them in production systems.

## Contact

If you have any questions or feedback, please open an issue in the repository or contact me directly through wojciech.kosnik.kowalczuk@gmail.com

Thank you for checking out my utility scripts!
