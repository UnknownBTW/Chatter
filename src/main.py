import os
import subprocess
import shutil
import tarfile
import zipfile
import requests
from Client_config import APP_NAME, APP_VERSION, UPDATE_URLS, PUBLIC_KEY
from Chat import main

# Your current local version
current_version = APP_VERSION

# GitHub API URL for latest release
url = f"https://api.github.com/repos/UnknownBTW/Chatter/releases/latest"

def safe_extract_tar(path, extract_path):
    """Try to extract a tar.gz or plain tar file."""
    try:
        with tarfile.open(path, "r:gz") as t:
            t.extractall(extract_path)
    except tarfile.ReadError:
        try:
            with tarfile.open(path, "r") as t:
                t.extractall(extract_path)
        except tarfile.ReadError:
            print(f"Warning: {path} is not a tar archive.")

def safe_extract_zip(path, extract_path):
    """Extract zip safely."""
    try:
        with zipfile.ZipFile(path) as z:
            z.extractall(extract_path)
    except zipfile.BadZipFile:
        print(f"Warning: {path} is not a zip archive.")

try:
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    latest_version = latest_release["tag_name"].lstrip("v")  # e.g., v0.0.1 -> 0.0.1

    if current_version < latest_version:
        assets = latest_release.get("assets", [])

        if assets:
            url, name = assets[0]["browser_download_url"], assets[0]["name"]
            path = os.path.join("/tmp", name)

            # Download the file
            with requests.get(url, stream=True) as r, open(path, "wb") as f:
                for c in r.iter_content(8192):
                    f.write(c)

            extract_path = os.path.join("/tmp", "new_version")
            os.makedirs(extract_path, exist_ok=True)

            # Extract depending on file type
            if name.endswith(".zip"):
                safe_extract_zip(path, extract_path)
            elif name.endswith((".tar.gz", ".tgz", ".tar")):
                safe_extract_tar(path, extract_path)
            else:
                print(f"Downloaded file {name} is not a recognized archive. Skipping extraction.")

            # Copy files to current directory
            for item in os.listdir(extract_path):
                s, d = os.path.join(extract_path, item), os.path.join(os.getcwd(), item)
                if os.path.isdir(s):
                    shutil.rmtree(d, ignore_errors=True)
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)

        # Restart the script
        subprocess.Popen(["python3", "your_main_script.py"])
        exit()

    else:
        main()

except requests.RequestException as e:
    print(f"Failed to check updates: {e}")