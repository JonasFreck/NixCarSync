import subprocess
import os

#problem may have been the way I referenced the source and destination by copying from the local path in VSCode, not sure why
path_to_source = os.environ.get("SOURCE_PATH")
path_to_destination = os.environ.get("DESTINATION_PATH")



#path_to_destination = "./destination/directory/"
#path_to_source = "./source/directory/"

print(path_to_source)
print(path_to_destination)

command = ["rsync", "-av", path_to_source, path_to_destination]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the standard output and standard error
print(result.stdout)
if result.stderr:
    print(result.stderr)
