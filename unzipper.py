import zipfile
import os
import subprocess
import time

zipdir = raw_input('Drag in folder')
zipdir_list = os.listdir(zipdir)

for x in zipdir_list:

    full_path = os.path.join(zipdir, x)

    if full_path.endswith('.zip'):

        output_name = (full_path[:-4] + '.tif')

        print 'Unzipping {}'.format(full_path)

        with zipfile.ZipFile(full_path, "r") as zip_ref:
            zip_ref.extractall(zipdir)