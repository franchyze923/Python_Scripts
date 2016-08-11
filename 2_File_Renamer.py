import os

folder = r'F:\Pictures\2016\iPhone Pics\rename_test'

rename_prefix = 'FRAN_' # ENTER WHAT YOU WANT PREFIX OF IMAGE TO BE

mylist = os.listdir(folder)
num = 0

for x in mylist:
    old = os.path.join(folder,x)

    if old.lower().endswith(('.jpg')):

        print 'Renaming {0}'.format(x)
        num2 = '{0}.jpg'.format(num)
        rename_name = rename_prefix + num2
        rename_path = os.path.join(folder,rename_prefix + num2)
        os.rename(old,rename_path)
        print 'Successfully renamed {0} to {1}'.format(x,rename_name)
        num +=1
    elif old.lower().endswith('.png'):
        print 'Renaming {0}'.format(x)
        num2 = '{0}.png'.format(num)
        rename_name = rename_prefix + num2
        rename_path = os.path.join(folder, rename_prefix + num2)
        os.rename(old, rename_path)
        print 'Successfully renamed {0} to {1}'.format(x, rename_name)
        num += 1

    else:
        print 'IDK what file type {0} is !!, skipping...'.format(x)
        continue

for x in range(10):
    print 'Finished Renaming Files!!'


