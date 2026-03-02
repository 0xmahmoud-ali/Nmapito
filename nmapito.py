import subprocess
import os

#Color Codes
VERSION = "1.0.0"
BLUE = '\033[94m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RED  = '\033[91m'
END  = '\033[0m'

#Nmapito Banner
banner = rf"""{BLUE}{BOLD}
  _   _                       _ _        
 | \ | |_ __ ___   __ _ _ __ (_) |_ ___  
 |  \| | '_ ` _ \ / _` | '_ \| | __/ _ \ 
 | |\  | | | | | | (_| | |_) | | || (_) |
 |_| \_|_| |_| |_|\__,_| .__/|_|\__\___/ 
                       |_|               
      >> The Little Web Scanner <<
             Version: {VERSION}
{END}"""

print(banner)

#Ask the user for the target
target = input(f"{CYAN}{BOLD}Please enter the target's IP or URL to start scanning: {END}")

print(f"\n{CYAN}   >>> Your target is  " + target + f" <<<{END}")

#Make a folder to save results
folder_name = "scan_results"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)


#Finds open ports and services
print(f"\n{BLUE}[*] Searching for open ports using Nmap{END}")

nmap_command = "nmap -sV -T4 " + target + " -oN " + folder_name + "/nmap_result.txt"
os.system(nmap_command) 

#Look into the nmap_result.txt file for a web service
print(f"\n{BLUE}[*] Checking Nmap results for web services.{END}")

with open(folder_name + "/nmap_result.txt", "r") as result:
    result_content = result.read()

#Check if port 80, 443, or 'http' appears in nmap_result.txt
if "http" in result_content.lower() or "80/tcp" in result_content or "443/tcp" in result_content:
    print(f"{CYAN}[!] Web service detected!!! Starting Nikto scan.{END}")
    #Looks for web vulnerabilities
    nikto_command = "nikto -h " + target + " -output " + folder_name + "/nikto_result.txt"
    os.system(nikto_command)
else:
    print(f"{RED}[-] No web services (HTTP/HTTPS) found. Skipping Nikto scan.{END}")


#Done
print(f"\n{BLUE}All scans are done!{END}\n")
