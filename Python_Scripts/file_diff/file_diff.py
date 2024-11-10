import sys
import os
import mimetypes as tp
import difflib

# SCRIPT ARGUMENTS:
def script_init(arg):
     '''Check if correct arguments were passed and assign them to proper varibles'''

     # If number of arguments correct
     amount_of_arguments = 3
     if len(arg) < amount_of_arguments: 
          sys.exit("Script takes {} arguments, {} were given".format(amount_of_arguments, len(arg)))
     
     # If files exist
     not_existing_files = []
     if not os.path.exists(arg[1]): not_existing_files.append(arg[1])
     if not os.path.exists(arg[2]): not_existing_files.append(arg[2])
     if not_existing_files: 
          sys.exit("File/s {} do/es not exist".format(', '.join(map(str, not_existing_files))))
     
     # If file types are the same
     mime_type1 = tp.guess_type(arg[1])[0]
     mime_type2 = tp.guess_type(arg[2])[0]
     if mime_type1 != mime_type2: 
          sys.exit("Files have different MIME types:\n{}:\t{}\n{}:\t{}\nFiles must have same MIME type".format(arg[1], mime_type1, arg[2], mime_type2)) 
     
     # Load files to variables
     try:
          f1 = open(arg[1], 'r')
          f2 = open(arg[2], 'r')
          f1_list = f1.readlines()
          f2_list = f2.readlines()
          f1_list[-1] += "\n"
          f2_list[-1] += "\n"
          return f1, f2, f1_list, f2_list
     except: sys.exit("Unexpected ERROR occured when tryin to open and read files:\n{e}")

# PREPARATION
def create_diff_file(file1_path, file2_path):
     '''Create and open third file to write to'''

     # Separate directory and file name
     file1_dir = os.path.dirname(file1_path)
     file1_name = os.path.basename(file1_path)
     file2_name = os.path.basename(file2_path)

     # Construct the new file name
     diff_file_name = f"{file1_dir}difference_{os.path.splitext(file1_name)[0]}_{file2_name}"

     # Construct the new file path
     diff_file_path = os.path.join(file1_dir, diff_file_name)

     # Open a new file
     if not os.path.exists(diff_file_path):
          diff_file = open(diff_file_path, 'a')
     # Add numeral to name to not overwrite existing file if necessary
     else:
          file_numeral = 1
          fn, fe = diff_file_path = os.path.splitext(diff_file_path)
          while True: 
               diff_file_path_temp = fn + "_" + str(file_numeral) + fe
               if not os.path.exists(diff_file_path_temp):
                    diff_file = open(diff_file_path_temp, 'a')
                    break
               file_numeral += 1

     return diff_file, file1_name, file2_name

# COMPARISON
def create_diff(list1, list2):
     '''Create list containing difference between two lists'''
     d = difflib.Differ()
     return list(d.compare(list1, list2))

def process_diff(difference, f1_name, f2_name):
     '''Create diff_list containing both lists with their difference messages'''
     # String constants
     difference_top = "\n##### DIFFERENCE IN FILES #####\n"
     from_1 = "\nFROM FILE {} :\n".format(f1_name)
     from_2 = "\nFROM FILE {} :\n".format(f2_name)
     difference_bot = "\n############# END #############\n\n"

     final_list = []
     buffer = []
     from_list_1_bool = False
     from_list_2_bool = False

     for line in difference:
          # Lines are the same -> append lines from buffer and this line
          if line.startswith('  '):
               if from_list_1_bool:
                    buffer.append(difference_bot)
                    from_list_1_bool = False
               if from_list_2_bool:
                    buffer.append(difference_bot)
                    from_list_2_bool = False
               if buffer:
                    final_list.extend(buffer)
                    buffer.clear()
               final_list.append(line[2:])

          # Line in list 1 only -> add line to the buffer
          elif line.startswith('- '):
               if not from_list_1_bool:
                    if not from_list_2_bool:
                         buffer.append(difference_top)
                    buffer.append(from_1)
                    from_list_1_bool = True
                    from_list_2_bool = False
               buffer.append(line[2:])

          # Line in list 2 only -> add line line to the buffer
          elif line.startswith('+ '):
               if not from_list_2_bool:
                    if not from_list_1_bool:
                         buffer.append(difference_top)
                    buffer.append(from_2)
                    from_list_2_bool = True
                    from_list_1_bool = False
               buffer.append(line[2:])

     # Add any remaining Elements from the buffer
     if buffer: 
          final_list.extend(buffer)
          final_list.append(difference_bot)

     return final_list

def save_2_diff_file(f1_file, f2_file, diff_file, list):
     '''Save processed diff to a third file and close all three files'''
     for line in list: 
          diff_file.write(line)
     f1_file.close()
     f2_file.close()
     diff_file.close()
      
def comparison(f1, f2, diff, l1, l2, f1n, f2n):
     save_2_diff_file(f1, f2, diff, process_diff(create_diff(l1, l2), f1n, f2n))

# EXIT MESSAGE
def are_files_identical(file_1_path, diff_path, path_of_diff_file):
     '''Check if there are any differences, if not delete the diff file'''
     with open(file_1_path, 'rb') as file1, open(diff_path, 'rb') as file2:
          content1 = file1.read()
          content2 = file2.read()
     if content1 == content2:
          try: os.remove(path_of_diff_file)
          except: pass
          sys.exit("Files are identical")
     else:
          sys.exit(f"{path_of_diff_file} file was created")
   

# MAIN PROGRAM
file_1, file_2, f1_lines, f2_lines = script_init(sys.argv)
diff_file, f1_name, f2_name = create_diff_file(sys.argv[1], sys.argv[2])
comparison(file_1, file_2, diff_file, f1_lines, f2_lines, f1_name, f2_name)
are_files_identical(sys.argv[1], sys.argv[2], diff_file.name)