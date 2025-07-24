from functions.get_files_info import get_files_info, get_file_content, write_file

calc_main_results = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print("Results for main.py contents")
print(f"{calc_main_results}")

calc_pkg_results = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print("Results for pkg/calculator.py contents")
print(f"{calc_pkg_results}")

calc_bin_results = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print("Results for bin/cat contents")
print(f"{calc_bin_results}")