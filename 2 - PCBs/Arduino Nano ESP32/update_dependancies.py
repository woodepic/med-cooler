import subprocess
import shutil
import os

def clone_repository(repo_url, folder_name):
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        # If the folder exists and is a directory, remove it
        try:
            shutil.rmtree(folder_name)
            print(f"Folder '{folder_name}' deleted successfully.")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"Folder '{folder_name}' does not exist.")

    try:
        # Construct the git clone command
        command = ['git', 'clone', repo_url, folder_name]
        
        # Execute the command
        subprocess.run(command, check=True)
        print("Repository cloned successfully!")
    except subprocess.CalledProcessError as e:
        print("Error: Failed to clone repository -", e)


# GitHub repository URL
repo_url = "https://github.com/woodepic/kicad-components"

# Folder name to clone into
folder_name = ".components"

# Call the function to clone the repository
clone_repository(repo_url, folder_name)

current_directory = os.getcwd()

#Remap the sym-lib-table
file_path = "sym-lib-table"
with open(file_path, 'r') as file:
    file_content = file.read()
    modified_content = file_content.replace(
        "/Users/matt/Library/CloudStorage/GoogleDrive-matt@angfam.com/My Drive/Personal/Projects/Meds Cooler/kicad-components",
        current_directory + "/components"
    )
with open(file_path, 'w') as file:
    file.write(modified_content)


#Remap the fp-lib-table
file_path = "fp-lib-table"
with open(file_path, 'r') as file:
    file_content = file.read()
    modified_content = file_content.replace(
        "/Users/matt/Library/CloudStorage/GoogleDrive-matt@angfam.com/My Drive/Personal/Projects/Meds Cooler/kicad-components",
        current_directory + "/.components"
    )
with open(file_path, 'w') as file:
    file.write(modified_content)