
import requests
from Chat import main

# Your current local version
current_version = "0.0.1"

# GitHub API URL for latest release
url = f"https://api.github.com/repos/UnknownBTW/Chatter/releases/latest"

try:
    response = requests.get(url)
    response.raise_for_status()
    latest_release = response.json()
    latest_version = latest_release["tag_name"].lstrip("v")  # remove 'v' if you use tags like v0.0.1

    if current_version < latest_version:
        print(f"New version available: {latest_version}")
        
    else:
        main()

except requests.RequestException as e:
    print(f"Failed to check updates: {e}")