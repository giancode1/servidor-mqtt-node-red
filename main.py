import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

banner = """

░██████╗░░█████╗░  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗░██████╗
██╔════╝░██╔══██╗  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝
██║░░██╗░██║░░╚═╝  ███████║███████║██║░░╚═╝█████═╝░╚█████╗░
██║░░╚██╗██║░░██╗  ██╔══██║██╔══██║██║░░██╗██╔═██╗░░╚═══██╗
╚██████╔╝╚█████╔╝  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗██████╔╝
░╚═════╝░░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░
"""

blue()
print(banner)
time.sleep(1.5) 

green()
print("[+] Actualizar e instalar dependecias esenciales...")
os.system("sudo apt-get update -y")
os.system("sudo apt-get upgrade -y")
os.system("sudo apt install net-tools -y")
os.system("sudo apt install curl wget -y")

print("[+] Instalando repositorio mosquitto...")
os.system("sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa -y") 
os.system("sudo apt-get update -y")
os.system("sudo apt install mosquitto mosquitto-clients -y")
os.system("sudo service mosquitto start")
os.system("sudo systemctl enable mosquitto")


with open("/etc/mosquitto/mosquitto.conf", "a") as file:
    file.write("\nlistener 1883\n")
    file.write("allow_anonymous true")

os.system("sudo systemctl restart mosquitto")


print("[+] Instalando dependencias de node-red...")
os.system("curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -")
# os.system("sudo apt-get install -y nodejs build-essential")
os.system("sudo apt-get install -y nodejs ")
os.system("sudo apt install npm -y")


print("[+] Instalando node-red e inicio automatico...")
os.system("sudo npm install -g --unsafe-perm node-red pm2")
os.system("pm2 start `which node-red` -- -v")
os.system("pm2 save")
os.system("pm2 startup")
os.system("source ~/.profile")

time.sleep(1)
print("Listo!!")
print("Broker mosquitto iniciado y a la escucha en el puerto 1883")
print("Accede a Node-red: http://TU_IP:1880")

#print("Accede a" , f"http://{os.popen('hostname -I').read()}:1880")


