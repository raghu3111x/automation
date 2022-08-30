import re
import os

global initial_file_name 
initial_file_name = []

global new_folder_name
new_folder_name = []
folder = 'C:\\Users\\RS21\\Downloads\\'
os.chdir(folder)
files_list = os.listdir()
for i in range(len(files_list)):
	try:
		#print(files_list[i].split(' ')[0] + files_list[i].split(' ')[1])
		initial_file_name.append(files_list[i].split(' ')[0] + ' ' + files_list[i].split(' ')[1])
	#print(files_list[i])
	#print(files_list[i].split(' ')[0] + files_list[i].split(' ')[1])
	except:
		pass

#print(initial_file_name)
#print()
repeatative_file_name = max(set(initial_file_name), key = initial_file_name.count)
#print(initial_file_name.index(max(set(initial_file_name), key = initial_file_name.count)))


for i in range(len(files_list)):
	if repeatative_file_name in files_list[i]:
		m = re.search(r"\d", files_list[i])
		if m:
			new_folder_name.append(files_list[i][0:m.start()])
		for path in new_folder_name:
			if os.path.isdir(path) == 0:
				print('Creating directory : ',path)
				print()
				os.makedirs(path)

			#os.system('move ' + '"' +files_list[i] + '"' +' ' + folder + '\\' + path )
			os.system(('move ' + '"' +files_list[i] + '"' +' ' + '"' + path + '"' ))
			print('moving file ' + files_list[i])
			print()