import os
import subprocess
import urllib.request
import tarfile

os.chdir('/data/data/com.termux/files/home')

def print_color(text, color='\033[94m'):
    print(f"{color}{text}\033[0m")

def run_command(command):
    # Function to run a shell command and check for errors
    subprocess.run(command, check=True)

def download_file(url, destination):
    # Function to download a file from a given URL
    with urllib.request.urlopen(url) as response, open(os.path.join(os.path.expanduser("~"), destination), 'wb') as out_file:
        out_file.write(response.read())

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

# List of commands to run
commands_to_run = [
    ["apt", "update", "-y"],
    ["apt", "upgrade", "-y"],
    ["pkg", "up", "-y", "openssl", "curl", "python", "openssh"]
]

# Run each command in the list
for command in commands_to_run:
    run_command(command)

print_color("Downloading Google Cloud SDK")
url = "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-458.0.1-linux-arm.tar.gz"
download_file(url, "google-cloud-cli-458.0.1-linux-arm.tar.gz")

print_color("Decompressing Google Cloud SDK file")
extract_tar("google-cloud-cli-458.0.1-linux-arm.tar.gz", ".")

print_color("Adding the gcloud CLI to your path")
run_command(["./google-cloud-sdk/install.sh"])

print_color("Initializing the gcloud CLI")
run_command(["./google-cloud-sdk/bin/gcloud", "init"])

# Setting up alias in bash.bashrc
bashrc_path = os.path.join(os.path.expanduser("~"), ".bashrc")
alias_command = "alias google='gcloud alpha cloud-shell ssh'"
append_to_bashrc(bashrc_path, alias_command)

print_color("Now exit and reopen your Termux, then type 'google' to start Google shell")
