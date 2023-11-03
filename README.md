# Utility Scripts Repository

## Description

This repository is a compilation of various scripts I've created as part of my programming learning journey. These scripts are not interconnected but instead serve individual purposes that range from file comparison, disk space analysis, to secure password generation.

Please note that these scripts are shared for educational purposes. They were created to help me with tasks I encounter along the way and even though they worked as I intended they are merely examples of my progress in coding and are provided "as is" without warranties. They may not always function as intended on your machine, and their safety is not guaranteed. Users are advised to review the code and use it at their own discretion.

## Scripts

### Python Scripts

- `file_diff.py`:<br>
Command-line tool. Compare two files and generate a detailed report of the differences between them.<br>
> **Functionality:**
> - **Argument Verification**: The script starts by checking if the correct number of arguments is passed. It requires exactly two file paths. It verifies the existence of the provided file paths. Compares the MIME types of both files to ensure they are the same before proceeding with the comparison.
> - **Difference Report Creation**: It uses the `difflib.Differ` class to compute the differences and creates a human-readable report.
> - **Overwrite Protection**: The script outputs the differences to a new file named using a combination of the input file names. If a file with the same name exists, it will append a numeral to ensure uniqueness.


## Usage

Each script can be run independently. For Python scripts, you'll need to have Python installed on your system.

For detailed usage instructions, refer to the individual script files.

- `file_diff.py`:<br>
  >Run the script from the command line by passing two file paths:<br> `>python file_diff.py path/to/file1 path/to/file2`.<br>
  >The files to be compared must be text-based and have the same MIME type.

## Contributing

Contributions to this project are welcome! If you have improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

This project is open source and available under the Apache v.2.0 (LICENSE).

## Disclaimer

These scripts are personal learning projects and may not be optimized for production use. The author is not responsible for any damage or data loss incurred through the use of these scripts.

## Contact

If you have any questions or feedback, please open an issue in the repository or contact me directly through wojciech.kosnik.kowalczuk@gmail.com

Thank you for checking out my utility scripts!
