import requests
import time
import subprocess
import logging

# Logging configuration
logging.basicConfig(filename='tor_ip_changer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_installation(package_name):
    try:
        subprocess.check_output(['dpkg', '-s', package_name])
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package_name):
    logging.info(f"Installing {package_name}...")
    subprocess.call(['sudo', 'apt-get', 'update'])
    subprocess.call(['sudo', 'apt-get', 'install', '-y', package_name])

def get_external_ip():
    url = 'https://www.myexternalip.com/raw'
    try:
        response = requests.get(url, proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error retrieving external IP: {e}")
        return None

def change_ip():
    try:
        subprocess.call(['sudo', 'service', 'tor', 'reload'])
        new_ip = get_external_ip()
        if new_ip:
            print('[+] Your IP has been changed to:', new_ip)
            logging.info(f"IP changed to {new_ip}")
    except Exception as e:
        logging.error(f"Error changing IP: {e}")

def main():
    try:
        print('''\033[1;32;40m \n Saudi-Ip''')
        print("\033[1;40;31m Made by port22ssh AKA Talal . \n")

        if not check_installation('python3-pip'):
            print('[+] pip3 is not installed')
            install_package('python3-pip')
            print('[!] pip3 installed successfully')

        if not check_installation('tor'):
            print('[+] Tor is not installed !')
            install_package('tor')
            print('[!] Tor installed successfully')

        print('Starting Tor service...')
        subprocess.call(['sudo', 'service', 'tor', 'start'])
        time.sleep(3)

        print("\033[1;32;40m Change your SOCKS to 127.0.0.1:9050 \n")

        time_interval = input("[+] Time to change IP in seconds [type=60] >> ")
        change_count = input("[+] How many times do you want to change your IP [type=1000] For infinite IP change type [0] >> ")

        time_interval = int(time_interval)
        change_count = int(change_count)

        if change_count == 0:
            try:
                while True:
                    time.sleep(time_interval)
                    change_ip()
            except KeyboardInterrupt:
                print('\nTor IP changer stopped.')
        else:
            for _ in range(change_count):
                time.sleep(time_interval)
                change_ip()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print('An error occurred. Please check the log file for details.')

if __name__ == '__main__':
    main()
