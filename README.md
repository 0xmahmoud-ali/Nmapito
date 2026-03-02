# Nmapito
**Nmapito** (v1.0.0) is a lightweight Python-based security automation tool designed to automate the initial phase of a web security audit by combining network scanning and web vulnerability detection using **Nmap** and **Nikto**.

## Features
* **Automated Recon:** Runs Nmap for service detection and Nikto for web vulnerability scanning.
* **Easy Setup:** Includes a Bash script `requirements.sh` to handle all Linux package dependencies.
* **Automated Reporting:** Creates a local `scan_results` directory to store detailed text logs of every scan.
* **Auto-Detection:** It only launches Nikto if an active HTTP/HTTPS service is detected, saving time and system resources.

## Installation
Clone the repository on your machine:

```bash
git clone https://github.com/0xmahmoud-ali/Nmapito.git
```
Move inside the script directory:
```bash
cd Nmapito
```
Give the script executable permissions:
```bash
chmod +x requirements.sh
```
Run the requirement script to install Nmap and Nikto:

```bash
./requirements.sh
```

## Usage
Run the main script and follow the interactive prompts:
```bash
python3 nmapito.py
```
