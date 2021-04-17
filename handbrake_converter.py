import subprocess
import os
import time
import logging
import sys
from shutil import copyfile
from pathlib import Path

master_start_time = time.time()

handbrake_cli_exe = r"C:\Users\franp\Downloads\HandBrakeCLI-1.3.3-win-x86_64\HandBrakeCLI.exe"
root_video_directory = Path(r"path to directory containing input videos")
root_video_output = Path(r"path to output directory")

# noinspection PyArgumentList
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler(r"D:\export_log.log"),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )

for path, directories, files in os.walk(root_video_directory):

    new_folder = root_video_output.joinpath(*Path(path).parts[1:])
    logging.info(f"Creating folder for {new_folder}")
    Path(new_folder).mkdir(parents=True, exist_ok=True)

    for file in files:
        if file.endswith(".avi"):
            avi_file = os.path.join(path, file)
            logging.info(f"Detected .avi file: {avi_file}")
            output_file = str(root_video_output.joinpath(*Path(avi_file).parts[1:])).replace(".avi", ".mp4")

            if Path(output_file).exists():
                logging.info("deteced mp4 already converted")
                continue
            else:

                handbrake_command = [handbrake_cli_exe, '-i', f'{avi_file}',"-o", output_file, "-e", "x264", "-q", "20", "-B", "160"]
                logging.info(f"Converting: {avi_file} to .MP4 with x264. Output MP4: {output_file}")
                start_time = time.time()

                process = subprocess.Popen(handbrake_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
                for line in process.stdout:
                    print(line)

                logging.info("Done")
                logging.info('Program took {} seconds to complete..\n'.format(time.time() - start_time))

        else:
            non_avi_file = os.path.join(path, file)
            output_file = str(root_video_output.joinpath(*Path(non_avi_file).parts[1:]))

            logging.info(f"Detected Non .avi file. Copying {non_avi_file} to {output_file}")
            copyfile(non_avi_file, output_file)

logging.info("Done")
logging.info('Program took {} seconds to complete.'.format(time.time() - master_start_time))