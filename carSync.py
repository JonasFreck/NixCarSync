import subprocess

#problem may have been the way I referenced the source and destination by copying from the local path in VSCode, not sure why
source = "./source/directory/"
destination = "./destination/directory/"

command = ["rsync", "-av", source, destination]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the standard output and standard error
print(result.stdout)
if result.stderr:
    print(result.stderr)
