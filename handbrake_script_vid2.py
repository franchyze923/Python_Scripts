import subprocess
import os

input_directory = r"D:\handbrake_cli"
directory_list = os.listdir(input_directory)

for file in directory_list:
    full_path = os.path.join(input_directory, file)
    if full_path.endswith(".avi"):
        print("Converting {} to .mp4".format(full_path))

        handbrake_command = [r"D:\handbrake_cli\HandBrakeCLI.exe", "-i",f"{full_path}", "-o","{}".format(full_path.replace(".avi", ".mp4")), "-e","x264", "-q","20", "-B", "160"]
        #subprocess.run(handbrake_command, shell=True)

        process = subprocess.Popen(handbrake_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:
            print(line)

        print("Finished converting")

print("Done")