import os

current_directory = os.getcwd()
print(f"Current Directory: {current_directory}\n")

entries = os.listdir(current_directory)

print("Files and directories in the current directory:")
for entry in entries:
    print(entry)
