import os
from os.path import isdir

current_working_path = os.getcwd()
print(current_working_path)
files = os.listdir(current_working_path)


for file in files:
	if os.path.isdir(file):
		print(f"Folder:\t{file}")
		os.chdir(os.path.join(current_working_path,file))
		for del_files in os.listdir(os.getcwd()):
			file = str(os.getcwd())+f"\{del_files}"
			print(f"deleting file:\t{file}")
			os.remove(file)
		os.chdir(current_working_path)

	else:
		print("[!] Ignoring file:",file)




