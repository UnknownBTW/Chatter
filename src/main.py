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

try:
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    latest_version = latest_release["tag_name"].lstrip("v")  # remove 'v' if you use tags like v0.0.1

    if current_version < latest_version:
        assets = latest_release.get("assets", [])

        if assets:
            url, name = assets[0]["browser_download_url"], assets[0]["name"]
            path = os.path.join("/tmp", name)
            with requests.get(url, stream=True) as r, open(path, "wb") as f:
                for c in r.iter_content(8192): f.write(c)
                
            extract_path = os.path.join("/tmp", "new_version")
            os.makedirs(extract_path, exist_ok=True)
            if name.endswith(".zip"):
                with zipfile.ZipFile(path) as z: z.extractall(extract_path)
            else:
                with tarfile.open(path, "r:gz") as t: t.extractall(extract_path)
                
            for item in os.listdir(extract_path):
                s, d = os.path.join(extract_path, item), os.path.join(os.getcwd(), item)
                if os.path.isdir(s):
                    shutil.rmtree(d, ignore_errors=True); shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
        
        subprocess.Popen(["python3", "your_main_script.py"]); exit()
        
    else:
        main()

except requests.RequestException as e:
    print(f"Failed to check updates: {e}")