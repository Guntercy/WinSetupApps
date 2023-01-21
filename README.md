# WinSetupApps
Overview
This script creates a new folder on the D drive with the name 'Downloaded Applications', and downloads a list of specified applications. The script also includes a function to automatically install the downloaded applications to the location where they were downloaded.

Requirements

This script requires the following Python modules:

"os": provides a way of using operating system dependent functionality like reading or writing to files, starting new processes, killing processes etc.
"urllib.request": module for opening URLs.
"subprocess": module for running new processes, and connecting to their input/output/error pipes.

Usage

Make sure you have the required Python modules installed.
Run the script in your Python environment.
The script will create a new folder on the D drive with the name 'Downloaded Applications', if it doesn't exist.
The script will then download the specified applications to the newly created folder.
The script will then call the install_applications function, which will automatically install the downloaded applications.

Customization

You can customize the script by editing the list of applications to download and their corresponding download links in the applications dictionary. You can also edit the path where the folder will be created or the name of the folder.

Note

Please note that in order for the script to work, the downloaded apps should be installer files, otherwise they will not be installed by this script. Also, the links that I've provided in the script are not direct download links, they are the links to the download page, you'll need to navigate through the website to find the direct download link.

Conclusion

This script is a useful tool for automating the process of downloading and installing multiple applications at once. With a few modifications, it can be tailored to suit your specific needs. I hope this script will be helpful for you.

Please let me know if you need any more help with it.
