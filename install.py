import os

choice = input('[+] To install, press (Y). To uninstall, press (N): ')

if choice.lower() == 'y':
    # Installation process
    run = os.system
    run('chmod 777 saudi-ip.py')
    run('mkdir /usr/share/saip')
    run('cp saudi-ip.py /usr/share/saip/saudi-ip.py')

    cmnd = '''#!/bin/sh 
exec python3 /usr/share/saip/saudi-ip.py "$@"
'''
    with open('/usr/bin/saip', 'w') as file:
        file.write(cmnd)
    
    run('chmod +x /usr/bin/saip')
    run('chmod +x /usr/share/saip/saudi-ip.py')

    print('''\n\nCongratulations! Saudi IP Tool has been installed successfully. 
You can now use 'saip' command in the terminal.''')
elif choice.lower() == 'n':
    # Uninstallation process
    run = os.system
    run('rm -r /usr/share/saip ')
    run('rm /usr/bin/saip ')
    print('[!] Saudi IP Tool has been removed successfully.')
else:
    print("Invalid choice. Please enter 'Y' to install or 'N' to uninstall.")
