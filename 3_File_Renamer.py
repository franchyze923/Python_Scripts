import os

# User Input
folder = r'F:\Pictures\2016\iPhone Pics\rename_test'
rename_prefix = 'Renamed_' # ENTER WHAT YOU WANT PREFIX OF IMAGE TO BE
num = 0

def file_renamer():
    global num
    for root, dir2, files in os.walk(folder):
        print 'Renaming Files in {} \n'.format(root)
        if len(dir2) > 0:
            print 'Found the following sub folders {} \n'.format(dir2)
        #print 'Found {} subfolders named {} and {}'.format(len(dir2),dir2[0],dir2[1])
        #num = 0 uncomment if you want each folder to start renaming files at 0
        for x in files:
            local_folder = os.path.join(folder, root)
            old = os.path.join(local_folder, x)
            #if x.startswith('IMG'):

            if old.lower().endswith(('.jpg')):

                print 'Renaming {0}'.format(x)
                num2 = '{0}.jpg'.format(num)
                rename_name = rename_prefix + num2
                rename_path = os.path.join(local_folder, rename_prefix + num2)
                os.rename(old, rename_path)
                print 'Successfully renamed {0} to {1} \n'.format(x, rename_name)
                num += 1
            elif old.lower().endswith('.png'):
                print 'Renaming {0}'.format(x)
                num2 = '{0}.png'.format(num)
                rename_name = rename_prefix + num2
                rename_path = os.path.join(local_folder, rename_prefix + num2)
                os.rename(old, rename_path)
                print 'Successfully renamed {0} to {1} \n'.format(x, rename_name)
                num += 1

            elif old.lower().endswith('.mov'):
                print 'Renaming {0}'.format(x)
                num2 = '{0}.mov'.format(num)
                rename_name = rename_prefix + num2
                rename_path = os.path.join(local_folder, rename_prefix + num2)
                os.rename(old, rename_path)
                print 'Successfully renamed {0} to {1} \n'.format(x, rename_name)
                num += 1

            else:
                print 'IDK what file type {0} is !!, skipping...'.format(x)
                continue
            #else:
                #print '{} Does not meet renaming criteria, moving to next file'.format(x)
                #continue

    print 'Finished Renaming all files in {}'.format(folder)


file_renamer()




