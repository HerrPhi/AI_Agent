from functions.get_files_info import get_files_info


print("Results for current directory:")
res = get_files_info("calculator", ".")
print(res)

print("Result for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))

print("Result for '/bin' directory:")
print(get_files_info("calculator", "/bin"))

print("Result for '../' directory:")
print(get_files_info("calculator", "../"))