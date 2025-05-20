import paramiko

# Create an SSH client
class SSHClient:
    pass


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept unknown keys

# Connect to the server
client.connect(hostname='your-server-ip', username='your-username', password='your-password')

# Run a command on the remote server
stdin, stdout, stderr = client.exec_command('ls -l')
print(stdout.read().decode())  # Print command output

# Close the connection
client.close()


