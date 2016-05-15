#To make a directory with the name as the filename and put the file in that directory.
#First ever python project done by myself.

import os
import shutil

# help(os)

# print(os.curdir)
# print(os.pardir)
# print(os.getcwd())

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
	for name in filenames:
		if(name != 'todirectory.py'):							# Specifically excluding the working file name.
			name_without_ext=os.path.splitext(name)[0]			# name is name_with_ext, and name_without_ext is for folder creations.
			print(name)
			os.mkdir(name+'tmp')
			shutil.move(name, name+'tmp')
			os.rename(name+'tmp', name_without_ext)

#Problem: Can't create directory with same name as the file name.
#So, an inelegant solution can be, create all concatening '2' in them at the end and then at the end of the script, renaming them to remove '2' from them afer moving files to their folders is done.?
#But how will I move the files to their specific folders?


#Warning: Make sure there are no folders in the working directory when you run the script. Because os.walk() goes inside these directories and takes their files also,
# but then move function can't find these files(which are inside directories), so throws an error.
