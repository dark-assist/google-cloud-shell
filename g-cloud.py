import os
import subprocess
import urllib.request
import tarfile

def print_color(text, color='\033[94m'):
    print(f"{color}{text}\033[0m")

def run_command(command, cwd=None):
    # Function to run a shell command and check for errors, with optional working directory
    subprocess.run(command, check=True, cwd=cwd)

def download_file(url, destination, cwd=None):
    # Function to download a file from a given URL with a progress bar, with optional working directory
    with urllib.request.urlopen(url) as response, open(os.path.join(os.path.expanduser("~"), destination), 'wb') as out_file:
        file_size = int(response.headers['Content-Length'])
        chunk_size = 1024 * 1024  # 1 MB
        bytes_so_far = 0

        print_color(f"Downloading {destination}...")

        for data in iter(lambda: response.read(chunk_size), b''):
            out_file.write(data)
            bytes_so_far += len(data)
            progress = bytes_so_far * 100 / file_size
            print_color(f"Progress: {progress:.2f}%", end='\r')

        print()  # Move to the next line after download completion

def extract_tar(file_path, output_dir):
    # Function to extract a tar.gz file to a specified directory
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=os.path.join(os.path.expanduser("~"), output_dir))

def append_to_bashrc(file_path, text):
    # Function to append text to a specified file
    with open(file_path, "a") as file:
        file.write(text)

# Script starts here
print_color("This script was coded by sanatani-hacker")

# Change working directory to $HOME
home_directory = os.path.expanduser("~")

# List of commands to run
commands_to_run = [
    ["apt", "update", "-y"],
    ["apt", "upgrade", "-y"],
    ["pkg", "up", "-y", "openssl", "curl", "python", "openssh"]
]

# Run each command in the list
for command in commands_to_run:
    run_command(command, cwd=home_directory)

# Google Cloud SDK download and setup
google_cloud_url = "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-458.0.1-linux-arm.tar.gz"
google_cloud_destination = "google-cloud-cli-458.0.1-linux-arm.tar.gz"

print_color(f"Downloading Google Cloud SDK from {google_cloud_url}")
download_file(google_cloud_url, google_cloud_destination, cwd=home_directory)

print_color("Decompressing Google Cloud SDK file")
extract_tar(os.path.join(home_directory, google_cloud_destination), home_directory)

print_color("Adding the gcloud CLI to your path")
run_command(["./google-cloud-sdk/install.sh"], cwd=home_directory)

print_color("Initializing the gcloud CLI")
run_command(["./google-cloud-sdk/bin/gcloud", "init"], cwd=home_directory)

# Setting up alias in .bashrc
bashrc_path = os.path.join(home_directory, ".bashrc")
alias_command = "alias google='gcloud alpha cloud-shell ssh'"
append_to_bashrc(bashrc_path, alias_command)

print_color("Now exit and reopen your Termux, then type 'google' to start Google shell")
