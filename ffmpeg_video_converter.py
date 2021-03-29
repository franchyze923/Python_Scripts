import subprocess
import os
from pathlib import Path
import time
import logging
import sys

master_start_time = time.time()

root_video_directory = r"E:\Media\Videos"
root_output_directory = r"D:\Videos"
ffmpeg_location = r"C:\Users\franp\Downloads\ffmpeg-2021-03-28-git-8b2bde0494-full_build\bin\ffmpeg.exe"

# noinspection PyArgumentList
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler(r"D:\export_log.log"),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )

for subdir, dirs, files in os.walk(root_video_directory):
    for file in files:
        if file.endswith(".avi"):
            avi_file = os.path.join(subdir, file)
            logging.info(f"Detected .avi file: {avi_file}")
            logging.info(f"Creating directory Structure: {os.path.dirname(avi_file).replace('E', 'D', 1)}")

            Path(os.path.dirname(avi_file).replace('E', 'D', 1)).mkdir(parents=True, exist_ok=True)
            output_file = os.path.join(avi_file.replace('E', 'D', 1).replace(".avi", ".mp4"))
            ## h.265 did not work with plex direct stream
            #ffmpeg_command = [ffmpeg_location, '-i', f'{avi_file}',  "-c:v", "libx265", "-crf", "26", output_file]
            #ffmpeg_command = [ffmpeg_location, '-i', f'{avi_file}', output_file]
            #ffmpeg_command = [ffmpeg_location, '-i', f'{avi_file}', "-c:v", "libx264", "-crf", "20", output_file]
            handbrake_command = [r"C:\Users\franp\Downloads\HandBrakeCLI-1.3.3-win-x86_64\HandBrakeCLI.exe", '-i', f'{avi_file}',"-o", output_file, "-e", "x264", "-q", "20", "-B", "160"]


            logging.info(f"Converting: {avi_file} to .MP4 with x264. Output MP4: {output_file}")
            start_time = time.time()

            process = subprocess.Popen(handbrake_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            for line in process.stdout:
                print(line)

            logging.info("Done")
            logging.info('Program took {} seconds to complete..\n'.format(time.time() - start_time))

logging.info("Done")
logging.info('Program took {} seconds to complete.'.format(time.time() - master_start_time))