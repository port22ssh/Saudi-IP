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
            print('\033[1;2mYour new IP is:\033[0m', new_ip)  # Adjusted brightness
            logging.info(f"IP changed to {new_ip}")
    except Exception as e:
        logging.error(f"Error changing IP: {e}")

def main():
    try:
        print('\033[1;2mMade in Saudi Arabia By Saudi Hands\033[0m\n')  # Adjusted brightness

        print("\033[1;2mProgrammed by port22ssh AKA Talal.\033[0m\n")  # Adjusted brightness

        print("\033[1;31mWARNING: Usage of this tool for illegal activities is strictly prohibited. The author is not responsible for any misuse of this tool.\033[0m\n")  # Adjusted brightness

        print("How This Tool Works:\n")
        print("Start Tor Service: The tool initiates the Tor service to anonymize internet traffic.\n")
        print("Retrieve IP Address: It fetches the external IP address through Tor from an external service.\n")
        print("Change IP Address: The tool reloads Tor to obtain a new IP address, ensuring anonymity.\n")
        print("User Interaction: Users set their SOCKS proxy and specify the frequency and number of IP changes.\n")
        print("Error Handling: Errors are logged for troubleshooting purposes.\n")
        
        print("Go to firefox or the browser you use and put the SOCKS proxy settings to 127.0.0.1:9050\n")

        if not check_installation('python3-pip'):
            print('\033[1;2m pip3 is not installed\033[0m')  # Adjusted brightness
            install_package('python3-pip')
            print('\033[1;2m pip3 installed successfully\033[0m')  # Adjusted brightness

        if not check_installation('tor'):
            print('\033[1;2m Tor is not installed !\033[0m')  # Adjusted brightness
            install_package('tor')
            print('\033[1;2m Tor installed successfully\033[0m')  # Adjusted brightness

        print('\033[1;2m Booting Tor Up\033[0m\n')  # Adjusted brightness
        subprocess.call(['sudo', 'service', 'tor', 'start'])
        time.sleep(3)

        print("\033[1;2m Change your SOCKS to 127.0.0.1:9050\033[0m\n")  # Adjusted brightness

        time_interval = input("\033[1;2m Time to change IP in seconds put=60 -->\033[0m ")
        change_count = input("\033[1;2m How many times do you want to change your IP [type=1000] For infinite IP change type 0 -->\033[0m ")

        time_interval = int(time_interval)
        change_count = int(change_count)

        if change_count == 0:
            try:
                while True:
                    time.sleep(time_interval)
                    change_ip()
            except KeyboardInterrupt:
                print('\n\033[1;2m Tool Stopped.\033[0m')  # Adjusted brightness
        else:
            for _ in range(change_count):
                time.sleep(time_interval)
                change_ip()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print('\033[1;2m An error occurred. Please check the log file for details.\033[0m')  # Adjusted brightness

if __name__ == '__main__':
    main()
