from functions.get_files_info import get_files_info

calculator_results = get_files_info("calculator", ".")
print(f"Result for current directory:")
print(f"{calculator_results}")

calc_pkg_results = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(f"{calc_pkg_results}")

calc_bin_results = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(f"{calc_bin_results}")

calc_elip_results = get_files_info("calculator", "../")
print("Result for '../':")
print(f"{calc_elip_results}")