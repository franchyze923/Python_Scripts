import subprocess

handbrake_command = ["D:\handbrake_cli\HandBrakeCLI.exe", "-i", r"D:\handbrake_cli\2020-09-13 09.12.17 gokart.avi", "-o", r"D:\handbrake_cli\2020-09-13 09.12.17 gokart_from_python.mp4","-e", "x264", "-q", "20", "-B", "160"]

subprocess.run(handbrake_command, shell=True)