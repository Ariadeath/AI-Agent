from functions.get_files_info import get_files_info, get_file_content, write_file, run_python_file

calc_main_results = run_python_file("calculator", "main.py")
print("Results for main.py contents")
print(f"{calc_main_results}")

calc_math_results = run_python_file("calculator", "main.py", ["3 + 5"])
print("Results for math using main.py")
print(f"{calc_math_results}")

calc_tests_result = run_python_file("calculator", "tests.py")
print("Results for tests.py contents")
print(f"{calc_tests_result}")

calc_first_error = run_python_file("calculator", "../main.py")
print("Results for first error contents")
print(f"{calc_first_error}")

calc_second_error = run_python_file("calculator", "nonexistent.py")
print("Results for second error")
print(f"{calc_second_error}")