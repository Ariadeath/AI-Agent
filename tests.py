from functions.get_files_info import get_files_info, get_file_content

calc_main_results = get_file_content("calculator", "main.py")
print("Results for main.py contents")
print(f"{calc_main_results}")

calc_pkg_results = get_file_content("calculator", "pkg/calculator.py")
print("Results for pkg/calculator.py contents")
print(f"{calc_pkg_results}")

calc_bin_results = get_file_content("calculator", "/bin/cat")
print("Results for bin/cat contents")
print(f"{calc_bin_results}")