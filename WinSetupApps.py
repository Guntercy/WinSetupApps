import os
import urllib.request
import subprocess

# Create a new folder on the D drive with the name 'Downloaded Applications'
path = "D:\\Downloaded Applications"
if not os.path.exists(path):
    os.makedirs(path)

# Download the applications
applications = {
    "Discord": "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86",
    "Steam": "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe",
    "Nvidia Experience": "https://uk.download.nvidia.com/GFE/GFEClient/3.23.0.74/GeForce_Experience_v3.23.0.74.exe",
    "Logitech G Hub": "https://download01.logi.com/web/ftp/pub/techsupport/gaming/lghub_installer.exe",
    "Corsair ICUE": "https://downloads.corsair.com/Files/CUE/iCUESetup_4.32.129_release.msi",
    "Python": "https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe"
}

for application, url in applications.items():
    filename = os.path.join(path, application + ".exe")
    urllib.request.urlretrieve(url, filename)

print("Downloaded all the applications to the folder: ", path)

# Function to install the downloaded applications
def install_applications(path):
    for application in applications:
        filename = os.path.join(path, application + ".exe")
        try:
            subprocess.run([filename, "/S"], check=True)
            print(application + " successfully installed.")
        except subprocess.CalledProcessError as e:
            print(application + " failed to install.")
            print(e)

# Call the function to install the downloaded applications
install_applications(path)