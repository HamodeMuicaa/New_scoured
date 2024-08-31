import subprocess

try:

    subprocess.run("sudo apt-get update && sudo apt-get install python3-pip ffmpeg -y", shell=True, check=True)
    print("Packages updated and installed successfully.")


    subprocess.run("curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install nodejs -y && sudo npm install -g npm@9.6.3", shell=True, check=True)
    print("Node.js and npm installed successfully.")


    subprocess.run("pip3 install -U -r requirements.txt", shell=True, check=True)
    print("Python requirements installed successfully.")


    subprocess.run("bash start", shell=True, check=True)
    print("Script started successfully.")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
