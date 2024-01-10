import paramiko
from datetime import datetime

def check_file_exists(hostname, port, username, password, remote_path, file_name, local_path, local_file_name):
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    sftp = None

    try:
        # Automatically add the servers host key
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SFTP server
        ssh_client.connect(hostname, port, username, password)

        # Open an SFTP session
        sftp = ssh_client.open_sftp()

        # Check if the file exists
        file_exists = True
        try:
            sftp.stat(remote_path + '/' + file_name)
        except FileNotFoundError:
            file_exists = False

        # Copy the file if it exists
        if file_exists:
            sftp.get(remote_path + '/' + file_name, local_path + '/' + local_file_name)

        return file_exists

    finally:

        # Close the SFTP session and the SSH connection

        if sftp:
            sftp.close()

        ssh_client.close()

hostname = '---'
port = 22
username = '---'
password = '---'
remote_path = '/koll'
file_name = 'userid.ext'
local_path = '---'
datestamp = datetime.now().strftime("%Y-%m-%d")
local_file_name = f'{datestamp}_userid.ext'

if check_file_exists(hostname, port, username, password, remote_path, file_name, local_path, local_file_name):
    print(f"\n'{file_name}' fanns på SFTP:n och har kopierats som '{local_file_name}' till Filskyffeln.")
else:
    print(f"\n'{file_name}' finns inte på SFTP:n.")
