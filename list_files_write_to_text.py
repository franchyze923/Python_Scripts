import os

dir = raw_input('Drag in directory')
dir_list = os.listdir(dir)

out_file = raw_input('Drag in full path to output txt file)

the_list = []

for x in dir_list:
    fullpath = os.path.join(dir, x)
    the_list.append(fullpath)

thefile = open(out_file, 'w')

for item in the_list:
  thefile.write("{}\n".format(item)

