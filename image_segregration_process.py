#Requirement :- Segregrate Front and Back Images From a Folder

#Use Below Command To Run The Script :- python image_segregration_process.py

import os
import shutil
import re

print("-----Image Segregation Process Started-----")

source='/home/divum/image_segregation_input/input/'
destination=''

file_names=os.listdir(source)
print(file_names)

for f in file_names:

	front = re.search("^[0-9]{9} ?(-|.|_) ?1 ?(\(?|\)?|_?|-?|.?)? ?[a-z]{0,10} ?(\(?|\)?|_?|-?|.?)? ?.[a-z]{3,10}$", f)

	if front:
		destination='/home/divum/image_segregation_input/front/'
		shutil.copy(source + f,destination + f)
	else:
		back = re.search("^[0-9]{9} ?(-|.|_) ?2 ?(\(?|\)?|_?|-?|.?)? ?[a-z]{0,10} ?(\(?|\)?|_?|-?|.?)? ?.[a-z]{3,10}$", f)

		if back:
			destination='/home/divum/image_segregation_input/back/'
			shutil.copy(source + f,destination + f)

print("-----Image Segregation Process Completed-----")
